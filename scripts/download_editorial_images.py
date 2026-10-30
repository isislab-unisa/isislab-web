#!/usr/bin/env python3
"""Download ORIGINAL ISISLab news/press images into assets/img/news and assets/img/press.

Usage:
  python3 scripts/download_editorial_images.py
  python3 scripts/download_editorial_images.py --uploads /path/to/wp-content/uploads

Only images verified as actual images are saved. News media is matched to the
WordPress post by exact article permalink or uniquely matching date/title.
Failures are recorded in MEDIA_DOWNLOAD_REPORT.json (never silently substituted).
"""
from __future__ import annotations
import argparse
import difflib
import hashlib
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, unquote, urlparse

import requests
import yaml
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://www.isislab.it'
DATA = ROOT / '_data'
IMG = ROOT / 'assets' / 'img'
ALLOWED = {'www.isislab.it','isislab.it'}
MAX_IMAGE_BYTES = 35 * 1024 * 1024
HEADERS = {'User-Agent':'Mozilla/5.0 (compatible; ISISLabJekyllImageBackup/1.0)'}


def norm(value):
    text = BeautifulSoup(str(value or ''), 'html.parser').get_text(' ', strip=True)
    return re.sub(r'[^a-z0-9]+', ' ', text.casefold()).strip()


def source_url(url):
    url = str(url or '').strip()
    if url.startswith('//'): url = 'https:' + url
    if url.startswith('/'): url = urljoin(SOURCE, url)
    if not url.startswith(('http://','https://')): return ''
    parsed=urlparse(url)
    return url if parsed.hostname in ALLOWED else ''


def read_yaml(path, fallback):
    if path.exists(): return yaml.safe_load(path.read_text(encoding='utf8')) or fallback
    return fallback


def write_yaml(path, obj):
    path.write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True,width=115),encoding='utf8')


def online_posts(session, timeout):
    posts=[]
    for page in range(1,50):
        res=session.get(SOURCE + '/wp-json/wp/v2/posts',params={'per_page':100,'page':page,'_embed':1},timeout=timeout)
        if page>1 and res.status_code in (400,404):break
        res.raise_for_status()
        batch=res.json()
        if not isinstance(batch,list):raise ValueError('Unexpected WordPress REST response')
        posts.extend(batch)
        if len(batch)<100:break
    return posts


def match_post(item,posts):
    original = item.get('url','').rstrip('/')
    if original and '/news' not in urlparse(original).path:
        exact=[p for p in posts if p.get('link','').rstrip('/') == original]
        if len(exact)==1:return exact[0]
    date=str(item.get('date',''))[:10]
    name=norm(item.get('title_it'))
    choices=[]
    for p in posts:
        if str(p.get('date',''))[:10] != date:continue
        candidate=norm(p.get('title',{}).get('rendered',''))
        score=difflib.SequenceMatcher(None,name,candidate).ratio()
        choices.append((score,p))
    choices.sort(key=lambda t:t[0],reverse=True)
    if choices and choices[0][0] >= .68 and (len(choices)==1 or choices[0][0]-choices[1][0]>=.12):
        return choices[0][1]
    return None


def archive_links(session, timeout):
    """Crawl WordPress archive pagination in either language without guessing page URLs.

    WP themes can use page/2/ or dynamically named ?paged12345=2; links in
    actual pagination are authoritative. Only follow archive pagination links.
    """
    from collections import deque
    queue=deque([SOURCE+'/news/', SOURCE+'/en/isislab-news/'])
    visited=set();links={}
    while queue and len(visited)<100:
        page=queue.popleft()
        if page in visited:continue
        visited.add(page)
        try:
            r=session.get(page,timeout=timeout)
            if r.status_code in (404,410):continue
            r.raise_for_status()
        except requests.RequestException:
            if len(visited)==1:raise
            continue
        soup=BeautifulSoup(r.text,'html.parser')
        for a in soup.select('article h1 a, article h2 a, article h3 a, h2.wp-block-post-title a, h3.wp-block-post-title a, .entry-title a, a[rel=bookmark]'):
            target=source_url(urljoin(page,a.get('href') or ''))
            title=a.get_text(' ',strip=True)
            if target and title and target not in visited and target.rstrip('/') not in (SOURCE+'/news', SOURCE+'/en/isislab-news'):
                if re.search(r'/\d{4}/\d{1,2}/',urlparse(target).path):links[target]=title
        for a in soup.select('.page-numbers a, a.page-numbers, .wp-block-query-pagination a, nav.pagination a, .pagination a, a.next, a[rel=next]'):
            target=source_url(urljoin(page,a.get('href') or ''))
            if not target or target in visited:continue
            parsed=urlparse(target)
            if parsed.path.startswith(('/news/','/en/isislab-news/')) and len(queue)<100:
                queue.append(target)
    return links

def match_archive_article(item,links):
    wanted=norm(item.get('title_it',''))
    choices=sorted([(difflib.SequenceMatcher(None,wanted,norm(title)).ratio(),url) for url,title in links.items()],reverse=True)
    if choices and choices[0][0]>=.72 and (len(choices)==1 or choices[0][0]-choices[1][0]>=.12):return choices[0][1]
    return ''


