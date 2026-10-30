# GitHub Pages — ISISLab /isislab-web/ (v10.2)

The public website is **https://isislab-unisa.github.io/isislab-web/**.
The repository is **isislab-unisa/isislab-web**.

The required Jekyll settings in `_config.yml` are now:

```yaml
url: "https://isislab-unisa.github.io"
baseurl: "/isislab-web"
```

Previous versions shipped an empty `baseurl` and therefore requested `/assets/css/…`
instead of `/isislab-web/assets/css/…`. This fix works with GitHub Pages
**Deploy from a branch** as well as the included **GitHub Actions** workflow.
The footer and sidebar links are also fixed using Jekyll's `relative_url`.

## Update the existing repository (keep imported posts and photos)

Copy **the PATCH ZIP's contents** into your current clone of `isislab-unisa/isislab-web`
and overwrite its corresponding files. Do not delete your existing `imported/`,
`articles/`, `press-articles/`, `assets/img/news/`, or `assets/img/press/`.

```bash
git add -A
git commit -m "Fix /isislab-web/ URL paths on GitHub Pages"
git push origin main
```

For **GitHub Pages → Deploy from a branch**: use the `main` branch and `/ (root)` folder.
For **GitHub Pages → GitHub Actions**: keep the included `.github/workflows/pages.yml`
and choose **GitHub Actions** as the deployment source. The workflow builds with
`--baseurl /isislab-web` and checks generated links. Pick ONE deployment mode.

Test after the Pages deployment finishes:

- https://isislab-unisa.github.io/isislab-web/assets/css/elegant.css
- https://isislab-unisa.github.io/isislab-web/assets/js/physics-balls.js
- https://isislab-unisa.github.io/isislab-web/assets/img/isislab-brand-horizontal.png

## Local Jekyll preview

The production config has `baseurl: /isislab-web`. For local development at
`http://localhost:4000/`, override it without editing `_config.yml`:

```bash
bundle exec jekyll serve --livereload --baseurl ""
```

`./start.sh` and Docker Compose already include that local override.

## About share-modal.js

The Jekyll project does **not** contain or reference `share-modal.js`. If it
continues to error, inspect its script URL in browser DevTools or test with
extensions disabled; that error is separate from the broken Pages asset paths.

## Validation

With dependencies installed:

```bash
bundle exec jekyll build --baseurl /isislab-web
python3 scripts/verify_github_pages.py --baseurl /isislab-web
python3 scripts/check_built_site.py --baseurl /isislab-web
```

Missing imported news or press image files must still be imported or committed
separately; fixing the URL prefix does not create missing image data.
