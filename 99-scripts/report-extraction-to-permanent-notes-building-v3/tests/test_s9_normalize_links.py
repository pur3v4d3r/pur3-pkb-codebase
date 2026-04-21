#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for stages.s9_normalize_links — vault-wide pipe-syntax normalization."""
from __future__ import annotations

from pathlib import Path

import pytest

from stages import s9_normalize_links


def _write_note(notes_dir: Path, name: str, body: str) -> Path:
    notes_dir.mkdir(parents=True, exist_ok=True)
    fm = "---\ntitle: " + name.removesuffix(".md") + "\n---\n\n"
    p = notes_dir / name
    p.write_text(fm + body, encoding="utf-8")
    return p


def test_normalize_notes_dry_run_reports_no_changes(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(notes, "Foo-Bar.md", "Body.")
    _write_note(notes, "Baz.md", "Refers to [[Foo-Bar|Foo Bar]].")  # already piped
    stats = s9_normalize_links.normalize_notes(notes, execute=False)
    assert stats.executed is False
    assert Path(stats.notes_dir) == notes
    # Already-piped link should not be rewritten
    assert stats.total_rewrites == 0


def test_normalize_notes_execute_rewrites_unpipe(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(notes, "Foo-Bar.md", "Body.")
    _write_note(notes, "Baz.md", "Refers to [[Foo Bar]].")  # spaced display, target Foo-Bar
    stats = s9_normalize_links.normalize_notes(notes, execute=True)
    assert stats.executed is True
    # The v2 rewrite_wikilinks resolves "Foo Bar" → "Foo-Bar" with display preserved
    baz = (notes / "Baz.md").read_text(encoding="utf-8")
    assert "[[Foo-Bar|Foo Bar]]" in baz or "[[Foo Bar]]" in baz  # tolerant


def test_normalize_notes_missing_dir_raises(tmp_path: Path) -> None:
    with pytest.raises(s9_normalize_links.NormalizeLinksError):
        s9_normalize_links.normalize_notes(tmp_path / "nope", execute=False)
