#!/usr/bin/env python3
"""
broken_link_fixer.py
─────────────────────────────────────────────────────────────────────────────
Parse a broken links output file and fix/triage broken wiki-links across
your Obsidian vault.

STRATEGY:
  1. REMOVE junk links   — .claude/, .smart-env/, template vars, relative paths
  2. FIX moved paths     — find the actual file and update [[path]] in source notes
  3. CREATE date stubs   — weekly/monthly/quarterly/daily period notes
  4. CREATE concept stubs — high-frequency ghost links get a stub permanent note
  5. REPORT the rest     — low-frequency concept links for manual review

USAGE:
  python broken_link_fixer.py --vault "D:/10_pur3v4d3r's-vault"
  python broken_link_fixer.py --vault "D:/10_pur3v4d3r's-vault" --execute

SAFETY:
  - Dry-run by default.  Pass --execute to write changes.
  - Generates a detailed report before and after.

REQUIREMENTS:
  pip install rich click
"""

import os
import re
import sys
import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Optional

try:
    import click
    from rich.console import Console
    from rich.table import Table
    from rich.progress import track
    from rich.panel import Panel
except ImportError:
    sys.exit("Missing dependencies. Run:\n  pip install rich click")

console = Console()

# ── CONFIGURATION ─────────────────────────────────────────────────────────

# Folders to never scan/touch
IGNORE_DIRS = {
    ".git", ".obsidian", ".trash", "node_modules",
    ".smart-env", ".specstory", ".vs", ".venv",
}

# Path prefixes in broken links that indicate junk (not real notes)
JUNK_PATH_PREFIXES = [
    ".claude/", ".smart-env/", ".specstory/", ".vs/",
    "assets/", "images/", "docs/", "apps/",
    ".claude\\", ".smart-env\\", ".specstory\\", ".vs\\",
]

# Broken link names that start with these are template variables
TEMPLATE_VAR_PATTERNS = [
    re.compile(r"^\$\{"),        # ${variable}
    re.compile(r"^\{[A-Z]"),     # {Topic}
    re.compile(r"^\{[a-z]"),     # {topic}
    re.compile(r"^<%"),          # Templater syntax
]

# Where to create date stubs
DATE_FOLDERS = {
    "daily":     "01_daily-notes",
    "weekly":    "01_daily-notes",
    "monthly":   "01_daily-notes",
    "quarterly": "01_daily-notes",
}

# Where to create concept stub notes
CONCEPT_STUB_FOLDER = "03-notes/01_permanent-notes/01_cognitive-development"

# Minimum # of source files referencing a concept before we create a stub
CONCEPT_STUB_THRESHOLD = 5

# ─────────────────────────────────────────────────────────────────────────


def parse_broken_links_file(filepath: Path) -> list[dict]:
    """
    Parse the broken links output.md file.
    Each line: - [[Broken Link]] in [[source1]], [[source2]], ...

    Returns list of dicts:
      { "target": "Broken Link", "sources": ["source1", "source2", ...] }
    """
    entries = []
    pattern = re.compile(r"^- \[\[([^\]]+)\]\] in (.+)$")
    source_pattern = re.compile(r"\[\[([^\]]+)\]\]")

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            m = pattern.match(line)
            if m:
                target = m.group(1)
                sources_text = m.group(2)
                sources = source_pattern.findall(sources_text)
                entries.append({"target": target, "sources": sources})

    return entries


def classify_broken_link(target: str) -> str:
    """Classify a broken link target into a category."""
    # Template variables
    for pat in TEMPLATE_VAR_PATTERNS:
        if pat.match(target):
            return "template_var"

    # Relative paths that leaked
    if target.startswith("..") or target.startswith("./"):
        return "junk_relative"

    # Junk paths (plugin internals)
    for prefix in JUNK_PATH_PREFIXES:
        if target.startswith(prefix):
            return "junk_path"

    # Empty/dot-only paths
    if target in (".", ""):
        return "junk_path"

    # Dates
    if re.match(r"^\d{4}-W\d+$", target):
        return "date_weekly"
    if re.match(r"^\d{4}-\d{2}$", target):
        return "date_monthly"
    if re.match(r"^\d{4}-Q\d$", target):
        return "date_quarterly"
    if re.match(r"^\d{4}-\d{2}-\d{2}$", target):
        return "date_daily"

    # Path-based (contains /) — could be moved/renamed files
    if "/" in target:
        return "path_moved"

    # Concept/ghost link
    return "concept"


