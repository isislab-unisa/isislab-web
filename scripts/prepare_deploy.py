#!/usr/bin/env python3
"""Make imported image mappings safe before a Jekyll/GitHub Pages build.

Imported media lists may refer to files available on the editor's machine but not
committed to Git. Remove ONLY those invalid *local* mappings on the build runner;
archives then use bundled SVG placeholders rather than broken URLs. This script
also checks that the critical theme assets were committed.
"""
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: python3 -m pip install PyYAML")

ROOT = Path(__file__).resolve().parent.parent
CORE = [
    'assets/css/style.css', 'assets/css/elegant.css',
    'assets/css/reference-fidelity.css', 'assets/css/refinements-v10.css',
    'assets/js/site.js', 'assets/js/physics-balls.js',
    'assets/img/isislab-brand-horizontal.png', 'assets/img/isislab-mascot.png',
    'assets/img/news-placeholder.svg', 'assets/img/press-placeholder.svg',
]

def local_exists(value):
    if not isinstance(value, str) or not value.strip():
        return False
    if value.startswith(('http://', 'https://', '//', 'data:')):
        return False
    value = value.split('?', 1)[0].split('#', 1)[0].lstrip('/')
    if '..' in Path(value).parts:
        return False
    file = ROOT / value
    return file.is_file()

missing = [x for x in CORE if not (ROOT / x).is_file()]
if missing:
    sys.exit('Required theme assets are missing from the Git checkout:\n' + '\n'.join(missing))

rejected = []
for file in ['media_local.yml', 'media_thumbs.yml']:
    path = ROOT / '_data' / file
    values = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    if not isinstance(values, dict):
        sys.exit(f'Expected mapping in {path}')
    kept = {}
    for source, dest in values.items():
        if local_exists(dest):
            kept[source] = dest
        else:
            rejected.append(f'{file}: {dest}')
    if len(kept) != len(values):
        path.write_text(yaml.safe_dump(kept, allow_unicode=True, sort_keys=False), encoding='utf-8')

photos = ROOT / '_data/people_photos.yml'
if photos.exists():
    values = yaml.safe_load(photos.read_text(encoding='utf-8')) or {}
    if isinstance(values, dict):
        clean = {}
        for name, record in values.items():
            if isinstance(record, dict) and local_exists(record.get('image')):
                clean[name] = record
            else:
                rejected.append(f'people_photos.yml: {name}')
        if len(clean) != len(values):
            photos.write_text(yaml.safe_dump(clean, allow_unicode=True, sort_keys=False), encoding='utf-8')

for folder in ('articles', 'press-articles', 'pages', 'en'):
    for path in (ROOT / folder).glob('*.md'):
        source = path.read_text(encoding='utf-8')
        if not source.startswith('---\n'):
            continue
        parts = source.split('---\n', 2)
        if len(parts) != 3:
            continue
        meta = yaml.safe_load(parts[1]) or {}
        if not isinstance(meta, dict):
            continue
        front = parts[1]
        for key in ('local_hero_image', 'local_thumbnail_image'):
            if key in meta and not local_exists(meta[key]):
                rejected.append(f'{path.relative_to(ROOT)}: {key}={meta[key]}')
                front = re.sub(r'^' + key + r':[^\n]*\n', '', front, flags=re.MULTILINE)
        if front != parts[1]:
            path.write_text('---\n' + front + '---\n' + parts[2], encoding='utf-8')

print('Theme asset check: PASS (' + str(len(CORE)) + ' mandatory assets present)')
print('Unbundled local image references replaced by safe placeholders:', len(rejected))
for val in rejected[:25]:
    print('  ', val)
if len(rejected) > 25:
    print(f'  ... plus {len(rejected)-25} more')
