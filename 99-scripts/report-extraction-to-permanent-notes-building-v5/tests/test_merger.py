#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for lib/merger.py — focuses on logic without real LLM calls."""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pytest

from v5lib.matcher import MatchResult
from v5lib.merger import (
    Merger,
    harvest_wikilinks,
    make_backup,
    parse_existing,
    resolve_status,
)


# ─── unit helpers ───────────────────────────────────────────────────────

def test_harvest_wikilinks_dedupes_and_preserves_order() -> None:
    body = "See [[Foo]] then [[Bar|alt]] and again [[Foo]] plus [[Baz]]."
    assert harvest_wikilinks(body) == ["Foo", "Bar", "Baz"]


def test_harvest_wikilinks_empty() -> None:
    assert harvest_wikilinks("") == []
    assert harvest_wikilinks("no links here") == []


@pytest.mark.parametrize("existing,rec,expected", [
    ("seedling", "promote_to_enriched", "enriched"),
    ("stub",     "promote_to_enriched", "enriched"),
    ("enriched", "promote_to_enriched", "enriched"),
    ("budding",  "promote_to_enriched", "budding"),    # never demote-to-enriched
    ("evergreen","promote_to_enriched", "evergreen"),
    ("seedling", "keep",                "seedling"),
    ("",         "keep",                "enriched"),   # empty → safe default
])
def test_resolve_status(existing: str, rec: str, expected: str) -> None:
    assert resolve_status(existing, rec) == expected


def test_parse_existing_with_frontmatter(tmp_path: Path) -> None:
    p = tmp_path / "n.md"
    p.write_text(
        "---\n"
        'title: "X"\n'
        "status: budding\n"
        "---\n"
        "# Body\n",
        encoding="utf-8",
    )
    fm, body = parse_existing(p)
    assert fm["status"] == "budding"
    assert body.startswith("# Body")


def test_parse_existing_no_frontmatter(tmp_path: Path) -> None:
    p = tmp_path / "n.md"
    p.write_text("just a body, no frontmatter\n", encoding="utf-8")
    fm, body = parse_existing(p)
    assert fm == {}
    assert body == "just a body, no frontmatter\n"


def test_make_backup_creates_sibling(tmp_path: Path) -> None:
    p = tmp_path / "n.md"
    p.write_text("hello", encoding="utf-8")
    when = dt.datetime(2026, 4, 23, 10, 30, 5)
    bak = make_backup(p, when=when)
    assert bak.exists()
    assert bak.read_text(encoding="utf-8") == "hello"
    assert ".bak.20260423-103005" in bak.name


# ─── full merge path with mock LLM ──────────────────────────────────────

@dataclass
class _MockLLMResponse:
    parsed: Any
    cached: bool = False


@dataclass
class _MockResponseObj:
    """Stand-in for MergeResponse pydantic instance."""
    merged_definition: str = "Updated definition that is at least 20 characters long."
    merged_explanation: list[str] = field(default_factory=lambda: ["Para 1.", "Para 2."])
    preserved_sections: list[str] = field(default_factory=list)
    new_content_summary: list[str] = field(default_factory=lambda: ["new bullet"])
    preserved_wikilinks: list[str] = field(default_factory=lambda: ["Existing-Link"])
    new_wikilinks: list[str] = field(default_factory=lambda: ["Fresh-Link"])
    change_summary: str = "Added new perspective."
    status_recommendation: str = "keep"
    tensions_introduced: list[str] = field(default_factory=list)
    related_concepts: list[str] = field(default_factory=list)
    practical_implications: list[str] = field(default_factory=list)
    key_distinctions: list[str] = field(default_factory=list)
    key_figures: list[str] = field(default_factory=list)
    tensions_or_questions: list[str] = field(default_factory=list)


@dataclass
class _MockClient:
    """Minimal OllamaClient stand-in. Records last call for inspection."""
    response: Any = None
    cached: bool = False
    last_call: dict[str, Any] = field(default_factory=dict)
    raise_exc: Exception | None = None

    def chat_json(self, **kw: Any) -> Any:
        if self.raise_exc:
            raise self.raise_exc
        self.last_call = kw
        return _MockLLMResponse(parsed=self.response, cached=self.cached)


@dataclass
class _Bundle:
    """Stand-in for V4 ConceptBundle."""
    title: str = "Self-Determination Theory"
    filename_stem: str = "self-determination-theory"
    domain: str = "psychology"
    aliases: tuple[str, ...] = ("SDT",)
    definition_body: str = "SDT is a meta-theory of human motivation."
    support: tuple = ()
    report_stem: str = "test-report"


def _existing_note_text() -> str:
    return (
        "---\n"
        'title: "Self-Determination Theory"\n'
        "status: seedling\n"
        'aliases: ["SDT"]\n'
        "created: 2024-01-15\n"
        "mastery-stage: budding\n"
        "importance: high\n"
        "---\n"
        "# Self-Determination Theory\n"
        "Old explanation. See [[Existing-Link]].\n"
    )


