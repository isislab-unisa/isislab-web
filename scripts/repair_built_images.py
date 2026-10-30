#!/usr/bin/env python3
"""Replace missing *local* editorial images with bundled local placeholders.

A WordPress import can leave image paths in Markdown or HTML even when the
actual media file was not committed to Git. Do not deploy HTML that requests
those non-existent files. This adjusts only the generated _site output, not
source articles or their metadata.
"""
from pathlib import Path
from urllib.parse import urlparse, unquote
import argparse
import re

cli = argparse.ArgumentParser()
cli.add_argument('--site', default='_site')
cli.add_argument('--baseurl', default='')
args = cli.parse_args()
root = Path(args.site).resolve()
base = '/' + args.baseurl.strip('/') if args.baseurl.strip('/') else ''
if not root.is_dir():
    cli.error('Run Jekyll build before repairing its output.')

def exists(src, html):
    parsed = urlparse(src)
    if not src or src.startswith(('data:', 'blob:', '#')) or parsed.scheme or parsed.netloc:
        return True
    path = unquote(parsed.path)
    if path.startswith('/'):
        if base and path.startswith(base + '/'):
            path = path[len(base):]
        elif base:
            return False
        return (root / path.lstrip('/')).is_file()
    return (html.parent / path).is_file()

image_tag = re.compile(r'<img\b[^>]*>', re.I | re.S)
source_attr = re.compile(r'(?<![-\w])src\s*=\s*(["\'])(.*?)\1', re.I | re.S)
srcset_attr = re.compile(r'\s+srcset\s*=\s*(["\']).*?\1', re.I | re.S)
missing = []
for html in root.rglob('*.html'):
    old = html.read_text(encoding='utf-8', errors='replace')
    def update(match):
        tag = match.group()
        src_match = source_attr.search(tag)
        if not src_match:
            return tag
        src = src_match.group(2)
        if exists(src, html):
            return tag
        press = 'press' in src.lower() or 'stampa' in str(html).lower() or 'press' in str(html).lower()
        fallback = 'press-placeholder.svg' if press else 'news-placeholder.svg'
        new_url = base + '/assets/img/' + fallback
        missing.append(str(html.relative_to(root)) + ': ' + src)
        tag = tag[:src_match.start(2)] + new_url + tag[src_match.end(2):]
        return srcset_attr.sub('', tag)
    new = image_tag.sub(update, old)
    if new != old:
        html.write_text(new, encoding='utf-8')

print('Missing local <img> sources replaced with bundled SVG placeholders:', len(missing))
for item in missing[:20]:
    print('  ', item)
if len(missing) > 20:
    print('  ... plus', len(missing) - 20, 'others')
