#!/usr/bin/env bash
# Download original WordPress images to assets/img/news, assets/img/press.
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="${PYTHON:-python3}"
"$PYTHON" -m pip install -r scripts/requirements.txt
"$PYTHON" scripts/sync_press_archive.py || true
"$PYTHON" scripts/download_editorial_images.py "$@" || true
"$PYTHON" scripts/sync_article_media.py "$@" || true
"$PYTHON" scripts/audit_offline.py
