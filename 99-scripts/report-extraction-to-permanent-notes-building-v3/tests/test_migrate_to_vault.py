#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for migrate_to_vault.

Run with:
    pytest tests/test_migrate_to_vault.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_PROJ = _HERE.parent
if str(_PROJ) not in sys.path:
    sys.path.insert(0, str(_PROJ))

import migrate_to_vault as mv  # noqa: E402


# --- kebab_filename ---------------------------------------------------------

@pytest.mark.parametrize("raw,expected", [
    ("4CID Blueprint Completeness Checklist",          "4cid-blueprint-completeness-checklist"),
    ("4CID Blueprint Completeness Checklist.md",       "4cid-blueprint-completeness-checklist"),
    ("2x2 Achievement Goal Framework",                 "2x2-achievement-goal-framework"),
    ("2\u00d72 Achievement Goal Framework",            "2x2-achievement-goal-framework"),
    ("Chunk (Miller, 1956; Chase & Simon, 1973)",      "chunk-miller-1956-chase-simon-1973"),
    ("Bandura's Self-Efficacy Theory",                 "banduras-self-efficacy-theory"),
    ("Jeroen van Merri\u00ebnboer",                    "jeroen-van-merrienboer"),
    ("",                                               ""),
])
def test_kebab_filename(raw: str, expected: str) -> None:
    assert mv.kebab_filename(raw) == expected


# --- parse / dump frontmatter ----------------------------------------------

def test_parse_frontmatter_happy() -> None:
    fm, body = mv.parse_frontmatter("---\ntitle: X\n---\nbody\n")
    assert fm == {"title": "X"}
    assert body.strip() == "body"


def test_dump_frontmatter_round_trip() -> None:
    fm = {"title": "X", "aliases": ["x", "X"], "tags": ["a", "b"]}
    text = mv.dump_frontmatter(fm)
    assert text.startswith("---\n") and text.endswith("---\n")
    parsed, _ = mv.parse_frontmatter(text + "body\n")
    assert parsed == fm


# --- normalize_frontmatter --------------------------------------------------

def test_normalize_adds_aliases() -> None:
    fm = {"title": "Foo Bar", "aliases": []}
    out, generated = mv.normalize_frontmatter(
        fm, source_title="Foo Bar", slug="foo-bar",
    )
    assert "Foo Bar" in out["aliases"]
    assert "foo-bar" in out["aliases"]
    assert generated == ["Foo Bar", "foo-bar"]


def test_normalize_preserves_existing_aliases() -> None:
    fm = {"title": "Foo Bar", "aliases": ["existing"]}
    out, _ = mv.normalize_frontmatter(
        fm, source_title="Foo Bar", slug="foo-bar",
    )
    assert "existing" in out["aliases"]
    assert "Foo Bar" in out["aliases"]
    assert "foo-bar" in out["aliases"]


def test_normalize_sets_required_defaults() -> None:
    fm: dict = {"title": "X"}
    out, _ = mv.normalize_frontmatter(fm, source_title="X", slug="x")
    assert out["type"] == "permanent-note"
    assert out["status"] == "evergreen"
    assert "permanent-note" in out["tags"]


# --- clean_related_line -----------------------------------------------------

def test_clean_related_dedupes_and_caps() -> None:
    content = (
        "[[A]] [[B]] [[A]] [[A]] [[C]] [[B]] [[D]] [[E]] [[A]] [[F]]"
    )
    cleaned, before, after = mv.clean_related_line(content, top_n=3)
    assert before == 10
    assert after == 3
    # Top 3 by frequency: A (4x), B (2x), then C/D/E/F all tied at 1 -> first one (C)
    assert cleaned == "[[A]] \u00b7 [[B]] \u00b7 [[C]]"


def test_clean_related_preserves_aliased_links() -> None:
    content = "[[Foo|Foo Display]] [[Foo|Foo Display]] [[Bar]]"
    cleaned, before, after = mv.clean_related_line(content, top_n=10)
    assert before == 3
    assert after == 2
    assert "[[Foo|Foo Display]]" in cleaned
    assert "[[Bar]]" in cleaned


def test_clean_related_handles_empty() -> None:
    cleaned, before, after = mv.clean_related_line("no links here", top_n=10)
    assert before == 0
    assert after == 0


# --- transform_body ---------------------------------------------------------

