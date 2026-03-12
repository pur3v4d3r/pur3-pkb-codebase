#!/usr/bin/env python3
"""
================================================================================
SCRIPT NAME: pkb_extractor.py
VERSION:     1.0.0
CREATED:     2026-03-12
AUTHOR:      PKB Script Builder Agent (Claude)
================================================================================

PURPOSE:
    Comprehensive Markdown extraction pipeline for populating a Personal
    Knowledge Base (PKB). Reads Obsidian-flavored Markdown files (especially
    Claude-generated reports) and extracts every extractable element —
    callouts, wiki-links, inline fields, headings, tags, code blocks,
    tables, external links, definitions, embeds, mermaid diagrams,
    footnotes, bold/italic emphasis, semantic color spans, lists, and
    YAML frontmatter — then writes BOTH a machine-readable JSON file
    and a human-readable Markdown report for each source file.

WHAT IT EXTRACTS:
    - YAML Frontmatter (full structured metadata)
    - Callouts ([!TYPE] blocks with type, title, body)
    - Wiki-Links ([[Target]], [[Target|Alias]], [[Target#Heading]])
    - Inline Fields ([**FieldName**:: Value] and FieldName:: Value)
    - Tags (#tag-name, including hierarchical #parent/child)
    - Headings (all levels, with document outline tree)
    - Code Blocks (fenced ``` blocks with language identifier)
    - Tables (headers, alignment, all data rows)
    - External Links ([Display](URL) and bare URLs)
    - Embeds (![[Target]])
    - Block References (^block-id)
    - Definitions ([**Term**:: definition] semantic extraction)
    - Mermaid Diagrams (```mermaid blocks)
    - Footnotes ([^ref]: text and [^ref] references)
    - Bold & Italic emphasis spans
    - Semantic Color Spans (<span style='color: #HEX;'>text</span>)
    - Ordered and Unordered Lists

INPUTS:
    - A single Markdown file  (--input path/to/file.md)
    - OR a directory of files (--input path/to/folder/)

OUTPUTS:
    - {source_name}_extracted.json    -> Machine-readable structured data
    - {source_name}_report.md         -> Human-readable Obsidian report

USAGE:
    python pkb_extractor.py --input "path/to/file.md"
    python pkb_extractor.py --input "path/to/folder/" --output "path/to/output/"
    python pkb_extractor.py --input "path/to/folder/" --recursive
    python pkb_extractor.py --help

REQUIREMENTS:
    Python 3.8+
    No external libraries required (uses only Python standard library)
    Optional: pip install pyyaml  (for enhanced YAML parsing)

NOTES:
    - Designed for Obsidian-flavored Markdown with Claude-generated reports
    - Handles nested callouts, multi-line callout bodies, and complex YAML
    - Processes files with UTF-8 encoding
    - All regex patterns are heavily commented for readability
================================================================================
"""

# ══════════════════════════════════════════════════════════════════════════════
# IMPORTS
# ══════════════════════════════════════════════════════════════════════════════

# ── Standard Library ──────────────────────────────────────────────────────────
import re           # Regular expression matching for pattern extraction
import json         # JSON encoding for machine-readable output
import os           # File path operations
import sys          # System-level operations
import argparse     # User-friendly command-line interface
from pathlib import Path        # Modern, cross-platform file path handling
from datetime import datetime   # Timestamps for extraction metadata
from typing import Dict, List, Any, Optional, Tuple  # Type hints for clarity
from collections import defaultdict, Counter  # Convenient data grouping
import time         # Processing time measurement

# ── Optional: Enhanced YAML (install with: pip install pyyaml) ────────────────
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    # Script will use built-in regex-based YAML parsing if PyYAML not installed


# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════

SCRIPT_NAME = "pkb_extractor.py"
SCRIPT_VERSION = "1.1.0"

# ── All recognized Obsidian callout types ─────────────────────────────────────
# This includes standard Obsidian types plus custom PKB types found in reports.
KNOWN_CALLOUT_TYPES = {
    # Standard Obsidian callout types
    "note", "abstract", "summary", "tldr", "info", "todo", "tip", "hint",
    "important", "success", "check", "done", "question", "help", "faq",
    "warning", "caution", "attention", "failure", "fail", "missing",
    "danger", "error", "bug", "example", "quote", "cite",
    # Custom PKB callout types (found in user's reports)
    "definition", "key-claim", "insight", "counter-argument", "reflection",
    "ask-yourself-this", "observation", "assumption", "principle-point",
    "methodology-and-sources", "critical", "what-this-does", "helpful-tip",
    "analogy", "thought-experiment", "evidence",
    # Additional types found in older reports
    "overview", "core-principle", "claude-thinking", "purpose",
}

# ── Semantic Color Mapping ────────────────────────────────────────────────────
# Maps hex colors to their semantic roles in the PKB color system.
SEMANTIC_COLORS = {
    "#FFC700": "Primary (Imperial Gold) — Key concepts, definitions",
    "#E50000": "Secondary (Vivid Crimson) — Structural elements, meta-notes",
    "#9E6CD3": "Technical (Deep Amethyst) — Technical terms, syntax",
    "#FF00DC": "Critical (Neon Magenta) — Warnings, conflicts, errors",
    "#27FF00": "Definition (Terminal Green) — Verified truths, principles",
    "#FF5700": "Reference (Reactor Orange) — Citations, external sources",
}


# ══════════════════════════════════════════════════════════════════════════════
# REGEX PATTERN LIBRARY
# ══════════════════════════════════════════════════════════════════════════════
# Each pattern is documented with what it matches and example input.

