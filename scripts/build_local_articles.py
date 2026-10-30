#!/usr/bin/env python3
"""Build fully local press/news detail pages from verified metadata and authored summaries.
Imported long-form WordPress copies (site-owner-only) are never overwritten.
"""
from pathlib import Path
import re, unicodedata, yaml
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'_data'
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'-+','-',re.sub('[^a-z0-9]+','-',s)).strip('-')[:74]
def text(x):return str(x or '').replace('\r','').strip()
def write(path,meta,body):
    if path.exists():return
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text('---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=120).strip()+'\n---\n\n'+body+'\n',encoding='utf-8')
news=yaml.safe_load((D/'news.yml').read_text())
for n in news:
    s=n.get('slug') or slug(n['title_en'])
    n['slug']=s
    for lang in ('it','en'):
        title=n[f'title_{lang}']; summary=n[f'summary_{lang}']
        perm=f"/{'en/' if lang=='en' else ''}news/{s}/"
        meta=dict(layout='article',article_kind='news',title=title,lang=lang,alt_url=f"/{'en/' if lang=='it' else ''}news/{s}/",date=str(n['date']),permalink=perm,section='News',description=summary)
        if n.get('image'):meta['feature_source_image']=n['image']
        body=summary+'\n\n' + ('*Scheda informativa.*' if lang=='it' else '*News overview.*')
        write(ROOT/'articles'/f'{lang}-{s}.md',meta,body)
(D/'news.yml').write_text(yaml.safe_dump(news,allow_unicode=True,sort_keys=False,width=105),encoding='utf-8')
press=yaml.safe_load((D/'press.yml').read_text())
for i,p in enumerate(press):
    s=p.get('slug') or slug(p['publication']+'-'+str(p['date']))
    p['slug']=s
    for lang in ('it','en'):
        perm=f"/{'en/' if lang=='en' else ''}rassegna-stampa/{s}/"
        metadata=dict(layout='press-article',lang=lang,alt_url=f"/{'en/' if lang=='it' else ''}rassegna-stampa/{s}/",title=p['publication'],description=p['title'],section='Press' if lang=='en' else 'Rassegna stampa',date=str(p['date']),publication=p['publication'],press_image=p['image'],permalink=perm)
        if p.get('pdf'):metadata['press_pdf']=p['pdf']
        body=p['title']
        write(ROOT/'press-articles'/f'{lang}-{s}.md',metadata,body)
(D/'press.yml').write_text(yaml.safe_dump(press,allow_unicode=True,sort_keys=False,width=105),encoding='utf-8')
print(f'Local news: {len(news)} IT + {len(news)} EN; press: {len(press)} IT + {len(press)} EN')
