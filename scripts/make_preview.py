"""Generate standalone visual preview in IT and EN without Jekyll.
Real Jekyll pages require bundle exec jekyll serve.
"""
from pathlib import Path
import re,base64,html,yaml
root=Path(__file__).resolve().parents[1]
css=(root/'assets/css/style.css').read_text()+'\n'+(root/'assets/css/elegant.css').read_text()+'\n'+(root/'assets/css/reference-fidelity.css').read_text()+'\n'+(root/'assets/css/refinements-v10.css').read_text();js=(root/'assets/js/site.js').read_text();physics=(root/'assets/js/physics-balls.js').read_text()
logo='assets/img/isislab-brand-horizontal.png'
press=yaml.safe_load((root/'_data/press.yml').read_text())
news=yaml.safe_load((root/'_data/news.yml').read_text())
media_local=yaml.safe_load((root/'_data/media_local.yml').read_text()) or {}
media_thumbs=yaml.safe_load((root/'_data/media_thumbs.yml').read_text()) or {}
for lang in ['it','en']:
    is_en=lang=='en'; nav=yaml.safe_load((root/'_data'/f'navigation_{lang}.yml').read_text())
    prefix='/en' if is_en else ''
    home=(root/'en/index.html' if is_en else root/'index.html').read_text().split('---',2)[-1]
    home=re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}",lambda m:m.group(1),home)
    # Replace Jekyll press/news loops with local preview equivalents.
    cards=''.join('<a class="home-press-item" href="'+prefix+'/rassegna-stampa/'+item['slug']+'/"><img loading="lazy" src="'+media_thumbs.get(item['image'], media_local.get(item['image'], 'assets/img/press-placeholder.svg')).lstrip('/')+'" alt=""><span class="press-thumb-info"><time>'+str(item['date'])+'</time><strong>'+html.escape(item['publication'])+'</strong><small>'+html.escape(item['title'])+'</small></span></a>' for item in press[:3])
    home=re.sub(r'\{% for item in site.data.press limit:3 %\}.*?\{% endfor %\}',cards,home,flags=re.S)
    snippets=''.join('<li class="lab-reveal is-visible"><div class="lab-card lab-news-card"><a class="home-news-thumb" href="'+prefix+'/news/'+item['slug']+'/"><img src="'+media_thumbs.get(item.get('image'), media_local.get(item.get('image'), 'assets/img/news-placeholder.svg')).lstrip('/')+'" alt=""></a><div class="wp-block-post-date">'+str(item['date'])+'</div><h3 class="wp-block-post-title"><a href="'+prefix+'/news/'+item['slug']+'/">'+html.escape(item['title_en' if is_en else 'title_it'])+'</a></h3><p class="wp-block-post-excerpt__excerpt">'+html.escape(item['summary_en' if is_en else 'summary_it'])+'</p><a class="lab-news-more" href="'+prefix+'/news/'+item['slug']+'/">Read →</a></div></li>' for item in news[:3])
    home=re.sub(r'\{% for item in site.data.news limit:3 %\}.*?\{% endfor %\}',snippets,home,flags=re.S)
    h=['<a class="skip-link" href="#main-content">'+('Skip to content' if is_en else 'Vai al contenuto')+'</a>','<header class="lab-header" id="top"><div class="lab-header-inner alignwide">',f'<a class="lab-brand-link" href="#top"><img class="lab-brand-logo" src="{logo}" alt="ISISLab"></a>', '<button class="nav-toggle" type="button" aria-controls="main-navigation" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button>', '<nav class="lab-primary-nav" id="main-navigation"><ul class="nav-list">']
    for item in nav:
        h.append('<li class="nav-item nav-item--parent"><div class="nav-item-head"><a href="'+html.escape(item['url'])+'">'+html.escape(item['title'])+'</a><button class="submenu-toggle" type="button" aria-expanded="false"><svg viewBox="0 0 12 12"><path d="m2 4 4 4 4-4"/></svg></button></div><ul class="nav-dropdown">')
        for child in item.get('children',[]):h.append('<li><a href="'+html.escape(child['url'])+'">'+html.escape(child['title'])+'</a></li>')
        h.append('</ul></li>')
    h.append('</ul></nav>')
    if is_en:h.append('<div class="language-selector"><a href="preview.html" data-language-choice="it">IT</a> / <a class="is-current" href="preview-en.html">EN</a></div>')
    else:h.append('<div class="language-selector"><a class="is-current" href="preview.html">IT</a> / <a href="preview-en.html" data-language-choice="en">EN</a></div>')
    h.append('</div></header>')
    footer='<footer class="lab-footer"><div class="alignwide footer-inner"><div class="footer-about"><img src="'+logo+'" alt="ISISLab" width="160"><p>University of Salerno · Department of Computer Science</p><p>Edificio F, Stecca 7, Lab. 10, Fisciano (SA)</p></div><div class="footer-links"><h3>Research</h3><a href="'+prefix+'/tematiche/">Research areas</a><a href="'+prefix+'/progetti/">Projects</a><a href="'+prefix+'/pubblicazioni-scientifiche/">Publications</a></div><div class="footer-links"><h3>Students</h3><a href="'+prefix+'/informazioni-utili/">Theses</a><a href="'+prefix+'/erasmus/">Erasmus</a></div><div class="footer-links"><h3>ISISLab</h3><a href="'+prefix+'/rassegna-stampa/">Press</a><a href="'+prefix+'/news/">News</a></div></div></footer>'
    out='<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ISISLab · '+lang.upper()+' preview</title><style>'+css+'</style></head><body class="home">'+''.join(h)+home+footer+'<script>'+js+'</script><script>'+physics+'</script></body></html>'
    name='preview-en.html' if is_en else 'preview.html'
    (root/name).write_text(out);print(name,len(out))
