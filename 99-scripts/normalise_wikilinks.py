#!/usr/bin/env python3
"""
normalise_wikilinks.py
─────────────────────────────────────────────────────────────────────────────
Scan markdown files for wiki-links and rewrite them to match the actual
filenames of your permanent notes.

PROBLEM THIS SOLVES:
  Reports and notes often contain [[Space Separated Links]] while the
  permanent notes on disk use Kebab-Case-Names.md.  Obsidian treats these
  as different targets, creating thousands of ghost/broken links.

HOW IT WORKS:
  1. Index every .md file in your permanent-notes folder(s).
  2. Scan target files/folders for all [[Wiki-Links]].
  3. For each link, normalise it (lowercase, hyphens→spaces) and check
     if a permanent note matches.
  4. If yes → rewrite the link to use the permanent note's actual filename.
  5. Optionally add the space-based form as a YAML alias on the permanent
     note so both forms resolve in Obsidian.

USAGE:
  # Dry run — scan entire vault against permanent notes
  python normalise_wikilinks.py

  # Dry run — scan only a specific folder of new reports
  python normalise_wikilinks.py --scan "00-inbox/01-reports"

  # Dry run — scan a single file
  python normalise_wikilinks.py --scan "00-inbox/01-reports/my-new-report.md"

  # Apply changes
  python normalise_wikilinks.py --scan "00-inbox/01-reports" --execute

  # Also add aliases to permanent notes (belt-and-suspenders)
  python normalise_wikilinks.py --scan "00-inbox/01-reports" --add-aliases --execute

  # Use multiple permanent note folders
  python normalise_wikilinks.py --perm-dir "03-notes/01_permanent-notes" --perm-dir "999-report-orginizing/_permanent-notes/_permanent-notes"

SAFETY:
  - Dry-run by default.  Pass --execute to write changes.
  - Only rewrites links where a matching permanent note is found.
  - Never touches files in ignored directories.

REQUIREMENTS:
  pip install rich click
"""

import re
import os
import sys
import datetime
from pathlib import Path
from collections import defaultdict

try:
    import click
    from rich.console import Console
    from rich.table import Table
    from rich.progress import track
    from rich.panel import Panel
except ImportError:
    sys.exit("Missing dependencies. Run:\n  pip install rich click")

console = Console()

# ── DEFAULT CONFIGURATION ─────────────────────────────────────────────────

DEFAULT_VAULT = Path(r"D:/10_pur3v4d3r's-vault")

DEFAULT_PERM_DIRS = [
    "999-report-orginizing/_permanent-notes/_permanent-notes",
]

IGNORE_DIRS = {
    ".git", ".obsidian", ".trash", "node_modules",
    ".smart-env", ".specstory", ".vs", ".venv",
}

WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")

# ─────────────────────────────────────────────────────────────────────────


def normalize(name: str) -> str:
    """Lowercase, hyphens/underscores → spaces, collapse whitespace."""
    n = name.lower().replace("-", " ").replace("_", " ").strip()
    return re.sub(r"\s+", " ", n)


def index_permanent_notes(vault: Path, perm_dirs: list[str]) -> dict[str, Path]:
    """
    Build normalized-name → Path index for every .md in the permanent
    note directories.
    """
    index = {}
    for rel in perm_dirs:
        perm_path = vault / rel
        if not perm_path.exists():
            console.print(f"[yellow]Warning: permanent notes dir not found: {perm_path}[/yellow]")
            continue
        for f in perm_path.rglob("*.md"):
            key = normalize(f.stem)
            if key not in index:
                index[key] = f
    return index


def collect_scan_files(vault: Path, scan_target: str | None) -> list[Path]:
    """
    Collect markdown files to scan for wiki-links.
    If scan_target is None, scan the entire vault.
    If it's a file, return just that file.
    If it's a folder, scan recursively.
    """
    if scan_target:
        target = vault / scan_target
        if target.is_file() and target.suffix == ".md":
            return [target]
        elif target.is_dir():
            return [
                f for f in target.rglob("*.md")
                if not any(part in IGNORE_DIRS for part in f.parts)
            ]
        else:
            console.print(f"[red]Scan target not found: {target}[/red]")
            return []
    else:
        # Scan entire vault
        files = []
        for root, dirs, filenames in os.walk(vault):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for fname in filenames:
                if fname.endswith(".md"):
                    files.append(Path(root) / fname)
        return files


