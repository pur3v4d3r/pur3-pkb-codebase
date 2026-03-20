"""
report_parser.py — Reads extracted JSON files and identifies permanent note candidates
═══════════════════════════════════════════════════════════════════════════════
Each JSON file (produced by pkb_extractor.py v1.1.0) contains structured
extraction data from one report in the PKM/PKB Framework series.

This module:
  1. Loads and validates JSON structure
  2. Extracts note-worthy callouts (definitions, original-syntheses)
  3. Parses callout titles to extract concept names and domains
  4. Gathers supporting content (evidence, insights, connections)
  5. Extracts relationship data (wiki-links, expansion topics)

REQUIRES: Python 3.10+ (stdlib only — no external packages)
"""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from config import (
    NOTE_GENERATING_CALLOUTS, EVIDENCE_CALLOUTS, INSIGHT_CALLOUTS,
    CONNECTION_CALLOUTS, PRACTICE_CALLOUTS, EXPANSION_CALLOUTS,
    WARNING_CALLOUTS, REFLECTION_CALLOUTS, DOMAIN_MAP, VALID_DOMAINS,
    MAX_EVIDENCE_PER_NOTE, MAX_INSIGHTS_PER_NOTE, MAX_CONNECTIONS_PER_NOTE,
    MAX_PRACTICES_PER_NOTE, MAX_WARNINGS_PER_NOTE, MAX_EXPANSION_TOPICS,
    MAX_REFLECTIONS_PER_NOTE,
)


# ══════════════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class ReportMetadata:
    """Metadata extracted from a report's JSON frontmatter."""
    doc_id: str = ""
    source_file: str = ""
    primary_domain: str = ""
    secondary_domains: list[str] = field(default_factory=list)
    analytical_focus: str = ""
    series_position: str = ""
    builds_on: list[str] = field(default_factory=list)
    feeds_into: list[str] = field(default_factory=list)
    confidence: str = "medium"
    knowledge_level: str = "intermediate"
    tags: list[str] = field(default_factory=list)
    related_concepts: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)


@dataclass
class NoteCandidate:
    """A single permanent note to be generated from a report callout."""
    concept_name: str
    callout_type: str  # 'definition' or 'original-synthesis'
    domain: str = "other"
    attribution: str = ""
    definition_body: str = ""
    source_report: str = ""
    line_number: int = 0
    report_metadata: Optional[ReportMetadata] = None
    # Supporting content gathered from the same report
    evidence: list[str] = field(default_factory=list)
    insights: list[str] = field(default_factory=list)
    connections: list[str] = field(default_factory=list)
    practices: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    expansion_topics: list[dict] = field(default_factory=list)
    wiki_links: list[str] = field(default_factory=list)
    reflections: list[str] = field(default_factory=list)


# ══════════════════════════════════════════════════════════════════════════════
# JSON LOADING
# ══════════════════════════════════════════════════════════════════════════════

