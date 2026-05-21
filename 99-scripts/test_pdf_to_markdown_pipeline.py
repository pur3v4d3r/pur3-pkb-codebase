#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for pdf_to_markdown_pipeline.

Run with:
    cd D:\\10_pur3v4d3r's-vault\\99-scripts
    pytest test_pdf_to_markdown_pipeline.py -v
    pytest test_pdf_to_markdown_pipeline.py -v --tb=short
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Ensure the scripts directory is on sys.path so the module is importable
sys.path.insert(0, str(Path(__file__).parent))
import pdf_to_markdown_pipeline as pipeline


# ─────────────────────────────────────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture
def tmp_pdf_dir(tmp_path: Path) -> Path:
    """Temporary directory with dummy files for log/path tests."""
    d = tmp_path / "pdfs"
    d.mkdir()
    return d


@pytest.fixture
def small_pdf(tmp_path: Path) -> Path:
    """Write a tiny binary blob that acts as a stand-in PDF for hashing."""
    p = tmp_path / "sample.pdf"
    p.write_bytes(b"%PDF-1.4 fake content for hashing 12345")
    return p


@pytest.fixture
def log_with_entries(tmp_path: Path) -> tuple[Path, list[dict]]:
    """A pre-populated JSON log file plus its content."""
    data = [
        {"path": "/a/b.pdf", "category": "digital"},
        {"path": "/c/d.pdf", "category": "scanned"},
    ]
    log_path = tmp_path / "test.json"
    log_path.write_text(json.dumps(data), encoding="utf-8")
    return log_path, data


# ─────────────────────────────────────────────────────────────────────────────
# slugify
# ─────────────────────────────────────────────────────────────────────────────

class TestSlugify:
    def test_lowercase_output(self):
        result = pipeline.slugify("Hello World")
        assert result == result.lower()

    def test_spaces_become_underscores(self):
        assert "_" in pipeline.slugify("hello world")

    def test_max_length_respected(self):
        long_text = "a" * 200
        assert len(pipeline.slugify(long_text)) <= 80

    def test_custom_max_length(self):
        result = pipeline.slugify("hello world", max_len=5)
        assert len(result) <= 5

    def test_empty_string(self):
        assert pipeline.slugify("") == ""

    def test_special_chars_removed(self):
        result = pipeline.slugify("Chain-of-Thought (2022): A Survey")
        assert "(" not in result
        assert ")" not in result
        assert ":" not in result


# ─────────────────────────────────────────────────────────────────────────────
# load_log / save_log
# ─────────────────────────────────────────────────────────────────────────────

class TestLoadSaveLog:
    def test_load_missing_file_returns_empty(self, tmp_path: Path):
        missing = tmp_path / "nonexistent.json"
        assert pipeline.load_log(missing) == []

    def test_load_valid_json(self, log_with_entries):
        log_path, expected = log_with_entries
        result = pipeline.load_log(log_path)
        assert result == expected

    def test_load_corrupt_json_returns_empty(self, tmp_path: Path):
        bad = tmp_path / "bad.json"
        bad.write_text("{not valid json", encoding="utf-8")
        assert pipeline.load_log(bad) == []

    def test_save_and_reload(self, tmp_path: Path):
        data = [{"key": "value", "num": 42}]
        log_path = tmp_path / "out.json"
        pipeline.save_log(log_path, data)
        assert pipeline.load_log(log_path) == data

    def test_save_dry_run_does_not_write(self, tmp_path: Path):
        log_path = tmp_path / "not_written.json"
        pipeline.save_log(log_path, [{"x": 1}], dry_run=True)
        assert not log_path.exists()

    def test_save_creates_parent_dirs(self, tmp_path: Path):
        nested = tmp_path / "deep" / "nested" / "log.json"
        pipeline.save_log(nested, [])
        assert nested.exists()

    def test_save_is_atomic_via_tmp(self, tmp_path: Path):
        """Verify no .tmp file lingers after a successful save."""
        log_path = tmp_path / "log.json"
        pipeline.save_log(log_path, [{"a": 1}])
        tmp_file = log_path.with_suffix(".tmp")
        assert not tmp_file.exists()


