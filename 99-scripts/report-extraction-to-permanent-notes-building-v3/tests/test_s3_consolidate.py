#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for ``stages.s3_consolidate``.

Covers discovery, candidate building from validated payloads, the consolidate
reduction, the evidence-loss checksum gate, the JSON snapshot output, and CLI
behavior (exit codes, dry-run, missing input).
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import pytest

from lib.candidate import Candidate, EvidenceItem, SourceReport, normalize_name
from stages import s3_consolidate as s3


# ═════════════════════════════════════════════════════════════════════════
# Fixtures: synthetic _validated.json payloads
# ═════════════════════════════════════════════════════════════════════════

def _validated_payload(
    callouts: list[dict],
    *,
    domain: str = "educational-psychology",
    confidence: str = "high",
    wiki_links: list[str] | None = None,
) -> dict:
    """Mimic the real Stage-2 output shape."""
    return {
        "schema_version": "1.0.0",
        "document_metadata": {
            "frontmatter": {
                "primary_domain": domain,
                "secondary_domains": ["motivation"],
                "confidence": confidence,
                "complexity": "advanced-practitioner",
                "importance": "high",
            },
        },
        "extracted_items": {
            "callouts": callouts,
            "wiki_links": [
                {"target": t, "kept": True} for t in (wiki_links or [])
            ],
        },
    }


@pytest.fixture
def two_batch_corpus(tmp_path: Path) -> Path:
    """Create a 2-batch corpus where one concept appears in both batches."""
    b1 = tmp_path / "batch-001"
    b2 = tmp_path / "batch-002"
    b1.mkdir()
    b2.mkdir()

    # Concept "Self-Determination Theory" in batch-001
    (b1 / "report-a_validated.json").write_text(
        json.dumps(_validated_payload([
            {"title": "Self-Determination Theory", "type": "definition",
             "body": "SDT defines three psychological needs.", "line_number": 12},
            {"title": "Autonomy", "type": "key-claim",
             "body": "Autonomy is the experience of volition.", "line_number": 25},
        ], wiki_links=["Autonomy", "Competence"])),
        encoding="utf-8",
    )
    # Concept "Self-Determination Theory" again in batch-002 with different body
    (b2 / "report-b_validated.json").write_text(
        json.dumps(_validated_payload([
            {"title": "Self-Determination Theory", "type": "analytical-insight",
             "body": "SDT predicts engagement when needs are met.", "line_number": 8},
            {"title": "Relatedness", "type": "key-claim",
             "body": "Relatedness is connection to others.", "line_number": 30},
        ], wiki_links=["Relatedness"])),
        encoding="utf-8",
    )
    return tmp_path


# ═════════════════════════════════════════════════════════════════════════
# discover_inputs
# ═════════════════════════════════════════════════════════════════════════

def test_discover_inputs_directory(two_batch_corpus: Path) -> None:
    found = s3.discover_inputs(two_batch_corpus)
    assert len(found) == 2
    assert {f.batch for f in found} == {"batch-001", "batch-002"}


def test_discover_inputs_single_file(two_batch_corpus: Path) -> None:
    one = next(two_batch_corpus.rglob("*_validated.json"))
    found = s3.discover_inputs(one)
    assert len(found) == 1
    assert found[0].file == one.name


def test_discover_inputs_missing_path_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        s3.discover_inputs(tmp_path / "nonexistent")


def test_discover_inputs_empty_dir_returns_empty(tmp_path: Path) -> None:
    assert s3.discover_inputs(tmp_path) == []


# ═════════════════════════════════════════════════════════════════════════
# candidates_from_validated
# ═════════════════════════════════════════════════════════════════════════

def test_candidates_from_validated_skips_titleless(tmp_path: Path) -> None:
    payload = _validated_payload([
        {"title": "", "type": "key-claim", "body": "no title", "line_number": 1},
        {"title": "Real", "type": "key-claim", "body": "yes", "line_number": 2},
    ])
    cands = s3.candidates_from_validated(payload, batch="b", file="f.json")
    assert len(cands) == 1
    assert cands[0].primary_name == "Real"


def test_candidates_from_validated_carries_frontmatter() -> None:
    payload = _validated_payload(
        [{"title": "X", "type": "definition", "body": "y", "line_number": 1}],
        domain="philosophy", confidence="medium",
    )
    cands = s3.candidates_from_validated(payload, batch="b", file="f.json")
    assert cands[0].domain == "philosophy"
    assert cands[0].confidence == "medium"


def test_candidates_from_validated_handles_extracted_content_alias(tmp_path: Path) -> None:
    """Some payloads may use the legacy ``extracted_content`` key."""
    payload = {
        "document_metadata": {"frontmatter": {}},
        "extracted_content": {
            "callouts": [{"title": "X", "type": "definition", "body": "y", "line_number": 1}],
            "wiki_links": [],
        },
    }
    cands = s3.candidates_from_validated(payload, batch="b", file="f.json")
    assert len(cands) == 1


# ═════════════════════════════════════════════════════════════════════════
# consolidate
# ═════════════════════════════════════════════════════════════════════════

