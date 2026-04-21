#!/usr/bin/env python3
"""
generate_frontmatter.py
─────────────────────────────────────────────────────────────────────────────
Review a markdown file and generate (or update) a PKB-compliant YAML
frontmatter block.

WHAT IT DOES
  1. Reads a markdown file (and any existing frontmatter).
  2. Extracts what it can automatically:
       - title             (from existing FM, first H1, or filename)
       - doc_created       (from filename date prefix or filesystem ctime)
       - doc_modified      (today, or filesystem mtime)
       - aliases           (slug variants of the title)
       - tags              (from #hashtags in the body, deduplicated)
       - related_concepts  (from [[wiki-links]] in the body)
       - summary           (first non-empty paragraph after the H1)
       - keywords          (top-frequency content words)
  3. Asks the user to confirm or fill any missing required fields
     (interactive mode), OR fills sensible defaults (--non-interactive).
  4. Writes the new frontmatter to the file (or prints to stdout in
     --dry-run mode). Existing frontmatter values are preserved unless
     --overwrite is passed.

REQUIREMENTS
  pip install python-frontmatter rich click pyyaml

USAGE
  python 99-scripts/generate_frontmatter.py path/to/note.md
  python 99-scripts/generate_frontmatter.py path/to/note.md --dry-run
  python 99-scripts/generate_frontmatter.py path/to/note.md --non-interactive
  python 99-scripts/generate_frontmatter.py path/to/note.md --overwrite

@author   PKB Scripting Architect
@version  1.0.0
"""

from __future__ import annotations

import re
import sys
import datetime
from collections import Counter
from pathlib import Path
from typing import Any

try:
    import click
    import frontmatter
    import yaml
    from rich.console import Console
    from rich.prompt import Prompt, Confirm
    from rich.syntax import Syntax
except ImportError:
    sys.exit(
        "Missing dependencies. Run:\n"
        "  pip install python-frontmatter rich click pyyaml"
    )

console = Console()

# ── CONFIGURATION ─────────────────────────────────────────────────────────
CONFIG = {
    # Default author when none can be inferred / provided
    "default_author": "GitHub Copilot",

    # Default values applied in --non-interactive mode
    "defaults": {
        "doc_type":         "Permanent Note",
        "primary_domain":   "General",
        "knowledge_level":  "developing",
        "status":           "draft",
        "maturity":         "in progress",
        "confidence":       "medium",
        "epistemic_status": "provisional",
    },

    # Tag inference
    "max_inferred_tags":     8,
    "max_inferred_keywords": 10,
    "max_inferred_related":  10,

    # Stop-words for keyword extraction
    "stopwords": {
        "the", "and", "for", "are", "but", "not", "you", "all", "can", "had",
        "her", "was", "one", "our", "out", "day", "get", "has", "him", "his",
        "how", "man", "new", "now", "old", "see", "two", "way", "who", "boy",
        "did", "its", "let", "put", "say", "she", "too", "use", "this", "that",
        "with", "from", "have", "they", "them", "what", "when", "your", "will",
        "into", "more", "than", "then", "some", "such", "only", "also", "very",
        "been", "were", "would", "could", "should", "their", "there", "these",
        "those", "which", "while", "about", "after", "before", "where",
    },
}
# ──────────────────────────────────────────────────────────────────────────

# Regex patterns
RE_H1            = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
RE_DATE_PREFIX   = re.compile(r"(\d{4}-\d{2}-\d{2})")
RE_HASHTAG       = re.compile(r"(?<![\w/])#([A-Za-z][\w/-]{2,})")
RE_WIKILINK      = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
RE_WORD          = re.compile(r"\b[A-Za-z][A-Za-z-]{3,}\b")
RE_CODE_BLOCK    = re.compile(r"```.*?```", re.DOTALL)
RE_INLINE_CODE   = re.compile(r"`[^`]+`")


# ═════════════════════════════════════════════════════════════════════════
# EXTRACTION HELPERS
# ═════════════════════════════════════════════════════════════════════════

def strip_code(text: str) -> str:
    """Remove fenced and inline code so they don't pollute extraction."""
    text = RE_CODE_BLOCK.sub("", text)
    text = RE_INLINE_CODE.sub("", text)
    return text


def extract_title(body: str, filepath: Path, existing: dict) -> str:
    """Title precedence: existing FM → first H1 → humanised filename."""
    if existing.get("title"):
        return str(existing["title"])
    h1 = RE_H1.search(body)
    if h1:
        return h1.group(1).strip()
    # Humanise filename: strip date prefix, replace separators
    stem = filepath.stem
    stem = RE_DATE_PREFIX.sub("", stem).strip(" -_")
    return stem.replace("-", " ").replace("_", " ").title()


def extract_dates(filepath: Path, existing: dict) -> tuple[str, str]:
    """Return (created, modified) ISO date strings."""
    today = datetime.date.today().isoformat()

    # doc_created: existing → filename prefix → ctime
    created = existing.get("doc_created") or existing.get("created")
    if not created:
        m = RE_DATE_PREFIX.search(filepath.stem)
        if m:
            created = m.group(1)
        else:
            try:
                created = datetime.date.fromtimestamp(
                    filepath.stat().st_ctime
                ).isoformat()
            except OSError:
                created = today
    created = str(created)

    # doc_modified: always set to today on regeneration
    modified = today
    return created, modified


