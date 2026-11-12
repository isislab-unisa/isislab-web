#!/usr/bin/env python3
"""Merge dblp publications into a Jekyll-friendly JSON file.

Python stdlib only. All requests happen in GitHub Actions, never in browsers.

Default: use the independently hosted dblp SPARQL service, not the XML
endpoints that may return an interactive anti-bot challenge (HTTP 202).
For offline testing, supply --fixture-dir pointing to downloaded XML files.

Stops on an author download or parsing error rather than publishing partial data.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import gzip
import html.entities
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

PEOPLE = [
    {"pid": "71/11144", "name": "Carmine Spagnuolo"},
    {"pid": "224/0266", "name": "Maria Angela Pellegrino"},
    {"pid": "32/6668", "name": "Vittorio Scarano"},
    {"pid": "26/4019", "name": "Gennaro Cordasco"},
    {"pid": "07/527", "name": "Biagio Cosenza"},
]

USER_AGENT = "Jekyll-dblp-publications/2.0 (public SPARQL bibliography updater)"
SPARQL_ENDPOINT = "https://qlever.dev/api/dblp"
SPARQL_PAGE_SIZE = 2000
SPARQL_MAX_PAGES = 100
# Legacy optional XML mode; these websites may return an HTML anti-bot challenge.
# The default SPARQL mode does not request these endpoints.
XML_HOSTS = ("https://dblp.org", "https://dblp.uni-trier.de")
MAX_RESPONSE_BYTES = 20 * 1024 * 1024  # Guard against unexpected/huge responses.
REPO_ROOT = Path(__file__).resolve().parents[1]


def text(node: ET.Element | None) -> str:
    """Return plain text, including nested inline markup in publication titles."""
    if node is None:
        return ""
    return re.sub(r"\s+", " ", "".join(node.itertext())).strip()


def field(record: ET.Element, tag: str) -> str:
    return text(record.find(tag))


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    return re.sub(r"\s+", " ", value.casefold()).strip()


def safe_link(value: str) -> str:
    return value if value.startswith(("https://", "http://")) else ""


def response_preview(data: bytes, limit: int = 160) -> str:
    """Render a short, safe diagnostic for unexpected server responses."""
    return repr(data[:limit].decode("utf-8", errors="replace"))


def unpack_xml_response(data: bytes, *, url: str, status: int, content_type: str,
                        content_encoding: str) -> bytes:
    """Detect HTTP error pages and handle servers returning gzip XML."""
    if not data:
        raise ValueError(f"Empty response (HTTP {status}; Content-Type: {content_type}) from {url}")
    if data[:2] == b"\x1f\x8b" or "gzip" in content_encoding.lower():
        try:
            data = gzip.decompress(data)
        except (OSError, EOFError) as exc:
            raise ValueError(f"Corrupt gzip body from {url}: {exc}") from exc
    if len(data) > MAX_RESPONSE_BYTES:
        raise ValueError(f"Response from {url} exceeds {MAX_RESPONSE_BYTES} bytes")
    # Also accept UTF-8/UTF-16 BOMs, although dblp normally serves UTF-8 XML.
    cleaned = data.lstrip(b" \t\r\n\xef\xbb\xbf")
    if not (cleaned.startswith(b"<") or data.startswith((b"\xff\xfe", b"\xfe\xff"))):
        raise ValueError(
            f"Non-XML response from {url} (HTTP {status}; Content-Type: {content_type}). "
            f"First bytes: {response_preview(data)}"
        )
    if "text/html" in content_type.lower() or cleaned[:80].lower().startswith((b"<html", b"<!doctype html")):
        raise ValueError(
            f"HTML instead of XML from {url} (HTTP {status}; Content-Type: {content_type}). "
            f"First bytes: {response_preview(data)}"
        )
    return data


def fetch_person_xml(pid: str, fixture_dir: Path | None = None,
                     hosts: tuple[str, ...] = XML_HOSTS) -> bytes:
    if fixture_dir is not None:
        return (fixture_dir / (pid.replace("/", "_") + ".xml")).read_bytes()
    errors: list[str] = []
    for host in hosts:
        url = f"{host.rstrip('/')}/pid/{pid}.xml"
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/xml, text/xml;q=0.9",
                "Accept-Encoding": "identity",
            },
        )
        for attempt in range(3):
            try:
                print(f"Fetching {url} (attempt {attempt + 1}/3)", flush=True)
                with urllib.request.urlopen(request, timeout=45) as response:
                    status = response.status or 200
                    content_type = response.headers.get("Content-Type", "unknown")
                    content_encoding = response.headers.get("Content-Encoding", "")
                    data = response.read(MAX_RESPONSE_BYTES + 1)
                    data = unpack_xml_response(
                        data, url=url, status=status, content_type=content_type,
                        content_encoding=content_encoding,
                    )
                    print(f"  HTTP {status} · {content_type} · {len(data)} bytes", flush=True)
                    return data
            except urllib.error.HTTPError as exc:
                reason = f"HTTP {exc.code} {exc.reason} from {url}"
                errors.append(reason)
                # No point retrying a stable 4xx except throttling/temporary outage.
                retryable = exc.code in (408, 429, 500, 502, 503, 504)
                if not retryable:
                    break
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
                errors.append(str(exc))
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(
        f"Could not download valid XML for PID {pid}. "
        f"Tried both dblp hosts. Last errors: {' | '.join(errors[-4:])}"
    )


# Standard XML parsers do not automatically download/resolve dblp's external DTD.
# Convert well-known named HTML/XML entities such as &uuml; to XML numeric references,
# leaving the five built-in XML entities and numeric entities unchanged.
NAMED_ENTITY = re.compile(rb"&([A-Za-z][A-Za-z0-9._:-]*);")
XML_BUILTIN = {"amp", "lt", "gt", "quot", "apos"}


def expand_named_entities(data: bytes, pid: str) -> bytes:
    def replace(match: re.Match[bytes]) -> bytes:
        name = match.group(1).decode("ascii")
        if name in XML_BUILTIN:
            return match.group(0)
        characters = html.entities.html5.get(name + ";")
        if characters is None:
            raise ValueError(f"Unknown XML entity &{name}; in PID {pid} export")
        return "".join(f"&#{ord(char)};" for char in characters).encode("ascii")
    return NAMED_ENTITY.sub(replace, data)


def make_publication(record: ET.Element) -> dict | None:
    kind = record.tag
    if kind == "www":  # homepage records are not research publications
        return None
    title = field(record, "title")
    if not title:
        return None
    key = record.get("key", "").strip()
    authors = [text(author) for author in record.findall("author")]
    authors = [a for a in authors if a]
    if not authors:
        authors = [text(editor) for editor in record.findall("editor") if text(editor)]
    raw_year = field(record, "year")
    year = int(raw_year) if raw_year.isdigit() else 0
    venue = next((field(record, tag) for tag in ("journal", "booktitle", "school", "publisher") if field(record, tag)), "")
    edition_urls = [safe_link(text(ee)) for ee in record.findall("ee")]
    edition = next((url for url in edition_urls if url), "")
    doi = field(record, "doi")
    if not doi:
        for url in edition_urls:
            match = re.match(r"^https?://(?:dx\.)?doi\.org/(.+)$", url, re.I)
            if match:
                doi = match.group(1)
                break
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    if not key:
        # Older or unusual records lacking a dblp key still get deterministic IDs.
        seed = normalize(title) + "|" + raw_year + "|" + normalize(venue)
        key = "derived/" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:20]
    record_url = "https://dblp.org/rec/" + key
    return {
        "key": key,
        "title": title,
        "year": year,
        "authors": authors,
        "venue": venue,
        "type": kind,
        "doi": doi,
        "url": record_url,
        "edition": edition,
        "pages": field(record, "pages"),
        "volume": field(record, "volume"),
        "number": field(record, "number"),
        "publisher": field(record, "publisher"),
        "sourceIds": [],
    }


def parse_person_xml(data: bytes, pid: str) -> list[dict]:
    try:
        root = ET.fromstring(expand_named_entities(data, pid))
    except ET.ParseError as exc:
        raise ValueError(
            f"Invalid XML from dblp for PID {pid}: {exc}. "
            f"First bytes: {response_preview(data)}. "
            "A proxy, rate limit, or error page may have replaced the XML."
        ) from exc
    if root.tag != "dblpperson":
        raise ValueError(f"Unexpected XML root for {pid}: {root.tag}")
    if root.get("pid") and root.get("pid") != pid:
        raise ValueError(f"PID mismatch: asked for {pid}, got {root.get('pid')}")
    publications = []
    for item in root.findall("r"):
        if len(item) == 0:
            continue
        publication = make_publication(item[0])
        if publication:
            publication["sourceIds"].append(pid)
            publications.append(publication)
    if not publications:
        raise ValueError(f"No publication records found for {pid}; refusing incomplete update")
    return publications


def sparql_query(pid: str, limit: int = SPARQL_PAGE_SIZE, offset: int = 0) -> str:
    """Query dblp's RDF graph using a permanent *person PID*, never name matching.

    Return one row per creator per publication. We page the RDF query itself,
    independently of the 20-publications-per-page browser display.
    """
    if pid not in {p["pid"] for p in PEOPLE}:
        raise ValueError("Unexpected PID")
    return f"""PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT ?publication ?title ?year ?legacyVenue ?streamName ?bibtype ?doi
       ?edition ?pages ?volume ?issue ?number ?publisher ?creatorName
