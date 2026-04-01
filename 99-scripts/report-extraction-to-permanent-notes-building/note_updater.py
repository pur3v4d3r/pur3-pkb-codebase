"""
note_updater.py  -- Merge New Content Into Existing Permanent Notes
===============================================================================
The core missing capability: takes matched (NoteCandidate -> existing note)
pairs and merges new evidence, insights, wiki-links, source reports, and
connections into the existing note without duplicating existing content.

REQUIRES: Python 3.10+
USAGE:
    from note_updater import NoteUpdater

    updater = NoteUpdater(dry_run=True)
    results = updater.update_matched(match_report.matched)
"""

from __future__ import annotations

import re
import datetime
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional

from config import (
    MAX_EVIDENCE_PER_NOTE,
    MAX_INSIGHTS_PER_NOTE,
    MAX_CONNECTIONS_PER_NOTE,
    MAX_PRACTICES_PER_NOTE,
    MAX_WARNINGS_PER_NOTE,
    MAX_WIKI_LINKS_DISPLAY,
    MAX_FLASHCARDS_PER_NOTE,
    MAX_PERSONS_PER_NOTE,
    MAX_TENSIONS_PER_NOTE,
    MAX_OPEN_QUESTIONS_PER_NOTE,
    MAX_PROTOCOLS_PER_NOTE,
    MAX_DIAGRAMS_PER_NOTE,
    MAX_CITATIONS_PER_NOTE,
    MAX_METHODOLOGY_PER_NOTE,
)
from report_parser import NoteCandidate
from note_matcher import MatchResult, NoteIndex, _normalize


# ==============================================================================
# DATA CLASSES
# ==============================================================================

@dataclass
class UpdateAction:
    """Describes what was changed in a single note update."""
    note_path: Path
    concept_name: str
    source_reports_added: list[str] = field(default_factory=list)
    evidence_added: int = 0
    insights_added: int = 0
    connections_added: int = 0
    practices_added: int = 0
    warnings_added: int = 0
    reflections_added: int = 0
    wiki_links_added: int = 0
    see_also_added: int = 0
    # Enhanced content (v2.1)
    flashcards_added: int = 0
    persons_added: int = 0
    tensions_added: int = 0
    open_questions_added: int = 0
    protocols_added: int = 0
    diagrams_added: int = 0
    citations_added: int = 0
    methodology_added: int = 0
    timestamp_updated: bool = False
    errors: list[str] = field(default_factory=list)

    @property
    def total_changes(self) -> int:
        return (
            len(self.source_reports_added)
            + self.evidence_added
            + self.insights_added
            + self.connections_added
            + self.practices_added
            + self.warnings_added
            + self.reflections_added
            + self.wiki_links_added
            + self.see_also_added
            + self.flashcards_added
            + self.persons_added
            + self.tensions_added
            + self.open_questions_added
            + self.protocols_added
            + self.diagrams_added
            + self.citations_added
            + self.methodology_added
        )

    @property
    def was_modified(self) -> bool:
        return self.total_changes > 0


@dataclass
class UpdateReport:
    """Aggregated results from updating multiple notes."""
    actions: list[UpdateAction] = field(default_factory=list)
    dry_run: bool = True

    @property
    def modified_count(self) -> int:
        return sum(1 for a in self.actions if a.was_modified)

    @property
    def unchanged_count(self) -> int:
        return sum(1 for a in self.actions if not a.was_modified)

    @property
    def error_count(self) -> int:
        return sum(1 for a in self.actions if a.errors)


# ==============================================================================
# CONTENT PARSING
# ==============================================================================

_FRONTMATTER_RE = re.compile(r'^(---\s*\n)(.*?)(\n---)', re.DOTALL)
_WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]')

# Patterns that indicate a garbage / non-concept wiki-link target
_GARBAGE_LINK_PATTERNS = [
    re.compile(r'<%'),                     # Templater syntax
    re.compile(r'%>'),                     # Templater syntax
    re.compile(r'tp\.'),                   # Templater function references
    re.compile(r'^\*\*.*\*\*$'),           # Bold-wrapped text (not a concept)
    re.compile(r'^__.*__$'),               # Underline-wrapped text
    re.compile(r'^\d{1,4}$'),             # Pure numbers / years
    re.compile(r'^Note-?\d+$', re.I),     # Template placeholders like Note-1
    re.compile(r'^Note Title', re.I),     # Template placeholder text
    re.compile(r'priority:|aliases:|topic:', re.I),  # YAML fragment leak
    re.compile(r'^\s*$'),                 # Empty / whitespace-only
    re.compile(r'^[^a-zA-Z]*$'),          # No alphabetic characters at all
]


