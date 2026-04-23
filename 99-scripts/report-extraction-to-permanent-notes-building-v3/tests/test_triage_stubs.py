#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for triage_stubs.

Run with:
    pytest tests/test_triage_stubs.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make the script importable when run from the project root
_HERE = Path(__file__).resolve().parent
_PROJ = _HERE.parent
if str(_PROJ) not in sys.path:
    sys.path.insert(0, str(_PROJ))

import triage_stubs as ts  # noqa: E402


# ─── normalize_key ──────────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected", [
    ("Achievement Goal",                                          "achievement-goal"),
    ("Achievement-Goal.md",                                       "achievement-goal"),
    ("Achievement Goal (Achievement Goal Theory tradition)",      "achievement-goal"),
    ("achievement-goal-theory",                                   "achievement-goal-theory"),
    ("Bandura's Self-Efficacy Theory",                            "banduras-self-efficacy-theory"),
    ("",                                                          ""),
    ("   ",                                                       ""),
    ("4CID — Blueprint Completeness Checklist",                   "4cid-blueprint-completeness-checklist"),
    ("2×2 Achievement Goal Framework",                            "2-2-achievement-goal-framework"),
])
def test_normalize_key(raw: str, expected: str) -> None:
    assert ts.normalize_key(raw) == expected


# ─── parse_frontmatter ──────────────────────────────────────────────────────

def test_parse_frontmatter_happy_path() -> None:
    text = "---\ntitle: Foo\naliases: [F, foo]\n---\nbody here\n"
    fm, body = ts.parse_frontmatter(text)
    assert fm == {"title": "Foo", "aliases": ["F", "foo"]}
    assert body.strip() == "body here"


def test_parse_frontmatter_no_block() -> None:
    fm, body = ts.parse_frontmatter("just body, no fm")
    assert fm == {}
    assert body == "just body, no fm"


def test_parse_frontmatter_malformed_yaml_returns_empty() -> None:
    text = "---\nthis: is: not: valid: yaml: [\n---\nbody\n"
    fm, _ = ts.parse_frontmatter(text)
    assert fm == {}


# ─── parse_stub ─────────────────────────────────────────────────────────────

def _write(tmp: Path, name: str, text: str) -> Path:
    p = tmp / name
    p.write_text(text, encoding="utf-8")
    return p


def test_parse_stub_extracts_ref_count(tmp_path: Path) -> None:
    p = _write(tmp_path, "x.md",
               "---\ntitle: X\nreferenced-by-count: 42\n---\nbody\n")
    stub = ts.parse_stub(p)
    assert stub is not None
    assert stub.title == "X"
    assert stub.ref_count == 42
    assert stub.normalized_key == "x"


def test_parse_stub_falls_back_to_filename(tmp_path: Path) -> None:
    p = _write(tmp_path, "Some Concept.md", "---\n---\n# Some Concept\n")
    stub = ts.parse_stub(p)
    assert stub is not None
    assert stub.title == "Some Concept"


# ─── classify_stub ──────────────────────────────────────────────────────────

def _make(key: str = "x", **kw: object) -> ts.StubCandidate:
    base = dict(
        path=Path("x.md"), title=key, normalized_key=key,
        ref_count=0, alias_count=0, body_len=0, h2_count=0,
        has_real_definition=False, aliases=[],
    )
    base.update(kw)
    return ts.StubCandidate(**base)  # type: ignore[arg-type]


def test_classify_skips_already_enriched_by_key() -> None:
    s = _make("achievement-goal")
    ts.classify_stub(s, {"achievement-goal"})
    assert s.decision == ts.Decision.SKIP_ALREADY_ENRICHED


def test_classify_skips_already_enriched_by_alias() -> None:
    s = _make("ag", aliases=["achievement-goal"])
    ts.classify_stub(s, {"achievement-goal"})
    assert s.decision == ts.Decision.SKIP_ALREADY_ENRICHED


def test_classify_marks_comprehensive() -> None:
    s = _make("foo", body_len=2000, h2_count=3, has_real_definition=True)
    ts.classify_stub(s, set())
    assert s.decision == ts.Decision.READY_FOR_VAULT


def test_classify_marks_low_signal() -> None:
    s = _make("foo", body_len=10, ref_count=0)
    ts.classify_stub(s, set())
    assert s.decision == ts.Decision.SKIP_LOW_SIGNAL


def test_classify_marks_candidate_when_refs_present() -> None:
    s = _make("foo", body_len=10, ref_count=15)
    ts.classify_stub(s, set())
    assert s.decision == ts.Decision.CANDIDATE


# ─── score_stub ─────────────────────────────────────────────────────────────

def test_score_dominated_by_ref_count() -> None:
    high = _make("a", ref_count=100)
    low = _make("b", ref_count=1, alias_count=10, body_len=999)
    assert ts.score_stub(high) > ts.score_stub(low)


# ─── dedupe_by_key ──────────────────────────────────────────────────────────

def test_dedupe_keeps_highest_scoring_variant() -> None:
    a = _make("k", ref_count=5);    a.score = ts.score_stub(a)
    b = _make("k", ref_count=50);   b.score = ts.score_stub(b)
    a.decision = ts.Decision.CANDIDATE
    b.decision = ts.Decision.CANDIDATE
    ts.dedupe_by_key([a, b])
    assert b.decision == ts.Decision.CANDIDATE
    assert a.decision == ts.Decision.SKIP_DUPLICATE


# ─── select_top_n ───────────────────────────────────────────────────────────

def test_select_top_n_caps_keepers() -> None:
    pool: list[ts.StubCandidate] = []
    for i in range(10):
        s = _make(f"k{i}", ref_count=i)
        s.score = ts.score_stub(s)
        s.decision = ts.Decision.CANDIDATE
        pool.append(s)
    keepers = ts.select_top_n(pool, top_n=3)
    assert len(keepers) == 3
    assert all(k.decision == ts.Decision.CANDIDATE for k in keepers)
    rejected = [s for s in pool if s.decision == ts.Decision.NOT_SELECTED]
    assert len(rejected) == 7


# ─── end-to-end I/O ─────────────────────────────────────────────────────────

def test_run_triage_dry_run_writes_nothing(tmp_path: Path) -> None:
    src = tmp_path / "src"; src.mkdir()
    tgt = tmp_path / "tgt"; tgt.mkdir()
    out = tmp_path / "out"
    _write(src, "Foo.md", "---\ntitle: Foo\nreferenced-by-count: 99\n---\nbody\n")
    stats = ts.run_triage(src, tgt, out, top_n=10, include_comprehensive=False, dry_run=True)
    assert stats["total"] == 1
    assert not out.exists()


def test_run_triage_copies_candidates(tmp_path: Path) -> None:
    src = tmp_path / "src"; src.mkdir()
    tgt = tmp_path / "tgt"; tgt.mkdir()
    out = tmp_path / "out"
    _write(src, "Foo.md", "---\ntitle: Foo\nreferenced-by-count: 99\n---\nbody\n")
    _write(src, "Bar.md", "---\ntitle: Bar\nreferenced-by-count: 50\n---\nbody\n")
    stats = ts.run_triage(src, tgt, out, top_n=10, include_comprehensive=False, dry_run=False)
    assert (out / "curated-for-enrichment" / "Foo.md").exists()
    assert (out / "curated-for-enrichment" / "Bar.md").exists()
    assert (out / "triage-report.csv").exists()
    assert stats["curated_copied"] == 2
