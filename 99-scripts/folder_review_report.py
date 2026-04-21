#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: folder_review_report.py
VERSION:     1.0.0
CREATED:     2026-04-21
AUTHOR:      PKB Scripting Architect (Claude)
================================================================================

PURPOSE:
    Review every Markdown file in a folder and emit a single, comprehensive
    Markdown REVIEW REPORT saved into that same folder. Focused on three
    pillars beyond raw indexing:
      1. THEME / TOPIC ANALYSIS — keyword frequency, common terms, tag clusters
      2. WIKI LINK ANALYTICS    — usage patterns, density, hub/orphan detection,
                                  most-linked targets, alias usage
      3. LINK INTEGRITY         — broken wiki-links, broken embeds, broken
                                  external URL syntax, missing references

DIFFERS FROM `vault_indexer.py`:
    - Indexer = navigational MOC of every doc (per-doc cards).
    - This script = ANALYTICAL REPORT (aggregate insights + integrity audit).
    - Designed to live alongside the files it reviews as a snapshot artifact.

DESIGN GOALS:
    - Efficient on large folders (streaming reads, single pass per file)
    - Zero required external dependencies (PyYAML used if available)
    - Defensive: never fails on a single bad file; logs and continues
    - Self-contained Markdown output with YAML frontmatter

INPUTS:
    --input    PATH   Folder to review (REQUIRED)
    --output   NAME   Report filename (default: _REVIEW-REPORT-<date>.md)
    --recursive       Recurse into subfolders (default: False)
    --vault    PATH   Vault root for cross-folder broken-link validation
                      (default: same as --input)
    --exclude  DIRS   Comma-separated folder names to skip
    --top      N      How many entries in 'top N' tables (default: 20)
    --stopwords FILE  Optional newline-delimited stopword file
    --dry-run         Print summary, do not write file
    --quiet           Suppress per-file progress output

USAGE:
    python folder_review_report.py --input "./03-notes"
    python folder_review_report.py --input "./04-library/philosophy" --recursive
    python folder_review_report.py --input "./00-inbox" --vault "." --top 30

OUTPUT:
    A single Markdown file with sections:
      - YAML frontmatter (date, file count, vault, settings)
      - Executive Summary
      - File Inventory (table)
      - Theme & Topic Analysis (keywords, tag clusters)
      - Wiki Link Analytics (density, hubs, orphans, top targets, aliases)
      - Link Integrity Report (broken wiki links, broken embeds)
      - Frontmatter Audit (missing fields, schema coverage)
      - Notable Patterns & Recommendations
================================================================================
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

# ── Optional YAML support ─────────────────────────────────────────────────────
try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ── CONFIGURATION DEFAULTS ────────────────────────────────────────────────────
DEFAULT_EXCLUDES = {".obsidian", ".git", ".trash", "_attachments", "node_modules", ".venv"}

DEFAULT_STOPWORDS = {
    # English filler
    "the","a","an","and","or","but","if","then","else","for","of","to","in","on",
    "at","by","with","from","as","is","are","was","were","be","been","being","have",
    "has","had","do","does","did","will","would","should","could","may","might","can",
    "this","that","these","those","it","its","they","them","their","there","here",
    "you","your","we","our","i","me","my","not","no","so","also","such","than",
    "into","about","over","under","between","through","during","before","after",
    "while","because","when","where","which","who","whom","how","what","why",
    "very","just","more","most","some","any","each","every","other","another",
    "one","two","three","first","second","new","old","make","made","use","used",
    "like","get","got","go","goes","see","seen","take","taken","know","known",
    # Markdown noise
    "https","http","www","com","org","md","png","jpg","yaml","yes","no","true","false",
}

# Regex patterns (compiled once)
RX_FRONTMATTER  = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
RX_WIKILINK     = re.compile(r"(?<!!)\[\[([^\[\]\|\n#]+?)(?:#([^\[\]\|\n]+?))?(?:\|([^\[\]\n]+?))?\]\]")
RX_EMBED        = re.compile(r"!\[\[([^\[\]\|\n]+?)(?:\|[^\[\]\n]+?)?\]\]")
RX_HEADING      = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
RX_CALLOUT      = re.compile(r"^>\s*\[!([a-zA-Z\-_]+)\]", re.MULTILINE)
RX_TAG_INLINE   = re.compile(r"(?<![\w\d/#])#([a-zA-Z][a-zA-Z0-9/_\-]*)")
RX_INLINE_FIELD = re.compile(r"\[\*?\*?([A-Za-z][A-Za-z0-9_\- ]*?)\*?\*?::\s*([^\]]+?)\]")
RX_EXT_LINK     = re.compile(r"(?<!!)\[([^\]\n]+?)\]\((https?://[^\)\s]+?)\)")
RX_WORD         = re.compile(r"\b[a-zA-Z][a-zA-Z\-']{2,}\b")
RX_CODE_FENCE   = re.compile(r"```[\s\S]*?```", re.MULTILINE)