def find_links_in_file(file_path: Path) -> list[tuple[str, int]]:
    """
    Extract all wiki-link targets from a file.
    Returns list of (link_target, line_number).
    """
    links = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                for m in WIKILINK_PATTERN.finditer(line):
                    links.append((m.group(1).strip(), line_num))
    except Exception:
        pass
    return links


def rewrite_links_in_file(
    file_path: Path,
    rewrites: dict[str, str],  # old_link → new_link
    dry_run: bool,
) -> int:
    """
    Apply all link rewrites to a single file.
    Returns total number of replacements made.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return 0

    total = 0
    new_content = content

    for old_link, new_link in rewrites.items():
        escaped = re.escape(old_link)
        pattern = re.compile(r"\[\[" + escaped + r"(\|[^\]]*|\#[^\]]*)?\]\]")
        count = len(pattern.findall(new_content))
        if count > 0:
            total += count
            if not dry_run:
                def make_replacer(nl):
                    def replacer(m):
                        suffix = m.group(1) or ""
                        return f"[[{nl}{suffix}]]"
                    return replacer
                new_content = pattern.sub(make_replacer(new_link), new_content)

    if total > 0 and not dry_run:
        file_path.write_text(new_content, encoding="utf-8")

    return total


def add_alias_to_frontmatter(file_path: Path, alias: str, dry_run: bool) -> bool:
    """Add alias to YAML frontmatter. Returns True if changed."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    if not content.startswith("---"):
        if dry_run:
            return True
        new_fm = f'---\naliases:\n  - "{alias}"\n---\n'
        file_path.write_text(new_fm + content, encoding="utf-8")
        return True

    end = content.find("\n---", 3)
    if end == -1:
        return False

    fm_block = content[3:end]

    if alias.lower() in fm_block.lower():
        return False

    alias_match = re.search(r"^(aliases:\s*)(.*)$", fm_block, re.MULTILINE)
    if alias_match:
        rest = alias_match.group(2).strip()
        if rest.startswith("["):
            if rest == "[]":
                new_rest = f'["{alias}"]'
            else:
                new_rest = rest[:-1].rstrip() + f', "{alias}"]'
            new_line = f"aliases: {new_rest}"
            new_fm = fm_block[:alias_match.start()] + new_line + fm_block[alias_match.end():]
        else:
            insert_pos = alias_match.end()
            new_item = f'\n  - "{alias}"'
            new_fm = fm_block[:insert_pos] + new_item + fm_block[insert_pos:]
    else:
        new_fm = fm_block.rstrip() + f'\naliases:\n  - "{alias}"'

    if dry_run:
        return True

    new_content = "---" + new_fm + content[end:]
    file_path.write_text(new_content, encoding="utf-8")
    return True


@click.command()
@click.option("--vault", default=str(DEFAULT_VAULT), type=click.Path(exists=True),
              help="Path to your Obsidian vault root.")
@click.option("--perm-dir", "perm_dirs", multiple=True,
              help="Relative path to a permanent notes folder (repeatable). "
                   "Defaults to: " + ", ".join(DEFAULT_PERM_DIRS))
@click.option("--scan", "scan_target", default=None,
              help="Relative path to file or folder to scan. Default: entire vault.")
@click.option("--add-aliases", is_flag=True, default=False,
              help="Also add space-based aliases to permanent notes' frontmatter.")
@click.option("--execute", is_flag=True, default=False,
              help="Apply changes. Default is dry-run.")
