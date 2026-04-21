#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for stages.s5_match — uses a stub model so no GPU/HF needed.

Run with:
    pytest tests/test_s5_match.py -v
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pytest

_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
if str(_V3_ROOT) not in sys.path:
    sys.path.insert(0, str(_V3_ROOT))

from lib.candidate import Candidate, EvidenceItem, SourceReport  # noqa: E402
from lib.embeddings import EMBEDDING_DIM, EmbeddingStore  # noqa: E402
from stages.s5_match import (  # noqa: E402
    AUTO_MATCH_THRESHOLD,
    REVIEW_QUEUE_THRESHOLD,
    ExistingNote,
    MatchError,
    classify,
    hybrid_score,
    load_existing_notes,
    match_candidates,
    string_similarity,
    write_report,
)


# ─── classify / hybrid_score / string_similarity ─────────────────────────

def test_classify_bands() -> None:
    assert classify(1.0) == "matched"
    assert classify(AUTO_MATCH_THRESHOLD) == "matched"
    assert classify(0.85) == "review_queue"
    assert classify(REVIEW_QUEUE_THRESHOLD) == "review_queue"
    assert classify(0.5) == "new"
    assert classify(0.0) == "new"


def test_hybrid_score_formula() -> None:
    # 0.4*1.0 + 0.6*0.5 = 0.7
    assert hybrid_score(1.0, 0.5) == pytest.approx(0.7)


def test_hybrid_score_clamped_to_unit_interval() -> None:
    assert hybrid_score(2.0, 2.0) == 1.0
    assert hybrid_score(-1.0, -1.0) == 0.0


def test_string_similarity_case_insensitive() -> None:
    assert string_similarity("Foo Bar", "foo bar") == pytest.approx(1.0)
    assert string_similarity("foo", "bar") < 0.5


# ─── load_existing_notes ─────────────────────────────────────────────────

def _write_note(p: Path, title: str, aliases: list[str] | None = None) -> None:
    aliases_part = ""
    if aliases:
        aliases_part = "aliases: [" + ", ".join(aliases) + "]\n"
    p.write_text(
        f"---\ntitle: {title}\n{aliases_part}---\n\n# {title}\nbody\n",
        encoding="utf-8",
    )


def test_load_existing_notes_parses_frontmatter(tmp_path: Path) -> None:
    _write_note(tmp_path / "Foo.md", "Foo Concept", ["FC", "foo-c"])
    _write_note(tmp_path / "Bar.md", "Bar Concept")
    notes = load_existing_notes(tmp_path)
    assert len(notes) == 2
    titles = sorted(n.title for n in notes)
    assert titles == ["Bar Concept", "Foo Concept"]
    foo = next(n for n in notes if n.title == "Foo Concept")
    assert foo.aliases == ("FC", "foo-c")


def test_load_existing_notes_empty_dir(tmp_path: Path) -> None:
    assert load_existing_notes(tmp_path) == []


def test_load_existing_notes_missing_dir(tmp_path: Path) -> None:
    assert load_existing_notes(tmp_path / "nope") == []


def test_existing_note_text_includes_aliases(tmp_path: Path) -> None:
    n = ExistingNote(path=tmp_path / "x.md", mtime=1.0, title="Foo", aliases=("Bar",))
    assert "Foo" in n.text and "Bar" in n.text


def test_existing_note_text_without_aliases(tmp_path: Path) -> None:
    n = ExistingNote(path=tmp_path / "x.md", mtime=1.0, title="Foo", aliases=())
    assert n.text == "Foo"


# ─── match_candidates with a deterministic stub model ────────────────────

class _DeterministicModel:
    """Stub that returns a fixed vector per text fragment.

    ``mapping`` overrides the default hash-bucket vector so individual tests
    can engineer specific cosine values.
    """

    def __init__(self, mapping: dict[str, np.ndarray] | None = None) -> None:
        self.mapping = mapping or {}

    def encode(self, texts, **_kwargs):
        out = np.zeros((len(texts), EMBEDDING_DIM), dtype=np.float32)
        for i, t in enumerate(texts):
            if t in self.mapping:
                v = self.mapping[t].astype(np.float32)
            else:
                v = np.zeros(EMBEDDING_DIM, dtype=np.float32)
                v[hash(t) % EMBEDDING_DIM] = 1.0
            # L2-normalize to mirror normalize_embeddings=True.
            n = np.linalg.norm(v)
            out[i] = v if n == 0 else v / n
        return out


def _candidate(name: str, aliases: tuple[str, ...] = ()) -> Candidate:
    src = SourceReport(batch="b", file="f.json", line=0)
    ev = EvidenceItem(body="x", title=name, callout_type="definition", source=src)
    return Candidate(
        canonical_name=name,
        primary_name=name,
        aliases=aliases,
        evidence=(ev,),
        source_reports=(src,),
    )


