#!/usr/bin/env bash
# Import public WordPress pages/posts, press records and media locally.
# Compatible with the Bash 3.2 version shipped on macOS.
set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" != "--i-have-rights-to-migrate" ]]; then
  echo 'Usage: ./migrate.sh --i-have-rights-to-migrate [--from-wxr wordpress.xml] [--uploads /path/to/wp-content/uploads]' >&2
  exit 2
fi
shift

UPLOADS_PATH=''
validate_args() {
  # The shifts in this function do not consume the script's original "$@".
  while (( $# > 0 )); do
    case "$1" in
      --uploads)
        if (( $# < 2 )) || [[ -z "${2:-}" ]]; then
          echo 'Error: --uploads requires a directory path.' >&2
          exit 2
        fi
        UPLOADS_PATH="$2"
        if [[ ! -d "$UPLOADS_PATH" ]]; then
          echo "Error: --uploads must be an existing directory: $UPLOADS_PATH" >&2
          exit 2
        fi
        shift 2
        ;;
      --from-wxr)
        if (( $# < 2 )) || [[ -z "${2:-}" ]]; then
          echo 'Error: --from-wxr requires an XML file path.' >&2
          exit 2
        fi
        if [[ ! -f "$2" ]]; then
          echo "Error: --from-wxr must be an existing file: $2" >&2
          exit 2
        fi
        shift 2
        ;;
      *) shift ;;
    esac
  done
}
validate_args "$@"

PYTHON="${PYTHON:-python3}"
if [[ ! -x .venv/bin/python ]]; then "$PYTHON" -m venv .venv; fi
.venv/bin/python -m pip install -r scripts/requirements.txt

# "$@" is safe when no optional flags are supplied, even with set -u on
# macOS Bash 3.2. An empty ARGS=(...) array was not.
.venv/bin/python scripts/import_wordpress.py --i-have-rights-to-migrate \
  --download-media --replace-existing-pages "$@"

# WordPress press scans may not be attached to individual posts.
if [[ -n "$UPLOADS_PATH" ]]; then
  .venv/bin/python scripts/download_editorial_images.py --uploads "$UPLOADS_PATH" || true
  .venv/bin/python scripts/sync_article_media.py --uploads "$UPLOADS_PATH" || true
else
  .venv/bin/python scripts/download_editorial_images.py || true
  .venv/bin/python scripts/sync_article_media.py || true
fi
.venv/bin/python scripts/refresh_press_details.py
.venv/bin/python scripts/dedupe_archives.py
.venv/bin/python scripts/refresh_archives.py
.venv/bin/python scripts/audit_offline.py
printf '\nImport finished. Review MIGRATION_REPORT.json, ARTICLE_IMAGE_REPORT.json and OFFLINE_AUDIT.json.\n'
printf 'Any unavailable images remain unavailable, not silently replaced by unrelated pictures.\n'
