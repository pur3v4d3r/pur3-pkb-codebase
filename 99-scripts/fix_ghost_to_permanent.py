#!/usr/bin/env python3
"""
fix_ghost_to_permanent.py
─────────────────────────────────────────────────────────────────────────────
Fix ghost wiki-links that match existing permanent notes by:
  1. Adding the space-based name as a YAML alias to the permanent note
  2. Rewriting [[Space Name]] → [[Kebab-Case-Name]] in every source file

USAGE:
  python fix_ghost_to_permanent.py                    # dry run
  python fix_ghost_to_permanent.py --execute          # apply changes

SAFETY:
  - Dry-run by default. Nothing is written unless --execute is passed.
  - Prints full summary of what would change.

REQUIREMENTS:
  pip install rich
"""

import re
import sys
import datetime
from pathlib import Path
from collections import defaultdict

try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import track
    from rich.panel import Panel
except ImportError:
    sys.exit("Missing dependency. Run:\n  pip install rich")

console = Console()

# ── CONFIGURATION ─────────────────────────────────────────────────────────
VAULT_PATH       = Path(r"D:/10_pur3v4d3r's-vault")
BROKEN_LINKS     = VAULT_PATH / "broken links output.md"
PERMANENT_DIR    = VAULT_PATH / "999-report-organizing" / "_permanent-notes" / "_permanent-notes"

# Folders to never scan when rewriting links in source files
IGNORE_DIRS = {
    ".git", ".obsidian", ".trash", "node_modules",
    ".smart-env", ".specstory", ".vs", ".venv",
}
# ─────────────────────────────────────────────────────────────────────────


def normalize(name: str) -> str:
    """Lowercase, hyphens/underscores → spaces, collapse whitespace."""
    n = name.lower().replace("-", " ").replace("_", " ").strip()
    return re.sub(r"\s+", " ", n)


def parse_broken_links(path: Path) -> list[tuple[str, list[str]]]:
    """Parse broken links output → list of (target, [source, …])."""
    entries = []
    line_pat = re.compile(r"^- \[\[([^\]]+)\]\] in (.+)$")
    src_pat  = re.compile(r"\[\[([^\]]+)\]\]")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = line_pat.match(line.strip())
            if m:
                entries.append((m.group(1), src_pat.findall(m.group(2))))
    return entries


def index_permanent_notes(perm_dir: Path) -> dict[str, Path]:
    """normalized-name → Path for every .md in the permanent notes folder."""
    index = {}
    for f in perm_dir.rglob("*.md"):
        index[normalize(f.stem)] = f
    return index


def build_vault_file_index(vault: Path) -> dict[str, Path]:
    """lowercase stem → Path for every .md in the vault (first-found wins)."""
    idx = {}
    for root, dirs, files in vault.walk():
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            if fname.endswith(".md"):
                stem = fname[:-3].lower()
                if stem not in idx:
                    idx[stem] = root / fname
    return idx


def find_source_file(source_name: str, vault_idx: dict[str, Path]) -> Path | None:
    """Resolve a source name from the broken-links list to an actual file."""
    # Try full name as-is (lowered)
    key = source_name.lower()
    if key in vault_idx:
        return vault_idx[key]
    # Try after stripping any path prefix
    key = source_name.rsplit("/", 1)[-1].lower()
    if key in vault_idx:
        return vault_idx[key]
    return None


