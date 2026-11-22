
#!/usr/bin/env python3
"""
Genera e aggiorna le pagine individuali dei seminari ISISLab.

- Supporta date DD-MM-YYYY, DD/MM/YYYY e YYYY-MM-DD.
- Riconosce le pagine storiche tramite data e titolo.
- Conserva gli slug e i permalink storici.
- Genera automaticamente le pagine nuove.
- Aggiorna soltanto i metadati esplicitamente forniti nel YAML.
- Mantiene la compatibilità con il vecchio campo time.
- Non converte automaticamente time in start_time.
- Non sostituisce le locandine storiche con immagini predefinite.
- Conserva i metadati non gestiti dal generatore.
- Crea backup soltanto prima di modifiche effettive.
- Utilizza scrittura atomica dei file.
"""

from pathlib import Path
from collections import defaultdict
from datetime import date, datetime
import argparse
import html
import os
import re
import shutil
import tempfile
import unicodedata

import yaml


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "_data" / "seminars-nolink.yml"
OUTPUT = ROOT / "seminar-articles"
SLUGS_FILE = ROOT / "_data" / "seminar-slugs.yml"
BACKUP_DIR = ROOT / ".seminar-page-backups"


# ============================================================
# DATE
# ============================================================

def normalize_date(value):
    """Normalizza le date in YYYY-MM-DD."""

    if isinstance(value, (date, datetime)):
        return value.strftime("%Y-%m-%d")

    value = str(value or "").strip()

    for fmt in (
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%Y-%m-%d",
    ):
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    raise ValueError(f"Data non riconosciuta: {value}")


def display_date(value):
    """Restituisce la data nel formato italiano DD-MM-YYYY."""

    if isinstance(value, (date, datetime)):
        return value.strftime("%d-%m-%Y")

    return str(value or "").strip()


# ============================================================
# TITOLI E SLUG
# ============================================================

def normalize_title(value):
    value = html.unescape(str(value or ""))
    value = unicodedata.normalize("NFKC", value).lower()

    return "".join(
        char for char in value
        if char.isalnum()
    )


def normalize_display_text(value):
    """
    Normalizza gli spazi per confrontare i titoli.

    Due o più spazi consecutivi non devono provocare
    aggiornamenti inutili delle pagine storiche.
    """

    value = html.unescape(str(value or ""))
    return re.sub(r"\s+", " ", value).strip()


def slugify(value):
    value = unicodedata.normalize("NFKD", str(value))
    value = value.encode("ascii", "ignore").decode().lower()

    value = re.sub(r"[^a-z0-9]+", "-", value)

    return re.sub(r"-+", "-", value).strip("-")


def time_for_slug(item):
    """
    Estrae l'orario iniziale per costruire lo slug.
    start_time ha priorità sul vecchio campo time.
    """

    value = item.get("start_time") or item.get("time") or ""

    match = re.search(
        r"(?<!\d)(\d{1,2})[:.](\d{2})(?!\d)",
        str(value)
    )

    if not match:
        return ""

    return f"{int(match.group(1)):02d}{match.group(2)}"


# ============================================================
# UTILITA'
# ============================================================

def has_value(value):
    """Verifica che un campo YAML sia effettivamente valorizzato."""

    if value is None:
        return False

    if isinstance(value, str):
        return bool(value.strip())

    if isinstance(value, (list, dict)):
        return bool(value)

    return True


def is_default_image(value):
    """
    Riconosce le immagini generiche predefinite.

    Non devono sostituire le locandine o le immagini storiche.
    """

    if not has_value(value):
        return False

    normalized = str(value).replace("\\", "/").strip().rstrip("/")
    filename = normalized.split("/")[-1].lower()

    return filename in {
        "default.png",
        "default.jpg",
        "default.jpeg",
    }


# ============================================================
# FRONT MATTER
# ============================================================

FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)",
    re.S
)


def split_frontmatter(content):
    match = FRONTMATTER_RE.match(content)

    if not match:
        raise ValueError("Front matter Markdown non riconosciuto.")

    metadata = yaml.safe_load(match.group(1)) or {}
    body = content[match.end():]

    if not isinstance(metadata, dict):
        raise ValueError("Front matter non valido.")

    return metadata, body


def render_page(metadata, body):
    frontmatter = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        sort_keys=False,
        width=120
    ).rstrip()

    return f"---\n{frontmatter}\n---\n{body}"


# ============================================================
# SCRITTURA ATOMICA
# ============================================================

def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)

    temporary_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False
        ) as stream:

            temporary_path = Path(stream.name)

            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())

        os.replace(temporary_path, path)

    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()


# ============================================================
# LETTURA PAGINE STORICHE
# ============================================================

