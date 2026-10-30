> GitHub Pages fix (v10.2): `/isislab-web/` base URL is configured in `_config.yml`. See [GITHUB_PAGES.md](GITHUB_PAGES.md). For local serving use `bundle exec jekyll serve --baseurl ""`.

# ISISLab — Jekyll migration (v9)

A responsive Jekyll website based on the provided WordPress homepage. The original submitted ISISLab logo and three-color interactive sphere animation are bundled. Italian/English menus and browser-language selection remain in place.

## Run

```bash
cd isislab-jekyll
bundle install
bundle exec jekyll serve --livereload
```

Open `http://localhost:4000/` (Italian) or `http://localhost:4000/en/` (English). Docker is also supported: `docker compose up --build`.


### macOS Bash compatibility (v9.1 fix)

`migrate.sh` now works with the macOS-provided Bash 3.2 even when no optional flags are provided. It forwards `"$@"` directly and avoids expanding uninitialized/empty arrays with `set -u`. The script reports missing XML files or uploads directories before running the importer.

```bash
./migrate.sh --i-have-rights-to-migrate
```

If using a local export, specify **existing paths** for `--from-wxr` and optionally `--uploads`.

## News and press — working pagination

- **News:** `/news/`, `/news/page/2/`, … and `/en/news/`, `/en/news/page/2/`, …
- **Press:** `/rassegna-stampa/`, `/rassegna-stampa/page/2/`, … and equivalent `/en/` URLs.
- **9 entries per page**, with page numbers and previous/next links. Pages are generated statically, with no Jekyll pagination plugin.
- Both archives display **small thumbnails**. Individual news and press pages show the **full original image**, if imported.
- `python3 scripts/refresh_archives.py` recalculates pagination after every content import, based on actual Jekyll article files and `_data/press.yml`. The import command does this automatically.
- Curated summary pages can remain accessible but are hidden from archive listings when a matching full WordPress article has been imported.

## Download original photographs and press scans

This ZIP **does not include the original WordPress photographs**: this environment cannot resolve `www.isislab.it`, so remote HTTP downloads fail. All included image files have been verified as local; nothing is represented as an original photograph unless its bytes have actually been obtained. The supplied ISISLab logo is bundled.

On a machine that can reach the website:

```bash
./download-images.sh
```

The downloader finds press scans and featured images via WordPress REST, embedded media and the paginated news archive. It writes to `assets/img/press/`, `assets/img/news/`, generates WebP thumbnails and records failures in `MEDIA_DOWNLOAD_REPORT.json` and `ARTICLE_IMAGE_REPORT.json`. It can discover additional press scans in the original press-page HTML.

**More reliable offline option:** Export the original WordPress site using **Tools → Export → All content**, then copy the original `wp-content/uploads` directory. Run:

```bash
./migrate.sh --i-have-rights-to-migrate \
  --from-wxr /path/to/wordpress-export.xml \
  --uploads /path/to/wp-content/uploads
```

The authorized importer copies full post/page content into the Jekyll project, discovers press scans from the WordPress press page, resolves featured images using WXR attachment IDs, and writes downloaded images and PDFs locally. It handles WordPress image-size filenames like `image-300x200.jpg`, `image-scaled.jpg` when only the full-sized source exists in the uploads export.

If remote WordPress REST and its media server are accessible, use:

```bash
./migrate.sh --i-have-rights-to-migrate
```

You may also import from a saved HTML copy of the press archive:

```bash
python3 scripts/sync_press_archive.py --html /path/to/rassegna-stampa.html
```

After importing, inspect these **truthful completion reports**:

- `MIGRATION_REPORT.json` — imported posts, pages, failures and WP REST totals when available.
- `MEDIA_DOWNLOAD_REPORT.json` — which of the originally indexed press/news images were saved.
- `ARTICLE_IMAGE_REPORT.json` — image coverage for **every** imported news article.
- `OFFLINE_AUDIT.json` — actual local image counts, links and duplicate permalink audit.