def add_alias_to_frontmatter(file_path: Path, alias: str, dry_run: bool) -> bool:
    """
    Add `alias` to the YAML frontmatter aliases list.
    Returns True if a change was (or would be) made.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    # Must start with ---
    if not content.startswith("---"):
        # No frontmatter — prepend one with aliases
        if dry_run:
            return True
        new_fm = f'---\naliases:\n  - "{alias}"\n---\n'
        file_path.write_text(new_fm + content, encoding="utf-8")
        return True

    # Find the closing ---
    end = content.find("\n---", 3)
    if end == -1:
        return False

    fm_block = content[3:end]

    # Check if alias already present (case-insensitive)
    if alias.lower() in fm_block.lower():
        return False

    # Find 'aliases:' line
    alias_match = re.search(r"^(aliases:\s*)(.*)$", fm_block, re.MULTILINE)
    if alias_match:
        rest = alias_match.group(2).strip()
        if rest.startswith("["):
            # Inline array: aliases: [A, B]
            if rest == "[]":
                new_rest = f'["{alias}"]'
            else:
                # Insert before closing bracket
                new_rest = rest[:-1].rstrip() + f', "{alias}"]'
            new_line = f"aliases: {new_rest}"
            new_fm = fm_block[:alias_match.start()] + new_line + fm_block[alias_match.end():]
        else:
            # Block-style list or empty
            # Check for list items below
            insert_pos = alias_match.end()
            indent = "  "
            new_item = f'\n{indent}- "{alias}"'
            # If rest is empty and next lines have "  - ", add to that list
            new_fm = fm_block[:insert_pos] + new_item + fm_block[insert_pos:]
    else:
        # No aliases field — add one at the end of frontmatter
        new_fm = fm_block.rstrip() + f'\naliases:\n  - "{alias}"'

    if dry_run:
        return True

    new_content = "---" + new_fm + content[end:]
    file_path.write_text(new_content, encoding="utf-8")
    return True


def rewrite_link_in_file(
    file_path: Path, old_link: str, new_link: str, dry_run: bool
) -> int:
    """
    Replace [[old_link]] → [[new_link]] in file_path.
    Handles [[old_link|alias]] and [[old_link#heading]] forms.
    Returns the number of replacements made (or that would be made).
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return 0

    escaped = re.escape(old_link)
    pattern = re.compile(r"\[\[" + escaped + r"(\|[^\]]*|\#[^\]]*)?\]\]")

    count = len(pattern.findall(content))
    if count == 0:
        return 0

    if not dry_run:
        def replacer(m):
            suffix = m.group(1) or ""
            return f"[[{new_link}{suffix}]]"
        new_content = pattern.sub(replacer, content)
        file_path.write_text(new_content, encoding="utf-8")

    return count


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix ghost links → permanent notes")
    parser.add_argument("--execute", action="store_true",
                        help="Apply changes (default: dry run)")
    args = parser.parse_args()
    dry_run = not args.execute

    console.print(Panel.fit(
        "[bold]Ghost Link → Permanent Note Fixer[/bold]\n"
        f"Vault: [cyan]{VAULT_PATH}[/cyan]\n"
        f"Permanent notes: [cyan]{PERMANENT_DIR}[/cyan]\n"
        f"Mode: [{'yellow]DRY RUN' if dry_run else 'green]EXECUTE'}[/]",
        title="🔗 Dual Fix"
    ))

    # ── 1. Parse & match ──────────────────────────────────────────────────
    console.print("\n[dim]Parsing broken links...[/dim]")
    entries = parse_broken_links(BROKEN_LINKS)
    console.print(f"  Broken link entries: [cyan]{len(entries)}[/cyan]")

    console.print("[dim]Indexing permanent notes...[/dim]")
    perm_idx = index_permanent_notes(PERMANENT_DIR)
    console.print(f"  Permanent notes: [cyan]{len(perm_idx)}[/cyan]")

    console.print("[dim]Building vault file index...[/dim]")
    vault_idx = build_vault_file_index(VAULT_PATH)
    console.print(f"  Vault files indexed: [cyan]{len(vault_idx)}[/cyan]")

    # Find matches
    matches = []  # (ghost_link, perm_file_path, perm_stem, [sources])
    for target, sources in entries:
        norm = normalize(target)
        if norm in perm_idx:
            perm_path = perm_idx[norm]
            matches.append((target, perm_path, perm_path.stem, sources))

    console.print(f"\n  [bold green]Matches: {len(matches)} ghost links → permanent notes[/bold green]")
    total_refs = sum(len(m[3]) for m in matches)
    console.print(f"  Total source references: [cyan]{total_refs}[/cyan]\n")

    if not matches:
        console.print("[yellow]No matches found. Nothing to do.[/yellow]")
        return

    # ── 2. Phase A: Add aliases to permanent notes ────────────────────────
    console.print("[bold]Phase A:[/bold] Adding aliases to permanent notes...\n")
    aliases_added = 0
    aliases_skipped = 0

    for ghost, perm_path, perm_stem, _ in track(matches, description="Adding aliases..."):
        # The alias to add is the ghost link text (the space-based version)
        # Only add if it differs from the filename stem
        if ghost == perm_stem:
            aliases_skipped += 1
            continue
        if add_alias_to_frontmatter(perm_path, ghost, dry_run):
            aliases_added += 1
        else:
            aliases_skipped += 1

    verb = "Would add" if dry_run else "Added"
    console.print(f"  {verb} [cyan]{aliases_added}[/cyan] aliases")
    console.print(f"  Skipped (already present or identical): [dim]{aliases_skipped}[/dim]\n")

    # ── 3. Phase B: Rewrite links in source files ─────────────────────────
    console.print("[bold]Phase B:[/bold] Rewriting links in source files...\n")
    links_rewritten = 0
    files_touched = set()
    sources_not_found = 0

    for ghost, perm_path, perm_stem, sources in track(matches, description="Rewriting links..."):
        # Skip if ghost link already matches the permanent note stem exactly
        if ghost == perm_stem:
            continue

        for source_name in sources:
            src_file = find_source_file(source_name, vault_idx)
            if not src_file:
                sources_not_found += 1
                continue

            count = rewrite_link_in_file(src_file, ghost, perm_stem, dry_run)
            if count > 0:
                links_rewritten += count
                files_touched.add(str(src_file))

    verb = "Would rewrite" if dry_run else "Rewrote"
    console.print(f"  {verb} [cyan]{links_rewritten}[/cyan] link references")
    console.print(f"  Files touched: [cyan]{len(files_touched)}[/cyan]")
    console.print(f"  Source files not found: [dim]{sources_not_found}[/dim]\n")

    # ── 4. Summary ────────────────────────────────────────────────────────
    t = Table(title="Summary")
    t.add_column("Metric", style="cyan")
    t.add_column("Value", justify="right")
    t.add_row("Ghost links matched", str(len(matches)))
    t.add_row("Aliases added to permanent notes", str(aliases_added))
    t.add_row("Link references rewritten", str(links_rewritten))
    t.add_row("Source files modified", str(len(files_touched)))
    t.add_row("Sources not resolved", str(sources_not_found))
    console.print(t)

    if dry_run:
        console.print("\n[yellow]This was a DRY RUN. Pass --execute to apply changes.[/yellow]")
    else:
        console.print("\n[green]All changes applied successfully.[/green]")

    # ── 5. Show top 30 matches ────────────────────────────────────────────
    console.print("\n[bold]Top 30 Matches:[/bold]")
    matches.sort(key=lambda x: len(x[3]), reverse=True)
    for ghost, _, perm_stem, sources in matches[:30]:
        console.print(f"  [{len(sources):>3} refs] [[{ghost}]] → [[{perm_stem}]]")


if __name__ == "__main__":
    main()