def read_historical_pages():
    pages = defaultdict(list)

    for path in sorted(OUTPUT.glob("*.md")):

        content = path.read_text(encoding="utf-8")

        try:
            metadata, _ = split_frontmatter(content)

            title = normalize_title(metadata.get("title"))
            seminar_date = normalize_date(metadata.get("date"))
            permalink = metadata.get("permalink")

        except (ValueError, yaml.YAMLError) as error:

            print(f"ATTENZIONE: pagina non riconosciuta: {path.name}")
            print(f"  Motivo: {error}")

            continue

        if not title or not permalink:
            continue

        pages[(seminar_date, title)].append(permalink)

    return pages


def permalink_to_slug(permalink):
    match = re.search(
        r"/seminars/([^/]+)/?",
        str(permalink)
    )

    if not match:
        raise ValueError(f"Permalink non valido: {permalink}")

    return match.group(1)


# ============================================================
# METADATI
# ============================================================

def build_seminar_metadata(item, seminar_date):
    """
    Costruisce i metadati del seminario.

    I campi opzionali vengono inclusi solo se presenti
    e valorizzati nel YAML.

    Il vecchio campo time rimane time:
    non viene trasformato automaticamente in start_time.
    """

    metadata = {
        "layout": "seminar-detail",
        "article_kind": "seminar",
        "lang": "it",
        "title": item.get("title", ""),
        "date": seminar_date,
        "date_display": display_date(item.get("date")),
    }

    # Nuovo modello: start_time.
    if has_value(item.get("start_time")):
        metadata["start_time"] = item["start_time"]

    # Modello storico: time.
    elif has_value(item.get("time")):
        metadata["time"] = item["time"]

    optional_fields = {
        "end_time": item.get("end_time"),
        "location": item.get("venue") or item.get("location"),
        "speakers": item.get("speakers"),
        "seminar_image": item.get("image") or item.get("seminar_image"),
    }

    for key, value in optional_fields.items():
        if has_value(value):
            metadata[key] = value

    return metadata


def metadata_value_equal(key, current, expected):
    """Confronto intelligente dei metadati."""

    if key == "date":
        try:
            return normalize_date(current) == normalize_date(expected)
        except ValueError:
            return current == expected

    if key == "title":
        return (
            normalize_display_text(current)
            == normalize_display_text(expected)
        )

    return current == expected


# ============================================================
# CREAZIONE NUOVE PAGINE
# ============================================================

def create_new_page(item, seminar_date, slug, apply=False):

    metadata = build_seminar_metadata(item, seminar_date)

    metadata["permalink"] = f"/seminars/{slug}/"

    body = str(item.get("description") or "").strip()

    if body:
        body = "\n" + body + "\n"
    else:
        body = "\n"

    target = OUTPUT / f"{slug}.md"
    content = render_page(metadata, body)

    if apply:

        if target.exists():
            raise FileExistsError(
                f"La pagina esiste già: {target}"
            )

        atomic_write(target, content)

        print(f"PAGINA CREATA: {target.name}")

    else:
        print(f"DA CREARE: {target.name}")


# ============================================================
# AGGIORNAMENTO PAGINE ESISTENTI
# ============================================================

def update_existing_page(item, slug, apply=False):

    target = OUTPUT / f"{slug}.md"

    if not target.exists():
        raise FileNotFoundError(
            f"Pagina associata al permalink non trovata: {target}"
        )

    original = target.read_text(encoding="utf-8")

    metadata, old_body = split_frontmatter(original)

    seminar_date = normalize_date(item.get("date"))

    expected_metadata = build_seminar_metadata(
        item,
        seminar_date
    )

    updated_metadata = metadata.copy()
    changes = []

    # --------------------------------------------------------
    # CONFRONTO METADATI
    # --------------------------------------------------------

    for key, expected_value in expected_metadata.items():

        # Un'immagine predefinita non deve sostituire
        # una locandina o un dato storico.
        if key == "seminar_image" and is_default_image(expected_value):
            continue

        current_value = metadata.get(key)

        if not metadata_value_equal(
            key,
            current_value,
            expected_value
        ):

            updated_metadata[key] = expected_value
            changes.append(key)

    # --------------------------------------------------------
    # CONFRONTO DESCRIZIONE
    # --------------------------------------------------------

    new_body = str(item.get("description") or "").strip()

    if new_body and old_body.strip() != new_body:

        updated_body = "\n" + new_body + "\n"
        changes.append("description")

    else:
        # Una descrizione vuota non cancella il testo storico.
        updated_body = old_body

    # --------------------------------------------------------
    # NESSUNA MODIFICA
    # --------------------------------------------------------

    if not changes:

        print(f"GIA' AGGIORNATA: {target.name}")

        return "unchanged", None

    # --------------------------------------------------------
    # SIMULAZIONE
    # --------------------------------------------------------

    if not apply:

        print(
            f"DA AGGIORNARE: {target.name} "
            f"(campi: {', '.join(changes)})"
        )

        return "updated", None

    # --------------------------------------------------------
    # BACKUP SOLO PRIMA DI MODIFICHE REALI
    # --------------------------------------------------------

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d-%H%M%S-%f"
    )

    backup = BACKUP_DIR / f"{target.stem}-{timestamp}.md"

    shutil.copy2(target, backup)

    # --------------------------------------------------------
    # SCRITTURA AGGIORNAMENTO
    # --------------------------------------------------------

    updated_content = render_page(
        updated_metadata,
        updated_body
    )

    atomic_write(target, updated_content)

    print(f"PAGINA AGGIORNATA: {target.name}")
    print(f"  Campi modificati: {', '.join(changes)}")
    print(f"  Backup creato: {backup.relative_to(ROOT)}")
    print(
        f"  Permalink conservato: {metadata.get('permalink')}"
    )

    return "updated", backup


