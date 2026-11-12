/* Reads a SAME-ORIGIN JSON file built by the GitHub Action. No CORS requests to dblp. */
(function () {
  'use strict';
  const root = document.getElementById('dblp-library');
  if (!root || root.dataset.initialized) return;
  root.dataset.initialized = 'true';
  const PEOPLE = [
    { pid: '71/11144', name: 'Carmine Spagnuolo' },
    { pid: '224/0266', name: 'Maria Angela Pellegrino' },
    { pid: '32/6668', name: 'Vittorio Scarano' },
    { pid: '26/4019', name: 'Gennaro Cordasco' },
    { pid: '07/527', name: 'Biagio Cosenza' }
  ];
  const PAGE_SIZE = 20;
  const DATA_URL = root.dataset.jsonUrl;
  const $ = (id) => root.querySelector('#' + id);
  const els = {
    people: $('dblp-people'), topic: $('dblp-topic'), venue: $('dblp-venue'),
    from: $('dblp-from'), to: $('dblp-to'), author: $('dblp-author'),
    coauthor: $('dblp-coauthor'), sort: $('dblp-sort'), reset: $('dblp-reset'),
    refresh: $('dblp-refresh'), scope: $('dblp-scope'), format: $('dblp-format'),
    export: $('dblp-export'), results: $('dblp-results'), count: $('dblp-count'),
    status: $('dblp-status'), pagination: $('dblp-pagination')
  };
  let publications = [], filtered = [], currentPage = 1;

  function norm(value) { return String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase(); }
  function safeUrl(value) {
    try {
      const url = new URL(String(value || ''));
      return (url.protocol === 'https:' || url.protocol === 'http:') ? url.href : '';
    } catch (_) { return ''; }
  }
  function makeLink(label, url, className) {
    const a = document.createElement('a');
    a.textContent = label;
    if (className) a.className = className;
    a.href = safeUrl(url) || '#';
    a.target = '_blank'; a.rel = 'noopener noreferrer';
    return a;
  }
  function setStatus(message, error) {
    els.status.textContent = message;
    els.status.setAttribute('role', error ? 'alert' : 'status');
  }

/* for (const person of PEOPLE) {
    els.people.appendChild(makeLink(person.name, 'https://dblp.org/pid/' + person.pid));
    const option = document.createElement('option');
    option.value = person.pid; option.textContent = person.name;
    els.author.appendChild(option);
  }*/


  async function load(reload) {
    els.refresh.disabled = true;
    els.export.disabled = true;
    setStatus('Loading local bibliography…');
    try {
      if (!DATA_URL) throw new Error('Missing JSON path. Render this include through Jekyll.');
      const response = await fetch(DATA_URL, { cache: reload ? 'no-store' : 'default' });
      if (!response.ok) throw new Error('HTTP ' + response.status + ' for ' + DATA_URL);
      const data = await response.json();
      if (!Array.isArray(data.publications)) throw new Error('Invalid bibliography JSON.');
      publications = data.publications;
      if (!publications.length) {
        setStatus('No publications generated yet. Run the GitHub Action: Update dblp publications and deploy Jekyll.', true);
      } else {
        const date = data.generated_at ? new Date(data.generated_at) : null;
        const stamp = date && !Number.isNaN(date.getTime()) ? ' · Last update: ' + date.toLocaleDateString() : '';
        setStatus('Loaded ' + publications.length + ' unique publications' + stamp + '.');
      }
      els.export.disabled = publications.length === 0;
      applyFilters();
    } catch (error) {
      console.error('Could not load local dblp cache:', error);
      publications = [];
      applyFilters();
      setStatus('Unable to read the Jekyll JSON cache (' + error.message + '). Run GitHub Actions and check the deployed JSON path.', true);
    } finally {
      els.refresh.disabled = false;
    }
  }

  function applyFilters() {
    const topic = norm(els.topic.value.trim()), venue = norm(els.venue.value.trim());
    const coauthor = norm(els.coauthor.value.trim()), pid = els.author.value;
    const from = Number(els.from.value) || -Infinity;
    const to = Number(els.to.value) || Infinity;
    const terms = topic.split(/\s+/).filter(Boolean);
    filtered = publications.filter((p) => (
      p.year >= from && p.year <= to &&
      (!pid || p.sourceIds.includes(pid)) &&
      terms.every((term) => norm(p.title).includes(term)) &&
      (!venue || norm(p.venue).includes(venue)) &&
      (!coauthor || p.authors.some((author) => norm(author).includes(coauthor)))
    ));
    const sort = els.sort.value;
    filtered.sort((a, b) => sort === 'title'
      ? a.title.localeCompare(b.title) || b.year - a.year
      : sort === 'oldest' ? a.year - b.year || a.title.localeCompare(b.title)
      : b.year - a.year || a.title.localeCompare(b.title));
    currentPage = 1;
    render();
  }

  function addText(parent, tag, text, className) {
    const el = document.createElement(tag);
    if (className) el.className = className;
    el.textContent = text; parent.appendChild(el); return el;
  }
  function render() {
    const pages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    currentPage = Math.max(1, Math.min(currentPage, pages));
    const start = (currentPage - 1) * PAGE_SIZE;
    const visible = filtered.slice(start, start + PAGE_SIZE);
    els.count.textContent = filtered.length
      ? 'Showing ' + (start + 1) + '–' + (start + visible.length) + ' of ' + filtered.length + ' publications'
      : publications.length ? 'No matching publications' : 'No publications available';
    els.results.replaceChildren();
    if (!visible.length) addText(els.results, 'li', 'Try broadening your search or clearing the filters.', 'dblp-empty');
    for (const p of visible) {
      const li = document.createElement('li'); li.className = 'dblp-paper';
      const title = makeLink(p.title, p.url || p.edition, 'dblp-paper-title'); li.appendChild(title);
      addText(li, 'div', p.authors.join(', ') || 'Authors not listed', 'dblp-byline');
      const meta = document.createElement('div'); meta.className = 'dblp-meta';
      const bits = [String(p.year || 'Year unavailable'), p.venue, p.type].filter(Boolean);
      meta.appendChild(document.createTextNode(bits.join(' · ')));
      if (p.doi) { meta.appendChild(document.createTextNode(' · '));
        meta.appendChild(makeLink('DOI', 'https://doi.org/' + encodeURI(p.doi))); }
      if (p.edition) { meta.appendChild(document.createTextNode(' · '));
        meta.appendChild(makeLink('External link', p.edition)); }
      li.appendChild(meta);
      for (const id of p.sourceIds) {
        const person = PEOPLE.find((a) => a.pid === id);
        if (person) addText(li, 'span', person.name, 'dblp-tag');
      }
      els.results.appendChild(li);
    }
    els.pagination.replaceChildren();
    if (pages <= 1) return;
    const makeButton = (label, page, disabled, current) => {
      const btn = document.createElement('button');
      btn.type = 'button'; btn.textContent = label; btn.disabled = disabled;
      if (current) btn.setAttribute('aria-current', 'page');
      btn.addEventListener('click', () => {
        currentPage = page; render();
        els.count.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      els.pagination.appendChild(btn);
    };
    makeButton('‹ Previous', currentPage - 1, currentPage === 1, false);
    const shown = new Set([1, pages]);
    for (let n = currentPage - 2; n <= currentPage + 2; n++) if (n > 0 && n <= pages) shown.add(n);
    let last = 0;
    for (const page of [...shown].sort((a, b) => a - b)) {
      if (last && page - last > 1) addText(els.pagination, 'span', '…');
      makeButton(String(page), page, false, page === currentPage); last = page;
    }
    makeButton('Next ›', currentPage + 1, currentPage === pages, false);
  }

  function csvEscape(v) {
    let value = String(v == null ? '' : v);
    // Prevent spreadsheet applications evaluating untrusted text as a formula.
    if (/^[=+@\-]/.test(value)) value = "'" + value;
    return '"' + value.replace(/"/g, '""') + '"';
  }
  function bibEscape(value) {
    return String(value || '').replace(/\\/g, '\\textbackslash{}')
      .replace(/([{}%&#_$])/g, '\\$1').replace(/~/g, '\\textasciitilde{}')
      .replace(/\^/g, '\\textasciicircum{}');
  }
  function bibEntry(p) {
    const type = ['article', 'inproceedings', 'incollection', 'book', 'phdthesis', 'mastersthesis', 'proceedings'].includes(p.type) ? p.type : 'misc';
    const key = (p.key || p.identity).replace(/[^a-zA-Z0-9_:-]/g, '_');
    const fields = [
      ['title', p.title], ['author', p.authors.join(' and ')], ['year', p.year || ''],
      [type === 'article' ? 'journal' : 'booktitle', p.venue],
      ['volume', p.volume], ['number', p.number], ['pages', p.pages], ['publisher', p.publisher], ['doi', p.doi], ['url', p.url]
    ].filter(([, v]) => String(v).length > 0);
    return '@' + type + '{' + key + ',\n' + fields.map(([k, v]) => '  ' + k + ' = {' + bibEscape(v) + '}').join(',\n') + '\n}';
  }
  function download() {
    const allSorted = [...publications].sort((a, b) => b.year - a.year || a.title.localeCompare(b.title));
    const records = els.scope.value === 'filtered' ? filtered : allSorted;
    if (!records.length) { setStatus('No records to export.', true); return; }
    const format = els.format.value;
    const rows = records.map((p) => ({
      key: p.key, year: p.year, title: p.title, authors: p.authors.join('; '),
      venue: p.venue, type: p.type, doi: p.doi, dblp_url: p.url,
      full_text_url: p.edition, listed_researchers: p.sourceIds.map((pid) => PEOPLE.find((a) => a.pid === pid)?.name || pid).join('; ')
    }));
    let content, mime, extension;
    if (format === 'json') {
      content = JSON.stringify(rows, null, 2); mime = 'application/json;charset=utf-8'; extension = 'json';
    } else if (format === 'bib') {
      content = records.map(bibEntry).join('\n\n') + '\n'; mime = 'application/x-bibtex;charset=utf-8'; extension = 'bib';
    } else {
      const headers = Object.keys(rows[0]);
      content = '\uFEFF' + headers.map(csvEscape).join(',') + '\r\n' +
        rows.map((r) => headers.map((h) => csvEscape(r[h])).join(',')).join('\r\n');
      mime = 'text/csv;charset=utf-8'; extension = 'csv';
    }
    const blob = new Blob([content], { type: mime });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'dblp-publications-' + els.scope.value + '.' + extension;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 30000);
  }

  let debounce;
  for (const field of [els.topic, els.venue, els.from, els.to, els.author, els.coauthor, els.sort]) {
    field.addEventListener(field.tagName === 'SELECT' ? 'change' : 'input', () => {
      clearTimeout(debounce); debounce = setTimeout(applyFilters, 180);
    });
  }
  els.reset.addEventListener('click', () => {
    for (const field of [els.topic, els.venue, els.from, els.to, els.coauthor]) field.value = '';
    els.author.value = ''; els.sort.value = 'newest'; applyFilters();
  });
  els.refresh.addEventListener('click', () => load(true));
  els.export.addEventListener('click', download);
  load(false);
})();
