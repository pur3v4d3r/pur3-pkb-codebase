#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: vault_indexer.py
VERSION:     1.0.0
CREATED:     2026-03-13
AUTHOR:      PKB Scripting Architect (Claude)
================================================================================

PURPOSE:
    Index an Obsidian vault folder (or any directory of Markdown files) and
    produce a comprehensive Markdown index document with:
      - YAML frontmatter for the index itself
      - Wikilinks to every discovered document
      - Per-document metadata extracted from each file's frontmatter,
        content structure, and filesystem attributes
      - Aggregate statistics, tag taxonomies, status breakdowns,
        category distributions, and health indicators

DESIGN PHILOSOPHY:
    An index is more than a list of links — it is a navigational map.
    This script produces a living document that surfaces buried structure,
    exposes patterns in your knowledge base, and gives you a dashboard-
    quality overview of any folder's contents.

WHAT IT EXTRACTS PER DOCUMENT:
    - Filesystem: file size, creation date, modification date, path depth
    - Frontmatter: title, tags, aliases, status, certainty, note_type,
                   knowledge_level, and ALL other custom YAML fields
    - Content analysis: heading count, word count, wiki-link count,
                        outgoing links list, callout count, code block count,
                        has dataview queries, has templater blocks,
                        first heading (as inferred title)
    - Derived: estimated read time, content density score,
               connectivity score, staleness indicator

AGGREGATE INDEX FEATURES:
    - Total document count, combined word count, combined file size
    - Tag frequency cloud / table
    - Status distribution breakdown
    - Note type distribution
    - Connectivity overview (most/least linked)
    - Recently modified documents
    - Stale documents (not modified in configurable days)
    - Documents missing frontmatter
    - Alphabetical wikilink directory with per-doc metadata cards

INPUTS:
    --input   PATH    Folder to index (required)
    --output  PATH    Where to write the index .md file (default: <input>/_index.md)
    --name    NAME    Custom name for the index file (default: _index)
    --depth   N       Max folder recursion depth (default: unlimited)
    --exclude DIRS    Comma-separated folder names to skip
    --stale   DAYS    Days since modification to flag as stale (default: 30)
    --no-content      Skip content analysis (faster, metadata/filesystem only)
    --dry-run         Print summary to console without writing file

USAGE:
    python vault_indexer.py --input "D:/vault/04-library/philosophy"
    python vault_indexer.py --input "./03-notes" --output "./07-mocs/notes-index.md"
    python vault_indexer.py --input "./04-library" --stale 60 --exclude "_templates,_archive"
    python vault_indexer.py --input "." --depth 1 --name "root-index"

REQUIREMENTS:
    Python 3.8+
    No external libraries required (standard library only)
    Optional: pip install pyyaml  (for robust YAML frontmatter parsing)

NOTES:
    - Designed for Obsidian-flavored Markdown
    - Handles nested YAML, bullet-list tags/aliases, and complex frontmatter
    - All wikilinks in the output use Obsidian [[Note Name]] format
    - UTF-8 encoding throughout
    - Safe: read-only on source files, only writes the index output