# ── DATA STRUCTURES ───────────────────────────────────────────────────────────
@dataclass
class FileReview:
    path: Path
    rel_path: str
    size_bytes: int
    mtime: float
    title: str = ""
    word_count: int = 0
    heading_count: int = 0
    wikilinks: list[tuple[str, str]] = field(default_factory=list)  # (target, alias_or_target)
    embeds: list[str] = field(default_factory=list)
    callouts: Counter = field(default_factory=Counter)
    tags: set[str] = field(default_factory=set)
    body_tags: set[str] = field(default_factory=set)
    inline_fields: list[tuple[str, str]] = field(default_factory=list)
    external_links: list[tuple[str, str]] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    frontmatter_keys: set[str] = field(default_factory=set)
    has_frontmatter: bool = False
    parse_error: str | None = None


# ── CORE PARSING ──────────────────────────────────────────────────────────────
def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (metadata_dict, body_text). Empty dict if no/invalid frontmatter."""
    m = RX_FRONTMATTER.match(text)
    if not m:
        return {}, text
    raw_yaml = m.group(1)
    body = text[m.end():]

    if HAS_YAML:
        try:
            data = yaml.safe_load(raw_yaml) or {}
            return (data if isinstance(data, dict) else {}), body
        except Exception:
            pass

    # Naive fallback parser: top-level "key: value" only
    data: dict = {}
    for line in raw_yaml.splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, _, v = line.partition(":")
            data[k.strip()] = v.strip().strip('"').strip("'")
    return data, body


def review_file(path: Path, root: Path) -> FileReview:
    """Single-pass review of a markdown file. Defensive: never raises."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        rv = FileReview(path=path, rel_path=str(path.relative_to(root)),
                        size_bytes=0, mtime=0.0, parse_error=f"read error: {e}")
        return rv

    fm, body = parse_frontmatter(text)
    rv = FileReview(
        path=path,
        rel_path=str(path.relative_to(root)).replace("\\", "/"),
        size_bytes=path.stat().st_size,
        mtime=path.stat().st_mtime,
        has_frontmatter=bool(fm),
        frontmatter_keys=set(fm.keys()),
    )

    # Title resolution
    rv.title = (str(fm.get("title") or fm.get("prompt_title") or "")).strip()
    if not rv.title:
        first_h = RX_HEADING.search(body)
        rv.title = first_h.group(2).strip() if first_h else path.stem

    # Aliases
    aliases = fm.get("aliases", [])
    if isinstance(aliases, str):
        aliases = [aliases]
    rv.aliases = [str(a).strip() for a in (aliases or []) if str(a).strip()]

    # Tags from frontmatter
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = re.split(r"[,\s]+", tags)
    rv.tags = {str(t).lstrip("#").strip() for t in (tags or []) if str(t).strip()}

    # Strip code fences before scanning body for tags/links to reduce noise
    body_clean = RX_CODE_FENCE.sub("", body)

    # Body tags
    rv.body_tags = {m.group(1) for m in RX_TAG_INLINE.finditer(body_clean)}

    # Wiki links: (target, displayed_alias)
    for m in RX_WIKILINK.finditer(body_clean):
        target = m.group(1).strip()
        alias = (m.group(3) or target).strip()
        rv.wikilinks.append((target, alias))

    # Embeds
    rv.embeds = [m.group(1).strip() for m in RX_EMBED.finditer(body_clean)]

    # Headings, callouts, inline fields, external links
    rv.heading_count = len(RX_HEADING.findall(body_clean))
    for m in RX_CALLOUT.finditer(body_clean):
        rv.callouts[m.group(1).lower()] += 1
    rv.inline_fields = [(m.group(1).strip(), m.group(2).strip())
                        for m in RX_INLINE_FIELD.finditer(body_clean)]
    rv.external_links = [(m.group(1), m.group(2))
                         for m in RX_EXT_LINK.finditer(body_clean)]

    # Word count (after removing code blocks)
    rv.word_count = len(RX_WORD.findall(body_clean))

    return rv


