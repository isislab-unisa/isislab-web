#!/usr/bin/env python3
"""Complete-ish site-owner migration: WordPress pages, posts, images, PDF and links.

Run this only for sites whose content and media you have permission to copy.
Downloads all public WP REST pages/posts, falls back to public XML sitemaps.
The generated Jekyll pages use locally resolved links and media, never original
isislab.it URLs as navigation targets. Prints an audit report of limitations.
"""
import argparse, hashlib, html, json, mimetypes, re, sys, time, unicodedata, shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import requests, yaml
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
UPLOADS=None
SITE='https://www.isislab.it'
HOSTS={'www.isislab.it','isislab.it'}
HEADERS={'User-Agent':'ISISLab-Jekyll-Migration/2.0 (authorized website owner backup)','Accept':'application/json, text/html, application/xml;q=.8'}

def slug(value):
    value=unicodedata.normalize('NFKD',unquote(str(value or ''))).encode('ascii','ignore').decode().lower()
    return re.sub(r'-+','-',re.sub('[^a-z0-9]+','-',value)).strip('-')[:94] or 'untitled'

def language(item):
    url=item.get('link','')
    translations=item.get('lang','')
    return 'en' if '/en/' in urlparse(url).path or translations=='en' else 'it'

def endpoint(session,kind):
    records=[];total=None;api_errors=[]
    for base in (f'{SITE}/wp-json/wp/v2/{kind}',f'{SITE}/?rest_route=/wp/v2/{kind}'):
        records.clear()
        for page in range(1,10001):
            try:
                response=session.get(base,params={'page':page,'per_page':100,'_embed':1},timeout=35)
                if response.status_code in (400,404) and page>1:break
                response.raise_for_status()
                payload=response.json()
                if not isinstance(payload,list):raise ValueError('WP API returned non-list')
                if not payload:break
                records.extend(payload)
                total=int(response.headers.get('X-WP-Total',0)) or None
                print(f'  REST {kind}: page {page}, {len(records)}/{total or "?"}',flush=True)
                if len(payload)<100 or (total and len(records)>=total):break
            except Exception as e:
                api_errors.append(f'{base}: {e}')
                break
        if records:return records,total,api_errors
    return [],total,api_errors

def sitemap_entries(session,max_count=0):
    queue=[SITE+'/wp-sitemap.xml',SITE+'/sitemap_index.xml']
    seen=set();urls=[];failures=[]
    while queue and len(seen)<2500:
        address=queue.pop(0)
        if address in seen:continue
        seen.add(address)
        try:
            r=session.get(address,timeout=30);r.raise_for_status()
            root=ET.fromstring(r.content)
            found=[x.text.strip() for x in root.iter() if x.tag.endswith('loc') and x.text]
            if root.tag.endswith('sitemapindex'):
                for u in found:
                    if urlparse(u).hostname in HOSTS:queue.append(u)
            else:
                for u in found:
                    if urlparse(u).hostname in HOSTS and not '/wp-content/' in u and u not in urls:urls.append(u)
            if max_count and len(urls)>=max_count:break
        except Exception as e:failures.append(f'{address}: {e}')
    print(f'Sitemap found {len(urls)} public URLs; {len(failures)} sitemap errors')
    return urls[:max_count] if max_count else urls,failures

def cached_media(session,url,errors):
    url=urljoin(SITE,url)
    parsed=urlparse(url)
    if parsed.hostname not in HOSTS:return url
    if not parsed.path.lower().endswith(('.jpg','.jpeg','.png','.gif','.webp','.svg','.pdf','.avif','.mp4','.webm','.ogg','.mp3','.woff','.woff2')):
        return url
    ext=Path(parsed.path).suffix.lower()
    name=hashlib.sha256(url.encode()).hexdigest()[:14]+'-'+slug(Path(parsed.path).stem)[:55]+ext
    path=ROOT/'assets/media'/name
    public='/assets/media/'+name
    if path.exists() and path.stat().st_size:return public
    path.parent.mkdir(parents=True,exist_ok=True)
    # Prefer a user-provided WordPress uploads export: no network required.
    # Resolve resize suffixes (-300x200, -scaled) to their source original.
    if UPLOADS:
        from download_editorial_images import locate_local
        local=locate_local(url,UPLOADS)
        if local:
            shutil.copy2(local,path)
            return public
        errors.append(f'Missing in uploads export: {url}')
        return ''
    try:
        response=session.get(url,timeout=35,stream=True);response.raise_for_status()
        mime=response.headers.get('content-type','').lower()
        if 'text/html' in mime or 'application/json' in mime:raise ValueError(f'wrong MIME {mime}')
        with path.open('wb') as target:
            count=0
            for chunk in response.iter_content(65536):
                count+=len(chunk)
                if count>70*1024*1024:raise ValueError('media exceeds 70 MB')
                target.write(chunk)
        return public
    except Exception as e:
        path.unlink(missing_ok=True)
        errors.append(f'{url}: {e}')
        return ''

