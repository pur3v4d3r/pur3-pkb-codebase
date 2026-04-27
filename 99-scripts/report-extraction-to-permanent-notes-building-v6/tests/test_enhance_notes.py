#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for enhance_notes — section parsing, merge logic, frontmatter update.

Run with:
    pytest tests/test_enhance_notes.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Add the v6 dir to sys.path so we can import the module under test.
_HERE = Path(__file__).resolve().parent
_V6_DIR = _HERE.parent
if str(_V6_DIR) not in sys.path:
    sys.path.insert(0, str(_V6_DIR))

import enhance_notes as en  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────

SAMPLE_BODY = """\
# Schema Theory

> [!definition] **Schema Theory**
> Schema Theory treats long-term knowledge as organized into hierarchical
> slot-and-filler structures.

## Core Explanation

Schema Theory posits that knowledge is organized into schemas. These
schemas guide perception and recall.

## Practical Implications

> [!example] **Application 1 — Worked examples**
> Worked examples reduce extraneous load.

> [!example] **Application 2 — Scaffolded fading**
> Faded scaffolds support transfer.

## Connections & Context

**Falls under:** [[cognitive-architecture]]
"""


SAMPLE_FRONTMATTER = {
    "title": "Schema Theory",
    "domain": "cognitive-psychology",
    "parent-concept": "Cognitive Architecture",
    "aliases": ["Schema Theory"],
    "maturity-stage": "budding",
    "depth-level": "elaborated",
    "provenance": {"pipeline-version": "v6.0.0"},
}


@pytest.fixture
def sample_response() -> en.EnhancementResponse:
    return en.EnhancementResponse(
        extra_explanation_paragraphs=[
            "Schemas operate over multiple timescales — perception in milliseconds, "
            "comprehension in seconds, expertise in years. The unifying claim is "
            "that all of these depend on prior structure being available for binding "
            "incoming elements.",
        ],
        mechanism_addition=(
            "Element interactivity is the engine: as elements bind into chunks, "
            "working-memory load collapses and processing shifts from controlled "
            "to automatic."
        ),
        extra_implications=[
            en._Implication(
                scenario="Reading comprehension",
                body=(
                    "When learners lack the relevant schema, even fluent decoding "
                    "fails to produce comprehension because there is nothing into "
                    "which the textual elements can be assimilated."
                ),
            ),
        ],
        extra_distinctions=[
            en._Distinction(
                title="Schema vs Mental Model",
                body=(
                    "Schemas are stable, retrieval-oriented structures. Mental "
                    "models are constructed on the fly to simulate a specific situation."
                ),
            ),
        ],
        extra_figures=[
            en._Figure(
                name="Frederic Bartlett",
                contribution=(
                    "Bartlett's 1932 'Remembering' introduced the schema construct "
                    "to memory research via the War of the Ghosts study."
                ),
            ),
        ],
        extra_questions=[
            en._Question(
                question="How are schemas neurally instantiated?",
                resolution="Convergent fMRI/lesion evidence on hippocampal-cortical binding could resolve this.",
            ),
        ],
        synthesis_addition=(
            "Schema Theory remains the bridge between memory research and "
            "instructional design — it is the construct that lets cognitive "
            "load theory and expertise research speak to one another."
        ),
        evidence_addition=(
            "Meta-analyses of worked-example research consistently report "
            "moderate-to-large effects (d ≈ 0.5–0.8) on transfer for novices, "
            "with the effect attenuating as expertise develops."
        ),
    )


# ─────────────────────────────────────────────────────────────────────────
# Section parsing
# ─────────────────────────────────────────────────────────────────────────

def test_split_sections_extracts_h2_blocks() -> None:
    preamble, sections = en._split_sections(SAMPLE_BODY)
    assert preamble.startswith("# Schema Theory")
    assert "Core Explanation" in sections
    assert "Practical Implications" in sections
    assert "Connections & Context" in sections
    assert "Schema Theory posits" in sections["Core Explanation"]


def test_split_sections_handles_no_headers() -> None:
    body = "Just a paragraph with no h2 headers at all."
    preamble, sections = en._split_sections(body)
    assert preamble == body
    assert sections == {}


