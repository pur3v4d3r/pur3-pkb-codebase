#!/usr/bin/env python3
"""
dedicated_notes_builder.py — Build Dedicated Aggregate Index Notes
═══════════════════════════════════════════════════════════════════════════════
Scans all extraction batch JSON files and builds four dedicated aggregate
notes that collect specific callout types across ALL reports into single
organised Obsidian notes:

  1. Master Definition Index    — All definitions, sorted alphabetically + TOC
  2. Master Reference Index     — All citations, sorted by topic + TOC
  3. Master PKB Connections     — All connections-and-links, sorted by topic + TOC
  4. Master Expansion Topics    — All topic-ideas, sorted by topic + TOC

Additionally:
  - Ensures every definition has a corresponding permanent note (creates or updates)
  - Links all entries to existing permanent notes via wiki-links

USAGE:
  python dedicated_notes_builder.py                          # Dry run
  python dedicated_notes_builder.py --execute                # Apply changes
  python dedicated_notes_builder.py --execute --only=defs    # Only definitions
  python dedicated_notes_builder.py --stats                  # Show callout stats

REQUIRES: Python 3.10+
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

# ══════════════════════════════════════════════════════════════════════════════
# FORCE UTF-8 ON WINDOWS
# ══════════════════════════════════════════════════════════════════════════════
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True
    )

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

VAULT_ROOT = Path(r"D:\10_pur3v4d3r's-vault")
EXTRACTOR_OUTPUT_ROOT = VAULT_ROOT / "999-report-organizing" / "_extractor-output"
PERMANENT_NOTES_DIR = (
    VAULT_ROOT / "999-report-organizing"
    / "_permanent-notes" / "_permanent-notes"
)
PIPELINE_DIR = (
    VAULT_ROOT / "99-scripts" / "report-extraction-to-permanent-notes-building"
)

# Dedicated note filenames (prefixed with _ to sort to top of directory)
DEFINITION_INDEX_FILE = "_Master-Definition-Index.md"
REFERENCE_INDEX_FILE = "_Master-Reference-Index.md"
CONNECTIONS_INDEX_FILE = "_Master-PKB-Connections-Index.md"
EXPANSION_INDEX_FILE = "_Master-Expansion-Topics-Index.md"

# Callout types that feed each dedicated note
DEFINITION_CALLOUT_TYPES = ["definition"]
REFERENCE_CALLOUT_TYPES = ["cite", "citation", "references", "bibliography"]
CONNECTION_CALLOUT_TYPES = ["connections-and-links", "connection-ideas", "connections"]
EXPANSION_CALLOUT_TYPES = ["topic-idea", "further-exploration"]

# Domain mapping for topic grouping (reuse from config.py)
DOMAIN_DISPLAY_NAMES = {
    "cognitive-psychology": "Cognitive Psychology",
    "educational-psychology": "Educational Psychology",
    "philosophy": "Philosophy",
    "neuroscience": "Neuroscience",
    "prompt-engineering": "Prompt Engineering",
    "computer-science": "Computer Science",
    "decision-science": "Decision Science",
    "epistemology": "Epistemology",
    "learning-science": "Learning Science",
    "linguistics": "Linguistics",
    "mathematics": "Mathematics",
    "systems-thinking": "Systems Thinking",
    "other": "Other / Uncategorised",
}

MAX_FILENAME_LENGTH = 80


# ══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class CalloutEntry:
    """A single extracted callout with its metadata."""
    callout_type: str
    title: str
    body: str
    source_report: str
    source_json: str
    report_domain: str = "other"
    line_number: int = 0
    wiki_links: list[str] = field(default_factory=list)


@dataclass
class DefinitionEntry:
    """A parsed definition with concept name, domain, and body."""
    concept_name: str
    domain: str
    attribution: str
    body: str
    source_report: str
    wiki_links: list[str] = field(default_factory=list)

    @property
    def sort_key(self) -> str:
        return self.concept_name.lower().lstrip("the ").strip()


@dataclass
class BuildReport:
    """Report of what was built/changed."""
    definitions_collected: int = 0
    references_collected: int = 0
    connections_collected: int = 0
    expansions_collected: int = 0
    definition_notes_created: int = 0
    definition_notes_already_exist: int = 0
    dedicated_notes_written: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    dry_run: bool = True


# ══════════════════════════════════════════════════════════════════════════════
# JSON SCANNING
# ══════════════════════════════════════════════════════════════════════════════

def find_all_json_files(root: Path) -> list[Path]:
    """Find all extraction JSON files across all batches."""
    if not root.exists():
        return []
    return sorted(root.rglob("*_extracted.json"))


def extract_report_domain(data: dict) -> str:
    """Extract the primary domain from a report's JSON metadata."""
    fm = data.get("document_metadata", {}).get("frontmatter", {})
    domain = fm.get("primary_domain", "")
    if isinstance(domain, str) and domain.strip():
        return domain.strip().lower()
    return "other"


