#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for detect_orphan_wikilinks.

Run with:
    pytest 99-scripts/test_detect_orphan_wikilinks.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import detect_orphan_wikilinks as dow  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────

@pytest.fixture
def vault(tmp_path: Path) -> Path:
    """A minimal vault with a couple of existing notes."""
    (tmp_path / "notes").mkdir()
    (tmp_path / "notes" / "Existing Note.md").write_text("# Existing\n", encoding="utf-8")
    (tmp_path / "notes" / "another-note.md").write_text("# Another\n", encoding="utf-8")
    (tmp_path / "folder").mkdir()
    (tmp_path / "folder" / "Nested.md").write_text("# Nested\n", encoding="utf-8")
    return tmp_path


# ─────────────────────────────────────────────────────────────────────────
# Pure function tests
# ─────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("inp,expected", [
    ("My Note Title", "my-note-title"),
    ("snake_case_thing", "snake-case-thing"),
    ("Mixed  Spaces__And_Symbols!@#", "mixed-spaces-and-symbols"),
    ("already-kebab", "already-kebab"),
    ("  -trim-  ", "trim"),
])
def test_to_kebab_case(inp: str, expected: str) -> None:
    assert dow.to_kebab_case(inp) == expected


@pytest.mark.parametrize("inner,expected", [
    ("Note", ("Note", None, None, None, False)),
    ("Note|Alias", ("Note", "Alias", None, None, False)),
    ("Note#Heading", ("Note", None, "Heading", None, False)),
    ("Note^block123", ("Note", None, None, "block123", False)),
    ("folder/Note", ("folder/Note", None, None, None, True)),
    ("folder/Note#H|A", ("folder/Note", "A", "H", None, True)),
])
def test_parse_wikilink_inner(inner: str, expected: tuple) -> None:
    assert dow.parse_wikilink_inner(inner) == expected


def test_strip_code_removes_fenced_and_inline() -> None:
    txt = "before `inline [[bad]]` and\n```\n[[also bad]]\n```\nafter [[good]]"
    out = dow.strip_code(txt)
    assert "[[bad]]" not in out
    assert "[[also bad]]" not in out
    assert "[[good]]" in out


# ─────────────────────────────────────────────────────────────────────────
# Extraction tests
# ─────────────────────────────────────────────────────────────────────────

def test_extract_wikilinks_skips_fenced_code(vault: Path) -> None:
    src = vault / "src.md"
    src.write_text(
        "Text [[Real Link]] here.\n"
        "```\n[[Should Skip]]\n```\n"
        "Tail [[Another]] line.\n",
        encoding="utf-8",
    )
    links = dow.extract_wikilinks(src, vault)
    targets = [L.target for L in links]
    assert "Real Link" in targets
    assert "Another" in targets
    assert "Should Skip" not in targets


def test_extract_wikilinks_skips_inline_code(vault: Path) -> None:
    src = vault / "src.md"
    src.write_text("Use `[[Inline]]` not real, but [[Real]] is.\n", encoding="utf-8")
    targets = [L.target for L in dow.extract_wikilinks(src, vault)]
    assert targets == ["Real"]


def test_extract_wikilinks_line_numbers(vault: Path) -> None:
    src = vault / "src.md"
    src.write_text("L1\nL2 [[A]]\nL3\nL4 [[B]] [[C]]\n", encoding="utf-8")
    links = dow.extract_wikilinks(src, vault)
    line_targets = [(L.line_number, L.target) for L in links]
    assert (2, "A") in line_targets
    assert (4, "B") in line_targets
    assert (4, "C") in line_targets


# ─────────────────────────────────────────────────────────────────────────
# Index + orphan tests
# ─────────────────────────────────────────────────────────────────────────

def test_build_vault_index_finds_notes(vault: Path) -> None:
    by_basename, by_path = dow.build_vault_index(vault)
    assert "existing note" in by_basename
    assert "another-note" in by_basename
    assert "nested" in by_basename
    assert "folder/nested" in by_path


def test_is_orphan_basename_match(vault: Path) -> None:
    by_basename, by_path = dow.build_vault_index(vault)
    link = dow.WikiLink(
        source_file=Path("x.md"), line_number=1, raw="Existing Note",
        target="Existing Note", alias=None, heading=None, block=None,
        is_embed=False, is_path=False,
    )
    assert dow.is_orphan(link, by_basename, by_path) is False


