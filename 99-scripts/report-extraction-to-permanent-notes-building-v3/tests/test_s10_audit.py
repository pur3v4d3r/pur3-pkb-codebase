#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for stages.s10_audit — Stage 10 audit + gate enforcement."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from stages import s10_audit


# ─── Helpers ────────────────────────────────────────────────────────────

def _write_note(notes_dir: Path, name: str, body: str, *, stub: bool = False) -> Path:
    """Write a minimal permanent note (or stub) to ``notes_dir/name``."""
    fm_lines = ["---", f"title: {name.removesuffix('.md')}", "tags:", "  - concept"]
    if stub:
        fm_lines.append("source-type: stub-generation")
    fm_lines.append("---")
    notes_dir.mkdir(parents=True, exist_ok=True)
    path = notes_dir / name
    path.write_text("\n".join(fm_lines) + "\n\n" + body, encoding="utf-8")
    return path


# ─── _is_stub_note ──────────────────────────────────────────────────────

def test_is_stub_note_detects_stub_marker(tmp_path: Path) -> None:
    p = _write_note(tmp_path, "Foo.md", "body", stub=True)
    assert s10_audit._is_stub_note(p) is True


def test_is_stub_note_returns_false_for_regular_note(tmp_path: Path) -> None:
    p = _write_note(tmp_path, "Foo.md", "body", stub=False)
    assert s10_audit._is_stub_note(p) is False


def test_is_stub_note_returns_false_on_missing_file(tmp_path: Path) -> None:
    assert s10_audit._is_stub_note(tmp_path / "missing.md") is False


# ─── _percentile ────────────────────────────────────────────────────────

def test_percentile_empty_returns_zero() -> None:
    assert s10_audit._percentile([], 50.0) == 0.0


def test_percentile_single_value() -> None:
    assert s10_audit._percentile([42.0], 50.0) == 42.0


def test_percentile_median_odd() -> None:
    assert s10_audit._percentile([1.0, 2.0, 3.0], 50.0) == 2.0


def test_percentile_median_even_interpolates() -> None:
    # Linear interpolation: pos = 1.5 → between 2 and 3
    assert s10_audit._percentile([1.0, 2.0, 3.0, 4.0], 50.0) == 2.5


# ─── GateResult ─────────────────────────────────────────────────────────

def test_gate_result_to_dict_round_trip() -> None:
    g = s10_audit.GateResult(
        name="resolution_rate", measured=0.96, target=0.95,
        comparator=">=", passed=True,
    )
    d = g.to_dict()
    assert d == {
        "name": "resolution_rate",
        "measured": 0.96,
        "target": 0.95,
        "comparator": ">=",
        "passed": True,
    }


# ─── evaluate_gates ─────────────────────────────────────────────────────

def _make_summary(**overrides) -> s10_audit.AuditSummary:
    base = dict(
        notes_dir="x",
        total_notes=100,
        unique_targets=200,
        resolved_targets=190,
        unresolved_targets=10,
        placeholder_targets=0,
        report_targets=0,
        missing_concepts=10,
        real_missing_concepts=4,
        resolution_rate=0.95,
        orphan_count=0,
        well_connected_count=0,
        quality_avg=60.0,
        quality_median=60.0,
        quality_min=40,
        quality_max=80,
        low_quality_count=2,
        low_quality_fraction=0.02,
        low_quality_threshold=40.0,
        stub_count=0,
        non_stub_count=100,
        quality_avg_non_stub=60.0,
        quality_median_non_stub=60.0,
    )
    base.update(overrides)
    return s10_audit.AuditSummary(**base)


def test_evaluate_gates_all_pass() -> None:
    s = _make_summary()
    gates = s10_audit.evaluate_gates(s)
    assert {g.name for g in gates} == {
        "resolution_rate", "avg_quality_non_stub",
        "low_quality_fraction", "missing_concepts",
    }
    assert all(g.passed for g in gates)


def test_evaluate_gates_resolution_fail() -> None:
    s = _make_summary(resolution_rate=0.50)
    gates = {g.name: g for g in s10_audit.evaluate_gates(s)}
    assert gates["resolution_rate"].passed is False
    assert gates["avg_quality_non_stub"].passed is True


