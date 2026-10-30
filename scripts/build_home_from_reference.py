"""One-off importer: builds index.html from the supplied WordPress homepage markup.

Requires BeautifulSoup (`pip install beautifulsoup4`) for regeneration; the generated
index.html is committed and does not need Python or BeautifulSoup when using Jekyll.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, parse_qs

root=Path(__file__).resolve().parents[1]
soup=BeautifulSoup((root/'reference/isislab-original.html').read_text(encoding='utf-8'),'html.parser')
main=soup.select_one('main')
main['id']='main-content'
for a in main.select('a[href]'):
    url=a['href']
    if url.startswith('http://localhost:8080/'):
        parts=urlsplit(url)
        if parse_qs(parts.query).get('page_id')==['10']:
            path='/indirizzo-cloud-computing/'
        elif parts.query.startswith('p='):
            path='/news/'
        else:
            path=parts.path or '/'
        if parts.fragment:
            path+='#'+parts.fragment
        a['href']="{{ '"+path+"' | relative_url }}"
canvas=main.find('canvas')
if canvas:
    canvas.attrs={'class': 'lab-physics-hero__canvas','aria-hidden':'true'}
# Original homepage contained WordPress's demo "Ciao mondo!" post. Replace with
# verified public ISISLab news items, using the same 3-column card visual.
posts=[
  ('19 Maggio 2026','XRTourGuide al Museo di Morigerati','Il progetto XRTourGuide è stato sperimentato il 9 maggio 2026 al Museo Etnografico di Morigerati, tra tecnologia, cultura e territorio.'),
  ('7 Maggio 2026','Open Day Data Center — Regione Campania','La seconda edizione dell’Open Day Data Center si è svolta il 5 maggio 2026 con il Dipartimento di Informatica dell’Università di Salerno.'),
  ('17 Aprile 2026','Geckode Hackathon 2026','Il 16 e 17 aprile, a UNISA, un hackathon dedicato a innovazione, XR e sviluppo del metaverso NEOLAiA.'),
]
query=main.select_one('.wp-block-query')
if query:
    query.clear()
    ul=soup.new_tag('ul', attrs={'class':'is-flex-container columns-3 wp-block-post-template is-layout-flow lab-news-grid'})
    for dt, title, desc in posts:
        li=soup.new_tag('li',attrs={'class':'lab-reveal is-visible'})
        card=soup.new_tag('div',attrs={'class':'lab-card lab-news-card'})
        date=soup.new_tag('div',attrs={'class':'wp-block-post-date has-xs-font-size'});date.string=dt
        h=soup.new_tag('h3',attrs={'class':'wp-block-post-title has-large-font-size'})
        link=soup.new_tag('a',href="{{ '/news/' | relative_url }}");link.string=title;h.append(link)
        p=soup.new_tag('p',attrs={'class':'wp-block-post-excerpt__excerpt'});p.string=desc
        more=soup.new_tag('a',attrs={'class':'lab-news-more'},href="{{ '/news/' | relative_url }}");more.string='Leggi →'
        card.extend([date,h,p,more]);li.append(card);ul.append(li)
    query.append(ul)
main_html=str(main)
(root/'index.html').write_text('---\nlayout: default\ntitle: ""\ndescription: "ISISLab: calcolo scalabile, collaborazione aperta e tecnologie immersive all’Università di Salerno."\n---\n'+main_html+'\n',encoding='utf-8')
print('Wrote',root/'index.html')