PATTERNS = {
    # ── YAML FRONTMATTER ──────────────────────────────────────────────────
    # Matches the --- delimited block at the very start of a file.
    # Example: ---\ntitle: "My Note"\ntags: [a, b]\n---
    "frontmatter": re.compile(
        r"^---\s*\n(.*?)\n---",
        re.DOTALL | re.MULTILINE
    ),

    # ── CALLOUT HEADER ────────────────────────────────────────────────────
    # Matches: > [!TYPE] Optional Title
    # Groups: (1) type, (2) optional title text
    "callout_header": re.compile(
        r"^>\s*\[!([^\]]+)\]\s*(.*)?$",
        re.MULTILINE
    ),

    # ── WIKI-LINKS ────────────────────────────────────────────────────────
    # Matches: [[Target]], [[Target|Display]], [[Target#Section]],
    #          [[Target#Section|Display]]
    # Groups: (1) target, (2) optional heading, (3) optional display text
    # Negative lookbehind (?<!\!) prevents matching embeds ![[...]]
    "wiki_link": re.compile(
        r'(?<!!)\[\['           # Opening [[ (not preceded by ! for embeds)
        r'([^\]|#]+)'           # Group 1: Target note name
        r'(?:#([^\]|]+))?'      # Group 2 (optional): Heading after #
        r'(?:\|([^\]]+))?'      # Group 3 (optional): Display text after |
        r'\]\]',                # Closing ]]
        re.MULTILINE
    ),

    # ── INLINE FIELDS (Bracket Format) ────────────────────────────────────
    # Matches: [**FieldName**:: Value] or [FieldName:: Value]
    # Groups: (1) field name (may contain **), (2) value
    "inline_field_bracket": re.compile(
        r'\[(\*{0,2}[^:\]]+?\*{0,2})::\s*([^\]]+)\]'
    ),

    # ── INLINE FIELDS (Bare Format) ───────────────────────────────────────
    # Matches: FieldName:: Value (at start of line or after list marker)
    # Groups: (1) field name, (2) value
    "inline_field_bare": re.compile(
        r'^([A-Za-z][A-Za-z0-9_\- ]+)::\s*(.+)$',
        re.MULTILINE
    ),

    # ── TAGS ──────────────────────────────────────────────────────────────
    # Matches: #tag-name or #category/subcategory but NOT inside code blocks
    # or URLs. Negative lookbehind prevents matching inside URLs or brackets.
    "tag": re.compile(
        r'(?<![/\[&])#([A-Za-z][A-Za-z0-9_/-]*)',
        re.MULTILINE
    ),

    # ── HEADINGS ──────────────────────────────────────────────────────────
    # Matches: # Heading through ###### Heading
    # Groups: (1) hash marks, (2) heading text
    "heading": re.compile(
        r'^(#{1,6})\s+(.+)$',
        re.MULTILINE
    ),

    # ── CODE BLOCKS (Fenced) ──────────────────────────────────────────────
    # Matches: ```language\ncode\n```
    # Groups: (1) language identifier, (2) code content
    "code_block": re.compile(
        r'```(\w*)\n(.*?)```',
        re.DOTALL
    ),

    # ── TABLES ────────────────────────────────────────────────────────────
    # Table rows: | cell | cell | cell |
    "table_row": re.compile(
        r'^\|(.+)\|$',
        re.MULTILINE
    ),
    # Table separator: |---|---|---|
    "table_separator": re.compile(
        r'^\|[-:| ]+\|$',
        re.MULTILINE
    ),

    # ── EXTERNAL LINKS ────────────────────────────────────────────────────
    # Matches: [Display Text](https://url.com)
    # Groups: (1) display text, (2) URL
    "external_link": re.compile(
        r'\[([^\]]+)\]\((https?://[^\)]+)\)'
    ),
    # Bare URLs: https://example.com
    "bare_url": re.compile(
        r'(?<!\()(https?://[^\s\)>\]]+)'
    ),

    # ── EMBEDS ────────────────────────────────────────────────────────────
    # Matches: ![[Target]] or ![[Target#Heading]] or ![[image.png]]
    # Groups: (1) full embed target
    "embed": re.compile(
        r'!\[\[([^\]]+)\]\]'
    ),

    # ── BLOCK REFERENCES ──────────────────────────────────────────────────
    # Matches: ^block-id at end of a line (preceded by any non-alphanumeric char)
    # Examples: " ^block-id", "]^verified", ".^established"
    # Groups: (1) block ID
    "block_ref_def": re.compile(
        r'(?<=[^a-zA-Z0-9])\^([a-zA-Z0-9-]+)\s*$',
        re.MULTILINE
    ),
    # Block reference usage: [[note^block-id]] or [[#^block-id]]
    "block_ref_use": re.compile(
        r'\[\[([^\]]*)\^([a-zA-Z0-9-]+)\]\]'
    ),

    # ── FOOTNOTES ─────────────────────────────────────────────────────────
    # Definition: [^ref]: text
    "footnote_def": re.compile(
        r'^\[\^([^\]]+)\]:\s*(.+)$',
        re.MULTILINE
    ),
    # Reference: [^ref]
    "footnote_ref": re.compile(
        r'\[\^([^\]]+)\](?!:)'
    ),

    # ── BOLD TEXT ──────────────────────────────────────────────────────────
    # Matches: **bold text**
    "bold": re.compile(
        r'\*\*(.+?)\*\*'
    ),

    # ── ITALIC TEXT ───────────────────────────────────────────────────────
    # Matches: *italic* or _italic_ (single delimiter)
    "italic": re.compile(
        r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)|(?<!_)_(?!_)(.+?)(?<!_)_(?!_)'
    ),

    # ── SEMANTIC COLOR SPANS ──────────────────────────────────────────────
    # Matches: <span style='color: #HEX;'>text</span>
    # Groups: (1) hex color, (2) text content
    "color_span": re.compile(
        r"<span\s+style=['\"]color:\s*(#[A-Fa-f0-9]{6});?['\"]>(.*?)</span>",
        re.DOTALL
    ),

    # ── MERMAID DIAGRAMS ──────────────────────────────────────────────────
    # Matches: ```mermaid\n...\n```
    "mermaid": re.compile(
        r'```mermaid\n(.*?)```',
        re.DOTALL
    ),

    # ── HORIZONTAL RULES ──────────────────────────────────────────────────
    "horizontal_rule": re.compile(
        r'^(-{3,}|={3,}|\*{3,})$',
        re.MULTILINE
    ),

    # ── ORDERED LIST ITEMS ────────────────────────────────────────────────
    # Matches: 1. Item text or  1. Nested item
    "ordered_list": re.compile(
        r'^(\s*)\d+\.\s+(.+)$',
        re.MULTILINE
    ),

    # ── UNORDERED LIST ITEMS ──────────────────────────────────────────────
    # Matches: - Item text or  - Nested item or * Item or + Item
    "unordered_list": re.compile(
        r'^(\s*)[-*+]\s+(.+)$',
        re.MULTILINE
    ),

    # ── HTML COMMENTS ─────────────────────────────────────────────────────
    # Matches: <!-- comment --> (used in reports for generation metadata)
    "html_comment": re.compile(
        r'<!--(.*?)-->',
        re.DOTALL
    ),

    # ── OBSIDIAN COMMENTS ─────────────────────────────────────────────────
    # Matches: %%comment%% (Obsidian's native invisible comment syntax)
    # Used in older reports for QA tags, synthesis markers, counterexamples.
    # Examples: %%QA:reasoning:scale-emergence%%
    #           %%counterexample: cot-always-improves-reasoning%%
    "obsidian_comment": re.compile(
        r'%%(.+?)%%',
        re.DOTALL
    ),

    # ── LATEX MATH ────────────────────────────────────────────────────────
    # Display math: $$...$$ (block-level equations)
    "math_display": re.compile(
        r'\$\$(.*?)\$\$',
        re.DOTALL
    ),
    # Inline math: $...$ (but NOT $$)
    "math_inline": re.compile(
        r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)'
    ),
}


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def read_markdown_file(file_path: str) -> Optional[str]:
    """
    Read a Markdown file and return its content as a string.
    Returns None if the file cannot be read, with a helpful error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"  ERROR: File not found: {file_path}")
        print(f"    -> Check that the path is correct and the file exists.")
        return None
    except PermissionError:
        print(f"  ERROR: Permission denied reading: {file_path}")
        print(f"    -> Check your file permissions.")
        return None
    except UnicodeDecodeError:
        # Try with latin-1 as fallback
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception:
            print(f"  ERROR: Encoding issue reading: {file_path}")
            print(f"    -> Try re-saving the file as UTF-8.")
            return None


def get_line_number(content: str, char_position: int) -> int:
    """
    Convert a character position to a 1-based line number.

    Args:
        content: The full text content.
        char_position: The 0-based character offset.

    Returns:
        The 1-based line number where that character appears.
    """
    return content[:char_position].count('\n') + 1


def get_context_line(content: str, line_number: int) -> str:
    """
    Get the full text of a specific line (1-based).

    Args:
        content: The full text content.
        line_number: The 1-based line number to retrieve.

    Returns:
        The text of that line, stripped of leading/trailing whitespace.
    """
    lines = content.split('\n')
    if 1 <= line_number <= len(lines):
        return lines[line_number - 1].strip()
    return ""


def generate_anchor(heading_text: str) -> str:
    """
    Generate a URL-safe anchor from heading text (Obsidian-style).
    Lowercases, replaces spaces with hyphens, strips special chars.

    Args:
        heading_text: The raw heading text.

    Returns:
        A slugified anchor string (e.g., "my-heading-text").
    """
    # Remove bold/italic markers, wiki-link brackets, HTML tags
    anchor = re.sub(r'\*+|_+', '', heading_text)
    anchor = re.sub(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', r'\1', anchor)
    anchor = re.sub(r'<[^>]+>', '', anchor)
    # Lowercase, replace non-alphanum with hyphens, collapse multi-hyphens
    anchor = anchor.lower().strip()
    anchor = re.sub(r'[^a-z0-9\s-]', '', anchor)
    anchor = re.sub(r'[\s]+', '-', anchor)
    anchor = re.sub(r'-+', '-', anchor)
    return anchor.strip('-')


def strip_frontmatter(content: str) -> str:
    """
    Remove YAML frontmatter from content so body-only extraction
    doesn't double-count items that appear in frontmatter.

    Args:
        content: Full file content.

    Returns:
        Content with frontmatter stripped, or original if no frontmatter.
    """
    match = PATTERNS["frontmatter"].match(content)
    if match:
        # Return everything after the closing ---
        end_pos = match.end()
        return content[end_pos:]
    return content


def get_section_for_line(headings: List[Dict], line_number: int) -> str:
    """
    Determine which section a given line belongs to, based on headings.

    Args:
        headings: List of heading dicts with 'line_number' and 'text' keys.
        line_number: The line to locate.

    Returns:
        The heading text of the enclosing section, or "Document Start".
    """
    current_section = "Document Start"
    for h in headings:
        if h["line_number"] <= line_number:
            current_section = h["text"]
        else:
            break
    return current_section


# ══════════════════════════════════════════════════════════════════════════════
# EXTRACTOR FUNCTIONS
# Each function extracts one type of element from the Markdown content.
# All return structured data (lists of dicts or dicts).
# ══════════════════════════════════════════════════════════════════════════════

def extract_frontmatter(content: str) -> Dict[str, Any]:
    """
    Extract the YAML frontmatter block from the top of a Markdown file.
    Returns the parsed frontmatter as a Python dictionary.
    Falls back to regex parsing if PyYAML is not installed.

    Args:
        content: The full text content of the Markdown file.

    Returns:
        Dictionary with 'frontmatter' (parsed dict) and
        '_frontmatter_raw' (raw YAML string).
    """
    match = PATTERNS["frontmatter"].match(content)
    if not match:
        return {"frontmatter": {}, "_frontmatter_raw": ""}

    raw_yaml = match.group(1)

    # Try PyYAML first (more reliable for complex YAML)
    if YAML_AVAILABLE:
        try:
            parsed = yaml.safe_load(raw_yaml)
            if parsed is None:
                parsed = {}
            return {"frontmatter": parsed, "_frontmatter_raw": raw_yaml}
        except yaml.YAMLError as e:
            print(f"    Warning: YAML parse error (falling back to regex): {e}")

    # Fallback: basic regex-based key-value extraction for simple YAML
    parsed = {}
    current_key = None
    current_list = None

    for line in raw_yaml.split('\n'):
        stripped = line.strip()

        # Skip empty lines and comments that are decorative (═══)
        if not stripped or stripped.startswith('#'):
            continue

        # Check for key: value pair
        kv_match = re.match(r'^([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*)$', line)
        if kv_match and not line.startswith(' ') and not line.startswith('\t'):
            key = kv_match.group(1)
            value = kv_match.group(2).strip()
            current_key = key

            if value.startswith('[') and value.endswith(']'):
                # Inline list: [a, b, c]
                items = [v.strip().strip('"').strip("'")
                         for v in value[1:-1].split(',') if v.strip()]
                parsed[key] = items
                current_list = None
            elif value == '' or value == '[]':
                # Start of a block list or empty value
                parsed[key] = []
                current_list = key
            else:
                # Simple value — strip quotes
                parsed[key] = value.strip('"').strip("'")
                current_list = None
        elif stripped.startswith('- ') and current_list:
            # List item under current key
            item = stripped[2:].strip().strip('"').strip("'")
            if isinstance(parsed.get(current_list), list):
                parsed[current_list].append(item)

    return {"frontmatter": parsed, "_frontmatter_raw": raw_yaml}


def extract_callouts(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all Obsidian-style callout blocks from Markdown content.

    Callouts use the format:
        > [!TYPE] Optional Title
        > Callout body text continues here
        > More body text on additional lines

    Handles multi-line callout bodies, nested callouts, and all known
    callout types (standard Obsidian + custom PKB types).

    Args:
        content: The full text content of the Markdown file.
        source_file: The filename (for metadata tagging in output).

    Returns:
        List of dicts, each representing one callout with:
        - type, title, body, line_number, source, char_start, char_end
    """
    # Work on body content only (exclude frontmatter)
    body = strip_frontmatter(content)
    # Calculate the offset so line numbers are correct relative to full file
    body_offset = len(content) - len(body)

    callouts = []
    lines = body.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]
        # Check if this line starts a callout: > [!TYPE] ...
        header_match = re.match(r'^>\s*\[!([^\]]+)\]\s*(.*)?$', line)

        if header_match:
            callout_type = header_match.group(1).strip().lower()
            title = (header_match.group(2) or "").strip()
            # Remove any bold markers from title
            title = re.sub(r'^\*\*|\*\*$', '', title).strip()

            # Calculate line number in the original file
            # Count newlines in content up to this point
            char_start = body_offset + sum(len(l) + 1 for l in lines[:i])
            line_num = get_line_number(content, char_start)

            # Collect all subsequent lines that are part of this callout
            # (lines starting with > that are not a new callout header)
            body_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i]
                # Check if it's a continuation of the callout (starts with >)
                if re.match(r'^>\s', next_line) or next_line.strip() == '>':
                    # Check if it's a NEW callout header (nested callout)
                    if re.match(r'^>\s*\[!', next_line):
                        break  # Let the outer loop handle it
                    # Strip the leading > and optional space
                    body_text = re.sub(r'^>\s?', '', next_line)
                    body_lines.append(body_text)
                    i += 1
                else:
                    break

            callout_body = '\n'.join(body_lines).strip()
            char_end = body_offset + sum(len(l) + 1 for l in lines[:i])

            callouts.append({
                "type": callout_type,
                "title": title if title else "Untitled",
                "body": callout_body,
                "line_number": line_num,
                "source": source_file,
                "char_start": char_start,
                "char_end": char_end,
            })
        else:
            i += 1

    return callouts


