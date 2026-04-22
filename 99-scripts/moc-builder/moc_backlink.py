"""MOC Builder — Phase 5: Back-linking.

For each generated MOC file, ensures every wiki-linked permanent note has the
MOC declared in its frontmatter `parent-moc` list. Idempotent.

Usage:
    python 99-scripts/moc-builder/moc_backlink.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

VAULT = Path(r"D:\10_pur3v4d3r's-vault")
MOC_DIR = VAULT / "999-report-organizing" / "_maps-of-content-for-permenent-notes"
NOTES_DIR = VAULT / "999-report-organizing" / "_permanent-notes" / "llm-generated-permanent-notes"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
FM_DELIM = "---"


def split_frontmatter(text: str) -> tuple[dict[str, Any], str, bool]:
    """Return (frontmatter_dict, body, had_frontmatter)."""
    if not text.startswith(FM_DELIM):
        return {}, text, False
    try:
        end = text.index("\n" + FM_DELIM, len(FM_DELIM))
    except ValueError:
        return {}, text, False
    try:
        data = yaml.safe_load(text[len(FM_DELIM) : end]) or {}
    except yaml.YAMLError:
        return {}, text, False
    body = text[end + len(FM_DELIM) + 1 :]
    if body.startswith("\n"):
        body = body[1:]
    return data if isinstance(data, dict) else {}, body, True


def render(fm: dict[str, Any], body: str) -> str:
    yaml_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True)
    return f"{FM_DELIM}\n{yaml_text}{FM_DELIM}\n\n{body.lstrip()}"


def ensure_parent(fm: dict[str, Any], moc_link: str) -> bool:
    parents = fm.get("parent-moc")
    if parents is None:
        parents = []
    elif isinstance(parents, str):
        parents = [parents]
    elif not isinstance(parents, list):
        parents = [str(parents)]
    if moc_link in parents:
        return False
    parents.append(moc_link)
    fm["parent-moc"] = parents
    return True


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Back-link MOCs into member notes.")
    p.add_argument("--dry-run", action="store_true", help="Report changes; write nothing.")
    args = p.parse_args(argv)

    if not MOC_DIR.exists():
        print(f"ERROR: MOC dir not found: {MOC_DIR}")
        return 2

    moc_files = [f for f in sorted(MOC_DIR.glob("*-moc.md")) if not f.name.startswith("_")]
    if not moc_files:
        print("No MOC files found (expecting *-moc.md).")
        return 0

    grand_updated = 0
    for moc in moc_files:
        moc_text = moc.read_text(encoding="utf-8", errors="ignore")
        targets = sorted(set(WIKILINK_RE.findall(moc_text)))
        moc_link = f"[[{moc.stem}]]"
        updated_count = 0
        for link in targets:
            target_path = NOTES_DIR / f"{link}.md"
            if not target_path.exists():
                continue
            text = target_path.read_text(encoding="utf-8", errors="ignore")
            fm, body, had_fm = split_frontmatter(text)
            if not had_fm:
                continue
            if not ensure_parent(fm, moc_link):
                continue
            if not args.dry_run:
                tmp = target_path.with_suffix(".md.tmp")
                tmp.write_text(render(fm, body), encoding="utf-8")
                tmp.replace(target_path)
            updated_count += 1
        grand_updated += updated_count
        action = "would update" if args.dry_run else "updated"
        print(f"  {moc.stem}: {action} {updated_count} member notes")

    print(f"Total notes {'to update' if args.dry_run else 'updated'}: {grand_updated}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