def _is_garbage_link(target: str) -> bool:
    """Return True if the wiki-link target is not a valid concept name."""
    if not target or len(target.strip()) < 2:
        return True
    return any(p.search(target) for p in _GARBAGE_LINK_PATTERNS)


def _read_note(filepath: Path) -> str:
    """Read a note file, returning its full text."""
    return filepath.read_text(encoding="utf-8", errors="replace")


def _split_frontmatter_body(text: str) -> tuple[str, str, str]:
    """
    Split note into (frontmatter_open, yaml_content, body_after_closing_dashes).

    Returns ('---\\n', yaml_text, rest_including_closing_dashes_and_body).
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return "", "", text
    return m.group(1), m.group(2), text[m.end():]


def _extract_existing_callouts(body: str, callout_type: str) -> list[str]:
    """
    Extract existing callout bodies of a specific type from note body.

    Returns list of body texts (for deduplication comparison).
    """
    pattern = re.compile(
        rf'> \[!{re.escape(callout_type)}\].*?\n((?:>.*\n)*)',
        re.MULTILINE,
    )
    results = []
    for m in pattern.finditer(body):
        body_text = m.group(1)
        # Strip leading "> " from each line
        clean = "\n".join(
            line.lstrip(">").strip() for line in body_text.split("\n")
        ).strip()
        results.append(clean)
    return results


def _extract_existing_wikilinks(body: str) -> set[str]:
    """Extract all wiki-link targets from body text."""
    return {m.group(1).strip().lower() for m in _WIKILINK_RE.finditer(body)}


def _extract_source_reports(yaml_text: str) -> list[str]:
    """Extract source-reports list from frontmatter YAML text."""
    reports: list[str] = []
    in_source_reports = False
    for line in yaml_text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("source-reports:"):
            in_source_reports = True
            # Check inline value
            after = stripped.replace("source-reports:", "").strip()
            if after and not after.startswith("["):
                continue
            if after.startswith("["):
                inner = after.strip("[]")
                reports.extend(
                    v.strip().strip('"').strip("'")
                    for v in inner.split(",") if v.strip()
                )
                in_source_reports = False
            continue
        if in_source_reports:
            if stripped.startswith("- "):
                val = stripped[2:].strip().strip('"').strip("'")
                reports.append(val)
            elif stripped and not stripped.startswith("#") and not stripped.startswith("="):
                in_source_reports = False
    return reports


def _extract_see_also(yaml_text: str) -> list[str]:
    """Extract see-also list from frontmatter YAML text."""
    see_also: list[str] = []
    in_see_also = False
    for line in yaml_text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("see-also:"):
            in_see_also = True
            continue
        if in_see_also:
            if stripped.startswith("- "):
                val = stripped[2:].strip().strip('"').strip("'")
                see_also.append(val)
            elif stripped and not stripped.startswith("#") and not stripped.startswith("="):
                in_see_also = False
    return see_also


# ==============================================================================
# CONTENT DEDUPLICATION
# ==============================================================================

def _is_duplicate_callout(new_body: str, existing_bodies: list[str]) -> bool:
    """
    Check if new callout body is a duplicate of existing content.

    Uses normalized text comparison  -- strips formatting, lowers, and checks
    for significant overlap. Enhanced with SequenceMatcher for near-duplicate
    (paraphrased) detection.
    """
    new_norm = _normalize_for_dedup(new_body)
    if not new_norm or len(new_norm) < 20:
        return True  # Skip trivially short content

    for existing in existing_bodies:
        existing_norm = _normalize_for_dedup(existing)
        # Check exact match
        if new_norm == existing_norm:
            return True
        # Check high overlap (first 100 chars match)
        if len(new_norm) > 50 and len(existing_norm) > 50:
            if new_norm[:100] == existing_norm[:100]:
                return True
        # SequenceMatcher fuzzy check for paraphrased duplicates
        if len(new_norm) > 30 and len(existing_norm) > 30:
            ratio = SequenceMatcher(None, new_norm[:300], existing_norm[:300]).ratio()
            if ratio >= 0.80:
                return True
    return False


def _normalize_for_dedup(text: str) -> str:
    """Normalize text for deduplication comparison."""
    text = text.lower()
    text = re.sub(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', r'\1', text)  # strip wiki-links
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # strip bold
    text = re.sub(r'\*([^*]+)\*', r'\1', text)  # strip italics
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ==============================================================================
# CONTENT INSERTION
# ==============================================================================

def _build_callout_block(callout_type: str, title: str, body: str) -> str:
    """Build a properly formatted callout block."""
    lines = [f"> [!{callout_type}] {title}"]
    for line in body.split("\n"):
        lines.append(f"> {line}")
    return "\n".join(lines)


def _find_section(body: str, heading: str) -> Optional[tuple[int, int]]:
    """
    Find the character range of a ## section in the body.

    Returns (start, end) where end is the start of the next ## heading
    or end of body.
    """
    pattern = re.compile(
        rf'^## {re.escape(heading)}\s*$',
        re.MULTILINE,
    )
    m = pattern.search(body)
    if not m:
        return None

    start = m.start()
    # Find next ## heading
    next_heading = re.search(r'^## ', body[m.end():], re.MULTILINE)
    if next_heading:
        end = m.end() + next_heading.start()
    else:
        end = len(body)

    return (start, end)


def _insert_before_section_end(
    body: str,
    section_heading: str,
    new_content: str,
) -> str:
    """
    Insert new content at the end of a named section (before the next section).

    If the section doesn't exist, creates it before Connections & Context.
    """
    section = _find_section(body, section_heading)

    if section:
        start, end = section
        # Find the last non-blank line in the section
        section_text = body[start:end]
        insert_pos = end
        # Insert before trailing blank lines
        trailing_blanks = len(section_text) - len(section_text.rstrip("\n"))
        if trailing_blanks > 0:
            insert_pos = end - trailing_blanks
        return body[:insert_pos] + "\n\n" + new_content + "\n" + body[insert_pos:]
    else:
        # Create the section  -- insert before "## Connections" or at end
        conn_section = _find_section(body, "Connections & Context")
        if conn_section:
            insert_pos = conn_section[0]
        else:
            insert_pos = len(body)
        new_section = f"\n## {section_heading}\n\n{new_content}\n\n"
        return body[:insert_pos] + new_section + body[insert_pos:]


def _pipe_link(name: str) -> str:
    """Build a [[Filename-Stem|Display Name]] wiki-link."""
    stem = name.replace(" ", "-")
    return f"[[{stem}|{name}]]"


# ==============================================================================
# UPDATER
# ==============================================================================

class NoteUpdater:
    """
    Updates existing permanent notes with new content from matched candidates.

    Merges:
    - Source reports -> frontmatter source-reports list
    - Evidence callouts -> Core Explanation section
    - Insight callouts -> Core Explanation section
    - Practice callouts -> Practical Implications section
    - Warning callouts -> Practical Implications section
    - Wiki-links -> Connections & Context section
    - See-also links -> frontmatter see-also list
    - Updated timestamp
    """

    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run
        self.today = datetime.date.today().isoformat()

    def update_note(
        self,
        note: NoteIndex,
        candidates: list[NoteCandidate],
    ) -> UpdateAction:
        """
        Update a single existing note with content from one or more candidates.

        Multiple candidates for the same concept (from different reports)
        are merged together.
        """
        action = UpdateAction(
            note_path=note.filepath,
            concept_name=note.title or note.stem,
        )

        try:
            text = _read_note(note.filepath)
        except Exception as e:
            action.errors.append(f"Failed to read {note.filepath.name}: {e}")
            return action

        fm_open, yaml_text, body_and_close = _split_frontmatter_body(text)
        if not fm_open:
            action.errors.append(f"No frontmatter found in {note.filepath.name}")
            return action

        # Split closing --- from body
        if body_and_close.startswith("\n"):
            body = body_and_close
        else:
            body = body_and_close

        # -- 1. Update source-reports in frontmatter -----------------------
        existing_reports = _extract_source_reports(yaml_text)
        existing_reports_lower = {r.lower() for r in existing_reports}

        new_reports = []
        for c in candidates:
            report_name = c.source_report
            if report_name and report_name.lower() not in existing_reports_lower:
                new_reports.append(report_name)
                existing_reports_lower.add(report_name.lower())

        if new_reports:
            yaml_text = self._add_source_reports(yaml_text, new_reports)
            action.source_reports_added = new_reports

        # -- 1b. Deduplicate source-reports (handle .md variants) ----------
        yaml_text = self._deduplicate_source_reports(yaml_text)

        # -- 2. Update see-also in frontmatter -----------------------------
        existing_see_also = _extract_see_also(yaml_text)
        existing_see_also_lower = {s.lower() for s in existing_see_also}
        existing_body_links = _extract_existing_wikilinks(body)

        new_see_also = []
        for c in candidates:
            for wl in c.wiki_links:
                if _is_garbage_link(wl):
                    continue
                wl_norm = _normalize(wl)
                wl_stem = wl_norm.replace(" ", "-")
                if (
                    wl_norm not in existing_see_also_lower
                    and wl_stem not in existing_see_also_lower
                    and wl_norm != _normalize(note.title or note.stem)
                ):
                    link_str = _pipe_link(wl)
                    new_see_also.append(link_str)
                    existing_see_also_lower.add(wl_norm)

        if new_see_also:
            yaml_text = self._add_see_also(yaml_text, new_see_also[:8])
            action.see_also_added = min(len(new_see_also), 8)

        # -- 2b. Deduplicate existing see-also entries ----------------------
        yaml_text = self._deduplicate_see_also(yaml_text)

        # -- 3. Update timestamp -------------------------------------------
        yaml_text = self._update_timestamp(yaml_text)
        action.timestamp_updated = True

        # -- 4. Add evidence callouts --------------------------------------
        existing_evidence = _extract_existing_callouts(body, "evidence")
        for c in candidates:
            for ev in c.evidence:
                if not _is_duplicate_callout(ev, existing_evidence):
                    callout = _build_callout_block(
                        "evidence",
                        f"Supporting Evidence *(from {c.source_report})*",
                        ev,
                    )
                    body = _insert_before_section_end(body, "Core Explanation", callout)
                    existing_evidence.append(ev)
                    action.evidence_added += 1

        # -- 5. Add insight callouts ---------------------------------------
        existing_insights = _extract_existing_callouts(body, "analytical-insight")
        for c in candidates:
            for insight in c.insights:
                if not _is_duplicate_callout(insight, existing_insights):
                    callout = _build_callout_block(
                        "analytical-insight",
                        f"Key Insight *(from {c.source_report})*",
                        insight,
                    )
                    body = _insert_before_section_end(body, "Core Explanation", callout)
                    existing_insights.append(insight)
                    action.insights_added += 1

        # -- 6. Add practice callouts --------------------------------------
        existing_practices = _extract_existing_callouts(body, "example")
        for c in candidates:
            for practice in c.practices:
                if not _is_duplicate_callout(practice, existing_practices):
                    callout = _build_callout_block(
                        "example",
                        f"**Application** *(from {c.source_report})*",
                        practice,
                    )
                    body = _insert_before_section_end(
                        body, "Practical Implications", callout
                    )
                    existing_practices.append(practice)
                    action.practices_added += 1

        # -- 7. Add warning callouts ---------------------------------------
        existing_warnings = _extract_existing_callouts(body, "warning")
        for c in candidates:
            for warning in c.warnings:
                if not _is_duplicate_callout(warning, existing_warnings):
                    callout = _build_callout_block(
                        "warning",
                        f"**Key Distinction** *(from {c.source_report})*",
                        warning,
                    )
                    body = _insert_before_section_end(
                        body, "Practical Implications", callout
                    )
                    existing_warnings.append(warning)
                    action.warnings_added += 1

        # -- 7b. Add reflection callouts -----------------------------------
        existing_reflections = _extract_existing_callouts(body, "reflection")
        for c in candidates:
            for reflection in getattr(c, 'reflections', []):
                if not _is_duplicate_callout(reflection, existing_reflections):
                    callout = _build_callout_block(
                        "reflection",
                        f"**Reflect** *(from {c.source_report})*",
                        reflection,
                    )
                    body = _insert_before_section_end(
                        body, "Reflection Prompts", callout
                    )
                    existing_reflections.append(reflection)
                    action.reflections_added += 1

        # -- 7c. Add flashcard callouts (v2.1) -----------------------------
        existing_flashcards = _extract_existing_callouts(body, "flashcard")
        for c in candidates:
            for card in getattr(c, 'flashcards', []):
                q = card.get("question", card.get("title", ""))
                a = card.get("answer", card.get("body", ""))
                card_body = f"**Q:** {q}\n**A:** {a}"
                if card.get("difficulty"):
                    card_body += f"\n*Difficulty: {card['difficulty']}*"
                if not _is_duplicate_callout(card_body, existing_flashcards):
                    callout = _build_callout_block(
                        "flashcard",
                        f"**Spaced Repetition** *(from {c.source_report})*",
                        card_body,
                    )
                    body = _insert_before_section_end(
                        body, "Spaced Repetition Seeds", callout
                    )
                    existing_flashcards.append(card_body)
                    action.flashcards_added += 1

        # -- 7d. Add person callouts (v2.1) --------------------------------
        existing_persons = _extract_existing_callouts(body, "person")
        for c in candidates:
            for person in getattr(c, 'persons', []):
                person_body = person.get("body", "")
                person_title = person.get("title", "Key Figure")
                if not _is_duplicate_callout(person_body, existing_persons):
                    callout = _build_callout_block(
                        "person",
                        f"**{person_title}** *(from {c.source_report})*",
                        person_body,
                    )
                    body = _insert_before_section_end(
                        body, "Key Figures & Intellectual Lineage", callout
                    )
                    existing_persons.append(person_body)
                    action.persons_added += 1

        # -- 7e. Add tension callouts (v2.1) -------------------------------
        existing_tensions = _extract_existing_callouts(body, "tension")
        for c in candidates:
            for tension in getattr(c, 'tensions', []):
                tension_body = tension.get("body", "")
                tension_title = tension.get("title", "Unresolved Tension")
                if not _is_duplicate_callout(tension_body, existing_tensions):
                    callout = _build_callout_block(
                        "tension",
                        f"**{tension_title}** *(from {c.source_report})*",
                        tension_body,
                    )
                    body = _insert_before_section_end(
                        body, "Conceptual Tensions", callout
                    )
                    existing_tensions.append(tension_body)
                    action.tensions_added += 1

        # -- 7f. Add open question callouts (v2.1) -------------------------
        existing_oqs = _extract_existing_callouts(body, "open-question")
        for c in candidates:
            for oq in getattr(c, 'open_questions', []):
                oq_body = oq.get("body", "")
                oq_title = oq.get("title", "")
                if not _is_duplicate_callout(oq_body, existing_oqs):
                    callout = _build_callout_block(
                        "open-question",
                        f"**{oq_title}** *(from {c.source_report})*" if oq_title else f"*(from {c.source_report})*",
                        oq_body,
                    )
                    body = _insert_before_section_end(
                        body, "Open Questions", callout
                    )
                    existing_oqs.append(oq_body)
                    action.open_questions_added += 1

        # -- 7g. Add protocol callouts (v2.1) ------------------------------
        existing_protocols = _extract_existing_callouts(body, "protocol")
        for c in candidates:
            for protocol in getattr(c, 'protocols', []):
                protocol_body = protocol.get("body", "")
                protocol_title = protocol.get("title", "Method")
                if not _is_duplicate_callout(protocol_body, existing_protocols):
                    callout = _build_callout_block(
                        "protocol",
                        f"**{protocol_title}** *(from {c.source_report})*",
                        protocol_body,
                    )
                    body = _insert_before_section_end(
                        body, "Protocols & Methods", callout
                    )
                    existing_protocols.append(protocol_body)
                    action.protocols_added += 1

        # -- 7h. Add diagram callouts (v2.1) -------------------------------
        existing_diagrams = _extract_existing_callouts(body, "diagram")
        for c in candidates:
            for diagram in getattr(c, 'diagrams', []):
                diagram_body = diagram.get("body", "")
                diagram_title = diagram.get("title", "")
                if not _is_duplicate_callout(diagram_body, existing_diagrams):
                    callout = _build_callout_block(
                        "diagram",
                        f"**{diagram_title}**" if diagram_title else "",
                        diagram_body,
                    )
                    body = _insert_before_section_end(
                        body, "Visual Representations", callout
                    )
                    existing_diagrams.append(diagram_body)
                    action.diagrams_added += 1

        # -- 7i. Add citation entries (v2.1) -------------------------------
        for c in candidates:
            for cite in getattr(c, 'citations', []):
                cite_title = cite.get("title", "")
                cite_body = cite.get("body", "")
                cite_text = f"**{cite_title}**: {cite_body}" if cite_title else cite_body
                # Simple dedup: check if cite text already in body
                if _normalize_for_dedup(cite_text) not in _normalize_for_dedup(body):
                    body = _insert_before_section_end(
                        body, "References", f"- {cite_text}"
                    )
                    action.citations_added += 1

        # -- 7j. Add methodology callouts (v2.1) ---------------------------
        existing_methodology = _extract_existing_callouts(body, "methodology-and-sources")
        for c in candidates:
            for meth in getattr(c, 'methodology', []):
                meth_body = meth.get("body", "")
                meth_title = meth.get("title", "")
                if not _is_duplicate_callout(meth_body, existing_methodology):
                    callout = _build_callout_block(
                        "methodology-and-sources",
                        f"**{meth_title}** *(from {c.source_report})*" if meth_title else f"*(from {c.source_report})*",
                        meth_body,
                    )
                    body = _insert_before_section_end(
                        body, "Methodology Notes", callout
                    )
                    existing_methodology.append(meth_body)
                    action.methodology_added += 1

        # -- 7k. Add schema-activation callouts (v2.2) --------------------
        existing_schema = _extract_existing_callouts(body, "schema-activation")
        for c in candidates:
            for sa in getattr(c, 'schema_activations', []):
                sa_body = sa.get("body", "")
                sa_title = sa.get("title", "")
                if not _is_duplicate_callout(sa_body, existing_schema):
                    callout = _build_callout_block(
                        "schema-activation",
                        f"**{sa_title}** *(from {c.source_report})*" if sa_title else f"*(from {c.source_report})*",
                        sa_body,
                    )
                    body = _insert_before_section_end(
                        body, "Schema Activations", callout
                    )
                    existing_schema.append(sa_body)

        # -- 7l. Add active-reading callouts (v2.2) ------------------------
        existing_ar = _extract_existing_callouts(body, "active-reading")
        for c in candidates:
            for ar in getattr(c, 'active_readings', []):
                ar_body = ar.get("body", "")
                ar_title = ar.get("title", "")
                if not _is_duplicate_callout(ar_body, existing_ar):
                    callout = _build_callout_block(
                        "active-reading",
                        f"**{ar_title}** *(from {c.source_report})*" if ar_title else f"*(from {c.source_report})*",
                        ar_body,
                    )
                    body = _insert_before_section_end(
                        body, "Active Reading Prompts", callout
                    )
                    existing_ar.append(ar_body)

        # -- 7m. Add far-transfer callouts (v2.2) -------------------------
        existing_ft = _extract_existing_callouts(body, "far-transfer")
        for c in candidates:
            for ft in getattr(c, 'far_transfers', []):
                ft_body = ft.get("body", "")
                ft_title = ft.get("title", "")
                if not _is_duplicate_callout(ft_body, existing_ft):
                    callout = _build_callout_block(
                        "far-transfer",
                        f"**{ft_title}** *(from {c.source_report})*" if ft_title else f"*(from {c.source_report})*",
                        ft_body,
                    )
                    body = _insert_before_section_end(
                        body, "Far Transfer Applications", callout
                    )
                    existing_ft.append(ft_body)

        # -- 7n. Add debate callouts (v2.2) --------------------------------
        existing_debates = _extract_existing_callouts(body, "debate")
        for c in candidates:
            for debate in getattr(c, 'debates', []):
                debate_body = debate.get("body", "")
                debate_title = debate.get("title", "")
                if not _is_duplicate_callout(debate_body, existing_debates):
                    callout = _build_callout_block(
                        "debate",
                        f"**{debate_title}** *(from {c.source_report})*" if debate_title else f"*(from {c.source_report})*",
                        debate_body,
                    )
                    body = _insert_before_section_end(
                        body, "Debates", callout
                    )
                    existing_debates.append(debate_body)

        # -- 7o. Add example callouts (v2.2) -------------------------------
        existing_examples = _extract_existing_callouts(body, "example")
        for c in candidates:
            for ex in getattr(c, 'examples', []):
                ex_body = ex.get("body", "")
                ex_title = ex.get("title", "")
                if not _is_duplicate_callout(ex_body, existing_examples):
                    callout = _build_callout_block(
                        "example",
                        f"**{ex_title}** *(from {c.source_report})*" if ex_title else f"*(from {c.source_report})*",
                        ex_body,
                    )
                    body = _insert_before_section_end(
                        body, "Concrete Examples", callout
                    )
                    existing_examples.append(ex_body)

        # -- 7p. Add claude-insight callouts (v2.2) ------------------------
        existing_ci = _extract_existing_callouts(body, "claude-insight")
        for c in candidates:
            for ci in getattr(c, 'claude_insights', []):
                ci_body = ci.get("body", "")
                ci_title = ci.get("title", "")
                if not _is_duplicate_callout(ci_body, existing_ci):
                    callout = _build_callout_block(
                        "claude-insight",
                        f"**{ci_title}** *(from {c.source_report})*" if ci_title else f"*(from {c.source_report})*",
                        ci_body,
                    )
                    body = _insert_before_section_end(
                        body, "AI Insights", callout
                    )
                    existing_ci.append(ci_body)

        # -- 7q. Add section-summary callouts (v2.2) ----------------------
        existing_ss = _extract_existing_callouts(body, "section-summary")
        for c in candidates:
            for ss in getattr(c, 'section_summaries', []):
                ss_body = ss.get("body", "")
                ss_title = ss.get("title", "")
                if not _is_duplicate_callout(ss_body, existing_ss):
                    callout = _build_callout_block(
                        "section-summary",
                        f"**{ss_title}** *(from {c.source_report})*" if ss_title else f"*(from {c.source_report})*",
                        ss_body,
                    )
                    body = _insert_before_section_end(
                        body, "Section Summaries", callout
                    )
                    existing_ss.append(ss_body)

        # -- 8. Add new wiki-links to Connections section ------------------
        new_wl_for_body = []
        for c in candidates:
            for wl in c.wiki_links:
                if _is_garbage_link(wl):
                    continue
                wl_lower = wl.lower().strip()
                if (
                    wl_lower not in existing_body_links
                    and wl_lower != _normalize(note.title or note.stem)
                ):
                    new_wl_for_body.append(wl)
                    existing_body_links.add(wl_lower)

        if new_wl_for_body:
            # Build a "Related concepts" line with pipe-links
            source_label = ", ".join(
                sorted(set(c.source_report for c in candidates if c.source_report))
            )
            link_text = " * ".join(
                _pipe_link(wl) for wl in new_wl_for_body[:MAX_WIKI_LINKS_DISPLAY]
            )
            connections_block = (
                f"**Related concepts** *(from {source_label})*:\n{link_text}"
            )
            body = _insert_before_section_end(
                body, "Connections & Context", connections_block
            )
            action.wiki_links_added = min(len(new_wl_for_body), MAX_WIKI_LINKS_DISPLAY)

        # -- 9. Add cross-report connections -------------------------------
        for c in candidates:
            for conn in c.connections:
                existing_connections = _extract_existing_callouts(body, "cross-domain-connection")
                if not _is_duplicate_callout(conn, existing_connections):
                    # Extract wiki-links from connection text
                    conn_links = _WIKILINK_RE.findall(conn)
                    if conn_links:
                        conn_block = (
                            f"**Cross-report connections** *(from {c.source_report})*:\n"
                            + "\n".join(f"- {_pipe_link(cl)}" for cl in conn_links[:5])
                        )
                        body = _insert_before_section_end(
                            body, "Connections & Context", conn_block
                        )
                        action.connections_added += 1

        # -- WRITE ---------------------------------------------------------
        if action.was_modified and not self.dry_run:
            new_text = f"{fm_open}{yaml_text}{body_and_close[:3]}{body[3:] if body.startswith(body_and_close[:3]) else body}"
            # Reconstruct properly
            new_text = f"{fm_open}{yaml_text}\n---{body}"
            try:
                note.filepath.write_text(new_text, encoding="utf-8")
            except Exception as e:
                action.errors.append(f"Failed to write {note.filepath.name}: {e}")

        return action

    # -- Frontmatter helpers -----------------------------------------------

    def _add_source_reports(self, yaml_text: str, new_reports: list[str]) -> str:
        """Add new source-reports entries to frontmatter YAML."""
        new_entries = "\n".join(f'  - "{r}"' for r in new_reports)

        # Find the end of source-reports block
        lines = yaml_text.split("\n")
        result_lines = []
        in_source_reports = False
        inserted = False

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("source-reports:"):
                in_source_reports = True
                result_lines.append(line)
                continue

            if in_source_reports:
                if stripped.startswith("- "):
                    result_lines.append(line)
                    continue
                else:
                    # End of source-reports block  -- insert new entries
                    result_lines.append(new_entries)
                    in_source_reports = False
                    inserted = True

            result_lines.append(line)

        # If source-reports was the last field, append at end
        if in_source_reports and not inserted:
            result_lines.append(new_entries)

        return "\n".join(result_lines)

    def _add_see_also(self, yaml_text: str, new_links: list[str]) -> str:
        """Add new see-also entries to frontmatter YAML."""
        new_entries = "\n".join(f'  - "{link}"' for link in new_links)

        lines = yaml_text.split("\n")
        result_lines = []
        in_see_also = False
        inserted = False

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("see-also:"):
                in_see_also = True
                result_lines.append(line)
                continue

            if in_see_also:
                if stripped.startswith("- "):
                    result_lines.append(line)
                    continue
                else:
                    result_lines.append(new_entries)
                    in_see_also = False
                    inserted = True

            result_lines.append(line)

        if in_see_also and not inserted:
            result_lines.append(new_entries)

        return "\n".join(result_lines)

    def _update_timestamp(self, yaml_text: str) -> str:
        """Update the 'updated' field in frontmatter."""
        # Try updating existing 'updated:' field
        updated_re = re.compile(r'^(updated:\s*).*$', re.MULTILINE)
        if updated_re.search(yaml_text):
            return updated_re.sub(rf'\g<1>{self.today}', yaml_text)

        # If no 'updated' field, try inserting after 'created:'
        created_re = re.compile(r'^(created:\s*.*)$', re.MULTILINE)
        m = created_re.search(yaml_text)
        if m:
            insert_pos = m.end()
            return yaml_text[:insert_pos] + f"\nupdated: {self.today}" + yaml_text[insert_pos:]

        return yaml_text

    def _deduplicate_see_also(self, yaml_text: str) -> str:
        """Remove duplicate see-also entries from frontmatter YAML.

        Normalizes wiki-link stems to lowercase for comparison, keeping
        the first occurrence of each unique target.
        """
        lines = yaml_text.split("\n")
        result_lines = []
        in_see_also = False
        seen_stems: set[str] = set()

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("see-also:"):
                in_see_also = True
                result_lines.append(line)
                continue

            if in_see_also:
                if stripped.startswith("- "):
                    # Extract the wiki-link target for dedup
                    val = stripped[2:].strip().strip('"').strip("'")
                    # Extract stem from [[Stem|Display]] or [[Stem]]
                    stem_match = re.search(r'\[\[([^\]|#]+)', val)
                    stem_key = stem_match.group(1).strip().lower() if stem_match else val.lower()
                    if stem_key in seen_stems:
                        continue  # skip duplicate
                    seen_stems.add(stem_key)
                    result_lines.append(line)
                    continue
                else:
                    in_see_also = False

            result_lines.append(line)

        return "\n".join(result_lines)

    def _deduplicate_source_reports(self, yaml_text: str) -> str:
        """Remove duplicate source-reports entries (with/without .md)."""
        lines = yaml_text.split("\n")
        result_lines = []
        in_source_reports = False
        seen: set[str] = set()

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("source-reports:"):
                in_source_reports = True
                result_lines.append(line)
                continue

            if in_source_reports:
                if stripped.startswith("- "):
                    val = stripped[2:].strip().strip('"').strip("'")
                    # Normalize: strip .md suffix for comparison
                    norm = val.lower().removesuffix(".md")
                    if norm in seen:
                        continue  # skip duplicate
                    seen.add(norm)
                    result_lines.append(line)
                    continue
                else:
                    in_source_reports = False

            result_lines.append(line)

        return "\n".join(result_lines)

    # -- Batch operations --------------------------------------------------

    def update_matched(self, matched_results: list[MatchResult]) -> UpdateReport:
        """
        Update all matched notes.

        Groups candidates by target note to handle multiple candidates
        pointing to the same existing note.
        """
        report = UpdateReport(dry_run=self.dry_run)

        # Group candidates by target note path
        groups: dict[str, tuple[NoteIndex, list[NoteCandidate]]] = {}
        for result in matched_results:
            if result.matched_note is None:
                continue
            key = str(result.matched_note.filepath)
            if key not in groups:
                groups[key] = (result.matched_note, [])
            groups[key][1].append(result.candidate)

        for note, candidates in groups.values():
            action = self.update_note(note, candidates)
            report.actions.append(action)

        return report


# ==============================================================================
# CLI
# ==============================================================================

def main() -> None:
    import sys
    from scan_extractions import scan_all_batches
    from note_matcher import NoteMatcher

    dry_run = "--execute" not in sys.argv

    print("Building note index...")
    matcher = NoteMatcher()
    print(f"  Indexed {len(matcher.index)} existing permanent notes\n")

    print("Scanning extraction batches...")
    scan = scan_all_batches()
    candidates = scan.all_candidates
    print(f"  Found {len(candidates)} candidates\n")

    print("Matching candidates...")
    match_report = matcher.match_candidates(candidates)
    print(f"  Matched: {len(match_report.matched)}")
    print(f"  Unmatched: {len(match_report.unmatched)}\n")

    mode_str = "DRY RUN" if dry_run else "EXECUTING"
    print(f"Updating matched notes ({mode_str})...")
    updater = NoteUpdater(dry_run=dry_run)
    update_report = updater.update_matched(match_report.matched)

    # Summary
    print("\n" + "=" * 72)
    print(f"UPDATE REPORT ({'DRY RUN' if dry_run else 'APPLIED'})")
    print("=" * 72)
    print(f"  Notes processed:    {len(update_report.actions)}")
    print(f"  Notes modified:     {update_report.modified_count}")
    print(f"  Notes unchanged:    {update_report.unchanged_count}")
    print(f"  Errors:             {update_report.error_count}")

    # Detail modified notes
    modified = [a for a in update_report.actions if a.was_modified]
    if modified:
        print(f"\n{'-' * 72}")
        print("MODIFIED NOTES:")
        for a in modified[:30]:
            changes = []
            if a.source_reports_added:
                changes.append(f"+{len(a.source_reports_added)} reports")
            if a.evidence_added:
                changes.append(f"+{a.evidence_added} evidence")
            if a.insights_added:
                changes.append(f"+{a.insights_added} insights")
            if a.practices_added:
                changes.append(f"+{a.practices_added} practices")
            if a.wiki_links_added:
                changes.append(f"+{a.wiki_links_added} links")
            if a.see_also_added:
                changes.append(f"+{a.see_also_added} see-also")
            if a.flashcards_added:
                changes.append(f"+{a.flashcards_added} flashcards")
            if a.persons_added:
                changes.append(f"+{a.persons_added} persons")
            if a.tensions_added:
                changes.append(f"+{a.tensions_added} tensions")
            if a.open_questions_added:
                changes.append(f"+{a.open_questions_added} questions")
            if a.protocols_added:
                changes.append(f"+{a.protocols_added} protocols")
            if a.diagrams_added:
                changes.append(f"+{a.diagrams_added} diagrams")
            if a.citations_added:
                changes.append(f"+{a.citations_added} citations")
            if a.methodology_added:
                changes.append(f"+{a.methodology_added} methodology")
            change_str = ", ".join(changes)
            print(f"  {a.note_path.stem}: {change_str}")

    if dry_run:
        print(f"\n[DRY RUN  -- run with --execute to apply changes]")
    print("=" * 72)


if __name__ == "__main__":
    main()