def extract_wiki_links(content: str, source_file: str,
                       headings: List[Dict] = None) -> List[Dict[str, Any]]:
    """
    Extract all [[wiki-link]] references from body content.

    Handles:
    - Simple: [[Target]]
    - With alias: [[Target|Display Text]]
    - With heading: [[Target#Section]]
    - Combined: [[Target#Section|Display]]

    Args:
        content: The full text content of the Markdown file.
        source_file: The filename for metadata.
        headings: Pre-extracted headings for section attribution.

    Returns:
        List of dicts, each with: target, heading, display_text,
        full_match, line_number, section, context_line, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    wiki_links = []
    for match in PATTERNS["wiki_link"].finditer(body):
        target = match.group(1).strip()
        heading = match.group(2)
        display_text = match.group(3)

        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)
        ctx_line = get_context_line(content, line_num)

        # Determine which section this link is in
        section = "Unknown"
        if headings:
            section = get_section_for_line(headings, line_num)

        wiki_links.append({
            "target": target,
            "heading": heading.strip() if heading else None,
            "display_text": display_text.strip() if display_text else None,
            "full_match": match.group(0),
            "line_number": line_num,
            "section": section,
            "context_line": ctx_line,
            "source": source_file,
        })

    return wiki_links


def extract_inline_fields(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract Dataview-style inline fields in both formats:
    - Bracket: [**FieldName**:: Value] or [FieldName:: Value]
    - Bare:    FieldName:: Value (at start of line)

    Args:
        content: The full text content of the Markdown file.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: field_name, value, format, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)
    fields = []

    # ── Bracket format: [FieldName:: Value] ───────────────────────────────
    for match in PATTERNS["inline_field_bracket"].finditer(body):
        # Clean up field name (remove ** bold markers if present)
        field_name = match.group(1).strip().replace('**', '').strip()
        value = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        fields.append({
            "field_name": field_name,
            "value": value,
            "format": "bracket",
            "line_number": line_num,
            "source": source_file,
        })

    # ── Bare format: FieldName:: Value ────────────────────────────────────
    for match in PATTERNS["inline_field_bare"].finditer(body):
        field_name = match.group(1).strip()
        value = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        # Avoid duplicates if already captured by bracket pattern
        # Also skip lines that are clearly YAML-like inside code blocks
        if not any(f["line_number"] == line_num and
                   f["field_name"] == field_name for f in fields):
            fields.append({
                "field_name": field_name,
                "value": value,
                "format": "bare",
                "line_number": line_num,
                "source": source_file,
            })

    return fields


def extract_tags(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all #tags from content body (excluding frontmatter and code blocks).
    Handles hierarchical tags: #category/subcategory/leaf

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: tag, full_tag, hierarchy, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    # Remove code blocks so we don't extract tags from code
    body_no_code = PATTERNS["code_block"].sub('', body)

    tags = []
    seen_positions = set()  # Avoid duplicates at same position

    for match in PATTERNS["tag"].finditer(body_no_code):
        tag_text = match.group(1)
        char_pos = body_offset + match.start()

        if char_pos in seen_positions:
            continue
        seen_positions.add(char_pos)

        line_num = get_line_number(content, char_pos)

        # Break hierarchical tags into components
        hierarchy = tag_text.split('/')

        tags.append({
            "tag": tag_text,
            "full_tag": f"#{tag_text}",
            "hierarchy": hierarchy,
            "line_number": line_num,
            "source": source_file,
        })

    return tags


def extract_headings(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all Markdown headings with level, text, and document position.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: level, text, anchor, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    headings = []
    for match in PATTERNS["heading"].finditer(body):
        level = len(match.group(1))  # Number of # symbols = heading level
        text = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        headings.append({
            "level": level,
            "text": text,
            "anchor": generate_anchor(text),
            "line_number": line_num,
            "source": source_file,
        })

    return headings


def build_document_outline(headings: List[Dict]) -> List[Dict]:
    """
    Build a hierarchical document outline from flat heading list.

    Takes the flat list of headings and nests them according to level,
    producing a tree structure where each heading can have children.

    Args:
        headings: Flat list of heading dicts from extract_headings().

    Returns:
        Nested list of heading dicts with 'children' key added.
    """
    if not headings:
        return []

    # Create copies with children arrays
    nodes = [dict(h, children=[]) for h in headings]

    # Build tree using a stack-based approach
    root = []
    stack = []  # Stack of (level, node) tuples

    for node in nodes:
        level = node["level"]

        # Pop stack until we find a parent with lower level
        while stack and stack[-1][0] >= level:
            stack.pop()

        if stack:
            # Add as child of the top of stack
            stack[-1][1]["children"].append(node)
        else:
            # Top-level heading
            root.append(node)

        stack.append((level, node))

    return root


def extract_code_blocks(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all fenced code blocks (``` ``` ).
    Captures language identifier and full code content.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: language, code, line_start, line_end,
        char_count, line_count, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    blocks = []
    for match in PATTERNS["code_block"].finditer(body):
        language = match.group(1) or "plaintext"
        code = match.group(2)
        char_pos = body_offset + match.start()
        line_start = get_line_number(content, char_pos)
        line_end = line_start + code.count('\n') + 1  # +1 for closing ```

        # Skip mermaid blocks (handled separately)
        if language.lower() == "mermaid":
            continue

        blocks.append({
            "language": language,
            "code": code.strip(),
            "line_start": line_start,
            "line_end": line_end,
            "char_count": len(code.strip()),
            "line_count": code.strip().count('\n') + 1,
            "source": source_file,
        })

    return blocks


def extract_tables(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all Markdown tables. Parses headers, alignment, and all data rows.

    A Markdown table has:
    - Header row: | Col 1 | Col 2 |
    - Separator:  |-------|-------|
    - Data rows:  | val 1 | val 2 |

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: headers, alignment, rows, line_start,
        row_count, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    # Remove code blocks first so we don't parse tables inside code
    body_no_code = PATTERNS["code_block"].sub(
        lambda m: '\n' * m.group(0).count('\n'), body
    )

    tables = []
    lines = body_no_code.split('\n')
    i = 0

    while i < len(lines) - 1:
        line = lines[i]
        # Check if this line looks like a table header (has pipes)
        if re.match(r'^\|.+\|$', line.strip()):
            # Check if the NEXT line is a separator
            if i + 1 < len(lines) and re.match(r'^\|[-:| ]+\|$', lines[i + 1].strip()):
                # We found a table! Parse it.
                header_line = line.strip()
                sep_line = lines[i + 1].strip()

                # Parse headers
                headers = [cell.strip() for cell in header_line.strip('|').split('|')]

                # Parse alignment from separator
                alignment = []
                for cell in sep_line.strip('|').split('|'):
                    cell = cell.strip()
                    if cell.startswith(':') and cell.endswith(':'):
                        alignment.append("center")
                    elif cell.endswith(':'):
                        alignment.append("right")
                    else:
                        alignment.append("left")

                # Parse data rows
                rows = []
                j = i + 2
                while j < len(lines):
                    row_line = lines[j].strip()
                    if re.match(r'^\|.+\|$', row_line):
                        cells = [cell.strip() for cell in row_line.strip('|').split('|')]
                        rows.append(cells)
                        j += 1
                    else:
                        break

                char_pos = body_offset + sum(len(l) + 1 for l in lines[:i])
                line_start = get_line_number(content, char_pos)

                tables.append({
                    "headers": headers,
                    "alignment": alignment,
                    "rows": rows,
                    "line_start": line_start,
                    "row_count": len(rows),
                    "source": source_file,
                })

                i = j  # Skip past the table
                continue

        i += 1

    return tables


def extract_external_links(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all hyperlinks: [Display Text](URL) and bare URLs.
    Excludes wiki-links (handled separately).

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: display_text, url, format, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    links = []

    # ── Markdown-format links: [text](url) ────────────────────────────────
    for match in PATTERNS["external_link"].finditer(body):
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)
        links.append({
            "display_text": match.group(1).strip(),
            "url": match.group(2).strip(),
            "format": "markdown",
            "line_number": line_num,
            "source": source_file,
        })

    # ── Bare URLs ─────────────────────────────────────────────────────────
    # Only add bare URLs that weren't already captured in markdown format
    markdown_urls = {link["url"] for link in links}
    for match in PATTERNS["bare_url"].finditer(body):
        url = match.group(0).strip()
        if url not in markdown_urls:
            char_pos = body_offset + match.start()
            line_num = get_line_number(content, char_pos)
            links.append({
                "display_text": url,  # No display text for bare URLs
                "url": url,
                "format": "bare",
                "line_number": line_num,
                "source": source_file,
            })

    return links


def extract_embeds(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all Obsidian embeds: ![[Target]] for notes, images, PDFs.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: target, is_image, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    embeds = []
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp'}

    for match in PATTERNS["embed"].finditer(body):
        target = match.group(1).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        # Check if this is an image embed
        is_image = any(target.lower().endswith(ext) for ext in image_extensions)

        embeds.append({
            "target": target,
            "is_image": is_image,
            "line_number": line_num,
            "source": source_file,
        })

    return embeds


def extract_block_references(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all block IDs (^block-id) and references to them.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: block_id, type (definition/reference),
        line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    refs = []

    # Block ID definitions: ^block-id at end of line
    for match in PATTERNS["block_ref_def"].finditer(body):
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)
        refs.append({
            "block_id": match.group(1),
            "type": "definition",
            "line_number": line_num,
            "source": source_file,
        })

    # Block reference usage: [[note^block-id]]
    for match in PATTERNS["block_ref_use"].finditer(body):
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)
        refs.append({
            "block_id": match.group(2),
            "type": "reference",
            "note_target": match.group(1) if match.group(1) else None,
            "line_number": line_num,
            "source": source_file,
        })

    return refs


def extract_definitions(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract [**Term**:: Definition] patterns used as PKB definition fields.
    These are inline fields that are specifically definitional in nature
    (identified by bold ** markers around the field name).

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: term, definition, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    definitions = []

    # Look specifically for [**Term**:: Definition] pattern
    # This pattern identifies fields where the name is wrapped in bold
    pattern = re.compile(r'\[\*\*([^*]+)\*\*::\s*([^\]]+)\]')

    for match in pattern.finditer(body):
        term = match.group(1).strip()
        definition = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        definitions.append({
            "term": term,
            "definition": definition,
            "line_number": line_num,
            "source": source_file,
        })

    return definitions


def extract_mermaid(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract all ```mermaid code blocks as separate items.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: diagram_code, diagram_type, line_start, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    diagrams = []
    for match in PATTERNS["mermaid"].finditer(body):
        code = match.group(1).strip()
        char_pos = body_offset + match.start()
        line_start = get_line_number(content, char_pos)

        # Try to determine diagram type from first line
        first_line = code.split('\n')[0].strip().lower() if code else ""
        diagram_type = "unknown"
        for dt in ["graph", "flowchart", "sequencediagram", "classDiagram",
                    "statediagram", "gantt", "pie", "journey", "mindmap",
                    "timeline", "erdiagram", "gitgraph"]:
            if first_line.startswith(dt.lower()):
                diagram_type = dt
                break

        diagrams.append({
            "diagram_code": code,
            "diagram_type": diagram_type,
            "line_start": line_start,
            "line_count": code.count('\n') + 1,
            "source": source_file,
        })

    return diagrams


def extract_footnotes(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract footnote definitions [^1]: text and references [^1].

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: ref_id, content (for defs), type, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    footnotes = []

    # Definitions: [^ref]: text
    for match in PATTERNS["footnote_def"].finditer(body):
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)
        footnotes.append({
            "ref_id": match.group(1),
            "content": match.group(2).strip(),
            "type": "definition",
            "line_number": line_num,
            "source": source_file,
        })

    # References: [^ref] (usage in text)
    for match in PATTERNS["footnote_ref"].finditer(body):
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)
        footnotes.append({
            "ref_id": match.group(1),
            "content": None,
            "type": "reference",
            "line_number": line_num,
            "source": source_file,
        })

    return footnotes


def extract_color_spans(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract semantic color-coded spans: <span style='color: #HEX;'>text</span>

    The PKB uses a semantic color system where different colors indicate
    different types of information (definitions, warnings, key concepts, etc.)

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: color_hex, text, semantic_role, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    spans = []
    for match in PATTERNS["color_span"].finditer(body):
        color_hex = match.group(1).upper()
        text = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        # Look up semantic role from the color map
        semantic_role = SEMANTIC_COLORS.get(color_hex, f"Custom ({color_hex})")

        spans.append({
            "color_hex": color_hex,
            "text": text,
            "semantic_role": semantic_role,
            "line_number": line_num,
            "source": source_file,
        })

    return spans


def extract_lists(content: str, source_file: str) -> Dict[str, List[Dict]]:
    """
    Extract ordered and unordered list items with nesting level.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        Dict with 'ordered' and 'unordered' keys, each containing
        list of dicts with: text, indent_level, line_number, source
    """
    body = strip_frontmatter(content)
    body_offset = len(content) - len(body)

    # Remove code blocks to avoid extracting list-like syntax from code
    body_no_code = PATTERNS["code_block"].sub(
        lambda m: '\n' * m.group(0).count('\n'), body
    )

    result = {"ordered": [], "unordered": []}

    # ── Ordered lists: 1. Item ─────────────────────────────────────────────
    for match in PATTERNS["ordered_list"].finditer(body_no_code):
        indent = len(match.group(1))
        text = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        result["ordered"].append({
            "text": text,
            "indent_level": indent // 2,  # Every 2 spaces = 1 level
            "line_number": line_num,
            "source": source_file,
        })

    # ── Unordered lists: - Item ────────────────────────────────────────────
    for match in PATTERNS["unordered_list"].finditer(body_no_code):
        indent = len(match.group(1))
        text = match.group(2).strip()
        char_pos = body_offset + match.start()
        line_num = get_line_number(content, char_pos)

        # Skip lines that are callout body lines (start with >)
        ctx = get_context_line(content, line_num)
        if ctx.startswith('>'):
            continue

        result["unordered"].append({
            "text": text,
            "indent_level": indent // 2,
            "line_number": line_num,
            "source": source_file,
        })

    return result


def extract_html_comments(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract HTML comments <!-- ... --> which often contain generation
    metadata in Claude-generated reports.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: comment_text, line_number, source
    """
    comments = []
    for match in PATTERNS["html_comment"].finditer(content):
        text = match.group(1).strip()
        line_num = get_line_number(content, match.start())
        comments.append({
            "comment_text": text,
            "line_number": line_num,
            "source": source_file,
        })
    return comments


