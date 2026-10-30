#!/usr/bin/env python3
"""Hide curated summaries from archive after importing verified original posts.

Summary article pages remain accessible at their preexisting links, but they do
not appear twice in paginated news archives.
"""
from pathlib import Path
import re,difflib,unicodedata,yaml
ROOT=Path(__file__).resolve().parents[1]

def fm(p):
    text=p.read_text(encoding='utf8')
    if not text.startswith('---\n'):return None
    return yaml.safe_load(text.split('---',2)[1]) or {}

def normalized(t):
    s=unicodedata.normalize('NFKD',str(t)).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

def main():
    folder=ROOT/'articles'
    if not folder.is_dir():return
    docs=[(p,fm(p)) for p in folder.glob('*') if p.suffix in ('.md','.html')]
    imports=[m for p,m in docs if m and m.get('import_origin')=='wordpress' and m.get('article_kind')=='news']
    hidden=0
    for p,m in docs:
        if not m or m.get('import_origin')=='wordpress' or m.get('article_kind')!='news':continue
        options=[]
        for imported in imports:
            if imported.get('lang')!=m.get('lang') or str(imported.get('date'))[:10]!=str(m.get('date'))[:10]:continue
            score=difflib.SequenceMatcher(None,normalized(imported.get('title')),normalized(m.get('title'))).ratio()
            if score>=.73:options.append(score)
        if not options:continue
        if m.get('archive_hidden'):continue
        m['archive_hidden']=True
        content=p.read_text(encoding='utf8').split('---',2)[2]
        p.write_text('---\n'+yaml.safe_dump(m,allow_unicode=True,sort_keys=False).strip()+'\n---'+content,encoding='utf8')
        hidden+=1
    print(f'Hidden {hidden} duplicate editorial summaries from news pagination')
if __name__=='__main__':main()