def extract_source_filename(data: dict) -> str:
    """Extract the source report filename from JSON metadata."""
    ext = data.get("extraction_metadata", {})
    source = ext.get("source_file", "")
    if source:
        return source.replace(".md", "")
    return ""


def extract_wiki_links(data: dict) -> list[str]:
    """Extract all wiki-link targets from a report's JSON."""
    items = data.get("extracted_items", {}).get("wiki_links", [])
    return sorted({item.get("target", "") for item in items if item.get("target")})


def scan_all_callouts(
    json_files: list[Path],
) -> dict[str, list[CalloutEntry]]:
    """
    Scan all JSON files and collect callouts grouped by category.

    Returns dict with keys: 'definitions', 'references', 'connections', 'expansions'
    """
    results: dict[str, list[CalloutEntry]] = {
        "definitions": [],
        "references": [],
        "connections": [],
        "expansions": [],
    }

    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue

        domain = extract_report_domain(data)
        source = extract_source_filename(data)
        wiki_links = extract_wiki_links(data)

        callouts = data.get("extracted_items", {}).get("callouts", [])

        for callout in callouts:
            ctype = callout.get("type", "").lower().strip()
            title = callout.get("title", "").strip()
            body = callout.get("body", "").strip()
            line_num = callout.get("line_number", 0)

            if not body and not title:
                continue

            entry = CalloutEntry(
                callout_type=ctype,
                title=title,
                body=body,
                source_report=source,
                source_json=jf.name,
                report_domain=domain,
                line_number=line_num,
                wiki_links=wiki_links,
            )

            if ctype in DEFINITION_CALLOUT_TYPES:
                results["definitions"].append(entry)
            elif ctype in REFERENCE_CALLOUT_TYPES:
                results["references"].append(entry)
            elif ctype in CONNECTION_CALLOUT_TYPES:
                results["connections"].append(entry)
            elif ctype in EXPANSION_CALLOUT_TYPES:
                results["expansions"].append(entry)

    return results


# ══════════════════════════════════════════════════════════════════════════════
# DEFINITION PARSING
# ══════════════════════════════════════════════════════════════════════════════

def parse_definition_title(raw_title: str) -> tuple[str, str, str]:
    """
    Parse a definition callout title into (concept_name, domain, attribution).
    Mirrors the logic in report_parser.py.
    """
    title = raw_title.strip()
    title = re.sub(r"^\*\*\s*", "", title)

    if "**" in title:
        parts = title.split("**", 1)
        concept_name = parts[0].strip()
        rest = parts[1].strip()
    else:
        paren_match = re.match(r"^([^(]+)\((.+)\)\s*$", title)
        if paren_match:
            concept_name = paren_match.group(1).strip()
            rest = f"({paren_match.group(2)})"
        else:
            concept_name = title
            rest = ""

    domain = "other"
    attribution = ""

    paren_match = re.search(r"\(([^)]+)\)", rest)
    if paren_match:
        paren_content = paren_match.group(1)
        if "\u2014" in paren_content:
            domain_raw, attribution = paren_content.split("\u2014", 1)
        elif "\u2013" in paren_content:
            domain_raw, attribution = paren_content.split("\u2013", 1)
        elif " - " in paren_content:
            domain_raw, attribution = paren_content.split(" - ", 1)
        else:
            domain_raw = paren_content
            attribution = ""

        domain_raw = domain_raw.strip().lower()
        attribution = attribution.strip()

        # Normalise domain
        domain_map = {
            "cognitive psychology": "cognitive-psychology",
            "educational philosophy": "educational-psychology",
            "educational psychology": "educational-psychology",
            "philosophy": "philosophy",
            "neuroscience": "neuroscience",
            "information science": "learning-science",
            "knowledge management": "learning-science",
            "cognitive science": "cognitive-psychology",
            "epistemology": "epistemology",
            "learning science": "learning-science",
            "social psychology": "cognitive-psychology",
            "motivation research": "educational-psychology",
            "instructional design": "educational-psychology",
            "metacognition": "cognitive-psychology",
            "network science": "systems-thinking",
            "novel synthesis": "cognitive-psychology",
            "systems thinking": "systems-thinking",
            "decision science": "decision-science",
            "computer science": "computer-science",
            "prompt engineering": "prompt-engineering",
        }
        domain_parts = [d.strip() for d in domain_raw.split("/") if d.strip()]
        for dpart in domain_parts:
            if dpart in domain_map:
                domain = domain_map[dpart]
                break
            elif dpart.replace(" ", "-") in DOMAIN_DISPLAY_NAMES:
                domain = dpart.replace(" ", "-")
                break

    # Clean concept name
    concept_name = re.sub(r"<[^>]+>", "", concept_name).strip()
    concept_name = re.sub(r"^\*+|\*+$", "", concept_name).strip()
    concept_name = concept_name.replace("[[", "").replace("]]", "").strip()

    return concept_name, domain, attribution


