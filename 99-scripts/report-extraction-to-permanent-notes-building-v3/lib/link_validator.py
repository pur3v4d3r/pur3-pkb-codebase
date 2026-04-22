#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""link_validator.py — Single source of truth for concept-name validation.

Consolidates every wiki-link / concept rejection rule that was scattered across
v2's ``note_updater.py``, ``note_builder.py``, and ``audit_notes.py`` into one
canonical predicate:

    is_valid_concept(name: str) -> tuple[bool, str]

Returns ``(True, "")`` for valid concept names. Returns ``(False, reason_code)``
for rejections, where ``reason_code`` is a short slug (``empty``, ``too-short``,
``templater-syntax``, etc.). Reason codes are stable strings — Stage 2's
``_validation-report.json`` and any downstream analysis can rely on them.

This module is pure (no I/O, no globals beyond compiled regex), import-cheap,
and exhaustively tested. Every behavior documented here has a fixture in
``tests/test_link_validator.py``.

Phase 1 deliverable. See spec §5 Phase 1.
"""
from __future__ import annotations

import re
from typing import Final

# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Minimum length for a concept name after stripping whitespace.
MIN_NAME_LENGTH: Final[int] = 3

#: Maximum whitespace-separated word tokens permitted. Anything longer is
#: almost certainly a sentence the extractor misread as a concept.
#: (Phase 1.5 tuning: raised from 8 to 10 to admit legitimate long concept
#: titles such as "The Forgetting Curve and the Power of Retrieval Practice".)
MAX_CONCEPT_TOKENS: Final[int] = 10

#: Maximum total length; longer ⇒ sentence/paragraph.
MAX_NAME_LENGTH: Final[int] = 120


# ════════════════════════════════════════════════════════════════════════════
# Regex inventory  (each pattern paired with the reason code it triggers)
# ════════════════════════════════════════════════════════════════════════════

# Templater plugin syntax leaking into link targets — never a real concept.
_TEMPLATER_PATTERNS: Final[tuple[re.Pattern[str], ...]] = (
    re.compile(r"<%"),
    re.compile(r"%>"),
    re.compile(r"\btp\."),
)

# Pure-formatting wrappers (the entire string is bold/italic markers).
_FORMATTING_ONLY_PATTERNS: Final[tuple[re.Pattern[str], ...]] = (
    re.compile(r"^\*\*[^*]+\*\*$"),
    re.compile(r"^__[^_]+__$"),
    re.compile(r"^_[^_]+_$"),
    re.compile(r"^\*[^*]+\*$"),
)

# Pure numbers / years (1–4 digits).
_PURE_NUMERIC_PATTERN: Final[re.Pattern[str]] = re.compile(r"^\d{1,4}$")

# Template placeholder text the extractor sometimes captures verbatim.
_TEMPLATE_PLACEHOLDER_PATTERNS: Final[tuple[re.Pattern[str], ...]] = (
    re.compile(r"^Note-?\d+$", re.IGNORECASE),
    re.compile(r"^Note Title", re.IGNORECASE),
    re.compile(r"^Concept-?\d+$", re.IGNORECASE),
    re.compile(r"^Untitled", re.IGNORECASE),
    re.compile(r"^Placeholder", re.IGNORECASE),
)

# YAML key fragments leaked from a frontmatter block into link text.
_YAML_FRAGMENT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(priority|aliases|topic|tags|status|type|created|modified):",
    re.IGNORECASE,
)

# Any character classified as alphabetic.
_HAS_ALPHA: Final[re.Pattern[str]] = re.compile(r"[A-Za-z]")

# Report-document filename signature. Source reports are literature, not
# permanent notes; refuse to mint a concept note from one.
_REPORT_FILENAME_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"-(foundational-report|focused-analysis|dialectical(-re-examination)?"
    r"|socratic(-dialogue)?|comparative(-synthesis)?|first-principles"
    r"|generative-learning|pkb-focused-analysis)-\d{4}-\d{2}-\d{2}",
    re.IGNORECASE,
)

# Sentence-shape detector: ends with sentence punctuation.
_SENTENCE_TERMINATOR: Final[re.Pattern[str]] = re.compile(r"[.!?]\s*$")

# Author-citation / abbreviation forms whose terminal period is NOT a sentence
# end. Phase 1.5 tuning: exempt these from the sentence-shaped rejection so
# legitimate scholarly references survive ("Pressley et al.", "Holmes Jr.",
# "patient H.M.", "F.D.R.", etc.).
_AUTHOR_CITATION_EXEMPT: Final[re.Pattern[str]] = re.compile(
    r"(?:"
    r"\bet\s+al\.?$"            # "... et al." / "... et al"
    r"|\b[JS]r\.$"               # "... Jr." / "... Sr."
    r"|\bI{1,3}\.$"              # "... II." / "... III."
    r"|\b(?:[A-Z]\.){2,}$"       # initials: "H.M.", "F.D.R."
    r")",
    re.IGNORECASE,
)

# Forbidden characters that break Obsidian links or indicate parser garbage.
_DISALLOWED_CHARS: Final[re.Pattern[str]] = re.compile(r"[<>{}|\\^`\[\]]")

# APA-style citation signature. Triggers on any string that looks like a
# bibliography entry slugified into a wiki-link target. Three independent
# signals must all be present:
#   (1) a surname-then-initial pattern: ``Surname,-X.`` or ``Surname,-X.-Y.``
#   (2) a 4-digit year (1850-2099)
#   (3) at least one period after the surname (citation punctuation)
# This combination is virtually never present in a legitimate concept name.
# Phase 1.5 leak-fix: the audit showed 1000+ unresolved targets of this shape
# (e.g. ``Bjork,-R.-A.-1994.-Memory-and-metamemory-considerations-...``).
_CITATION_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^[A-Z][a-z\u00C0-\u017F'’\-]+,[\s\-]*[A-Z]\."   # "Surname,-X."
    r".*?\b(?:18[5-9]\d|19\d{2}|20\d{2})\b",          # plus 4-digit year somewhere
)

# Author-bio signature. The extractor sometimes captures section headings of
# the form "Albert Bandura (1925–2021) — Stanford University" as wiki-link
# targets. After slugification these become unresolvable and self-fragmenting:
# every report restates the affiliation slightly differently and produces a
# distinct broken link. Detect the lifespan/affiliation marker:
#   (1) en-dash (U+2013) or em-dash (U+2014) anywhere
#   (2) AND either a 4-digit year OR a multi-word affiliation token
# Phase 1.5 leak-fix: audit showed ~10 distinct author-bio leaks each with 80+
# refs (e.g. ``Albert-Bandura-1925–2021-—-Stanford-University``).
_AUTHOR_BIO_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"[\u2013\u2014]"                              # en-dash or em-dash
    r".*?(?:\b(?:18[5-9]\d|19\d{2}|20\d{2})\b"     # year OR
    r"|\b(?:University|Institute|College|Center|Centre|School|Laboratory|Lab|present)\b)",
    re.IGNORECASE,
)


# ════════════════════════════════════════════════════════════════════════════
# Reason codes  (stable identifiers — downstream depends on these strings)
# ════════════════════════════════════════════════════════════════════════════

#: Frozenset of every rejection code emitted by ``is_valid_concept``.
REASON_CODES: Final[frozenset[str]] = frozenset({
    "empty",
    "too-short",
    "too-long",
    "templater-syntax",
    "formatting-only",
    "pure-numeric",
    "template-placeholder",
    "yaml-fragment-leak",
    "no-alphabetic",
    "disallowed-chars",
    "report-filename",
    "citation",
    "author-bio",
    "too-many-tokens",
    "sentence-shaped",
})


# ════════════════════════════════════════════════════════════════════════════
# Public API
# ════════════════════════════════════════════════════════════════════════════

def is_valid_concept(name: str) -> tuple[bool, str]:
    """Validate a wiki-link target / concept name.

    Returns:
        ``(True, "")`` if ``name`` is a plausible concept name suitable for a
        permanent note; ``(False, reason_code)`` otherwise. Reason codes are
        members of :data:`REASON_CODES`.

    The check is intentionally conservative — false positives (rejecting a
    real concept) are far less harmful than false negatives (admitting
    garbage). Stage 2 logs every rejection so the user can spot
    over-rejection in practice.

    Args:
        name: The raw wiki-link target. Surrounding whitespace is stripped.

    Examples:
        >>> is_valid_concept("Self-Determination Theory")
        (True, '')
        >>> is_valid_concept("")
        (False, 'empty')
        >>> is_valid_concept("<%tp.file.title%>")
        (False, 'templater-syntax')
        >>> is_valid_concept("**Bold Text**")
        (False, 'formatting-only')
        >>> is_valid_concept("2024")
        (False, 'pure-numeric')
    """
    if name is None:  # type: ignore[truthy-bool]
        return (False, "empty")

    stripped = name.strip()

    if not stripped:
        return (False, "empty")
    if len(stripped) < MIN_NAME_LENGTH:
        return (False, "too-short")
    if len(stripped) > MAX_NAME_LENGTH:
        return (False, "too-long")

    for pattern in _TEMPLATER_PATTERNS:
        if pattern.search(stripped):
            return (False, "templater-syntax")

    for pattern in _FORMATTING_ONLY_PATTERNS:
        if pattern.match(stripped):
            return (False, "formatting-only")

    if _PURE_NUMERIC_PATTERN.match(stripped):
        return (False, "pure-numeric")

    for pattern in _TEMPLATE_PLACEHOLDER_PATTERNS:
        if pattern.match(stripped):
            return (False, "template-placeholder")

    if _YAML_FRAGMENT_PATTERN.search(stripped):
        return (False, "yaml-fragment-leak")

    if not _HAS_ALPHA.search(stripped):
        return (False, "no-alphabetic")

    if _DISALLOWED_CHARS.search(stripped):
        return (False, "disallowed-chars")

    if _REPORT_FILENAME_PATTERN.search(stripped):
        return (False, "report-filename")

    if _CITATION_PATTERN.search(stripped):
        return (False, "citation")

    if _AUTHOR_BIO_PATTERN.search(stripped):
        return (False, "author-bio")

    word_tokens = stripped.split()
    if len(word_tokens) > MAX_CONCEPT_TOKENS:
        return (False, "too-many-tokens")

    if _SENTENCE_TERMINATOR.search(stripped):
        # Exempt author-citation / abbreviation forms ("Pressley et al.",
        # "Holmes Jr.", "H.M.") whose terminal period is not a sentence end.
        if not _AUTHOR_CITATION_EXEMPT.search(stripped):
            return (False, "sentence-shaped")

    return (True, "")


def is_garbage(name: str) -> bool:
    """Return ``True`` iff ``name`` is rejected by :func:`is_valid_concept`.

    Drop-in replacement for v2's ``_is_garbage_link``.
    """
    return not is_valid_concept(name)[0]


def rejection_reason(name: str) -> str:
    """Return the reason code for a rejected name, or ``""`` if accepted."""
    return is_valid_concept(name)[1]