================================================================================
"""

# ══════════════════════════════════════════════════════════════════════════════
# IMPORTS
# ══════════════════════════════════════════════════════════════════════════════

import re
import os
import sys
import argparse
import math
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, Counter

# ── Optional: Enhanced YAML parsing ───────────────────────────────────────────
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTS & CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

SCRIPT_NAME = "vault_indexer.py"
SCRIPT_VERSION = "1.0.0"

# Average words per minute for read-time estimation
WORDS_PER_MINUTE = 200

# Directories to always exclude
DEFAULT_EXCLUDES = {
    ".git", ".obsidian", ".trash", ".venv", "node_modules",
    "__pycache__", ".DS_Store", "Thumbs.db",
}

# Regex patterns compiled once for performance
PATTERNS = {
    "frontmatter":   re.compile(r"^---\n(.*?)\n---", re.DOTALL),
    "wikilink":      re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]"),
    "heading":       re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE),
    "callout":       re.compile(r"^>\s*\[!(\w[\w-]*)\]", re.MULTILINE),
    "code_block":    re.compile(r"^```(\w*)", re.MULTILINE),
    "tag_inline":    re.compile(r"(?:^|\s)#([a-zA-Z][a-zA-Z0-9_/-]*)"),
    "dataview_block": re.compile(r"```dataview(?:js)?", re.MULTILINE),
    "templater":     re.compile(r"<%[*\-]?"),
    "inline_field":  re.compile(r"\[\*\*([^*]+)\*\*::\s*([^\]]+)\]"),
    "external_link": re.compile(r"\[([^\]]*)\]\((https?://[^)]+)\)"),
    "embed":         re.compile(r"!\[\[([^\]]+)\]\]"),
}


# ══════════════════════════════════════════════════════════════════════════════
# FRONTMATTER PARSER
# ══════════════════════════════════════════════════════════════════════════════

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """
    Extract and parse YAML frontmatter from markdown content.
    Uses PyYAML if available, falls back to regex-based parsing.

    Returns:
        Dictionary of all frontmatter key-value pairs.
    """
    match = PATTERNS["frontmatter"].match(content)
    if not match:
        return {}

    raw_yaml = match.group(1)

    # Try PyYAML first
    if YAML_AVAILABLE:
        try:
            parsed = yaml.safe_load(raw_yaml)
            return parsed if isinstance(parsed, dict) else {}
        except yaml.YAMLError:
            pass  # Fall through to regex parser

    # Fallback: regex-based key-value extraction
    parsed = {}
    current_key = None
    current_list = None

    for line in raw_yaml.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        kv_match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if kv_match and not line.startswith(" ") and not line.startswith("\t"):
            key = kv_match.group(1)
            value = kv_match.group(2).strip()
            current_key = key

            if value.startswith("[") and value.endswith("]"):
                items = [
                    v.strip().strip('"').strip("'")
                    for v in value[1:-1].split(",")
                    if v.strip()
                ]
                parsed[key] = items
                current_list = None
            elif value in ("", "[]"):
                parsed[key] = []
                current_list = key
            else:
                parsed[key] = value.strip('"').strip("'")
                current_list = None
        elif stripped.startswith("- ") and current_list:
            item = stripped[2:].strip().strip('"').strip("'")
            if isinstance(parsed.get(current_list), list):
                parsed[current_list].append(item)

    return parsed


# ══════════════════════════════════════════════════════════════════════════════
# CONTENT ANALYZER
# ══════════════════════════════════════════════════════════════════════════════

def analyze_content(content: str) -> Dict[str, Any]:
    """
    Perform structural analysis of markdown content.

    Returns dictionary with:
        word_count, heading_count, headings, wikilink_count, wikilinks,
        callout_count, callout_types, code_block_count, tag_count, tags,
        has_dataview, has_templater, inline_field_count, first_heading,
        external_link_count, embed_count
    """
    # Strip frontmatter for body analysis
    body = PATTERNS["frontmatter"].sub("", content, count=1).strip()

    # Word count (rough but fast)
    words = len(body.split())

    # Headings
    headings = PATTERNS["heading"].findall(body)
    heading_list = [(len(h[0]), h[1].strip()) for h in headings]
    first_heading = heading_list[0][1] if heading_list else None

    # Wikilinks
    wikilinks = PATTERNS["wikilink"].findall(body)
    wikilinks_clean = sorted(set(link.strip() for link in wikilinks))

    # Callouts
    callouts = PATTERNS["callout"].findall(body)
    callout_types = dict(Counter(callouts))

    # Code blocks
    code_blocks = PATTERNS["code_block"].findall(body)

    # Tags in body (not frontmatter)
    body_tags = PATTERNS["tag_inline"].findall(body)

    # Dataview / Templater presence
    has_dataview = bool(PATTERNS["dataview_block"].search(body))
    has_templater = bool(PATTERNS["templater"].search(body))

    # Inline fields
    inline_fields = PATTERNS["inline_field"].findall(body)

    # External links
    external_links = PATTERNS["external_link"].findall(body)

    # Embeds
    embeds = PATTERNS["embed"].findall(body)

    return {
        "word_count": words,
        "heading_count": len(heading_list),
        "headings": heading_list,
        "wikilink_count": len(wikilinks),
        "wikilinks": wikilinks_clean,
        "callout_count": len(callouts),
        "callout_types": callout_types,
        "code_block_count": len(code_blocks),
        "code_languages": list(set(c for c in code_blocks if c)),
        "body_tags": sorted(set(body_tags)),
        "has_dataview": has_dataview,
        "has_templater": has_templater,
        "inline_field_count": len(inline_fields),
        "first_heading": first_heading,
        "external_link_count": len(external_links),
        "embed_count": len(embeds),
    }


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT SCANNER
# ══════════════════════════════════════════════════════════════════════════════

def scan_document(filepath: Path, root: Path, skip_content: bool = False) -> Dict[str, Any]:
    """
    Scan a single markdown document and extract all metadata.

    Args:
        filepath: Absolute path to the .md file
        root: The root folder being indexed (for relative path calc)
        skip_content: If True, skip content analysis (faster)

    Returns:
        Dictionary of all extracted document metadata.
    """
    stat = filepath.stat()
    relative = filepath.relative_to(root)
    stem = filepath.stem

    # ── Filesystem metadata ────────────────────────────────────────────────
    file_size = stat.st_size
    # Use birthtime if available (macOS/some Windows), else ctime
    created_ts = stat.st_birthtime if hasattr(stat, "st_birthtime") else stat.st_ctime
    modified_ts = stat.st_mtime

    created_dt = datetime.fromtimestamp(created_ts)
    modified_dt = datetime.fromtimestamp(modified_ts)

    doc_info = {
        "filename": filepath.name,
        "stem": stem,
        "relative_path": str(relative).replace("\\", "/"),
        "parent_folder": relative.parent.name if relative.parent.name else "(root)",
        "path_depth": len(relative.parts) - 1,
        "file_size_bytes": file_size,
        "file_size_display": _format_size(file_size),
        "created_date": created_dt.strftime("%Y-%m-%d"),
        "created_datetime": created_dt.strftime("%Y-%m-%d %H:%M"),
        "modified_date": modified_dt.strftime("%Y-%m-%d"),
        "modified_datetime": modified_dt.strftime("%Y-%m-%d %H:%M"),
        "days_since_modified": (datetime.now() - modified_dt).days,
    }

    # ── Read content ───────────────────────────────────────────────────────
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        doc_info["error"] = str(e)
        doc_info["has_frontmatter"] = False
        doc_info["frontmatter"] = {}
        doc_info["content_analysis"] = {}
        return doc_info

    # ── Frontmatter ────────────────────────────────────────────────────────
    frontmatter = parse_frontmatter(content)
    doc_info["has_frontmatter"] = bool(frontmatter)
    doc_info["frontmatter"] = frontmatter

    # Extract commonly-used fields to top level for easy access
    doc_info["title"] = (
        frontmatter.get("title")
        or frontmatter.get("prompt_title")
        or None
    )
    doc_info["fm_tags"] = _normalize_list(frontmatter.get("tags", []))
    doc_info["fm_aliases"] = _normalize_list(frontmatter.get("aliases", []))
    doc_info["fm_status"] = frontmatter.get("status", "")
    doc_info["fm_certainty"] = frontmatter.get("certainty", "")
    doc_info["fm_note_type"] = (
        frontmatter.get("note_type")
        or frontmatter.get("doc_type")
        or frontmatter.get("type")
        or ""
    )
    doc_info["fm_knowledge_level"] = frontmatter.get("knowledge_level", "")

    # ── Content analysis ───────────────────────────────────────────────────
    if not skip_content:
        analysis = analyze_content(content)
        doc_info["content_analysis"] = analysis

        # Derived / computed fields
        doc_info["word_count"] = analysis["word_count"]
        doc_info["read_time_min"] = max(1, round(analysis["word_count"] / WORDS_PER_MINUTE))
        doc_info["outgoing_links"] = analysis["wikilinks"]
        doc_info["outgoing_link_count"] = analysis["wikilink_count"]

        # Inferred title: prefer frontmatter title, then first heading, then filename
        if not doc_info["title"]:
            doc_info["title"] = analysis["first_heading"] or stem

        # All tags: frontmatter + body
        all_tags = set(doc_info["fm_tags"]) | set(analysis["body_tags"])
        doc_info["all_tags"] = sorted(all_tags)

        # Content density: a rough quality signal
        # (headings + callouts + links per 1000 words)
        if analysis["word_count"] > 0:
            structure_points = (
                analysis["heading_count"]
                + analysis["callout_count"]
                + analysis["wikilink_count"]
                + analysis["inline_field_count"]
            )
            doc_info["content_density"] = round(
                structure_points / (analysis["word_count"] / 1000), 1
            )
        else:
            doc_info["content_density"] = 0
    else:
        doc_info["content_analysis"] = {}
        doc_info["word_count"] = 0
        doc_info["read_time_min"] = 0
        doc_info["outgoing_links"] = []
        doc_info["outgoing_link_count"] = 0
        doc_info["all_tags"] = doc_info["fm_tags"]
        doc_info["content_density"] = 0
        if not doc_info["title"]:
            doc_info["title"] = stem

    return doc_info


# ══════════════════════════════════════════════════════════════════════════════
# FOLDER SCANNER
# ══════════════════════════════════════════════════════════════════════════════

def scan_folder(
    input_path: Path,
    excludes: set,
    max_depth: Optional[int] = None,
    skip_content: bool = False,
) -> Tuple[List[Dict[str, Any]], Dict[str, List[str]]]:
    """
    Recursively scan a folder for markdown files and index them.

    Returns:
        (documents, folder_tree)
        - documents: list of per-document metadata dicts
        - folder_tree: dict mapping folder relative paths to lists of filenames
    """
    documents = []
    folder_tree: Dict[str, List[str]] = defaultdict(list)

    for dirpath, dirnames, filenames in os.walk(input_path):
        # Compute depth
        rel_dir = Path(dirpath).relative_to(input_path)
        depth = len(rel_dir.parts)

        # Prune excluded directories
        dirnames[:] = [
            d for d in dirnames
            if d not in excludes and not d.startswith(".")
        ]

        # Enforce depth limit
        if max_depth is not None and depth > max_depth:
            dirnames.clear()
            continue

        # Process markdown files
        for filename in sorted(filenames):
            if not filename.lower().endswith(".md"):
                continue

            filepath = Path(dirpath) / filename
            folder_key = str(rel_dir).replace("\\", "/") if str(rel_dir) != "." else "(root)"
            folder_tree[folder_key].append(filename)

            doc_info = scan_document(filepath, input_path, skip_content=skip_content)
            documents.append(doc_info)

    return documents, dict(folder_tree)


# ══════════════════════════════════════════════════════════════════════════════
# AGGREGATE STATISTICS
# ══════════════════════════════════════════════════════════════════════════════

def compute_aggregates(documents: List[Dict[str, Any]], stale_days: int) -> Dict[str, Any]:
    """
    Compute aggregate statistics across all indexed documents.
    """
    total = len(documents)
    if total == 0:
        return {"total_documents": 0}

    # ── Basic counts ───────────────────────────────────────────────────────
    total_words = sum(d.get("word_count", 0) for d in documents)
    total_size = sum(d.get("file_size_bytes", 0) for d in documents)
    total_links = sum(d.get("outgoing_link_count", 0) for d in documents)

    # ── Tag frequency ──────────────────────────────────────────────────────
    tag_counter = Counter()
    for doc in documents:
        for tag in doc.get("all_tags", []):
            tag_counter[tag] += 1

    # ── Status distribution ────────────────────────────────────────────────
    status_counter = Counter()
    for doc in documents:
        status = doc.get("fm_status", "") or "(none)"
        status_counter[status] += 1

    # ── Note type distribution ─────────────────────────────────────────────
    type_counter = Counter()
    for doc in documents:
        ntype = doc.get("fm_note_type", "") or "(untyped)"
        type_counter[ntype] += 1

    # ── Knowledge level distribution ───────────────────────────────────────
    level_counter = Counter()
    for doc in documents:
        level = doc.get("fm_knowledge_level", "") or "(none)"
        level_counter[level] += 1

    # ── Frontmatter health ─────────────────────────────────────────────────
    has_fm = sum(1 for d in documents if d.get("has_frontmatter"))
    missing_fm = total - has_fm

    # ── Staleness ──────────────────────────────────────────────────────────
    stale_docs = [
        d for d in documents
        if d.get("days_since_modified", 0) > stale_days
    ]

    # ── Recently modified (last 7 days) ────────────────────────────────────
    recent_docs = sorted(
        [d for d in documents if d.get("days_since_modified", 999) <= 7],
        key=lambda d: d.get("modified_datetime", ""),
        reverse=True,
    )[:15]

    # ── Most connected (by outgoing links) ─────────────────────────────────
    most_linked = sorted(
        documents,
        key=lambda d: d.get("outgoing_link_count", 0),
        reverse=True,
    )[:10]

    # ── Least connected ────────────────────────────────────────────────────
    least_linked = sorted(
        [d for d in documents if d.get("outgoing_link_count", 0) == 0],
        key=lambda d: d.get("word_count", 0),
        reverse=True,
    )

    # ── Largest documents ──────────────────────────────────────────────────
    largest_docs = sorted(
        documents,
        key=lambda d: d.get("word_count", 0),
        reverse=True,
    )[:10]

    # ── Folder distribution ────────────────────────────────────────────────
    folder_counter = Counter()
    for doc in documents:
        folder_counter[doc.get("parent_folder", "(root)")] += 1

    # ── Average metrics ────────────────────────────────────────────────────
    avg_words = round(total_words / total) if total else 0
    avg_links = round(total_links / total, 1) if total else 0
    densities = [d.get("content_density", 0) for d in documents]
    avg_density = round(sum(densities) / len(densities), 1) if densities else 0

    return {
        "total_documents": total,
        "total_words": total_words,
        "total_size_bytes": total_size,
        "total_size_display": _format_size(total_size),
        "total_links": total_links,
        "avg_word_count": avg_words,
        "avg_links_per_doc": avg_links,
        "avg_content_density": avg_density,
        "total_read_time_min": sum(d.get("read_time_min", 0) for d in documents),
        "has_frontmatter": has_fm,
        "missing_frontmatter": missing_fm,
        "tag_frequency": tag_counter.most_common(50),
        "status_distribution": dict(status_counter.most_common()),
        "type_distribution": dict(type_counter.most_common()),
        "level_distribution": dict(level_counter.most_common()),
        "folder_distribution": dict(folder_counter.most_common()),
        "stale_document_count": len(stale_docs),
        "stale_documents": stale_docs,
        "recent_documents": recent_docs,
        "most_linked": most_linked,
        "least_linked": least_linked[:15],
        "largest_documents": largest_docs,
    }


# ══════════════════════════════════════════════════════════════════════════════
# MARKDOWN INDEX RENDERER
# ══════════════════════════════════════════════════════════════════════════════

def render_index(
    documents: List[Dict[str, Any]],
    folder_tree: Dict[str, List[str]],
    aggregates: Dict[str, Any],
    input_path: Path,
    stale_days: int,
) -> str:
    """
    Render the complete Markdown index document.
    """
    now = datetime.now()
    folder_name = input_path.name
    total = aggregates["total_documents"]

    lines: List[str] = []

    def w(text: str = ""):
        lines.append(text)

    # ══════════════════════════════════════════════════════════════════════
    # YAML FRONTMATTER
    # ══════════════════════════════════════════════════════════════════════
    w("---")
    w(f'title: "Index — {folder_name}"')
    w(f'doc_type: "folder-index"')
    w(f'doc_created: {now.strftime("%Y-%m-%d")}')
    w(f'doc_modified: {now.strftime("%Y-%m-%d")}')
    w(f'indexed_folder: "{input_path}"')
    w(f"total_documents: {total}")
    w(f'total_words: {aggregates.get("total_words", 0)}')
    w(f'total_size: "{aggregates.get("total_size_display", "0 B")}"')
    w(f'generated_by: "{SCRIPT_NAME} v{SCRIPT_VERSION}"')
    w("status: evergreen")
    w("certainty: verified")
    w("tags:")
    w("  - index")
    w("  - auto-generated")
    w("  - folder-index")
    w("aliases:")
    w(f'  - "{folder_name} index"')
    w(f'  - "{folder_name} directory"')
    w("---")
    w()

    # ══════════════════════════════════════════════════════════════════════
    # HEADER
    # ══════════════════════════════════════════════════════════════════════
    w(f"# 📂 Index — {folder_name}")
    w()
    w(f"> [!abstract] Overview")
    w(f"> Auto-generated index of **{total}** documents in `{folder_name}/`.")
    w(f"> Generated on {now.strftime('%Y-%m-%d at %H:%M')} by `{SCRIPT_NAME}` v{SCRIPT_VERSION}.")
    w(f"> Total content: **{aggregates.get('total_words', 0):,}** words · "
      f"**{aggregates.get('total_size_display', '0 B')}** · "
      f"~**{aggregates.get('total_read_time_min', 0):,}** min read time.")
    w()

    if total == 0:
        w("> [!warning] Empty Folder")
        w("> No markdown documents found in this directory.")
        return "\n".join(lines)

    # ══════════════════════════════════════════════════════════════════════
    # TABLE OF CONTENTS
    # ══════════════════════════════════════════════════════════════════════
    w("## 📋 Table of Contents")
    w()
    w("1. [[#📊 Aggregate Statistics]]")
    w("2. [[#📁 Folder Structure]]")
    w("3. [[#🏷️ Tag Taxonomy]]")
    w("4. [[#📈 Status & Type Distribution]]")
    w("5. [[#🕐 Recently Modified]]")
    w("6. [[#⚠️ Stale Documents]]")
    w("7. [[#🔗 Connectivity Overview]]")
    w("8. [[#📏 Largest Documents]]")
    w("9. [[#🚨 Health Indicators]]")
    w("10. [[#📖 Document Directory]]")
    w()
    w("---")
    w()

    # ══════════════════════════════════════════════════════════════════════
    # 1. AGGREGATE STATISTICS
    # ══════════════════════════════════════════════════════════════════════
    w("## 📊 Aggregate Statistics")
    w()
    w("| Metric | Value |")
    w("|--------|-------|")
    w(f"| **Total Documents** | {total} |")
    w(f"| **Total Words** | {aggregates.get('total_words', 0):,} |")
    w(f"| **Total File Size** | {aggregates.get('total_size_display', '0 B')} |")
    w(f"| **Total Outgoing Links** | {aggregates.get('total_links', 0):,} |")
    w(f"| **Avg. Words/Document** | {aggregates.get('avg_word_count', 0):,} |")
    w(f"| **Avg. Links/Document** | {aggregates.get('avg_links_per_doc', 0)} |")
    w(f"| **Avg. Content Density** | {aggregates.get('avg_content_density', 0)} |")
    w(f"| **Est. Total Read Time** | ~{aggregates.get('total_read_time_min', 0):,} min |")
    w(f"| **With Frontmatter** | {aggregates.get('has_frontmatter', 0)} / {total} "
      f"({_pct(aggregates.get('has_frontmatter', 0), total)}) |")
    w(f"| **Missing Frontmatter** | {aggregates.get('missing_frontmatter', 0)} |")
    w(f"| **Stale (>{stale_days}d)** | {aggregates.get('stale_document_count', 0)} |")
    w()

    # ══════════════════════════════════════════════════════════════════════
    # 2. FOLDER STRUCTURE
    # ══════════════════════════════════════════════════════════════════════
    w("## 📁 Folder Structure")
    w()
    folder_dist = aggregates.get("folder_distribution", {})
    if folder_dist:
        w("| Folder | Document Count |")
        w("|--------|---------------|")
        for folder, count in sorted(folder_dist.items()):
            w(f"| `{folder}` | {count} |")
        w()

    # Directory tree
    if folder_tree:
        w("### Directory Tree")
        w()
        w("```")
        w(f"{folder_name}/")
        for folder_key in sorted(folder_tree.keys()):
            file_list = folder_tree[folder_key]
            if folder_key == "(root)":
                for f in file_list:
                    w(f"├── {f}")
            else:
                depth = folder_key.count("/")
                indent = "│   " * depth
                w(f"{indent}├── 📂 {folder_key.split('/')[-1]}/")
                for f in file_list:
                    w(f"{indent}│   ├── {f}")
        w("```")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 3. TAG TAXONOMY
    # ══════════════════════════════════════════════════════════════════════
    w("## 🏷️ Tag Taxonomy")
    w()
    tag_freq = aggregates.get("tag_frequency", [])
    if tag_freq:
        w("| Tag | Frequency | Bar |")
        w("|-----|-----------|-----|")
        max_count = tag_freq[0][1] if tag_freq else 1
        for tag, count in tag_freq[:30]:
            bar_len = max(1, round((count / max_count) * 20))
            bar = "█" * bar_len
            w(f"| `#{tag}` | {count} | {bar} |")
        w()
        if len(tag_freq) > 30:
            w(f"*... and {len(tag_freq) - 30} more tags*")
            w()
    else:
        w("*No tags found across indexed documents.*")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 4. STATUS & TYPE DISTRIBUTION
    # ══════════════════════════════════════════════════════════════════════
    w("## 📈 Status & Type Distribution")
    w()

    # Status
    status_dist = aggregates.get("status_distribution", {})
    if status_dist:
        w("### Status Breakdown")
        w()
        w("| Status | Count | % |")
        w("|--------|-------|---|")
        for status, count in status_dist.items():
            w(f"| **{status}** | {count} | {_pct(count, total)} |")
        w()

    # Note type
    type_dist = aggregates.get("type_distribution", {})
    if type_dist:
        w("### Note Type Breakdown")
        w()
        w("| Type | Count | % |")
        w("|------|-------|---|")
        for ntype, count in type_dist.items():
            w(f"| **{ntype}** | {count} | {_pct(count, total)} |")
        w()

    # Knowledge level
    level_dist = aggregates.get("level_distribution", {})
    if level_dist and not all(k == "(none)" for k in level_dist):
        w("### Knowledge Level Breakdown")
        w()
        w("| Level | Count | % |")
        w("|-------|-------|---|")
        for level, count in level_dist.items():
            w(f"| **{level}** | {count} | {_pct(count, total)} |")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 5. RECENTLY MODIFIED
    # ══════════════════════════════════════════════════════════════════════
    w("## 🕐 Recently Modified")
    w()
    recent = aggregates.get("recent_documents", [])
    if recent:
        w("| Document | Modified | Words | Status |")
        w("|----------|----------|-------|--------|")
        for doc in recent:
            link = f"[[{doc['stem']}]]"
            w(f"| {link} | {doc.get('modified_date', '—')} | "
              f"{doc.get('word_count', 0):,} | {doc.get('fm_status', '—')} |")
        w()
    else:
        w("*No documents modified in the last 7 days.*")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 6. STALE DOCUMENTS
    # ══════════════════════════════════════════════════════════════════════
    w("## ⚠️ Stale Documents")
    w()
    stale = aggregates.get("stale_documents", [])
    if stale:
        w(f"> [!warning] {len(stale)} documents not modified in over {stale_days} days")
        w()
        w("| Document | Last Modified | Days Stale | Status |")
        w("|----------|---------------|------------|--------|")
        stale_sorted = sorted(stale, key=lambda d: d.get("days_since_modified", 0), reverse=True)
        for doc in stale_sorted[:25]:
            link = f"[[{doc['stem']}]]"
            w(f"| {link} | {doc.get('modified_date', '—')} | "
              f"{doc.get('days_since_modified', '—')} | {doc.get('fm_status', '—')} |")
        if len(stale) > 25:
            w(f"\n*... and {len(stale) - 25} more stale documents*")
        w()
    else:
        w(f"*No documents older than {stale_days} days without modification. ✅*")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 7. CONNECTIVITY OVERVIEW
    # ══════════════════════════════════════════════════════════════════════
    w("## 🔗 Connectivity Overview")
    w()

    # Most connected
    most = aggregates.get("most_linked", [])
    if most:
        w("### Most Connected (by outgoing links)")
        w()
        w("| Document | Outgoing Links | Words | Density |")
        w("|----------|---------------|-------|---------|")
        for doc in most:
            link = f"[[{doc['stem']}]]"
            w(f"| {link} | {doc.get('outgoing_link_count', 0)} | "
              f"{doc.get('word_count', 0):,} | {doc.get('content_density', 0)} |")
        w()

    # Least connected (isolated)
    least = aggregates.get("least_linked", [])
    if least:
        w("### Isolated Documents (0 outgoing links)")
        w()
        w(f"> [!attention] {len(least)} documents have no outgoing wiki-links")
        w()
        w("| Document | Words | Status | Modified |")
        w("|----------|-------|--------|----------|")
        for doc in least:
            link = f"[[{doc['stem']}]]"
            w(f"| {link} | {doc.get('word_count', 0):,} | "
              f"{doc.get('fm_status', '—')} | {doc.get('modified_date', '—')} |")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 8. LARGEST DOCUMENTS
    # ══════════════════════════════════════════════════════════════════════
    w("## 📏 Largest Documents")
    w()
    largest = aggregates.get("largest_documents", [])
    if largest:
        w("| Document | Words | Read Time | File Size | Links |")
        w("|----------|-------|-----------|-----------|-------|")
        for doc in largest:
            link = f"[[{doc['stem']}]]"
            w(f"| {link} | {doc.get('word_count', 0):,} | "
              f"~{doc.get('read_time_min', 0)} min | "
              f"{doc.get('file_size_display', '—')} | "
              f"{doc.get('outgoing_link_count', 0)} |")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 9. HEALTH INDICATORS
    # ══════════════════════════════════════════════════════════════════════
    w("## 🚨 Health Indicators")
    w()

    # Missing frontmatter
    no_fm = [d for d in documents if not d.get("has_frontmatter")]
    if no_fm:
        w(f"### Missing Frontmatter ({len(no_fm)} documents)")
        w()
        w("> [!important] These documents have no YAML frontmatter")
        w()
        for doc in sorted(no_fm, key=lambda d: d["stem"]):
            w(f"- [[{doc['stem']}]]")
        w()

    # Empty documents (under 50 words)
    empty_docs = [d for d in documents if d.get("word_count", 0) < 50]
    if empty_docs:
        w(f"### Near-Empty Documents ({len(empty_docs)} under 50 words)")
        w()
        for doc in sorted(empty_docs, key=lambda d: d.get("word_count", 0)):
            w(f"- [[{doc['stem']}]] — {doc.get('word_count', 0)} words")
        w()

    # Documents without tags
    no_tags = [d for d in documents if not d.get("all_tags")]
    if no_tags:
        w(f"### Missing Tags ({len(no_tags)} documents)")
        w()
        for doc in sorted(no_tags, key=lambda d: d["stem"]):
            w(f"- [[{doc['stem']}]]")
        w()

    if not no_fm and not empty_docs and not no_tags:
        w("> [!tip] All Clear")
        w("> All documents have frontmatter, content, and tags. ✅")
        w()

    # ══════════════════════════════════════════════════════════════════════
    # 10. DOCUMENT DIRECTORY
    # ══════════════════════════════════════════════════════════════════════
    w("---")
    w()
    w("## 📖 Document Directory")
    w()
    w(f"Complete listing of all **{total}** indexed documents with extracted metadata.")
    w()

    # Sort documents alphabetically by stem
    sorted_docs = sorted(documents, key=lambda d: d["stem"].lower())

    for i, doc in enumerate(sorted_docs, 1):
        _render_document_card(w, doc, i)

    # ══════════════════════════════════════════════════════════════════════
    # FOOTER
    # ══════════════════════════════════════════════════════════════════════
    w("---")
    w()
    w(f"*Generated by `{SCRIPT_NAME}` v{SCRIPT_VERSION} on "
      f"{now.strftime('%Y-%m-%d at %H:%M')}*")
    w()

    return "\n".join(lines)


def _render_document_card(w, doc: Dict[str, Any], index: int):
    """Render a single document's metadata card in the directory."""
    stem = doc["stem"]
    title = doc.get("title", stem)

    w(f"### {index}. [[{stem}|{title}]]")
    w()

    # Info table
    w("| Property | Value |")
    w("|----------|-------|")
    w(f"| **File** | `{doc.get('relative_path', doc['filename'])}` |")
    w(f"| **Size** | {doc.get('file_size_display', '—')} |")
    w(f"| **Created** | {doc.get('created_date', '—')} |")
    w(f"| **Modified** | {doc.get('modified_date', '—')} |")
    w(f"| **Days Since Modified** | {doc.get('days_since_modified', '—')} |")
    w(f"| **Words** | {doc.get('word_count', 0):,} |")
    w(f"| **Est. Read Time** | ~{doc.get('read_time_min', 0)} min |")
    w(f"| **Outgoing Links** | {doc.get('outgoing_link_count', 0)} |")
    w(f"| **Content Density** | {doc.get('content_density', 0)} |")
    w(f"| **Has Frontmatter** | {'✅' if doc.get('has_frontmatter') else '❌'} |")

    # Status / type / certainty
    if doc.get("fm_status"):
        w(f"| **Status** | `{doc['fm_status']}` |")
    if doc.get("fm_note_type"):
        w(f"| **Note Type** | `{doc['fm_note_type']}` |")
    if doc.get("fm_certainty"):
        w(f"| **Certainty** | `{doc['fm_certainty']}` |")
    if doc.get("fm_knowledge_level"):
        w(f"| **Knowledge Level** | `{doc['fm_knowledge_level']}` |")
    w()

    # Tags
    all_tags = doc.get("all_tags", [])
    if all_tags:
        tag_str = " ".join(f"`#{t}`" for t in all_tags)
        w(f"**Tags:** {tag_str}")
        w()

    # Aliases
    aliases = doc.get("fm_aliases", [])
    if aliases:
        alias_str = ", ".join(f"*{a}*" for a in aliases)
        w(f"**Aliases:** {alias_str}")
        w()

    # Outgoing links
    links = doc.get("outgoing_links", [])
    if links:
        link_str = " · ".join(f"[[{lnk}]]" for lnk in links[:20])
        w(f"**Links to:** {link_str}")
        if len(links) > 20:
            w(f"*... and {len(links) - 20} more*")
        w()

    # Content analysis highlights
    analysis = doc.get("content_analysis", {})
    if analysis:
        features = []
        if analysis.get("heading_count", 0) > 0:
            features.append(f"{analysis['heading_count']} headings")
        if analysis.get("callout_count", 0) > 0:
            features.append(f"{analysis['callout_count']} callouts")
        if analysis.get("code_block_count", 0) > 0:
            langs = analysis.get("code_languages", [])
            lang_info = f" ({', '.join(langs)})" if langs else ""
            features.append(f"{analysis['code_block_count']} code blocks{lang_info}")
        if analysis.get("has_dataview"):
            features.append("📊 Dataview")
        if analysis.get("has_templater"):
            features.append("⚙️ Templater")
        if analysis.get("inline_field_count", 0) > 0:
            features.append(f"{analysis['inline_field_count']} inline fields")
        if analysis.get("external_link_count", 0) > 0:
            features.append(f"{analysis['external_link_count']} external links")
        if analysis.get("embed_count", 0) > 0:
            features.append(f"{analysis['embed_count']} embeds")

        if features:
            w(f"**Content Features:** {' · '.join(features)}")
            w()

    # Custom frontmatter fields (show any non-standard fields)
    fm = doc.get("frontmatter", {})
    standard_keys = {
        "title", "tags", "aliases", "status", "certainty", "note_type",
        "doc_type", "type", "knowledge_level", "doc_created", "doc_modified",
        "created", "modified", "date", "prompt_title",
    }
    custom_fields = {k: v for k, v in fm.items() if k not in standard_keys and v}
    if custom_fields:
        w("**Additional Metadata:**")
        w()
        for key, value in sorted(custom_fields.items()):
            display_val = value
            if isinstance(value, list):
                display_val = ", ".join(str(v) for v in value)
            elif isinstance(value, str) and len(value) > 100:
                display_val = value[:100] + "…"
            w(f"- `{key}`: {display_val}")
        w()

    w("---")
    w()


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def _format_size(size_bytes: int) -> str:
    """Format bytes into human-readable string."""
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB"]
    i = 0
    size = float(size_bytes)
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f"{size:.1f} {units[i]}"