A WordPress WXR file may exclude media bytes: you need `wp-content/uploads` too. The import scripts do not claim parity unless the original WordPress totals have been checked against the local output. Content republishing is supported only if you have the necessary rights.

## File layout

| Location | Purpose |
|---|---|
| `articles/`, `press-articles/` | Local news and full-size press/article detail routes |
| `pages/`, `en/` | Public informational and archive entry pages |
| `archive-generated/` | Automatic static pagination pages in both languages |
| `_layouts/news.html`, `_layouts/press.html` | Paginated archive listing templates |
| `_includes/archive-pagination.html` | Accessible numbered and next/previous page navigation |
| `assets/img/news/`, `assets/img/press/` | Original imported images and compact WebP thumbnails |
| `assets/img/isislab-logo-original.png` | Original user-uploaded lab logo |
| `assets/js/physics-balls.js` | Moving, colliding spheres with randomized tap/click impulses |
| `scripts/import_wordpress.py` | REST / sitemap / WXR migration |
| `scripts/sync_press_archive.py` | Extract press clippings from the original press page |
| `scripts/download_editorial_images.py` | Fetch featured images and press scans, including offline filename variants |
| `scripts/sync_article_media.py` | Thumbnail generator for **all** imported WordPress articles |
| `scripts/refresh_archives.py` | Regenerate IT/EN archive pagination |
| `scripts/audit_offline.py` | Local completeness check |

## Existing coverage, and what is still missing

This package starts with **12 curated Italian/English news summaries and 13 press records**, not a complete historical WordPress export. It currently has two news and two press archive pages in each language. WordPress publishes older news (and may have more press items), so **the rest can only be migrated after the source site or its export can be accessed**. Once imported, the routes, pagination and local image paths expand to cover the additional posts automatically.

The original WordPress theme JavaScript `isislab_files/site.js` was not included with the uploaded HTML. The bundled animation uses the independently tested custom physics implementation from v7.

## Validation

Python scripts compiled and a synthetic WordPress WXR+uploads integration test verified offline image matching and 3-page pagination after 14 additional news articles. `OFFLINE_AUDIT.json` reports actual bundled media. Jekyll Ruby dependencies could not be installed in this execution environment, so a full local Jekyll build was not verified here.

## Version 10 — visual refinements

The homepage uses `assets/css/refinements-v10.css`, loaded after the original
CSS files. Both `index.html` and `en/index.html` now have:

- Enlarged and better-spaced text for headings, research cards, hub cards and
  interior reading pages, with specific mobile sizes.
- Three small glass research spheres with the same translucent, highlighted,
  halo finish and exactly the same cyan/violet/green hues as the moving hero balls.
  Their subtle CSS float is disabled with reduced-motion preferences.
- Eight different accessible decorative SVG icons for **Explore ISISLab** in a
  separate warm/neutral palette, distinct from the three research colors.
- An even 4-by-2 hub layout on desktop, 2 columns on tablets and comfortable
  single-column text-and-icon cards on phones.

To regenerate the standalone HTML previews, run:
`python3 scripts/make_preview.py` (requires `PyYAML`).
These style updates do not alter existing pages, editorial data or migration scripts.

## GitHub Pages deployment (v10.1)

**Use the bundled GitHub Actions workflow** at `.github/workflows/pages.yml` and select **Settings → Pages → Source: GitHub Actions**. It determines the correct `/REPOSITORY` prefix automatically for project sites, checks required files, prevents stale imported image mappings from producing broken image links, builds the site, and validates the generated CSS/JS/image paths before publishing. Read [GITHUB_PAGES.md](GITHUB_PAGES.md) for step-by-step deployment.

If updating an existing repository, copy the **contents** of the `isislab-jekyll` directory to the repository root and commit the hidden `.github` directory. If you continue to publish from a branch, you must configure `baseurl` manually to match your Pages URL.
