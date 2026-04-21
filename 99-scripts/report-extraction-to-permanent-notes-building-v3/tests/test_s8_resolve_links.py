#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for stages.s8_resolve_links — report-side wiki-link rewriting."""
from __future__ import annotations

from pathlib import Path

import pytest

from stages import s8_resolve_links


def _write_note(notes_dir: Path, name: str, body: str = "Body.") -> Path:
    notes_dir.mkdir(parents=True, exist_ok=True)
    fm = "---\ntitle: " + name.removesuffix(".md") + "\n---\n\n"
    p = notes_dir / name
    p.write_text(fm + body, encoding="utf-8")
    return p


def _write_report(reports_dir: Path, name: str, body: str) -> Path:
    reports_dir.mkdir(parents=True, exist_ok=True)
    p = reports_dir / name
    p.write_text(body, encoding="utf-8")
    return p


def test_resolve_report_links_dry_run(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    reports = tmp_path / "reports"
    _write_note(notes, "Stoicism.md")
    _write_report(reports, "report-1.md", "Refers to [[Stoicism]].")
    stats = s8_resolve_links.resolve_report_links(
        notes, [reports], execute=False,
    )
    assert stats.executed is False
    assert stats.files_scanned >= 1


def test_resolve_report_links_missing_notes_dir_raises(tmp_path: Path) -> None:
    with pytest.raises(s8_resolve_links.ResolveLinksError):
        s8_resolve_links.resolve_report_links(
            tmp_path / "missing-notes", [tmp_path], execute=False,
        )


def test_resolve_report_links_empty_reports_dirs_raises(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(notes, "Foo.md")
    with pytest.raises(s8_resolve_links.ResolveLinksError):
        s8_resolve_links.resolve_report_links(notes, [], execute=False)