def main(vault, perm_dirs, scan_target, add_aliases, execute):
    """
    Normalise wiki-links to match permanent note filenames.

    Scans markdown files for [[Wiki Links]] and rewrites them to match the
    actual Kebab-Case-Name.md filenames of your permanent notes.
    """
    vault_path = Path(vault)
    dry_run = not execute

    # Use defaults if no --perm-dir specified
    if not perm_dirs:
        perm_dirs = DEFAULT_PERM_DIRS

    console.print(Panel.fit(
        "[bold]Wiki-Link Normaliser[/bold]\n"
        f"Vault: [cyan]{vault_path}[/cyan]\n"
        f"Scan: [cyan]{scan_target or 'entire vault'}[/cyan]\n"
        f"Perm dirs: [dim]{', '.join(perm_dirs)}[/dim]\n"
        f"Add aliases: [{'green]YES' if add_aliases else 'dim]NO'}[/]\n"
        f"Mode: [{'yellow]DRY RUN' if dry_run else 'green]EXECUTE'}[/]",
        title="🔗 normalise_wikilinks.py"
    ))

    # ── 1. Index permanent notes ──────────────────────────────────────────
    console.print("\n[dim]Indexing permanent notes...[/dim]")
    perm_idx = index_permanent_notes(vault_path, list(perm_dirs))
    console.print(f"  Permanent notes indexed: [cyan]{len(perm_idx)}[/cyan]")

    if not perm_idx:
        console.print("[red]No permanent notes found. Check --perm-dir paths.[/red]")
        return

    # ── 2. Collect files to scan ──────────────────────────────────────────
    console.print("[dim]Collecting files to scan...[/dim]")
    scan_files = collect_scan_files(vault_path, scan_target)
    console.print(f"  Files to scan: [cyan]{len(scan_files)}[/cyan]\n")

    if not scan_files:
        console.print("[yellow]No files to scan.[/yellow]")
        return

    # ── 3. Scan and match ─────────────────────────────────────────────────
    # For each scanned file, build a dict of rewrites needed
    file_rewrites: dict[Path, dict[str, str]] = {}  # file → {old → new}
    all_matches: dict[str, str] = {}                 # ghost → perm_stem (global)
    unmatched: set[str] = set()

    for fpath in track(scan_files, description="Scanning wiki-links..."):
        links = find_links_in_file(fpath)
        rewrites = {}
        for link_target, _ in links:
            # Skip if it's already in our rewrite map
            norm = normalize(link_target)
            if norm in perm_idx:
                perm_path = perm_idx[norm]
                # Only rewrite if the link text doesn't already match the filename
                if link_target != perm_path.stem:
                    rewrites[link_target] = perm_path.stem
                    all_matches[link_target] = perm_path.stem
            else:
                unmatched.add(link_target)

        if rewrites:
            file_rewrites[fpath] = rewrites

    unique_ghosts = len(all_matches)
    total_files = len(file_rewrites)
    console.print(f"\n  Unique ghost links matched: [bold green]{unique_ghosts}[/bold green]")
    console.print(f"  Files needing rewrites: [cyan]{total_files}[/cyan]\n")

    if unique_ghosts == 0:
        console.print("[green]All wiki-links already match permanent note filenames. Nothing to do![/green]")
        return

    # ── 4. Phase A: Rewrite links ─────────────────────────────────────────
    console.print("[bold]Phase A:[/bold] Rewriting wiki-links in source files...\n")
    total_rewrites = 0
    files_touched = 0

    for fpath, rewrites in track(file_rewrites.items(), description="Rewriting links...", total=total_files):
        count = rewrite_links_in_file(fpath, rewrites, dry_run)
        if count > 0:
            total_rewrites += count
            files_touched += 1

    verb = "Would rewrite" if dry_run else "Rewrote"
    console.print(f"  {verb} [cyan]{total_rewrites}[/cyan] link references across [cyan]{files_touched}[/cyan] files\n")

    # ── 5. Phase B: Add aliases (optional) ────────────────────────────────
    aliases_added = 0
    if add_aliases:
        console.print("[bold]Phase B:[/bold] Adding aliases to permanent notes...\n")
        for ghost, perm_stem in track(all_matches.items(), description="Adding aliases..."):
            perm_path = perm_idx[normalize(ghost)]
            if add_alias_to_frontmatter(perm_path, ghost, dry_run):
                aliases_added += 1

        verb = "Would add" if dry_run else "Added"
        console.print(f"  {verb} [cyan]{aliases_added}[/cyan] aliases\n")

    # ── 6. Summary ────────────────────────────────────────────────────────
    t = Table(title="Summary")
    t.add_column("Metric", style="cyan")
    t.add_column("Value", justify="right")
    t.add_row("Permanent notes indexed", str(len(perm_idx)))
    t.add_row("Files scanned", str(len(scan_files)))
    t.add_row("Unique ghost links matched", str(unique_ghosts))
    t.add_row("Link references rewritten", str(total_rewrites))
    t.add_row("Source files modified", str(files_touched))
    if add_aliases:
        t.add_row("Aliases added", str(aliases_added))
    console.print(t)

    if dry_run:
        console.print("\n[yellow]This was a DRY RUN. Pass --execute to apply changes.[/yellow]")
    else:
        console.print("\n[green]All changes applied successfully.[/green]")

    # ── 7. Top rewrites ──────────────────────────────────────────────────
    if all_matches:
        console.print("\n[bold]Sample rewrites:[/bold]")
        for ghost, perm_stem in list(all_matches.items())[:20]:
            console.print(f"  [[{ghost}]] → [[{perm_stem}]]")
        if len(all_matches) > 20:
            console.print(f"  [dim]... and {len(all_matches) - 20} more[/dim]")


if __name__ == "__main__":
    main()
