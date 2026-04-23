#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for lib/matcher.py."""
from __future__ import annotations

from pathlib import Path

import pytest

from v5lib.matcher import (
    DEFAULT_THRESHOLD,
    AmbiguousMatchError,
    Matcher,
    MatchResult,
)
from v5lib.output_index import OutputIndex


def _write(dir_: Path, slug: str, title: str, aliases: list[str] | None = None) -> Path:
    aliases = aliases or []
    alias_block = "[" + ", ".join(f'"{a}"' for a in aliases) + "]"
    p = dir_ / f"{slug}.md"
    p.write_text(
        "---\n"
        f'title: "{title}"\n'
        "status: enriched\n"
        f"aliases: {alias_block}\n"
        "---\n"
        f"# {title}\n",
        encoding="utf-8",
    )
    return p


@pytest.fixture
def populated_index(tmp_path: Path) -> OutputIndex:
    _write(tmp_path, "self-determination-theory",
           "Self-Determination Theory", aliases=["SDT"])
    _write(tmp_path, "cognitive-load-theory",
           "Cognitive Load Theory", aliases=["CLT"])
    _write(tmp_path, "metacognition", "Metacognition")
    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    return idx


def test_match_tier_exact_slug(populated_index: OutputIndex) -> None:
    m = Matcher(index=populated_index)
    res = m.find("Anything goes here", "self-determination-theory")
    assert isinstance(res, MatchResult)
    assert res.tier == "exact_slug"
    assert res.score == 1.0


def test_match_tier_alias(populated_index: OutputIndex) -> None:
    m = Matcher(index=populated_index)
    res = m.find("SDT", "no-such-slug")
    assert res is not None
    assert res.tier == "alias"
    assert res.score == 1.0


def test_match_tier_normalized_title(populated_index: OutputIndex) -> None:
    m = Matcher(index=populated_index)
    res = m.find("self---determination___theory", "no-such-slug")
    assert res is not None
    assert res.tier == "normalized_title"
    assert res.score == 1.0


def test_match_tier_fuzzy_above_threshold(populated_index: OutputIndex) -> None:
    m = Matcher(index=populated_index, threshold=0.85)
    # Drop one char — should fuzzy match self-determination-theory
    res = m.find("Self Determinatin Theory", "no-such-slug")
    assert res is not None
    assert res.tier == "fuzzy"
    assert res.score >= 0.85


def test_match_below_threshold_returns_none(populated_index: OutputIndex) -> None:
    m = Matcher(index=populated_index, threshold=0.99)
    res = m.find("Quantum Chromodynamics", "no-such-slug")
    assert res is None


def test_default_threshold_is_documented_value() -> None:
    assert DEFAULT_THRESHOLD == 0.92


def test_ambiguous_match_raises(tmp_path: Path) -> None:
    # Two distinct notes with identical-distance fuzzy hits
    _write(tmp_path, "alpha-beta", "alpha beta")
    _write(tmp_path, "alpha-beta-2", "alpha beta")  # identical norm title
    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    # Identical normalized titles → tier-3 hits (deterministic, last write wins).
    # To force AmbiguousMatchError we create two NEAR-but-not-equal titles.
    _write(tmp_path, "gamma-1", "Apollo Theory of Mind")
    _write(tmp_path, "gamma-2", "Apolla Theory of Mind")
    idx = OutputIndex(output_dir=tmp_path)
    idx.build()
    m = Matcher(index=idx, threshold=0.5)
    with pytest.raises(AmbiguousMatchError):
        m.find("Apoll? Theory of Mind", "no-such-slug")