def test_merge_protected_status_skips(tmp_path: Path) -> None:
    p = tmp_path / "self-determination-theory.md"
    p.write_text(
        _existing_note_text().replace("status: seedling", "status: evergreen"),
        encoding="utf-8",
    )
    client = _MockClient(response=_MockResponseObj())
    m = Merger(client=client, model="x",
               protect_statuses=frozenset({"evergreen"}), backup=False)
    match = MatchResult(path=p, tier="exact_slug", score=1.0,
                        matched_against="self-determination-theory")
    out = m.merge(bundle=_Bundle(), match=match, today=dt.date(2026, 4, 23))
    assert out.skipped is True
    assert "protected" in out.skipped_reason
    assert client.last_call == {}     # LLM was never called


def test_merge_force_overrides_protection(tmp_path: Path) -> None:
    p = tmp_path / "self-determination-theory.md"
    p.write_text(
        _existing_note_text().replace("status: seedling", "status: evergreen"),
        encoding="utf-8",
    )
    client = _MockClient(response=_MockResponseObj())
    m = Merger(client=client, model="x",
               protect_statuses=frozenset({"evergreen"}),
               force=True, backup=False)
    match = MatchResult(path=p, tier="exact_slug", score=1.0,
                        matched_against="self-determination-theory")
    out = m.merge(bundle=_Bundle(), match=match, today=dt.date(2026, 4, 23))
    assert out.ok is True
    assert out.skipped is False
    assert client.last_call != {}


def test_merge_writes_and_creates_backup(tmp_path: Path) -> None:
    p = tmp_path / "self-determination-theory.md"
    p.write_text(_existing_note_text(), encoding="utf-8")
    original = p.read_text(encoding="utf-8")
    client = _MockClient(response=_MockResponseObj())
    m = Merger(client=client, model="x",
               protect_statuses=frozenset({"evergreen", "budding"}),
               backup=True)
    match = MatchResult(path=p, tier="exact_slug", score=1.0,
                        matched_against="self-determination-theory")
    out = m.merge(bundle=_Bundle(), match=match, today=dt.date(2026, 4, 23))
    assert out.ok is True
    assert out.backup_path is not None
    assert out.backup_path.exists()
    assert out.backup_path.read_text(encoding="utf-8") == original
    new = p.read_text(encoding="utf-8")
    assert "Updated definition" in new
    assert "v5-llm-merged" in new
    # created field preserved
    assert "created: 2024-01-15" in new
    # updated rewritten
    assert "updated: 2026-04-23" in new


def test_merge_dry_run_writes_nothing(tmp_path: Path) -> None:
    p = tmp_path / "self-determination-theory.md"
    p.write_text(_existing_note_text(), encoding="utf-8")
    original = p.read_text(encoding="utf-8")
    client = _MockClient(response=_MockResponseObj())
    m = Merger(client=client, model="x", backup=True)
    match = MatchResult(path=p, tier="exact_slug", score=1.0,
                        matched_against="self-determination-theory")
    out = m.merge(bundle=_Bundle(), match=match,
                  today=dt.date(2026, 4, 23), dry_run=True)
    assert out.ok is True
    assert out.skipped_reason == "dry-run"
    assert out.rendered.strip().startswith("---")
    assert out.backup_path is None
    assert p.read_text(encoding="utf-8") == original   # untouched


def test_merge_status_promotion_seedling_to_enriched(tmp_path: Path) -> None:
    p = tmp_path / "self-determination-theory.md"
    p.write_text(_existing_note_text(), encoding="utf-8")  # status: seedling
    rsp = _MockResponseObj(status_recommendation="promote_to_enriched")
    client = _MockClient(response=rsp)
    m = Merger(client=client, model="x", backup=False)
    match = MatchResult(path=p, tier="exact_slug", score=1.0,
                        matched_against="self-determination-theory")
    out = m.merge(bundle=_Bundle(), match=match, today=dt.date(2026, 4, 23))
    assert out.ok is True
    new = p.read_text(encoding="utf-8")
    assert "status: enriched" in new


def test_merge_propagates_llm_error_as_outcome(tmp_path: Path) -> None:
    p = tmp_path / "self-determination-theory.md"
    p.write_text(_existing_note_text(), encoding="utf-8")
    client = _MockClient(raise_exc=RuntimeError("ollama down"))
    m = Merger(client=client, model="x", backup=False)
    match = MatchResult(path=p, tier="exact_slug", score=1.0,
                        matched_against="self-determination-theory")
    out = m.merge(bundle=_Bundle(), match=match, today=dt.date(2026, 4, 23))
    assert out.ok is False
    assert "ollama down" in out.error
    # File untouched
    assert "Old explanation" in p.read_text(encoding="utf-8")