# ── COLLECTION ────────────────────────────────────────────────────────────────
def gather_markdown_files(root: Path, recursive: bool, excludes: set[str]) -> list[Path]:
    if recursive:
        return [p for p in root.rglob("*.md")
                if not any(part in excludes for part in p.relative_to(root).parts)]
    return sorted(p for p in root.glob("*.md") if p.is_file())


def index_vault_targets(vault_root: Path) -> set[str]:
    """Build a lowercase set of all note stems (and folder/stem) for link validation."""
    targets: set[str] = set()
    for p in vault_root.rglob("*.md"):
        if any(ex in p.parts for ex in DEFAULT_EXCLUDES):
            continue
        targets.add(p.stem.lower())
        # Also allow folder/stem style references
        try:
            rel = p.relative_to(vault_root).with_suffix("")
            targets.add(str(rel).replace("\\", "/").lower())
        except ValueError:
            pass
    return targets


# ── ANALYSIS ──────────────────────────────────────────────────────────────────
def analyze_themes(reviews: list[FileReview], stopwords: set[str], top_n: int) -> dict:
    word_counter: Counter = Counter()
    tag_counter: Counter = Counter()
    heading_words: Counter = Counter()
    bigrams: Counter = Counter()

    for rv in reviews:
        # Collect from title + all wiki link aliases (high-signal terms)
        seed_text = " ".join([rv.title] + [a for _, a in rv.wikilinks])
        words = [w.lower() for w in RX_WORD.findall(seed_text)
                 if w.lower() not in stopwords and len(w) > 2]
        word_counter.update(words)

        # Tag aggregation (frontmatter + body)
        for t in rv.tags | rv.body_tags:
            tag_counter[t] += 1

        # Bigrams from titles
        title_words = [w.lower() for w in RX_WORD.findall(rv.title)
                       if w.lower() not in stopwords]
        for a, b in zip(title_words, title_words[1:]):
            bigrams[f"{a} {b}"] += 1
        heading_words.update(title_words)

    return {
        "top_keywords": word_counter.most_common(top_n),
        "top_tags": tag_counter.most_common(top_n),
        "top_bigrams": bigrams.most_common(min(top_n, 15)),
        "title_words": heading_words.most_common(top_n),
        "unique_keywords": len(word_counter),
        "unique_tags": len(tag_counter),
    }


def analyze_wiki_links(reviews: list[FileReview], top_n: int) -> dict:
    out_counter: Counter = Counter()      # how often each target is linked TO
    incoming: dict[str, set[str]] = defaultdict(set)   # target → set of sources
    aliased: Counter = Counter()          # links that use |alias syntax
    per_doc_density: list[tuple[str, float]] = []
    total_links = 0
    docs_no_links = []
    docs_with_links = 0

    for rv in reviews:
        n = len(rv.wikilinks)
        total_links += n
        if n == 0:
            docs_no_links.append(rv.rel_path)
        else:
            docs_with_links += 1
        if rv.word_count > 0:
            per_doc_density.append((rv.rel_path, n / max(rv.word_count, 1) * 1000))
        for target, alias in rv.wikilinks:
            key = target.lower()
            out_counter[target] += 1
            incoming[key].add(rv.rel_path)
            if alias.lower() != target.lower():
                aliased[f"{target} → {alias}"] += 1

    # Hubs = files with most outgoing links
    hubs = sorted(
        ((rv.rel_path, len(rv.wikilinks)) for rv in reviews),
        key=lambda x: x[1], reverse=True
    )[:top_n]

    # Orphans within scope: files in folder with zero incoming links from other reviewed files
    in_scope_stems = {Path(rv.rel_path).stem.lower() for rv in reviews}
    orphans = []
    for rv in reviews:
        stem = Path(rv.rel_path).stem.lower()
        # Did any other reviewed file link here?
        linkers = incoming.get(stem, set()) - {rv.rel_path}
        if not linkers:
            orphans.append(rv.rel_path)

    return {
        "total_links": total_links,
        "unique_targets": len(out_counter),
        "docs_with_links": docs_with_links,
        "docs_without_links": docs_no_links,
        "top_targets": out_counter.most_common(top_n),
        "hubs": hubs,
        "orphans_in_scope": orphans,
        "aliased_links": aliased.most_common(min(top_n, 15)),
        "avg_links_per_doc": (total_links / len(reviews)) if reviews else 0,
        "highest_density": sorted(per_doc_density, key=lambda x: x[1], reverse=True)[:10],
    }