def test_reassemble_uses_canonical_order() -> None:
    sections = {
        "Practical Implications": "imp body",
        "Core Explanation": "core body",
        "Mechanism": "mech body",
    }
    out = en._reassemble("# Title\n", sections)
    # Core Explanation must come before Mechanism, which must come before Practical Implications
    assert out.index("## Core Explanation") < out.index("## Mechanism")
    assert out.index("## Mechanism") < out.index("## Practical Implications")


def test_reassemble_preserves_unknown_sections() -> None:
    sections = {"Core Explanation": "x", "Custom Section": "y"}
    out = en._reassemble("# T\n", sections)
    assert "## Custom Section" in out
    assert out.index("## Core Explanation") < out.index("## Custom Section")


# ─────────────────────────────────────────────────────────────────────────
# Append helpers
# ─────────────────────────────────────────────────────────────────────────

def test_append_paragraphs_marks_pass() -> None:
    sections = {"Core Explanation": "original"}
    changed = en._append_paragraphs(
        sections, "Core Explanation", ["new paragraph"], pass_n=2, today="2026-04-27",
    )
    assert changed
    assert "enhancement-pass:2" in sections["Core Explanation"]
    assert "original" in sections["Core Explanation"]
    assert "new paragraph" in sections["Core Explanation"]


def test_append_paragraphs_creates_missing_section() -> None:
    sections: dict[str, str] = {}
    changed = en._append_paragraphs(
        sections, "Mechanism", ["mech text"], pass_n=1, today="2026-04-27",
    )
    assert changed
    assert "Mechanism" in sections
    assert "mech text" in sections["Mechanism"]


def test_append_paragraphs_skips_blank_input() -> None:
    sections = {"Core Explanation": "original"}
    changed = en._append_paragraphs(
        sections, "Core Explanation", ["", "   "], pass_n=1, today="2026-04-27",
    )
    assert not changed
    assert sections["Core Explanation"] == "original"


def test_append_implications_continues_numbering() -> None:
    sections = {"Practical Implications": "> [!example] **Application 1 — X**\n> body"}
    items = [en._Implication(scenario="New Y", body="A new application body that is long enough.")]
    changed = en._append_implications(
        sections, items, existing_count=1, pass_n=2, today="2026-04-27",
    )
    assert changed
    assert "Application 2" in sections["Practical Implications"]


def test_append_distinctions_uses_callout_type() -> None:
    sections: dict[str, str] = {}
    items = [en._Distinction(
        title="A vs B",
        body="A body that is comfortably longer than the validator's minimum.",
    )]
    en._append_distinctions(sections, items, pass_n=1, today="2026-04-27")
    assert "[!key-distinction]" in sections["Key Distinctions"]
    assert "**A vs B**" in sections["Key Distinctions"]


def test_append_questions_includes_resolution_when_present() -> None:
    sections: dict[str, str] = {}
    items = [en._Question(
        question="Is X true under condition Y?",
        resolution="A within-subjects replication would clarify it.",
    )]
    en._append_questions(sections, items, pass_n=1, today="2026-04-27")
    assert "What would resolve it" in sections["Open Questions"]


# ─────────────────────────────────────────────────────────────────────────
# Schema validation
# ─────────────────────────────────────────────────────────────────────────

def test_enhancement_response_is_empty_detects_no_content() -> None:
    rsp = en.EnhancementResponse()
    assert rsp.is_empty()


def test_enhancement_response_is_empty_returns_false_with_paragraph() -> None:
    rsp = en.EnhancementResponse(extra_explanation_paragraphs=["something"])
    assert not rsp.is_empty()


def test_enhancement_response_strips_blank_paragraphs() -> None:
    rsp = en.EnhancementResponse(
        extra_explanation_paragraphs=["", "  ", "real content"],
    )
    assert rsp.extra_explanation_paragraphs == ["real content"]


# ─────────────────────────────────────────────────────────────────────────
# Frontmatter update
# ─────────────────────────────────────────────────────────────────────────

