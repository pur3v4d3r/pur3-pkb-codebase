#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for pkb_report_generator.

Run with:
    pytest 99-scripts/test_pkb_report_generator.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make the script importable regardless of cwd
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

import pkb_report_generator as prg  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────

@pytest.fixture
def sample_md(tmp_path: Path) -> Path:
    """A representative Obsidian-style markdown file."""
    content = """---
tags: [test, example]
status: evergreen
---

# Sample Note

This is a [[linked-note]] with a #inline-tag and another [[other-note|alias]].

> [!important] Test callout
> Stuff here.

## Section

```python
def code(): pass
```

More text with [[linked-note]] again.
"""
    p = tmp_path / "sample.md"
    p.write_text(content, encoding="utf-8")
    return p


@pytest.fixture
def sample_folder(tmp_path: Path) -> Path:
    """A folder of three small markdown files."""
    (tmp_path / "a.md").write_text(
        "---\ntags: [foo]\n---\n# A\n[[b]]\n#bar\n", encoding="utf-8"
    )
    (tmp_path / "b.md").write_text(
        "# B\n[[a]] [[ghost]]\n", encoding="utf-8"
    )
    (tmp_path / "c.md").write_text(
        "# C\nOrphan with no links.\n", encoding="utf-8"
    )
    return tmp_path


# ─────────────────────────────────────────────────────────────────────────
# Pure analyzer tests — happy path
# ─────────────────────────────────────────────────────────────────────────

def test_parse_frontmatter_extracts_yaml(sample_md: Path) -> None:
    text = sample_md.read_text(encoding="utf-8")
    fm, body, has_fm = prg.parse_frontmatter(text)
    assert has_fm is True
    assert "status" in fm
    assert body.lstrip().startswith("# Sample Note")


def test_parse_frontmatter_handles_missing() -> None:
    fm, body, has_fm = prg.parse_frontmatter("# No frontmatter here\n")
    assert has_fm is False
    assert fm == {}
    assert body.startswith("# No")


def test_strip_code_blocks_removes_fenced() -> None:
    text = "Hello\n```python\nx = 1\n```\nWorld"
    out = prg.strip_code_blocks(text)
    assert "x = 1" not in out
    assert "Hello" in out and "World" in out


def test_analyze_text_extracts_all_features(sample_md: Path) -> None:
    text = sample_md.read_text(encoding="utf-8")
    stat = sample_md.stat()
    a = prg.analyze_text(sample_md, text, stat)
    assert a.has_frontmatter
    assert "linked-note" in a.wikilinks
    assert "other-note" in a.wikilinks
    assert "inline-tag" in a.tags
    assert "important" in a.callouts
    assert a.heading_count == 2
    assert a.word_count > 0
    assert a.size_bytes == stat.st_size
    assert a.error is None


# ─────────────────────────────────────────────────────────────────────────
# Edge-case tests
# ─────────────────────────────────────────────────────────────────────────

def test_analyze_empty_file(tmp_path: Path) -> None:
    p = tmp_path / "empty.md"
    p.write_text("", encoding="utf-8")
    a = prg.analyze_file(p)
    assert a.error is None
    assert a.word_count == 0
    assert a.wikilinks == []


def test_analyze_unicode_content(tmp_path: Path) -> None:
    p = tmp_path / "uni.md"
    p.write_text("# 日本語 🚀\n[[notiôn]] café résumé\n", encoding="utf-8")
    a = prg.analyze_file(p)
    assert a.error is None
    assert a.word_count >= 2


def test_extract_fm_tags_list_form() -> None:
    assert sorted(prg._extract_fm_tags({"tags": ["a", "b"]})) == ["a", "b"]


def test_extract_fm_tags_string_form() -> None:
    assert sorted(prg._extract_fm_tags({"tags": "#a #b"})) == ["a", "b"]


def test_extract_fm_tags_comma_form() -> None:
    assert sorted(prg._extract_fm_tags({"tags": "a, b, c"})) == ["a", "b", "c"]


def test_extract_fm_tags_missing() -> None:
    assert prg._extract_fm_tags({}) == []


# ─────────────────────────────────────────────────────────────────────────
# Aggregator tests
# ─────────────────────────────────────────────────────────────────────────

def test_link_graph_detects_orphans_and_broken(sample_folder: Path) -> None:
    paths = prg.discover_files(sample_folder, recursive=False, excludes=frozenset())
    files = [prg.analyze_file(p) for p in paths]
    g = prg.link_graph(files)
    assert "c.md" in g["orphans"]
    broken_targets = {tgt for _, tgt in g["broken"]}
    assert "ghost" in broken_targets


