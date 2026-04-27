#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for reports_to_tts.

Run with:
    pytest test_reports_to_tts.py -v
    pytest test_reports_to_tts.py --cov=reports_to_tts --cov-report=term-missing

These tests cover only the deterministic, network-free parts of the pipeline:
markdown cleaning, chunking, frontmatter extraction, title derivation, the
backend factory's error path, and CLI dry-run integration. Live audio
synthesis is intentionally NOT tested — those backends are external services
or large local models and belong in an integration suite.
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Make the script importable when tests are run from the same directory.
sys.path.insert(0, str(Path(__file__).parent))
import reports_to_tts as rtt  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────

SAMPLE_REPORT = """---
title: A Report on Something
author: Test Author
tags: ["tag1", "tag2"]
---

# A Report on Something

This is the **opening** paragraph. It has [[Wiki Links]] and
[regular links](https://example.com).

## Section One

Here is some content with `inline code` and ![an image](img.png).

```python
print("this should not be spoken")
```

> [!important] Read this
> This callout text is important.

- Bullet one
- Bullet two

## Section Two

| Col A | Col B |
|-------|-------|
| 1     | 2     |

Final sentence.
"""


@pytest.fixture
def sample_report_file(tmp_path: Path) -> Path:
    p = tmp_path / "sample.md"
    p.write_text(SAMPLE_REPORT, encoding="utf-8")
    return p


# ─────────────────────────────────────────────────────────────────────────
# Frontmatter extraction
# ─────────────────────────────────────────────────────────────────────────

def test_frontmatter_parses_top_level_fields() -> None:
    fields, body = rtt._extract_frontmatter(SAMPLE_REPORT)
    assert fields["title"] == "A Report on Something"
    assert fields["author"] == "Test Author"
    assert body.lstrip().startswith("# A Report on Something")


def test_frontmatter_absent_returns_empty_dict() -> None:
    text = "# Just a heading\n\nNo frontmatter here.\n"
    fields, body = rtt._extract_frontmatter(text)
    assert fields == {}
    assert body == text


# ─────────────────────────────────────────────────────────────────────────
# Markdown cleaning — happy paths
# ─────────────────────────────────────────────────────────────────────────

def test_clean_markdown_removes_code_blocks() -> None:
    out = rtt.clean_markdown("Before\n\n```py\nprint('x')\n```\n\nAfter")
    assert "print" not in out
    assert "Before" in out and "After" in out


def test_clean_markdown_removes_inline_code() -> None:
    out = rtt.clean_markdown("Use `foo` carefully.")
    assert "foo" not in out


def test_clean_markdown_resolves_wikilinks() -> None:
    assert "Display Text" in rtt.clean_markdown("See [[Target|Display Text]] now.")
    assert "Plain Target" in rtt.clean_markdown("See [[Plain Target]] now.")


def test_clean_markdown_resolves_md_links() -> None:
    assert "the docs" in rtt.clean_markdown("Read [the docs](http://x).")
    assert "http://x" not in rtt.clean_markdown("Read [the docs](http://x).")


def test_clean_markdown_strips_emphasis() -> None:
    out = rtt.clean_markdown("This is **very** *important* and _emphasized_.")
    assert "**" not in out and "*" not in out and "_" not in out
    assert "very" in out and "important" in out


def test_clean_markdown_callout_becomes_sentence() -> None:
    out = rtt.clean_markdown("> [!warning] Be careful\n> Body text.")
    assert "Warning" in out
    assert "Be careful" in out


def test_clean_markdown_heading_becomes_section_mark() -> None:
    out = rtt.clean_markdown("# Title\n\nBody.\n\n## Sub\n\nMore.")
    assert rtt.SECTION_MARK in out
    # Both headings should produce markers
    assert out.count(rtt.SECTION_MARK) == 2


def test_clean_markdown_strips_html() -> None:
    out = rtt.clean_markdown("Hello <span>world</span> end.")
    assert "<span>" not in out
    assert "world" in out


# ─────────────────────────────────────────────────────────────────────────
# Markdown cleaning — edge cases
# ─────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("text", ["", "   ", "\n\n\n"])
def test_clean_markdown_empty_input(text: str) -> None:
    assert rtt.clean_markdown(text) == ""


def test_clean_markdown_unicode_preserved() -> None:
    out = rtt.clean_markdown("Naïve **café** résumé — 你好.")
    assert "Naïve" in out and "café" in out and "你好" in out


def test_clean_markdown_table_dividers_removed() -> None:
    md = "| a | b |\n|---|---|\n| 1 | 2 |\n"
    out = rtt.clean_markdown(md)
    assert "---" not in out