def extract_summary(body: str) -> str:
    """First non-empty paragraph after stripping H1 / frontmatter / code."""
    cleaned = strip_code(body)
    # Drop H1 line(s)
    cleaned = RE_H1.sub("", cleaned)
    # Split into paragraphs
    for para in cleaned.split("\n\n"):
        p = para.strip()
        if not p:                       continue
        if p.startswith(("#", ">", "-", "*", "|", "```")):  continue
        # First sentence-ish chunk, capped at 280 chars
        return (p[:280] + "…") if len(p) > 280 else p
    return ""


def extract_hashtags(body: str) -> list[str]:
    """Extract #hashtags from body, normalised, deduplicated."""
    cleaned = strip_code(body)
    tags = [m.group(1).lower() for m in RE_HASHTAG.finditer(cleaned)]
    # Dedupe preserving order
    seen, out = set(), []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(f"#{t}")
    return out[: CONFIG["max_inferred_tags"]]


def extract_wikilinks(body: str) -> list[str]:
    """Extract [[wiki-links]] as related concepts, deduplicated."""
    cleaned = strip_code(body)
    links = [m.group(1).strip() for m in RE_WIKILINK.finditer(cleaned)]
    seen, out = set(), []
    for link in links:
        key = link.lower()
        if key not in seen:
            seen.add(key)
            out.append(f"[[{link}]]")
    return out[: CONFIG["max_inferred_related"]]


def extract_keywords(body: str) -> list[str]:
    """Top-frequency content words (excluding stopwords)."""
    cleaned = strip_code(body).lower()
    # Strip wiki-links and hashtags before counting
    cleaned = RE_WIKILINK.sub("", cleaned)
    cleaned = RE_HASHTAG.sub("", cleaned)
    words = [
        w for w in RE_WORD.findall(cleaned)
        if w not in CONFIG["stopwords"]
    ]
    counts = Counter(words)
    return [w for w, _ in counts.most_common(CONFIG["max_inferred_keywords"])]


def make_doc_id(title: str, created: str) -> str:
    """Build a stable doc_id like PERM-CTMSR-2026-04-21."""
    # Initials from first letters of capital-led words, max 5 chars
    words = re.findall(r"[A-Za-z][a-z]*", title)
    initials = "".join(w[0].upper() for w in words[:5]) or "NOTE"
    return f"PERM-{initials}-{created}"


def make_aliases(title: str) -> list[str]:
    """Generate a couple of alias variants from the title."""
    aliases = set()
    aliases.add(title)
    aliases.add(title.lower())
    aliases.add(title.replace(" ", "-").lower())
    aliases.discard("")
    return sorted(aliases)


# ═════════════════════════════════════════════════════════════════════════
# FRONTMATTER ASSEMBLY
# ═════════════════════════════════════════════════════════════════════════

def build_frontmatter(
    filepath: Path,
    body: str,
    existing: dict,
    interactive: bool,
    overwrite: bool,
) -> dict[str, Any]:
    """Construct the frontmatter dict, prompting where needed."""

    # ── Auto-extracted ────────────────────────────────────────────────────
    title              = extract_title(body, filepath, existing)
    created, modified  = extract_dates(filepath, existing)
    summary            = existing.get("summary") or extract_summary(body)
    inferred_tags      = extract_hashtags(body)
    inferred_related   = extract_wikilinks(body)
    inferred_keywords  = extract_keywords(body)
    aliases            = existing.get("aliases") or make_aliases(title)
    doc_id             = existing.get("doc_id") or make_doc_id(title, created)

    # ── Build candidate FM (start from existing if not overwriting) ───────
    fm: dict[str, Any] = {} if overwrite else dict(existing)

    fm["doc_id"]            = doc_id
    fm["doc_type"]          = fm.get("doc_type")          or CONFIG["defaults"]["doc_type"]
    fm["doc_created"]       = created
    fm["doc_modified"]      = modified
    fm["author"]            = fm.get("author")            or CONFIG["default_author"]

    fm["title"]             = title
    fm["primary_domain"]    = fm.get("primary_domain")    or CONFIG["defaults"]["primary_domain"]
    fm["secondary_domains"] = fm.get("secondary_domains") or []
    fm["knowledge_level"]   = fm.get("knowledge_level")   or CONFIG["defaults"]["knowledge_level"]
    fm["tags"]              = fm.get("tags")              or inferred_tags
    fm["status"]            = fm.get("status")            or CONFIG["defaults"]["status"]
    fm["maturity"]          = fm.get("maturity")          or CONFIG["defaults"]["maturity"]
    fm["confidence"]        = fm.get("confidence")        or CONFIG["defaults"]["confidence"]
    fm["epistemic_status"]  = fm.get("epistemic_status")  or CONFIG["defaults"]["epistemic_status"]

    fm["aliases"]           = fm.get("aliases")           or aliases
    fm["related_concepts"]  = fm.get("related_concepts")  or inferred_related
    fm["summary"]           = fm.get("summary")           or summary
    fm["keywords"]          = fm.get("keywords")          or inferred_keywords

    # ── Interactive confirmation for required fields ──────────────────────
    if interactive:
        console.rule("[bold cyan]Confirm metadata[/bold cyan]")
        fm["title"]           = Prompt.ask("Title",           default=str(fm["title"]))
        fm["author"]          = Prompt.ask("Author",          default=str(fm["author"]))
        fm["doc_type"]        = Prompt.ask("Doc type",        default=str(fm["doc_type"]))
        fm["primary_domain"]  = Prompt.ask("Primary domain",  default=str(fm["primary_domain"]))
        fm["knowledge_level"] = Prompt.ask("Knowledge level", default=str(fm["knowledge_level"]))
        fm["status"]          = Prompt.ask(
            "Status",
            default=str(fm["status"]),
            choices=["draft", "developing", "evergreen", "archived",
                     "seedling", "budding"],
        )
        fm["confidence"]      = Prompt.ask(
            "Confidence", default=str(fm["confidence"]),
            choices=["low", "medium", "high"],
        )
        # Secondary domains as comma-separated input
        sec = Prompt.ask(
            "Secondary domains (comma-separated, blank = none)",
            default=", ".join(fm["secondary_domains"]) if fm["secondary_domains"] else "",
        )
        fm["secondary_domains"] = [s.strip() for s in sec.split(",") if s.strip()]

        # Tags review
        tags_in = Prompt.ask(
            "Tags (comma-separated, # optional)",
            default=", ".join(fm["tags"]) if fm["tags"] else "",
        )
        fm["tags"] = [
            (t.strip() if t.strip().startswith("#") else f"#{t.strip()}")
            for t in tags_in.split(",") if t.strip()
        ]

        # Summary
        if Confirm.ask("Edit summary?", default=False):
            fm["summary"] = Prompt.ask("Summary", default=str(fm["summary"]))

    return fm


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

