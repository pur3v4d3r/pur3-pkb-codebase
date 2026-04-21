#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for stages/s6_render.py."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import pytest

from lib.candidate import Candidate, EvidenceItem, SourceReport
from stages import s6_render


def _src(file: str = "report-A_validated.json", line: int = 1) -> SourceReport:
    return SourceReport(batch="b1", file=file, line=line)


def _ev(body: str, title: str = "E", file: str = "report-A_validated.json") -> EvidenceItem:
    return EvidenceItem(body=body, title=title, callout_type="evidence", source=_src(file))


def _make_candidate(**kw) -> Candidate:
    src = _src()
    defaults = dict(
        canonical_name="Self-Determination Theory",
        primary_name="Self-Determination Theory",
        aliases=("SDT",),
        domain="educational-psychology",
        subdomains=("motivation",),
        confidence="high",
        complexity="advanced-practitioner",
        importance="high",
        definition_body="A macro-theory of motivation.",
        evidence=(_ev("Autonomy is intrinsic.", "Autonomy"),),
        warnings=(EvidenceItem(body="Don't confuse with self-efficacy.",
                                title="Caution", callout_type="warning", source=src),),
        source_reports=(src,),
        wiki_links_seen=("Intrinsic-Motivation", "Autonomy"),
    )
    defaults.update(kw)
    return Candidate(**defaults)


def _write_consolidated(path: Path, candidates: list[Candidate]) -> Path:
    payload = {
        "version": "3.0.0-test",
        "stats": {},
        "candidates": [c.to_dict() for c in candidates],
    }
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


# ─── render_candidate ────────────────────────────────────────────────────