def parse_definitions(entries: list[CalloutEntry]) -> list[DefinitionEntry]:
    """Parse callout entries into structured DefinitionEntry objects."""
    definitions = []
    seen_names = set()

    for entry in entries:
        concept_name, domain, attribution = parse_definition_title(entry.title)

        if not concept_name or len(concept_name) < 3:
            continue

        # Skip template placeholders
        if re.match(r"^\{.*\}$", concept_name):
            continue
        if re.match(r"^[^a-zA-Z]*$", concept_name):
            continue

        blocklist = {
            "purpose", "definition", "tools", "resources", "prompts",
            "feedback", "mastery", "information", "overview", "summary",
            "introduction", "conclusion", "references", "background",
            "methodology", "results", "discussion", "appendix",
            "core definition", "core concept", "key terms", "understanding",
            "script", "untitled",
        }
        if concept_name.lower() in blocklist:
            continue

        # Use report domain as fallback
        if domain == "other" and entry.report_domain != "other":
            domain = entry.report_domain

        # Deduplicate by name (keep first occurrence)
        norm_name = concept_name.lower().strip()
        if norm_name in seen_names:
            continue
        seen_names.add(norm_name)

        definitions.append(DefinitionEntry(
            concept_name=concept_name,
            domain=domain,
            attribution=attribution,
            body=entry.body,
            source_report=entry.source_report,
            wiki_links=entry.wiki_links,
        ))

    definitions.sort(key=lambda d: d.sort_key)
    return definitions


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY: WIKI-LINK HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def sanitize_filename(name: str) -> str:
    """Convert a concept name to a safe Obsidian filename stem."""
    safe = re.sub(r'[<>:"/\\|?*\[\]()]', "", name)
    safe = re.sub(r"[\s_]+", "-", safe)
    safe = re.sub(r"-{2,}", "-", safe)
    safe = safe.strip("-")
    if len(safe) > MAX_FILENAME_LENGTH:
        safe = safe[:MAX_FILENAME_LENGTH].rstrip("-")
    return safe


def pipe_link(display_name: str) -> str:
    """Build [[Filename-Stem|Display Name]] wiki-link."""
    stem = sanitize_filename(display_name)
    if stem == display_name:
        return f"[[{display_name}]]"
    return f"[[{stem}|{display_name}]]"


def get_existing_note_stems(notes_dir: Path) -> set[str]:
    """Get set of lowercase filename stems from permanent notes directory."""
    if not notes_dir.exists():
        return set()
    return {f.stem.lower() for f in notes_dir.glob("*.md")}


# ══════════════════════════════════════════════════════════════════════════════
# FRONTMATTER BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def build_dedicated_note_frontmatter(
    title: str,
    note_type: str,
    description: str,
    tags: list[str],
) -> str:
    """Build YAML frontmatter for a dedicated aggregate note."""
    today = date.today().isoformat()
    tag_lines = "\n".join(f"  - {t}" for t in tags)

    return f"""---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "{title}"
aliases:
  - "{title.replace('Master ', '')}"
type: {note_type}
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
{tag_lines}

domain: multi-domain
subdomains:
  - cognitive-psychology
  - educational-psychology
  - philosophy

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: {today}
updated: {today}

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: pipeline-aggregate
extraction-method: "dedicated_notes_builder.py v1.0"
description: "{description}"

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: monthly
mastery-stage: evergreen
importance: high
---"""


# ══════════════════════════════════════════════════════════════════════════════
# BUILDER: MASTER DEFINITION INDEX
# ══════════════════════════════════════════════════════════════════════════════

