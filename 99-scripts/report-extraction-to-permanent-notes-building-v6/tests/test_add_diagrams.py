#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for add_diagrams.py — V6 diagram-injection pipeline.

Run with:
    pytest tests/test_add_diagrams.py -v
    pytest tests/test_add_diagrams.py --cov=add_diagrams --cov-report=term-missing
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

# ── path injection so the test can import add_diagrams directly ────────────
_TESTS_DIR = Path(__file__).resolve().parent
_V6_DIR = _TESTS_DIR.parent
_V3_DIR = _V6_DIR.parent / "report-extraction-to-permanent-notes-building-v3"
for _p in (_V3_DIR, _V6_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import add_diagrams  # noqa: E402 (must come after path injection)
from add_diagrams import (
    Diagram,
    DiagramResponse,
    DiagramResult,
    NoteParseError,
    RunStats,
    V6Note,
    _body_excerpt,
    _render_diagram_block,
    build_diagram_section,
    insert_diagram_section,
    load_note,
    scan_notes,
    update_frontmatter,
    write_note_atomic,
)


# ════════════════════════════════════════════════════════════════════════════
# Fixtures
# ════════════════════════════════════════════════════════════════════════════

_MINIMAL_FRONTMATTER = """\
---
title: Test Concept
type: permanent-note
status: enriched
domain: cognitive-science
provenance:
  pipeline-version: v6.0.0
  diagram-passes: 0
---
"""

_FULL_BODY = """\
# Test Concept

> [!definition] **Test Concept**
> This is a test concept definition.

## Core Explanation

Some explanation text here.

## Connections & Context
Related concepts here.
"""


@pytest.fixture()
def note_path(tmp_path: Path) -> Path:
    """Create a minimal valid V6 note on disk."""
    p = tmp_path / "test-concept.md"
    p.write_text(_MINIMAL_FRONTMATTER + "\n" + _FULL_BODY, encoding="utf-8")
    return p


@pytest.fixture()
def already_diagrammed_note(tmp_path: Path) -> Path:
    """A note with diagram-passes: 1 already set."""
    fm = _MINIMAL_FRONTMATTER.replace("diagram-passes: 0", "diagram-passes: 1")
    p = tmp_path / "already-done.md"
    p.write_text(fm + "\n" + _FULL_BODY, encoding="utf-8")
    return p


@pytest.fixture()
def mermaid_diagram() -> Diagram:
    return Diagram(
        diagram_type="mermaid",
        caption="Test Concept Architecture Flow",
        view_hint="Follow arrows left-to-right through the pipeline.",
        content="flowchart LR\n  A[Input] --> B[Process] --> C[Output]",
    )


@pytest.fixture()
def ascii_diagram() -> Diagram:
    return Diagram(
        diagram_type="ascii",
        caption="Component Boundary Overview",
        view_hint="Each box is a distinct module; arrows show data flow.",
        content=(
            "┌──────────┐      ┌──────────┐\n"
            "│  Source  │ ───► │   Sink   │\n"
            "└──────────┘      └──────────┘"
        ),
    )


@pytest.fixture()
def diagram_response(mermaid_diagram: Diagram, ascii_diagram: Diagram) -> DiagramResponse:
    return DiagramResponse(diagrams=[mermaid_diagram, ascii_diagram])


# ════════════════════════════════════════════════════════════════════════════
# Diagram Pydantic schema validation
# ════════════════════════════════════════════════════════════════════════════

class TestDiagramSchema:
    def test_strips_mermaid_opening_fence(self) -> None:
        d = Diagram(
            diagram_type="mermaid",
            caption="Test",
            content="```mermaid\nflowchart LR\n  A-->B\n```",
        )
        assert d.content == "flowchart LR\n  A-->B"

    def test_strips_plain_opening_fence(self) -> None:
        d = Diagram(
            diagram_type="ascii",
            caption="Test",
            content="```\n+--+\n```",
        )
        assert d.content == "+--+"

    def test_strips_closing_fence_only(self) -> None:
        d = Diagram(
            diagram_type="ascii",
            caption="Test",
            content="flowchart LR\n  A-->B\n```",
        )
        assert not d.content.endswith("```")

    def test_caption_stripped(self) -> None:
        d = Diagram(
            diagram_type="ascii",
            caption="  My Caption  ",
            content="A --> B",
        )
        assert d.caption == "My Caption"

    def test_view_hint_stripped(self) -> None:
        d = Diagram(
            diagram_type="mermaid",
            caption="Flow",
            view_hint="  Read left to right.  ",
            content="graph LR\n  A-->B",
        )
        assert d.view_hint == "Read left to right."


class TestDiagramResponse:
    def test_is_empty_no_diagrams(self) -> None:
        r = DiagramResponse(diagrams=[])
        assert r.is_empty()

    def test_is_not_empty_with_content(self, diagram_response: DiagramResponse) -> None:
        assert not diagram_response.is_empty()

    def test_has_mermaid_true(self, mermaid_diagram: Diagram) -> None:
        r = DiagramResponse(diagrams=[mermaid_diagram])
        assert r.has_mermaid()

    def test_has_mermaid_false(self, ascii_diagram: Diagram) -> None:
        r = DiagramResponse(diagrams=[ascii_diagram])
        assert not r.has_mermaid()

    def test_null_diagrams_coerced_to_empty(self) -> None:
        r = DiagramResponse.model_validate({"diagrams": None})
        assert r.diagrams == []


# ════════════════════════════════════════════════════════════════════════════
# Note loading
# ════════════════════════════════════════════════════════════════════════════

class TestLoadNote:
    def test_loads_valid_note(self, note_path: Path) -> None:
        note = load_note(note_path)
        assert note.title == "Test Concept"
        assert note.domain == "cognitive-science"
        assert note.diagram_passes == 0

    def test_infers_title_from_stem_when_missing(self, tmp_path: Path) -> None:
        p = tmp_path / "some-concept-name.md"
        p.write_text("---\ntype: permanent-note\n---\n# Body\n", encoding="utf-8")
        note = load_note(p)
        assert note.title == "Some Concept Name"

    def test_raises_on_missing_file(self, tmp_path: Path) -> None:
        with pytest.raises(NoteParseError, match="Cannot read"):
            load_note(tmp_path / "nonexistent.md")

    def test_raises_on_empty_file(self, tmp_path: Path) -> None:
        p = tmp_path / "empty.md"
        p.write_text("", encoding="utf-8")
        with pytest.raises(NoteParseError, match="Empty file"):
            load_note(p)

    def test_raises_on_missing_frontmatter(self, tmp_path: Path) -> None:
        p = tmp_path / "no-fm.md"
        p.write_text("# Just a title\nNo frontmatter here.\n", encoding="utf-8")
        with pytest.raises(NoteParseError):
            load_note(p)

    def test_reads_diagram_passes_from_provenance(self, already_diagrammed_note: Path) -> None:
        note = load_note(already_diagrammed_note)
        assert note.diagram_passes == 1


# ════════════════════════════════════════════════════════════════════════════
# scan_notes
# ════════════════════════════════════════════════════════════════════════════

class TestScanNotes:
    def test_finds_unprocessed_notes(self, note_path: Path) -> None:
        notes = scan_notes(note_path.parent, name_filter=None, re_diagram=False, limit=None)
        stems = [n.path.stem for n in notes]
        assert "test-concept" in stems

    def test_skips_already_diagrammed(
        self, already_diagrammed_note: Path, tmp_path: Path
    ) -> None:
        notes = scan_notes(tmp_path, name_filter=None, re_diagram=False, limit=None)
        assert all(n.path.stem != "already-done" for n in notes)

    def test_re_diagram_includes_processed(
        self, already_diagrammed_note: Path, tmp_path: Path
    ) -> None:
        notes = scan_notes(tmp_path, name_filter=None, re_diagram=True, limit=None)
        stems = [n.path.stem for n in notes]
        assert "already-done" in stems

    def test_name_filter_case_insensitive(self, note_path: Path) -> None:
        notes = scan_notes(
            note_path.parent, name_filter="TEST-CONCEPT", re_diagram=False, limit=None
        )
        assert len(notes) == 1
        assert notes[0].path.stem == "test-concept"

    def test_limit_caps_results(self, tmp_path: Path) -> None:
        for i in range(5):
            p = tmp_path / f"note-{i}.md"
            p.write_text(_MINIMAL_FRONTMATTER + "\n# Body\n", encoding="utf-8")
        notes = scan_notes(tmp_path, name_filter=None, re_diagram=False, limit=3)
        assert len(notes) == 3

    def test_raises_when_dir_missing(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            scan_notes(tmp_path / "nonexistent", name_filter=None, re_diagram=False, limit=None)


# ════════════════════════════════════════════════════════════════════════════
# _body_excerpt
# ════════════════════════════════════════════════════════════════════════════

class TestBodyExcerpt:
    def test_returns_full_body_when_under_limit(self) -> None:
        body = "Short body text."
        assert _body_excerpt(body, max_chars=200) == body

    def test_truncates_at_paragraph_boundary(self) -> None:
        # Two paragraphs joined by \n\n; the second should be cut
        body = "Paragraph one.\n\nParagraph two that is long enough to push over budget."
        result = _body_excerpt(body, max_chars=20)
        assert "[... truncated for context ...]" in result

    def test_truncated_result_is_shorter_than_original(self) -> None:
        body = "A" * 10000
        result = _body_excerpt(body, max_chars=5000)
        assert len(result) < len(body)


# ════════════════════════════════════════════════════════════════════════════
# _render_diagram_block
# ════════════════════════════════════════════════════════════════════════════

class TestRenderDiagramBlock:
    def test_mermaid_uses_callout_wrapper(self, mermaid_diagram: Diagram) -> None:
        rendered = _render_diagram_block(mermaid_diagram, index=1)
        assert "> [!abstract]" in rendered
        assert "```mermaid" in rendered

    def test_mermaid_includes_caption(self, mermaid_diagram: Diagram) -> None:
        rendered = _render_diagram_block(mermaid_diagram, index=1)
        assert mermaid_diagram.caption in rendered

    def test_mermaid_includes_view_hint(self, mermaid_diagram: Diagram) -> None:
        rendered = _render_diagram_block(mermaid_diagram, index=1)
        assert mermaid_diagram.view_hint in rendered

    def test_mermaid_content_lines_prefixed(self, mermaid_diagram: Diagram) -> None:
        rendered = _render_diagram_block(mermaid_diagram, index=1)
        # All mermaid content lines inside callout should start with "> "
        for line in mermaid_diagram.content.splitlines():
            assert f"> {line}" in rendered

    def test_ascii_uses_code_fence(self, ascii_diagram: Diagram) -> None:
        rendered = _render_diagram_block(ascii_diagram, index=2)
        assert "```\n" in rendered

    def test_ascii_includes_caption(self, ascii_diagram: Diagram) -> None:
        rendered = _render_diagram_block(ascii_diagram, index=2)
        assert ascii_diagram.caption in rendered

    def test_ascii_includes_font_note(self, ascii_diagram: Diagram) -> None:
        rendered = _render_diagram_block(ascii_diagram, index=2)
        assert "monospace" in rendered

    def test_diagram_without_view_hint(self) -> None:
        d = Diagram(
            diagram_type="mermaid",
            caption="No hint diagram",
            view_hint="",
            content="graph LR\n  A-->B",
        )
        rendered = _render_diagram_block(d, index=1)
        # Should not emit an empty hint line
        assert "**\n>\n> ```" not in rendered


# ════════════════════════════════════════════════════════════════════════════
# build_diagram_section
# ════════════════════════════════════════════════════════════════════════════

class TestBuildDiagramSection:
    def test_starts_with_section_header(self, diagram_response: DiagramResponse) -> None:
        section = build_diagram_section(diagram_response, pass_n=1, today="2026-05-21")
        assert section.startswith(add_diagrams.DIAGRAM_SECTION_HEADER)

    def test_contains_marker(self, diagram_response: DiagramResponse) -> None:
        section = build_diagram_section(diagram_response, pass_n=1, today="2026-05-21")
        assert "<!-- diagram-pass:1 (2026-05-21) -->" in section

    def test_contains_all_diagrams(self, diagram_response: DiagramResponse) -> None:
        section = build_diagram_section(diagram_response, pass_n=1, today="2026-05-21")
        assert "Diagram 1" in section
        assert "Diagram 2" in section


# ════════════════════════════════════════════════════════════════════════════
# insert_diagram_section
# ════════════════════════════════════════════════════════════════════════════

class TestInsertDiagramSection:
    def test_diagram_section_before_title(self) -> None:
        body = "\n# My Title\n\nSome content.\n"
        section = "## 📊 Visual Overview\n\nDiagram here.\n"
        result = insert_diagram_section(body, section)
        title_pos = result.index("# My Title")
        diagram_pos = result.index("## 📊 Visual Overview")
        assert diagram_pos < title_pos

    def test_body_content_preserved(self) -> None:
        body = "\n# Title\n\nContent.\n"
        section = "## Diagrams\n\nDiagram.\n"
        result = insert_diagram_section(body, section)
        assert "Content." in result
        assert "Diagram." in result

    def test_no_leading_blank_lines_before_title(self) -> None:
        body = "\n\n\n# Title\n"
        section = "## Diagrams\n"
        result = insert_diagram_section(body, section)
        # Should not accumulate excessive blank lines
        assert result.count("\n\n\n\n") == 0


# ════════════════════════════════════════════════════════════════════════════
# update_frontmatter
# ════════════════════════════════════════════════════════════════════════════

class TestUpdateFrontmatter:
    def test_sets_diagram_passes(self) -> None:
        fm: dict = {"title": "T", "provenance": {"pipeline-version": "v6"}}
        out = update_frontmatter(fm, pass_n=1, model="qwen2.5", today="2026-05-21")
        assert out["provenance"]["diagram-passes"] == 1

    def test_sets_diagram_model(self) -> None:
        fm: dict = {"title": "T"}
        out = update_frontmatter(fm, pass_n=1, model="qwen2.5:14b", today="2026-05-21")
        assert out["provenance"]["diagram-model"] == "qwen2.5:14b"

    def test_sets_last_diagrammed(self) -> None:
        fm: dict = {"title": "T"}
        out = update_frontmatter(fm, pass_n=1, model="m", today="2026-05-21")
        assert out["provenance"]["last-diagrammed"] == "2026-05-21"

    def test_sets_updated_field(self) -> None:
        fm: dict = {"title": "T", "updated": "2025-01-01"}
        out = update_frontmatter(fm, pass_n=1, model="m", today="2026-05-21")
        assert out["updated"] == "2026-05-21"

    def test_preserves_user_editable_fields(self) -> None:
        fm: dict = {
            "title": "T",
            "status": "enriched",
            "tags": ["permanent-note"],
            "importance": "high",
        }
        out = update_frontmatter(fm, pass_n=1, model="m", today="2026-05-21")
        assert out["status"] == "enriched"
        assert out["tags"] == ["permanent-note"]
        assert out["importance"] == "high"

    def test_does_not_mutate_input(self) -> None:
        fm: dict = {"title": "T", "provenance": {}}
        original_prov = dict(fm["provenance"])
        update_frontmatter(fm, pass_n=1, model="m", today="2026-05-21")
        assert fm["provenance"] == original_prov


# ════════════════════════════════════════════════════════════════════════════
# write_note_atomic
# ════════════════════════════════════════════════════════════════════════════

class TestWriteNoteAtomic:
    def test_writes_content_correctly(self, tmp_path: Path) -> None:
        p = tmp_path / "out.md"
        write_note_atomic(p, "Hello world\n")
        assert p.read_text(encoding="utf-8") == "Hello world\n"

    def test_no_tmp_file_left_behind(self, tmp_path: Path) -> None:
        p = tmp_path / "out.md"
        write_note_atomic(p, "Content\n")
        tmp = p.with_suffix(".md.tmp")
        assert not tmp.exists()

    def test_creates_parent_directories(self, tmp_path: Path) -> None:
        p = tmp_path / "subdir" / "deep" / "out.md"
        write_note_atomic(p, "Content\n")
        assert p.exists()

    def test_overwrites_existing_file(self, tmp_path: Path) -> None:
        p = tmp_path / "out.md"
        write_note_atomic(p, "First\n")
        write_note_atomic(p, "Second\n")
        assert p.read_text(encoding="utf-8") == "Second\n"


# ════════════════════════════════════════════════════════════════════════════
# CLI integration — build_parser / main
# ════════════════════════════════════════════════════════════════════════════

class TestCLI:
    def test_help_includes_required_flags(self, capsys: pytest.CaptureFixture) -> None:
        with pytest.raises(SystemExit):
            add_diagrams.build_parser().parse_args(["--help"])
        captured = capsys.readouterr()
        for flag in ("--dry-run", "--note", "--limit", "--re-diagram", "--bypass-cache"):
            assert flag in captured.out

    def test_dry_run_flag_parsed(self) -> None:
        args = add_diagrams.build_parser().parse_args(["--dry-run", "--limit", "5"])
        assert args.dry_run is True
        assert args.limit == 5

    def test_version_flag(self, capsys: pytest.CaptureFixture) -> None:
        with pytest.raises(SystemExit):
            add_diagrams.build_parser().parse_args(["--version"])
        captured = capsys.readouterr()
        assert add_diagrams.__version__ in captured.out

    def test_main_returns_2_when_input_dir_missing(self, tmp_path: Path) -> None:
        result = add_diagrams.main([
            "--input-dir", str(tmp_path / "nonexistent"),
            "--dry-run",
        ])
        assert result == 2

    def test_main_returns_4_when_no_notes_found(self, tmp_path: Path) -> None:
        result = add_diagrams.main([
            "--input-dir", str(tmp_path),
            "--dry-run",
        ])
        assert result == 4

    def test_main_dry_run_does_not_write(
        self,
        note_path: Path,
        diagram_response: DiagramResponse,
    ) -> None:
        """Dry-run invocation must not modify any file."""
        original_content = note_path.read_text(encoding="utf-8")

        mock_rsp = MagicMock()
        mock_rsp.parsed = diagram_response
        mock_rsp.cached = False

        mock_client = MagicMock()
        mock_client.chat_json.return_value = mock_rsp

        with (
            patch("add_diagrams.OllamaClient", return_value=mock_client),
            patch("add_diagrams.config_v3.OLLAMA_URL", "http://localhost:11434"),
            patch("add_diagrams.config_v3.LLM_CACHE_DIR", note_path.parent),
        ):
            result = add_diagrams.main([
                "--input-dir", str(note_path.parent),
                "--dry-run",
            ])

        assert result == 0
        assert note_path.read_text(encoding="utf-8") == original_content