def build_file_index(vault_path: Path) -> dict[str, Path]:
    """
    Build a lookup: lowercase filename (no .md) → full Path.
    For files with duplicate names, stores the first found.
    """
    index = {}
    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            if fname.endswith(".md"):
                stem = fname[:-3].lower()
                full = Path(root) / fname
                if stem not in index:
                    index[stem] = full
    return index


def find_actual_file(target: str, file_index: dict[str, Path]) -> Optional[Path]:
    """
    For a path-based broken link like '99-archive/05-mocs/cognitive-science-moc',
    check if the filename part exists somewhere else in the vault.
    """
    # Extract just the filename from the path
    filename = target.rsplit("/", 1)[-1].lower()
    return file_index.get(filename)


def replace_link_in_file(
    file_path: Path, old_link: str, new_link: str, dry_run: bool
) -> bool:
    """Replace [[old_link]] with [[new_link]] in a file. Returns True if changed."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    # Build regex that matches [[old_link]], [[old_link|alias]], [[old_link#heading]]
    escaped = re.escape(old_link)
    pattern = re.compile(r"\[\[" + escaped + r"(\|[^\]]*|\#[^\]]*)?\]\]")

    if not pattern.search(content):
        return False

    if dry_run:
        return True

    def replacer(m):
        suffix = m.group(1) or ""
        return f"[[{new_link}{suffix}]]"

    new_content = pattern.sub(replacer, content)
    file_path.write_text(new_content, encoding="utf-8")
    return True


def remove_link_in_file(
    file_path: Path, target: str, dry_run: bool
) -> bool:
    """
    Remove broken [[target]] links from a file, replacing them with plain text.
    For example: [[.claude/something]] → just removes the [[ ]] wrapper.
    Returns True if anything would change.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    escaped = re.escape(target)
    pattern = re.compile(r"\[\[" + escaped + r"(?:\|([^\]]*))?\]\]")

    if not pattern.search(content):
        return False

    if dry_run:
        return True

    def replacer(m):
        # If alias exists, keep the alias text; otherwise use the target name
        alias = m.group(1)
        if alias:
            return alias
        # For junk paths, just return the last part or empty
        name = target.rsplit("/", 1)[-1]
        return name

    new_content = pattern.sub(replacer, content)
    file_path.write_text(new_content, encoding="utf-8")
    return True


def create_date_stub(
    vault_path: Path, target: str, category: str, dry_run: bool
) -> Optional[Path]:
    """Create a minimal period note stub."""
    folder = vault_path / DATE_FOLDERS.get(category.replace("date_", ""), "01_daily-notes")
    file_path = folder / f"{target}.md"

    if file_path.exists():
        return None

    if category == "date_weekly":
        title = f"Week {target}"
        content = f"""---
title: "{target}"
doc_type: "weekly-note"
doc_created: {datetime.date.today().isoformat()}
tags:
  - journal/weekly
---

# {title}

"""
    elif category == "date_monthly":
        title = target
        content = f"""---
title: "{target}"
doc_type: "monthly-note"
doc_created: {datetime.date.today().isoformat()}
tags:
  - journal/monthly
---

# {title}

"""
    elif category == "date_quarterly":
        title = target
        content = f"""---
title: "{target}"
doc_type: "quarterly-note"
doc_created: {datetime.date.today().isoformat()}
tags:
  - journal/quarterly
---

# {title}

"""
    elif category == "date_daily":
        title = target
        content = f"""---
title: "{target}"
doc_type: "daily-note"
doc_created: {datetime.date.today().isoformat()}
tags:
  - journal/daily
---

# {title}

"""
    else:
        return None

    if not dry_run:
        folder.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

    return file_path


def create_concept_stub(
    vault_path: Path, target: str, source_count: int, dry_run: bool
) -> Optional[Path]:
    """Create a minimal stub permanent note for a frequently-referenced concept."""
    folder = vault_path / CONCEPT_STUB_FOLDER
    # Sanitize filename
    safe_name = re.sub(r'[<>:"/\\|?*]', "", target)
    file_path = folder / f"{safe_name}.md"

    if file_path.exists():
        return None

    today = datetime.date.today().isoformat()
    content = f"""---
title: "{target}"
aliases: []
doc_type: "permanent-note"
doc_created: {today}
doc_modified: {today}
status: "seedling"
certainty: "provisional"
tags:
  - stub
  - needs-development
---

# {target}

> [!abstract] Summary
> *Stub note auto-generated from broken link analysis. Referenced in {source_count} files.*

## Overview

<!-- This concept was referenced across {source_count} notes but had no dedicated page. Develop as needed. -->

## Related Notes

"""

    if not dry_run:
        folder.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

    return file_path