def test_evaluate_gates_quality_uses_non_stub() -> None:
    # Overall quality dragged down by stubs, non-stub is fine
    s = _make_summary(quality_avg=30.0, quality_avg_non_stub=70.0)
    gates = {g.name: g for g in s10_audit.evaluate_gates(s)}
    assert gates["avg_quality_non_stub"].passed is True


def test_evaluate_gates_low_quality_fail() -> None:
    s = _make_summary(low_quality_fraction=0.10)
    gates = {g.name: g for g in s10_audit.evaluate_gates(s)}
    assert gates["low_quality_fraction"].passed is False


def test_evaluate_gates_missing_concepts_uses_real_missing() -> None:
    # Raw missing huge, but real_missing under threshold → PASS
    s = _make_summary(missing_concepts=5000, real_missing_concepts=10)
    gates = {g.name: g for g in s10_audit.evaluate_gates(s)}
    assert gates["missing_concepts"].passed is True


def test_evaluate_gates_missing_concepts_fail_when_real_missing_exceeds() -> None:
    s = _make_summary(real_missing_concepts=300)
    gates = {g.name: g for g in s10_audit.evaluate_gates(s)}
    assert gates["missing_concepts"].passed is False


# ─── enforce_gates ──────────────────────────────────────────────────────

def test_enforce_gates_passes_when_all_pass() -> None:
    s = _make_summary()
    out = s10_audit.enforce_gates(s)
    assert out.all_gates_passed is True


def test_enforce_gates_raises_on_failure() -> None:
    s = _make_summary(resolution_rate=0.10)
    with pytest.raises(s10_audit.GateFailure):
        s10_audit.enforce_gates(s, fail_on_violation=True)


def test_enforce_gates_no_raise_when_fail_on_violation_false() -> None:
    s = _make_summary(resolution_rate=0.10)
    out = s10_audit.enforce_gates(s, fail_on_violation=False)
    assert out.all_gates_passed is False


# ─── write_json_report ──────────────────────────────────────────────────

def test_write_json_report_shape(tmp_path: Path) -> None:
    s = _make_summary()
    s10_audit.enforce_gates(s, fail_on_violation=False)
    # Build a minimal AuditResult-like object (audit_notes.AuditResult is a
    # plain class with a no-arg ctor + setattr fields).
    audit = s10_audit.audit_notes.AuditResult()
    audit.missing_concepts = {}
    audit.unresolved = {}
    out = s10_audit.write_json_report(s, audit, tmp_path)
    assert out.exists()
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["summary"]["resolution_rate"] == 0.95
    assert payload["summary"]["all_gates_passed"] is True
    assert len(payload["summary"]["gates"]) == 4


# ─── run_audit_stage end-to-end on a tiny corpus ────────────────────────

def test_run_audit_stage_on_tiny_corpus(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    _write_note(notes, "Alpha.md",
                "Body refers to [[Beta]] and [[Gamma]].")
    _write_note(notes, "Beta.md", "Beta body.")
    _write_note(notes, "Gamma.md", "Gamma body.", stub=True)

    out_dir = tmp_path / "audit"
    summary = s10_audit.run_audit_stage(
        notes, out_dir, fail_on_violation=False, write_markdown=True,
    )
    assert summary.total_notes == 3
    assert summary.stub_count == 1
    assert summary.non_stub_count == 2
    assert (out_dir / "audit-report.json").exists()
    assert (out_dir / "audit-report.md").exists()


def test_run_audit_stage_writes_report_even_on_failure(tmp_path: Path) -> None:
    notes = tmp_path / "notes"
    # Single note linking to many missing concepts to trip resolution gate
    body = " ".join(f"[[Missing-{i}]]" for i in range(50))
    _write_note(notes, "Hub.md", body)
    out_dir = tmp_path / "audit"
    with pytest.raises(s10_audit.GateFailure):
        s10_audit.run_audit_stage(
            notes, out_dir, fail_on_violation=True, write_markdown=False,
        )
    # Report must exist even though gates failed
    assert (out_dir / "audit-report.json").exists()