# ─────────────────────────────────────────────────────────────────────────
# Title derivation
# ─────────────────────────────────────────────────────────────────────────

def test_derive_title_prefers_frontmatter() -> None:
    assert rtt.derive_title({"title": "FM Title"}, "ignored", "fallback") == "FM Title"


def test_derive_title_falls_back_to_first_section_mark() -> None:
    text = f"{rtt.SECTION_MARK}First Heading.\n\nbody"
    assert rtt.derive_title({}, text, "fallback") == "First Heading"


def test_derive_title_falls_back_to_filename() -> None:
    assert rtt.derive_title({}, "no headings here", "the-stem") == "the-stem"


# ─────────────────────────────────────────────────────────────────────────
# Chunking — happy paths
# ─────────────────────────────────────────────────────────────────────────

def test_chunk_text_short_input_one_chunk() -> None:
    chunks = rtt.chunk_text("Hello world.", max_chars=100)
    assert len(chunks) == 1
    assert chunks[0].text == "Hello world."
    assert chunks[0].is_section_break is False


def test_chunk_text_section_marks_create_breaks() -> None:
    text = (
        f"{rtt.SECTION_MARK}Intro.\n\nFirst paragraph.\n\n"
        f"{rtt.SECTION_MARK}Body.\n\nSecond paragraph."
    )
    chunks = rtt.chunk_text(text, max_chars=1000)
    assert len(chunks) == 2
    assert chunks[0].is_section_break is False  # first section never has preceding break
    assert chunks[1].is_section_break is True


def test_chunk_text_splits_long_section_at_sentence_boundary() -> None:
    section = ". ".join([f"Sentence number {i}" for i in range(50)]) + "."
    chunks = rtt.chunk_text(section, max_chars=200)
    assert len(chunks) > 1
    for ch in chunks:
        assert len(ch.text) <= 250  # some slack for sentence-boundary splits


# ─────────────────────────────────────────────────────────────────────────
# Chunking — error paths
# ─────────────────────────────────────────────────────────────────────────

def test_chunk_text_invalid_max_chars_raises() -> None:
    with pytest.raises(ValueError, match="positive"):
        rtt.chunk_text("anything", max_chars=0)


def test_hard_wrap_handles_no_whitespace() -> None:
    out = list(rtt._hard_wrap("a" * 100, 30))
    assert all(len(p) <= 30 for p in out)
    assert "".join(out) == "a" * 100


# ─────────────────────────────────────────────────────────────────────────
# Filename safety
# ─────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected_safe", [
    ("normal-name", "normal-name"),
    ("with spaces", "with spaces"),
    ('quotes"and?stars*', "quotes_and_stars_"),
    ("path/with\\slashes", "path_with_slashes"),
    ("", "report"),
    ("...", "report"),
])
def test_safe_stem(raw: str, expected_safe: str) -> None:
    assert rtt._safe_stem(raw) == expected_safe


# ─────────────────────────────────────────────────────────────────────────
# Backend factory
# ─────────────────────────────────────────────────────────────────────────

def test_build_backend_unknown_raises() -> None:
    cfg = rtt.BackendConfig(voice="x")
    with pytest.raises(rtt.BackendUnavailableError, match="Unknown backend"):
        rtt.build_backend("nonexistent", cfg)


def test_resolve_voice_uses_default_when_none() -> None:
    assert rtt._resolve_voice("edge", None) == rtt.DEFAULT_VOICE["edge"]
    assert rtt._resolve_voice("kokoro", "custom") == "custom"


def test_resolve_chunk_chars_default() -> None:
    assert rtt._resolve_chunk_chars("edge", None) == rtt.DEFAULT_CHUNK_CHARS["edge"]


def test_resolve_chunk_chars_invalid_raises() -> None:
    with pytest.raises(ValueError, match="positive"):
        rtt._resolve_chunk_chars("edge", -1)


# ─────────────────────────────────────────────────────────────────────────
# load_report integration
# ─────────────────────────────────────────────────────────────────────────

def test_load_report_produces_clean_text(sample_report_file: Path) -> None:
    report = rtt.load_report(sample_report_file)
    assert report.title == "A Report on Something"
    assert report.author == "Test Author"
    assert "print(" not in report.text          # code block stripped
    assert "https://example.com" not in report.text  # link URL stripped
    assert "Wiki Links" in report.text          # wikilink display preserved
    assert rtt.SECTION_MARK in report.text      # headings → section marks