@click.command()
@click.option("--vault", required=True, type=click.Path(exists=True),
              help="Path to your Obsidian vault root")
@click.option("--broken-links-file", default=None,
              help="Path to broken links output file (default: vault/broken links output.md)")
@click.option("--execute", is_flag=True, default=False,
              help="Apply changes. Default is dry-run.")
@click.option("--fix-paths/--no-fix-paths", default=True,
              help="Fix path-based broken links by finding actual file")
@click.option("--clean-junk/--no-clean-junk", default=True,
              help="Remove junk links (.claude/, .smart-env/, template vars)")
@click.option("--create-dates/--no-create-dates", default=True,
              help="Create stub period notes for date links")
@click.option("--create-stubs/--no-create-stubs", default=True,
              help="Create stub permanent notes for frequent concept links")
@click.option("--stub-threshold", default=CONCEPT_STUB_THRESHOLD, type=int,
              help=f"Min references to create a concept stub (default: {CONCEPT_STUB_THRESHOLD})")
def main(vault, broken_links_file, execute, fix_paths, clean_junk,
         create_dates, create_stubs, stub_threshold):
    """Fix broken wiki-links in your Obsidian vault."""

    vault_path = Path(vault)

    if broken_links_file:
        bl_path = Path(broken_links_file)
    else:
        bl_path = vault_path / "broken links output.md"

    if not bl_path.exists():
        console.print(f"[red]Broken links file not found: {bl_path}[/red]")
        return

    # ── Parse ──────────────────────────────────────────────────────────────
    console.print(Panel.fit(
        "[bold]Broken Link Fixer[/bold]\n"
        f"Vault: [cyan]{vault_path}[/cyan]\n"
        f"Mode: [{'green]EXECUTE' if execute else 'yellow]DRY RUN'}[/]\n"
        f"Source: [dim]{bl_path.name}[/dim]",
        title="🔗 PKB Link Repair"
    ))

    entries = parse_broken_links_file(bl_path)
    console.print(f"\nParsed [cyan]{len(entries)}[/cyan] broken link entries.\n")

    # ── Classify ───────────────────────────────────────────────────────────
    classified = defaultdict(list)
    for entry in entries:
        cat = classify_broken_link(entry["target"])
        entry["category"] = cat
        classified[cat].append(entry)

    # Summary table
    t = Table(title="Broken Link Classification")
    t.add_column("Category", style="cyan")
    t.add_column("Count", justify="right")
    t.add_column("Action")
    for cat in ["junk_path", "junk_relative", "template_var",
                "path_moved", "date_daily", "date_weekly",
                "date_monthly", "date_quarterly", "concept"]:
        items = classified.get(cat, [])
        action = {
            "junk_path": "🗑️  Remove link wrappers" if clean_junk else "⏭️  Skip",
            "junk_relative": "🗑️  Remove link wrappers" if clean_junk else "⏭️  Skip",
            "template_var": "⏭️  Skip (template syntax)",
            "path_moved": "🔄 Find & relink" if fix_paths else "⏭️  Skip",
            "date_daily": "📅 Create stub" if create_dates else "⏭️  Skip",
            "date_weekly": "📅 Create stub" if create_dates else "⏭️  Skip",
            "date_monthly": "📅 Create stub" if create_dates else "⏭️  Skip",
            "date_quarterly": "📅 Create stub" if create_dates else "⏭️  Skip",
            "concept": f"📝 Stub if ≥{stub_threshold} refs" if create_stubs else "📊 Report only",
        }.get(cat, "?")
        if items:
            t.add_row(cat, str(len(items)), action)
    console.print(t)
    console.print()

    # ── Build file index ───────────────────────────────────────────────────
    console.print("[dim]Building vault file index...[/dim]")
    file_index = build_file_index(vault_path)
    console.print(f"[dim]Indexed {len(file_index)} markdown files.[/dim]\n")

    # ── Counters ───────────────────────────────────────────────────────────
    stats = {
        "junk_removed": 0,
        "junk_files_touched": 0,
        "paths_fixed": 0,
        "paths_not_found": 0,
        "dates_created": 0,
        "stubs_created": 0,
        "stubs_already_exist": 0,
        "concept_below_threshold": 0,
    }

    # ══════════════════════════════════════════════════════════════════════
    # PHASE 1: CLEAN JUNK LINKS
    # ══════════════════════════════════════════════════════════════════════
    if clean_junk:
        junk_entries = classified["junk_path"] + classified["junk_relative"]
        if junk_entries:
            console.print(f"[bold]Phase 1:[/bold] Cleaning {len(junk_entries)} junk link targets...")
            files_touched = set()
            for entry in track(junk_entries, description="Removing junk links..."):
                for source in entry["sources"]:
                    source_file = file_index.get(source.lower().rsplit("/", 1)[-1])
                    if not source_file:
                        # Try full path match
                        source_file = vault_path / f"{source}.md"
                        if not source_file.exists():
                            continue
                    if remove_link_in_file(source_file, entry["target"], dry_run=not execute):
                        stats["junk_removed"] += 1
                        files_touched.add(str(source_file))
            stats["junk_files_touched"] = len(files_touched)
            console.print(f"  → {'Would remove' if not execute else 'Removed'} {stats['junk_removed']} junk links across {stats['junk_files_touched']} files\n")

    # ══════════════════════════════════════════════════════════════════════
    # PHASE 2: FIX MOVED PATHS
    # ══════════════════════════════════════════════════════════════════════
    if fix_paths:
        moved_entries = classified.get("path_moved", [])
        if moved_entries:
            console.print(f"[bold]Phase 2:[/bold] Fixing {len(moved_entries)} path-based broken links...")
            not_found = []
            for entry in track(moved_entries, description="Fixing paths..."):
                actual = find_actual_file(entry["target"], file_index)
                if actual:
                    # Compute the new relative wiki-link (just the stem)
                    new_link = actual.stem
                    for source in entry["sources"]:
                        source_file = file_index.get(source.lower().rsplit("/", 1)[-1])
                        if not source_file:
                            source_file = vault_path / f"{source}.md"
                            if not source_file.exists():
                                continue
                        if replace_link_in_file(source_file, entry["target"], new_link, dry_run=not execute):
                            stats["paths_fixed"] += 1
                else:
                    not_found.append(entry["target"])
                    stats["paths_not_found"] += 1

            console.print(f"  → {'Would fix' if not execute else 'Fixed'} {stats['paths_fixed']} path links")
            console.print(f"  → {stats['paths_not_found']} targets not found in vault\n")

            # Show unfound sample
            if not_found and len(not_found) <= 20:
                for nf in not_found[:20]:
                    console.print(f"    [dim]✗ {nf}[/dim]")
                console.print()

    # ══════════════════════════════════════════════════════════════════════
    # PHASE 3: CREATE DATE STUBS
    # ══════════════════════════════════════════════════════════════════════
    if create_dates:
        date_entries = (
            classified.get("date_weekly", []) +
            classified.get("date_monthly", []) +
            classified.get("date_quarterly", []) +
            classified.get("date_daily", [])
        )
        if date_entries:
            console.print(f"[bold]Phase 3:[/bold] Creating {len(date_entries)} date note stubs...")
            for entry in date_entries:
                result = create_date_stub(
                    vault_path, entry["target"], entry["category"],
                    dry_run=not execute
                )
                if result:
                    stats["dates_created"] += 1
                    console.print(f"  {'📅 Would create' if not execute else '📅 Created'}: {result.name}")
            console.print(f"  → {stats['dates_created']} date stubs {'planned' if not execute else 'created'}\n")

    # ══════════════════════════════════════════════════════════════════════
    # PHASE 4: CREATE CONCEPT STUBS
    # ══════════════════════════════════════════════════════════════════════
    if create_stubs:
        concept_entries = classified.get("concept", [])
        if concept_entries:
            above = [e for e in concept_entries if len(e["sources"]) >= stub_threshold]
            below = [e for e in concept_entries if len(e["sources"]) < stub_threshold]
            stats["concept_below_threshold"] = len(below)

            console.print(f"[bold]Phase 4:[/bold] Creating stubs for {len(above)} concept links (≥{stub_threshold} refs)...")
            console.print(f"  [dim]({len(below)} concept links below threshold — report only)[/dim]")

            created_list = []
            already_exist = []
            for entry in track(above, description="Creating concept stubs..."):
                # Check if it already exists in the vault
                if entry["target"].lower() in file_index:
                    already_exist.append(entry["target"])
                    stats["stubs_already_exist"] += 1
                    continue

                result = create_concept_stub(
                    vault_path, entry["target"], len(entry["sources"]),
                    dry_run=not execute
                )
                if result:
                    stats["stubs_created"] += 1
                    created_list.append(entry["target"])

            console.print(f"  → {stats['stubs_created']} concept stubs {'planned' if not execute else 'created'}")
            console.print(f"  → {stats['stubs_already_exist']} already exist in vault\n")

            if already_exist[:10]:
                console.print("  [green]Already exist:[/green]")
                for name in already_exist[:10]:
                    console.print(f"    ✓ {name}")
                if len(already_exist) > 10:
                    console.print(f"    ... and {len(already_exist) - 10} more")
                console.print()

    # ══════════════════════════════════════════════════════════════════════
    # FINAL SUMMARY
    # ══════════════════════════════════════════════════════════════════════
    summary = Table(title="Summary")
    summary.add_column("Metric", style="cyan")
    summary.add_column("Value", justify="right")
    summary.add_row("Broken links parsed", str(len(entries)))
    summary.add_row("Junk links removed", str(stats["junk_removed"]))
    summary.add_row("Files touched (junk cleanup)", str(stats["junk_files_touched"]))
    summary.add_row("Path links fixed", str(stats["paths_fixed"]))
    summary.add_row("Paths not found", str(stats["paths_not_found"]))
    summary.add_row("Date stubs created", str(stats["dates_created"]))
    summary.add_row("Concept stubs created", str(stats["stubs_created"]))
    summary.add_row("Concepts already existing", str(stats["stubs_already_exist"]))
    summary.add_row("Concepts below threshold", str(stats["concept_below_threshold"]))
    console.print(summary)

    if not execute:
        console.print("\n[yellow]This was a DRY RUN. Pass --execute to apply changes.[/yellow]")
    else:
        console.print("\n[green]Changes applied successfully.[/green]")

    # ── Write report ───────────────────────────────────────────────────────
    report_path = vault_path / "99-scripts" / f"broken-link-report-{datetime.date.today().isoformat()}.md"
    write_report(report_path, entries, classified, stats, stub_threshold, execute)
    console.print(f"\n[dim]Report written to: {report_path}[/dim]")