def test_is_orphan_missing_target(vault: Path) -> None:
    by_basename, by_path = dow.build_vault_index(vault)
    link = dow.WikiLink(
        source_file=Path("x.md"), line_number=1, raw="Ghost",
        target="Ghost", alias=None, heading=None, block=None,
        is_embed=False, is_path=False,
    )
    assert dow.is_orphan(link, by_basename, by_path) is True


def test_is_orphan_path_match(vault: Path) -> None:
    by_basename, by_path = dow.build_vault_index(vault)
    link = dow.WikiLink(
        source_file=Path("x.md"), line_number=1, raw="folder/Nested",
        target="folder/Nested", alias=None, heading=None, block=None,
        is_embed=False, is_path=True,
    )
    assert dow.is_orphan(link, by_basename, by_path) is False


# ─────────────────────────────────────────────────────────────────────────
# Scan + report integration tests
# ─────────────────────────────────────────────────────────────────────────

def test_scan_folder_finds_orphans(vault: Path) -> None:
    scan = vault / "scan"
    scan.mkdir()
    (scan / "doc.md").write_text(
        "Refs: [[Existing Note]] and [[Ghost Note]] and [[folder/Nested]] and ![[Embed Ghost]]\n",
        encoding="utf-8",
    )
    by_basename, by_path = dow.build_vault_index(vault)
    result = dow.scan_folder(scan, vault, by_basename, by_path, include_embeds=False)
    targets = [L.target for L in result.orphans]
    assert "Ghost Note" in targets
    assert "Existing Note" not in targets
    assert "folder/Nested" not in targets
    assert "Embed Ghost" not in targets  # embeds skipped by default


def test_scan_folder_with_embeds(vault: Path) -> None:
    scan = vault / "scan"
    scan.mkdir()
    (scan / "doc.md").write_text("![[Embed Ghost]]\n", encoding="utf-8")
    by_basename, by_path = dow.build_vault_index(vault)
    result = dow.scan_folder(scan, vault, by_basename, by_path, include_embeds=True)
    assert any(L.target == "Embed Ghost" for L in result.orphans)


def test_render_report_no_orphans(vault: Path) -> None:
    result = dow.ScanResult(files_scanned=1, links_found=0, orphans=[])
    md = dow.render_markdown_report(result, Path("scan"), vault, suggest_kebab=False)
    assert "No orphan wiki-links detected" in md


def test_render_report_with_orphans_and_kebab(vault: Path) -> None:
    link = dow.WikiLink(
        source_file=Path("scan/doc.md"), line_number=3, raw="Ghost Note",
        target="Ghost Note", alias=None, heading=None, block=None,
        is_embed=False, is_path=False,
    )
    result = dow.ScanResult(files_scanned=1, links_found=1, orphans=[link])
    md = dow.render_markdown_report(result, Path("scan"), vault, suggest_kebab=True)
    assert "Ghost Note" in md
    assert "ghost-note" in md
    assert "kebab-case" in md.lower()


# ─────────────────────────────────────────────────────────────────────────
# CLI tests
# ─────────────────────────────────────────────────────────────────────────

def test_cli_help_lists_required_flags(capsys: pytest.CaptureFixture) -> None:
    parser = dow.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])
    out = capsys.readouterr().out
    for flag in ("--scan-folder", "--vault-root", "--output",
                 "--include-embeds", "--suggest-kebab", "--version"):
        assert flag in out


def test_cli_main_writes_report_file(vault: Path, capsys: pytest.CaptureFixture) -> None:
    scan = vault / "scan"
    scan.mkdir()
    (scan / "doc.md").write_text("[[Ghost]] and [[Existing Note]]\n", encoding="utf-8")
    out = vault / "report.md"
    rc = dow.main([
        "--scan-folder", str(scan),
        "--vault-root", str(vault),
        "--output", str(out),
        "--quiet",
    ])
    assert rc == 0
    assert out.exists()
    content = out.read_text(encoding="utf-8")
    assert "Ghost" in content
    assert "Orphan Wiki-Links Report" in content


def test_cli_main_missing_folder_returns_2(vault: Path) -> None:
    rc = dow.main([
        "--scan-folder", str(vault / "does-not-exist"),
        "--vault-root", str(vault),
        "--quiet",
    ])
    assert rc == 2


def test_cli_main_stdout_default(vault: Path, capsys: pytest.CaptureFixture) -> None:
    scan = vault / "scan"
    scan.mkdir()
    (scan / "doc.md").write_text("[[Ghost]]\n", encoding="utf-8")
    rc = dow.main(["--scan-folder", str(scan), "--vault-root", str(vault), "--quiet"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "Orphan Wiki-Links Report" in out
    assert "Ghost" in out