def build_definition_index(definitions: list[DefinitionEntry], existing_stems: set[str]) -> str:
    """
    Build the Master Definition Index note.

    Structure:
    - YAML frontmatter
    - Overview with stats
    - Alphabetical table of contents
    - Definitions grouped by first letter, each with:
      - Definition callout
      - Link to permanent note
      - Source report attribution
    """
    frontmatter = build_dedicated_note_frontmatter(
        title="Master Definition Index",
        note_type="index-note",
        description="Alphabetical index of all definitions extracted from reports",
        tags=["index-note", "definitions", "permanent-note", "evergreen", "pkb-infrastructure"],
    )

    lines = [frontmatter, "", "# Master Definition Index", ""]
    lines.append("> [!abstract] Overview")
    lines.append(f"> This index collects **{len(definitions)} unique definitions** extracted from reports across the PKB.")
    lines.append("> Each definition links to its corresponding permanent note. Definitions without a permanent note are flagged for creation.")
    lines.append(f"> ")
    lines.append(f"> *Auto-generated by `dedicated_notes_builder.py` on {date.today().isoformat()}*")
    lines.append("")

    # Stats
    has_note = sum(1 for d in definitions if sanitize_filename(d.concept_name).lower() in existing_stems)
    missing_note = len(definitions) - has_note
    domain_counts = defaultdict(int)
    for d in definitions:
        domain_counts[d.domain] += 1

    lines.append("## Statistics")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total definitions | {len(definitions)} |")
    lines.append(f"| With permanent note | {has_note} |")
    lines.append(f"| Missing permanent note | {missing_note} |")
    lines.append("")

    lines.append("**By Domain:**")
    lines.append("")
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        lines.append(f"- {display}: {count}")
    lines.append("")

    # Table of Contents (alphabetical groups)
    letter_groups: dict[str, list[DefinitionEntry]] = defaultdict(list)
    for d in definitions:
        first = d.sort_key[0].upper() if d.sort_key else "#"
        if not first.isalpha():
            first = "#"
        letter_groups[first].append(d)

    lines.append("## Table of Contents")
    lines.append("")
    for letter in sorted(letter_groups.keys()):
        count = len(letter_groups[letter])
        lines.append(f"- [[#_{letter}|{letter}]] ({count} definitions)")
    lines.append("")

    # Definition entries by letter
    lines.append("---")
    lines.append("")

    for letter in sorted(letter_groups.keys()):
        group = letter_groups[letter]
        lines.append(f"## _{letter}")
        lines.append("")

        for defn in group:
            stem = sanitize_filename(defn.concept_name).lower()
            has_perm = stem in existing_stems
            link = pipe_link(defn.concept_name)
            status_icon = "**[perm-note]**" if has_perm else "*[needs-note]*"

            lines.append(f"> [!definition] **{defn.concept_name}** {status_icon}")

            # Body text (truncate if very long)
            body = defn.body.strip()
            if len(body) > 600:
                body = body[:597] + "..."
            for body_line in body.split("\n"):
                lines.append(f"> {body_line}")

            lines.append(f"> ")
            if defn.attribution:
                lines.append(f"> *Attribution: {defn.attribution}*")
            lines.append(f"> *Source: {defn.source_report}* | *Domain: {DOMAIN_DISPLAY_NAMES.get(defn.domain, defn.domain)}*")
            lines.append(f"> *Permanent Note: {link}*")
            lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append(f"*Index contains {len(definitions)} definitions from {len(set(d.source_report for d in definitions))} reports.*")
    lines.append(f"*Last updated: {date.today().isoformat()}*")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# BUILDER: MASTER REFERENCE INDEX
# ══════════════════════════════════════════════════════════════════════════════

def build_reference_index(entries: list[CalloutEntry]) -> str:
    """
    Build the Master Reference Index note.
    References are grouped by source report domain/topic.
    """
    frontmatter = build_dedicated_note_frontmatter(
        title="Master Reference Index",
        note_type="index-note",
        description="All academic references and citations extracted from reports, organised by topic",
        tags=["index-note", "references", "citations", "evergreen", "pkb-infrastructure"],
    )

    # Group by domain
    by_domain: dict[str, list[CalloutEntry]] = defaultdict(list)
    for entry in entries:
        by_domain[entry.report_domain].append(entry)

    lines = [frontmatter, "", "# Master Reference Index", ""]
    lines.append("> [!abstract] Overview")
    lines.append(f"> This index collects **{len(entries)} citations** from reports across the PKB,")
    lines.append(f"> organised by topic domain. Use this as a bibliography and source-tracking hub.")
    lines.append(f"> ")
    lines.append(f"> *Auto-generated by `dedicated_notes_builder.py` on {date.today().isoformat()}*")
    lines.append("")

    # Stats
    lines.append("## Statistics")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total citations | {len(entries)} |")
    lines.append(f"| Topic areas | {len(by_domain)} |")
    lines.append(f"| Source reports | {len(set(e.source_report for e in entries))} |")
    lines.append("")

    # TOC
    lines.append("## Table of Contents")
    lines.append("")
    for domain in sorted(by_domain.keys()):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        count = len(by_domain[domain])
        safe_anchor = domain.replace(" ", "-")
        lines.append(f"- [[#{safe_anchor}|{display}]] ({count} references)")
    lines.append("")

    lines.append("---")
    lines.append("")

    # References by domain
    for domain in sorted(by_domain.keys()):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        domain_entries = by_domain[domain]
        lines.append(f"## {display}")
        lines.append("")

        # Sub-group by source report
        by_report: dict[str, list[CalloutEntry]] = defaultdict(list)
        for entry in domain_entries:
            by_report[entry.source_report or "Unknown"].append(entry)

        for report, report_entries in sorted(by_report.items()):
            report_link = f"[[{sanitize_filename(report)}|{report}]]" if report != "Unknown" else "Unknown"
            lines.append(f"### From: {report_link}")
            lines.append("")

            for entry in report_entries:
                body = entry.body.strip()
                if body:
                    # Render each citation as a callout
                    lines.append(f"> [!cite] Reference")
                    for body_line in body.split("\n"):
                        lines.append(f"> {body_line}")
                    lines.append("")

        lines.append("---")
        lines.append("")

    lines.append(f"*Index contains {len(entries)} references from {len(set(e.source_report for e in entries))} reports.*")
    lines.append(f"*Last updated: {date.today().isoformat()}*")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# BUILDER: MASTER PKB CONNECTIONS INDEX