def load_json(filepath: Path) -> dict:
    """Load and return parsed JSON from an extracted report file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# ══════════════════════════════════════════════════════════════════════════════
# METADATA EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def extract_report_metadata(data: dict) -> ReportMetadata:
    """Extract report-level metadata from the JSON structure."""
    fm = data.get("document_metadata", {}).get("frontmatter", {})
    ext = data.get("extraction_metadata", {})

    builds_on = [_strip_wikilink(b) for b in fm.get("builds-on", []) if b]
    feeds_into = [_strip_wikilink(f) for f in fm.get("feeds-into", []) if f]
    related = [_strip_wikilink(r) for r in fm.get("related-concepts", []) if r]

    aliases_raw = fm.get("aliases", [])
    if isinstance(aliases_raw, list):
        aliases = [_strip_wikilink(a) for a in aliases_raw if a]
    else:
        aliases = [str(aliases_raw)] if aliases_raw else []

    return ReportMetadata(
        doc_id=fm.get("doc_id", ""),
        source_file=ext.get("source_file", ""),
        primary_domain=fm.get("primary_domain", ""),
        secondary_domains=fm.get("secondary_domains", []),
        analytical_focus=fm.get("analytical-focus", ""),
        series_position=fm.get("framework-series-position", ""),
        builds_on=builds_on,
        feeds_into=feeds_into,
        confidence=fm.get("confidence", "medium"),
        knowledge_level=fm.get("knowledge_level", "intermediate"),
        tags=fm.get("tags", []),
        related_concepts=related,
        aliases=aliases,
    )


# ══════════════════════════════════════════════════════════════════════════════
# TITLE PARSING
# ══════════════════════════════════════════════════════════════════════════════

def parse_definition_title(raw_title: str) -> tuple[str, str, str]:
    """
    Parse a definition callout title into (concept_name, domain_slug, attribution).

    The JSON extractor captures titles in formats like:
      "Schema** (Cognitive Psychology — Bartlett, 1932; Rumelhart, 1975)"
      "Cognitive Alignment Principle** (Novel synthesis — this report, 2026)"
      "Basic-Level Category** (Cognitive Psychology — Rosch & Mervis, 1975)"

    The leading ** is stripped by the extractor when splitting on "> [!definition] **".
    The trailing ** remains attached to the concept name.

    Returns:
      (concept_name, domain_slug, attribution_string)
    """
    title = raw_title.strip()

    # Remove leading ** if present (sometimes the extractor leaves both)
    title = re.sub(r'^\*\*\s*', '', title)

    # Split on ** to separate concept name from parenthetical
    if '**' in title:
        parts = title.split('**', 1)
        concept_name = parts[0].strip()
        rest = parts[1].strip()
    else:
        # No ** — try splitting on first opening parenthesis
        paren_match = re.match(r'^([^(]+)\((.+)\)\s*$', title)
        if paren_match:
            concept_name = paren_match.group(1).strip()
            rest = f"({paren_match.group(2)})"
        else:
            # Plain title with no domain/attribution
            concept_name = title
            rest = ""

    # Parse domain and attribution from parenthetical
    domain = "other"
    attribution = ""

    paren_match = re.search(r'\(([^)]+)\)', rest)
    if paren_match:
        paren_content = paren_match.group(1)
        # Try splitting on em-dash or en-dash
        if '—' in paren_content:
            domain_raw, attribution = paren_content.split('—', 1)
        elif '–' in paren_content:
            domain_raw, attribution = paren_content.split('–', 1)
        elif ' - ' in paren_content:
            domain_raw, attribution = paren_content.split(' - ', 1)
        else:
            domain_raw = paren_content
            attribution = ""

        domain_raw = domain_raw.strip().lower()
        attribution = attribution.strip()

        # Handle slash-separated multi-domain strings like
        # "Educational Philosophy/Cognitive Psychology"
        domain_parts = [d.strip() for d in domain_raw.split('/') if d.strip()]

        domain = "other"
        for dpart in domain_parts:
            if dpart in VALID_DOMAINS:
                domain = dpart
                break
            mapped = DOMAIN_MAP.get(dpart, None)
            if mapped and mapped in VALID_DOMAINS:
                domain = mapped
                break

    return concept_name, domain, attribution


def parse_synthesis_title(raw_title: str, body: str = "") -> str:
    """
    Parse an original-synthesis callout title to extract the concept name.
    Synthesis titles are typically plain text, e.g. "The Schema-KOS Structural Parallel".
    When the title is "Untitled", attempts to extract the name from the body
    (e.g. "**The Cognitive Partnership Model**: ...").
    """
    title = raw_title.strip()
    title = re.sub(r'^\*\*\s*', '', title)
    title = re.sub(r'\*\*\s*$', '', title)

    # Fallback: extract bold concept name from body when title is empty/Untitled
    if title.lower() in ("untitled", "") and body:
        bold_match = re.match(r'\*\*([^*]+)\*\*', body.strip())
        if bold_match:
            title = bold_match.group(1).strip().rstrip(':')

    return title


def parse_framework_profile_title(raw_title: str) -> tuple[str, str]:
    """
    Parse a framework-profile callout title into (concept_name, attribution).

    Titles typically follow one of these formats:
      "**Framework: Self-Determination Theory (Deci & Ryan, 1985–2017)**"
      "Self-Determination Theory — Edward Deci & Richard Ryan (1985–2017)"
      "Self-Determination Theory"

    The em-dash (—) separates framework name from developer name.

    Returns:
      (concept_name, attribution_string)
    """
    title = raw_title.strip()
    # Strip ** markers
    title = re.sub(r'^\*\*\s*', '', title)
    title = re.sub(r'\*\*\s*$', '', title)

    # Strip "Framework: " prefix if present
    title = re.sub(r'^Framework:\s*', '', title, flags=re.IGNORECASE)

    # Extract year/attribution from trailing parenthetical
    year_info = ""
    paren_match = re.search(r'\(([^)]+)\)\s*$', title)
    if paren_match:
        year_info = paren_match.group(1).strip()
        title = title[:paren_match.start()].strip()

    # Split on em-dash to separate framework name from developer name
    developer = ""
    if " — " in title:
        parts = title.split(" — ", 1)
        title = parts[0].strip()
        developer = parts[1].strip()

    # Build attribution: "Developer (Years)" or just "Developer" or just "(Years)"
    if developer and year_info:
        attribution = f"{developer} ({year_info})"
    elif developer:
        attribution = developer
    else:
        attribution = year_info

    return title, attribution


# ══════════════════════════════════════════════════════════════════════════════
# CANDIDATE EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def extract_note_candidates(data: dict) -> list[NoteCandidate]:
    """
    Extract all permanent note candidates from a single report's JSON data.

    Identifies definition and original-synthesis callouts as note generators,
    then gathers supporting content from other callout types to enrich each note.
    """
    metadata = extract_report_metadata(data)
    callouts = data.get("extracted_items", {}).get("callouts", [])
    wiki_links_data = data.get("extracted_items", {}).get("wiki_links", [])

    # Collect unique wiki-link targets from this report
    all_wiki_links = sorted({
        wl.get("target", "")
        for wl in wiki_links_data
        if wl.get("target")
    })

    # ── Gather supporting content by callout type ─────────────────────────
    evidence_items = []
    insight_items = []
    connection_items = []
    practice_items = []
    warning_items = []
    expansion_items = []
    reflection_items = []

    for callout in callouts:
        ctype = callout.get("type", "")
        body = callout.get("body", "").strip()
        title = callout.get("title", "").strip()

        if ctype in EVIDENCE_CALLOUTS and body:
            entry = f"**{title}**: {body}" if title else body
            evidence_items.append(entry)

        elif ctype in INSIGHT_CALLOUTS and body:
            entry = f"**{title}**: {body}" if title else body
            insight_items.append(entry)

        elif ctype in CONNECTION_CALLOUTS and body:
            connection_items.append(body)

        elif ctype in PRACTICE_CALLOUTS and body:
            entry = f"**{title}**: {body}" if title else body
            practice_items.append(entry)

        elif ctype in WARNING_CALLOUTS and body:
            warning_items.append(body)

        elif ctype in EXPANSION_CALLOUTS:
            topic_link = _strip_wikilink(title) if title else ""
            if topic_link:
                expansion_items.append({
                    "topic": topic_link,
                    "description": body[:200].replace('\n', ' ') if body else "",
                })

        elif ctype in REFLECTION_CALLOUTS and body:
            entry = f"**{title}**: {body}" if title else body
            reflection_items.append(entry)

    # ── Extract note-generating callouts ──────────────────────────────────
    candidates = []

    for callout in callouts:
        ctype = callout.get("type", "")
        if ctype not in NOTE_GENERATING_CALLOUTS:
            continue

        title = callout.get("title", "").strip()
        body = callout.get("body", "").strip()
        line_num = callout.get("line_number", 0)

        if not title or not body:
            continue

        if ctype == "definition":
            concept_name, domain, attribution = parse_definition_title(title)
            # Fallback: use report's primary_domain when title lacks domain info
            if domain == "other":
                pd = metadata.primary_domain.lower()
                if pd in VALID_DOMAINS:
                    domain = pd
                elif pd in DOMAIN_MAP and DOMAIN_MAP[pd] in VALID_DOMAINS:
                    domain = DOMAIN_MAP[pd]
        elif ctype == "original-synthesis":
            concept_name = parse_synthesis_title(title, body)
            # Derive domain from report primary_domain
            pd = metadata.primary_domain.lower()
            if pd in VALID_DOMAINS:
                domain = pd
            else:
                domain = DOMAIN_MAP.get(pd, "other")
            attribution = "Novel synthesis — this report series"
        elif ctype == "framework-profile":
            concept_name, attribution = parse_framework_profile_title(title)
            # Derive domain from report primary_domain
            pd = metadata.primary_domain.lower()
            if pd in VALID_DOMAINS:
                domain = pd
            else:
                domain = DOMAIN_MAP.get(pd, "other")
            if not attribution:
                attribution = "Framework profile — this report series"
        else:
            continue

        if not concept_name:
            continue

        candidate = NoteCandidate(
            concept_name=concept_name,
            callout_type=ctype,
            domain=domain,
            attribution=attribution,
            definition_body=body,
            source_report=metadata.source_file,
            line_number=line_num,
            report_metadata=metadata,
            evidence=evidence_items[:MAX_EVIDENCE_PER_NOTE],
            insights=insight_items[:MAX_INSIGHTS_PER_NOTE],
            connections=connection_items[:MAX_CONNECTIONS_PER_NOTE],
            practices=practice_items[:MAX_PRACTICES_PER_NOTE],
            warnings=warning_items[:MAX_WARNINGS_PER_NOTE],
            expansion_topics=expansion_items[:MAX_EXPANSION_TOPICS],
            wiki_links=all_wiki_links,
            reflections=reflection_items[:MAX_REFLECTIONS_PER_NOTE],
        )
        candidates.append(candidate)

    return candidates


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def _strip_wikilink(text: str) -> str:
    """
    Remove [[]] wikilink syntax, returning the inner text.
    Handles: [[Target]], [[Target|Display]], [[Target#Heading]]
    """
    text = text.strip()
    # Full wikilink pattern
    match = re.match(r'^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$', text)
    if match:
        return match.group(1).strip()
    # Partial patterns (opening/closing brackets only)
    text = re.sub(r'^\[\[', '', text)
    text = re.sub(r'\]\]$', '', text)
    # Strip any remaining alias after |
    if '|' in text:
        text = text.split('|')[0]
    return text.strip()
