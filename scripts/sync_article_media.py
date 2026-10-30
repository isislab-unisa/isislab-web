#!/usr/bin/env python3
"""Cache the featured pictures of *all* imported local news articles.

Handles WordPress posts imported from REST or WXR and original media from either
HTTP or --uploads. Generates compressed thumbnails for paginated archives while
keeping source-size images for article pages. Does not use fake replacement media.
"""
import argparse, json
from pathlib import Path
from urllib.parse import urlparse
import requests, yaml
from bs4 import BeautifulSoup
from download_editorial_images import ROOT, DATA, IMG, source_url, image_bytes, save_image, locate_local, update_frontmatter, write_yaml

def frontmatter(path):
    content=path.read_text(encoding='utf8')
    if not content.startswith('---\n'):return {},content
    parts=content.split('---',2)
    return yaml.safe_load(parts[1]) or {},parts[2]

def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--uploads',type=Path)
    cli.add_argument('--timeout',type=int,default=12)
    args=cli.parse_args()
    uploads=args.uploads.resolve() if args.uploads else None
    if uploads and not uploads.is_dir():cli.error('Uploads folder not found')
    mapping=yaml.safe_load((DATA/'media_local.yml').read_text(encoding='utf8')) or {}
    thumbs=yaml.safe_load((DATA/'media_thumbs.yml').read_text(encoding='utf8')) or {}
    pages=[]
    for directory in (ROOT/'articles',ROOT/'imported'):
        if directory.exists():
            for p in directory.rglob('*'):
                if p.suffix not in ('.md','.html'):continue
                meta,body=frontmatter(p)
                if meta.get('article_kind')=='news':pages.append((p,meta,body))
    result={'news_pages':len(pages),'news_unique_pictures':0,'news_pages_with_images':0,'missing':[]}
    unique={}
    session=requests.Session();session.headers.update({'User-Agent':'Mozilla/5.0 ISISLab authorized offline website archive'})
    for p,meta,body in pages:
        url=meta.get('feature_source_image')
        if not url:
            soup=BeautifulSoup(body,'html.parser')
            img=soup.select_one('figure img, .wp-block-image img, img')
            if img:url=img.get('data-full-url') or img.get('data-src') or img.get('src')
        # Some WXR content already uses a local /assets/media/... path.
        direct=meta.get('local_hero_image')
        local=ROOT/str(direct or '').lstrip('/')
        if local.is_file() and local.suffix.lower() in ('.jpg','.jpeg','.png','.webp','.gif'):
            raw=local.read_bytes()
            cache_key=str(direct)
        elif source_url(url):
            cache_key=url
            try:raw=image_bytes(session,url,uploads,args.timeout)
            except Exception as exc:
                result['missing'].append({'article':str(p.relative_to(ROOT)),'source':url,'error':str(exc)[:180]});continue
        else:
            result['missing'].append({'article':str(p.relative_to(ROOT)),'source':str(url or ''),'error':'No matching original image URL in WP export'});continue
        if cache_key not in unique:
            try:
                full,thumb,_,_=save_image(raw,'news',p.stem)
                unique[cache_key]=(full,thumb)
                result['news_unique_pictures']+=1
            except ValueError as exc:
                result['missing'].append({'article':str(p.relative_to(ROOT)),'error':str(exc)});continue
        full,thumb=unique[cache_key]
        update_frontmatter(p,dict(local_hero_image=full,local_thumbnail_image=thumb,feature_source_image=url) if source_url(url) else dict(local_hero_image=full,local_thumbnail_image=thumb))
        result['news_pages_with_images']+=1
        if source_url(url):mapping[url]=full;thumbs[url]=thumb
    write_yaml(DATA/'media_local.yml',mapping)
    write_yaml(DATA/'media_thumbs.yml',thumbs)
    out=ROOT/'ARTICLE_IMAGE_REPORT.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    print(f'News picture sync: {result["news_pages_with_images"]}/{len(pages)} article pages assigned original photos; {result["news_unique_pictures"]} unique images')
    return 0 if not result['missing'] else 2
if __name__=='__main__':raise SystemExit(main())