# ─────────────────────────────────────────────────────────────────────────────
# hash_file
# ─────────────────────────────────────────────────────────────────────────────

class TestHashFile:
    def test_returns_string(self, small_pdf: Path):
        result = pipeline._hash_file(small_pdf)
        assert isinstance(result, str)

    def test_returns_hex(self, small_pdf: Path):
        result = pipeline._hash_file(small_pdf)
        # MD5 hex digest is exactly 32 chars
        assert len(result) == 32
        assert all(c in "0123456789abcdef" for c in result)

    def test_identical_files_same_hash(self, tmp_path: Path):
        f1 = tmp_path / "a.pdf"
        f2 = tmp_path / "b.pdf"
        content = b"same content"
        f1.write_bytes(content)
        f2.write_bytes(content)
        assert pipeline._hash_file(f1) == pipeline._hash_file(f2)

    def test_different_files_different_hash(self, tmp_path: Path):
        f1 = tmp_path / "a.pdf"
        f2 = tmp_path / "b.pdf"
        f1.write_bytes(b"content A")
        f2.write_bytes(b"content B")
        assert pipeline._hash_file(f1) != pipeline._hash_file(f2)

    def test_empty_file(self, tmp_path: Path):
        empty = tmp_path / "empty.pdf"
        empty.write_bytes(b"")
        result = pipeline._hash_file(empty)
        assert len(result) == 32  # MD5 of empty = d41d8cd98f00b204e9800998ecf8427e

    def test_missing_file_raises_oserror(self, tmp_path: Path):
        missing = tmp_path / "missing.pdf"
        with pytest.raises(OSError):
            pipeline._hash_file(missing)


# ─────────────────────────────────────────────────────────────────────────────
# find_marker_output
# ─────────────────────────────────────────────────────────────────────────────

class TestFindMarkerOutput:
    def test_returns_primary_path_when_exists(self, tmp_path: Path):
        output_dir = tmp_path / "output"
        stem = "my_paper"
        expected = output_dir / stem / f"{stem}.md"
        expected.parent.mkdir(parents=True)
        expected.write_text("# content")
        result = pipeline.find_marker_output(output_dir, stem)
        assert result == expected

    def test_returns_none_when_nothing_found(self, tmp_path: Path):
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        result = pipeline.find_marker_output(output_dir, "nonexistent")
        assert result is None

    def test_fallback_to_direct_md(self, tmp_path: Path):
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        stem = "paper"
        direct = output_dir / f"{stem}.md"
        direct.write_text("# content")
        result = pipeline.find_marker_output(output_dir, stem)
        assert result == direct

    def test_excludes_original_backups(self, tmp_path: Path):
        output_dir = tmp_path / "output"
        stem = "paper"
        sub_dir = output_dir / stem
        sub_dir.mkdir(parents=True)
        # Only create a .original.md file — should not be returned
        backup = sub_dir / f"{stem}.original.md"
        backup.write_text("backup")
        result = pipeline.find_marker_output(output_dir, stem)
        assert result is None


# ─────────────────────────────────────────────────────────────────────────────
# _extract_yaml_block
# ─────────────────────────────────────────────────────────────────────────────

