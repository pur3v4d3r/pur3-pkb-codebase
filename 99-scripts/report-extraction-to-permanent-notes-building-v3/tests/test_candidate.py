#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for ``lib.candidate``.

Covers normalization, single-callout construction, merge algebra (associativity
on content, commutativity on content, conflict resolution), JSON round-trip,
and content-hash determinism.
"""
from __future__ import annotations

import pytest

from lib.candidate import (
    BUCKET_FIELDS,
    CALLOUT_TYPE_TO_BUCKET,
    Candidate,
    DEFAULT_COMPLEXITY,
    DEFAULT_CONFIDENCE,
    DEFAULT_DOMAIN,
    DEFAULT_IMPORTANCE,
    EvidenceItem,
    SourceReport,
    callout_to_bucket,
    normalize_name,
)


# ═════════════════════════════════════════════════════════════════════════
# normalize_name
# ═════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("a,b", [
    ("Self-Determination Theory", "self determination theory"),
    ("self_determination_theory", "self determination theory"),
    ("  Self  Determination  Theory  ", "self determination theory"),
    ("Pintrich's Motivational Integration", "pintrich's motivational integration"),
    ("Schöne", "schone"),
    ("CafÉ", "cafe"),
])
def test_normalize_name_collapses_variants(a: str, b: str) -> None:
    assert normalize_name(a) == b


def test_normalize_name_groups_equivalent_forms() -> None:
    a = normalize_name("Self-Determination Theory")
    b = normalize_name("self_determination theory")
    c = normalize_name("SELF DETERMINATION THEORY")
    assert a == b == c


def test_normalize_name_empty() -> None:
    assert normalize_name("") == ""
    assert normalize_name("   ") == ""


# ═════════════════════════════════════════════════════════════════════════
# callout_to_bucket
# ═════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("ctype,bucket", [
    ("definition", "_definition"),
    ("key-claim", "evidence"),
    ("analytical-insight", "insights"),
    ("warning", "warnings"),
    ("reflection", "reflections"),
    ("ask-yourself-this", "open_questions"),
    ("tension-identified", "tensions"),
    ("methodology-and-sources", "methodology"),
    ("cite", "citations"),
    ("DEFINITION", "_definition"),     # case-insensitive
    ("  warning  ", "warnings"),       # whitespace-stripped
])
def test_callout_to_bucket_known(ctype: str, bucket: str) -> None:
    assert callout_to_bucket(ctype) == bucket


def test_callout_to_bucket_unknown_falls_to_evidence() -> None:
    assert callout_to_bucket("never-seen-before-type") == "evidence"
    assert callout_to_bucket("") == "evidence"
    assert callout_to_bucket(None) == "evidence"


def test_callout_to_bucket_map_targets_real_fields() -> None:
    """Every mapped target must be either '_definition' or a real bucket field."""
    for target in CALLOUT_TYPE_TO_BUCKET.values():
        assert target == "_definition" or target in BUCKET_FIELDS, (
            f"unknown bucket target: {target!r}"
        )


# ═════════════════════════════════════════════════════════════════════════
# from_callout
# ═════════════════════════════════════════════════════════════════════════

@pytest.fixture
def src() -> SourceReport:
    return SourceReport(batch="batch-1", file="file_validated.json", line=42)


def test_from_callout_definition_populates_definition_body(src: SourceReport) -> None:
    c = Candidate.from_callout(
        {"title": "Self-Determination Theory", "body": "SDT defines three needs.", "type": "definition"},
        src,
    )
    assert c.primary_name == "Self-Determination Theory"
    assert c.canonical_name == "Self-Determination Theory"
    assert c.definition_body == "SDT defines three needs."
    # Definition is also captured as evidence for provenance.
    assert len(c.evidence) == 1
    assert c.evidence[0].body == "SDT defines three needs."
    assert c.source_reports == (src,)


def test_from_callout_non_definition_files_into_bucket(src: SourceReport) -> None:
    c = Candidate.from_callout(
        {"title": "Autonomous Motivation", "body": "When the activity is enacted with willingness.",
         "type": "analytical-insight"},
        src,
    )
    assert c.definition_body == ""
    assert len(c.insights) == 1
    assert c.insights[0].callout_type == "analytical-insight"
    # Other buckets remain empty.
    assert c.evidence == ()
    assert c.warnings == ()


def test_from_callout_unknown_type_to_evidence(src: SourceReport) -> None:
    c = Candidate.from_callout(
        {"title": "Foo", "body": "Bar", "type": "wholly-novel-type"},
        src,
    )
    assert len(c.evidence) == 1


def test_from_callout_metadata_carried_through(src: SourceReport) -> None:
    c = Candidate.from_callout(
        {"title": "X", "body": "Y", "type": "definition"},
        src,
        domain="educational-psychology",
        subdomains=("motivation", "srl"),
        confidence="high",
        complexity="advanced-practitioner",
        importance="high",
        wiki_links_seen=("Foo", "Bar"),
    )
    assert c.domain == "educational-psychology"
    assert c.subdomains == ("motivation", "srl")
    assert c.confidence == "high"
    assert c.complexity == "advanced-practitioner"
    assert c.importance == "high"
    assert c.wiki_links_seen == ("Foo", "Bar")


def test_from_callout_computes_extraction_hash(src: SourceReport) -> None:
    c = Candidate.from_callout(
        {"title": "X", "body": "Y", "type": "definition"}, src,
    )
    assert len(c.extraction_hash) == 64  # sha256 hex


# ═════════════════════════════════════════════════════════════════════════
# merge
# ═════════════════════════════════════════════════════════════════════════

def _cand(title: str, body: str, ctype: str, batch: str, line: int = 1,
          **meta) -> Candidate:
    return Candidate.from_callout(
        {"title": title, "body": body, "type": ctype},
        SourceReport(batch=batch, file=f"{batch}.json", line=line),
        **meta,
    )


def test_merge_unions_evidence_and_sources() -> None:
    a = _cand("Self-Determination Theory", "definition body A", "definition", "b1")
    b = _cand("Self-Determination Theory", "insight body B", "analytical-insight", "b2")
    merged = a.merge(b)
    assert merged.primary_name == "Self-Determination Theory"
    assert merged.definition_body == "definition body A"
    assert len(merged.evidence) == 1   # from definition (a)
    assert len(merged.insights) == 1   # from b
    assert len(merged.source_reports) == 2


def test_merge_picks_first_non_empty_definition() -> None:
    a = _cand("X", "insight a", "analytical-insight", "b1")  # no definition
    b = _cand("X", "the definition", "definition", "b2")
    merged = a.merge(b)
    assert merged.definition_body == "the definition"


def test_merge_definition_self_wins_when_both_present() -> None:
    a = _cand("X", "def-A", "definition", "b1")
    b = _cand("X", "def-B", "definition", "b2")
    merged = a.merge(b)
    assert merged.definition_body == "def-A"


def test_merge_aliases_union() -> None:
    # Two same-key forms of differing length → shorter wins, longer becomes alias.
    a = _cand("Self-Determination  Theory", "x", "definition", "b1")  # double space
    b = _cand("Self-Determination Theory", "y", "definition", "b2")
    assert a.grouping_key == b.grouping_key
    merged = a.merge(b)
    assert merged.primary_name == "Self-Determination Theory"
    assert "Self-Determination  Theory" in merged.aliases


def test_merge_aliases_equal_length_self_wins() -> None:
    # Equal-length canonical-key-equivalent forms → self wins, other becomes alias.
    a = _cand("Self-Determination Theory", "x", "definition", "b1")
    b = _cand("Self Determination Theory", "y", "definition", "b2")
    merged = a.merge(b)
    assert merged.primary_name == "Self-Determination Theory"
    assert "Self Determination Theory" in merged.aliases


def test_merge_rejects_different_grouping_keys() -> None:
    a = _cand("Apple", "x", "definition", "b1")
    b = _cand("Banana", "y", "definition", "b2")
    with pytest.raises(ValueError, match="grouping keys"):
        a.merge(b)


def test_merge_dedupes_identical_callouts() -> None:
    """Two callouts with the same (body, batch, file, line) are deduped."""
    a = _cand("X", "same body", "analytical-insight", "b1", line=10)
    b = _cand("X", "same body", "analytical-insight", "b1", line=10)
    merged = a.merge(b)
    assert len(merged.insights) == 1


def test_merge_preserves_corroboration_from_different_sources() -> None:
    """Same body from different files = legitimate corroboration; keep both."""
    a = _cand("X", "shared evidence", "key-claim", "b1", line=10)
    b = _cand("X", "shared evidence", "key-claim", "b2", line=10)
    merged = a.merge(b)
    assert len(merged.evidence) == 2


def test_merge_metadata_self_wins_unless_default() -> None:
    a = _cand("X", "a", "definition", "b1",
              domain=DEFAULT_DOMAIN, confidence=DEFAULT_CONFIDENCE)
    b = _cand("X", "b", "definition", "b2",
              domain="educational-psychology", confidence="high")
    merged = a.merge(b)
    # a's domain was default → b wins
    assert merged.domain == "educational-psychology"
    assert merged.confidence == "high"


def test_merge_metadata_self_wins_when_non_default() -> None:
    a = _cand("X", "a", "definition", "b1",
              domain="philosophy", confidence="high")
    b = _cand("X", "b", "definition", "b2",
              domain="educational-psychology", confidence="medium")
    merged = a.merge(b)
    assert merged.domain == "philosophy"
    assert merged.confidence == "high"


def test_merge_associative_on_content() -> None:
    """((a ∪ b) ∪ c) and (a ∪ (b ∪ c)) yield the same content (order-stable buckets)."""
    a = _cand("X", "A body", "key-claim", "b1", line=1)
    b = _cand("X", "B body", "analytical-insight", "b2", line=2)
    c = _cand("X", "C body", "warning", "b3", line=3)
    left = a.merge(b).merge(c)
    right = a.merge(b.merge(c))
    # Content checksum equal (order in evidence/insights/warnings same shape).
    assert left.extraction_hash == right.extraction_hash


def test_merge_recomputes_hash() -> None:
    a = _cand("X", "A", "definition", "b1")
    b = _cand("X", "B", "analytical-insight", "b2")
    merged = a.merge(b)
    assert merged.extraction_hash != a.extraction_hash
    assert merged.extraction_hash != b.extraction_hash


# ═════════════════════════════════════════════════════════════════════════
# JSON round-trip
# ═════════════════════════════════════════════════════════════════════════

def test_to_dict_from_dict_round_trip() -> None:
    a = _cand("Self-Determination Theory", "def body", "definition", "b1",
              domain="educational-psychology", subdomains=("motivation",),
              confidence="high", complexity="advanced-practitioner",
              importance="high", wiki_links_seen=("Autonomy", "Competence"))
    b = _cand("Self-Determination Theory", "insight body", "analytical-insight", "b2")
    merged = a.merge(b)
    d = merged.to_dict()
    rebuilt = Candidate.from_dict(d)
    assert rebuilt == merged


def test_to_dict_is_json_serializable() -> None:
    import json
    a = _cand("X", "Y", "definition", "b1")
    json.dumps(a.to_dict())  # must not raise


def test_from_dict_handles_missing_fields() -> None:
    """Backward-compatible read: missing keys take defaults, not raise."""
    minimal = {"primary_name": "X", "canonical_name": "X"}
    c = Candidate.from_dict(minimal)
    assert c.primary_name == "X"
    assert c.domain == DEFAULT_DOMAIN
    assert c.evidence == ()


# ═════════════════════════════════════════════════════════════════════════
# Properties
# ═════════════════════════════════════════════════════════════════════════

def test_grouping_key_is_normalized_primary_name() -> None:
    c = _cand("Self-Determination Theory", "x", "definition", "b1")
    assert c.grouping_key == normalize_name("Self-Determination Theory")


def test_all_items_concatenates_every_bucket() -> None:
    a = _cand("X", "ev1", "key-claim", "b1", line=1)
    b = _cand("X", "in1", "analytical-insight", "b2", line=2)
    c = _cand("X", "wn1", "warning", "b3", line=3)
    merged = a.merge(b).merge(c)
    bodies = [it.body for it in merged.all_items()]
    assert "ev1" in bodies and "in1" in bodies and "wn1" in bodies
    assert len(merged.all_items()) == 3
