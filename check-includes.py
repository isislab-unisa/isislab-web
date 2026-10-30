#!/usr/bin/env python3
"""Fail early if any Jekyll include tag references an absent include file."""
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parent
rx = re.compile(r"\{%\s*include\s+([a-zA-Z0-9_./-]+)")
missing=[]
for p in root.rglob("*"):
    if not p.is_file() or p.suffix not in {".html", ".md", ".markdown"} or any(d in {"_site", "vendor", ".git"} for d in p.parts):
        continue
    try: src=p.read_text(encoding="utf-8")
    except UnicodeError: continue
    for requested in rx.findall(src):
        if not (root/"_includes"/requested).is_file():
            missing.append((str(p.relative_to(root)), requested))
if missing:
    for file, inc in missing: print(f"MISSING: {file} -> _includes/{inc}")
    sys.exit(1)
print("All Jekyll include references resolve.")