def test_no_existing_notes_marks_all_new(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    model = _DeterministicModel()
    cands = [_candidate("Foo"), _candidate("Bar")]
    decisions, stats = match_candidates(cands, [], store=store, model=model)
    assert all(d.status == "new" for d in decisions)
    assert stats.by_status["new"] == 2
    assert stats.encoded_existing == 0


def test_identical_text_yields_match(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    same_vec = np.ones(EMBEDDING_DIM, dtype=np.float32)
    model = _DeterministicModel(mapping={"Cognitive Load Theory": same_vec})
    note_path = tmp_path / "CLT.md"
    note_path.write_text("---\ntitle: x\n---\n\n", encoding="utf-8")
    note = ExistingNote(
        path=note_path, mtime=1.0,
        title="Cognitive Load Theory", aliases=(),
    )
    cands = [_candidate("Cognitive Load Theory")]
    decisions, _stats = match_candidates(cands, [note], store=store, model=model)
    assert decisions[0].status == "matched"
    assert decisions[0].matched_path == "CLT.md"
    assert decisions[0].score >= AUTO_MATCH_THRESHOLD


def test_unrelated_concepts_marked_new(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    v_a = np.zeros(EMBEDDING_DIM, dtype=np.float32); v_a[0] = 1.0
    v_b = np.zeros(EMBEDDING_DIM, dtype=np.float32); v_b[100] = 1.0
    model = _DeterministicModel(mapping={
        "Fibonacci sequence": v_a,
        "Bayesian inference": v_b,
    })
    note_path = tmp_path / "Bayes.md"
    note_path.write_text("---\ntitle: x\n---\n\n", encoding="utf-8")
    note = ExistingNote(
        path=note_path, mtime=1.0, title="Bayesian inference", aliases=(),
    )
    cands = [_candidate("Fibonacci sequence")]
    decisions, _stats = match_candidates(cands, [note], store=store, model=model)
    assert decisions[0].status == "new"
    assert decisions[0].score < REVIEW_QUEUE_THRESHOLD


def test_partial_overlap_lands_in_review_band(tmp_path: Path) -> None:
    """Engineer a ~0.85 score: cosine 0.85, string ~0.85 → hybrid ~0.85."""
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    v_a = np.zeros(EMBEDDING_DIM, dtype=np.float32)
    v_b = np.zeros(EMBEDDING_DIM, dtype=np.float32)
    # cosine = cos(theta); for two unit vectors with components
    # (sqrt(0.85), sqrt(0.15)) and (1, 0) → cosine = sqrt(0.85) ≈ 0.922
    # We want ~0.85 cosine: vectors at angle arccos(0.85).
    import math
    cos_target = 0.85
    sin_target = math.sqrt(1 - cos_target ** 2)
    v_a[0] = 1.0
    v_b[0] = cos_target
    v_b[1] = sin_target
    model = _DeterministicModel(mapping={
        "Self-Determination Theory": v_a,
        "self determination model": v_b,  # close but not identical title
    })
    note_path = tmp_path / "SDT.md"
    note_path.write_text("---\ntitle: x\n---\n\n", encoding="utf-8")
    note = ExistingNote(
        path=note_path, mtime=1.0,
        title="self determination model", aliases=(),
    )
    cands = [_candidate("Self-Determination Theory")]
    decisions, _stats = match_candidates(cands, [note], store=store, model=model)
    # Just verify it lands in review_queue band (string sim alone won't push to matched).
    assert REVIEW_QUEUE_THRESHOLD <= decisions[0].score < AUTO_MATCH_THRESHOLD
    assert decisions[0].status == "review_queue"


def test_match_picks_best_among_many(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    v_target = np.ones(EMBEDDING_DIM, dtype=np.float32)
    model = _DeterministicModel(mapping={"target concept": v_target})
    notes = []
    for i, title in enumerate(["other one", "target concept", "third unrelated"]):
        p = tmp_path / f"n{i}.md"
        p.write_text("---\ntitle: x\n---\n\n", encoding="utf-8")
        notes.append(ExistingNote(path=p, mtime=float(i), title=title, aliases=()))
    cands = [_candidate("target concept")]
    decisions, _stats = match_candidates(cands, notes, store=store, model=model)
    assert decisions[0].matched_title == "target concept"


def test_stats_count_aggregates(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    model = _DeterministicModel()
    cands = [_candidate("alpha"), _candidate("beta"), _candidate("gamma")]
    _decisions, stats = match_candidates(cands, [], store=store, model=model)
    assert stats.candidates_total == 3
    assert sum(stats.by_status.values()) == 3


# ─── write_report ────────────────────────────────────────────────────────

def test_write_report_creates_json(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    model = _DeterministicModel()
    cands = [_candidate("alpha")]
    decisions, stats = match_candidates(cands, [], store=store, model=model)
    out = write_report(decisions, stats, tmp_path / "run-1")
    assert out.exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "decisions" in data and "stats" in data and "thresholds" in data
    assert data["stats"]["candidates_total"] == 1
    assert data["thresholds"]["auto_match"] == AUTO_MATCH_THRESHOLD


def test_write_report_preserves_decision_fields(tmp_path: Path) -> None:
    store = EmbeddingStore(path=tmp_path / "cache.npz")
    same_vec = np.ones(EMBEDDING_DIM, dtype=np.float32)
    model = _DeterministicModel(mapping={"Foo": same_vec})
    np_path = tmp_path / "Foo.md"
    np_path.write_text("---\ntitle: x\n---\n\n", encoding="utf-8")
    note = ExistingNote(path=np_path, mtime=1.0, title="Foo", aliases=())
    decisions, stats = match_candidates([_candidate("Foo")], [note], store=store, model=model)
    out = write_report(decisions, stats, tmp_path / "run-2")
    data = json.loads(out.read_text(encoding="utf-8"))
    d0 = data["decisions"][0]
    assert d0["candidate_name"] == "Foo"
    assert d0["status"] == "matched"
    assert d0["matched_path"] == "Foo.md"
    assert "score" in d0 and "string_sim" in d0 and "cosine_sim" in d0


# ─── error path ──────────────────────────────────────────────────────────

def test_load_candidates_missing_file_raises(tmp_path: Path) -> None:
    from stages.s5_match import _load_candidates
    with pytest.raises(FileNotFoundError):
        _load_candidates(tmp_path / "nope.json")


def test_load_candidates_bad_shape_raises(tmp_path: Path) -> None:
    from stages.s5_match import _load_candidates
    p = tmp_path / "bad.json"
    p.write_text(json.dumps({"not_candidates": []}), encoding="utf-8")
    with pytest.raises(MatchError):
        _load_candidates(p)