def canonical_path(e,kind):
    lang=language(e)
    raw=unquote(urlparse(e.get('link','')).path)
    name=slug(e.get('slug') or raw.rstrip('/').split('/')[-1])
    if kind=='posts':return f"/{'en/' if lang=='en' else ''}news/{name}/"
    # Keep original page URLs where possible; existing project pages are updated in-place.
    if raw in ('/','/en/'):
        return '/en/' if lang=='en' else '/'
    return f"/{'en/' if lang=='en' else ''}{name}/"

def internal_link(url, mapping, lang):
    parsed=urlparse(url)
    if parsed.hostname not in HOSTS:return url
    pure=f'{parsed.scheme}://{parsed.netloc}{parsed.path}'
    if pure in mapping:return mapping[pure]+('#'+parsed.fragment if parsed.fragment else '')
    path=unquote(parsed.path).strip('/')
    if path.startswith('wp-content/'):
        return ''  # caller downloads image/document attachments separately
    pieces=path.split('/')
    # WordPress articles normally have a YYYY/MM/DD/slug URL.
    if len(pieces)>=4 and re.fullmatch(r'20\d\d',pieces[0]) and pieces[1].isdigit():
        return f"/{'en/' if lang=='en' else ''}news/{slug(pieces[-1])}/"
    if len(pieces)>=5 and pieces[0]=='en' and re.fullmatch(r'20\d\d',pieces[1]):
        return f'/en/news/{slug(pieces[-1])}/'
    if pieces and pieces[0] in ('en','it'):pieces=pieces[1:]
    if not pieces or not pieces[0]:return '/en/' if lang=='en' else '/'
    if pieces[0] in ('category','tag','author','feed'):return '/en/blog/' if lang=='en' else '/blog/'
    return f"/{'en/' if lang=='en' else ''}{slug(pieces[-1])}/"

def clean_markup(markup,session,media,linkmap,lang,errors):
    soup=BeautifulSoup(markup or '','html.parser')
    for n in soup.select('script,style,form,nav,button,meta,link,noscript,aside,.sharedaddy,.wp-block-social-links'):
        n.decompose()
    for n in soup.find_all(True):
        for key in list(n.attrs):
            if key.startswith('on') or key in ('srcset','sizes','style') or key.startswith('data-wp-'):
                del n.attrs[key]
        if n.name in ('img','video','audio','source'):
            raw=n.get('data-full-url') or n.get('data-src') or n.get('src') or ''
            if raw and media:
                local=cached_media(session,raw,errors)
                if local:n['src']=local
                elif urlparse(urljoin(SITE,raw)).hostname in HOSTS:n['src']='/assets/img/news-placeholder.svg'
            elif raw and urlparse(urljoin(SITE,raw)).hostname in HOSTS:
                n['src']='/assets/img/news-placeholder.svg'
            n.attrs.pop('data-src',None)
        if n.name=='a' and n.has_attr('href'):
            source=urljoin(SITE,n['href'])
            parsed=urlparse(source)
            if parsed.hostname in HOSTS and parsed.path.lower().endswith(('.jpg','.jpeg','.png','.webp','.gif','.svg','.pdf')):
                if media:
                    local=cached_media(session,source,errors)
                    if local:n['href']=local
                    else:n.unwrap()
                else:n.unwrap()
            else:
                to=internal_link(source,linkmap,lang)
                if to:n['href']=to
                else:n.unwrap()
            n.attrs.pop('target',None)
        if n.name=='iframe' and urlparse(n.get('src','')).hostname in HOSTS:
            n.decompose()
    return str(soup)

def get_from_html(session,url):
    r=session.get(url,timeout=30);r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser')
    for s in soup.select('.entry-content,.wp-block-post-content,.post-content,.elementor-widget-theme-post-content'):
        content=str(s);break
    else:
        article=soup.select_one('article') or soup.select_one('main')
        content=str(article) if article else ''
    title=(soup.select_one('h1') or soup.select_one('title'))
    title=title.get_text(' ',strip=True) if title else 'Archived page'
    return {'title':{'rendered':title},'content':{'rendered':content},'link':url,'slug':urlparse(url).path.rstrip('/').split('/')[-1],'status':'publish','date':'','excerpt':{'rendered':''}}