# ══════════════════════════════════════════════════════════════════════════════

def build_connections_index(entries: list[CalloutEntry], existing_stems: set[str]) -> str:
    """
    Build the Master PKB Connections Index note.
    Connections are grouped by source report domain/topic.
    """
    frontmatter = build_dedicated_note_frontmatter(
        title="Master PKB Connections Index",
        note_type="index-note",
        description="All internal PKB connections extracted from reports, organised by topic",
        tags=["index-note", "connections", "knowledge-graph", "evergreen", "pkb-infrastructure"],
    )

    by_domain: dict[str, list[CalloutEntry]] = defaultdict(list)
    for entry in entries:
        by_domain[entry.report_domain].append(entry)

    # Extract all wiki-links from connection bodies
    all_mentioned = set()
    wikilink_re = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
    for entry in entries:
        for match in wikilink_re.finditer(entry.body):
            all_mentioned.add(match.group(1).strip())

    linked_to_existing = {n for n in all_mentioned if sanitize_filename(n).lower() in existing_stems}

    lines = [frontmatter, "", "# Master PKB Connections Index", ""]
    lines.append("> [!abstract] Overview")
    lines.append(f"> This index collects **{len(entries)} PKB connection blocks** from reports,")
    lines.append(f"> mapping how report content integrates with your existing knowledge graph.")
    lines.append(f"> ")
    lines.append(f"> **{len(all_mentioned)} unique concepts** referenced across connections.")
    lines.append(f"> **{len(linked_to_existing)}** link to existing permanent notes.")
    lines.append(f"> ")
    lines.append(f"> *Auto-generated by `dedicated_notes_builder.py` on {date.today().isoformat()}*")
    lines.append("")

    # Stats
    lines.append("## Statistics")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total connection blocks | {len(entries)} |")
    lines.append(f"| Unique concepts mentioned | {len(all_mentioned)} |")
    lines.append(f"| Links to existing notes | {len(linked_to_existing)} |")
    lines.append(f"| Topic areas | {len(by_domain)} |")
    lines.append("")

    # TOC
    lines.append("## Table of Contents")
    lines.append("")
    for domain in sorted(by_domain.keys()):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        count = len(by_domain[domain])
        safe_anchor = domain.replace(" ", "-")
        lines.append(f"- [[#{safe_anchor}|{display}]] ({count} connection blocks)")
    lines.append("")

    lines.append("---")
    lines.append("")

    # Connections by domain
    for domain in sorted(by_domain.keys()):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        domain_entries = by_domain[domain]
        lines.append(f"## {display}")
        lines.append("")

        for entry in domain_entries:
            report_link = f"[[{sanitize_filename(entry.source_report)}|{entry.source_report}]]" if entry.source_report else "Unknown"
            lines.append(f"> [!connections-and-links] From: {report_link}")
            body = entry.body.strip()
            for body_line in body.split("\n"):
                lines.append(f"> {body_line}")
            lines.append("")

        lines.append("---")
        lines.append("")

    lines.append(f"*Index contains {len(entries)} connection blocks from {len(set(e.source_report for e in entries))} reports.*")
    lines.append(f"*Last updated: {date.today().isoformat()}*")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# BUILDER: MASTER EXPANSION TOPICS INDEX
# ══════════════════════════════════════════════════════════════════════════════

