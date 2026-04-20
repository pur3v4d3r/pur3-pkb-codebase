"""
note_builder.py — Constructs permanent note markdown from parsed data
═══════════════════════════════════════════════════════════════════════════════
Takes NoteCandidate objects and produces complete markdown files matching
the permanent-note-template.md format used in the PKB.

Generates:
  - YAML frontmatter with all required fields
  - Markdown body with definition, explanation, implications, and connections
  - Properly formatted Obsidian callouts and wiki-links

REQUIRES: Python 3.10+ (stdlib only)
"""

import re
from datetime import date

from config import (
    VALID_DOMAINS, KNOWLEDGE_LEVEL_TO_COMPLEXITY, MAX_FILENAME_LENGTH,
    MAX_WIKI_LINKS_DISPLAY, MAX_RELATED_LINKS, MAX_SEE_ALSO_LINKS,
    MAX_REPORT_TAGS,
)
from report_parser import NoteCandidate


# ══════════════════════════════════════════════════════════════════════════════
# FILENAME GENERATION
# ══════════════════════════════════════════════════════════════════════════════

# Reject report-document filenames from becoming permanent notes.
# Source reports (foundational, focused-analysis, dialectical, etc.) are
# *literature*, not concepts; they belong in literature notes, not the
# permanent notes folder.
_REPORT_FILENAME_PATTERN = re.compile(
    r'-(foundational-report|focused-analysis|dialectical(-re-examination)?|socratic(-dialogue)?'
    r'|comparative(-synthesis)?|first-principles|generative-learning|pkb-focused-analysis)'
    r'-\d{4}-\d{2}-\d{2}',
    re.IGNORECASE,
)

# Maximum hyphen-separated tokens permitted in a concept filename.
# Anything longer is almost certainly a sentence/paragraph misread as a concept.
_MAX_CONCEPT_TOKENS = 8

# Minimum reasonable filename length (filters out garbage like "+-l-+").
_MIN_FILENAME_LENGTH = 3


class InvalidConceptNameError(ValueError):
    """Raised when a concept name cannot be turned into a valid permanent-note filename."""


def sanitize_filename(name: str) -> str:
    """
    Convert a concept name to a safe, lowercase, kebab-case filename.

    Rules:
      - Strip parenthetical disambiguators authors put in titles
      - Normalise common unicode (×, em-dashes, smart quotes)
      - Remove filesystem-unsafe + Obsidian-problematic characters
      - Lowercase everything (cross-OS case-sensitivity safety)
      - Collapse whitespace/underscores → single hyphen
      - Reject names that are obviously not concepts (too short, all-symbol,
        sentence-shaped, or matching a report-document pattern)
    """
    # Strip parenthetical content — usually citations/disambiguators
    cleaned = re.sub(r'\([^)]*\)', '', name)

    # Normalise unicode that breaks links / display.
    # Use explicit \u escapes to avoid editor-side glyph collisions.
    replacements = {
        '\u00d7': 'x',    # × multiplication sign
        '\u00f7': 'div',  # ÷ division sign
        '\u2014': '-',    # — em dash
        '\u2013': '-',    # – en dash
        '\u2212': '-',    # − minus sign
        '\u2018': '',     # ' left single quote
        '\u2019': '',     # ' right single quote / apostrophe
        '\u201c': '',     # " left double quote
        '\u201d': '',     # " right double quote
        '\u201a': '',     # ‚ single low-9 quote
        '\u201e': '',     # „ double low-9 quote
        '\u2026': '',     # … ellipsis
        '\u00a0': ' ',    # non-breaking space → regular space
    }
    for src, dst in replacements.items():
        cleaned = cleaned.replace(src, dst)

    # Strip filesystem-unsafe + Obsidian-problematic chars
    safe = re.sub(r'[<>:"/\\|?*\[\]()`,;&\'!@#$%^{}+]', '', cleaned)
    # Whitespace / underscore → hyphen
    safe = re.sub(r'[\s_]+', '-', safe)
    # Collapse runs of hyphens
    safe = re.sub(r'-{2,}', '-', safe)
    safe = safe.strip('-').lower()

    # ── Validation: reject pathological names ────────────────────────────
    if len(safe) < _MIN_FILENAME_LENGTH:
        raise InvalidConceptNameError(
            f"Concept name too short after sanitisation: {name!r} → {safe!r}"
        )
    if not re.search(r'[a-z]', safe):
        raise InvalidConceptNameError(
            f"Concept name contains no alphabetic characters: {name!r} → {safe!r}"
        )
    if len(safe.split('-')) > _MAX_CONCEPT_TOKENS:
        raise InvalidConceptNameError(
            f"Concept name too long ({len(safe.split('-'))} tokens, max {_MAX_CONCEPT_TOKENS}): "
            f"{name!r} — looks like a sentence, not a concept"
        )
    if _REPORT_FILENAME_PATTERN.search(safe):
        raise InvalidConceptNameError(
            f"Refusing to create permanent note from report-document filename: {safe!r}. "
            f"Source reports belong in literature notes, not permanent notes."
        )

    if len(safe) > MAX_FILENAME_LENGTH:
        safe = safe[:MAX_FILENAME_LENGTH].rstrip('-')
    return safe


