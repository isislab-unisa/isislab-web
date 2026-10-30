#!/usr/bin/env python3
"""Create missing local full-size clipping pages from discovered press media."""
from pathlib import Path
import re,unicodedata,yaml
ROOT=Path(__file__).resolve().parents[1]

def slug(value):
    value=unicodedata.normalize('NFKD',str(value)).encode('ascii','ignore').decode().lower()
    return re.sub('-+','-',re.sub('[^a-z0-9]+','-',value)).strip('-')[:74]

def main():
    path=ROOT/'_data/press.yml'
    items=yaml.safe_load(path.read_text(encoding='utf8')) or []
    for item in items:
        item.setdefault('slug',slug(item.get('publication','Press')+'-'+str(item.get('date',''))) or 'press')
        for lang in ('it','en'):
            dest=ROOT/'press-articles'/f'{lang}-{item["slug"]}.md'
            if dest.exists():continue
            permalink=('/en/' if lang=='en' else '/')+'rassegna-stampa/'+item['slug']+'/'
            other=('/en/' if lang=='it' else '/')+'rassegna-stampa/'+item['slug']+'/'
            meta=dict(layout='press-article',lang=lang,alt_url=other,title=item.get('publication','ISISLab press'),
                      description=item.get('title',''),section=('Press' if lang=='en' else 'Rassegna stampa'),
                      date=str(item.get('date','')),publication=item.get('publication',''),
                      press_image=item.get('image',''),permalink=permalink)
            if item.get('pdf'):meta['press_pdf']=item['pdf']
            dest.parent.mkdir(exist_ok=True,parents=True)
            dest.write_text('---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False)+'---\n\n'+str(item.get('title',''))+'\n',encoding='utf8')
    path.write_text(yaml.safe_dump(items,allow_unicode=True,sort_keys=False),encoding='utf8')
    print(f'Press detail pages indexed for {len(items)} clippings in IT/EN')
if __name__=='__main__':main()
