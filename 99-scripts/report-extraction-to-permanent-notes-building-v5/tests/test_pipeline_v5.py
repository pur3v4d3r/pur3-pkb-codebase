#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Smoke tests for pipeline_v5 — CLI surface + routing without LLM."""
from __future__ import annotations

import sys

import pytest

import pipeline_v5
from v5lib.matcher import MatchResult, Matcher
from v5lib.output_index import OutputIndex


def test_module_loads_and_has_version() -> None:
    assert pipeline_v5.__version__ == "1.0.0"
    assert pipeline_v5.DEFAULT_OUTPUT_DIR is not None
    assert pipeline_v5.DEFAULT_INPUT_DIR is not None


def test_build_parser_has_required_flags() -> None:
    p = pipeline_v5.build_parser()
    actions = {a.dest for a in p._actions}
    for required in (
        "input_dir", "output_dir", "report", "limit",
        "reconcile", "match_threshold", "protect_statuses",
        "force_merge", "no_backup", "report_merges",
        "new_mode", "dry_run", "bypass_cache", "model",
        "no_gate", "strict", "verbose", "quiet",
    ):
        assert required in actions, f"missing CLI flag: {required}"


def test_help_runs_without_crashing(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(SystemExit) as exc:
        pipeline_v5.main(["--help"])
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert "Examples" in out
    assert "--reconcile" in out
    assert "--force-merge" in out


def test_parse_protect_set_basic() -> None:
    s = pipeline_v5._parse_protect_set("evergreen, budding")
    assert s == frozenset({"evergreen", "budding"})


def test_route_bundle_miss_returns_new(tmp_path) -> None:
    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    matcher = Matcher(index=idx)

    class B:
        title = "Brand New Concept"
        filename_stem = "brand-new-concept"

    route, match, err = pipeline_v5.route_bundle(B(), matcher)
    assert route == "new"
    assert match is None
    assert err == ""


def test_route_bundle_hit_returns_merge(tmp_path) -> None:
    p = tmp_path / "existing.md"
    p.write_text(
        '---\ntitle: "Existing"\nstatus: enriched\naliases: []\n---\n# Existing\n',
        encoding="utf-8",
    )
    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    matcher = Matcher(index=idx)

    class B:
        title = "Existing"
        filename_stem = "existing"

    route, match, err = pipeline_v5.route_bundle(B(), matcher)
    assert route == "merge"
    assert isinstance(match, MatchResult)
    assert match.tier == "exact_slug"


def test_v5stats_initializes_to_zeros() -> None:
    s = pipeline_v5.V5Stats()
    for f_ in (
        "jsons", "concepts", "routed_merge", "routed_new",
        "merged_written", "merged_skipped", "merged_failed",
        "new_written", "new_skipped", "new_unworthy", "new_failed",
        "ambiguous", "cached",
    ):
        assert getattr(s, f_) == 0
