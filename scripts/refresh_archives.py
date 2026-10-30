#!/usr/bin/env python3
"""Generate Jekyll-native, static, bilingual news/press pagination (no plugins).

Run after import_wordpress.py. Scans all article front matter so imported older
posts automatically receive archive pages. Generated files can be regenerated.
"""
from pathlib import Path
import math
import yaml

ROOT = Path(__file__).resolve().parents[1]
PER_PAGE = 9
OUT = ROOT/'archive-generated'

def matter(path):
    try:
        src=path.read_text(encoding='utf8')
        if not src.startswith('---\n'): return {}
        return yaml.safe_load(src.split('---',2)[1]) or {}
    except Exception: return {}

def write_frontmatter(path, values, keep_body=True):
    previous=path.read_text(encoding='utf8') if keep_body and path.exists() else ''
    original=matter(path) if keep_body else {}
    original.update(values)
    body=previous.split('---',2)[2] if previous.startswith('---\n') else '\n'
    path.parent.mkdir(exist_ok=True,parents=True)
    path.write_text('---\n'+yaml.safe_dump(original,allow_unicode=True,sort_keys=False,width=120).strip()+'\n---'+body,encoding='utf8')

def refresh(kind, lang, total):
    pages=max(1,math.ceil(total/PER_PAGE))
    base=('/en/' if lang=='en' else '/')+kind+'/'
    other=('/en/' if lang=='it' else '/')+kind+'/'
    def nth(prefix,n):return prefix if n==1 else prefix+f'page/{n}/'
    dest=ROOT/('en' if lang=='en' else 'pages')/('news.md' if kind=='news' else 'rassegna-stampa.md')
    meta=dict(archive_page=1,archive_offset=0,archive_per_page=PER_PAGE,archive_total_pages=pages,
              archive_root=base,archive_next=nth(base,2) if pages>1 else None,archive_previous=None)
    write_frontmatter(dest,meta)
    for n in range(2,pages+1):
        out=OUT/f'{kind}-{lang}-{n}.md'
        meta=dict(layout='news' if kind=='news' else 'press', title=('News' if kind=='news' else ('Press coverage' if lang=='en' else 'Rassegna stampa')),
                  description=('Archive page '+str(n)),section='News' if kind=='news' else 'Press',lang=lang,
                  permalink=nth(base,n),alt_url=nth(other,n), archive_page=n,archive_offset=(n-1)*PER_PAGE,
                  archive_per_page=PER_PAGE,archive_total_pages=pages,archive_root=base,
                  archive_previous=nth(base,n-1),archive_next=nth(base,n+1) if n<pages else None)
        write_frontmatter(out,meta,keep_body=False)
    return pages

def main():
    OUT.mkdir(exist_ok=True)
    for p in OUT.glob('*.md'):p.unlink()
    articles=[]
    for folder in ('articles','imported'):
        directory=ROOT/folder
        if directory.exists():
            for p in directory.rglob('*'):
                if p.suffix.lower() not in ('.md','.html'):continue
                m=matter(p)
                if m.get('article_kind')=='news' and m.get('lang') in ('it','en') and not m.get('archive_hidden'):articles.append(m)
    press=yaml.safe_load((ROOT/'_data/press.yml').read_text(encoding='utf8')) or []
    counts={}
    for lang in ('it','en'):
        # Identical permalinks would be an invalid archive; fail loudly.
        urls=[m.get('permalink') for m in articles if m['lang']==lang]
        if len(urls)!=len(set(urls)):
            raise ValueError(f'Duplicate news permalinks for {lang}: {len(urls)-len(set(urls))}')
        counts[lang]={'news_items':len(urls),'news_pages':refresh('news',lang,len(urls)),
                      'press_items':len(press),'press_pages':refresh('rassegna-stampa',lang,len(press))}
    print('Archive pagination:',counts)
if __name__=='__main__':main()