class TestExtractYamlBlock:
    def test_clean_yaml_block_passthrough(self):
        raw = "---\ntitle: Hello\n---"
        result = pipeline._extract_yaml_block(raw)
        assert result.startswith("---")
        assert result.endswith("---")
        assert "title: Hello" in result

    def test_extracts_block_from_preamble_text(self):
        raw = "Here is the YAML:\n---\ntitle: Test\n---\nSome trailing text."
        result = pipeline._extract_yaml_block(raw)
        assert "title: Test" in result
        assert "Here is" not in result

    def test_handles_missing_closing_dashes(self):
        raw = "---\ntitle: Unterminated"
        result = pipeline._extract_yaml_block(raw)
        assert result.startswith("---")
        assert result.endswith("---")

    def test_wraps_bare_output(self):
        raw = "title: Bare\nauthor: Someone"
        result = pipeline._extract_yaml_block(raw)
        assert result.startswith("---")
        assert result.endswith("---")

    def test_empty_input(self):
        result = pipeline._extract_yaml_block("")
        assert result.startswith("---")
        assert result.endswith("---")

    def test_multiline_yaml_preserved(self):
        raw = "---\ntitle: A\nauthor: B\ntags:\n  - '#llm'\n---"
        result = pipeline._extract_yaml_block(raw)
        assert "tags:" in result
        assert "'#llm'" in result


# ─────────────────────────────────────────────────────────────────────────────
# _classify_pdf (mocking fitz)
# ─────────────────────────────────────────────────────────────────────────────

class TestClassifyPdf:
    def _make_mock_fitz(self, page_text: str):
        """Helper: create a fitz mock that returns page_text from page 0."""
        mock_page = MagicMock()
        mock_page.get_text.return_value = page_text
        mock_doc = MagicMock()
        mock_doc.__getitem__ = MagicMock(return_value=mock_page)
        mock_fitz = MagicMock()
        mock_fitz.open.return_value = mock_doc
        mock_doc.close = MagicMock()
        return mock_fitz

    def test_digital_pdf_classified_correctly(self, tmp_path: Path):
        pdf = tmp_path / "digital.pdf"
        pdf.write_bytes(b"fake")
        long_text = "A" * 500   # well above SCANNED_TEXT_THRESHOLD
        mock_fitz = self._make_mock_fitz(long_text)
        with patch.object(pipeline, "fitz", mock_fitz):
            result = pipeline._classify_pdf(pdf)
        assert result == "digital"

    def test_scanned_pdf_classified_correctly(self, tmp_path: Path):
        pdf = tmp_path / "scanned.pdf"
        pdf.write_bytes(b"fake")
        short_text = "X" * 10   # well below SCANNED_TEXT_THRESHOLD
        mock_fitz = self._make_mock_fitz(short_text)
        with patch.object(pipeline, "fitz", mock_fitz):
            result = pipeline._classify_pdf(pdf)
        assert result == "scanned"

    def test_empty_page_is_scanned(self, tmp_path: Path):
        pdf = tmp_path / "empty.pdf"
        pdf.write_bytes(b"fake")
        mock_fitz = self._make_mock_fitz("   ")
        with patch.object(pipeline, "fitz", mock_fitz):
            result = pipeline._classify_pdf(pdf)
        assert result == "scanned"

    def test_exactly_at_threshold_is_digital(self, tmp_path: Path):
        pdf = tmp_path / "threshold.pdf"
        pdf.write_bytes(b"fake")
        # Exactly at threshold — should be "digital"
        text = "T" * pipeline.SCANNED_TEXT_THRESHOLD
        mock_fitz = self._make_mock_fitz(text)
        with patch.object(pipeline, "fitz", mock_fitz):
            result = pipeline._classify_pdf(pdf)
        assert result == "digital"


# ─────────────────────────────────────────────────────────────────────────────
# ConversionResult / EnrichResult dataclasses
# ─────────────────────────────────────────────────────────────────────────────

