#!/usr/bin/env python3
"""
_common.py — Shared utilities for the extractor script suite.

Provides folder traversal, CLI argument parsing, and Markdown report
helpers used by every extractor (YAML, code blocks, wiki-links, callouts,
tables). Kept dependency-free (standard library only).
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Iterable

DEFAULT_EXCLUDES = {".obsidian", ".git", ".venv", "node_modules",
                    "_attachments", "_templates", "__pycache__"}


def build_arg_parser(description: str) -> argparse.ArgumentParser:
    """Standard CLI for every extractor."""
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--input", required=True,
                   help="Folder to scan (or single .md file)")
    p.add_argument("--output", default=None,
                   help="Report file path (default: <input>/<extractor>-report-<date>.md)")
    p.add_argument("--recursive", action="store_true",
                   help="Recurse into subfolders")
    p.add_argument("--exclude", default="",
                   help="Comma-separated folder names to skip")
    p.add_argument("--top", type=int, default=25,
                   help="Top-N rows in frequency tables (default: 25)")
    p.add_argument("--quiet", action="store_true", help="Suppress progress output")
    return p


def gather_markdown_files(input_path: Path, recursive: bool,
                          extra_excludes: Iterable[str] = ()) -> list[Path]:
    """Collect .md files honouring exclude rules."""
    excludes = DEFAULT_EXCLUDES | set(extra_excludes)
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() == ".md" else []

    iterator = input_path.rglob("*.md") if recursive else input_path.glob("*.md")
    return sorted(
        f for f in iterator
        if not any(part in excludes for part in f.parts)
    )


def resolve_output_path(args: argparse.Namespace, default_stem: str) -> Path:
    """Build the output path, defaulting to <input>/<stem>-<date>.md."""
    if args.output:
        return Path(args.output).expanduser().resolve()
    base = Path(args.input).expanduser().resolve()
    folder = base if base.is_dir() else base.parent
    date = datetime.now().strftime("%Y-%m-%d")
    return folder / f"{default_stem}-{date}.md"


def report_frontmatter(title: str, source: Path, file_count: int,
                       extractor: str) -> str:
    """Standard YAML frontmatter for every report."""
    today = datetime.now().strftime("%Y-%m-%d")
    return (
        "---\n"
        f'title: "{title}"\n'
        f'doc_type: "extraction-report"\n'
        f'extractor: "{extractor}"\n'
        f'source: "{source.as_posix()}"\n'
        f"file_count: {file_count}\n"
        f"doc_created: {today}\n"
        f"doc_modified: {today}\n"
        "tags:\n"
        "  - report/extraction\n"
        f"  - extractor/{extractor}\n"
        "---\n\n"
    )


def md_table(headers: list[str], rows: list[list]) -> str:
    """Render a Markdown table. Empty rows → '*(none)*' line."""
    if not rows:
        return "*(none found)*\n\n"
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        cells = [str(c).replace("|", "\\|").replace("\n", " ") for c in r]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n\n"


def safe_read(path: Path) -> str:
    """Read a markdown file, tolerating encoding issues."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def vault_relative(path: Path, root: Path) -> str:
    """Best-effort relative path for display."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()