def extract_picture_from_post(p):
    featured=(p.get('_embedded',{}).get('wp:featuredmedia',[]) or [{}])[0]
    url=featured.get('source_url')
    if source_url(url):return source_url(url)
    soup=BeautifulSoup(p.get('content',{}).get('rendered',''), 'html.parser')
    for img in soup.select('figure img, .wp-block-image img, img'):
        url=img.get('data-src') or img.get('src')
        if source_url(url):return source_url(url)
    return ''


def webpage_picture(session, url, timeout):
    if not source_url(url):return ''
    res=session.get(url,timeout=timeout)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'html.parser')
    for prop, attr in [('og:image','property'),('twitter:image','name')]:
        tag=soup.find('meta',attrs={attr:prop})
        if tag and source_url(tag.get('content')):return source_url(tag['content'])
    for img in soup.select('article figure img, article .wp-block-image img, main article img'):
        url=img.get('data-src') or img.get('src')
        if source_url(url):return source_url(url)
    return ''


def locate_local(url, uploads):
    """Resolve original/WordPress thumbnail variants from an offline uploads export.

    WXR frequently references `photo-300x200.jpg` although the uploads export only
    contains `photo.jpg` or `photo-scaled.jpg`. Never search across other date folders
    or match unrelated people/images by vague filename similarity.
    """
    if not uploads or not source_url(url): return None
    path=unquote(urlparse(url).path)
    if '/wp-content/uploads/' not in path:return None
    relative=path.split('/wp-content/uploads/',1)[1]
    target=(uploads/relative).resolve()
    if not target.is_relative_to(uploads): return None
    if target.is_file():return target
    folder=target.parent
    if not folder.is_dir():return None
    name=target.name
    base=re.sub(r'-(?:\d{2,5}x\d{2,5}|scaled|rotated)(?=\.[^.]+$)','',name,flags=re.I)
    stem=Path(base).stem
    # In priority order: original image, WP scaled original, alternate format.
    choices=[folder/base,folder/(stem+'-scaled'+Path(base).suffix),folder/(stem+'-rotated'+Path(base).suffix)]
    for ext in ('.jpg','.jpeg','.png','.webp'):
        choices.extend((folder/(stem+ext),folder/(stem+'-scaled'+ext)))
    for choice in choices:
        if choice.is_file() and choice.resolve().is_relative_to(uploads):return choice
    return None

def image_bytes(session, url, uploads, timeout):
    local=locate_local(url, uploads)
    if local:
        if local.stat().st_size > MAX_IMAGE_BYTES:raise ValueError('image exceeds size limit')
        return local.read_bytes()
    if uploads:raise FileNotFoundError('image not found in supplied WordPress uploads')
    if not source_url(url):raise ValueError('unexpected image host')
    resp=session.get(url,timeout=timeout,stream=True)
    resp.raise_for_status()
    blob=bytearray()
    for chunk in resp.iter_content(128*1024):
        blob.extend(chunk)
        if len(blob)>MAX_IMAGE_BYTES:raise ValueError('image exceeds size limit')
    return bytes(blob)


def save_image(raw, folder, slug):
    try:
        image=Image.open(io.BytesIO(raw))
        image.verify()
        image=Image.open(io.BytesIO(raw))
        fmt=(image.format or 'PNG').upper()
        image=ImageOps.exif_transpose(image)
    except (UnidentifiedImageError, OSError, ValueError) as exc:
        raise ValueError(f'server did not return a valid raster image: {exc}')
    if image.width < 30 or image.height < 30:raise ValueError('image is suspiciously small')
    if image.width*image.height>140_000_000:raise ValueError('image dimensions exceed limit')
    ext='.jpg' if fmt in ('JPEG','JPG') else '.png' if fmt=='PNG' else '.webp' if fmt=='WEBP' else '.gif' if fmt=='GIF' else '.jpg'
    path=IMG/folder
    path.mkdir(parents=True,exist_ok=True)
    filename=re.sub('[^a-z0-9-]+','-',slug.casefold()).strip('-') or hashlib.sha256(raw).hexdigest()[:12]
    original=path/(filename+ext)
    if not original.exists() or original.read_bytes()!=raw:original.write_bytes(raw)
    thumb=path/(filename+'-thumb.webp')
    resized=image.copy()
    if resized.mode not in ('RGB','RGBA'):resized=resized.convert('RGBA' if 'transparency' in resized.info else 'RGB')
    resized.thumbnail((560,420),Image.Resampling.LANCZOS)
    resized.save(thumb,'WEBP',quality=83,method=5)
    return ('/'+original.relative_to(ROOT).as_posix(),'/'+thumb.relative_to(ROOT).as_posix(),image.width,image.height)