class TestDataclasses:
    def test_conversion_result_to_dict(self, tmp_path: Path):
        r = pipeline.ConversionResult(
            pdf_path=tmp_path / "a.pdf",
            md_path=tmp_path / "a.md",
            status="success",
        )
        d = r.to_dict()
        assert d["status"] == "success"
        assert "pdf_path" in d
        assert "md_path" in d
        assert "timestamp" in d

    def test_conversion_result_none_md_path(self, tmp_path: Path):
        r = pipeline.ConversionResult(
            pdf_path=tmp_path / "a.pdf",
            md_path=None,
            status="failed",
            error="oops",
        )
        d = r.to_dict()
        assert d["md_path"] is None
        assert d["error"] == "oops"

    def test_enrich_result_to_dict(self, tmp_path: Path):
        r = pipeline.EnrichResult(md_path=tmp_path / "x.md", status="skipped")
        d = r.to_dict()
        assert d["status"] == "skipped"
        assert "md_path" in d


# ─────────────────────────────────────────────────────────────────────────────
# _enrich_single (dry-run and idempotency)
# ─────────────────────────────────────────────────────────────────────────────

class TestEnrichSingle:
    def test_dry_run_does_not_write(self, tmp_path: Path):
        md = tmp_path / "paper.md"
        md.write_text("# Some Content\n\nBody of the paper.", encoding="utf-8")

        with patch.object(pipeline, "_generate_frontmatter", return_value="---\ntitle: X\n---"):
            result = pipeline._enrich_single(md, dry_run=True)

        assert result.status == "skipped"
        # File must be unchanged
        assert not md.read_text().startswith("---")

    def test_already_enriched_is_skipped(self, tmp_path: Path):
        md = tmp_path / "enriched.md"
        md.write_text("---\ntitle: Done\n---\n\n# Body\n", encoding="utf-8")
        result = pipeline._enrich_single(md)
        assert result.status == "skipped"

    def test_missing_file_returns_failed(self, tmp_path: Path):
        missing = tmp_path / "ghost.md"
        result = pipeline._enrich_single(missing)
        assert result.status == "failed"

    def test_successful_enrichment_prepends_yaml(self, tmp_path: Path):
        md = tmp_path / "paper.md"
        original_body = "# Introduction\n\nSome text."
        md.write_text(original_body, encoding="utf-8")

        frontmatter = "---\ntitle: My Paper\nauthor: Author\n---"
        with patch.object(pipeline, "_generate_frontmatter", return_value=frontmatter):
            result = pipeline._enrich_single(md, dry_run=False)

        assert result.status == "success"
        content = md.read_text(encoding="utf-8")
        assert content.startswith("---\ntitle: My Paper")
        assert "# Introduction" in content

    def test_backup_created_on_enrich(self, tmp_path: Path):
        md = tmp_path / "paper.md"
        md.write_text("# Body text here.", encoding="utf-8")

        with patch.object(pipeline, "_generate_frontmatter", return_value="---\ntitle: T\n---"):
            pipeline._enrich_single(md, dry_run=False)

        backup = tmp_path / "paper.original.md"
        assert backup.exists()
        assert backup.read_text() == "# Body text here."

    def test_ollama_error_returns_failed(self, tmp_path: Path):
        md = tmp_path / "paper.md"
        md.write_text("# Body", encoding="utf-8")

        with patch.object(
            pipeline, "_generate_frontmatter",
            side_effect=pipeline.OllamaCallError("model not found"),
        ):
            result = pipeline._enrich_single(md, dry_run=False)

        assert result.status == "failed"
        assert "model not found" in result.error


# ─────────────────────────────────────────────────────────────────────────────
# CLI argument parsing
# ─────────────────────────────────────────────────────────────────────────────