def test_consolidate_groups_across_batches(two_batch_corpus: Path) -> None:
    raw: list[Candidate] = []
    for inp in s3.discover_inputs(two_batch_corpus):
        raw.extend(s3.candidates_from_validated(
            json.loads(inp.path.read_text(encoding="utf-8")),
            batch=inp.batch, file=inp.file,
        ))
    assert len(raw) == 4  # 2 callouts × 2 files

    consolidated = s3.consolidate(raw)
    by_key = {c.grouping_key: c for c in consolidated}
    assert "self determination theory" in by_key
    assert "autonomy" in by_key
    assert "relatedness" in by_key
    assert len(consolidated) == 3  # SDT collapsed from 2 → 1

    sdt = by_key["self determination theory"]
    # definition body preserved, insight evidence also preserved
    assert "three psychological needs" in sdt.definition_body
    # both source files contributed
    assert {s.batch for s in sdt.source_reports} == {"batch-001", "batch-002"}


def test_consolidate_skips_empty_grouping_key() -> None:
    """Candidates with empty primary_name are filtered out."""
    src = SourceReport(batch="b", file="f.json", line=1)
    junk = Candidate(canonical_name="", primary_name="")
    real = Candidate.from_callout(
        {"title": "X", "type": "definition", "body": "y"}, src,
    )
    out = s3.consolidate([junk, real])
    assert len(out) == 1
    assert out[0].primary_name == "X"


# ═════════════════════════════════════════════════════════════════════════
# Evidence-loss checksum
# ═════════════════════════════════════════════════════════════════════════

def test_evidence_signatures_match_after_clean_consolidation(
    two_batch_corpus: Path,
) -> None:
    inputs = s3.discover_inputs(two_batch_corpus)
    raw, consolidated, stats = s3.run_consolidation(inputs)
    assert stats["evidence_loss_checksum"] == "OK"
    assert stats["raw_candidates"] >= stats["consolidated_candidates"]

    raw_sig = s3.raw_evidence_signature(raw)
    cons_sig = s3.consolidated_evidence_signature(consolidated)
    assert raw_sig == cons_sig


def test_evidence_loss_detected(monkeypatch: pytest.MonkeyPatch,
                                two_batch_corpus: Path) -> None:
    """Patching consolidate to drop a candidate must trigger EvidenceLossError."""
    real_consolidate = s3.consolidate

    def lossy(cands):
        result = real_consolidate(cands)
        return result[:-1] if result else result  # drop the last one

    monkeypatch.setattr(s3, "consolidate", lossy)
    inputs = s3.discover_inputs(two_batch_corpus)
    with pytest.raises(s3.EvidenceLossError, match="checksum mismatch"):
        s3.run_consolidation(inputs)


# ═════════════════════════════════════════════════════════════════════════
# write_output
# ═════════════════════════════════════════════════════════════════════════

def test_write_output_round_trips(two_batch_corpus: Path, tmp_path: Path) -> None:
    inputs = s3.discover_inputs(two_batch_corpus)
    _, consolidated, stats = s3.run_consolidation(inputs)
    out = tmp_path / "snap.json"
    s3.write_output(consolidated, stats, out)
    assert out.exists()
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["stats"]["evidence_loss_checksum"] == "OK"
    assert len(payload["candidates"]) == len(consolidated)
    rebuilt = [Candidate.from_dict(d) for d in payload["candidates"]]
    assert rebuilt == consolidated


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

def test_cli_help_contains_examples(capsys: pytest.CaptureFixture) -> None:
    parser = s3.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--help"])
    out = capsys.readouterr().out
    assert "Examples:" in out
    assert "--dry-run" in out


def test_cli_main_dry_run_writes_nothing(two_batch_corpus: Path,
                                         tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    rc = s3.main([str(two_batch_corpus), "-o", str(out_dir), "--dry-run", "-q"])
    assert rc == 0
    assert not out_dir.exists() or not (out_dir / s3.OUTPUT_FILENAME).exists()


def test_cli_main_writes_snapshot(two_batch_corpus: Path, tmp_path: Path) -> None:
    out_dir = tmp_path / "out"
    rc = s3.main([str(two_batch_corpus), "-o", str(out_dir), "-q"])
    assert rc == 0
    snap = out_dir / s3.OUTPUT_FILENAME
    assert snap.exists()
    payload = json.loads(snap.read_text(encoding="utf-8"))
    assert payload["stats"]["evidence_loss_checksum"] == "OK"


def test_cli_missing_input_returns_2(tmp_path: Path) -> None:
    rc = s3.main([str(tmp_path / "nope"), "-q"])
    assert rc == 2


def test_cli_no_validated_files_returns_4(tmp_path: Path) -> None:
    rc = s3.main([str(tmp_path), "-q"])
    assert rc == 4


def test_cli_evidence_loss_returns_5(monkeypatch: pytest.MonkeyPatch,
                                     two_batch_corpus: Path,
                                     tmp_path: Path) -> None:
    real_consolidate = s3.consolidate
    monkeypatch.setattr(
        s3, "consolidate",
        lambda cands: real_consolidate(cands)[:-1] if real_consolidate(cands) else [],
    )
    rc = s3.main([str(two_batch_corpus), "-o", str(tmp_path / "o"), "-q"])
    assert rc == 5