def analyze_link_integrity(reviews: list[FileReview], vault_targets: set[str]) -> dict:
    broken_wiki: list[tuple[str, str]] = []     # (source, broken_target)
    broken_embeds: list[tuple[str, str]] = []
    suspicious_external: list[tuple[str, str]] = []

    for rv in reviews:
        for target, _alias in rv.wikilinks:
            key = target.lower().strip()
            # Strip any folder path prefix and try both
            stem_only = key.rsplit("/", 1)[-1]
            if key not in vault_targets and stem_only not in vault_targets:
                broken_wiki.append((rv.rel_path, target))

        for target in rv.embeds:
            key = target.lower().strip()
            stem_only = key.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            # Embeds can be images/files; only flag if it looks like a note (.md or no ext)
            if "." not in target or target.lower().endswith(".md"):
                if stem_only not in vault_targets and key not in vault_targets:
                    broken_embeds.append((rv.rel_path, target))

        for text, url in rv.external_links:
            if " " in url or url.endswith((",", ".", ")")):
                suspicious_external.append((rv.rel_path, url))

    return {
        "broken_wiki": broken_wiki,
        "broken_embeds": broken_embeds,
        "suspicious_external": suspicious_external,
    }


def analyze_frontmatter(reviews: list[FileReview], top_n: int) -> dict:
    field_counter: Counter = Counter()
    missing_fm = []
    for rv in reviews:
        if not rv.has_frontmatter:
            missing_fm.append(rv.rel_path)
        else:
            field_counter.update(rv.frontmatter_keys)
    total = len(reviews) or 1
    coverage = [(k, v, f"{(v / total) * 100:.1f}%")
                for k, v in field_counter.most_common(top_n)]
    return {
        "missing_frontmatter": missing_fm,
        "field_coverage": coverage,
        "total_unique_fields": len(field_counter),
    }