def get_output_filename(candidate: NoteCandidate) -> str:
    """Generate the output filename for a permanent note.

    Raises:
        InvalidConceptNameError: if the candidate's concept name is invalid
            (too short, sentence-shaped, or matches a report filename).
    """
    clean = _clean_concept_name(candidate.concept_name)
    safe_name = sanitize_filename(clean)
    return f'{safe_name}.md'


def _pipe_link(display_name: str) -> str:
    """Build pipe-syntax wiki-link: [[Filename-Stem|Display Name]].

    If the display name already matches the filename stem (single words),
    returns a plain link without the pipe. Falls back to a plain link if
    the display name cannot be sanitised into a valid filename stem.
    """
    try:
        stem = sanitize_filename(display_name)
    except InvalidConceptNameError:
        # Display name isn't a valid concept (e.g. a citation, sentence,
        # or symbol-only string). Fall back to a plain wiki-link with the
        # raw display name; the link-resolver pass can handle / flag it.
        return f'[[{display_name}]]'
    if stem == display_name:
        return f'[[{display_name}]]'
    return f'[[{stem}|{display_name}]]'


# ══════════════════════════════════════════════════════════════════════════════
# FRONTMATTER BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def build_frontmatter(candidate: NoteCandidate) -> str:
    """Build YAML frontmatter for a permanent note."""
    meta = candidate.report_metadata
    today = date.today().isoformat()

    # ── Derived fields ────────────────────────────────────────────────────
    complexity = KNOWLEDGE_LEVEL_TO_COMPLEXITY.get(
        meta.knowledge_level if meta else "intermediate",
        "intermediate"
    )

    confidence = meta.confidence if meta else "medium"
    if confidence not in ("high", "medium", "low"):
        confidence = "medium"

    domain = candidate.domain if candidate.domain in VALID_DOMAINS else "other"

    subdomains = []
    if meta and meta.secondary_domains:
        subdomains = meta.secondary_domains[:5]

    # ── Tags ──────────────────────────────────────────────────────────────
    tags = ["permanent-note", "evergreen", domain]
    if meta and meta.tags:
        for tag in meta.tags[:MAX_REPORT_TAGS]:
            tag_clean = str(tag).strip()
            if tag_clean and tag_clean not in tags:
                tags.append(tag_clean)

    # ── Clean concept name ────────────────────────────────────────────────
    clean_name = _clean_concept_name(candidate.concept_name)

    # ── Aliases ───────────────────────────────────────────────────────────
    aliases = _build_aliases(clean_name)

    # ── Source reports ────────────────────────────────────────────────────
    source_reports = []
    if candidate.source_report:
        source_reports.append(candidate.source_report.replace('.md', ''))

    # ── Relationship fields ───────────────────────────────────────────────
    related_links = []
    if meta and meta.related_concepts:
        for concept in meta.related_concepts[:MAX_RELATED_LINKS]:
            related_links.append(f'  - "{_pipe_link(concept)}"')

    related_set = set(meta.related_concepts) if meta else set()
    see_also = []
    for wl in candidate.wiki_links[:MAX_SEE_ALSO_LINKS + MAX_RELATED_LINKS]:
        if wl not in related_set and wl != clean_name:
            see_also.append(f'  - "{_pipe_link(wl)}"')
        if len(see_also) >= MAX_SEE_ALSO_LINKS:
            break

    builds_on = []
    if meta and meta.builds_on:
        for b in meta.builds_on[:5]:
            safe_b = b.replace('"', "'")
            builds_on.append(f'  - "{_pipe_link(safe_b)}"')

    enables = []
    if meta and meta.feeds_into:
        for f_item in meta.feeds_into[:5]:
            safe_f = f_item.replace('"', "'")
            enables.append(f'  - "{_pipe_link(safe_f)}"')

    # ── Expansion topics ──────────────────────────────────────────────────
    expansion_yaml = []
    if candidate.expansion_topics:
        for topic in candidate.expansion_topics[:4]:
            if isinstance(topic, dict):
                safe_topic = topic["topic"].replace('"', "'")
                desc = topic.get("description", "").replace('"', "'")[:100]
            else:
                safe_topic = str(topic).replace('"', "'")[:100]
                desc = ""
            expansion_yaml.append(f'  - topic: "{_pipe_link(safe_topic)}"')
            expansion_yaml.append(f'    description: "{desc}"')
            expansion_yaml.append(f'    priority: medium')

    # ── Importance heuristic ──────────────────────────────────────────────
    if candidate.callout_type == "original-synthesis":
        importance = "high"
    elif confidence == "high":
        importance = "high"
    else:
        importance = "medium"

    # ══════════════════════════════════════════════════════════════════════
    # ASSEMBLE YAML
    # ══════════════════════════════════════════════════════════════════════
    lines = [
        '---',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# CORE IDENTITY',
        '# ═══════════════════════════════════════════════════════════════════════════',
        f'title: "{_yaml_escape(clean_name)}"',
        'aliases:',
    ]
    for alias in aliases:
        lines.append(f'  - "{_yaml_escape(alias)}"')

    lines.extend([
        'type: permanent-note',
        'status: evergreen',
        f'confidence: {confidence}',
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# CLASSIFICATION',
        '# ═══════════════════════════════════════════════════════════════════════════',
        'tags:',
    ])
    for tag in tags:
        lines.append(f'  - {tag}')

    lines.extend([
        '',
        f'domain: {domain}',
        'subdomains:',
    ])
    if subdomains:
        for sd in subdomains:
            lines.append(f'  - {sd}')
    else:
        lines.append('  - ')

    lines.extend([
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# TEMPORAL',
        '# ═══════════════════════════════════════════════════════════════════════════',
        f'created: {today}',
        f'updated: {today}',
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# SOURCE TRACKING',
        '# ═══════════════════════════════════════════════════════════════════════════',
        'source-type: report-extraction',
        'source-reports:',
    ])
    for sr in source_reports:
        lines.append(f'  - "{_yaml_escape(sr)}"')

    # ── Provenance chain ──────────────────────────────────────────────────
    batch_name = ""
    if candidate.source_report:
        # Infer batch from source report path if available
        batch_name = getattr(candidate, 'extraction_batch', '')
    lines.extend([
        f'evidence-quality: {confidence}',
        'extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"',
        f'pipeline-version: "2.1.0"',
        f'extraction-date: "{today}"',
    ])
    if batch_name:
        lines.append(f'extraction-batch: "{_yaml_escape(batch_name)}"')

    lines.extend([
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# CONTENT CHARACTERISTICS',
        '# ═══════════════════════════════════════════════════════════════════════════',
        f'complexity-level: {complexity}',
        'depth-level: comprehensive',
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# RELATIONSHIPS',
        '# ═══════════════════════════════════════════════════════════════════════════',
        'prerequisites:',
        '  []',
        '',
        'related:',
    ])
    if related_links:
        lines.extend(related_links)
    else:
        lines.append('  []')

    lines.extend([
        '',
        'broader:',
        '  []',
        '',
        'narrower:',
        '  []',
        '',
        'see-also:',
    ])
    if see_also:
        lines.extend(see_also)
    else:
        lines.append('  []')

    lines.extend([
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# LEARNING PATHWAYS',
        '# ═══════════════════════════════════════════════════════════════════════════',
        'builds-on:',
    ])
    if builds_on:
        lines.extend(builds_on)
    else:
        lines.append('  []')

    lines.extend([
        '',
        'enables:',
    ])
    if enables:
        lines.extend(enables)
    else:
        lines.append('  []')

    lines.extend([
        '',
        'expansion-topics:',
    ])
    if expansion_yaml:
        lines.extend(expansion_yaml)
    else:
        lines.append('  []')

    lines.extend([
        '',
        '# ═══════════════════════════════════════════════════════════════════════════',
        '# PERSONAL KNOWLEDGE MANAGEMENT',
        '# ═══════════════════════════════════════════════════════════════════════════',
        'review-frequency: quarterly',
        'mastery-stage: seedling',
        f'importance: {importance}',
        '---',
    ])

    return '\n'.join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# BODY BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def build_body(candidate: NoteCandidate) -> str:
    """Build the markdown body for a permanent note.

    Structure (v2.2):
      # Title
      > [!definition] ...
      ## Core Explanation (evidence + insights)
      ## Practical Implications (practices + warnings)
      ## Key Figures & Intellectual Lineage (persons)
      ## Conceptual Tensions (tensions)
      ## Open Questions (open questions)
      ## Reflection Prompts (reflections)
      ## Schema Activations (schema-activation)
      ## Active Reading Prompts (active-reading)
      ## Far Transfer Applications (far-transfer)
      ## Debates (debate)
      ## Examples (example)
      ## AI Insights (claude-insight)
      ## Section Summaries (section-summary)
      ## Spaced Repetition Seeds (flashcards)
      ## Protocols & Methods (protocols)
      ## Visual Representations (diagrams)
      ## Connections & Context (connections + wiki-links)
      ## References & Citations (citations)
      ## Methodology Notes (methodology)
      ## Source Attribution (report metadata)

    Every callout includes a source link back to the originating report.
    """
    lines = []
    source_report_name = candidate.source_report.replace('.md', '') if candidate.source_report else ""
    source_tag = f" *(from [[{source_report_name}]])*" if source_report_name else ""

    # ── Title ─────────────────────────────────────────────────────────────
    clean_name = _clean_concept_name(candidate.concept_name)
    lines.append(f'# {clean_name}')
    lines.append('')

    # ── Definition callout ────────────────────────────────────────────────
    lines.append(f'> [!definition] **{clean_name}**{source_tag}')
    for body_line in candidate.definition_body.split('\n'):
        lines.append(f'> {body_line}')
    lines.append('')

    # Attribution inline
    if candidate.attribution:
        lines.append(f'*Source: {candidate.attribution}*')
        lines.append('')

    # ── Core Explanation ──────────────────────────────────────────────────
    lines.append('## Core Explanation')
    lines.append('')

    if candidate.evidence:
        for ev in candidate.evidence:
            lines.append(f'> [!evidence] Supporting Evidence{source_tag}')
            for ev_line in _wrap_callout_body(ev):
                lines.append(f'> {ev_line}')
            lines.append('')

    if candidate.insights:
        for insight in candidate.insights:
            lines.append(f'> [!analytical-insight] Key Insight{source_tag}')
            for i_line in _wrap_callout_body(insight):
                lines.append(f'> {i_line}')
            lines.append('')

    if not candidate.evidence and not candidate.insights:
        lines.append('<!-- Expand this section with deeper explanation -->')
        lines.append('')

    # ── Practical Implications ────────────────────────────────────────────
    lines.append('## Practical Implications')
    lines.append('')

    if candidate.practices:
        for practice in candidate.practices:
            lines.append(f'> [!example] **Application**{source_tag}')
            for p_line in _wrap_callout_body(practice):
                lines.append(f'> {p_line}')
            lines.append('')
    else:
        lines.append('> [!example] **Application**')
        lines.append('> *Describe how this concept applies in practice.*')
        lines.append('')

    if candidate.warnings:
        for warning in candidate.warnings:
            lines.append(f'> [!warning] **Key Distinction**{source_tag}')
            for w_line in _wrap_callout_body(warning):
                lines.append(f'> {w_line}')
            lines.append('')

    # ── Key Figures & Intellectual Lineage ─────────────────────────────────
    if candidate.persons:
        lines.append('## Key Figures & Intellectual Lineage')
        lines.append('')
        for person in candidate.persons:
            title = person.get("title", "")
            body = person.get("body", "")
            if title:
                lines.append(f'> [!person] **{title}**{source_tag}')
            else:
                lines.append(f'> [!person] **Key Figure**{source_tag}')
            for p_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {p_line}')
            lines.append('')

    # ── Conceptual Tensions ───────────────────────────────────────────────
    if candidate.tensions:
        lines.append('## Conceptual Tensions')
        lines.append('')
        for tension in candidate.tensions:
            title = tension.get("title", "")
            body = tension.get("body", "")
            if title:
                lines.append(f'> [!tension] **{title}**{source_tag}')
            else:
                lines.append(f'> [!tension] **Unresolved Tension**{source_tag}')
            for t_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {t_line}')
            lines.append('')

    # ── Open Questions ────────────────────────────────────────────────────
    if candidate.open_questions:
        lines.append('## Open Questions')
        lines.append('')
        for oq in candidate.open_questions:
            title = oq.get("title", "")
            body = oq.get("body", "")
            if title:
                lines.append(f'> [!open-question] **{title}**{source_tag}')
            else:
                lines.append(f'> [!open-question]{source_tag}')
            for q_line in _wrap_callout_body(body, max_length=400):
                lines.append(f'> {q_line}')
            lines.append('')

    # ── Reflection Prompts ────────────────────────────────────────────────
    if candidate.reflections:
        lines.append('## Reflection Prompts')
        lines.append('')
        for reflection in candidate.reflections:
            lines.append(f'> [!reflection] **Reflect**{source_tag}')
            for r_line in _wrap_callout_body(reflection):
                lines.append(f'> {r_line}')
            lines.append('')

    # ── Schema Activations (v2.2) ─────────────────────────────────────────
    if candidate.schema_activations:
        lines.append('## Schema Activations')
        lines.append('')
        for sa in candidate.schema_activations:
            title = sa.get("title", "")
            body = sa.get("body", "")
            if title:
                lines.append(f'> [!schema-activation] **{title}**{source_tag}')
            else:
                lines.append(f'> [!schema-activation]{source_tag}')
            for s_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {s_line}')
            lines.append('')

    # ── Active Reading Prompts (v2.2) ─────────────────────────────────────
    if candidate.active_readings:
        lines.append('## Active Reading Prompts')
        lines.append('')
        for ar in candidate.active_readings:
            title = ar.get("title", "")
            body = ar.get("body", "")
            if title:
                lines.append(f'> [!active-reading] **{title}**{source_tag}')
            else:
                lines.append(f'> [!active-reading]{source_tag}')
            for a_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {a_line}')
            lines.append('')

    # ── Far Transfer Applications (v2.2) ──────────────────────────────────
    if candidate.far_transfers:
        lines.append('## Far Transfer Applications')
        lines.append('')
        for ft in candidate.far_transfers:
            title = ft.get("title", "")
            body = ft.get("body", "")
            if title:
                lines.append(f'> [!far-transfer] **{title}**{source_tag}')
            else:
                lines.append(f'> [!far-transfer]{source_tag}')
            for f_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {f_line}')
            lines.append('')

    # ── Debates (v2.2) ────────────────────────────────────────────────────
    if candidate.debates:
        lines.append('## Debates')
        lines.append('')
        for debate in candidate.debates:
            title = debate.get("title", "")
            body = debate.get("body", "")
            if title:
                lines.append(f'> [!debate] **{title}**{source_tag}')
            else:
                lines.append(f'> [!debate]{source_tag}')
            for d_line in _wrap_callout_body(body, max_length=800):
                lines.append(f'> {d_line}')
            lines.append('')

    # ── Examples (v2.2) ───────────────────────────────────────────────────
    if candidate.examples:
        lines.append('## Concrete Examples')
        lines.append('')
        for ex in candidate.examples:
            title = ex.get("title", "")
            body = ex.get("body", "")
            if title:
                lines.append(f'> [!example] **{title}**{source_tag}')
            else:
                lines.append(f'> [!example]{source_tag}')
            for e_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {e_line}')
            lines.append('')

    # ── AI Insights (v2.2) ────────────────────────────────────────────────
    if candidate.claude_insights:
        lines.append('## AI Insights')
        lines.append('')
        for ci in candidate.claude_insights:
            title = ci.get("title", "")
            body = ci.get("body", "")
            if title:
                lines.append(f'> [!claude-insight] **{title}**{source_tag}')
            else:
                lines.append(f'> [!claude-insight]{source_tag}')
            for c_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {c_line}')
            lines.append('')

    # ── Section Summaries (v2.2) ──────────────────────────────────────────
    if candidate.section_summaries:
        lines.append('## Section Summaries')
        lines.append('')
        for ss in candidate.section_summaries:
            title = ss.get("title", "")
            body = ss.get("body", "")
            if title:
                lines.append(f'> [!section-summary] **{title}**{source_tag}')
            else:
                lines.append(f'> [!section-summary]{source_tag}')
            for s_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {s_line}')
            lines.append('')

    # ── Spaced Repetition Seeds ───────────────────────────────────────────
    if candidate.flashcards:
        lines.append('## Spaced Repetition Seeds')
        lines.append('')
        for i, card in enumerate(candidate.flashcards, 1):
            q = card.get("question", card.get("title", ""))
            a = card.get("answer", card.get("body", ""))
            lines.append(f'> [!flashcard] **Card {i}**{source_tag}')
            lines.append(f'> **Q:** {q}')
            lines.append(f'> **A:** {a}')
            if card.get("difficulty"):
                lines.append(f'> *Difficulty: {card["difficulty"]}*')
            lines.append('')

    # ── Protocols & Methods ───────────────────────────────────────────────
    if candidate.protocols:
        lines.append('## Protocols & Methods')
        lines.append('')
        for protocol in candidate.protocols:
            title = protocol.get("title", "")
            body = protocol.get("body", "")
            if title:
                lines.append(f'> [!protocol] **{title}**{source_tag}')
            else:
                lines.append(f'> [!protocol] **Method**{source_tag}')
            for pr_line in _wrap_callout_body(body, max_length=800):
                lines.append(f'> {pr_line}')
            lines.append('')

    # ── Diagrams ──────────────────────────────────────────────────────────
    if candidate.diagrams:
        lines.append('## Visual Representations')
        lines.append('')
        for diagram in candidate.diagrams:
            title = diagram.get("title", "")
            body = diagram.get("body", "")
            if title:
                lines.append(f'> [!diagram] **{title}**{source_tag}')
            else:
                lines.append(f'> [!diagram]{source_tag}')
            for d_line in body.split('\n'):
                lines.append(f'> {d_line}')
            lines.append('')

    # ── Connections & Context ─────────────────────────────────────────────
    lines.append('## Connections & Context')
    lines.append('')

    if candidate.connections:
        for conn in candidate.connections:
            conn_links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', conn)
            if conn_links:
                lines.append(f'**Cross-report connections**{source_tag}:')
                for cl in conn_links[:10]:
                    lines.append(f'- {_pipe_link(cl)}')
                lines.append('')

    # Wiki-link cloud for quick navigation
    if candidate.wiki_links:
        lines.append('**Related concepts:**')
        relevant_links = [
            wl for wl in candidate.wiki_links[:MAX_WIKI_LINKS_DISPLAY]
            if wl != clean_name
        ]
        link_text = ' \u00b7 '.join(_pipe_link(wl) for wl in relevant_links)
        lines.append(link_text)
        lines.append('')

    # ── References & Citations ────────────────────────────────────────────
    if candidate.citations:
        lines.append('## References')
        lines.append('')
        for cite in candidate.citations:
            title = cite.get("title", "")
            body = cite.get("body", "")
            if title:
                lines.append(f'- **{title}**: {body}')
            else:
                lines.append(f'- {body}')
        if source_report_name:
            lines.append(f'\n*Citations sourced from [[{source_report_name}]]*')
        lines.append('')

    # ── Methodology Notes ─────────────────────────────────────────────────
    if candidate.methodology:
        lines.append('## Methodology Notes')
        lines.append('')
        for meth in candidate.methodology:
            title = meth.get("title", "")
            body = meth.get("body", "")
            if title:
                lines.append(f'> [!methodology-and-sources] **{title}**{source_tag}')
            else:
                lines.append(f'> [!methodology-and-sources]{source_tag}')
            for m_line in _wrap_callout_body(body, max_length=600):
                lines.append(f'> {m_line}')
            lines.append('')

    # ── Source Attribution ─────────────────────────────────────────────────
    lines.append('---')
    lines.append('')
    lines.append('## Source Attribution')
    lines.append('')
    if candidate.source_report:
        report_name = candidate.source_report.replace('.md', '')
        lines.append(f'**Extracted from:** [[{report_name}]]')
    if candidate.report_metadata:
        meta = candidate.report_metadata
        if meta.doc_id:
            lines.append(f'**Report ID:** `{meta.doc_id}`')
        if meta.analytical_focus:
            lines.append(f'**Analytical focus:** {meta.analytical_focus}')
        if meta.series_position:
            lines.append(f'**Series position:** {meta.series_position}')
    lines.append('')

    return '\n'.join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# FULL NOTE ASSEMBLY
