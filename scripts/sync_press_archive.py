#!/usr/bin/env python3
"""Discover original press clippings from the complete WordPress press page.

Preserves the curated historical entries and adds clippings omitted from the
initial Jekyll data file. The local HTML or WordPress export option works when
remote network/DNS is blocked. Only original uploads media is accepted.
"""
from __future__ import annotations
import argparse, hashlib, re
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import requests, yaml
from bs4 import BeautifulSoup
from download_editorial_images import ROOT, DATA, source_url, write_yaml

URL='https://www.isislab.it/rassegna-stampa/'

def image_url(img):
    for attr in ('data-full-url','data-large-file','data-orig-file','data-src','src'):
        value=img.get(attr,'')
        if value and not value.startswith('data:'):
            url=source_url(urljoin(URL,value))
            if url and '/wp-content/uploads/' in urlparse(url).path:return url
    return ''

def original_identifier(url):
    path=unquote(urlparse(url).path)
    path=re.sub(r'-(?:\d{2,5}x\d{2,5}|scaled|rotated)(?=\.[^.]+$)','',path,flags=re.I)
    return path.casefold()

def discover(html):
    soup=BeautifulSoup(html,'html.parser')
    root=soup.select_one('.entry-content, .wp-block-post-content, article, main') or soup
    cards=[]
    for img in root.select('figure img, .wp-block-image img, .wp-block-gallery img, .entry-content img, main img'):
        url=image_url(img)
        if not url:continue
        figure=img.find_parent('figure')
        caption=figure.find('figcaption') if figure else None
        context=(caption.get_text(' ',strip=True) if caption else '') or img.get('alt','').strip()
        if not context:
            prev=figure.find_previous_sibling(['p','h3','h4']) if figure else None
            if prev:context=prev.get_text(' ',strip=True)
        context=re.sub(r'\s+',' ',context).strip()
        date=re.search(r'\b(?:19|20)\d{2}[-/.]\d{1,2}(?:[-/.]\d{1,2})?\b',context)
        cards.append({'image':url,'publication':context[:160] if context else 'ISISLab — Rassegna stampa',
                      'title':context[:200] if context else 'Ritaglio stampa originale',
                      'date':date.group(0) if date else ''})
    # Preserve appearance order; ignore WP duplicate responsive image occurrences.
    unique={}
    for card in cards:unique.setdefault(original_identifier(card['image']),card)
    return list(unique.values())

def merge(entries,cards):
    present={original_identifier(p['image']) for p in entries if p.get('image')}
    new=[]
    for item in cards:
        if original_identifier(item['image']) in present:continue
        item['slug']='press-'+hashlib.sha256(item['image'].encode()).hexdigest()[:14]
        entries.append(item);new.append(item)
        present.add(original_identifier(item['image']))
    return new

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--html',type=Path,help='Use saved HTML from WordPress (fully offline)')
    ap.add_argument('--timeout',type=int,default=18)
    opt=ap.parse_args()
    if opt.html:html=opt.html.read_text(encoding='utf8')
    else:
        r=requests.get(URL,headers={'User-Agent':'Mozilla/5.0 ISISLab site backup'},timeout=opt.timeout)
        r.raise_for_status();html=r.text
    path=DATA/'press.yml'
    entries=yaml.safe_load(path.read_text(encoding='utf8')) or []
    cards=discover(html)
    added=merge(entries,cards)
    write_yaml(path,entries)
    print(f'Press page contained {len(cards)} image entries; {len(added)} newly discovered; {len(entries)} total in archive')
    from refresh_press_details import main as press_details
    from refresh_archives import main as refresh
    press_details();refresh()
if __name__=='__main__':main()
