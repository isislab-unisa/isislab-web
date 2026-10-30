# ISISLab GitHub Pages build repair — missing Jekyll includes

This is an **overlay patch** for the existing repository `isislab-unisa/isislab-web`, NOT an entire replacement site. It adds the missing layout includes and the correct Pages `baseurl` without changing your imported news, media, or data.

## Why the build failed

`en/chi-siamo.md` and `pages/chi-siamo.md` request `{% include people-grid.html %}`, but `_includes/people-grid.html` is missing from the committed branch. The repository is also missing `header.html` and `archive-pagination.html`, referenced by other templates. Jekyll in GitHub Pages safe mode cannot resolve a missing include.

## Apply (from the root of your existing `isislab-web` Git repository)

```sh
# Unzip directly into the root of the repository (not its parent)
unzip -o ~/Downloads/isislab-github-pages-buildfix.zip

# Verify paths, including the leading underscore and correct capitalization
ls -l _includes/{people-grid,header,archive-pagination}.html

git add -f _includes/people-grid.html _includes/header.html _includes/archive-pagination.html
git add _config.yml
git status --short
git commit -m "Fix missing Jekyll includes and GitHub Pages baseurl"
git push origin main
```

In GitHub -> Actions, wait for the Pages build to succeed. For a repo served at
`https://isislab-unisa.github.io/isislab-web/`, `_config.yml` contains:

```yaml
url: "https://isislab-unisa.github.io"
baseurl: "/isislab-web"
```

If GitHub still says an include is missing, verify it is in the **same branch GitHub Pages is building**:

```sh
git ls-files '_includes/*'
git show HEAD:_includes/people-grid.html | head
```

GitHub Pages builds from the repository root. Do not place the files inside a nested `isislab-jekyll` directory.

### Notes

This repair fixes the specific **missing include / project URL** errors. It does not download missing news photographs, and it does not change other potentially incomplete WordPress imports. A complete remote Jekyll build cannot be tested in this environment.
