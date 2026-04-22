#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""markdown.py — Callout, link, and heading helpers for v3 rendering.

Pure functions that emit Obsidian-flavored Markdown. No I/O, no template engine
coupling — designed so :mod:`stages.s6_render` (Jinja2) and any future
ad-hoc rendering can share consistent output.

Public API:
    callout(type, title, body, *, source=None) — emit a ``> [!type]`` block
    wikilink(target, alias=None)               — ``[[target]]`` or ``[[target|alias]]``
    safe_filename(name)                        — Obsidian-safe filename stem
    to_kebab(name)                             — kebab-case slug
    indent_block(text, prefix=">")             — prefix each line of a block
    join_wikilinks(targets, sep=" · ")         — render a list as wikilinks
    truncate_for_callout(text, max_lines=12)   — collapse over-long bodies

Phase 3 deliverable.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Iterable

#: Characters Obsidian disallows in filenames.
_FORBIDDEN_FILENAME = re.compile(r'[\\/:*?"<>|\[\]]')

#: Run-of-non-alphanumerics for kebab-case conversion.
_NON_ALNUM = re.compile(r"[^a-z0-9]+")

#: Whitespace runs.
_WS = re.compile(r"\s+")


# ════════════════════════════════════════════════════════════════════════════
# Callout rendering
# ════════════════════════════════════════════════════════════════════════════

def indent_block(text: str, prefix: str = "> ") -> str:
    """Prefix every line of ``text`` with ``prefix`` (Obsidian callout body)."""
    if not text:
        return prefix.rstrip()
    return "\n".join(prefix + line if line.strip() else prefix.rstrip()
                     for line in text.splitlines())


def callout(
    callout_type: str,
    title: str,
    body: str,
    *,
    source: str | None = None,
) -> str:
    """Render an Obsidian callout block.

    Args:
        callout_type: e.g. ``"definition"``, ``"warning"``.
        title: First-line title (already-escaped).
        body: Multi-line callout body.
        source: Optional wiki-link target appended as italic attribution.

    Returns:
        A multi-line markdown string ending without a trailing newline.

    Example:
        >>> print(callout("warning", "Caution", "Don't do X."))
        > [!warning] Caution
        > Don't do X.
    """
    title = (title or "").strip().replace("\n", " ")
    head = f"> [!{callout_type.strip().lower()}] {title}".rstrip()
    body_block = indent_block((body or "").strip(), "> ")
    parts = [head, body_block] if body_block.strip("> ").strip() else [head]
    if source:
        parts.append(f"> *— [[{source}]]*")
    return "\n".join(parts)


def truncate_for_callout(text: str, max_lines: int = 12) -> str:
    """Collapse a body to ``max_lines`` lines + ellipsis. Preserves the head."""
    if not text:
        return ""
    lines = text.splitlines()
    if len(lines) <= max_lines:
        return text
    return "\n".join(lines[:max_lines]) + "\n…"


# ════════════════════════════════════════════════════════════════════════════
# Wiki-links
# ════════════════════════════════════════════════════════════════════════════

def wikilink(target: str, alias: str | None = None) -> str:
    """Render an Obsidian wiki-link.

    Examples:
        >>> wikilink("Self-Determination Theory")
        '[[Self-Determination Theory]]'
        >>> wikilink("self-determination-theory", "SDT")
        '[[self-determination-theory|SDT]]'
    """
    target = (target or "").strip().strip("[]")
    if not target:
        return ""
    if alias:
        return f"[[{target}|{alias.strip()}]]"
    return f"[[{target}]]"


def join_wikilinks(targets: Iterable[str], sep: str = " · ") -> str:
    """Render an iterable of targets as wikilinks joined by ``sep``."""
    rendered = [wikilink(t) for t in targets if t and t.strip()]
    return sep.join(rendered)


# ════════════════════════════════════════════════════════════════════════════
# Filename / slug helpers
# ════════════════════════════════════════════════════════════════════════════

#: Max filename length (stem only; leaves headroom for ``.md`` and parent path
#: under Windows' 260-char path limit).
MAX_FILENAME_STEM = 120


def safe_filename(name: str, max_len: int = MAX_FILENAME_STEM) -> str:
    """Return a filename-safe form of ``name`` (Obsidian-compatible).

    Strips disallowed chars, collapses whitespace, trims dots and spaces from
    the ends. Truncates to ``max_len`` characters at a word boundary when
    possible. Preserves human-readable casing.
    """
    if not name:
        return "untitled"
    cleaned = _FORBIDDEN_FILENAME.sub("", name)
    cleaned = _WS.sub(" ", cleaned).strip(" .")
    if not cleaned:
        return "untitled"
    if len(cleaned) > max_len:
        truncated = cleaned[:max_len].rsplit(" ", 1)[0] or cleaned[:max_len]
        cleaned = truncated.strip(" .")
    return cleaned or "untitled"


def to_kebab(name: str) -> str:
    """Return ``name`` as a lowercase, hyphen-separated slug.

    Strips diacritics, replaces non-alphanumeric runs with a single hyphen.

    Examples:
        >>> to_kebab("Self-Determination Theory")
        'self-determination-theory'
        >>> to_kebab("Pintrich's MSLQ")
        'pintrichs-mslq'
    """
    if not name:
        return ""
    nfkd = unicodedata.normalize("NFKD", name)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    lowered = no_accents.casefold()
    slug = _NON_ALNUM.sub("-", lowered).strip("-")
    return slug
