#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI behavior tests for ``pipeline_v3.py``.

Covers stage-selection logic (``--from-stage``/``--to-stage``/``--skip-stubs``)
and the ``--rebuild`` Phase 6 guardrail. Does not exercise actual stage
execution; that is covered by the per-stage test modules.
"""
from __future__ import annotations

import pytest
from click.testing import CliRunner

import pipeline_v3


# ─────────────────────────────────────────────────────────────────────────
# _select_stage_range
# ─────────────────────────────────────────────────────────────────────────

def test_select_stage_range_default_returns_all_active() -> None:
    """No bounds → every stage in PIPELINE_STAGES (skips opt-in stage 4)."""
    result = pipeline_v3._select_stage_range(to_stage=None, from_stage=None)
    assert result == [1, 2, 3, 5, 6, 7, 8, 9, 10]


def test_select_stage_range_to_stage_truncates() -> None:
    result = pipeline_v3._select_stage_range(to_stage=6, from_stage=None)
    assert result == [1, 2, 3, 5, 6]


def test_select_stage_range_from_stage_resumes() -> None:
    result = pipeline_v3._select_stage_range(to_stage=None, from_stage=7)
    assert result == [7, 8, 9, 10]


def test_select_stage_range_inverted_bounds_raise() -> None:
    import click
    with pytest.raises(click.BadParameter):
        pipeline_v3._select_stage_range(to_stage=3, from_stage=8)


# ─────────────────────────────────────────────────────────────────────────
# --skip-stubs
# ─────────────────────────────────────────────────────────────────────────

def test_skip_stubs_removes_stage_7_from_full_range() -> None:
    """--skip-stubs drops stage 7 but leaves 8/9/10 intact."""
    runner = CliRunner()
    # Use --from-stage 7 --to-stage 10 with no target-dir → fast-fail BUT
    # only after stage selection is logged. We just assert exit message.
    result = runner.invoke(
        pipeline_v3.main,
        ["--from-stage", "7", "--to-stage", "10", "--skip-stubs"],
    )
    # Will error on missing --target-dir (exit 2), but the skip-stubs notice
    # MUST appear in output before the error.
    assert "Stage 7 removed" in result.output or "Stage 7 removed" in (result.stderr_bytes or b"").decode()


def test_skip_stubs_no_op_when_stage_7_not_selected() -> None:
    """--skip-stubs with --to-stage 6 has no effect (stage 7 wasn't going to run)."""
    runner = CliRunner()
    result = runner.invoke(
        pipeline_v3.main,
        ["--to-stage", "6", "--skip-stubs"],
    )
    assert "Stage 7 removed" not in result.output


# ─────────────────────────────────────────────────────────────────────────
# --rebuild guardrail (Phase 6 not yet open)
# ─────────────────────────────────────────────────────────────────────────

def test_rebuild_without_execute_refused() -> None:
    """--rebuild without --execute fails with the requires-execute message."""
    runner = CliRunner()
    result = runner.invoke(
        pipeline_v3.main,
        ["--rebuild", "--target-dir", "_v3-output/_smoketest/notes"],
    )
    combined = (result.output or "") + ((result.stderr_bytes or b"").decode())
    assert "--rebuild requires --execute" in combined


def test_rebuild_with_execute_still_refused_phase_6_locked() -> None:
    """Even with --execute, --rebuild MUST refuse with the Phase 6 gate message."""
    runner = CliRunner()
    result = runner.invoke(
        pipeline_v3.main,
        ["--rebuild", "--execute", "--target-dir", "_v3-output/_smoketest/notes"],
    )
    combined = (result.output or "") + ((result.stderr_bytes or b"").decode())
    assert "Phase 6 cutover gate is not yet open" in combined


# ─────────────────────────────────────────────────────────────────────────
# PIPELINE_STAGES invariants
# ─────────────────────────────────────────────────────────────────────────

def test_pipeline_stages_contains_no_stage_4() -> None:
    """Stage 4 (LLM normalize) is opt-in and intentionally excluded from defaults."""
    assert 4 not in pipeline_v3.PIPELINE_STAGES


def test_pipeline_stages_excludes_deferred_11_and_12() -> None:
    """Stages 11 (moc) and 12 (commit) are descriptor placeholders, not runnable."""
    assert 11 not in pipeline_v3.PIPELINE_STAGES
    assert 12 not in pipeline_v3.PIPELINE_STAGES