class TestCLIParser:
    def test_defaults(self):
        parser = pipeline.build_parser()
        args = parser.parse_args([])
        assert args.phase == "all"
        assert args.workers == pipeline.DEFAULT_WORKERS
        assert args.batch_multiplier == pipeline.DEFAULT_BATCH_MULTIPLIER
        assert args.model == pipeline.DEFAULT_MODEL
        assert args.limit == 0
        assert not args.resume
        assert not args.dry_run

    def test_phase_choices_accepted(self):
        parser = pipeline.build_parser()
        for phase in ("all", "dedupe", "triage", "convert", "enrich"):
            args = parser.parse_args(["--phase", phase])
            assert args.phase == phase

    def test_invalid_phase_raises(self):
        parser = pipeline.build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--phase", "invalid"])

    def test_dry_run_flag(self):
        parser = pipeline.build_parser()
        args = parser.parse_args(["--dry-run"])
        assert args.dry_run is True

    def test_workers_flag(self):
        parser = pipeline.build_parser()
        args = parser.parse_args(["-w", "3"])
        assert args.workers == 3

    def test_limit_flag(self):
        parser = pipeline.build_parser()
        args = parser.parse_args(["--limit", "10"])
        assert args.limit == 10

    def test_resume_flag(self):
        parser = pipeline.build_parser()
        args = parser.parse_args(["--resume"])
        assert args.resume is True

    def test_verbose_count(self):
        parser = pipeline.build_parser()
        args = parser.parse_args(["-vv"])
        assert args.verbose == 2

    def test_custom_model(self):
        parser = pipeline.build_parser()
        args = parser.parse_args(["--model", "llama3.2:3b"])
        assert args.model == "llama3.2:3b"


# ─────────────────────────────────────────────────────────────────────────────
# deduplicate_corpus
# ─────────────────────────────────────────────────────────────────────────────

class TestDeduplicateCorpus:
    def test_no_duplicates_returns_empty_dict(self, tmp_path: Path):
        pdf_dir = tmp_path / "pdfs"
        pdf_dir.mkdir()
        log = tmp_path / "dedupe.json"
        (pdf_dir / "a.pdf").write_bytes(b"content_a")
        (pdf_dir / "b.pdf").write_bytes(b"content_b")

        result = pipeline.deduplicate_corpus(pdf_dir, log, dry_run=True)
        assert result == {}

    def test_identical_files_detected(self, tmp_path: Path):
        pdf_dir = tmp_path / "pdfs"
        pdf_dir.mkdir()
        log = tmp_path / "dedupe.json"
        content = b"duplicate content"
        (pdf_dir / "a.pdf").write_bytes(content)
        (pdf_dir / "b.pdf").write_bytes(content)

        result = pipeline.deduplicate_corpus(pdf_dir, log, dry_run=True)
        assert len(result) == 1

    def test_dry_run_does_not_write_log(self, tmp_path: Path):
        pdf_dir = tmp_path / "pdfs"
        pdf_dir.mkdir()
        log = tmp_path / "dedupe.json"
        (pdf_dir / "a.pdf").write_bytes(b"x")

        pipeline.deduplicate_corpus(pdf_dir, log, dry_run=True)
        assert not log.exists()

    def test_writes_log_when_not_dry_run(self, tmp_path: Path):
        pdf_dir = tmp_path / "pdfs"
        pdf_dir.mkdir()
        log = tmp_path / "dedupe.json"
        same = b"same bytes"
        (pdf_dir / "orig.pdf").write_bytes(same)
        (pdf_dir / "copy.pdf").write_bytes(same)

        pipeline.deduplicate_corpus(pdf_dir, log, dry_run=False)
        assert log.exists()
        data = json.loads(log.read_text())
        assert len(data) == 1
        assert "canonical" in data[0]
        assert "duplicates" in data[0]


# ─────────────────────────────────────────────────────────────────────────────
# main() dry-run integration (no PDF dir needed — uses --dry-run)
# ─────────────────────────────────────────────────────────────────────────────

class TestMainDryRun:
    def test_help_exits_zero(self):
        with pytest.raises(SystemExit) as exc_info:
            pipeline.main(["--help"])
        assert exc_info.value.code == 0

    def test_version_exits_zero(self):
        with pytest.raises(SystemExit) as exc_info:
            pipeline.main(["--version"])
        assert exc_info.value.code == 0

    def test_bad_phase_exits_nonzero(self):
        with pytest.raises(SystemExit) as exc_info:
            pipeline.main(["--phase", "bad"])
        assert exc_info.value.code != 0