@click.command()
@click.argument("filepath", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--dry-run", is_flag=True, default=False,
              help="Print the proposed frontmatter without modifying the file.")
@click.option("--non-interactive", is_flag=True, default=False,
              help="Skip prompts; use defaults for missing fields.")
@click.option("--overwrite", is_flag=True, default=False,
              help="Replace existing frontmatter entirely (default: merge & preserve).")
@click.option("--backup/--no-backup", default=True,
              help="Write a .bak copy before modifying (default: True).")
def main(filepath: Path, dry_run: bool, non_interactive: bool,
         overwrite: bool, backup: bool) -> None:
    """Generate or update YAML frontmatter for a markdown FILEPATH."""

    if filepath.suffix.lower() not in (".md", ".markdown"):
        console.print(f"[red]Not a markdown file: {filepath}[/red]")
        sys.exit(1)

    # Load existing post (frontmatter + body)
    try:
        post = frontmatter.load(filepath)
    except Exception as exc:
        console.print(f"[red]Failed to parse {filepath.name}: {exc}[/red]")
        sys.exit(1)

    existing = dict(post.metadata) if post.metadata else {}
    body     = post.content or ""

    console.print(f"\n[bold]📝 Frontmatter Generator[/bold]")
    console.print(f"File:     [cyan]{filepath}[/cyan]")
    console.print(f"Existing: [{'green]has frontmatter' if existing else 'yellow]no frontmatter'}[/]]")
    console.print(f"Mode:     [{'yellow]DRY RUN' if dry_run else 'green]WRITE'}[/]] · "
                  f"[{'yellow]non-interactive' if non_interactive else 'cyan]interactive'}[/]] · "
                  f"[{'red]overwrite' if overwrite else 'green]merge'}[/]]\n")

    fm = build_frontmatter(
        filepath=filepath,
        body=body,
        existing=existing,
        interactive=not non_interactive,
        overwrite=overwrite,
    )

    # Render the new frontmatter as YAML
    yaml_text = yaml.safe_dump(
        fm, sort_keys=False, allow_unicode=True, default_flow_style=False
    )
    console.rule("[bold cyan]Proposed frontmatter[/bold cyan]")
    console.print(Syntax(yaml_text, "yaml", theme="ansi_dark", line_numbers=False))

    if dry_run:
        console.print("\n[yellow]Dry run — no changes written. "
                      "Re-run without --dry-run to apply.[/yellow]")
        return

    if not non_interactive and not Confirm.ask(
        "\n[bold]Write this frontmatter to the file?[/bold]", default=True
    ):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    # Backup
    if backup:
        bak = filepath.with_suffix(filepath.suffix + ".bak")
        bak.write_text(
            filepath.read_text(encoding="utf-8"), encoding="utf-8"
        )
        console.print(f"[dim]Backup → {bak.name}[/dim]")

    # Write merged file
    new_post = frontmatter.Post(content=body, **fm)
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(frontmatter.dumps(new_post))
        f.write("\n")

    console.print(f"[green]✅ Wrote frontmatter to {filepath.name}[/green]\n")


if __name__ == "__main__":
    main()
