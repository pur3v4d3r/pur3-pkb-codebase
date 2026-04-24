#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for v6lib.prompts — schema validation + relation normalization.

Run with:
    pytest 99-scripts/report-extraction-to-permanent-notes-building-v6/tests/test_prompts.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make the V6 dir importable regardless of where pytest is invoked from.
_HERE = Path(__file__).resolve().parent
_V6 = _HERE.parent
if str(_V6) not in sys.path:
    sys.path.insert(0, str(_V6))

from v6lib import prompts  # noqa: E402

pytestmark = pytest.mark.skipif(
    not prompts._PYDANTIC_AVAILABLE,
    reason="pydantic v2 not installed",
)


# ─────────────────────────────────────────────────────────────────────────
# OutlineResponse
# ─────────────────────────────────────────────────────────────────────────

def _minimal_outline_dict() -> dict:
    return {
        "worthy": True,
        "worthy_reason": "Has a clear definition and supporting context.",
        "canonical_title": "Self-Determination Theory",
        "seed_definition": "A macro-theory of human motivation.",
        "definition_boundary": "Distinct from extrinsic-only frameworks.",
        "parent_concept": "Motivation Theory",
        "domain_hint": "psychology",
        "section_outline": [
            {"section": "Core Explanation",
             "intent": "Explain the three needs.",
             "source_hooks": ["autonomy", "competence", "relatedness"]},
        ],
        "related_concepts": [
            {"concept": "Intrinsic Motivation", "relation": "sibling",
             "rationale": "Closely related construct."},
        ],
        "key_figures": [{"name": "Edward Deci", "role": "co-founder"}],
        "open_questions_seed": ["How does culture mediate need satisfaction?"],
        "key_distinctions_seed": ["SDT vs. behaviorism"],
    }


def test_outline_minimal_valid():
    o = prompts.OutlineResponse(**_minimal_outline_dict())
    assert o.worthy is True
    assert o.canonical_title == "Self-Determination Theory"
    assert o.parent_concept == "Motivation Theory"
    assert len(o.section_outline) == 1
    assert o.related_concepts[0].relation == "sibling"


def test_outline_unworthy_path():
    d = _minimal_outline_dict()
    d["worthy"] = False
    d["worthy_reason"] = "Too thin to elaborate meaningfully."
    o = prompts.OutlineResponse(**d)
    assert o.worthy is False
    assert "thin" in o.worthy_reason.lower()


def test_outline_relation_normalization_from_synonyms():
    d = _minimal_outline_dict()
    d["related_concepts"] = [
        {"concept": "Behaviorism", "relation": "contrast", "rationale": "x"},
        {"concept": "Theories of Motivation", "relation": "broader", "rationale": "x"},
        {"concept": "CET", "relation": "narrower", "rationale": "x"},
    ]
    o = prompts.OutlineResponse(**d)
    rels = [rc.relation for rc in o.related_concepts]
    # Synonyms should normalize to canonical relation types.
    assert "contrasts-with" in rels
    assert "generalizes" in rels
    assert "specializes" in rels
    for r in rels:
        assert r in prompts.RELATION_TYPES


def test_outline_unknown_relation_falls_back_to_sibling():
    d = _minimal_outline_dict()
    d["related_concepts"] = [
        {"concept": "Random Concept",
         "relation": "totally-made-up", "rationale": "x"},
    ]
    o = prompts.OutlineResponse(**d)
    assert o.related_concepts[0].relation == "sibling"


def test_outline_coerce_string_to_list():
    """If LLM returns a string for a list field, coerce to single-item list."""
    d = _minimal_outline_dict()
    d["open_questions_seed"] = "How does context shape motivation?"
    d["key_distinctions_seed"] = "SDT vs. behaviorism"
    o = prompts.OutlineResponse(**d)
    assert isinstance(o.open_questions_seed, list)
    assert len(o.open_questions_seed) == 1


# ─────────────────────────────────────────────────────────────────────────
# ElaborateResponse
# ─────────────────────────────────────────────────────────────────────────