def _pct(part: int, whole: int) -> str:
    """Format a percentage string."""
    if whole == 0:
        return "0%"
    return f"{(part / whole) * 100:.1f}%"


def _normalize_list(value) -> List[str]:
    """Normalize a frontmatter value that should be a list."""
    if isinstance(value, list):
        return [str(v).strip() for v in value if v]
    if isinstance(value, str) and value.strip():
        # Could be space-separated tags like "#tag1 #tag2"
        return [v.strip().lstrip("#") for v in value.split() if v.strip()]
    return []


# ══════════════════════════════════════════════════════════════════════════════
# CLI ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        prog="vault_indexer",
        description=(
            "Index an Obsidian vault folder and produce a comprehensive "
            "Markdown index with wikilinks and per-document metadata."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  python vault_indexer.py --input "./04-library/philosophy"
  python vault_indexer.py --input "./03-notes" --output "./07-mocs/notes-index.md"
  python vault_indexer.py --input "." --depth 1 --name "root-index"
  python vault_indexer.py --input "./04-library" --stale 60 --exclude "_templates,_archive"
        """,
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Folder to index (path to directory)",
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="Output file path (default: <input>/_index.md)",
    )
    parser.add_argument(
        "--name", "-n", default="_index",
        help="Name for the index file without extension (default: _index)",
    )
    parser.add_argument(
        "--depth", "-d", type=int, default=None,
        help="Max folder recursion depth (default: unlimited)",
    )
    parser.add_argument(
        "--exclude", "-e", default="",
        help="Comma-separated folder names to exclude (added to defaults)",
    )
    parser.add_argument(
        "--stale", "-s", type=int, default=30,
        help="Days since modification to flag as stale (default: 30)",
    )
    parser.add_argument(
        "--no-content", action="store_true",
        help="Skip content analysis (faster, filesystem + frontmatter only)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print summary to console without writing file",
    )

    args = parser.parse_args()

    # ── Resolve paths ──────────────────────────────────────────────────────
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.is_dir():
        print(f"❌ Error: '{input_path}' is not a directory.")
        sys.exit(1)

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
    else:
        # Sanitize name
        safe_name = re.sub(r"[^\w\-]", "_", args.name)
        output_path = input_path / f"{safe_name}.md"

    # ── Build exclusion set ────────────────────────────────────────────────
    excludes = set(DEFAULT_EXCLUDES)
    if args.exclude:
        for ex in args.exclude.split(","):
            ex = ex.strip()
            if ex:
                excludes.add(ex)

    # ── Banner ─────────────────────────────────────────────────────────────
    print(f"\n{'═' * 70}")
    print(f"  📂 VAULT INDEXER v{SCRIPT_VERSION}")
    print(f"{'═' * 70}")
    print(f"  Input:    {input_path}")
    print(f"  Output:   {output_path}")
    print(f"  Depth:    {'Unlimited' if args.depth is None else args.depth}")
    print(f"  Stale:    >{args.stale} days")
    print(f"  Content:  {'Skipped' if args.no_content else 'Full analysis'}")
    print(f"  Mode:     {'DRY RUN' if args.dry_run else 'WRITE'}")
    print(f"{'═' * 70}\n")

    # ── Scan ───────────────────────────────────────────────────────────────
    print("🔍 Scanning documents...")
    documents, folder_tree = scan_folder(
        input_path,
        excludes=excludes,
        max_depth=args.depth,
        skip_content=args.no_content,
    )
    print(f"   Found {len(documents)} markdown documents.")

    if not documents:
        print("⚠️  No markdown files found. Nothing to index.")
        sys.exit(0)

    # ── Aggregate ──────────────────────────────────────────────────────────
    print("📊 Computing aggregate statistics...")
    aggregates = compute_aggregates(documents, stale_days=args.stale)

    # ── Render ─────────────────────────────────────────────────────────────
    print("📝 Rendering index document...")
    markdown = render_index(
        documents, folder_tree, aggregates, input_path, stale_days=args.stale,
    )

    # ── Output ─────────────────────────────────────────────────────────────
    if args.dry_run:
        print(f"\n{'─' * 70}")
        print("DRY RUN — Summary:")
        print(f"  Documents:        {aggregates['total_documents']}")
        print(f"  Total words:      {aggregates.get('total_words', 0):,}")
        print(f"  Total size:       {aggregates.get('total_size_display', '0 B')}")
        print(f"  With frontmatter: {aggregates.get('has_frontmatter', 0)}")
        print(f"  Missing FM:       {aggregates.get('missing_frontmatter', 0)}")
        print(f"  Stale (>{args.stale}d):  {aggregates.get('stale_document_count', 0)}")
        print(f"  Unique tags:      {len(aggregates.get('tag_frequency', []))}")
        print(f"  Output would be:  ~{len(markdown):,} characters")
        print(f"{'─' * 70}\n")
        print("Pass --no-dry-run or remove --dry-run to write the file.")
    else:
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        print(f"\n✅ Index written to: {output_path}")
        print(f"   Size: {_format_size(len(markdown.encode('utf-8')))}")
        print(f"   Documents indexed: {len(documents)}")
    
    print()


if __name__ == "__main__":
    main()
