#!/usr/bin/env bash
# Start ISISLab with optional official-image synchronization, then Jekyll.
set -euo pipefail
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
  if [[ ! -x .venv/bin/python ]]; then
    echo 'Setting up local Python environment for site photos…'
    python3 -m venv .venv || echo 'Virtual environment unavailable; Jekyll will still run.'
  fi
  if [[ -x .venv/bin/python ]]; then
    if ! .venv/bin/python -c 'import requests, yaml, bs4' >/dev/null 2>&1; then
      .venv/bin/python -m pip install -r scripts/requirements.txt || echo 'Photo dependencies unavailable; using verified photos already cached.'
    fi
    if .venv/bin/python -c 'import requests, yaml, bs4' >/dev/null 2>&1; then
      .venv/bin/python scripts/sync_people.py || echo 'Original staff photos cannot be fetched right now; showing initials for missing portraits.'
    fi
  fi
fi
if ! command -v bundle >/dev/null 2>&1; then
  echo 'Bundler is required. Install Ruby and Bundler first.' >&2
  exit 1
fi
bundle install
exec bundle exec jekyll serve --livereload --baseurl ""
