#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for stages.s7_stubs — hardened stub generation."""
from __future__ import annotations

from pathlib import Path

import pytest

from stages import s7_stubs


def _write_note(notes_dir: Path, name: str, body: str) -> Path:
    notes_dir.mkdir(parents=True, exist_ok=True)
    fm = "---\ntitle: " + name.removesuffix(".md") + "\ntags:\n  - concept\n---\n\n"
    p = notes_dir / name
    p.write_text(fm + body, encoding="utf-8")
    return p


# ─── filter_missing_concepts ────────────────────────────────────────────

def test_filter_missing_concepts_accepts_clean_concept_names() -> None:
    raw = {"Stoicism": ["Note-A.md"], "Cognitive-Bias": ["Note-B.md"]}
    accepted, rejection = s7_stubs.filter_missing_concepts(raw)
    assert "Stoicism" in accepted
    assert "Cognitive-Bias" in accepted
    assert sum(rejection.values()) == 0


def test_filter_missing_concepts_rejects_garbage() -> None:
    raw = {
        "Stoicism": ["A.md"],                                        # accept
        "This is a sentence-shaped concept name string.": ["B.md"],  # reject (sentence-shaped: terminal period)
        "Bad|Pipe": ["C.md"],                                        # reject (disallowed-chars)
        "something-foundational-report-2025-01-01": ["D.md"],        # reject (report-filename)
    }
    accepted, rejection = s7_stubs.filter_missing_concepts(raw)
    assert "Stoicism" in accepted
    assert "Bad|Pipe" not in accepted
    assert "something-foundational-report-2025-01-01" not in accepted
    assert "This is a sentence-shaped concept name string." not in accepted
    assert sum(rejection.values()) == 3


def test_filter_missing_concepts_empty_input() -> None:
    accepted, rejection = s7_stubs.filter_missing_concepts({})
    assert accepted == {}
    assert rejection == {}


# ─── _make_filtered_audit ───────────────────────────────────────────────

def test_make_filtered_audit_overrides_missing_only() -> None:
    from stages.s7_stubs import audit_notes
    original = audit_notes.AuditResult()
    original.total_notes = 10
    original.unique_targets = 5
    original.resolved = {"X": ["a.md"]}
    original.unresolved = {"Y": ["b.md"]}
    original.placeholders = {}
    original.report_refs = {}
    original.missing_concepts = {"Old": ["c.md"]}
    original.orphans = []
    original.well_connected = []
    original.note_incoming = {}
    original.note_outgoing = {}

    filtered = s7_stubs._make_filtered_audit(original, {"New": ["d.md"]})
    assert filtered.total_notes == 10
    assert filtered.missing_concepts == {"New": ["d.md"]}
    # Originals untouched on other fields
    assert filtered.resolved == {"X": ["a.md"]}


# ─── generate_stubs_filtered (dry-run) ──────────────────────────────────

def test_generate_stubs_filtered_dry_run_writes_nothing(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(notes, "Hub.md", "Refers to [[Stoicism]] and [[Cognitive-Bias]].")
    stats = s7_stubs.generate_stubs_filtered(notes, execute=False)
    assert stats.executed is False
    assert stats.written == 0
    # No new files appeared
    assert {p.name for p in notes.glob("*.md")} == {"Hub.md"}


def test_generate_stubs_filtered_execute_creates_stubs(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(notes, "Hub.md", "Refers to [[Stoicism]] and [[Cognitive-Bias]].")
    stats = s7_stubs.generate_stubs_filtered(notes, execute=True)
    assert stats.executed is True
    assert stats.written >= 1  # at least one stub written
    written_files = {p.name for p in notes.glob("*.md")} - {"Hub.md"}
    assert len(written_files) == stats.written


def test_generate_stubs_filtered_filters_garbage(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(
        notes, "Hub.md",
        "Refers to [[Stoicism]] and [[something-foundational-report-2025-01-01]].",
    )
    stats = s7_stubs.generate_stubs_filtered(notes, execute=False)
    assert stats.rejected >= 1
    assert stats.accepted >= 1