def test_render_candidate_includes_title_and_definition(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate()
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert out.startswith("---\n")
    assert "# Self-Determination Theory" in out
    assert "> [!definition] Self-Determination Theory" in out
    assert "> A macro-theory of motivation." in out


def test_render_candidate_renders_evidence(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate()
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert "## Core Explanation" in out
    assert "> [!evidence] Autonomy" in out
    assert "> Autonomy is intrinsic." in out
    assert "report-A" in out


def test_render_candidate_renders_warnings(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate()
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert "## Practical Implications" in out
    assert "> [!warning] Caution" in out


def test_render_candidate_skips_empty_sections(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate(evidence=(), warnings=(), insights=())
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert "## Core Explanation" not in out
    assert "## Practical Implications" not in out


def test_render_candidate_includes_dataview_block(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate()
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert "```dataview" in out
    assert "LIST FROM [[Self-Determination Theory]]" in out


def test_render_candidate_includes_sources_footer(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate()
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert "**Sources:**" in out
    assert "[[report-A]]" in out


def test_render_missing_definition_emits_pending(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate(definition_body="")
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    assert "*Definition pending" in out


# ─── update path (merge with existing) ───────────────────────────────────

def test_render_with_existing_frontmatter_preserves_status(tmp_path: Path) -> None:
    env = s6_render._build_env()
    c = _make_candidate()
    existing_fm = {"status": "evergreen-curated", "created": "2025-01-01",
                   "tags": ["my-custom-tag"]}
    out = s6_render.render_candidate(
        c, env=env, today=dt.date(2026, 4, 21),
        existing_frontmatter=existing_fm,
    )
    assert "status: evergreen-curated" in out
    assert "created: '2025-01-01'" in out or "created: 2025-01-01" in out
    assert "my-custom-tag" in out


# ─── load + write ────────────────────────────────────────────────────────

def test_load_candidates_from_file(tmp_path: Path) -> None:
    fp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                              [_make_candidate()])
    cands = s6_render.load_candidates(fp)
    assert len(cands) == 1
    assert cands[0].primary_name == "Self-Determination Theory"


def test_load_candidates_from_directory(tmp_path: Path) -> None:
    _write_consolidated(tmp_path / "_consolidated-candidates.json",
                         [_make_candidate()])
    cands = s6_render.load_candidates(tmp_path)
    assert len(cands) == 1


def test_load_candidates_missing_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        s6_render.load_candidates(tmp_path / "nope.json")


def test_run_render_writes_files(tmp_path: Path) -> None:
    inp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                               [_make_candidate()])
    out_dir = tmp_path / "rendered"
    stats = s6_render.run_render(inp, out_dir, today=dt.date(2026, 4, 21))
    assert stats.notes_total == 1
    assert stats.notes_created == 1
    assert stats.notes_updated == 0
    assert (out_dir / "Self-Determination Theory.md").is_file()


def test_run_render_dry_run_writes_nothing(tmp_path: Path) -> None:
    inp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                               [_make_candidate()])
    out_dir = tmp_path / "rendered"
    stats = s6_render.run_render(inp, out_dir, dry_run=True,
                                 today=dt.date(2026, 4, 21))
    assert stats.notes_total == 1
    assert not out_dir.exists() or not any(out_dir.iterdir())


def test_run_render_update_path_counts_as_updated(tmp_path: Path) -> None:
    inp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                               [_make_candidate()])
    out_dir = tmp_path / "rendered"
    s6_render.run_render(inp, out_dir, today=dt.date(2026, 4, 21))
    # Re-render
    stats2 = s6_render.run_render(inp, out_dir, today=dt.date(2026, 4, 22))
    assert stats2.notes_updated == 1
    assert stats2.notes_created == 0


def test_run_render_update_preserves_user_status(tmp_path: Path) -> None:
    inp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                               [_make_candidate()])
    out_dir = tmp_path / "rendered"
    s6_render.run_render(inp, out_dir, today=dt.date(2026, 4, 21))
    note_path = out_dir / "Self-Determination Theory.md"
    # Simulate user editing the status field
    text = note_path.read_text(encoding="utf-8")
    text = text.replace("status: evergreen", "status: evergreen-curated")
    note_path.write_text(text, encoding="utf-8")
    # Re-render
    s6_render.run_render(inp, out_dir, today=dt.date(2026, 4, 22))
    new_text = note_path.read_text(encoding="utf-8")
    assert "status: evergreen-curated" in new_text


# ─── frontmatter line budget on a real-shaped candidate ─────────────────

def test_rendered_frontmatter_under_25_lines(tmp_path: Path) -> None:
    """Spec §3.2 budget: ≤25 frontmatter lines for typical notes."""
    env = s6_render._build_env()
    c = _make_candidate()
    out = s6_render.render_candidate(c, env=env, today=dt.date(2026, 4, 21))
    # Extract frontmatter block
    assert out.startswith("---\n")
    end_idx = out.find("\n---", 4)
    fm_block = out[: end_idx + 4]
    fm_lines = fm_block.count("\n")
    assert fm_lines <= 25, f"frontmatter is {fm_lines} lines:\n{fm_block}"


# ─── CLI ─────────────────────────────────────────────────────────────────

def test_cli_help() -> None:
    parser = s6_render.build_parser()
    help_text = parser.format_help()
    assert "--target-dir" in help_text
    assert "--dry-run" in help_text


def test_cli_missing_input_returns_2(tmp_path: Path) -> None:
    rc = s6_render.main([str(tmp_path / "missing.json"),
                         "-t", str(tmp_path / "out")])
    assert rc == 2


def test_cli_writes_files_end_to_end(tmp_path: Path) -> None:
    inp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                               [_make_candidate()])
    out_dir = tmp_path / "out"
    rc = s6_render.main([str(inp), "-t", str(out_dir), "-q"])
    assert rc == 0
    assert (out_dir / "Self-Determination Theory.md").is_file()


def test_cli_dry_run_writes_nothing(tmp_path: Path) -> None:
    inp = _write_consolidated(tmp_path / "_consolidated-candidates.json",
                               [_make_candidate()])
    out_dir = tmp_path / "out"
    rc = s6_render.main([str(inp), "-t", str(out_dir), "--dry-run", "-q"])
    assert rc == 0
    assert not out_dir.exists() or not any(out_dir.iterdir())