def test_transform_body_cleans_related_line() -> None:
    body = (
        "## Connections\n\n"
        "**Related:** [[A]] [[B]] [[A]] [[A]]\n\n"
        "Other content.\n"
    )
    new_body, before, after = mv.transform_body(body, top_related=10)
    assert before == 4
    assert after == 2
    assert "**Related:** [[A]] \u00b7 [[B]]" in new_body
    assert "Other content." in new_body


def test_transform_body_no_related_line_unchanged() -> None:
    body = "## Connections\n\nNo related line here.\n"
    new_body, before, after = mv.transform_body(body, top_related=10)
    assert new_body == body
    assert before == 0 and after == 0


# --- end-to-end migration ---------------------------------------------------

_SAMPLE = """---
title: "4C/ID Blueprint Completeness Checklist"
aliases: []
type: permanent-note
status: evergreen
tags: [permanent-note, instructional-design]
---

# 4C/ID Blueprint Completeness Checklist

> [!definition]
> some def.

## Connections

**Related:** [[A]] [[B]] [[A]] [[C]] [[A]]
"""


def _write(tmp: Path, name: str, text: str) -> Path:
    p = tmp / name
    p.write_text(text, encoding="utf-8")
    return p


def test_migrate_one_dry_run_writes_nothing(tmp_path: Path) -> None:
    src = _write(tmp_path, "4C_ID Blueprint Completeness Checklist.md", _SAMPLE)
    staging = tmp_path / "out"
    rec = mv.migrate_one(
        src, staging_dir=staging, vault_index=set(),
        top_related=10, dry_run=True,
    )
    assert rec.outcome == mv.Outcome.DRY_RUN
    assert not staging.exists()
    assert rec.new_filename == "4c-id-blueprint-completeness-checklist.md"
    assert rec.related_links_before == 5
    assert rec.related_links_after == 3


def test_migrate_one_writes_normalized_file(tmp_path: Path) -> None:
    src = _write(tmp_path, "4C_ID Blueprint Completeness Checklist.md", _SAMPLE)
    staging = tmp_path / "out"
    rec = mv.migrate_one(
        src, staging_dir=staging, vault_index=set(),
        top_related=10, dry_run=False,
    )
    assert rec.outcome == mv.Outcome.MIGRATED
    new_file = staging / "4c-id-blueprint-completeness-checklist.md"
    assert new_file.exists()
    content = new_file.read_text(encoding="utf-8")
    # frontmatter normalized
    assert "title: 4C/ID Blueprint Completeness Checklist" in content
    assert "4c-id-blueprint-completeness-checklist" in content  # alias added
    # related-line deduped
    assert "**Related:** [[A]] \u00b7 [[B]] \u00b7 [[C]]" in content


def test_migrate_one_skips_collision(tmp_path: Path) -> None:
    src = _write(tmp_path, "Foo.md", _SAMPLE.replace(
        "4C/ID Blueprint Completeness Checklist", "Foo"
    ))
    staging = tmp_path / "out"
    rec = mv.migrate_one(
        src, staging_dir=staging,
        vault_index={"foo"},  # already exists in vault
        top_related=10, dry_run=False,
    )
    assert rec.outcome == mv.Outcome.SKIPPED_COLLISION
    assert not staging.exists()


def test_run_migration_end_to_end(tmp_path: Path) -> None:
    src_dir = tmp_path / "src"; src_dir.mkdir()
    vault_dir = tmp_path / "vault"; vault_dir.mkdir()
    (vault_dir / "existing-note.md").write_text("---\n---\n", encoding="utf-8")

    _write(src_dir, "Foo Bar.md", _SAMPLE.replace(
        "4C/ID Blueprint Completeness Checklist", "Foo Bar"
    ))
    _write(src_dir, "Existing Note.md", _SAMPLE.replace(
        "4C/ID Blueprint Completeness Checklist", "Existing Note"
    ))

    staging = tmp_path / "stage"
    records, stats = mv.run_migration(
        src_dir, staging, vault_dir,
        top_related=10, dry_run=False,
    )
    assert stats["total"] == 2
    assert stats[mv.Outcome.MIGRATED] == 1
    assert stats[mv.Outcome.SKIPPED_COLLISION] == 1
    assert (staging / "foo-bar.md").exists()
    assert not (staging / "existing-note.md").exists()
