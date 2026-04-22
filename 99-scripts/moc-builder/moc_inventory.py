"""MOC Builder — Phase 1: Inventory.

Scans the permanent-note corpus and emits a JSON manifest containing the
frontmatter fields and outgoing wiki-links needed by Phase 2 clustering.

Usage:
    python 99-scripts/moc-builder/moc_inventory.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

VAULT = Path(r"D:\10_pur3v4d3r's-vault")
NOTES_DIR = VAULT / "999-report-organizing" / "_permanent-notes" / "llm-generated-permanent-notes"
OUT_DIR = VAULT / "999-report-organizing" / "_maps-of-content-for-permenent-notes"
OUT_FILE = OUT_DIR / "_inventory.json"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
FM_DELIM = "---"


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith(FM_DELIM):
        return {}
    try:
        end = text.index("\n" + FM_DELIM, len(FM_DELIM))
    except ValueError:
        return {}
    try:
        data = yaml.safe_load(text[len(FM_DELIM) : end])
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def main() -> int:
    if not NOTES_DIR.exists():
        print(f"ERROR: notes dir not found: {NOTES_DIR}")
        return 2
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, Any]] = []
    for note in sorted(NOTES_DIR.glob("*.md")):
        try:
            text = note.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            print(f"WARN: skip {note.name}: {exc}")
            continue
        fm = parse_frontmatter(text)
        outlinks = sorted(set(WIKILINK_RE.findall(text)))
        tags = fm.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        manifest.append(
            {
                "filename": note.stem,
                "wikilink": f"[[{note.stem}]]",
                "title": fm.get("title", note.stem),
                "domain": fm.get("domain"),
                "tags": tags,
                "status": fm.get("status"),
                "type": fm.get("type"),
                "referenced_by_count": fm.get("referenced-by-count", 0),
                "outlinks": outlinks,
                "outlink_count": len(outlinks),
                "size_bytes": note.stat().st_size,
            }
        )

    OUT_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Inventoried {len(manifest)} notes -> {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