def build_expansion_index(entries: list[CalloutEntry], existing_stems: set[str]) -> str:
    """
    Build the Master Expansion Topics Index note.
    Topics are grouped by domain/topic area.
    """
    frontmatter = build_dedicated_note_frontmatter(
        title="Master Expansion Topics Index",
        note_type="index-note",
        description="All expansion topics and further exploration ideas from reports, organised by topic",
        tags=["index-note", "expansion-topics", "research-ideas", "evergreen", "pkb-infrastructure"],
    )

    by_domain: dict[str, list[CalloutEntry]] = defaultdict(list)
    for entry in entries:
        by_domain[entry.report_domain].append(entry)

    # Extract topic names from bodies (look for [[Topic-Name]] patterns)
    wikilink_re = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
    all_topics = set()
    for entry in entries:
        for match in wikilink_re.finditer(entry.body):
            all_topics.add(match.group(1).strip())
        for match in wikilink_re.finditer(entry.title):
            all_topics.add(match.group(1).strip())

    topics_with_notes = {t for t in all_topics if sanitize_filename(t).lower() in existing_stems}

    lines = [frontmatter, "", "# Master Expansion Topics Index", ""]
    lines.append("> [!abstract] Overview")
    lines.append(f"> This index collects **{len(entries)} expansion topics** and research ideas")
    lines.append(f"> suggested across all reports. These represent potential paths for deepening")
    lines.append(f"> your knowledge graph.")
    lines.append(f"> ")
    lines.append(f"> **{len(all_topics)} unique topics** referenced.")
    lines.append(f"> **{len(topics_with_notes)}** already have permanent notes.")
    lines.append(f"> ")
    lines.append(f"> *Auto-generated by `dedicated_notes_builder.py` on {date.today().isoformat()}*")
    lines.append("")

    # Stats
    lines.append("## Statistics")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total expansion entries | {len(entries)} |")
    lines.append(f"| Unique topics referenced | {len(all_topics)} |")
    lines.append(f"| Topics with permanent notes | {len(topics_with_notes)} |")
    lines.append(f"| Topics needing notes | {len(all_topics) - len(topics_with_notes)} |")
    lines.append(f"| Topic areas | {len(by_domain)} |")
    lines.append("")

    # TOC
    lines.append("## Table of Contents")
    lines.append("")
    for domain in sorted(by_domain.keys()):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        count = len(by_domain[domain])
        safe_anchor = domain.replace(" ", "-")
        lines.append(f"- [[#{safe_anchor}|{display}]] ({count} topics)")
    lines.append("")

    lines.append("---")
    lines.append("")

    # Expansion topics by domain
    for domain in sorted(by_domain.keys()):
        display = DOMAIN_DISPLAY_NAMES.get(domain, domain.replace("-", " ").title())
        domain_entries = by_domain[domain]
        lines.append(f"## {display}")
        lines.append("")

        for entry in domain_entries:
            report_link = f"[[{sanitize_filename(entry.source_report)}|{entry.source_report}]]" if entry.source_report else "Unknown"
            callout_label = "topic-idea" if entry.callout_type == "topic-idea" else "further-exploration"
            lines.append(f"> [!{callout_label}] From: {report_link}")

            body = entry.body.strip()
            if entry.title and entry.title.lower() != "untitled":
                # Include title as first line
                lines.append(f"> **{entry.title}**")
                lines.append(f"> ")

            for body_line in body.split("\n"):
                lines.append(f"> {body_line}")
            lines.append("")

        lines.append("---")
        lines.append("")

    lines.append(f"*Index contains {len(entries)} expansion topics from {len(set(e.source_report for e in entries))} reports.*")
    lines.append(f"*Last updated: {date.today().isoformat()}*")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# DEFINITION PERMANENT NOTE ENSURER
# ══════════════════════════════════════════════════════════════════════════════

def build_minimal_definition_note(defn: DefinitionEntry) -> str:
    """Build a minimal permanent note for a definition that doesn't have one yet."""
    today = date.today().isoformat()
    clean_name = defn.concept_name.replace("[[", "").replace("]]", "").strip()
    stem = sanitize_filename(clean_name)
    domain = defn.domain if defn.domain in DOMAIN_DISPLAY_NAMES else "other"

    tags = ["permanent-note", "evergreen", domain, "definition-sourced"]
    tag_lines = "\n".join(f"  - {t}" for t in tags)

    frontmatter = f"""---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "{clean_name}"
aliases:
  - "{clean_name}"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
{tag_lines}

domain: {domain}
subdomains:
  -

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: {today}
updated: {today}

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "{defn.source_report}"
evidence-quality: medium
extraction-method: "dedicated_notes_builder.py v1.0 — definition-sourced"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: foundational

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  []

related:
  []

broader:
  []

narrower:
  []

see-also:
  []

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  []

enables:
  []

expansion-topics:
  []

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---"""

    body_lines = [
        f"# {clean_name}",
        "",
        f"> [!definition] **{clean_name}**",
    ]
    for line in defn.body.split("\n"):
        body_lines.append(f"> {line}")

    body_lines.append("")
    if defn.attribution:
        body_lines.append(f"*Source: {defn.attribution}*")
        body_lines.append("")

    body_lines.extend([
        "## Core Explanation",
        "",
        "<!-- Expand this section with deeper explanation -->",
        "",
        "## Practical Implications",
        "",
        "> [!example] **Application**",
        "> *Describe how this concept applies in practice.*",
        "",
        "## Connections & Context",
        "",
    ])

    # Add wiki-link cloud from source report
    if defn.wiki_links:
        relevant = [wl for wl in defn.wiki_links[:15] if wl.lower() != clean_name.lower()]
        if relevant:
            link_text = " \u00b7 ".join(pipe_link(wl) for wl in relevant)
            body_lines.append(f"**Related concepts:** {link_text}")
            body_lines.append("")

    return frontmatter + "\n\n" + "\n".join(body_lines)