# ══════════════════════════════════════════════════════════════════════════════

def build_permanent_note(candidate: NoteCandidate) -> str:
    """Build a complete permanent note markdown document."""
    frontmatter = build_frontmatter(candidate)
    body = build_body(candidate)
    return f'{frontmatter}\n\n{body}'


# ══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def _yaml_escape(text: str) -> str:
    """Escape special characters for YAML string values."""
    return text.replace('"', '\\"')


def _clean_concept_name(raw: str) -> str:
    """
    Strip wiki-link brackets and normalise a raw concept name.

    Examples:
      '[[Blocking]]'                      -> 'Blocking'
      '[[Testing Effect]] / [[Retrieval Practice Effect]]'
                                          -> 'Testing Effect / Retrieval Practice Effect'
      'Feeling of Knowing — FOK'          -> 'Feeling of Knowing — FOK'  (unchanged)
      'Adaptive Learning Systems — Ed...' -> 'Adaptive Learning Systems — Ed...' (unchanged)
    """
    # Strip all [[ and ]] from the name
    cleaned = raw.replace('[[', '').replace(']]', '')
    return cleaned.strip()


def _build_aliases(clean_name: str) -> list[str]:
    """
    Generate a comprehensive alias list for Obsidian wiki-link resolution.

    Handles compound names separated by / or — (em-dash) by splitting them
    into individual aliases.  Also generates commonly-used short forms.

    Returns a deduplicated list with the full clean name first.
    """
    seen = set()
    aliases = []

    def _add(name: str) -> None:
        """Add a name to aliases if not already present."""
        name = name.strip()
        if name and name.lower() not in seen:
            seen.add(name.lower())
            aliases.append(name)

    # 1. Full clean name is always first
    _add(clean_name)

    # 2. Split on em-dash (—) — usually separates concept from domain/context
    #    e.g. "Feeling of Knowing — FOK"
    #    e.g. "Adaptive Learning Systems — Educational Technology"
    if '—' in clean_name:
        parts = [p.strip() for p in clean_name.split('—') if p.strip()]
        for part in parts:
            # Each part might itself have / separators
            if '/' in part:
                subparts = [s.strip() for s in part.split('/') if s.strip()]
                for sp in subparts:
                    _add(sp)
            else:
                _add(part)

    # 3. Split on slash (/) — usually separates synonyms or subtypes
    #    e.g. "Confirmation Bias / Myside Bias"
    #    e.g. "Constructivist Learning Environments / CLEs"
    elif '/' in clean_name:
        parts = [p.strip() for p in clean_name.split('/') if p.strip()]
        for part in parts:
            _add(part)

    # 4. Generate a useful acronym ONLY for the primary concept
    #    (the first part before any — or /)
    primary = aliases[0] if not ('—' in clean_name or '/' in clean_name) else aliases[1] if len(aliases) > 1 else aliases[0]
    primary_words = [w for w in primary.split() if w[0:1].isalpha()]
    if len(primary_words) >= 3:
        acronym = ''.join(w[0].upper() for w in primary_words)
        if 3 <= len(acronym) <= 6:
            _add(acronym)

    return aliases


def _wrap_callout_body(text: str, max_length: int = 500) -> list[str]:
    """
    Prepare text for use inside an Obsidian callout block.
    Truncates excessively long bodies and splits into lines.
    """
    if len(text) > max_length:
        text = text[:max_length].rsplit(' ', 1)[0] + '…'
    return text.split('\n')
