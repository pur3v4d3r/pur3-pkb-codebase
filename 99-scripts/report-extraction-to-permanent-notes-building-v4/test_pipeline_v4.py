#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for pipeline_v4.

Run with:
    pytest test_pipeline_v4.py -v
    pytest test_pipeline_v4.py --cov=pipeline_v4 --cov-report=term-missing

These tests do not require Ollama or pydantic — LLM calls are stubbed and
schema validation is exercised via a thin mock response object.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

import pipeline_v4 as v4


# ═════════════════════════════════════════════════════════════════════════
# Fixtures
# ═════════════════════════════════════════════════════════════════════════

@pytest.fixture
def sample_payload() -> dict:
    """Minimal extractor JSON payload covering the fields V4 reads."""
    return {
        "extraction_metadata": {"source_file": "sample-report.md"},
        "document_metadata": {
            "frontmatter": {
                "title": "Sample Foundational Report on Cognitive Load",
                "aliases": ["CLT Report", "Sample CLT"],
                "primary_domain": "Cognitive Psychology",
                "secondary_domains": ["Educational Psychology"],
                "confidence": "high",
                "related": ["[[working-memory]]", "[[schema-theory]]"],
                "see-also": ["[[chunking]]"],
                "broader": [],
                "narrower": [],
                "prerequisites": [],
            },
        },
        "extracted_items": {
            "callouts": [
                {
                    "type": "definition",
                    "title": "Cognitive Load (Sweller, 1988)",
                    "body": "The total amount of mental effort being used in working memory.",
                },
                {
                    "type": "definition",
                    "title": "Element Interactivity",
                    "body": "The degree to which information elements depend on each other.",
                },
                {
                    "type": "key-claim",
                    "title": "Working memory is severely capacity-limited.",
                    "body": "Holds at most 4±1 chunks for ~20 seconds without rehearsal.",
                },
                {
                    "type": "person",
                    "title": "John Sweller",
                    "body": "Originator of cognitive load theory and element interactivity.",
                },
                {
                    "type": "example",
                    "title": "Worked Example",
                    "body": "Demonstrating cognitive load reduction through worked examples.",
                },
                {
                    "type": "open-question",
                    "title": "Boundary of element interactivity",
                    "body": "Where does element interactivity end and germane load begin?",
                },
            ],
        },
        "knowledge_graph": {
            "unique_wiki_link_targets": [
                "working-memory", "schema-theory", "chunking", "germane-load",
            ],
        },
    }


@pytest.fixture
def sample_json_file(tmp_path: Path, sample_payload: dict) -> Path:
    p = tmp_path / "sample-report-2026-04-21_extracted.json"
    p.write_text(json.dumps(sample_payload), encoding="utf-8")
    return p


@dataclass
class _FakeResponse:
    definition: str = "Mocked definition of the concept."
    core_explanation: list[str] = None
    practical_implications: list[str] = None
    key_figures: list[str] = None
    related_concepts: list[str] = None
    tensions_or_questions: list[str] = None
    key_distinctions: list[str] = None

    def __post_init__(self) -> None:
        if self.core_explanation is None:
            self.core_explanation = ["Para A.", "Para B."]
        if self.practical_implications is None:
            self.practical_implications = ["Implication X."]
        if self.key_figures is None:
            self.key_figures = ["Some Person — role"]
        if self.related_concepts is None:
            self.related_concepts = ["Working Memory", "Schema"]
        if self.tensions_or_questions is None:
            self.tensions_or_questions = []
        if self.key_distinctions is None:
            self.key_distinctions = []


# ═════════════════════════════════════════════════════════════════════════
# Title cleaning
# ═════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("raw,expected", [
    ("Cognitive Load (Sweller, 1988)", "Cognitive Load"),
    ("Self-Determination Theory", "Self-Determination Theory"),
    ("Element Interactivity — a sub-mechanism", "Element Interactivity"),
    ("[[Schema Theory]]", "Schema Theory"),
    ("  Spaced Practice  ", "Spaced Practice"),
    ("", ""),
])
def test_clean_title(raw, expected):
    assert v4._clean_title(raw) == expected