def write_page(e,kind,session,media,links,errors,replace_pages):
    if e.get('status','publish')!='publish':return None
    lang=language(e);key=slug(e.get('slug') or urlparse(e.get('link','')).path)
    path=canonical_path(e,kind)
    if kind=='pages' and path in ('/', '/en/'):
        path='/en/lab-home-archive/' if lang=='en' else '/lab-home-archive/'
    # Preserve Jekyll pagination layouts on WordPress archive landing pages.
    protected={'news','rassegna-stampa','blog','galleria'}
    protected_archive=kind=='pages' and key in protected
    if protected_archive:
        path="/" + ("en/" if lang=='en' else "") + "wordpress-archive/" + key + "/"
    soup_title=BeautifulSoup(e.get('title',{}).get('rendered',''),'html.parser').get_text(' ',strip=True)
    summary=BeautifulSoup(e.get('excerpt',{}).get('rendered',''),'html.parser').get_text(' ',strip=True)
    fields=dict(layout='article' if kind=='posts' else 'page',lang=lang,title=soup_title or key,description=summary[:300] or soup_title,permalink=path)
    if kind=='posts':
        fields['article_kind']='news';fields['date']=str(e.get('date',''))[:10];fields['import_origin']='wordpress';fields['source_url']=e.get('link','')
        fields['section']='News'
    else:
        fields['section']='Page' if lang=='en' else 'Pagina'
        fields['article_kind']='imported_page'
    if kind=='pages' and replace_pages:
        dest=ROOT/('en' if lang=='en' else 'pages')/(key+'.md')
        if protected_archive or not dest.exists() or dest.name=='index.md':
            dest=ROOT/'imported'/(f'{lang}-{key}-source.html' if protected_archive else f'{lang}-{key}.html')
    else:dest=ROOT/('articles' if kind=='posts' else 'imported')/(f'{lang}-{key}-source.html' if protected_archive else f'{lang}-{key}.html')
    dest.parent.mkdir(exist_ok=True)
    # The imported original should replace its prior summary at the same URL.
    if kind=='posts':
        old_summary=ROOT/'articles'/f'{lang}-{key}.md'
        if old_summary.exists() and old_summary != dest:old_summary.unlink()
    extra=e.get('_embedded',{}).get('wp:featuredmedia',[])
    if extra:
        cover=extra[0].get('source_url')
        if cover:fields['feature_source_image']=cover
        if cover and media:
            cached=cached_media(session,cover,errors)
            if cached:
                fields['local_hero_image']=cached
                fields['feature_source_image']=cover
    body=clean_markup(e.get('content',{}).get('rendered',''),session,media,links,lang,errors)
    if fields.get('local_hero_image') and '<img' not in body:
        body=f'<figure><img class="article-hero-img" src="{fields["local_hero_image"]}" alt=""></figure>\n'+body
    # Markdown pages can embed HTML just as Jekyll pages do.
    out='---\n'+yaml.safe_dump(fields,allow_unicode=True,sort_keys=False,width=105).strip()+'\n---\n'+body+'\n'
    dest.write_text(out,encoding='utf-8')
    return str(dest.relative_to(ROOT))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--i-have-rights-to-migrate',action='store_true',help='Required: confirm permission to copy source text and images')
    parser.add_argument('--download-media',action='store_true',help='Download images, PDFs, video/audio attachments')
    parser.add_argument('--limit',type=int,default=0,help='Maximum articles for tests; 0 = all')
    parser.add_argument('--replace-existing-pages',action='store_true',help='Replace initial editorial page summaries with complete WordPress page bodies')
    parser.add_argument('--from-wxr',type=Path,help='Use a WordPress WXR XML export if live REST/sitemaps are inaccessible')
    parser.add_argument('--uploads',type=Path,help='Local wp-content/uploads exported alongside WordPress WXR')
    args=parser.parse_args()
    global UPLOADS
    UPLOADS=args.uploads.expanduser().resolve() if args.uploads else None
    if UPLOADS and not UPLOADS.is_dir():parser.error('--uploads must be an existing folder')
    if not args.i_have_rights_to_migrate:parser.error('Use --i-have-rights-to-migrate only if authorized to republish source content and media.')
    failures=[];api_totals={};entries=[]
    with requests.Session() as session:
        session.headers.update(HEADERS)
        if args.from_wxr:
            xml=ET.parse(args.from_wxr).getroot()
            namespaces={'content':'http://purl.org/rss/1.0/modules/content/','wp':'http://wordpress.org/export/1.2/'}
            raw_items=list(xml.findall('.//item'))
            attachments={}
            for item in raw_items:
                if item.findtext('wp:post_type',default='',namespaces=namespaces)=='attachment':
                    media_id=item.findtext('wp:post_id',default='',namespaces=namespaces)
                    url=item.findtext('wp:attachment_url',default='',namespaces=namespaces)
                    if media_id and url:attachments[media_id]=url
            for item in raw_items:
                kind=item.findtext('wp:post_type',default='',namespaces=namespaces)
                status=item.findtext('wp:status',default='publish',namespaces=namespaces)
                if kind not in ('post','page') or status!='publish':continue
                feature=''
                for pm in item.findall('wp:postmeta',namespaces=namespaces):
                    key=pm.findtext('wp:meta_key',default='',namespaces=namespaces)
                    if key=='_thumbnail_id':
                        feature=attachments.get(pm.findtext('wp:meta_value',default='',namespaces=namespaces),'')
                        break
                item_obj={'title':{'rendered':item.findtext('title',default='')},'content':{'rendered':item.findtext('content:encoded',default='',namespaces=namespaces)},'excerpt':{'rendered':''},'link':item.findtext('link',default=''),'slug':item.findtext('wp:post_name',default='',namespaces=namespaces),'date':item.findtext('wp:post_date',default='',namespaces=namespaces),'status':'publish'}
                if feature:item_obj['_embedded']={'wp:featuredmedia':[{'source_url':feature}]}
                entries.append((item_obj,'posts' if kind=='post' else 'pages'))
            print(f'WXR import: {len(entries)} posts/pages and {len(attachments)} attachment URLs',flush=True)
        else:
            for kind in ('pages','posts'):
                items,total,errs=endpoint(session,kind)
                failures+=errs if not items else []
                api_totals[kind]=total
                entries.extend((e,kind) for e in items)
            # Fill gaps even when *one* REST endpoint is available. For example,
            # /pages may work while /posts is disabled or times out.
            have={kind:sum(1 for _,k in entries if k==kind) for kind in ('posts','pages')}
            incomplete=not entries or any(have[k]==0 or (api_totals.get(k) and have[k]<api_totals[k]) for k in ('posts','pages'))
            if incomplete:
                print('WordPress REST incomplete; supplementing with public XML sitemaps...')
                urls,errs=sitemap_entries(session,args.limit)
                failures+=errs
                known={e.get('link','').rstrip('/') for e,k in entries}
                for i,url in enumerate(urls,1):
                    if url.rstrip('/') in known:continue
                    try:
                        e=get_from_html(session,url)
                        path=urlparse(url).path
                        kind='posts' if re.search(r'/20\d\d/\d\d/',path) else 'pages'
                        entries.append((e,kind))
                        known.add(url.rstrip('/'))
                        print('  HTML',i,'/',len(urls),url,flush=True)
                    except Exception as ex:failures.append(f'{url}: {ex}')
        # Discover *additional* press scans from the original WordPress press
        # page instead of assuming the earlier 13-item manual list is complete.
        try:
            from sync_press_archive import discover, merge
            press_file=ROOT/'_data/press.yml'
            press_data=yaml.safe_load(press_file.read_text(encoding='utf8')) or []
            for e,kind in entries:
                if kind=='pages' and slug(e.get('slug','')) in ('rassegna-stampa','press-review'):
                    found=discover(e.get('content',{}).get('rendered',''))
                    new=merge(press_data,found)
                    print(f'Press from WordPress page: {len(found)} scanned images, {len(new)} newly found')
            press_file.write_text(yaml.safe_dump(press_data,allow_unicode=True,sort_keys=False),encoding='utf8')
        except Exception as exc:
            failures.append('WordPress press image index: '+str(exc))
        if args.limit:entries=entries[:args.limit]
        mapping={}
        for e,k in entries:
            old=e.get('link','')
            if old:mapping[old.rstrip('/')+'/']=canonical_path(e,k)
            if old:mapping[old.rstrip('/')]=canonical_path(e,k)
        files=[]
        for i,(e,kind) in enumerate(entries,1):
            try:
                generated=write_page(e,kind,session,args.download_media,mapping,failures,args.replace_existing_pages)
                if generated:files.append(generated)
                if i%20==0:print(f'Written {i}/{len(entries)}',flush=True)
            except Exception as ex:failures.append(f"{e.get('link', '')}: {ex}")
    report=dict(items_discovered=len(entries),items_written=len(files),files=files,api_totals=api_totals,failures=failures,complete=(len(files)==len(entries) and not failures and all(not n or n==sum(1 for _,kind in entries if kind==k) for k,n in api_totals.items())),permissions_confirmed=True)
    report_path=ROOT/'MIGRATION_REPORT.json';report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2))
    from refresh_press_details import main as ensure_press_details
    from dedupe_archives import main as hide_duplicate_summaries
    from refresh_archives import main as refresh_pages
    ensure_press_details(); hide_duplicate_summaries(); refresh_pages()
    print(f"Generated {len(files)}/{len(entries)} local pages and posts. Report: {report_path}")
    if failures:print(f'{len(failures)} fetch or media errors; see report. Not certified as a complete export.',file=sys.stderr)
    else:print('All discovered entries imported; compare authoritative WP totals for completeness.')
if __name__=='__main__':main()