def test_detect_duplicates_finds_identical(tmp_path: Path) -> None:
    (tmp_path / "x.md").write_text("identical body\n", encoding="utf-8")
    (tmp_path / "y.md").write_text("identical body\n", encoding="utf-8")
    (tmp_path / "z.md").write_text("different body\n", encoding="utf-8")
    paths = prg.discover_files(tmp_path, recursive=False, excludes=frozenset())
    files = [prg.analyze_file(p) for p in paths]
    dupes = prg.detect_duplicates(files)
    assert len(dupes) == 1
    assert len(dupes[0]) == 2


def test_frontmatter_audit_counts(sample_folder: Path) -> None:
    paths = prg.discover_files(sample_folder, recursive=False, excludes=frozenset())
    files = [prg.analyze_file(p) for p in paths]
    audit = prg.frontmatter_audit(files)
    assert audit["with_fm"] == 1
    assert len(audit["without_fm"]) == 2


# ─────────────────────────────────────────────────────────────────────────
# Visualisation tests
# ─────────────────────────────────────────────────────────────────────────

def test_ascii_bar_chart_handles_empty() -> None:
    assert prg.ascii_bar_chart([]) == "(no data)"


def test_ascii_bar_chart_renders_bars() -> None:
    out = prg.ascii_bar_chart([("foo", 5), ("bar", 10)])
    assert "foo" in out and "bar" in out
    assert "█" in out


def test_ascii_histogram_handles_empty() -> None:
    assert prg.ascii_histogram([]) == "(no data)"


# ─────────────────────────────────────────────────────────────────────────
# Recommendation engine tests
# ─────────────────────────────────────────────────────────────────────────

def test_recommendations_flag_orphans(sample_folder: Path) -> None:
    paths = prg.discover_files(sample_folder, recursive=False, excludes=frozenset())
    files = [prg.analyze_file(p) for p in paths]
    g = prg.link_graph(files)
    audit = prg.frontmatter_audit(files)
    dupes = prg.detect_duplicates(files)
    recs = prg.generate_recommendations(files, g, audit, dupes)
    categories = {r.category for r in recs}
    assert "links" in categories  # orphans + broken
    assert "metadata" in categories  # without frontmatter


# ─────────────────────────────────────────────────────────────────────────
# Discovery + error tests
# ─────────────────────────────────────────────────────────────────────────

def test_discover_files_raises_on_missing(tmp_path: Path) -> None:
    with pytest.raises(prg.InvalidInputError):
        prg.discover_files(tmp_path / "nope", False, frozenset())


def test_discover_files_raises_when_empty(tmp_path: Path) -> None:
    with pytest.raises(prg.NoFilesFoundError):
        prg.discover_files(tmp_path, False, frozenset())


def test_discover_files_recursive(tmp_path: Path) -> None:
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "deep.md").write_text("hi", encoding="utf-8")
    (tmp_path / "top.md").write_text("hi", encoding="utf-8")
    files = prg.discover_files(tmp_path, recursive=True, excludes=frozenset())
    assert len(files) == 2


def test_discover_files_respects_excludes(tmp_path: Path) -> None:
    excluded = tmp_path / ".obsidian"
    excluded.mkdir()
    (excluded / "skip.md").write_text("x", encoding="utf-8")
    (tmp_path / "keep.md").write_text("x", encoding="utf-8")
    files = prg.discover_files(
        tmp_path, recursive=True, excludes=frozenset({".obsidian"})
    )
    assert len(files) == 1
    assert files[0].name == "keep.md"


# ─────────────────────────────────────────────────────────────────────────
# CLI integration tests
# ─────────────────────────────────────────────────────────────────────────

def test_cli_dry_run_produces_no_files(sample_folder: Path, capsys: pytest.CaptureFixture) -> None:
    rc = prg.main([str(sample_folder), "--dry-run", "--no-progress", "--quiet"])
    assert rc == 0
    # No report file should be present
    reports = list(sample_folder.glob("_REPORT-*.md"))
    assert reports == []


def test_cli_writes_report(sample_folder: Path) -> None:
    rc = prg.main([str(sample_folder), "--no-progress", "--quiet"])
    assert rc == 0
    reports = list(sample_folder.glob("_REPORT-*.md"))
    assert len(reports) == 1
    body = reports[0].read_text(encoding="utf-8")
    assert "# 📊 PKB Analysis Report" in body
    assert "## Recommendations" in body
    assert "## File Index" in body


def test_cli_returns_2_on_missing_input(tmp_path: Path) -> None:
    rc = prg.main([str(tmp_path / "does-not-exist"), "--no-progress", "--quiet"])
    assert rc == 2


def test_cli_returns_3_on_empty_folder(tmp_path: Path) -> None:
    rc = prg.main([str(tmp_path), "--no-progress", "--quiet"])
    assert rc == 3


def test_cli_help_contains_examples(capsys: pytest.CaptureFixture) -> None:
    parser = prg.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])
    out = capsys.readouterr().out
    assert "Examples:" in out
    assert "Exit codes" in out
    assert "--dry-run" in out
    assert "--charts" in out


def test_cli_version_flag(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as exc:
        prg.main(["--version"])
    assert exc.value.code == 0
