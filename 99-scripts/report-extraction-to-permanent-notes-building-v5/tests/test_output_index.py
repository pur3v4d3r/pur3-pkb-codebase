#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for lib/output_index.py."""
from __future__ import annotations

from pathlib import Path

import pytest

from v5lib.output_index import (
    OutputIndex,
    _extract_frontmatter,
    normalize_title,
)


# ─── normalize_title ────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected", [
    ("Self-Determination Theory", "self determination theory"),
    ("[[Self Determination Theory]]", "self determination theory"),
    ("  self---determination___theory  ", "self determination theory"),
    ("Self-Determination Theory!", "self determination theory"),
    ("UPPER_lower", "upper lower"),
    ("", ""),
])
def test_normalize_title(raw: str, expected: str) -> None:
    assert normalize_title(raw) == expected


# ─── _extract_frontmatter ───────────────────────────────────────────────

def test_extract_frontmatter_inline_aliases() -> None:
    txt = (
        "---\n"
        'title: "Self-Determination Theory"\n'
        "status: enriched\n"
        'aliases: ["SDT", "Deci & Ryan"]\n'
        "---\n"
        "# Body\n"
    )
    fm = _extract_frontmatter(txt)
    assert fm["title"] == "Self-Determination Theory"
    assert fm["status"] == "enriched"
    assert fm["aliases"] == ["SDT", "Deci & Ryan"]


def test_extract_frontmatter_block_aliases() -> None:
    txt = (
        "---\n"
        'title: "X"\n'
        "aliases:\n"
        '  - "alpha"\n'
        '  - "beta"\n'
        "status: budding\n"
        "---\n"
    )
    fm = _extract_frontmatter(txt)
    assert fm["aliases"] == ["alpha", "beta"]
    assert fm["status"] == "budding"


def test_extract_frontmatter_missing_returns_empty() -> None:
    assert _extract_frontmatter("no frontmatter here") == {}


# ─── OutputIndex ────────────────────────────────────────────────────────

def _write_note(
    dir_: Path, slug: str, title: str, status: str = "enriched",
    aliases: list[str] | None = None,
) -> Path:
    aliases = aliases or []
    alias_block = "[" + ", ".join(f'"{a}"' for a in aliases) + "]"
    txt = (
        "---\n"
        f'title: "{title}"\n'
        f"status: {status}\n"
        f"aliases: {alias_block}\n"
        "---\n"
        f"# {title}\n"
    )
    p = dir_ / f"{slug}.md"
    p.write_text(txt, encoding="utf-8")
    return p


def test_build_indexes_only_top_level(tmp_path: Path) -> None:
    p1 = _write_note(tmp_path, "self-determination-theory",
                     "Self-Determination Theory", aliases=["SDT"])
    p2 = _write_note(tmp_path, "cognitive-load-theory",
                     "Cognitive Load Theory", status="seedling")
    sub = tmp_path / "subdir"
    sub.mkdir()
    _write_note(sub, "ignored", "Should Be Ignored")

    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    assert len(idx) == 2
    assert "self-determination-theory" in idx
    assert idx.by_slug["self-determination-theory"] == p1
    assert idx.by_alias["sdt"] == p1
    assert idx.by_norm_title["self determination theory"] == p1
    assert idx.status_of(p2) == "seedling"


def test_build_missing_dir_raises(tmp_path: Path) -> None:
    nonexistent = tmp_path / "nope"
    with pytest.raises(FileNotFoundError):
        OutputIndex(output_dir=nonexistent).build()


def test_build_handles_unreadable_files(tmp_path: Path, caplog) -> None:
    good = _write_note(tmp_path, "good", "Good Title")
    bad = tmp_path / "bad.md"
    bad.write_bytes(b"\xff\xfe\xfd not utf8")
    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    # Bad file may register with empty fm but should not crash; good must work.
    assert good in idx.by_slug.values()
