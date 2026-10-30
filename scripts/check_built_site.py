#!/usr/bin/env python3
"""Fail deployment when built HTML links to CSS, JS, or images not in _site.

The same scan works for GitHub Pages project routes (/repository-name/) and
root deployments (a custom domain or username.github.io).
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script' and attrs.get('src'):
            self.items.append(('script', attrs['src']))
        if tag == 'link' and attrs.get('rel') == 'stylesheet' and attrs.get('href'):
            self.items.append(('stylesheet', attrs['href']))
        if tag in ('img', 'source'):
            if attrs.get('src'):
                self.items.append(('image', attrs['src']))
            if attrs.get('srcset'):
                for part in attrs['srcset'].split(','):
                    self.items.append(('image', part.strip().split(' ')[0]))

parser = argparse.ArgumentParser()
parser.add_argument('--site', default='_site')
parser.add_argument('--baseurl', default='')
args = parser.parse_args()
root = Path(args.site).resolve()
base = '/' + args.baseurl.strip('/') if args.baseurl.strip('/') else ''
if not root.is_dir():
    parser.error(f'Cannot find generated site at {root}. Run Jekyll build first.')

errors, checked = [], 0
pages = list(root.rglob('*.html'))
if not pages:
    parser.error('No HTML documents were produced by Jekyll.')

for html in pages:
    refs = Refs()
    refs.feed(html.read_text(encoding='utf-8', errors='replace'))
    for kind, reference in refs.items:
        if not reference or reference.startswith(('data:', '#', 'blob:', 'mailto:')):
            continue
        parsed = urlparse(reference)
        if parsed.scheme or parsed.netloc:  # external font/image/etc.
            continue
        if reference.startswith('/'):
            path = unquote(parsed.path)
            if base and (path == base or path.startswith(base + '/')):
                path = path[len(base):] or '/'
            elif base:
                errors.append(f'{html.relative_to(root)}: {kind} lacks base path {base}: {reference}')
                continue
            file = root / path.lstrip('/')
        else:
            file = html.parent / unquote(parsed.path)
        checked += 1
        if not file.is_file():
            errors.append(f'{html.relative_to(root)}: missing {kind}: {reference}')

print(f'Asset audit: {len(pages)} HTML pages, {checked} CSS/JS/image references checked')
if errors:
    for error in errors[:65]:
        print('ERROR', error)
    if len(errors) > 65:
        print(f'... and {len(errors) - 65} more')
    raise SystemExit(f'Build blocked: {len(errors)} broken local asset URLs')
print('Asset audit: PASS')
