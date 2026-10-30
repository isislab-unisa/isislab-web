#!/usr/bin/env python3
"""Import authentic staff photos from the public ISISLab people page.

Only photos located on www.isislab.it and paired with the matching person are
accepted. No stock portraits, inferred file names or unrelated people.
Output is assets/people/* plus _data/people_photos.yml, used by both locales.

Run: python -m pip install -r scripts/requirements.txt
     python scripts/sync_people.py
"""
import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://www.isislab.it/chi-siamo/'
DEST = ROOT / 'assets' / 'people'
DATA = ROOT / '_data' / 'people_photos.yml'


def norm(value):
    return re.sub(r'[^a-z0-9]+', ' ', unicodedata.normalize('NFKD', value or '').encode('ascii', 'ignore').decode().lower()).strip()


def slug(value):
    return norm(value).replace(' ', '-')


def images_for_people(html, known):
    """Choose a portrait *before* its name in visual DOM order.

    Supports WordPress block groups, column containers and other layouts where
    the image block precedes an adjacent heading block. Rejects ambiguous runs.
    """
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.select_one('main') or soup.select_one('article') or soup.select_one('.entry-content') or soup
    for el in main.select('script, style, nav, footer, header, noscript'):
        el.decompose()
    pending = []
    people = {}
    headings = {norm(person): person for person in known}
    nodes = main.find_all(re.compile(r'^(?:img|h[1-6])$'))
    for node in nodes:
        if node.name == 'img':
            pending.append(node)
            if len(pending)>5:pending.pop(0)
            continue
        label = norm(node.get_text(' ', strip=True))
        if label in headings:
            person = headings[label]
            # Prefer alt text matching exactly; otherwise the nearest preceding
            # image only when one plausible image precedes the person heading.
            candidate = next((i for i in reversed(pending) if label in norm(i.get('alt', ''))), None)
            if candidate is None and len(pending)==1:
                # Blank/generic alt is common in WordPress; descriptive alt
                # naming a different person must never be treated as a match.
                alt = norm(pending[-1].get('alt', ''))
                if alt in ('', 'image', 'photo', 'portrait', 'immagine', 'fotografia'):
                    candidate = pending[-1]
            if candidate is not None:
                src = candidate.get('data-src') or candidate.get('data-lazy-src') or candidate.get('src') or ''
                if src.startswith('data:'):
                    src = ''
                if not src and candidate.get('srcset'):
                    src = candidate['srcset'].split(',')[0].strip().split(' ')[0]
                url = urljoin(SOURCE, src)
                parsed = urlparse(url)
                if parsed.hostname in ('www.isislab.it', 'isislab.it') and '/wp-content/uploads/' in parsed.path:
                    people[person] = url
            pending.clear()
        else:
            # Crossing a heading such as "Docenti" resets the image candidate.
            pending.clear()
    return people


def get_html(session, timeout):
    candidates = [SOURCE,
                  'https://www.isislab.it/about-us-2/']
    for url in candidates:
        try:
            res = session.get(url, timeout=timeout)
            res.raise_for_status()
            if '<img' in res.text.lower():
                print('Read original people page:', url)
                return res.text
        except requests.RequestException as ex:
            print(f'Source unavailable ({url}): {ex}', file=sys.stderr)
    # REST endpoint can expose the same page for installations with strict HTML
    # caching; never invent a portrait URL if this also fails.
    try:
        endpoint='https://www.isislab.it/wp-json/wp/v2/pages'
        res=session.get(endpoint,params={'slug':'chi-siamo'},timeout=timeout)
        res.raise_for_status()
        result=res.json()
        if isinstance(result,list) and result:
            markup=result[0].get('content',{}).get('rendered','')
            if '<img' in markup.lower():
                print('Read official WordPress API')
                return markup
    except (requests.RequestException,ValueError,TypeError,KeyError) as ex:
        print('WordPress API unavailable:',ex,file=sys.stderr)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--timeout', type=int, default=25)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    groups = yaml.safe_load((ROOT / '_data' / 'people_groups.yml').read_text(encoding='utf-8'))
    names = [n for group in groups for n in group['people']]
    existing = yaml.safe_load(DATA.read_text(encoding='utf-8')) if DATA.exists() else {}
    existing = existing or {}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Mozilla/5.0 (compatible; ISISLab-Jekyll/1.0; public photo sync)'})
    html = get_html(sess, args.timeout)
    if html is None:
        print('Could not access ISISLab. Existing photo mappings were preserved; try the sync from an internet-connected machine.')
        return 2
    found = images_for_people(html, names)
    print(f'Matched {len(found)} image(s) to {len(names)} official people.')
    if args.dry_run:
        for n,u in found.items(): print(n, u)
        return 0
    DEST.mkdir(parents=True, exist_ok=True)
    for name, url in found.items():
        key=slug(name)
        ext=Path(urlparse(url).path).suffix.lower()
        if ext not in ('.jpeg','.jpg','.png','.webp','.gif'):ext='.jpg'
        filename=f'{key}-{hashlib.sha256(url.encode()).hexdigest()[:8]}{ext}'
        target=DEST/filename
        try:
            if not target.exists():
                resp=sess.get(url, timeout=args.timeout)
                resp.raise_for_status()
                ct=resp.headers.get('content-type', '')
                if not ct.startswith('image/') or len(resp.content)<500:
                    raise ValueError(f'Not a valid portrait image: {ct}')
                target.write_bytes(resp.content)
            existing[key]={'image':f'/assets/people/{filename}', 'source':url}
            print('OK', name, filename)
        except (requests.RequestException, OSError, ValueError) as ex:
            print('Skipped', name, ex, file=sys.stderr)
    DATA.write_text(yaml.safe_dump(existing,allow_unicode=True,sort_keys=True),encoding='utf-8')
    print(f'Locally cached {len(existing)} verified portraits. Rebuild Jekyll to display them.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