@pytest.mark.parametrize("title,ok", [
    ("Cognitive Load", True),
    ("X", False),                      # too short
    ("a" * 90, False),                 # too long
    ("This title has way too many words to be a real concept name", False),
    ("Self-Determination Theory", True),
])
def test_is_usable_title(title, ok):
    assert v4._is_usable_title(title) is ok


# ═════════════════════════════════════════════════════════════════════════
# Concept mining
# ═════════════════════════════════════════════════════════════════════════

def test_mine_concepts_definitions_only(sample_payload):
    concepts = v4.mine_concepts(sample_payload, include_key_claims=False)
    titles = [v4._clean_title(co["title"]) for _, co in concepts]
    assert "Cognitive Load" in titles
    assert "Element Interactivity" in titles
    # Key-claim title should NOT be present
    assert not any("capacity-limited" in t.lower() for t in titles)


def test_mine_concepts_with_key_claims(sample_payload):
    concepts = v4.mine_concepts(sample_payload, include_key_claims=True)
    types = [t for t, _ in concepts]
    assert "key-claim" in types or "definition" in types
    # Definition should not be displaced by a key-claim with the same title
    titles = {v4._clean_title(co["title"]).lower() for _, co in concepts}
    assert "cognitive load" in titles


def test_mine_concepts_dedupes(sample_payload):
    payload = dict(sample_payload)
    payload["extracted_items"]["callouts"] = (
        sample_payload["extracted_items"]["callouts"] * 2
    )
    concepts = v4.mine_concepts(payload, include_key_claims=False)
    titles = [v4._clean_title(co["title"]).lower() for _, co in concepts]
    assert len(titles) == len(set(titles))


# ═════════════════════════════════════════════════════════════════════════
# Bundle construction
# ═════════════════════════════════════════════════════════════════════════

def test_build_bundles_populates_support(sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample-report-2026-04-21",
        include_key_claims=False,
    )
    assert bundles, "expected at least one bundle"
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    assert cl.domain == "cognitive-psychology"
    assert "working-memory" in cl.related_links
    # Support callouts should mention Cognitive Load
    assert any("cognitive load" in (sc.title + sc.body).lower() for sc in cl.support)


def test_filename_stem_is_kebab(sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample", include_key_claims=False,
    )
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    assert cl.filename_stem == "cognitive-load"


# ═════════════════════════════════════════════════════════════════════════
# Rendering
# ═════════════════════════════════════════════════════════════════════════

def test_render_note_contains_definition_callout(sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample", include_key_claims=False,
    )
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    note = v4.render_note(cl, _FakeResponse(), today=__import__("datetime").date(2026, 4, 23))
    assert "> [!definition]" in note
    assert "**Cognitive Load**" in note
    assert "## Core Explanation" in note
    assert "## Practical Implications" in note
    assert "## Connections & Context" in note
    assert "[[sample]]" in note
    # Frontmatter sanity
    assert note.startswith("---\n")
    assert "title: \"Cognitive Load\"" in note
    assert "status: enriched" in note


def test_render_note_handles_empty_optional_sections(sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample", include_key_claims=False,
    )
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    rsp = _FakeResponse(
        key_figures=[], practical_implications=[],
        tensions_or_questions=[], key_distinctions=[],
    )
    note = v4.render_note(cl, rsp, today=__import__("datetime").date(2026, 4, 23))
    assert "## Key Figures" not in note
    assert "## Practical Implications" not in note
    assert "## Open Threads" not in note


# ═════════════════════════════════════════════════════════════════════════
# I/O
# ═════════════════════════════════════════════════════════════════════════

def test_load_payload_round_trip(sample_json_file, sample_payload):
    loaded = v4.load_payload(sample_json_file)
    assert loaded["document_metadata"] == sample_payload["document_metadata"]