# ── REPORT RENDERING ──────────────────────────────────────────────────────────
def fmt_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def fmt_date(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


def render_report(
    folder: Path,
    reviews: list[FileReview],
    themes: dict,
    links: dict,
    integrity: dict,
    fm_audit: dict,
    args: argparse.Namespace,
) -> str:
    today = datetime.now(timezone.utc).astimezone()
    total_words = sum(r.word_count for r in reviews)
    total_size = sum(r.size_bytes for r in reviews)
    parse_errs = [r for r in reviews if r.parse_error]

    lines: list[str] = []

    # ── YAML FRONTMATTER ─────────────────────────────────────────────────────
    lines += [
        "---",
        f'title: "Folder Review Report — {folder.name}"',
        'doc_type: "review-report"',
        f"report_date: {today.strftime('%Y-%m-%d')}",
        f"report_timestamp: \"{today.isoformat(timespec='seconds')}\"",
        f"folder_reviewed: \"{folder.as_posix()}\"",
        f"recursive: {str(args.recursive).lower()}",
        f"files_reviewed: {len(reviews)}",
        f"total_words: {total_words}",
        f"total_size_bytes: {total_size}",
        f"total_wikilinks: {links['total_links']}",
        f"broken_wikilinks: {len(integrity['broken_wiki'])}",
        f"script: \"folder_review_report.py v1.0.0\"",
        "tags:",
        "  - report/folder-review",
        "  - generated/automated",
        "status: \"generated\"",
        "---",
        "",
        f"# 📋 Folder Review Report — `{folder.name}`",
        "",
        f"*Generated {today.strftime('%Y-%m-%d %H:%M %Z')} by `folder_review_report.py`*",
        "",
    ]

    # ── EXECUTIVE SUMMARY ────────────────────────────────────────────────────
    lines += [
        "## 📊 Executive Summary",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Folder | `{folder.as_posix()}` |",
        f"| Recursive scan | {'Yes' if args.recursive else 'No'} |",
        f"| Files reviewed | **{len(reviews)}** |",
        f"| Total words | {total_words:,} |",
        f"| Avg words/file | {(total_words // len(reviews)) if reviews else 0:,} |",
        f"| Total size | {fmt_size(total_size)} |",
        f"| Total wiki-links | {links['total_links']:,} |",
        f"| Avg links/file | {links['avg_links_per_doc']:.1f} |",
        f"| Unique link targets | {links['unique_targets']:,} |",
        f"| Files with frontmatter | {len(reviews) - len(fm_audit['missing_frontmatter'])} / {len(reviews)} |",
        f"| 🔴 Broken wiki-links | **{len(integrity['broken_wiki'])}** |",
        f"| 🔴 Broken embeds | **{len(integrity['broken_embeds'])}** |",
        f"| ⚠️ Files missing frontmatter | {len(fm_audit['missing_frontmatter'])} |",
        f"| ⚠️ Files with zero links | {len(links['docs_without_links'])} |",
        f"| ⚠️ Parse errors | {len(parse_errs)} |",
        "",
    ]

    # ── FILE INVENTORY ───────────────────────────────────────────────────────
    lines += [
        "## 📁 File Inventory",
        "",
        "| # | File | Words | Links | Tags | Modified |",
        "|---|---|---:|---:|---:|---|",
    ]
    for i, rv in enumerate(sorted(reviews, key=lambda r: r.rel_path), 1):
        lines.append(
            f"| {i} | [[{Path(rv.rel_path).stem}\\|{Path(rv.rel_path).stem}]] "
            f"| {rv.word_count:,} | {len(rv.wikilinks)} | {len(rv.tags | rv.body_tags)} "
            f"| {fmt_date(rv.mtime)} |"
        )
    lines.append("")

    # ── THEME / TOPIC ANALYSIS ───────────────────────────────────────────────
    lines += [
        "## 🎯 Theme & Topic Analysis",
        "",
        f"*Extracted from titles and wiki-link aliases (signal-rich terms). "
        f"Stopwords filtered. {themes['unique_keywords']:,} unique keywords found.*",
        "",
        "### Top Keywords",
        "",
        "| Rank | Keyword | Frequency |",
        "|---:|---|---:|",
    ]
    for i, (word, count) in enumerate(themes["top_keywords"], 1):
        lines.append(f"| {i} | `{word}` | {count} |")
    lines.append("")

    if themes["top_bigrams"]:
        lines += [
            "### Common Phrases (Title Bigrams)",
            "",
            "| Phrase | Count |",
            "|---|---:|",
        ]
        for phrase, count in themes["top_bigrams"]:
            lines.append(f"| `{phrase}` | {count} |")
        lines.append("")

    if themes["top_tags"]:
        lines += [
            "### Tag Cluster",
            "",
            f"*{themes['unique_tags']} unique tags across folder.*",
            "",
            "| Tag | Frequency |",
            "|---|---:|",
        ]
        for tag, count in themes["top_tags"]:
            lines.append(f"| `#{tag}` | {count} |")
        lines.append("")

    # ── WIKI LINK ANALYTICS ──────────────────────────────────────────────────
    lines += [
        "## 🔗 Wiki Link Analytics",
        "",
        "### Most-Linked Targets (within and beyond folder)",
        "",
        "| Target | Times Linked |",
        "|---|---:|",
    ]
    for target, count in links["top_targets"]:
        lines.append(f"| [[{target}]] | {count} |")
    lines.append("")

    lines += [
        "### Connection Hubs (most outgoing links)",
        "",
        "| File | Outgoing Links |",
        "|---|---:|",
    ]
    for rel, count in links["hubs"]:
        if count == 0:
            continue
        lines.append(f"| [[{Path(rel).stem}]] | {count} |")
    lines.append("")

    if links["highest_density"]:
        lines += [
            "### Highest Link Density (links per 1000 words)",
            "",
            "| File | Density |",
            "|---|---:|",
        ]
        for rel, density in links["highest_density"]:
            lines.append(f"| [[{Path(rel).stem}]] | {density:.2f} |")
        lines.append("")

    if links["aliased_links"]:
        lines += [
            "### Notable Aliased Links",
            "",
            "| Link Pattern | Count |",
            "|---|---:|",
        ]
        for pattern, count in links["aliased_links"]:
            lines.append(f"| `{pattern}` | {count} |")
        lines.append("")

    if links["orphans_in_scope"]:
        lines += [
            "### Orphans Within Folder (no incoming links from other reviewed files)",
            "",
        ]
        for rel in links["orphans_in_scope"][:50]:
            lines.append(f"- [[{Path(rel).stem}]]")
        if len(links["orphans_in_scope"]) > 50:
            lines.append(f"- *…and {len(links['orphans_in_scope']) - 50} more*")
        lines.append("")

    # ── LINK INTEGRITY ───────────────────────────────────────────────────────
    lines += [
        "## 🚨 Link Integrity Report",
        "",
    ]
    if integrity["broken_wiki"]:
        lines += [
            f"### Broken Wiki-Links ({len(integrity['broken_wiki'])})",
            "",
            "| Source File | Broken Target |",
            "|---|---|",
        ]
        for src, target in integrity["broken_wiki"][:200]:
            lines.append(f"| [[{Path(src).stem}]] | `[[{target}]]` |")
        if len(integrity["broken_wiki"]) > 200:
            lines.append(f"| *…and {len(integrity['broken_wiki']) - 200} more* | |")
        lines.append("")
    else:
        lines += ["> [!success] ✅ No broken wiki-links detected.", ""]

    if integrity["broken_embeds"]:
        lines += [
            f"### Broken Embeds ({len(integrity['broken_embeds'])})",
            "",
            "| Source | Broken Embed |",
            "|---|---|",
        ]
        for src, target in integrity["broken_embeds"][:100]:
            lines.append(f"| [[{Path(src).stem}]] | `![[{target}]]` |")
        lines.append("")

    if integrity["suspicious_external"]:
        lines += [
            f"### Suspicious External URLs ({len(integrity['suspicious_external'])})",
            "",
            "| Source | URL |",
            "|---|---|",
        ]
        for src, url in integrity["suspicious_external"][:50]:
            lines.append(f"| [[{Path(src).stem}]] | `{url}` |")
        lines.append("")

    # ── FRONTMATTER AUDIT ────────────────────────────────────────────────────
    lines += [
        "## 🧾 Frontmatter Audit",
        "",
        f"*{fm_audit['total_unique_fields']} unique frontmatter fields detected across folder.*",
        "",
        "### Field Coverage",
        "",
        "| Field | Count | Coverage |",
        "|---|---:|---:|",
    ]
    for field_name, count, pct in fm_audit["field_coverage"]:
        lines.append(f"| `{field_name}` | {count} | {pct} |")
    lines.append("")

    if fm_audit["missing_frontmatter"]:
        lines += [
            f"### Files Missing Frontmatter ({len(fm_audit['missing_frontmatter'])})",
            "",
        ]
        for rel in fm_audit["missing_frontmatter"][:50]:
            lines.append(f"- [[{Path(rel).stem}]]")
        lines.append("")

    # ── PARSE ERRORS ─────────────────────────────────────────────────────────
    if parse_errs:
        lines += [
            "## ⚠️ Parse Errors",
            "",
            "| File | Error |",
            "|---|---|",
        ]
        for rv in parse_errs:
            lines.append(f"| `{rv.rel_path}` | {rv.parse_error} |")
        lines.append("")

    # ── RECOMMENDATIONS ──────────────────────────────────────────────────────
    lines += [
        "## 💡 Notable Patterns & Recommendations",
        "",
    ]
    recs = []
    if integrity["broken_wiki"]:
        recs.append(f"- **Fix {len(integrity['broken_wiki'])} broken wiki-link(s)** — "
                    "either create the missing notes or update the references.")
    if fm_audit["missing_frontmatter"]:
        recs.append(f"- **Add frontmatter to {len(fm_audit['missing_frontmatter'])} file(s)** "
                    "to enable Dataview queries and standardise metadata.")
    if links["docs_without_links"]:
        recs.append(f"- **{len(links['docs_without_links'])} file(s) have zero outgoing links** — "
                    "consider connecting them into the knowledge graph.")
    if links["orphans_in_scope"]:
        recs.append(f"- **{len(links['orphans_in_scope'])} file(s) are orphans within this folder** — "
                    "no other reviewed file links to them.")
    avg_density = (links["total_links"] / max(total_words, 1)) * 1000
    if avg_density < 2:
        recs.append(f"- **Low overall link density** ({avg_density:.2f} links/1000 words) — "
                    "the folder is text-heavy but graph-light.")
    if not recs:
        recs.append("- ✅ Folder appears healthy — no major issues detected.")
    lines += recs
    lines += ["", "---", "", f"*Report generated in single pass over {len(reviews)} file(s).*", ""]

    return "\n".join(lines)


# ── MAIN ──────────────────────────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate a comprehensive Markdown review report for a folder of notes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--input", required=True, help="Folder to review")
    p.add_argument("--output", default=None,
                   help="Report filename (default: _REVIEW-REPORT-<date>.md)")
    p.add_argument("--recursive", action="store_true", help="Recurse into subfolders")
    p.add_argument("--vault", default=None,
                   help="Vault root for cross-folder broken-link checks (default: --input)")
    p.add_argument("--exclude", default="",
                   help="Comma-separated folder names to skip when recursive")
    p.add_argument("--top", type=int, default=20, help="Top N rows in tables")
    p.add_argument("--stopwords", default=None, help="Path to newline-delimited stopword file")
    p.add_argument("--dry-run", action="store_true", help="Print summary, do not write file")
    p.add_argument("--quiet", action="store_true", help="Suppress per-file progress")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    folder = Path(args.input).expanduser().resolve()
    if not folder.is_dir():
        print(f"❌ Not a directory: {folder}", file=sys.stderr)
        return 2

    excludes = DEFAULT_EXCLUDES | {x.strip() for x in args.exclude.split(",") if x.strip()}
    vault_root = Path(args.vault).expanduser().resolve() if args.vault else folder

    # Stopwords
    stopwords = set(DEFAULT_STOPWORDS)
    if args.stopwords:
        try:
            stopwords |= {ln.strip().lower() for ln in Path(args.stopwords).read_text().splitlines()
                          if ln.strip()}
        except OSError as e:
            print(f"⚠️ Could not read stopword file: {e}", file=sys.stderr)

    # Phase 1: gather files
    t0 = time.perf_counter()
    files = gather_markdown_files(folder, args.recursive, excludes)
    if not files:
        print(f"⚠️ No markdown files found in {folder}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"📂 Reviewing {len(files)} file(s) in {folder}")
        if not HAS_YAML:
            print("ℹ️  PyYAML not installed — using fallback parser. "
                  "Run `pip install pyyaml` for richer frontmatter parsing.")

    # Phase 2: review each file
    reviews: list[FileReview] = []
    for i, fp in enumerate(files, 1):
        if not args.quiet and (i % 50 == 0 or i == len(files)):
            print(f"  ...processed {i}/{len(files)}")
        try:
            reviews.append(review_file(fp, folder))
        except Exception as e:  # ultimate safety net
            reviews.append(FileReview(
                path=fp, rel_path=str(fp.relative_to(folder)),
                size_bytes=0, mtime=0.0, parse_error=f"unhandled: {e}"
            ))

    # Phase 3: vault index for link integrity
    if not args.quiet:
        print(f"🔍 Indexing vault targets from {vault_root} for broken-link check...")
    vault_targets = index_vault_targets(vault_root)

    # Phase 4: analyses
    themes = analyze_themes(reviews, stopwords, args.top)
    link_stats = analyze_wiki_links(reviews, args.top)
    integrity = analyze_link_integrity(reviews, vault_targets)
    fm_audit = analyze_frontmatter(reviews, args.top)

    # Phase 5: render
    report = render_report(folder, reviews, themes, link_stats, integrity, fm_audit, args)

    # Phase 6: output
    out_name = args.output or f"_REVIEW-REPORT-{datetime.now().strftime('%Y-%m-%d')}.md"
    out_path = folder / out_name

    elapsed = time.perf_counter() - t0

    def _safe_print(text: str) -> None:
        enc = sys.stdout.encoding or "utf-8"
        sys.stdout.write(text.encode(enc, errors="replace").decode(enc) + "\n")

    if args.dry_run:
        _safe_print(f"\n--- DRY RUN -- would write {len(report):,} chars to {out_path} ---\n")
        _safe_print(report[:1500] + ("\n...[truncated]..." if len(report) > 1500 else ""))
        _safe_print(f"\nCompleted in {elapsed:.2f}s")
        return 0

    try:
        out_path.write_text(report, encoding="utf-8")
    except OSError as e:
        print(f"❌ Failed to write report: {e}", file=sys.stderr)
        return 3

    print(f"✅ Report written: {out_path}")
    print(f"   {len(reviews)} files · {link_stats['total_links']} links · "
          f"{len(integrity['broken_wiki'])} broken · {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