def update_frontmatter(path,meta):
    if not path.exists():return
    content=path.read_text(encoding='utf8')
    blocks=content.split('---',2)
    if len(blocks)<3:return
    front=yaml.safe_load(blocks[1]) or {}
    front.update(meta)
    path.write_text('---\n'+yaml.safe_dump(front,allow_unicode=True,sort_keys=False).rstrip()+'\n---'+blocks[2],encoding='utf8')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--uploads',type=Path,help='Use an already exported wp-content/uploads folder instead of HTTP downloads')
    parser.add_argument('--timeout',type=int,default=12,help='HTTP timeout per request')
    options=parser.parse_args()
    uploads=options.uploads.resolve() if options.uploads else None
    if uploads and not uploads.is_dir():parser.error('--uploads must be an existing directory')
    press=read_yaml(DATA/'press.yml',[])
    news=read_yaml(DATA/'news.yml',[])
    media=read_yaml(DATA/'media_local.yml',{})
    thumbnails=read_yaml(DATA/'media_thumbs.yml',{})
    report={'generated_at':datetime.now(timezone.utc).isoformat(),'press_total':len(press),'news_total':len(news),'downloaded_press':0,'downloaded_news':0,'existing_local':0,'unavailable':[], 'files':[]}
    with requests.Session() as session:
        session.headers.update(HEADERS)
        posts=[]
        archives={}
        if not uploads:
            try:
                posts=online_posts(session, options.timeout)
                print(f'WordPress post index: {len(posts)} posts')
            except (requests.RequestException,ValueError) as exc:
                print(f'WordPress API unavailable ({str(exc)[:140]}). Trying public news archive.',file=sys.stderr)
                try:
                    archives=archive_links(session,options.timeout)
                    print(f'Public news archive: {len(archives)} links')
                except requests.RequestException as e:
                    print('Public news archive not reachable:',str(e)[:120],file=sys.stderr)
        else:print('Working from WordPress uploads directory:',uploads)

        def import_item(item,kind,url):
            if not source_url(url):
                report['unavailable'].append({'type':kind,'slug':item.get('slug'),'reason':'no verified source image URL'})
                return
            if url in media and (ROOT/media[url].lstrip('/')).is_file():
                # Previous site versions cached images under assets/media. Move them
                # into the requested assets/img/<kind> tree and create thumbnails.
                try:
                    old=(ROOT/media[url].lstrip('/'))
                    original,thumb,w,h=save_image(old.read_bytes(),kind,item['slug'])
                    media[url]=original
                    thumbnails[url]=thumb
                    report['existing_local']+=1
                    report['files'].append({'type':kind,'slug':item['slug'],'source':url,'image':original,'thumbnail':thumb,'width':w,'height':h,'from_cache':True})
                    print('IMPORTED EXISTING ASSET',kind,item.get('slug'),original)
                    return
                except (OSError,ValueError) as exc:
                    print('Existing asset invalid, trying source:',exc,file=sys.stderr)
            try:
                original,thumb,w,h=save_image(image_bytes(session,url,uploads,options.timeout),kind,item['slug'])
                media[url]=original
                thumbnails[url]=thumb
                report['downloaded_'+kind]+=1
                report['files'].append({'type':kind,'slug':item['slug'],'source':url,'image':original,'thumbnail':thumb,'width':w,'height':h})
                print('DOWNLOADED',kind,item.get('slug'),original)
            except (requests.RequestException,OSError,ValueError) as exc:
                report['unavailable'].append({'type':kind,'slug':item.get('slug'),'url':url,'reason':str(exc)[:240]})
                print('UNAVAILABLE',kind,item.get('slug'),str(exc)[:100],file=sys.stderr)

        for p in press:
            import_item(p,'press',p.get('image',''))
        for n in news:
            # A known media source URL has highest priority; other sources are matched cautiously.
            url=source_url(n.get('image',''))
            post=match_post(n,posts)
            if not url and post:
                url=extract_picture_from_post(post)
            if not url and not uploads:
                page=n.get('url','')
                if not page or '/news/' in urlparse(page).path:
                    page=match_archive_article(n,archives)
                if source_url(page) and '/news/' not in urlparse(page).path:
                    try:url=webpage_picture(session,page,options.timeout)
                    except requests.RequestException:pass
            if url:
                n['image']=url
                import_item(n,'news',url)
                if url in media and (ROOT/media[url].lstrip('/')).exists():
                    for lang in ('it','en'):
                        update_frontmatter(ROOT/'articles'/f"{lang}-{n['slug']}.md",{'feature_source_image':url,'local_hero_image':media[url],'local_thumbnail_image':thumbnails[url]})
            else:
                report['unavailable'].append({'type':'news','slug':n.get('slug'),'reason':'featured image URL not found/verified'})
                print('NO MATCHING FEATURED IMAGE',n.get('slug'),file=sys.stderr)

    write_yaml(DATA/'media_local.yml',media)
    write_yaml(DATA/'media_thumbs.yml',thumbnails)
    write_yaml(DATA/'news.yml',news)
    (ROOT/'MEDIA_DOWNLOAD_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print('FINISHED',report['downloaded_press'],'press images,',report['downloaded_news'],'news images,',report['existing_local'],'already cached;',len(report['unavailable']),'unavailable')
    return 0 if not report['unavailable'] else 2

if __name__=='__main__':raise SystemExit(main())
