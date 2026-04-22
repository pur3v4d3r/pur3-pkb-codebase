#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for ``lib.link_validator``.

Exhaustive fixture coverage per spec §5 Phase 1 gate:
  - ≥30 garbage fixtures across all rejection categories — every one rejected
  - ≥10 real-world valid concept fixtures — every one accepted
  - Reason-code stability: every emitted reason ∈ ``REASON_CODES``
"""
from __future__ import annotations

import pytest

from lib.link_validator import (
    MAX_CONCEPT_TOKENS,
    MAX_NAME_LENGTH,
    MIN_NAME_LENGTH,
    REASON_CODES,
    is_garbage,
    is_valid_concept,
    rejection_reason,
)


# ════════════════════════════════════════════════════════════════════════════
# Garbage fixtures — must all be REJECTED with the matching reason code
# ════════════════════════════════════════════════════════════════════════════

GARBAGE_CASES: list[tuple[str, str]] = [
    # ── empty / whitespace ─────────────────────────────────────────────
    ("",                     "empty"),
    ("   ",                  "empty"),
    ("\n\t",                 "empty"),

    # ── too-short ──────────────────────────────────────────────────────
    ("a",                    "too-short"),
    ("ok",                   "too-short"),
    ("X",                    "too-short"),

    # ── too-long ───────────────────────────────────────────────────────
    ("x" * (MAX_NAME_LENGTH + 1), "too-long"),

    # ── templater syntax ───────────────────────────────────────────────
    ("<%tp.file.title%>",    "templater-syntax"),
    ("Some <% expr %> Thing","templater-syntax"),
    ("tp.frontmatter.value", "templater-syntax"),
    ("foo %> bar",           "templater-syntax"),

    # ── pure-formatting wrappers ───────────────────────────────────────
    ("**Bold Text**",        "formatting-only"),
    ("__Underlined__",       "formatting-only"),
    ("_italic_",             "formatting-only"),
    ("*emphasised*",         "formatting-only"),

    # ── pure numeric / years ───────────────────────────────────────────
    ("2024",                 "pure-numeric"),
    ("1999",                 "pure-numeric"),
    ("999",                  "pure-numeric"),
    ("007",                  "pure-numeric"),

    # ── template placeholders ──────────────────────────────────────────
    ("Note-1",               "template-placeholder"),
    ("note42",               "template-placeholder"),
    ("Note Title Here",      "template-placeholder"),
    ("Concept-7",            "template-placeholder"),
    ("Untitled",             "template-placeholder"),
    ("Untitled-3",           "template-placeholder"),
    ("Placeholder Concept",  "template-placeholder"),

    # ── YAML fragment leak ─────────────────────────────────────────────
    ("priority: high",       "yaml-fragment-leak"),
    ("aliases: [foo, bar]",  "yaml-fragment-leak"),
    ("topic: motivation",    "yaml-fragment-leak"),
    ("Some Tags: foo",       "yaml-fragment-leak"),
    ("status: evergreen",    "yaml-fragment-leak"),

    # ── no alphabetic characters ───────────────────────────────────────
    ("123 456",              "no-alphabetic"),
    ("---",                  "no-alphabetic"),
    ("+++",                  "no-alphabetic"),

    # ── disallowed characters ──────────────────────────────────────────
    ("Some [Bracketed] Thing", "disallowed-chars"),
    ("path\\with\\backslashes", "disallowed-chars"),
    ("pipe|delimited",       "disallowed-chars"),

    # ── report filename signatures ─────────────────────────────────────
    ("srl-foundational-report-2026-04-20",                    "report-filename"),
    ("sdt-comparative-synthesis-2026-03-19",                  "report-filename"),
    ("metacog-dialectical-re-examination-2026-04-15",         "report-filename"),
    ("learning-first-principles-2025-11-30",                  "report-filename"),
    # ── APA-style citation slugs (Phase 1.5 leak fix) ─────────────────
    ("Bjork,-R.-A.-1994.-Memory-and-metamemory-considerations", "citation"),
    ("Bandura,-A.-1997.-Self-efficacy-The-exercise-of-control", "citation"),
    ("Boekaerts,-M.-1996.-Self-regulated-learning-at-the-junction", "citation"),
    ("Ahrens,-S.-2017.-How-to-Take-Smart-Notes",                "citation"),
    ("Abramson,-L.-Y.,-Seligman,-M.-E.-P.,-1978.-Learned",      "citation"),

    # ── author-bio with lifespan/affiliation (Phase 1.5 leak fix) ───────
    ("Albert-Bandura-1925–2021-—-Stanford-University",            "author-bio"),
    ("Anastasia-Efklides-1949–-,-Aristotle-University-of-Thessaloniki", "author-bio"),
    ("Barry-J.-Zimmerman-1942–-,-CUNY-Graduate-Center",          "author-bio"),
    ("Ann-L.-Brown-1943–1999-—-University-of-California",        "author-bio"),
    ("Annemarie-Sullivan-Palincsar-—-University-of-Michigan",   "author-bio"),
    # ── too many tokens (sentence-shaped by length) ────────────────────
    (" ".join(["word"] * (MAX_CONCEPT_TOKENS + 1)),           "too-many-tokens"),
    ("This concept has way too many words to be a valid concept name", "too-many-tokens"),

    # ── sentence-shaped (terminating punctuation) ──────────────────────
    ("Self-Determination Theory.",  "sentence-shaped"),
    ("Is this a concept?",          "sentence-shaped"),
    ("Bang!",                       "sentence-shaped"),
]


@pytest.mark.parametrize("name,expected_reason", GARBAGE_CASES, ids=[f"reject:{c[1]}::{c[0]!r}" for c in GARBAGE_CASES])
def test_garbage_rejected_with_correct_reason(name: str, expected_reason: str) -> None:
    """Every garbage fixture is rejected with the documented reason code."""
    valid, reason = is_valid_concept(name)
    assert valid is False, f"expected rejection of {name!r}, got accept"
    assert reason == expected_reason, (
        f"for input {name!r}: expected reason {expected_reason!r}, got {reason!r}"
    )
    assert reason in REASON_CODES, f"emitted unknown reason code {reason!r}"


def test_garbage_count_meets_phase_1_gate() -> None:
    """Spec §5 Phase 1 gate: ≥30 garbage fixtures must be rejected."""
    assert len(GARBAGE_CASES) >= 30, (
        f"phase 1 gate requires ≥30 garbage fixtures; have {len(GARBAGE_CASES)}"
    )


# ════════════════════════════════════════════════════════════════════════════
# Valid fixtures — must all be ACCEPTED
# ════════════════════════════════════════════════════════════════════════════

VALID_CASES: list[str] = [
    # Real concepts pulled from the actual vault corpus
    "Self-Determination Theory",
    "Self-Regulated Learning",
    "Autonomous Motivation",
    "Internalization Continuum",
    "Working Memory",
    "Cognitive Load Theory",
    "Spaced Repetition",
    "Elaborative Encoding",
    "Schema Activation",
    "Deliberate Practice",
    "Andragogy",
    "Heutagogy",
    "Zimmerman SRL Model",
    "Pintrich's Motivational Integration",
    # Variations: hyphenated, apostrophes, ampersands, slashes
    "MOC",                            # 3-char minimum
    "AI/ML",
    "Crick & Watson",
    "First-Principles Thinking",
    "K-12 Education",
    "OECD 2030",
    # Phase 1.5 tuning: author-citation / abbreviation forms with terminal periods
    "Pressley et al.",
    "Chi et al",
    "Oliver Wendell Holmes Jr.",
    "patient H.M.",
    "F.D.R.",
    # Phase 1.5 tuning: legitimate 9–10 token concept titles
    "The Forgetting Curve and the Power of Retrieval Practice",
    "Token Economics and Cost Optimization for Production LLM Systems",
    # Phase 1.5 leak-fix guard: legitimate concepts that LOOK borderline
    # but must NOT trip citation / author-bio patterns.
    "Self-Determination Theory",                          # plain concept
    "Locke and Latham Goal Setting",                      # author-named theory, no year
    "K-12 Education in the United States",                # has 'United States' but no dash/year
    "Pre-1900 Educational Reform",                        # year present but no dash & no surname-comma
]


@pytest.mark.parametrize("name", VALID_CASES, ids=[f"accept::{c!r}" for c in VALID_CASES])
def test_valid_concepts_accepted(name: str) -> None:
    """Every valid fixture is accepted with empty reason."""
    valid, reason = is_valid_concept(name)
    assert valid is True, f"expected accept of {name!r}, got reject ({reason!r})"
    assert reason == ""


def test_valid_count_meets_phase_1_gate() -> None:
    """Spec §5 Phase 1 gate: ≥10 valid concept fixtures must be accepted."""
    assert len(VALID_CASES) >= 10, (
        f"phase 1 gate requires ≥10 valid fixtures; have {len(VALID_CASES)}"
    )


# ════════════════════════════════════════════════════════════════════════════
# API contract tests
# ════════════════════════════════════════════════════════════════════════════

def test_is_garbage_inverts_is_valid_concept() -> None:
    """``is_garbage`` is the boolean negation of ``is_valid_concept[0]``."""
    samples = [c[0] for c in GARBAGE_CASES] + VALID_CASES
    for name in samples:
        valid, _ = is_valid_concept(name)
        assert is_garbage(name) is (not valid), f"contract violation for {name!r}"


def test_rejection_reason_matches_is_valid_concept() -> None:
    """``rejection_reason`` returns the same reason as ``is_valid_concept[1]``."""
    samples = [c[0] for c in GARBAGE_CASES] + VALID_CASES
    for name in samples:
        _, reason = is_valid_concept(name)
        assert rejection_reason(name) == reason


def test_reason_codes_exhaustive() -> None:
    """Every reason code emitted by the fixtures appears in ``REASON_CODES``."""
    emitted = {reason for _, reason in (is_valid_concept(c[0]) for c in GARBAGE_CASES)}
    emitted.discard("")
    unknown = emitted - REASON_CODES
    assert not unknown, f"emitted reason codes not in REASON_CODES: {unknown}"


def test_none_input_rejected_as_empty() -> None:
    """``None`` input is rejected with ``empty`` (defensive guard)."""
    valid, reason = is_valid_concept(None)  # type: ignore[arg-type]
    assert valid is False
    assert reason == "empty"


def test_min_length_boundary() -> None:
    """A name of exactly ``MIN_NAME_LENGTH`` is accepted."""
    name = "x" * MIN_NAME_LENGTH
    # 'xxx' contains no rejection trigger ⇒ accepted
    valid, reason = is_valid_concept(name)
    assert valid is True, f"boundary accept failed: {reason!r}"


def test_max_length_boundary() -> None:
    """A name of exactly ``MAX_NAME_LENGTH`` (single token) is accepted."""
    name = "x" * MAX_NAME_LENGTH
    valid, reason = is_valid_concept(name)
    assert valid is True, f"boundary accept failed: {reason!r}"


def test_max_tokens_boundary() -> None:
    """A name with exactly ``MAX_CONCEPT_TOKENS`` words is accepted."""
    name = " ".join(["word"] * MAX_CONCEPT_TOKENS)
    valid, reason = is_valid_concept(name)
    assert valid is True, f"boundary accept failed: {reason!r}"
