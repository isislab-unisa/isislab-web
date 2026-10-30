#!/usr/bin/env python3
"""Audit local Jekyll migration completeness without claiming source parity.

Shows what is *actually bundled*. Original WordPress totals cannot be certified
until a complete export/import succeeds and is compared with its source totals.
"""
from pathlib import Path
from collections import defaultdict
import json,yaml
ROOT=Path(__file__).resolve().parents[1]

def matter(path):
    txt=path.read_text(encoding='utf8')
    if not txt.startswith('---\n'):return {}
    try:return yaml.safe_load(txt.split('---',2)[1]) or {}
    except Exception:return {}

def main():
    records=[]
    for dirname in ('articles','press-articles','imported','archive-generated','pages','en'):
        root=ROOT/dirname
        if not root.exists():continue
        for f in root.rglob('*'):
            if f.is_file() and f.suffix in ('.html','.md'):
                m=matter(f)
                if m:records.append((f,m))
    urls=defaultdict(list)
    for p,m in records:
        if m.get('permalink'):urls[m['permalink']].append(str(p.relative_to(ROOT)))
    clashes={x:y for x,y in urls.items() if len(y)>1}
    articles=[(p,m) for p,m in records if m.get('article_kind')=='news' and not m.get('archive_hidden')]
    press=yaml.safe_load((ROOT/'_data/press.yml').read_text(encoding='utf8')) or []
    visible_images=0; originals=[]; missing=[]
    for p,m in articles:
        loc=m.get('local_hero_image')
        if loc and (ROOT/loc.lstrip('/')).is_file():visible_images+=1;originals.append(str(loc))
        else:missing.append(str(m.get('permalink',p)))
    press_maps=yaml.safe_load((ROOT/'_data/media_local.yml').read_text(encoding='utf8')) or {}
    press_present=0
    for p in press:
        local=press_maps.get(p.get('image',''))
        if local and (ROOT/local.lstrip('/')).is_file():press_present+=1
        else:missing.append(p.get('image',''))
    output={'news_articles_all_languages':len(articles),'news_images_local_article_pages':visible_images,
            'press_items':len(press),'press_full_images_local':press_present,
            'pagination_pages_generated':len(list((ROOT/'archive-generated').glob('*.md'))),
            'duplicate_permalinks':clashes,'missing_images':missing,
            'original_wordpress_coverage_verified':False,
            'notes':'Source WordPress totals/images must be checked with a successful authorized WXR/REST import.'}
    (ROOT/'OFFLINE_AUDIT.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf8')
    print('Offline audit:',len(articles),'news article pages,',press_present,'/',len(press),'press image files,',visible_images,'/',len(articles),'news image files')
    if clashes:print('WARNING duplicate permalinks:',clashes)
    return 1 if clashes else 0
if __name__=='__main__':raise SystemExit(main())