# ============================================================
# PROGRAMMA PRINCIPALE
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Genera e aggiorna le pagine individuali dei seminari."
        )
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Applica le modifiche. Senza questa opzione esegue una simulazione."
    )

    args = parser.parse_args()

    if not DATA.exists():
        raise FileNotFoundError(
            f"File YAML non trovato: {DATA}"
        )

    seminars = yaml.safe_load(
        DATA.read_text(encoding="utf-8")
    ) or []

    if not isinstance(seminars, list):
        raise ValueError(
            "Il file seminars-nolink.yml deve contenere una lista."
        )

    # Validazione preliminare di tutti i record.
    for index, item in enumerate(seminars):

        if not isinstance(item, dict):
            raise ValueError(
                f"Record non valido alla posizione {index}."
            )

        normalize_date(item.get("date"))

        if not normalize_title(item.get("title")):
            raise ValueError(
                f"Titolo vuoto alla posizione {index}."
            )

    OUTPUT.mkdir(parents=True, exist_ok=True)

    historical_pages = read_historical_pages()

    used_slugs = {
        permalink_to_slug(permalink)
        for page_list in historical_pages.values()
        for permalink in page_list
    }

    generated_slugs = []
    consumed = defaultdict(int)

    historical_count = 0
    created_count = 0
    updated_count = 0
    unchanged_count = 0
    skipped_count = 0

    backups_created = []

    print("\n========== MODALITA' ==========")
    print(
        "APPLICAZIONE MODIFICHE"
        if args.apply
        else "SIMULAZIONE - NESSUNA MODIFICA"
    )

    # --------------------------------------------------------
    # ELABORAZIONE SEMINARI
    # --------------------------------------------------------

    for item in seminars:

        seminar_date = normalize_date(item.get("date"))
        title_key = normalize_title(item.get("title"))

        key = (seminar_date, title_key)

        matches = historical_pages.get(key, [])
        match_index = consumed[key]

        # Pagina storica o già generata.
        if match_index < len(matches):

            permalink = matches[match_index]

            consumed[key] += 1

            slug = permalink_to_slug(permalink)

            historical_count += 1

            result, backup = update_existing_page(
                item,
                slug,
                apply=args.apply
            )

            if result == "updated":
                updated_count += 1

            elif result == "unchanged":
                unchanged_count += 1

            else:
                skipped_count += 1

            if backup is not None:
                backups_created.append(backup)

        # Nuovo seminario.
        else:

            title_part = slugify(
                item.get("title", "")
            )[:65].rstrip("-")

            time_part = time_for_slug(item)

            base = f"{title_part}-{seminar_date}"

            if time_part:
                base += f"-{time_part}"

            slug = base
            suffix = 2

            while (
                slug in used_slugs
                or (OUTPUT / f"{slug}.md").exists()
            ):

                slug = f"{base}-{suffix}"
                suffix += 1

            used_slugs.add(slug)

            create_new_page(
                item,
                seminar_date,
                slug,
                apply=args.apply
            )

            created_count += 1

        generated_slugs.append(slug)

    # --------------------------------------------------------
    # AGGIORNAMENTO SLUG CANONICI
    # --------------------------------------------------------

    if args.apply:

        slugs_content = yaml.safe_dump(
            generated_slugs,
            allow_unicode=True,
            sort_keys=False
        )

        atomic_write(
            SLUGS_FILE,
            slugs_content
        )

    # --------------------------------------------------------
    # RIEPILOGO
    # --------------------------------------------------------

    print("\n========== RISULTATO ==========")

    print(f"Record YAML: {len(seminars)}")
    print(f"Seminari storici riconosciuti: {historical_count}")
    print(f"Pagine da creare / create: {created_count}")
    print(f"Pagine da aggiornare / aggiornate: {updated_count}")
    print(f"Pagine già aggiornate: {unchanged_count}")
    print(f"Aggiornamenti saltati: {skipped_count}")
    print(f"Slug generati: {len(generated_slugs)}")

    if args.apply:

        print(f"File slug: {SLUGS_FILE}")
        print(f"Backup creati: {len(backups_created)}")

        for backup in backups_created:
            print(f"  {backup.relative_to(ROOT)}")

    else:

        print("\nNessuna modifica effettuata.")
        print("Per applicare le modifiche, usare --apply.")


if __name__ == "__main__":
    main()
