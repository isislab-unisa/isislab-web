# ISISLab — complete GitHub Pages project

Deployment target: https://isislab-unisa.github.io/isislab-web/

This ZIP is **repository-root ready**: its `_config.yml`, `_includes`, `_layouts`, `assets`, `pages`, `en`, `.github` and other files belong directly in the `isislab-web` repository root. Do not place them inside another `isislab-jekyll` folder.

## Publish

1. Extract the ZIP into the root of a clone of `isislab-unisa/isislab-web`. Keep any imported local news, press pages and media that are already in the repository (the ZIP may not contain those later imports).
2. Confirm that `_includes/header.html`, `_includes/people-grid.html`, and `_includes/archive-pagination.html` are present.
3. Run `python3 check-includes.py` to check include references.
4. Run `git add -A && git commit -m "Deploy corrected Jekyll site" && git push origin main`.
5. Set GitHub repo **Settings > Pages > Build and deployment > Source: GitHub Actions**.
6. Verify the workflow in the Actions tab.

The GitHub Pages URL is configured as `url: https://isislab-unisa.github.io`, `baseurl: /isislab-web`. The workflow builds with the same prefix.

This project is the latest packaged source available in this conversation plus the missing-template repair. Previously imported content from your local/GitHub copy might not be contained in this ZIP, so preserve such files when merging. Missing original WordPress images remain placeholders until imported.