def test_update_frontmatter_writes_provenance() -> None:
    out = en.update_frontmatter(
        SAMPLE_FRONTMATTER, pass_n=1, model="qwen3:30b", today="2026-04-27",
    )
    assert out["updated"] == "2026-04-27"
    assert out["depth-level"] == "enhanced"
    prov = out["provenance"]
    assert prov["enhancement-passes"] == 1
    assert prov["enhancement-model"] == "qwen3:30b"
    assert prov["enhancement-method"] == "enhance_notes-v1"
    # Existing provenance preserved
    assert prov["pipeline-version"] == "v6.0.0"


def test_update_frontmatter_promotes_maturity_after_pass_2() -> None:
    out = en.update_frontmatter(
        SAMPLE_FRONTMATTER, pass_n=2, model="qwen3:30b", today="2026-04-27",
    )
    assert out["maturity-stage"] == "evergreen"


def test_update_frontmatter_does_not_promote_on_pass_1() -> None:
    out = en.update_frontmatter(
        SAMPLE_FRONTMATTER, pass_n=1, model="qwen3:30b", today="2026-04-27",
    )
    assert out["maturity-stage"] == "budding"


def test_update_frontmatter_preserves_user_fields() -> None:
    fm = dict(SAMPLE_FRONTMATTER)
    fm["status"] = "active"
    fm["tags"] = ["custom-tag"]
    fm["importance"] = "high"
    out = en.update_frontmatter(fm, pass_n=1, model="qwen3:30b", today="2026-04-27")
    assert out["status"] == "active"
    assert out["tags"] == ["custom-tag"]
    assert out["importance"] == "high"


# ─────────────────────────────────────────────────────────────────────────
# Full merge flow
# ─────────────────────────────────────────────────────────────────────────

def test_merge_response_appends_all_sections(sample_response: en.EnhancementResponse) -> None:
    note = en.V6Note(
        path=Path("/tmp/schema-theory.md"),
        title="Schema Theory",
        domain="cognitive-psychology",
        parent_concept="Cognitive Architecture",
        aliases=["Schema Theory"],
        frontmatter=SAMPLE_FRONTMATTER,
        body=SAMPLE_BODY,
        sections=en._split_sections(SAMPLE_BODY)[1],
        enhancement_passes=0,
    )
    preamble, sections = en.merge_response(
        note, sample_response, pass_n=1, today="2026-04-27",
    )
    body = en._reassemble(preamble, sections)
    # Preserved
    assert "Schema Theory posits" in body
    assert "Application 1 — Worked examples" in body
    # New material
    assert "Schemas operate over multiple timescales" in body
    assert "Element interactivity is the engine" in body
    assert "Application 3 — Reading comprehension" in body
    assert "Schema vs Mental Model" in body
    assert "Frederic Bartlett" in body
    assert "neurally instantiated" in body
    assert "bridge between memory research" in body
    assert "Meta-analyses of worked-example" in body
    # Marker present
    assert "enhancement-pass:1" in body


def test_merge_response_creates_missing_mechanism_section(
    sample_response: en.EnhancementResponse,
) -> None:
    note = en.V6Note(
        path=Path("/tmp/x.md"),
        title="X", domain="d", parent_concept="P", aliases=[],
        frontmatter=SAMPLE_FRONTMATTER, body=SAMPLE_BODY,
        sections=en._split_sections(SAMPLE_BODY)[1],
        enhancement_passes=0,
    )
    assert "Mechanism" not in note.sections
    _, sections = en.merge_response(note, sample_response, pass_n=1, today="2026-04-27")
    assert "Mechanism" in sections


# ─────────────────────────────────────────────────────────────────────────
# Body-hash determinism
# ─────────────────────────────────────────────────────────────────────────

def test_body_hash_is_deterministic() -> None:
    h1 = en._body_hash("hello world")
    h2 = en._body_hash("hello world")
    h3 = en._body_hash("hello world!")
    assert h1 == h2
    assert h1 != h3
    assert len(h1) == 16


# ─────────────────────────────────────────────────────────────────────────
# CLI smoke tests
# ─────────────────────────────────────────────────────────────────────────

def test_cli_help_runs(capsys: pytest.CaptureFixture[str]) -> None:
    parser = en.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])
    out = capsys.readouterr().out
    assert "--dry-run" in out
    assert "--max-passes" in out
    assert "--re-enhance" in out
    assert "qwen3:30b" in out
