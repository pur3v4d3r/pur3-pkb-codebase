#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for v6lib.renderer — section composition, callout rendering, ordering.

Run with:
    pytest 99-scripts/report-extraction-to-permanent-notes-building-v6/tests/test_renderer.py -v
"""
from __future__ import annotations

import datetime as dt
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pytest

# Make V6 + V3 + V4 importable regardless of cwd.
_HERE = Path(__file__).resolve().parent
_V6 = _HERE.parent
_SCRIPTS = _V6.parent
_V3 = _SCRIPTS / "report-extraction-to-permanent-notes-building-v3"
_V4 = _SCRIPTS / "report-extraction-to-permanent-notes-building-v4"
for p in (_V3, _V4, _V6):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from v6lib import renderer  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────
# Minimal stand-in objects (avoid pulling pydantic into rendering tests)
# ─────────────────────────────────────────────────────────────────────────

@dataclass
class FakeBundle:
    title: str = "Self-Determination Theory"
    filename_stem: str = "self-determination-theory"
    raw_title: str = "Self-Determination Theory"
    domain: str = "psychology"
    subdomains: list[str] = field(default_factory=lambda: ["motivation"])
    aliases: list[str] = field(default_factory=lambda: ["SDT"])
    related_links: list[str] = field(default_factory=list)
    report_title: str = "SDT Foundational Report"
    report_stem: str = "self-determination-theory-foundational"
    confidence: str = "high"


@dataclass
class FakeRC:
    concept: str
    relation: str
    rationale: str = ""


@dataclass
class FakeKF:
    name: str
    role: str = ""


@dataclass
class FakeKFContrib:
    name: str
    contribution: str = ""


@dataclass
class FakeSection:
    section: str
    intent: str = ""
    source_hooks: list[str] = field(default_factory=list)


@dataclass
class FakeOutline:
    canonical_title: str = "Self-Determination Theory"
    seed_definition: str = "A macro-theory of human motivation."
    definition_boundary: str = "Distinct from extrinsic-only frameworks."
    parent_concept: str = "Motivation Theory"
    domain_hint: str = "psychology"
    section_outline: list[FakeSection] = field(default_factory=list)
    related_concepts: list[FakeRC] = field(default_factory=list)
    key_figures: list[FakeKF] = field(default_factory=list)
    open_questions_seed: list[str] = field(default_factory=list)
    key_distinctions_seed: list[str] = field(default_factory=list)
    worthy: bool = True
    worthy_reason: str = ""


@dataclass
class FakeImpl:
    scenario: str
    body: str


@dataclass
class FakeDist:
    contrast: str
    body: str


@dataclass
class FakeOQ:
    question: str
    what_would_resolve_it: str = ""


@dataclass
class FakeElab:
    elaborated_definition: str = ""
    core_explanation_paragraphs: list[str] = field(default_factory=list)
    mechanism_paragraphs: list[str] = field(default_factory=list)
    practical_implications: list[FakeImpl] = field(default_factory=list)
    key_distinctions: list[FakeDist] = field(default_factory=list)
    key_figures: list[FakeKFContrib] = field(default_factory=list)
    open_questions: list[FakeOQ] = field(default_factory=list)
    synthesis_paragraphs: list[str] = field(default_factory=list)
    evidence_narrative: str = ""


# ─────────────────────────────────────────────────────────────────────────
# Definition callout
# ─────────────────────────────────────────────────────────────────────────

def test_definition_callout_appends_falls_under_when_missing():
    out = renderer.render_definition_callout(
        title="SDT",
        elaborated_definition="A macro-theory of human motivation.",
        parent="Motivation Theory",
    )
    assert "[!definition]" in out
    assert "**SDT**" in out
    assert "[[Motivation Theory]]" in out
    assert "Falls under" in out or "falls under" in out


def test_definition_callout_does_not_duplicate_parent_reference():
    body = ("A macro-theory of human motivation. It falls under "
            "[[Motivation Theory]] and emphasizes three needs.")
    out = renderer.render_definition_callout(
        title="SDT", elaborated_definition=body, parent="Motivation Theory",
    )
    assert out.count("[[Motivation Theory]]") == 1


# ─────────────────────────────────────────────────────────────────────────
# Section renderers
# ─────────────────────────────────────────────────────────────────────────

def test_render_implications_emits_callouts():
    out = "\n".join(renderer.render_implications([
        FakeImpl("Classroom autonomy", "Long body text describing the use case."),
        FakeImpl("Workplace", "Another scenario with sufficient detail."),
    ]))
    assert "## Practical Implications" in out
    assert "[!example]" in out
    assert "Application 1 — Classroom autonomy" in out
    assert "Application 2 — Workplace" in out


def test_render_distinctions_emits_callouts():
    out = "\n".join(renderer.render_distinctions([
        FakeDist("SDT vs. behaviorism", "Body explaining the contrast."),
    ]))
    assert "[!key-distinction]" in out
    assert "**SDT vs. behaviorism**" in out


def test_render_figures_emits_bullets():
    out = "\n".join(renderer.render_figures([
        FakeKFContrib("Edward Deci", "Co-founded the theory."),
        FakeKFContrib("Richard Ryan"),
    ]))
    assert "## Key Figures" in out
    assert "- **Edward Deci** — Co-founded the theory." in out
    assert "- **Richard Ryan**" in out


def test_render_open_questions_includes_resolution_hint():
    out = "\n".join(renderer.render_open_questions([
        FakeOQ("How does culture mediate?",
               "Cross-cultural longitudinal studies."),
    ]))
    assert "[!open-question]" in out
    assert "How does culture mediate?" in out
    assert "Cross-cultural longitudinal studies." in out


def test_empty_sections_render_to_nothing():
    assert renderer.render_implications([]) == []
    assert renderer.render_distinctions([]) == []
    assert renderer.render_figures([]) == []
    assert renderer.render_open_questions([]) == []


# ─────────────────────────────────────────────────────────────────────────
# Connections
# ─────────────────────────────────────────────────────────────────────────

def test_render_connections_groups_by_relation_in_canonical_order():
    bundle = FakeBundle()
    outline = FakeOutline(
        related_concepts=[
            FakeRC("Behaviorism", "contrasts-with"),
            FakeRC("Intrinsic Motivation", "sibling"),
            FakeRC("Cognitive Evaluation Theory", "specializes"),
            FakeRC("Motivation Research", "applies-to"),
        ],
    )
    out = "\n".join(renderer.render_connections(bundle, outline))
    assert "Falls under:** [[Motivation Theory]]" in out
    # Order check: Specializes appears before Sibling, before Contrasts with,
    # before Applies to (per CONNECTION_ORDER).
    spec_idx = out.find("Specializes:")
    sib_idx = out.find("Sibling concepts:")
    contr_idx = out.find("Contrasts with:")
    appl_idx = out.find("Applies to:")
    assert -1 < spec_idx < sib_idx < contr_idx < appl_idx
    assert "[[Behaviorism]]" in out
    assert f"[[{bundle.report_stem}]]" in out


# ─────────────────────────────────────────────────────────────────────────
# Full-note assembly
# ─────────────────────────────────────────────────────────────────────────

def test_render_note_section_ordering_and_frontmatter():
    bundle = FakeBundle()
    outline = FakeOutline(
        related_concepts=[FakeRC("Intrinsic Motivation", "sibling")],
    )
    elab = FakeElab(
        elaborated_definition="SDT is a macro-theory grounded in three needs.",
        core_explanation_paragraphs=[
            "Para 1 establishing the framework.",
            "Para 2 deepening the explanation.",
        ],
        mechanism_paragraphs=["Mechanism para describing OIT."],
        practical_implications=[
            FakeImpl("Classroom", "Long enough body to count as content."),
        ],
        key_distinctions=[FakeDist("SDT vs. CBT", "A real contrast.")],
        key_figures=[FakeKFContrib("Edward Deci", "Co-founder.")],
        open_questions=[FakeOQ("Cultural mediation?", "Studies needed.")],
        synthesis_paragraphs=["Synthesis paragraph."],
        evidence_narrative="A narrative summary of the evidence base.",
    )
    text = renderer.render_note(
        bundle, outline, elab,
        today=dt.date(2026, 4, 23),
        outline_contract="v6-outline-v1",
        elaborate_contract="v6-elaborate-v1",
    )
    # Frontmatter
    assert text.startswith("---\n")
    assert "title: \"Self-Determination Theory\"" in text
    assert "type: permanent-note" in text
    assert "status: enriched" in text
    assert "v6-llm-elaborated" in text
    assert "outline-contract: \"v6-outline-v1\"" in text
    assert "elaborate-contract: \"v6-elaborate-v1\"" in text
    assert "parent-concept: \"Motivation Theory\"" in text

    # Body section ordering
    h1 = text.find("# Self-Determination Theory")
    h_def = text.find("[!definition]")
    h_core = text.find("## Core Explanation")
    h_mech = text.find("## Mechanism")
    h_impl = text.find("## Practical Implications")
    h_dist = text.find("## Key Distinctions")
    h_fig = text.find("## Key Figures")
    h_oq = text.find("## Open Questions")
    h_syn = text.find("## Synthesis")
    h_evi = text.find("## Evidence")
    h_conn = text.find("## Connections & Context")

    indices = [h1, h_def, h_core, h_mech, h_impl, h_dist, h_fig,
               h_oq, h_syn, h_evi, h_conn]
    assert all(i != -1 for i in indices), \
        f"missing section: {indices}"
    assert indices == sorted(indices), \
        f"sections out of order: {indices}"


def test_render_note_omits_empty_sections():
    bundle = FakeBundle()
    outline = FakeOutline()  # no related concepts
    elab = FakeElab(
        elaborated_definition="A short definition.",
        core_explanation_paragraphs=["Just one paragraph."],
    )
    text = renderer.render_note(
        bundle, outline, elab,
        today=dt.date(2026, 4, 23),
        outline_contract="v6-outline-v1",
        elaborate_contract="v6-elaborate-v1",
    )
    assert "## Mechanism" not in text
    assert "## Practical Implications" not in text
    assert "## Key Distinctions" not in text
    assert "## Key Figures" not in text
    assert "## Open Questions" not in text
    assert "## Synthesis" not in text
    assert "## Evidence" not in text
    # Connections section is always emitted (for source backlink + parent)
    assert "## Connections & Context" in text
    assert f"[[{bundle.report_stem}]]" in text


# ─────────────────────────────────────────────────────────────────────────
# harvest_wikilinks
# ─────────────────────────────────────────────────────────────────────────

def test_harvest_wikilinks_dedup_and_strip_aliases():
    text = ("See [[Foo]] and [[Bar|alias]] and [[Foo]] again, also "
            "[[Baz#section]] for context.")
    out = renderer.harvest_wikilinks(text)
    assert out == ["Foo", "Bar", "Baz"]