WHERE {{
  ?publication (dblp:authoredBy|dblp:editedBy) <https://dblp.org/pid/{pid}> .
  ?publication dblp:title ?title .
  OPTIONAL {{
    ?publication (dblp:authoredBy|dblp:editedBy) ?creator .
    OPTIONAL {{ ?creator dblp:primaryCreatorName ?creatorName . }}
  }}
  OPTIONAL {{ ?publication dblp:yearOfPublication ?year . }}
  OPTIONAL {{ ?publication dblp:publishedIn ?legacyVenue . }}
  OPTIONAL {{
    ?publication dblp:publishedInStream ?stream .
    ?stream dblp:primaryStreamTitle ?streamName .
  }}
  OPTIONAL {{ ?publication dblp:bibtexType ?bibtype . }}
  OPTIONAL {{ ?publication dblp:doi ?doi . }}
  OPTIONAL {{ ?publication dblp:primaryDocumentPage ?edition . }}
  OPTIONAL {{ ?publication dblp:pagination ?pages . }}
  OPTIONAL {{ ?publication dblp:publishedInJournalVolume ?volume . }}
  OPTIONAL {{ ?publication dblp:publishedInJournalVolumeIssue ?issue . }}
  OPTIONAL {{ ?publication dblp:publicationNumber ?number . }}
  OPTIONAL {{ ?publication dblp:publishedBy ?publisher . }}
}}
ORDER BY ?publication ?creatorName
LIMIT {limit}
OFFSET {offset}"""


def parse_sparql_response(data: bytes, endpoint: str) -> list[dict]:
    """Read SPARQL 1.1 results, rejecting error/challenge HTML."""
    if not data or data.lstrip()[:1] not in (b"{",):
        raise ValueError(
            f"SPARQL endpoint {endpoint} returned non-JSON (possibly an anti-bot "
            f"challenge): {response_preview(data)}"
        )
    try:
        payload = json.loads(data)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Invalid SPARQL JSON from {endpoint}: {exc}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), dict):
        raise ValueError(f"Unexpected SPARQL response structure from {endpoint}")
    bindings = payload["results"].get("bindings")
    if not isinstance(bindings, list):
        raise ValueError(f"No bindings array in SPARQL response from {endpoint}")
    for row in bindings:
        if not isinstance(row, dict) or "publication" not in row or "title" not in row:
            raise ValueError(f"Incomplete SPARQL result from {endpoint}")
    return bindings


def sparql_value(row: dict, key: str) -> str:
    item = row.get(key)
    return str(item.get("value", "")).strip() if isinstance(item, dict) else ""


def sparql_request(endpoint: str, query: str) -> list[dict]:
    """One polite query, with bounded retries only for transient failures."""
    req = urllib.request.Request(
        endpoint, data=query.encode("utf-8"), method="POST",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/sparql-results+json",
            "Content-Type": "application/sparql-query; charset=utf-8",
            "Accept-Encoding": "identity",
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                status = getattr(response, "status", 200)
                ctype = response.headers.get("Content-Type", "")
                raw = response.read(MAX_RESPONSE_BYTES + 1)
                if len(raw) > MAX_RESPONSE_BYTES:
                    raise ValueError("SPARQL response exceeds maximum size")
                if status == 202 or "text/html" in ctype.lower():
                    raise ValueError(
                        f"SPARQL endpoint returned a challenge/error page: "
                        f"HTTP {status}, Content-Type={ctype}: {response_preview(raw)}"
                    )
                return parse_sparql_response(raw, endpoint)
        except urllib.error.HTTPError as exc:
            if exc.code not in (408, 429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError(f"SPARQL HTTP {exc.code} from {endpoint}") from exc
            retry_after = exc.headers.get("Retry-After", "")
            delay = min(60, int(retry_after)) if retry_after.isdigit() else 3 * (attempt + 1)
            print(f"  HTTP {exc.code}; waiting {delay}s", flush=True)
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 2:
                raise RuntimeError(f"SPARQL connection failed at {endpoint}: {exc}") from exc
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("SPARQL download failed")


def parse_sparql_papers(rows: list[dict], pid: str) -> list[dict]:
    papers: dict[str, dict] = {}
    for row in rows:
        iri = sparql_value(row, "publication")
        prefix = "https://dblp.org/rec/"
        if not iri.startswith(prefix):
            # Bibliographic resource IRIs have a persistent /rec/<key> identifier.
            raise ValueError(f"Unrecognized dblp publication IRI: {iri[:120]}")
        key = urllib.parse.unquote(iri[len(prefix):])
        title = sparql_value(row, "title")
        year_text = sparql_value(row, "year")
        year = int(year_text[:4]) if re.match(r"^\d{4}", year_text) else 0
        type_iri = sparql_value(row, "bibtype")
        kind = type_iri.rsplit("/", 1)[-1].rsplit("#", 1)[-1].lower()
        if kind not in {"article", "inproceedings", "incollection", "book", "proceedings", "phdthesis", "mastersthesis"}:
            kind = "misc"
        doi = sparql_value(row, "doi")
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
        paper = papers.setdefault(key, {
            "key": key,
            "title": title,
            "year": year,
            "authors": [],
            "venue": sparql_value(row, "legacyVenue") or sparql_value(row, "streamName"),
            "type": kind,
            "doi": doi,
            "url": iri,
            "edition": safe_link(sparql_value(row, "edition")),
            "pages": sparql_value(row, "pages"),
            "volume": sparql_value(row, "volume"),
            "number": sparql_value(row, "issue") or sparql_value(row, "number"),
            "publisher": sparql_value(row, "publisher"),
            "sourceIds": [pid],
        })
        author = sparql_value(row, "creatorName")
        if author and author not in paper["authors"]:
            paper["authors"].append(author)
        # Multiple rows can have different optional metadata values.
        for fld, binding in (("venue", "legacyVenue"), ("venue", "streamName"),
                             ("doi", "doi"), ("edition", "edition"),
                             ("pages", "pages"), ("volume", "volume"),
                             ("number", "issue"), ("number", "number"),
                             ("publisher", "publisher")):
            if not paper[fld] and sparql_value(row, binding):
                value = sparql_value(row, binding)
                if fld == "doi":
                    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.I)
                elif fld == "edition":
                    value = safe_link(value)
                paper[fld] = value
    if not papers:
        raise ValueError(f"No publications from SPARQL for {pid}")
    return list(papers.values())


def fetch_person_sparql(pid: str, endpoint: str = SPARQL_ENDPOINT) -> list[dict]:
    all_rows = []
    for page in range(SPARQL_MAX_PAGES):
        offset = page * SPARQL_PAGE_SIZE
        print(f"Fetching dblp SPARQL {pid}: rows {offset}–{offset + SPARQL_PAGE_SIZE - 1}", flush=True)
        rows = sparql_request(endpoint, sparql_query(pid, offset=offset))
        all_rows.extend(rows)
        if len(rows) < SPARQL_PAGE_SIZE:
            return parse_sparql_papers(all_rows, pid)
        time.sleep(1.5)
    raise RuntimeError(f"Result cap reached for PID {pid}; refusing to publish incomplete bibliography")


def aggregate(fixture_dir: Path | None = None, *, source: str = "sparql",
              endpoint: str = SPARQL_ENDPOINT) -> dict:
    combined: dict[str, dict] = {}
    contributors = []
    for person in PEOPLE:
        pid = person["pid"]
        try:
            records = (parse_person_xml(fetch_person_xml(pid, fixture_dir), pid)
                       if fixture_dir or source == "xml"
                       else fetch_person_sparql(pid, endpoint))
        except Exception as exc:
            raise RuntimeError(f"{person['name']} ({pid}): {exc}") from exc
        contributors.append({**person, "count": len(records)})
        for paper in records:
            key = paper["key"]
            if key not in combined:
                combined[key] = paper
            else:
                existing = combined[key]
                if pid not in existing["sourceIds"]:
                    existing["sourceIds"].append(pid)
                for fld in ("title", "venue", "doi", "edition", "pages", "volume", "number", "publisher"):
                    if not existing[fld] and paper[fld]:
                        existing[fld] = paper[fld]
                if len(paper["authors"]) > len(existing["authors"]):
                    existing["authors"] = paper["authors"]
        print(f"{person['name']}: {len(records)} publication records", flush=True)

    for paper in combined.values():
        paper["sourceIds"].sort(key=lambda pid: next(i for i, p in enumerate(PEOPLE) if p["pid"] == pid))
    publications = sorted(combined.values(), key=lambda p: (-p["year"], p["title"].casefold(), p["key"]))
    if not publications:
        raise ValueError("No publications, refusing to overwrite cache")
    return {"source": "dblp", "people": contributors, "total": len(publications), "publications": publications}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "assets/data/dblp-publications.json")
    parser.add_argument("--fixture-dir", type=Path, help="Offline XML files named <PID-with-underscores>.xml")
    parser.add_argument("--source", choices=("sparql", "xml"), default="sparql",
                        help="Default: public SPARQL graph; xml source may be blocked by a bot challenge")
    parser.add_argument("--endpoint", default=SPARQL_ENDPOINT,
                        help="SPARQL endpoint URL (default: QLever public dblp endpoint)")
    args = parser.parse_args()
    try:
        result = aggregate(args.fixture_dir, source=args.source, endpoint=args.endpoint)
        if args.output.exists():
            previous = json.loads(args.output.read_text(encoding="utf-8"))
            previous_data = {k: v for k, v in previous.items() if k != "generated_at"}
            if previous_data == result:
                print(f"No bibliographic changes; keeping {args.output} unchanged")
                return 0
        result["generated_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        temporary = args.output.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(args.output)
        print(f"Wrote {result['total']} unique publications to {args.output}")
        return 0
    except Exception as error:
        print(f"Update failed; existing data left untouched: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