def _minimal_elaborate_dict() -> dict:
    return {
        "elaborated_definition": (
            "Self-Determination Theory (SDT) is a macro-theory of human "
            "motivation grounded in three innate psychological needs — "
            "autonomy, competence, and relatedness. It falls under "
            "[[Motivation Theory]]."
        ),
        "core_explanation_paragraphs": [
            "Paragraph one — sets up the framework. " * 5,
            "Paragraph two — develops the needs. " * 5,
            "Paragraph three — discusses internalization. " * 5,
            "Paragraph four — synthesizes implications. " * 5,
        ],
        "mechanism_paragraphs": [
            "Mechanism paragraph describing the OIT continuum. " * 5,
        ],
        "practical_implications": [
            {"scenario": "Classroom autonomy support",
             "body": "Teachers who provide rationale and acknowledge "
                     "perspectives produce more autonomous engagement. " * 4},
        ],
        "key_distinctions": [
            {"contrast": "SDT vs. behaviorism",
             "body": "SDT emphasizes internal regulation; behaviorism "
                     "emphasizes external contingency. " * 3},
        ],
        "key_figures": [
            {"name": "Edward Deci", "contribution": "Co-founded the theory."},
            {"name": "Richard Ryan", "contribution": "Co-developed BPNT."},
        ],
        "open_questions": [
            {"question": "How does culture mediate need satisfaction?",
             "what_would_resolve_it": "Cross-cultural longitudinal studies."},
        ],
        "synthesis_paragraphs": [
            "Synthesis paragraph tying threads together. " * 5,
        ],
        "evidence_narrative": (
            "A robust evidence base across multiple domains supports the "
            "centrality of the three needs. " * 4
        ),
    }


def test_elaborate_minimal_valid():
    e = prompts.ElaborateResponse(**_minimal_elaborate_dict())
    assert e.elaborated_definition.startswith("Self-Determination")
    assert len(e.core_explanation_paragraphs) >= 4
    assert e.practical_implications[0].scenario.startswith("Classroom")
    assert e.key_figures[0].name == "Edward Deci"


def test_elaborate_implication_too_short_raises():
    d = _minimal_elaborate_dict()
    d["practical_implications"] = [
        {"scenario": "x", "body": "Way too short."},
    ]
    with pytest.raises(Exception):  # pydantic ValidationError
        prompts.ElaborateResponse(**d)


# ─────────────────────────────────────────────────────────────────────────
# Prompt builders — sanity smoke
# ─────────────────────────────────────────────────────────────────────────

def test_build_outline_prompt_contains_key_fields():
    user = prompts.build_outline_user_prompt(
        title="Self-Determination Theory",
        report_title="SDT Foundational Report",
        domain="psychology",
        aliases=["SDT"],
        related_links=["motivation"],
        definition_body="A macro-theory of human motivation.",
        support_block="(none)",
    )
    assert "Self-Determination Theory" in user
    assert "psychology" in user
    assert "SDT Foundational Report" in user


def test_build_elaborate_prompt_includes_outline_summary():
    o = prompts.OutlineResponse(**_minimal_outline_dict())
    user = prompts.build_elaborate_user_prompt(
        title="Self-Determination Theory",
        report_title="SDT Report",
        domain="psychology",
        definition_body="A macro-theory.",
        support_block="(none)",
        outline=o,
    )
    assert "Motivation Theory" in user            # parent
    assert "Edward Deci" in user                   # figure
    assert "Core Explanation" in user              # section


def test_build_merge_prompt_references_existing_note():
    user = prompts.build_merge_user_prompt(
        title="SDT",
        slug="self-determination-theory",
        domain="psychology",
        match_tier="exact-slug",
        match_score=1.0,
        existing_body="---\ntitle: SDT\nstatus: enriched\n---\n# SDT\nbody",
        definition_body="A macro-theory of human motivation.",
        support_block="(none)",
        existing_wikilinks=["Motivation Theory", "Intrinsic Motivation"],
    )
    assert "SDT" in user
    assert "psychology" in user
    assert "exact-slug" in user
    assert "Motivation Theory" in user           # preserved-wikilinks fed in
    assert "macro-theory" in user                 # new definition body
