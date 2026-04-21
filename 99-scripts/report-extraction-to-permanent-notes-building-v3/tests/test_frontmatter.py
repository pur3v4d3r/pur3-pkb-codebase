#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for lib/frontmatter.py."""
from __future__ import annotations

import datetime as dt

from lib.candidate import Candidate, EvidenceItem, SourceReport
from lib.frontmatter import (
    build_frontmatter,
    merge_frontmatter,
    parse_frontmatter,
    render_frontmatter,
)


def _make_candidate(**kw) -> Candidate:
    src = SourceReport(batch="b1", file="report-2026-04-12_validated.json", line=10)
    ev = EvidenceItem(body="Some evidence body.", title="E1",
                      callout_type="evidence", source=src)
    defaults = dict(
        canonical_name="Self-Determination Theory",
        primary_name="Self-Determination Theory",
        aliases=("SDT", "Self Determination Theory"),
        domain="educational-psychology",
        subdomains=("motivation",),
        confidence="high",
        complexity="advanced-practitioner",
        importance="high",
        definition_body="A macro-theory of human motivation.",
        evidence=(ev,),
        source_reports=(src,),
        wiki_links_seen=("Intrinsic-Motivation",),
    )
    defaults.update(kw)
    return Candidate(**defaults)


# ─── build ───────────────────────────────────────────────────────────────

def test_build_includes_required_fields() -> None:
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    assert fm["title"] == "Self-Determination Theory"
    assert "SDT" in fm["aliases"]
    assert fm["type"] == "permanent-note"
    assert fm["confidence"] == "high"
    assert fm["domain"] == "educational-psychology"
    assert fm["created"] == "2026-04-21"
    assert fm["updated"] == "2026-04-21"
    assert fm["provenance"]["pipeline-version"] == "3.0.0"
    assert fm["provenance"]["source-reports"] == ["report-2026-04-12"]


def test_build_drops_alias_equal_to_title() -> None:
    c = _make_candidate(aliases=("Self-Determination Theory", "SDT"))
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    assert "Self-Determination Theory" not in fm["aliases"]
    assert "SDT" in fm["aliases"]


def test_build_relationships_omitted_when_empty() -> None:
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    assert "relationships" not in fm


def test_build_relationships_included_when_provided() -> None:
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21),
                            related=("Autonomy",), builds_on=("CET",))
    assert fm["relationships"]["related"] == ["[[Autonomy]]"]
    assert fm["relationships"]["builds-on"] == ["[[CET]]"]


def test_build_tags_include_domain() -> None:
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    assert "permanent-note" in fm["tags"]
    assert "educational-psychology" in fm["tags"]


# ─── render ──────────────────────────────────────────────────────────────

def test_render_produces_yaml_block() -> None:
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    out = render_frontmatter(fm)
    assert out.startswith("---\n")
    assert out.rstrip().endswith("---")
    assert "title:" in out


def test_render_line_count_under_25_for_typical_note() -> None:
    """Spec §3.2 target: ≤25 frontmatter lines for typical notes."""
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    out = render_frontmatter(fm)
    line_count = out.count("\n")
    assert line_count <= 25, f"frontmatter is {line_count} lines, target ≤25:\n{out}"


# ─── parse ───────────────────────────────────────────────────────────────

def test_parse_extracts_dict_and_body() -> None:
    text = "---\ntitle: X\ntags:\n  - a\n---\n# Body\ncontent here"
    fm, body = parse_frontmatter(text)
    assert fm["title"] == "X"
    assert fm["tags"] == ["a"]
    assert body.startswith("# Body")


def test_parse_no_frontmatter() -> None:
    text = "# Just a body"
    fm, body = parse_frontmatter(text)
    assert fm == {}
    assert body == text


def test_parse_round_trip() -> None:
    c = _make_candidate()
    fm = build_frontmatter(c, today=dt.date(2026, 4, 21))
    rendered = render_frontmatter(fm)
    parsed, _body = parse_frontmatter(rendered + "body\n")
    assert parsed["title"] == "Self-Determination Theory"
    assert parsed["confidence"] == "high"
    # source-reports survives round-trip
    assert parsed["provenance"]["source-reports"] == ["report-2026-04-12"]


# ─── merge ───────────────────────────────────────────────────────────────

def test_merge_preserves_user_status() -> None:
    existing = {"status": "evergreen-curated", "title": "X"}
    fresh = {"status": "evergreen", "title": "X", "updated": "2026-05-01"}
    out = merge_frontmatter(existing, fresh)
    assert out["status"] == "evergreen-curated"
    assert out["updated"] == "2026-05-01"


def test_merge_preserves_created_date() -> None:
    existing = {"created": "2025-01-01"}
    fresh = {"created": "2026-04-21", "updated": "2026-04-21"}
    out = merge_frontmatter(existing, fresh)
    assert out["created"] == "2025-01-01"
    assert out["updated"] == "2026-04-21"


def test_merge_unions_user_tags() -> None:
    existing = {"tags": ["my-custom-tag", "permanent-note"]}
    fresh = {"tags": ["permanent-note", "auto-tag"]}
    out = merge_frontmatter(existing, fresh)
    assert out["tags"] == ["my-custom-tag", "permanent-note", "auto-tag"]


def test_merge_unions_aliases() -> None:
    existing = {"aliases": ["My-Alias"]}
    fresh = {"aliases": ["SDT"]}
    out = merge_frontmatter(existing, fresh)
    assert "My-Alias" in out["aliases"]
    assert "SDT" in out["aliases"]


def test_merge_unions_source_reports() -> None:
    existing = {"provenance": {"source-reports": ["report-A"]}}
    fresh = {"provenance": {"source-reports": ["report-B"], "source-type": "x"}}
    out = merge_frontmatter(existing, fresh)
    assert out["provenance"]["source-reports"] == ["report-A", "report-B"]


def test_merge_unions_relationships_per_edge() -> None:
    existing = {"relationships": {"related": ["[[A]]"], "builds-on": ["[[X]]"]}}
    fresh = {"relationships": {"related": ["[[B]]"]}}
    out = merge_frontmatter(existing, fresh)
    assert "[[A]]" in out["relationships"]["related"]
    assert "[[B]]" in out["relationships"]["related"]
    assert out["relationships"]["builds-on"] == ["[[X]]"]


def test_merge_fresh_wins_on_canonical_fields() -> None:
    existing = {"confidence": "low", "domain": "old-domain"}
    fresh = {"confidence": "high", "domain": "new-domain"}
    out = merge_frontmatter(existing, fresh)
    assert out["confidence"] == "high"
    assert out["domain"] == "new-domain"
