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

def sanitize_filename(name: str) -> str:
    """
    Convert a concept name to a safe, Obsidian-compatible filename.

    Rules:
      - Remove filesystem-unsafe characters
      - Replace spaces with hyphens
      - Collapse multiple hyphens
      - Truncate to MAX_FILENAME_LENGTH
    """
    safe = re.sub(r'[<>:"/\\|?*\[\]()]', '', name)
    safe = re.sub(r'[\s_]+', '-', safe)
    safe = re.sub(r'-{2,}', '-', safe)
    safe = safe.strip('-')
    if len(safe) > MAX_FILENAME_LENGTH:
        safe = safe[:MAX_FILENAME_LENGTH].rstrip('-')
    return safe


def get_output_filename(candidate: NoteCandidate) -> str:
    """Generate the output filename for a permanent note."""
    clean = _clean_concept_name(candidate.concept_name)
    safe_name = sanitize_filename(clean)
    return f'{safe_name}.md'


def _pipe_link(display_name: str) -> str:
    """Build pipe-syntax wiki-link: [[Filename-Stem|Display Name]].

    If the display name already matches the filename stem (single words),
    returns a plain link without the pipe.
    """
    stem = sanitize_filename(display_name)
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

    lines.extend([
        f'evidence-quality: {confidence}',
        'extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"',
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
        '  - "[[]]"',
        '',
        'related:',
    ])
    if related_links:
        lines.extend(related_links)
    else:
        lines.append('  - "[[]]"')

    lines.extend([
        '',
        'broader:',
        '  - "[[]]"',
        '',
        'narrower:',
        '  - "[[]]"',
        '',
        'see-also:',
    ])
    if see_also:
        lines.extend(see_also)
    else:
        lines.append('  - "[[]]"')

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
        lines.append('  - "[[]]"')

    lines.extend([
        '',
        'enables:',
    ])
    if enables:
        lines.extend(enables)
    else:
        lines.append('  - "[[]]"')

    lines.extend([
        '',
        'expansion-topics:',
    ])
    if expansion_yaml:
        lines.extend(expansion_yaml)
    else:
        lines.extend([
            '  - topic: "[[]]"',
            '    description: ""',
            '    priority: medium',
        ])

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
    """Build the markdown body for a permanent note."""
    lines = []

    # ── Title ─────────────────────────────────────────────────────────────
    clean_name = _clean_concept_name(candidate.concept_name)
    lines.append(f'# {clean_name}')
    lines.append('')

    # ── Definition callout ────────────────────────────────────────────────
    lines.append(f'> [!definition] **{clean_name}**')
    for body_line in candidate.definition_body.split('\n'):
        lines.append(f'> {body_line}')
    lines.append('')

    # Attribution
    if candidate.attribution:
        lines.append(f'*Source: {candidate.attribution}*')
        lines.append('')

    # ── Core Explanation ──────────────────────────────────────────────────
    lines.append('## Core Explanation')
    lines.append('')

    if candidate.evidence:
        for ev in candidate.evidence:
            lines.append('> [!evidence] Supporting Evidence')
            for ev_line in _wrap_callout_body(ev):
                lines.append(f'> {ev_line}')
            lines.append('')

    if candidate.insights:
        for insight in candidate.insights:
            lines.append('> [!analytical-insight] Key Insight')
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
            lines.append('> [!example] **Application**')
            for p_line in _wrap_callout_body(practice):
                lines.append(f'> {p_line}')
            lines.append('')
    else:
        lines.append('> [!example] **Application**')
        lines.append('> *Describe how this concept applies in practice.*')
        lines.append('')

    if candidate.warnings:
        for warning in candidate.warnings:
            lines.append('> [!warning] **Key Distinction**')
            for w_line in _wrap_callout_body(warning):
                lines.append(f'> {w_line}')
            lines.append('')

    # ── Reflection Prompts ────────────────────────────────────────────────
    if candidate.reflections:
        lines.append('## Reflection Prompts')
        lines.append('')
        for reflection in candidate.reflections:
            lines.append('> [!reflection] **Reflect**')
            for r_line in _wrap_callout_body(reflection):
                lines.append(f'> {r_line}')
            lines.append('')

    # ── Connections & Context ─────────────────────────────────────────────
    lines.append('## Connections & Context')
    lines.append('')

    if candidate.connections:
        for conn in candidate.connections:
            # Extract wiki-links from connection text for display
            conn_links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', conn)
            if conn_links:
                lines.append('**Cross-report connections:**')
                for cl in conn_links[:10]:
                    lines.append(f'- {_pipe_link(cl)}')
                lines.append('')

    # Wiki-link cloud for quick navigation
    if candidate.wiki_links:
        lines.append('**Related concepts:**')
        relevant_links = [
            wl for wl in candidate.wiki_links[:MAX_WIKI_LINKS_DISPLAY]
            if wl != _clean_concept_name(candidate.concept_name)
        ]
        link_text = ' \u00b7 '.join(_pipe_link(wl) for wl in relevant_links)
        lines.append(link_text)
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