def ensure_definition_permanent_notes(
    definitions: list[DefinitionEntry],
    existing_stems: set[str],
    notes_dir: Path,
    dry_run: bool = True,
) -> tuple[int, int, list[str]]:
    """
    Ensure every definition has a permanent note.
    Creates new minimal notes for definitions that don't have one.

    Returns (created_count, already_exist_count, errors)
    """
    created = 0
    exists = 0
    errors = []

    for defn in definitions:
        stem = sanitize_filename(defn.concept_name)
        stem_lower = stem.lower()

        if stem_lower in existing_stems:
            exists += 1
            continue

        # Create the note
        filepath = notes_dir / f"{stem}.md"

        if not dry_run:
            try:
                content = build_minimal_definition_note(defn)
                filepath.write_text(content, encoding="utf-8")
                existing_stems.add(stem_lower)  # Update for subsequent checks
                created += 1
            except Exception as e:
                errors.append(f"Failed to create {stem}.md: {e}")
        else:
            created += 1  # Count what would be created

    return created, exists, errors


# ══════════════════════════════════════════════════════════════════════════════
# MAIN BUILDER
# ══════════════════════════════════════════════════════════════════════════════

class DedicatedNotesBuilder:
    """Orchestrates building all 4 dedicated aggregate notes."""

    def __init__(self, dry_run: bool = True, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.report = BuildReport(dry_run=dry_run)

    def run(
        self,
        only: str | None = None,
        skip_perm_notes: bool = False,
    ) -> BuildReport:
        """
        Run the full dedicated notes build process.

        Args:
            only: If set, only build one type: 'defs', 'refs', 'conns', 'expns'
            skip_perm_notes: If True, skip creating permanent notes for definitions
        """
        mode = "DRY RUN" if self.dry_run else "EXECUTE"
        print(f"\n{'=' * 72}")
        print(f"  DEDICATED NOTES BUILDER — {mode}")
        print(f"{'=' * 72}")

        # 1. Scan all JSON files
        print(f"\n  Scanning extraction batches...")
        json_files = find_all_json_files(EXTRACTOR_OUTPUT_ROOT)
        print(f"  Found {len(json_files)} JSON files across extraction batches")

        if not json_files:
            print("  No JSON files found. Nothing to build.")
            return self.report

        # 2. Collect all callouts
        print(f"  Collecting callouts...")
        callouts = scan_all_callouts(json_files)

        self.report.definitions_collected = len(callouts["definitions"])
        self.report.references_collected = len(callouts["references"])
        self.report.connections_collected = len(callouts["connections"])
        self.report.expansions_collected = len(callouts["expansions"])

        print(f"  Definitions: {self.report.definitions_collected}")
        print(f"  References:  {self.report.references_collected}")
        print(f"  Connections: {self.report.connections_collected}")
        print(f"  Expansions:  {self.report.expansions_collected}")

        # 3. Get existing note stems
        existing_stems = get_existing_note_stems(PERMANENT_NOTES_DIR)
        print(f"\n  Existing permanent notes: {len(existing_stems)}")

        # 4. Build each dedicated note
        build_all = only is None

        if build_all or only == "defs":
            self._build_definitions(callouts["definitions"], existing_stems, skip_perm_notes)

        if build_all or only == "refs":
            self._build_references(callouts["references"])

        if build_all or only == "conns":
            self._build_connections(callouts["connections"], existing_stems)

        if build_all or only == "expns":
            self._build_expansions(callouts["expansions"], existing_stems)

        # 5. Summary
        self._print_summary()
        return self.report

    def _build_definitions(
        self,
        raw_entries: list[CalloutEntry],
        existing_stems: set[str],
        skip_perm_notes: bool,
    ):
        """Build the Definition Index and ensure permanent notes exist."""
        print(f"\n  {'─' * 60}")
        print(f"  Building: Master Definition Index")
        print(f"  {'─' * 60}")

        definitions = parse_definitions(raw_entries)
        print(f"  Parsed {len(definitions)} unique definitions from {len(raw_entries)} callouts")

        # Build the index note
        content = build_definition_index(definitions, existing_stems)
        output_path = PERMANENT_NOTES_DIR / DEFINITION_INDEX_FILE

        if not self.dry_run:
            output_path.write_text(content, encoding="utf-8")
            print(f"  Wrote: {DEFINITION_INDEX_FILE} ({len(content):,} chars)")
        else:
            print(f"  Would write: {DEFINITION_INDEX_FILE} ({len(content):,} chars)")
        self.report.dedicated_notes_written.append(DEFINITION_INDEX_FILE)

        # Ensure permanent notes for each definition
        if not skip_perm_notes:
            print(f"\n  Ensuring permanent notes for definitions...")
            created, already, errs = ensure_definition_permanent_notes(
                definitions, existing_stems, PERMANENT_NOTES_DIR, self.dry_run
            )
            self.report.definition_notes_created = created
            self.report.definition_notes_already_exist = already
            self.report.errors.extend(errs)
            verb = "Would create" if self.dry_run else "Created"
            print(f"  {verb} {created} new permanent notes")
            print(f"  Already exist: {already}")
            if errs:
                print(f"  Errors: {len(errs)}")

    def _build_references(self, entries: list[CalloutEntry]):
        """Build the Reference Index."""
        print(f"\n  {'─' * 60}")
        print(f"  Building: Master Reference Index")
        print(f"  {'─' * 60}")

        content = build_reference_index(entries)
        output_path = PERMANENT_NOTES_DIR / REFERENCE_INDEX_FILE

        if not self.dry_run:
            output_path.write_text(content, encoding="utf-8")
            print(f"  Wrote: {REFERENCE_INDEX_FILE} ({len(content):,} chars)")
        else:
            print(f"  Would write: {REFERENCE_INDEX_FILE} ({len(content):,} chars)")
        self.report.dedicated_notes_written.append(REFERENCE_INDEX_FILE)

    def _build_connections(self, entries: list[CalloutEntry], existing_stems: set[str]):
        """Build the PKB Connections Index."""
        print(f"\n  {'─' * 60}")
        print(f"  Building: Master PKB Connections Index")
        print(f"  {'─' * 60}")

        content = build_connections_index(entries, existing_stems)
        output_path = PERMANENT_NOTES_DIR / CONNECTIONS_INDEX_FILE

        if not self.dry_run:
            output_path.write_text(content, encoding="utf-8")
            print(f"  Wrote: {CONNECTIONS_INDEX_FILE} ({len(content):,} chars)")
        else:
            print(f"  Would write: {CONNECTIONS_INDEX_FILE} ({len(content):,} chars)")
        self.report.dedicated_notes_written.append(CONNECTIONS_INDEX_FILE)

    def _build_expansions(self, entries: list[CalloutEntry], existing_stems: set[str]):
        """Build the Expansion Topics Index."""
        print(f"\n  {'─' * 60}")
        print(f"  Building: Master Expansion Topics Index")
        print(f"  {'─' * 60}")

        content = build_expansion_index(entries, existing_stems)
        output_path = PERMANENT_NOTES_DIR / EXPANSION_INDEX_FILE

        if not self.dry_run:
            output_path.write_text(content, encoding="utf-8")
            print(f"  Wrote: {EXPANSION_INDEX_FILE} ({len(content):,} chars)")
        else:
            print(f"  Would write: {EXPANSION_INDEX_FILE} ({len(content):,} chars)")
        self.report.dedicated_notes_written.append(EXPANSION_INDEX_FILE)

    def _print_summary(self):
        """Print final summary."""
        mode = "DRY RUN" if self.dry_run else "COMPLETE"
        print(f"\n{'=' * 72}")
        print(f"  DEDICATED NOTES BUILDER — {mode}")
        print(f"{'=' * 72}")
        print(f"  Callouts collected:")
        print(f"    Definitions:  {self.report.definitions_collected}")
        print(f"    References:   {self.report.references_collected}")
        print(f"    Connections:  {self.report.connections_collected}")
        print(f"    Expansions:   {self.report.expansions_collected}")
        print(f"  Dedicated notes {'would be' if self.dry_run else ''} written:")
        for n in self.report.dedicated_notes_written:
            print(f"    - {n}")
        if self.report.definition_notes_created > 0:
            verb = "would be created" if self.dry_run else "created"
            print(f"  Definition permanent notes {verb}: {self.report.definition_notes_created}")
        if self.report.definition_notes_already_exist > 0:
            print(f"  Definition notes already exist: {self.report.definition_notes_already_exist}")
        if self.report.errors:
            print(f"  Errors: {len(self.report.errors)}")
            for err in self.report.errors[:10]:
                print(f"    - {err}")
        print()


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Build dedicated aggregate index notes from extraction data"
    )
    parser.add_argument(
        "--execute", action="store_true",
        help="Apply changes (default: dry run)"
    )
    parser.add_argument(
        "--only", choices=["defs", "refs", "conns", "expns"],
        help="Only build one type of dedicated note"
    )
    parser.add_argument(
        "--skip-perm-notes", action="store_true",
        help="Skip creating permanent notes for definitions"
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Show callout statistics and exit"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Detailed output"
    )

    args = parser.parse_args()

    if args.stats:
        json_files = find_all_json_files(EXTRACTOR_OUTPUT_ROOT)
        print(f"JSON files found: {len(json_files)}")
        callouts = scan_all_callouts(json_files)
        print(f"\nCallout counts for dedicated notes:")
        print(f"  Definitions:  {len(callouts['definitions'])}")
        print(f"  References:   {len(callouts['references'])}")
        print(f"  Connections:  {len(callouts['connections'])}")
        print(f"  Expansions:   {len(callouts['expansions'])}")
        return

    builder = DedicatedNotesBuilder(
        dry_run=not args.execute,
        verbose=args.verbose,
    )
    builder.run(
        only=args.only,
        skip_perm_notes=args.skip_perm_notes,
    )


if __name__ == "__main__":
    main()