def test_discover_reports_finds_markdown(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text("# A")
    (tmp_path / "b.md").write_text("# B")
    (tmp_path / "ignore.txt").write_text("nope")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.md").write_text("# C")
    found = rtt.discover_reports(tmp_path)
    assert len(found) == 3
    assert all(p.suffix == ".md" for p in found)


def test_discover_reports_single_file(tmp_path: Path) -> None:
    p = tmp_path / "only.md"
    p.write_text("# x")
    assert rtt.discover_reports(p) == [p]


def test_discover_reports_missing_path_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        rtt.discover_reports(tmp_path / "nope")


# ─────────────────────────────────────────────────────────────────────────
# CLI tests
# ─────────────────────────────────────────────────────────────────────────

def test_cli_help_includes_all_documented_flags(capsys: pytest.CaptureFixture) -> None:
    parser = rtt.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])
    out = capsys.readouterr().out
    for flag in ["--backend", "--voice", "--rate", "--format",
                 "--dry-run", "--overwrite", "--chunk-chars",
                 "--speaker-wav", "--strict", "--version"]:
        assert flag in out, f"--help missing {flag}"


def test_cli_dry_run_no_audio_written(sample_report_file: Path,
                                      tmp_path: Path) -> None:
    """`--dry-run` produces no audio side effects."""
    out_dir = tmp_path / "out"
    rc = rtt.main([
        str(sample_report_file),
        "--output-dir", str(out_dir),
        "--dry-run",
    ])
    assert rc == 0
    assert not out_dir.exists() or not any(out_dir.iterdir())


def test_cli_missing_input_returns_2(tmp_path: Path) -> None:
    rc = rtt.main([str(tmp_path / "nonexistent.md")])
    assert rc == 2


def test_cli_empty_dir_returns_4(tmp_path: Path) -> None:
    rc = rtt.main([str(tmp_path), "--dry-run"])
    assert rc == 4


# ─────────────────────────────────────────────────────────────────────────
# Synthesize_report integration (with a stubbed backend)
# ─────────────────────────────────────────────────────────────────────────

class _StubBackend(rtt.TTSBackend):
    """In-memory stub that writes a tiny silent WAV per chunk."""
    name = "edge"  # masquerade as edge to keep the chunk-format suffix simple

    def __init__(self) -> None:
        super().__init__(rtt.BackendConfig(voice="x"))
        self.calls: list[str] = []

    def synthesize(self, text: str, dest: Path) -> None:
        self.calls.append(text)
        # Minimal valid MP3 frame is non-trivial; we just touch the file. The
        # test path that exercises this stub does not actually run pydub
        # assembly, because the integration test below patches assemble_audio.
        dest.write_bytes(b"\x00")


def test_synthesize_report_dry_run_short_circuits(sample_report_file: Path,
                                                  tmp_path: Path) -> None:
    report = rtt.load_report(sample_report_file)
    backend = _StubBackend()
    result = rtt.synthesize_report(
        report, backend,
        out_dir=tmp_path,
        out_format="mp3",
        chunk_chars=4000,
        overwrite=False,
        dry_run=True,
    )
    assert result.ok is True
    assert result.chunk_count > 0
    assert backend.calls == []  # dry-run never calls the backend


def test_synthesize_report_skips_existing(sample_report_file: Path,
                                          tmp_path: Path) -> None:
    report = rtt.load_report(sample_report_file)
    out_path = tmp_path / f"{rtt._safe_stem(report.path.stem)}.mp3"
    out_path.write_bytes(b"existing")
    backend = _StubBackend()
    result = rtt.synthesize_report(
        report, backend,
        out_dir=tmp_path, out_format="mp3", chunk_chars=4000,
        overwrite=False, dry_run=False,
    )
    assert result.ok is True
    assert result.error == "skipped-exists"
    assert out_path.read_bytes() == b"existing"  # untouched
    assert backend.calls == []


def test_synthesize_report_calls_backend_per_chunk(sample_report_file: Path,
                                                   tmp_path: Path) -> None:
    report = rtt.load_report(sample_report_file)
    backend = _StubBackend()
    with patch.object(rtt, "assemble_audio", return_value=12345) as asm, \
         patch.object(rtt, "tag_mp3"):
        result = rtt.synthesize_report(
            report, backend,
            out_dir=tmp_path, out_format="mp3", chunk_chars=4000,
            overwrite=True, dry_run=False,
        )
    assert result.ok is True
    assert result.duration_ms == 12345
    assert len(backend.calls) == result.chunk_count
    assert asm.called