def write_report(
    report_path: Path, entries: list, classified: dict,
    stats: dict, threshold: int, executed: bool
):
    """Write a markdown report summarizing the broken link analysis."""
    lines = [
        f"# Broken Link Analysis Report",
        f"",
        f"**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Mode:** {'EXECUTED' if executed else 'DRY RUN'}",
        f"**Total broken links:** {len(entries)}",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Junk links removed | {stats['junk_removed']} |",
        f"| Path links fixed | {stats['paths_fixed']} |",
        f"| Date stubs created | {stats['dates_created']} |",
        f"| Concept stubs created | {stats['stubs_created']} |",
        f"| Concepts already exist | {stats['stubs_already_exist']} |",
        f"| Concepts below threshold | {stats['concept_below_threshold']} |",
        f"",
        f"## Concept Links Below Threshold (< {threshold} refs)",
        f"",
        f"These ghost links were referenced too few times for auto-stub generation.",
        f"Review and create manually if needed.",
        f"",
    ]

    # List concepts below threshold, sorted by count
    concept_below = [
        e for e in classified.get("concept", [])
        if len(e["sources"]) < threshold
    ]
    concept_below.sort(key=lambda x: len(x["sources"]), reverse=True)

    for entry in concept_below[:200]:  # Cap at 200 for readability
        lines.append(f"- **{entry['target']}** — {len(entry['sources'])} refs")

    if len(concept_below) > 200:
        lines.append(f"\n*... and {len(concept_below) - 200} more*\n")

    # Path links not found
    moved_not_found = [
        e for e in classified.get("path_moved", [])
        if not any("/" not in e["target"] for _ in [1])  # all path-based
    ]

    lines.extend([
        "",
        f"## Path-Based Links Not Found ({stats['paths_not_found']})",
        "",
    ])
    for entry in classified.get("path_moved", [])[:100]:
        lines.append(f"- `{entry['target']}` — {len(entry['sources'])} refs")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