def extract_obsidian_comments(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract Obsidian-native comments using %%...%% syntax.

    These are invisible in Obsidian's preview mode and are commonly used
    in older PKB reports for QA tags, synthesis markers, and counterexample
    annotations.

    Examples found in reports:
        %%QA:reasoning:scale-emergence%%
        %%synthesis-potential: self-consistency×ensemble-methods%%
        %%counterexample: cot-always-improves-reasoning%%

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: comment_text, comment_category, line_number, source
    """
    comments = []
    for match in PATTERNS["obsidian_comment"].finditer(content):
        text = match.group(1).strip()
        line_num = get_line_number(content, match.start())

        # Attempt to categorize the comment by its prefix pattern
        category = "general"
        if text.startswith("QA:"):
            category = "qa-tag"
        elif text.startswith("synthesis-potential:"):
            category = "synthesis-marker"
        elif text.startswith("counterexample:"):
            category = "counterexample"

        comments.append({
            "comment_text": text,
            "comment_category": category,
            "line_number": line_num,
            "source": source_file,
        })
    return comments


def extract_math_expressions(content: str, source_file: str) -> List[Dict[str, Any]]:
    """
    Extract LaTeX math expressions in both inline ($...$) and
    display ($$...$$) formats.

    These appear in technical reports, especially those covering
    mathematical concepts, attention mechanisms, probability theory, etc.

    Args:
        content: The full text content.
        source_file: The filename for metadata.

    Returns:
        List of dicts with: expression, format (inline|display), line_number, source
    """
    body = strip_frontmatter(content)
    results = []

    # Track display math positions to avoid double-counting in inline pass
    display_ranges = []

    # 1. Display math: $$...$$ (block-level equations)
    for match in PATTERNS["math_display"].finditer(body):
        expr = match.group(1).strip()
        if not expr:
            continue
        # Offset to find line number in original content
        line_num = get_line_number(content, match.start())
        display_ranges.append((match.start(), match.end()))
        results.append({
            "expression": expr,
            "format": "display",
            "line_number": line_num,
            "source": source_file,
        })

    # 2. Inline math: $...$ (single-dollar, not $$)
    for match in PATTERNS["math_inline"].finditer(body):
        expr = match.group(1).strip()
        if not expr:
            continue
        pos = match.start()
        # Skip if this position falls inside a display math block
        if any(s <= pos <= e for s, e in display_ranges):
            continue
        line_num = get_line_number(content, match.start())
        results.append({
            "expression": expr,
            "format": "inline",
            "line_number": line_num,
            "source": source_file,
        })

    return results


# ══════════════════════════════════════════════════════════════════════════════
# ANALYSIS FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def compute_document_stats(content: str) -> Dict[str, int]:
    """
    Compute basic document statistics: word count, character count, line count.

    Args:
        content: The full text content.

    Returns:
        Dict with word_count, character_count, line_count.
    """
    body = strip_frontmatter(content)
    words = len(body.split())
    chars = len(body)
    lines = body.count('\n') + 1
    return {
        "word_count": words,
        "character_count": chars,
        "line_count": lines,
    }


def build_knowledge_graph_analysis(wiki_links: List[Dict],
                                   tags: List[Dict],
                                   frontmatter: Dict) -> Dict[str, Any]:
    """
    Build a knowledge graph analysis section from extracted wiki-links,
    tags, and frontmatter relationships.

    Args:
        wiki_links: Extracted wiki-links list.
        tags: Extracted tags list.
        frontmatter: Parsed frontmatter dict.

    Returns:
        Dict with unique targets, tags, domains, relationship categories.
    """
    # Unique wiki-link targets
    unique_targets = sorted(set(wl["target"] for wl in wiki_links))

    # Unique tags
    unique_tags = sorted(set(t["full_tag"] for t in tags))

    # Extract relationship categories from frontmatter
    relationship_keys = [
        "prerequisites", "related", "broader", "narrower", "see-also",
        "contrasts-with", "applied-in", "builds-on", "enables",
        "related_concepts", "link_related", "link_up", "link_down",
    ]
    frontmatter_relations = {}
    fm = frontmatter.get("frontmatter", {})
    for key in relationship_keys:
        if key in fm and fm[key]:
            val = fm[key]
            if isinstance(val, list):
                frontmatter_relations[key] = val
            elif isinstance(val, str):
                frontmatter_relations[key] = [val]

    # Compute backlink candidates: targets that appear in wiki-links
    # but are NOT the current document
    backlink_candidates = unique_targets

    return {
        "unique_wiki_link_targets": unique_targets,
        "unique_wiki_link_count": len(unique_targets),
        "unique_tags": unique_tags,
        "unique_tag_count": len(unique_tags),
        "frontmatter_relationships": frontmatter_relations,
        "backlink_candidates": backlink_candidates,
    }


# ══════════════════════════════════════════════════════════════════════════════
# OUTPUT FORMATTERS
# ══════════════════════════════════════════════════════════════════════════════

def build_json_output(extraction_results: Dict[str, Any],
                      metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Assemble the master JSON output from all extraction results.

    This follows the canonical JSON schema defined in the PKB Script Builder
    Agent specification. All extraction types are included even if empty.

    Args:
        extraction_results: Dict of all extracted items by type.
        metadata: File metadata (paths, timestamps, etc.).

    Returns:
        Complete JSON-serializable dict matching the master schema.
    """
    # Count items by type
    type_counts = {}
    total = 0
    for key, value in extraction_results.items():
        if key in ("document_outline", "knowledge_graph", "document_stats",
                    "frontmatter_data"):
            continue
        if isinstance(value, list):
            type_counts[key] = len(value)
            total += len(value)
        elif isinstance(value, dict):
            # For lists dict (ordered/unordered)
            for sub_key, sub_val in value.items():
                if isinstance(sub_val, list):
                    count = len(sub_val)
                    type_counts[f"{key}_{sub_key}"] = count
                    total += count

    return {
        "extraction_metadata": {
            "script_name": SCRIPT_NAME,
            "script_version": SCRIPT_VERSION,
            "extraction_timestamp": datetime.now().isoformat(),
            "source_file": metadata["source_file"],
            "source_file_path": metadata["source_file_path"],
            "source_file_size_bytes": metadata["source_file_size"],
            "processing_time_seconds": metadata.get("processing_time", 0),
        },
        "document_metadata": {
            "frontmatter": extraction_results.get("frontmatter_data", {}).get("frontmatter", {}),
            **extraction_results.get("document_stats", {}),
            "heading_count": type_counts.get("headings", 0),
        },
        "extraction_summary": {
            "total_items_extracted": total,
            "by_type": type_counts,
        },
        "document_outline": extraction_results.get("document_outline", []),
        "extracted_items": {
            "callouts": extraction_results.get("callouts", []),
            "wiki_links": extraction_results.get("wiki_links", []),
            "inline_fields": extraction_results.get("inline_fields", []),
            "tags": extraction_results.get("tags", []),
            "headings": extraction_results.get("headings", []),
            "code_blocks": extraction_results.get("code_blocks", []),
            "tables": extraction_results.get("tables", []),
            "external_links": extraction_results.get("external_links", []),
            "embeds": extraction_results.get("embeds", []),
            "block_references": extraction_results.get("block_references", []),
            "definitions": extraction_results.get("definitions", []),
            "mermaid_diagrams": extraction_results.get("mermaid_diagrams", []),
            "footnotes": extraction_results.get("footnotes", []),
            "color_spans": extraction_results.get("color_spans", []),
            "lists": extraction_results.get("lists", {}),
            "html_comments": extraction_results.get("html_comments", []),
            "obsidian_comments": extraction_results.get("obsidian_comments", []),
            "math_expressions": extraction_results.get("math_expressions", []),
        },
        "knowledge_graph": extraction_results.get("knowledge_graph", {}),
    }


def build_yaml_frontmatter_for_report(metadata: Dict, extraction_summary: Dict,
                                      source_frontmatter: Dict) -> str:
    """
    Generate PKB-conformant YAML frontmatter for the Markdown extraction report.

    Args:
        metadata: File metadata dict.
        extraction_summary: Summary counts by type.
        source_frontmatter: Original frontmatter from source file.

    Returns:
        String of YAML frontmatter block (including --- delimiters).
    """
    source_name = Path(metadata["source_file"]).stem
    fm = source_frontmatter.get("frontmatter", {})

    # Infer domain from source frontmatter
    primary_domain = fm.get("primary_domain",
                            fm.get("domain", "unknown"))
    secondary_domains = fm.get("secondary_domains",
                               fm.get("subdomains", []))

    # Build the YAML block
    lines = [
        "---",
        f'doc_id: "extraction-report-{source_name}"',
        f'doc_created: "{datetime.now().strftime("%Y-%m-%d")}"',
        f'doc_modified: "{datetime.now().strftime("%Y-%m-%d")}"',
        'doc_type: "extraction-report"',
        f'source_file: "{metadata["source_file"]}"',
        f'extraction_script: "{SCRIPT_NAME}"',
        f'extraction_date: "{datetime.now().isoformat()}"',
        "",
        f'primary_domain: "{primary_domain}"',
    ]

    if secondary_domains:
        lines.append("secondary_domains:")
        for sd in secondary_domains[:5]:
            lines.append(f'  - "{sd}"')

    lines.extend([
        "",
        "tags:",
        "  - extraction-report",
        "  - auto-generated",
        f'  - {primary_domain}',
        "",
        'status: "auto-generated"',
        'confidence: "high"',
        "",
        "extraction_summary:",
    ])

    for type_name, count in extraction_summary.items():
        lines.append(f"  {type_name}: {count}")

    lines.append("---")
    return '\n'.join(lines)


def build_markdown_report(extraction_results: Dict[str, Any],
                          metadata: Dict[str, Any]) -> str:
    """
    Build a complete human-readable Markdown extraction report.

    This report is designed to be directly imported into Obsidian
    and follows PKB formatting conventions (callouts, wiki-links, tables).

    Args:
        extraction_results: Dict of all extracted items by type.
        metadata: File metadata.

    Returns:
        Complete Markdown report as a string.
    """
    source_name = Path(metadata["source_file"]).stem
    source_file = metadata["source_file"]

    # ── Gather counts ─────────────────────────────────────────────────────
    counts = {}
    for key, value in extraction_results.items():
        if key in ("document_outline", "knowledge_graph", "document_stats",
                    "frontmatter_data"):
            continue
        if isinstance(value, list):
            counts[key] = len(value)
        elif isinstance(value, dict) and key == "lists":
            counts["ordered_lists"] = len(value.get("ordered", []))
            counts["unordered_lists"] = len(value.get("unordered", []))

    total_items = sum(counts.values())

    # ── Summary counts for frontmatter ────────────────────────────────────
    summary_counts = {
        "callouts_found": counts.get("callouts", 0),
        "wiki_links_found": counts.get("wiki_links", 0),
        "inline_fields_found": counts.get("inline_fields", 0),
        "definitions_found": counts.get("definitions", 0),
        "headings_found": counts.get("headings", 0),
        "tags_found": counts.get("tags", 0),
        "code_blocks_found": counts.get("code_blocks", 0),
        "tables_found": counts.get("tables", 0),
        "external_links_found": counts.get("external_links", 0),
        "embeds_found": counts.get("embeds", 0),
        "mermaid_diagrams_found": counts.get("mermaid_diagrams", 0),
        "color_spans_found": counts.get("color_spans", 0),
        "footnotes_found": counts.get("footnotes", 0),
        "total_items_extracted": total_items,
    }

    # ── Build YAML frontmatter ────────────────────────────────────────────
    fm_block = build_yaml_frontmatter_for_report(
        metadata, summary_counts,
        extraction_results.get("frontmatter_data", {})
    )

    # ── Start building the report ─────────────────────────────────────────
    sections = []
    sections.append(fm_block)
    sections.append("")

    # ── Title ─────────────────────────────────────────────────────────────
    # Try to get title from source frontmatter
    fm = extraction_results.get("frontmatter_data", {}).get("frontmatter", {})
    title = fm.get("title", source_name.replace('-', ' ').title())
    sections.append(f"# Extraction Report: {title}")
    sections.append("")
    sections.append(f"> [!info] Auto-Generated Report")
    sections.append(f"> This report was automatically generated by `{SCRIPT_NAME}` on {datetime.now().strftime('%Y-%m-%d %H:%M')}.")
    sections.append(f"> **Source**: `{source_file}` | **Items Extracted**: {total_items}")
    sections.append("")
    sections.append("---")
    sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Document Overview
    # ══════════════════════════════════════════════════════════════════════
    stats = extraction_results.get("document_stats", {})
    sections.append("## 📋 Document Overview")
    sections.append("")
    sections.append("| Field | Value |")
    sections.append("|-------|-------|")
    sections.append(f"| **Source File** | `{source_file}` |")
    sections.append(f"| **Extraction Date** | {datetime.now().strftime('%Y-%m-%d %H:%M')} |")
    sections.append(f"| **Word Count** | {stats.get('word_count', 'N/A'):,} |")
    sections.append(f"| **Character Count** | {stats.get('character_count', 'N/A'):,} |")
    sections.append(f"| **Line Count** | {stats.get('line_count', 'N/A'):,} |")
    sections.append(f"| **Total Items Extracted** | {total_items:,} |")
    sections.append("")

    # Document Outline
    headings = extraction_results.get("headings", [])
    if headings:
        sections.append("### Document Outline")
        sections.append("")
        for h in headings:
            indent = "  " * (h["level"] - 1)
            sections.append(f"{indent}- {'#' * h['level']} {h['text']}")
        sections.append("")

    sections.append("---")
    sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Extraction Summary
    # ══════════════════════════════════════════════════════════════════════
    sections.append("## 📊 Extraction Summary")
    sections.append("")
    sections.append("| Item Type | Count |")
    sections.append("|-----------|-------|")
    for type_name, count in sorted(summary_counts.items()):
        if type_name != "total_items_extracted":
            display_name = type_name.replace('_found', '').replace('_', ' ').title()
            sections.append(f"| {display_name} | {count} |")
    sections.append(f"| **TOTAL** | **{total_items}** |")
    sections.append("")
    sections.append("---")
    sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Callouts
    # ══════════════════════════════════════════════════════════════════════
    callouts = extraction_results.get("callouts", [])
    if callouts:
        sections.append(f"## 🔔 Callouts ({len(callouts)})")
        sections.append("")
        sections.append("> [!note] What are Callouts?")
        sections.append("> Callouts are `> [!TYPE]` blocks used in Obsidian for structured annotation.")
        sections.append("> They carry semantic meaning — definitions, insights, warnings, etc.")
        sections.append("")

        # Group by type
        by_type = defaultdict(list)
        for c in callouts:
            by_type[c["type"]].append(c)

        sections.append("### By Type")
        sections.append("")
        sections.append("| Callout Type | Count |")
        sections.append("|-------------|-------|")
        for ctype, items in sorted(by_type.items()):
            sections.append(f"| `[!{ctype}]` | {len(items)} |")
        sections.append("")

        sections.append("### Full Callout List")
        sections.append("")
        for i, c in enumerate(callouts, 1):
            sections.append(f"#### {i}. [{c['type'].upper()}] {c['title']} *(Line {c['line_number']})*")
            sections.append("")
            sections.append(f"> [!{c['type']}] {c['title']}")
            # Add body lines, each prefixed with >
            if c['body']:
                for body_line in c['body'].split('\n'):
                    sections.append(f"> {body_line}")
            sections.append("")

        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Wiki-Links
    # ══════════════════════════════════════════════════════════════════════
    wiki_links = extraction_results.get("wiki_links", [])
    if wiki_links:
        unique_targets = sorted(set(wl["target"] for wl in wiki_links))
        sections.append(f"## 🔗 Wiki-Links ({len(wiki_links)} total, {len(unique_targets)} unique targets)")
        sections.append("")
        sections.append("> [!info] Knowledge Graph Connections")
        sections.append("> These links represent connections to other notes in your PKB.")
        sections.append(f"> **{len(unique_targets)}** distinct notes are referenced.")
        sections.append("")

        sections.append("### Unique Targets")
        sections.append("")
        for target in unique_targets:
            sections.append(f"- [[{target}]]")
        sections.append("")

        sections.append("### All Occurrences")
        sections.append("")
        sections.append("| # | Target | Display Text | Heading | Section | Line |")
        sections.append("|---|--------|-------------|---------|---------|------|")
        for i, wl in enumerate(wiki_links, 1):
            display = wl["display_text"] or "—"
            heading = wl["heading"] or "—"
            section = wl.get("section", "—")
            # Truncate long section names
            if len(section) > 40:
                section = section[:37] + "..."
            sections.append(
                f"| {i} | [[{wl['target']}]] | {display} | {heading} | {section} | {wl['line_number']} |"
            )
        sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Definitions
    # ══════════════════════════════════════════════════════════════════════
    definitions = extraction_results.get("definitions", [])
    if definitions:
        sections.append(f"## 📖 Definitions ({len(definitions)})")
        sections.append("")
        sections.append("> [!tip] PKB Definitions")
        sections.append("> These `[**Term**:: Definition]` fields define key concepts.")
        sections.append("> They are queryable by Dataview.")
        sections.append("")
        for i, d in enumerate(definitions, 1):
            sections.append(f"### {i}. {d['term']}")
            sections.append("")
            sections.append(f"> [!definition] {d['term']}")
            sections.append(f"> {d['definition']}")
            sections.append("")
            sections.append(f"*Source: Line {d['line_number']} in `{d['source']}`*")
            sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Inline Fields
    # ══════════════════════════════════════════════════════════════════════
    inline_fields = extraction_results.get("inline_fields", [])
    if inline_fields:
        sections.append(f"## 🏷️ Inline Fields ({len(inline_fields)})")
        sections.append("")
        sections.append("> [!tip] Dataview Fields")
        sections.append("> These `[FieldName:: Value]` pairs are queryable by Dataview.")
        sections.append("")
        sections.append("| # | Field Name | Value | Format | Line |")
        sections.append("|---|-----------|-------|--------|------|")
        for i, f in enumerate(inline_fields, 1):
            # Truncate long values for table readability
            value = f["value"]
            if len(value) > 80:
                value = value[:77] + "..."
            sections.append(
                f"| {i} | **{f['field_name']}** | {value} | {f['format']} | {f['line_number']} |"
            )
        sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Tags
    # ══════════════════════════════════════════════════════════════════════
    tags = extraction_results.get("tags", [])
    if tags:
        unique_tags = sorted(set(t["full_tag"] for t in tags))
        sections.append(f"## 🏷️ Tags ({len(tags)} occurrences, {len(unique_tags)} unique)")
        sections.append("")

        sections.append("### All Unique Tags")
        sections.append("")
        sections.append(", ".join(f"`{t}`" for t in unique_tags))
        sections.append("")

        # Group hierarchical tags
        hierarchical = [t for t in tags if '/' in t["tag"]]
        if hierarchical:
            sections.append("### Hierarchical Tags")
            sections.append("")
            by_root = defaultdict(set)
            for t in hierarchical:
                root = t["hierarchy"][0]
                by_root[root].add(t["full_tag"])
            for root, subtags in sorted(by_root.items()):
                sections.append(f"- **{root}/**")
                for st in sorted(subtags):
                    sections.append(f"  - `{st}`")
            sections.append("")

        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Code Blocks
    # ══════════════════════════════════════════════════════════════════════
    code_blocks = extraction_results.get("code_blocks", [])
    if code_blocks:
        sections.append(f"## 💻 Code Blocks ({len(code_blocks)})")
        sections.append("")

        # Summary by language
        lang_counts = Counter(cb["language"] for cb in code_blocks)
        sections.append("| Language | Count |")
        sections.append("|----------|-------|")
        for lang, count in lang_counts.most_common():
            sections.append(f"| `{lang}` | {count} |")
        sections.append("")

        for i, cb in enumerate(code_blocks, 1):
            sections.append(f"### Code Block {i} — `{cb['language']}` *(Lines {cb['line_start']}-{cb['line_end']})*")
            sections.append("")
            # Truncate very long code blocks to 30 lines
            code_lines = cb["code"].split('\n')
            if len(code_lines) > 30:
                truncated = '\n'.join(code_lines[:30])
                sections.append(f"```{cb['language']}")
                sections.append(truncated)
                sections.append(f"# ... ({len(code_lines) - 30} more lines truncated)")
                sections.append("```")
            else:
                sections.append(f"```{cb['language']}")
                sections.append(cb["code"])
                sections.append("```")
            sections.append("")

        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Tables
    # ══════════════════════════════════════════════════════════════════════
    tables = extraction_results.get("tables", [])
    if tables:
        sections.append(f"## 📊 Tables ({len(tables)})")
        sections.append("")
        for i, t in enumerate(tables, 1):
            sections.append(f"### Table {i} *(Line {t['line_start']}, {t['row_count']} rows)*")
            sections.append("")
            # Reproduce the table
            sections.append("| " + " | ".join(t["headers"]) + " |")
            sections.append("| " + " | ".join("---" for _ in t["headers"]) + " |")
            for row in t["rows"]:
                sections.append("| " + " | ".join(row) + " |")
            sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: External Links
    # ══════════════════════════════════════════════════════════════════════
    ext_links = extraction_results.get("external_links", [])
    if ext_links:
        sections.append(f"## 🌐 External Links ({len(ext_links)})")
        sections.append("")
        sections.append("| # | Display Text | URL | Line |")
        sections.append("|---|-------------|-----|------|")
        for i, link in enumerate(ext_links, 1):
            display = link["display_text"]
            if len(display) > 50:
                display = display[:47] + "..."
            url = link["url"]
            if len(url) > 60:
                url = url[:57] + "..."
            sections.append(f"| {i} | {display} | {url} | {link['line_number']} |")
        sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Embeds
    # ══════════════════════════════════════════════════════════════════════
    embeds = extraction_results.get("embeds", [])
    if embeds:
        sections.append(f"## 📎 Embeds ({len(embeds)})")
        sections.append("")
        sections.append("| # | Target | Type | Line |")
        sections.append("|---|--------|------|------|")
        for i, e in enumerate(embeds, 1):
            etype = "Image" if e["is_image"] else "Note/File"
            sections.append(f"| {i} | `{e['target']}` | {etype} | {e['line_number']} |")
        sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Mermaid Diagrams
    # ══════════════════════════════════════════════════════════════════════
    mermaid = extraction_results.get("mermaid_diagrams", [])
    if mermaid:
        sections.append(f"## 📐 Mermaid Diagrams ({len(mermaid)})")
        sections.append("")
        for i, d in enumerate(mermaid, 1):
            sections.append(f"### Diagram {i} — {d['diagram_type']} *(Line {d['line_start']})*")
            sections.append("")
            sections.append("```mermaid")
            sections.append(d["diagram_code"])
            sections.append("```")
            sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Semantic Color Spans
    # ══════════════════════════════════════════════════════════════════════
    color_spans = extraction_results.get("color_spans", [])
    if color_spans:
        sections.append(f"## 🎨 Semantic Color Spans ({len(color_spans)})")
        sections.append("")
        sections.append("> [!info] PKB Color System")
        sections.append("> The PKB uses semantic color coding to distinguish concept types.")
        sections.append("")
        sections.append("| # | Color | Semantic Role | Text | Line |")
        sections.append("|---|-------|--------------|------|------|")
        for i, cs in enumerate(color_spans, 1):
            text = cs["text"]
            if len(text) > 50:
                text = text[:47] + "..."
            sections.append(
                f"| {i} | `{cs['color_hex']}` | {cs['semantic_role']} | {text} | {cs['line_number']} |"
            )
        sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Footnotes
    # ══════════════════════════════════════════════════════════════════════
    footnotes = extraction_results.get("footnotes", [])
    if footnotes:
        defs = [f for f in footnotes if f["type"] == "definition"]
        refs = [f for f in footnotes if f["type"] == "reference"]
        sections.append(f"## 📝 Footnotes ({len(defs)} definitions, {len(refs)} references)")
        sections.append("")
        if defs:
            sections.append("### Footnote Definitions")
            sections.append("")
            for d in defs:
                sections.append(f"- **[^{d['ref_id']}]**: {d['content']} *(Line {d['line_number']})*")
            sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Obsidian Comments
    # ══════════════════════════════════════════════════════════════════════
    obs_comments = extraction_results.get("obsidian_comments", [])
    if obs_comments:
        sections.append(f"## 💬 Obsidian Comments ({len(obs_comments)})")
        sections.append("")
        sections.append("> [!info] Obsidian Comments")
        sections.append("> `%%comment%%` blocks are invisible in Obsidian preview mode.")
        sections.append("> They are used for QA tags, synthesis markers, and counterexample annotations.")
        sections.append("")
        # Group by category
        by_cat = {}
        for c in obs_comments:
            cat = c.get("comment_category", "general")
            by_cat.setdefault(cat, []).append(c)
        for cat, items in sorted(by_cat.items()):
            display_cat = cat.replace("-", " ").title()
            sections.append(f"### {display_cat} ({len(items)})")
            sections.append("")
            for item in items:
                sections.append(f"- `%%{item['comment_text']}%%` *(Line {item['line_number']})*")
            sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Math Expressions
    # ══════════════════════════════════════════════════════════════════════
    math_exprs = extraction_results.get("math_expressions", [])
    if math_exprs:
        display_math = [m for m in math_exprs if m["format"] == "display"]
        inline_math = [m for m in math_exprs if m["format"] == "inline"]
        sections.append(f"## 🔢 Math Expressions ({len(math_exprs)})")
        sections.append("")
        sections.append(f"> [!info] LaTeX Math")
        sections.append(f"> Found {len(display_math)} display (`$$...$$`) and {len(inline_math)} inline (`$...$`) expressions.")
        sections.append("")
        if display_math:
            sections.append("### Display Math (Block Equations)")
            sections.append("")
            for i, m in enumerate(display_math, 1):
                sections.append(f"#### Equation {i} *(Line {m['line_number']})*")
                sections.append("")
                sections.append(f"$$")
                sections.append(m["expression"])
                sections.append(f"$$")
                sections.append("")
            sections.append("")
        if inline_math:
            sections.append("### Inline Math")
            sections.append("")
            sections.append("| # | Expression | Line |")
            sections.append("|---|-----------|------|")
            for i, m in enumerate(inline_math, 1):
                expr = m["expression"]
                if len(expr) > 60:
                    expr = expr[:57] + "..."
                # Escape pipe chars for table
                expr = expr.replace("|", "\\|")
                sections.append(f"| {i} | `${expr}$` | {m['line_number']} |")
            sections.append("")
        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Knowledge Graph Analysis
    # ══════════════════════════════════════════════════════════════════════
    kg = extraction_results.get("knowledge_graph", {})
    if kg:
        sections.append("## 🕸️ Knowledge Graph Analysis")
        sections.append("")

        targets = kg.get("unique_wiki_link_targets", [])
        if targets:
            sections.append(f"### Unique Wiki-Link Targets ({len(targets)})")
            sections.append("")
            sections.append("> These represent all distinct notes referenced in the source document.")
            sections.append("> Each is a candidate for backlink creation in your PKB.")
            sections.append("")
            for t in targets:
                sections.append(f"- [[{t}]]")
            sections.append("")

        fm_rels = kg.get("frontmatter_relationships", {})
        if fm_rels:
            sections.append("### Frontmatter Relationships")
            sections.append("")
            for rel_type, rel_items in fm_rels.items():
                display_type = rel_type.replace('-', ' ').replace('_', ' ').title()
                sections.append(f"#### {display_type}")
                sections.append("")
                for item in rel_items:
                    # Clean up wiki-link formatting from frontmatter
                    clean = re.sub(r'^\[\[|\]\]$', '', str(item).strip('"').strip("'"))
                    sections.append(f"- [[{clean}]]")
                sections.append("")

        sections.append("---")
        sections.append("")

    # ══════════════════════════════════════════════════════════════════════
    # SECTION: Raw Data Reference
    # ══════════════════════════════════════════════════════════════════════
    sections.append("## 📁 Raw Data")
    sections.append("")
    sections.append("> [!abstract] JSON File Available")
    sections.append(f"> The full machine-readable extraction is saved alongside this report as:")
    sections.append(f"> `{source_name}_extracted.json`")
    sections.append("")
    sections.append("---")
    sections.append("")
    sections.append(f"*Report generated by `{SCRIPT_NAME} v{SCRIPT_VERSION}` · {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    return '\n'.join(sections)


# ══════════════════════════════════════════════════════════════════════════════
# FILE WRITERS
# ══════════════════════════════════════════════════════════════════════════════

def write_json_output(data: Dict, output_path: str):
    """
    Write the JSON extraction data to a file.

    Args:
        data: The complete extraction dict to serialize.
        output_path: Full path for the output JSON file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)


def write_markdown_report(content: str, output_path: str):
    """
    Write the Markdown report to a file.

    Args:
        content: The complete Markdown report string.
        output_path: Full path for the output .md file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


# ══════════════════════════════════════════════════════════════════════════════
# ORCHESTRATION
# ══════════════════════════════════════════════════════════════════════════════

def process_single_file(input_path: str, output_dir: str) -> Dict[str, Any]:
    """
    Process a single Markdown file: extract all items, generate both
    JSON and Markdown outputs.

    This is the main orchestration function that calls all extractors
    in the correct order and assembles the outputs.

    Args:
        input_path: Full path to the source .md file.
        output_dir: Directory where outputs will be written.

    Returns:
        Dict with success status, total items count, and output paths.
    """
    start_time = time.time()

    # ── Read the file ─────────────────────────────────────────────────────
    content = read_markdown_file(input_path)
    if content is None:
        return {"success": False, "file": input_path, "error": "Could not read file"}

    source_file = Path(input_path).name
    source_stem = Path(input_path).stem

    # ── Prepare metadata ──────────────────────────────────────────────────
    file_stat = os.stat(input_path)
    metadata = {
        "source_file": source_file,
        "source_file_path": str(Path(input_path).resolve()),
        "source_file_size": file_stat.st_size,
    }

    # ══════════════════════════════════════════════════════════════════════
    # RUN ALL EXTRACTORS
    # ══════════════════════════════════════════════════════════════════════

    # 1. Frontmatter (first, as it informs other extractors)
    frontmatter_data = extract_frontmatter(content)

    # 2. Headings (second, as they provide section context for other items)
    headings = extract_headings(content, source_file)

    # 3. Document outline (built from headings)
    document_outline = build_document_outline(headings)

    # 4. All other extractors
    callouts = extract_callouts(content, source_file)
    wiki_links = extract_wiki_links(content, source_file, headings)
    inline_fields = extract_inline_fields(content, source_file)
    definitions = extract_definitions(content, source_file)
    tags = extract_tags(content, source_file)
    code_blocks = extract_code_blocks(content, source_file)
    tables = extract_tables(content, source_file)
    external_links = extract_external_links(content, source_file)
    embeds = extract_embeds(content, source_file)
    block_refs = extract_block_references(content, source_file)
    mermaid_diagrams = extract_mermaid(content, source_file)
    footnotes = extract_footnotes(content, source_file)
    color_spans = extract_color_spans(content, source_file)
    lists = extract_lists(content, source_file)
    html_comments = extract_html_comments(content, source_file)
    obsidian_comments = extract_obsidian_comments(content, source_file)
    math_expressions = extract_math_expressions(content, source_file)

    # 5. Document statistics
    doc_stats = compute_document_stats(content)

    # 6. Knowledge graph analysis
    knowledge_graph = build_knowledge_graph_analysis(
        wiki_links, tags, frontmatter_data
    )

    # ── Assemble extraction results ───────────────────────────────────────
    extraction_results = {
        "frontmatter_data": frontmatter_data,
        "headings": headings,
        "document_outline": document_outline,
        "callouts": callouts,
        "wiki_links": wiki_links,
        "inline_fields": inline_fields,
        "definitions": definitions,
        "tags": tags,
        "code_blocks": code_blocks,
        "tables": tables,
        "external_links": external_links,
        "embeds": embeds,
        "block_references": block_refs,
        "mermaid_diagrams": mermaid_diagrams,
        "footnotes": footnotes,
        "color_spans": color_spans,
        "lists": lists,
        "html_comments": html_comments,
        "obsidian_comments": obsidian_comments,
        "math_expressions": math_expressions,
        "document_stats": doc_stats,
        "knowledge_graph": knowledge_graph,
    }

    # ── Calculate processing time ─────────────────────────────────────────
    processing_time = round(time.time() - start_time, 3)
    metadata["processing_time"] = processing_time

    # ══════════════════════════════════════════════════════════════════════
    # GENERATE OUTPUTS
    # ══════════════════════════════════════════════════════════════════════

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # ── JSON Output ───────────────────────────────────────────────────────
    json_data = build_json_output(extraction_results, metadata)
    json_path = os.path.join(output_dir, f"{source_stem}_extracted.json")
    write_json_output(json_data, json_path)

    # ── Markdown Report ───────────────────────────────────────────────────
    md_report = build_markdown_report(extraction_results, metadata)
    md_path = os.path.join(output_dir, f"{source_stem}_report.md")
    write_markdown_report(md_report, md_path)

    # ── Calculate total items ─────────────────────────────────────────────
    total_items = json_data["extraction_summary"]["total_items_extracted"]

    return {
        "success": True,
        "file": input_path,
        "total_items": total_items,
        "json_output": json_path,
        "md_output": md_path,
        "processing_time": processing_time,
    }


def process_directory(input_dir: str, output_dir: str, recursive: bool = True):
    """
    Process all Markdown files in a directory (and optionally subdirectories).

    Shows progress for each file and prints a summary at the end.

    Args:
        input_dir:  Path to directory containing .md files to process.
        output_dir: Path where JSON and Markdown outputs will be saved.
        recursive:  If True, also process files in subdirectories.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Find all Markdown files
    glob_pattern = "**/*.md" if recursive else "*.md"
    md_files = sorted(input_path.glob(glob_pattern))

    if not md_files:
        print(f"\nNo .md files found in: {input_dir}")
        if not recursive:
            print("  Tip: Use --recursive to include subdirectories.")
        return

    print(f"\n{'='*60}")
    print(f"  PKB Extraction Pipeline v{SCRIPT_VERSION}")
    print(f"{'='*60}")
    print(f"  Input:     {input_dir}")
    print(f"  Output:    {output_dir}")
    print(f"  Files:     {len(md_files)} Markdown file(s) found")
    print(f"  Recursive: {'Yes' if recursive else 'No'}")
    print(f"{'='*60}\n")

    results = []
    total_start = time.time()

    for i, file_path in enumerate(md_files, 1):
        print(f"  [{i:>3}/{len(md_files)}] {file_path.name}")

        try:
            result = process_single_file(str(file_path), output_dir)
            if result["success"]:
                count = result.get("total_items", 0)
                t = result.get("processing_time", 0)
                print(f"           ✓ {count} items extracted ({t}s)")
            else:
                print(f"           ✗ Failed: {result.get('error', 'Unknown')}")
            results.append(result)
        except Exception as e:
            print(f"           ✗ Error: {e}")
            results.append({
                "file": str(file_path),
                "success": False,
                "error": str(e),
            })

    # ── Print Summary ─────────────────────────────────────────────────────
    total_time = round(time.time() - total_start, 2)
    success_count = sum(1 for r in results if r.get("success"))
    total_items = sum(r.get("total_items", 0) for r in results)

    print(f"\n{'='*60}")
    print(f"  SUMMARY")
    print(f"{'='*60}")
    print(f"  Files Processed: {success_count}/{len(md_files)}")
    print(f"  Total Items:     {total_items:,}")
    print(f"  Total Time:      {total_time}s")
    print(f"  Outputs:         {output_dir}")
    print(f"{'='*60}\n")


# ══════════════════════════════════════════════════════════════════════════════
# CLI INTERFACE
# ══════════════════════════════════════════════════════════════════════════════

def create_argument_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser with user-friendly help text.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog=SCRIPT_NAME,
        description=(
            "PKB Markdown Extraction Pipeline\n"
            "================================\n\n"
            "Extracts callouts, wiki-links, inline fields, definitions,\n"
            "headings, tags, code blocks, tables, and more from Obsidian\n"
            "Markdown files. Produces both JSON (machine-readable) and\n"
            "Markdown report (human-readable) outputs.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  %(prog)s --input report.md\n"
            "  %(prog)s --input ./vault/reports/ --output ./extracted/\n"
            "  %(prog)s --input ./vault/ --recursive --output ./output/\n"
        ),
    )

    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to a single .md file OR a directory of .md files',
    )

    parser.add_argument(
        '--output', '-o',
        default=None,
        help='Output directory for JSON and Markdown files '
             '(default: same directory as input, or ./extracted/)',
    )

    parser.add_argument(
        '--recursive', '-r',
        action='store_true',
        default=False,
        help='Process subdirectories recursively (directory mode only)',
    )

    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'{SCRIPT_NAME} v{SCRIPT_VERSION}',
    )

    return parser


def main():
    """
    Entry point: parse arguments and run the extraction pipeline.
    """
    parser = create_argument_parser()
    args = parser.parse_args()

    input_path = Path(args.input)

    # Determine if input is a file or directory
    if input_path.is_file():
        # Single file mode
        if not input_path.suffix.lower() == '.md':
            print(f"ERROR: Input file must be a .md file: {input_path}")
            sys.exit(1)

        # Default output: same directory as input file
        output_dir = args.output or str(input_path.parent)

        print(f"\n  Processing: {input_path.name}")
        result = process_single_file(str(input_path), output_dir)

        if result["success"]:
            print(f"  ✓ {result['total_items']} items extracted in {result['processing_time']}s")
            print(f"  JSON:     {result['json_output']}")
            print(f"  Report:   {result['md_output']}")
        else:
            print(f"  ✗ Failed: {result.get('error', 'Unknown error')}")
            sys.exit(1)

    elif input_path.is_dir():
        # Directory mode
        output_dir = args.output or str(input_path / "extracted")
        process_directory(str(input_path), output_dir, recursive=args.recursive)

    else:
        print(f"ERROR: Path not found: {input_path}")
        print(f"  → Check that the path exists and is a file or directory.")
        sys.exit(1)


# ══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
