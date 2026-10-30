#!/usr/bin/env python3
"""Import original WordPress uploads from a local export into the Jekyll tree.

Example: python scripts/import_media_directory.py /path/to/wp-content/uploads
This is useful if the public media server is unreachable but you have an export.
Only maps filenames with an unambiguous matching original URL.
"""
import argparse, hashlib, shutil
from pathlib import Path
from urllib.parse import unquote,urlparse
import yaml
ROOT=Path(__file__).resolve().parents[1]

def sources():
    found=set()
    for filename in ('press.yml','media.yml','news.yml'):
        data=yaml.safe_load((ROOT/'_data'/filename).read_text(encoding='utf8')) or []
        for entry in data:
            for key in ('image','pdf','feature_source_image'):
                value=entry.get(key)
                if isinstance(value,str) and 'isislab.it' in value:found.add(value)
    for dirname in ('articles','press-articles'):
        for p in (ROOT/dirname).glob('*.md'):
            content=p.read_text(encoding='utf8')
            if content.startswith('---'):
                header=content.split('---',2)
                if len(header)==3:
                    meta=yaml.safe_load(header[1]) or {}
                    for key in ('feature_source_image','press_image','press_pdf'):
                        value=meta.get(key)
                        if isinstance(value,str) and 'isislab.it' in value:found.add(value)
    return sorted(found)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('uploads',type=Path,help='Local uploads folder exported from WordPress')
    args=ap.parse_args()
    folder=args.uploads.expanduser().resolve()
    if not folder.is_dir():ap.error('Folder does not exist')
    mapping=yaml.safe_load((ROOT/'_data/media_local.yml').read_text()) or {}
    target=ROOT/'assets/media';target.mkdir(parents=True,exist_ok=True)
    matched=[];missing=[]
    for url in sources():
        remote=unquote(urlparse(url).path)
        if '/wp-content/uploads/' not in remote:continue
        sub=remote.split('/wp-content/uploads/',1)[1].lstrip('/')
        candidate=(folder/sub).resolve()
        if not candidate.is_relative_to(folder) or not candidate.is_file():
            missing.append(url);continue
        ext=candidate.suffix.lower()
        if ext not in ('.jpg','.jpeg','.png','.webp','.gif','.svg','.pdf','.avif','.mp4','.webm'):
            continue
        name=hashlib.sha256(url.encode()).hexdigest()[:12]+'-'+candidate.name
        dest=target/name
        if not dest.exists():shutil.copy2(candidate,dest)
        mapping[url]='/assets/media/'+name
        matched.append(url)
    (ROOT/'_data/media_local.yml').write_text(yaml.safe_dump(mapping,allow_unicode=True,sort_keys=True),encoding='utf8')
    print(f'Imported {len(matched)} referenced original files. Missing {len(missing)}.')
    for item in missing[:20]:print('MISSING:',item)

if __name__=='__main__':main()
