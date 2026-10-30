#!/usr/bin/env python3
"""Check exact ISISLab project-site URL prefixes in generated Jekyll output."""
from argparse import ArgumentParser
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import sys

class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('a','link') and a.get('href'):
            self.refs.append((tag, a['href']))
        if tag in ('script','img','source') and a.get('src'):
            self.refs.append((tag, a['src']))

ap = ArgumentParser()
ap.add_argument('--site',default='_site')
ap.add_argument('--baseurl',default='/isislab-web')
args = ap.parse_args()
root = Path(args.site)
base = '/' + args.baseurl.strip('/')
if not root.is_dir():
    sys.exit('Missing _site folder; build with Jekyll before running this test')
errors=[]
count=0
for file in root.rglob('*.html'):
    parser=Collect()
    parser.feed(file.read_text(encoding='utf-8',errors='replace'))
    for tag,value in parser.refs:
        parsed = urlparse(value)
        if parsed.scheme or parsed.netloc or value.startswith(('#','mailto:','tel:','javascript:','data:')):
            continue
        if value.startswith('/') and not (parsed.path==base or parsed.path.startswith(base+'/')):
            errors.append(f'{file.relative_to(root)}: {tag} missing {base}: {value}')
        count += 1
home = root / 'index.html'
if not home.exists():
    errors.append('index.html missing')
else:
    content=home.read_text(encoding='utf-8')
    for asset in ('/assets/css/elegant.css','/assets/css/reference-fidelity.css','/assets/css/refinements-v10.css', '/assets/js/site.js', '/assets/js/physics-balls.js', '/assets/img/isislab-brand-horizontal.png'):
        if base+asset not in content:
            errors.append('index.html: missing prefixed asset '+base+asset)
print('Base path audit:', count, 'local refs; errors:', len(errors))
for e in errors[:70]:print('ERROR:',e)
if errors:raise SystemExit(1)
print('Base path audit PASS for',base)
