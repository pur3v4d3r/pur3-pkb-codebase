#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for lib/markdown.py."""
from __future__ import annotations

from lib.markdown import (
    callout,
    indent_block,
    join_wikilinks,
    safe_filename,
    to_kebab,
    truncate_for_callout,
    wikilink,
)


# ─── callout ─────────────────────────────────────────────────────────────

def test_callout_basic() -> None:
    out = callout("warning", "Caution", "Don't do X.")
    assert out == "> [!warning] Caution\n> Don't do X."


def test_callout_multiline_body() -> None:
    out = callout("evidence", "E1", "line one\nline two")
    assert "> line one" in out
    assert "> line two" in out


def test_callout_with_source() -> None:
    out = callout("evidence", "E1", "body", source="report-2026")
    assert out.endswith("> *— [[report-2026]]*")


def test_callout_lowercases_type() -> None:
    out = callout("WARNING", "X", "y")
    assert out.startswith("> [!warning]")


def test_callout_strips_newlines_from_title() -> None:
    out = callout("note", "title\nwith\nnewlines", "body")
    assert out.startswith("> [!note] title with newlines")


def test_callout_empty_body() -> None:
    out = callout("note", "T", "")
    assert out == "> [!note] T"


def test_indent_block_blank_lines() -> None:
    # Blank lines should still get the prefix-without-trailing-space
    out = indent_block("a\n\nb")
    assert out == "> a\n>\n> b"


# ─── wikilink ────────────────────────────────────────────────────────────

def test_wikilink_plain() -> None:
    assert wikilink("Self-Determination Theory") == "[[Self-Determination Theory]]"


def test_wikilink_with_alias() -> None:
    assert wikilink("self-determination-theory", "SDT") == "[[self-determination-theory|SDT]]"


def test_wikilink_strips_existing_brackets() -> None:
    assert wikilink("[[X]]") == "[[X]]"


def test_wikilink_empty() -> None:
    assert wikilink("") == ""


def test_join_wikilinks_filters_empty() -> None:
    out = join_wikilinks(["A", "", "B"])
    assert out == "[[A]] · [[B]]"


def test_join_wikilinks_custom_sep() -> None:
    assert join_wikilinks(["A", "B"], sep=", ") == "[[A]], [[B]]"


# ─── safe_filename ───────────────────────────────────────────────────────

def test_safe_filename_strips_forbidden() -> None:
    assert safe_filename('A/B*C?') == "ABC"


def test_safe_filename_preserves_case_and_hyphens() -> None:
    assert safe_filename("Self-Determination Theory") == "Self-Determination Theory"


def test_safe_filename_collapses_whitespace() -> None:
    assert safe_filename("a   b\t\nc") == "a b c"


def test_safe_filename_empty_returns_untitled() -> None:
    assert safe_filename("") == "untitled"
    assert safe_filename("///") == "untitled"


# ─── to_kebab ────────────────────────────────────────────────────────────

def test_to_kebab_basic() -> None:
    assert to_kebab("Self-Determination Theory") == "self-determination-theory"


def test_to_kebab_strips_diacritics() -> None:
    assert to_kebab("Café Society") == "cafe-society"


def test_to_kebab_strips_apostrophes() -> None:
    assert to_kebab("Pintrich's MSLQ") == "pintrich-s-mslq"


def test_to_kebab_empty() -> None:
    assert to_kebab("") == ""


# ─── truncate ────────────────────────────────────────────────────────────

def test_truncate_short_passes_through() -> None:
    assert truncate_for_callout("a\nb", max_lines=5) == "a\nb"


def test_truncate_long_collapses() -> None:
    text = "\n".join(str(i) for i in range(20))
    out = truncate_for_callout(text, max_lines=5)
    assert out.endswith("\n…")
    assert out.count("\n") == 5  # 5 lines + ellipsis line