def test_load_payload_rejects_non_object(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("[1,2,3]", encoding="utf-8")
    with pytest.raises(ValueError, match="not an object"):
        v4.load_payload(p)


def test_discover_jsons_filters(tmp_path, sample_payload):
    (tmp_path / "alpha-foo_extracted.json").write_text(json.dumps(sample_payload))
    (tmp_path / "beta-bar_extracted.json").write_text(json.dumps(sample_payload))
    (tmp_path / "ignore.json").write_text("{}")
    all_paths = v4.discover_jsons(tmp_path, report_filter=None)
    assert len(all_paths) == 2
    filtered = v4.discover_jsons(tmp_path, report_filter="alpha")
    assert len(filtered) == 1 and "alpha" in filtered[0].name


def test_discover_jsons_missing_dir_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        v4.discover_jsons(tmp_path / "nope", report_filter=None)


def test_write_atomic_creates_parent_and_file(tmp_path):
    target = tmp_path / "subdir" / "out.md"
    v4.write_atomic(target, "hello\n")
    assert target.read_text(encoding="utf-8") == "hello\n"


def test_existing_status_reads_yaml(tmp_path):
    p = tmp_path / "existing.md"
    p.write_text("---\ntitle: \"x\"\nstatus: enriched\n---\nbody\n", encoding="utf-8")
    assert v4.existing_status(p) == "enriched"


def test_existing_status_missing_file_returns_none(tmp_path):
    assert v4.existing_status(tmp_path / "nope.md") is None


def test_resolve_destination_skip_when_exists(tmp_path, sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample", include_key_claims=False,
    )
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    out = tmp_path / "out"
    out.mkdir()
    (out / "cognitive-load.md").write_text("---\nstatus: stub\n---\n", encoding="utf-8")
    dest, reason = v4.resolve_destination(cl, out, mode="skip")
    assert reason and "exists" in reason


def test_resolve_destination_overwrite(tmp_path, sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample", include_key_claims=False,
    )
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    out = tmp_path / "out"
    out.mkdir()
    (out / "cognitive-load.md").write_text("---\nstatus: enriched\n---\n", encoding="utf-8")
    dest, reason = v4.resolve_destination(cl, out, mode="overwrite")
    assert reason is None


def test_resolve_destination_merge_skips_enriched(tmp_path, sample_payload):
    bundles = v4.build_bundles(
        sample_payload, report_stem="sample", include_key_claims=False,
    )
    cl = next(b for b in bundles if b.title == "Cognitive Load")
    out = tmp_path / "out"
    out.mkdir()
    (out / "cognitive-load.md").write_text("---\nstatus: enriched\n---\n", encoding="utf-8")
    dest, reason = v4.resolve_destination(cl, out, mode="merge")
    assert reason and "enriched" in reason


# ═════════════════════════════════════════════════════════════════════════
# CLI integration (no Ollama)
# ═════════════════════════════════════════════════════════════════════════

def test_cli_help_lists_all_modes(capsys):
    parser = v4.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])
    out = capsys.readouterr().out
    for flag in ("--dry-run", "--bypass-cache", "--include-key-claims",
                 "--mode", "--strict", "--limit", "--report",
                 "--input-dir", "--output-dir"):
        assert flag in out


def test_main_returns_2_on_missing_input_dir(tmp_path, monkeypatch):
    rc = v4.main(["--input-dir", str(tmp_path / "does-not-exist")])
    assert rc == 2


def test_main_returns_4_when_no_jsons(tmp_path):
    rc = v4.main(["--input-dir", str(tmp_path)])
    assert rc == 4


def test_dry_run_writes_no_files(tmp_path, sample_json_file, monkeypatch):
    """End-to-end dry-run with the LLM client fully mocked."""
    output_dir = tmp_path / "out"

    fake_client = MagicMock()
    fake_client.__enter__ = MagicMock(return_value=fake_client)
    fake_client.__exit__ = MagicMock(return_value=False)
    fake_client.chat_json = MagicMock(return_value=SimpleNamespace(
        parsed=_FakeResponse(),
        cached=False,
        raw_text="{}",
        model="mock",
        cache_key="abc",
    ))

    monkeypatch.setattr(v4, "OllamaClient", lambda **kw: fake_client)

    rc = v4.main([
        "--input-dir", str(sample_json_file.parent),
        "--output-dir", str(output_dir),
        "--dry-run", "--limit", "2",
    ])
    assert rc == 0
    # No files written in dry-run
    assert not output_dir.exists() or not any(output_dir.iterdir())
    fake_client.chat_json.assert_called()
