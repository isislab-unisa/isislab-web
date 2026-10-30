#!/usr/bin/env python3
"""Cache referenced public images locally and update _data/media_local.yml.
Images remain at their original source URLs if downloading fails. Respect original rights.
"""
from pathlib import Path
from urllib.parse import urlparse
import hashlib, argparse, requests, yaml, sys, time
ROOT=Path(__file__).resolve().parents[1]
SOURCES=['press.yml','media.yml']

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--timeout',type=int,default=22);args=parser.parse_args()
    target=ROOT/'assets/media';target.mkdir(parents=True,exist_ok=True)
    mapping=yaml.safe_load((ROOT/'_data/media_local.yml').read_text()) or {}
    urls=set()
    for fn in SOURCES:
        for entry in yaml.safe_load((ROOT/'_data'/fn).read_text()):
            for key in ('image','pdf'):
                if entry.get(key):urls.add(entry[key])
    with requests.Session() as session:
        session.headers.update({'User-Agent':'ISISLab-Jekyll-Migration/1.0 (manual asset backup)'})
        for i,url in enumerate(sorted(urls),1):
            parsed=urlparse(url)
            if parsed.hostname not in ('www.isislab.it','isislab.it'):continue
            ext=Path(parsed.path).suffix.lower();ext=ext if ext in ('.jpg','.jpeg','.png','.webp','.gif','.svg','.pdf') else '.bin'
            filename=hashlib.sha256(url.encode()).hexdigest()[:12]+'-'+Path(parsed.path).stem[:65]+ext
            dest=target/filename
            try:
                if not dest.exists():
                    r=session.get(url,timeout=args.timeout);r.raise_for_status()
                    if not (r.headers.get('Content-Type','').startswith(('image/','application/pdf')) or r.content[:4] in (b'\xff\xd8\xff\xe0',b'\x89PNG',b'%PDF')):raise ValueError('Not image/PDF')
                    dest.write_bytes(r.content)
                mapping[url]='/assets/media/'+filename
                print(f'{i}/{len(urls)} OK {filename}')
            except Exception as e:print(f'{i}/{len(urls)} UNAVAILABLE {url}: {e}',file=sys.stderr)
    (ROOT/'_data/media_local.yml').write_text(yaml.safe_dump(mapping,allow_unicode=True,sort_keys=True))
    print('Cached',len(mapping),'image(s); original URLs remain as fallback for unsuccessful downloads.')
if __name__=='__main__':main()
