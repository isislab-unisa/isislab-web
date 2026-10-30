#!/usr/bin/env python3
"""Fetch VERIFIED featured images for known ISISLab news posts.

Uses the original WordPress REST API (_embed) and conservatively matches by
original article URL or dated, similar title. Downloads image bytes locally and
updates both the listing YAML and the existing IT/EN article front matter.
Never assigns a photo to a post on ambiguous matches.
"""
import difflib
import re
from pathlib import Path
from urllib.parse import urlparse
import requests
import yaml
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
NEWS=ROOT/'_data/news.yml'
LOCAL=ROOT/'_data/media_local.yml'
HOST='https://www.isislab.it'

def normalize(s):
    s=BeautifulSoup(s or '', 'html.parser').get_text(' ',strip=True).casefold()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

def wordpress_posts(session):
    found=[]
    for page in range(1,1000):
        response=session.get(HOST+'/wp-json/wp/v2/posts',params={'per_page':100,'page':page,'_embed':1},timeout=25)
        if page>1 and response.status_code in (400,404):break
        response.raise_for_status()
        batch=response.json()
        if not isinstance(batch,list):raise ValueError('WordPress REST returned unexpected response')
        found+=batch
        if len(batch)<100:break
    return found

def choose(item,posts):
    original=item.get('url','')
    if original and '/news/' not in urlparse(original).path:
        matches=[p for p in posts if p.get('link','').rstrip('/')==original.rstrip('/')]
        if len(matches)==1:return matches[0]
    title=normalize(item.get('title_it'))
    date=str(item.get('date',''))[:10]
    graded=[]
    for p in posts:
        if str(p.get('date',''))[:10]!=date:continue
        candidate=normalize(p.get('title',{}).get('rendered',''))
        graded.append((difflib.SequenceMatcher(None,title,candidate).ratio(),p))
    graded.sort(key=lambda t:t[0],reverse=True)
    if graded and graded[0][0]>=.67 and (len(graded)==1 or graded[0][0]-graded[1][0]>=.12):return graded[0][1]
    return None

def main():
    from import_wordpress import cached_media
    news=yaml.safe_load(NEWS.read_text(encoding='utf8'))
    mapping=yaml.safe_load(LOCAL.read_text(encoding='utf8')) or {}
    errors=[];match_count=0;media_count=0
    with requests.Session() as session:
        session.headers['User-Agent']='ISISLab authorized migration; original news media sync'
        try:posts=wordpress_posts(session)
        except requests.RequestException as ex:
            print('Source WordPress API unavailable. Nothing changed:',ex)
            return 2
        print(f'Found {len(posts)} WordPress posts')
        for item in news:
            post=choose(item,posts)
            if not post:
                print('UNMATCHED:',item['title_it']);continue
            match_count+=1
            feature=(post.get('_embedded',{}).get('wp:featuredmedia',[]) or [{}])[0].get('source_url')
            if not feature:
                soup=BeautifulSoup(post.get('content',{}).get('rendered',''),'html.parser')
                el=soup.select_one('figure img, .wp-block-image img, img')
                if el:feature=el.get('data-src') or el.get('src')
            if not feature:
                print('NO IMAGE:',item['title_it']);continue
            local=cached_media(session,feature,errors)
            if not local:
                print('DOWNLOAD FAILED:',item['title_it']);continue
            media_count+=1
            item['image']=feature
            mapping[feature]=local
            for lang in ('it','en'):
                path=ROOT/'articles'/f"{lang}-{item['slug']}.md"
                if not path.exists():continue
                source=path.read_text(encoding='utf8')
                pieces=source.split('---',2)
                if len(pieces)!=3:continue
                data=yaml.safe_load(pieces[1])
                data['feature_source_image']=feature
                data['local_hero_image']=local
                path.write_text('---\n'+yaml.safe_dump(data,allow_unicode=True,sort_keys=False)+'---'+pieces[2],encoding='utf8')
            print('CACHED:',item['title_it'],local)
    NEWS.write_text(yaml.safe_dump(news,allow_unicode=True,sort_keys=False,width=100),encoding='utf8')
    LOCAL.write_text(yaml.safe_dump(mapping,allow_unicode=True,sort_keys=True),encoding='utf8')
    print(f'Matched {match_count}/{len(news)} metadata entries; saved {media_count} originals; errors {len(errors)}')
    for e in errors[:30]:print('ERROR:',e)
    return 0 if media_count else 2

if __name__=='__main__':raise SystemExit(main())
