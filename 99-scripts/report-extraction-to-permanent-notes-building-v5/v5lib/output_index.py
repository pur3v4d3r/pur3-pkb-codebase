#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""output_index — Build a fast lookup index over the V5 output directory.

The index is rebuilt at the start of each run. It scans every ``*.md`` file
in the output directory, parses YAML frontmatter, and registers each note
under multiple keys for tiered matching:

    by_slug            — filename stem (lowercase)            → Path
    by_alias           — every alias (normalized)             → Path
    by_norm_title      — frontmatter title (normalized)       → Path
    all_norm_titles    — list of normalized titles for fuzzy matching
    path_to_status     — Path → frontmatter status string

Normalization (``normalize_title``) lowercases, strips punctuation, collapses
whitespace, and removes wiki-link brackets so that ``"Cognitive Load (CLT)"``
and ``"cognitive load"`` collide.

This module is intentionally output-dir-scoped — it does not traverse the
full vault. That is a hard design constraint: V5 is a merge-aware
reconciler over its own output, not a vault-wide deduplicator.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Frontmatter delimiter regex (handles both ``\n`` and ``\r\n`` line endings).
_FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.DOTALL)

#: Keys we extract from frontmatter for indexing.
_INDEXED_FIELDS: frozenset[str] = frozenset({
    "title", "aliases", "status",
    # Operator-managed fields the merger must preserve verbatim:
    "created", "mastery-stage", "importance", "review-frequency",
    "domain", "source-reports",
})

#: Characters stripped during title normalization.
_PUNCT_RE = re.compile(r"[^\w\s-]", re.UNICODE)
_WS_RE = re.compile(r"\s+")
_DASH_RE = re.compile(r"[-_]+")


# ════════════════════════════════════════════════════════════════════════════
# Public API
# ════════════════════════════════════════════════════════════════════════════

def normalize_title(s: str) -> str:
    """Normalize a title or alias string for indexing and matching.

    Lowercases, strips wiki-link brackets, removes punctuation (keeping
    word characters, whitespace, and dashes), collapses dashes/underscores
    and whitespace runs to a single space, then strips.

    Args:
        s: Raw title or alias string.

    Returns:
        Normalized form. Empty string if input is empty or only whitespace.

    Example:
        >>> normalize_title("Cognitive Load (CLT)")
        'cognitive load clt'
        >>> normalize_title("[[Self-Determination Theory]]")
        'self determination theory'
    """
    if not s:
        return ""
    t = s.replace("[[", "").replace("]]", "")
    t = t.lower()
    t = _PUNCT_RE.sub(" ", t)
    t = _DASH_RE.sub(" ", t)
    t = _WS_RE.sub(" ", t).strip()
    return t


@dataclass
class IndexedNote:
    """One entry in the output index.

    Attributes:
        path: Absolute path to the ``.md`` file.
        slug: Filename stem, lowercased.
        title: Frontmatter ``title`` field, raw (or empty string).
        aliases: Tuple of frontmatter aliases, raw (case preserved).
        status: Frontmatter ``status`` field, lowercased (or empty string).
    """
    path: Path
    slug: str
    title: str
    aliases: tuple[str, ...]
    status: str


@dataclass
class OutputIndex:
    """Lookup index over an output directory of permanent notes.

    Build by constructing then calling :meth:`build`. Lookups go through
    :class:`Matcher` (separate module) — this class exposes the raw index
    structures.

    Attributes:
        output_dir: Directory scanned at build time.
        notes: List of :class:`IndexedNote` for every ``.md`` indexed.
        by_slug: Filename stem (lowercase) → Path.
        by_alias: Normalized alias → Path.
        by_norm_title: Normalized title → Path.
        all_norm_titles: List of every (norm_title, Path) pair, used for
            fuzzy matching when no exact tier hits.
    """
    output_dir: Path
    notes: list[IndexedNote] = field(default_factory=list)
    by_slug: dict[str, Path] = field(default_factory=dict)
    by_alias: dict[str, Path] = field(default_factory=dict)
    by_norm_title: dict[str, Path] = field(default_factory=dict)
    all_norm_titles: list[tuple[str, Path]] = field(default_factory=list)

    def build(self) -> None:
        """Walk ``output_dir`` non-recursively, parse each ``.md``, register.

        Subdirectories are intentionally ignored — V5 keeps its output flat.
        Files that fail to parse are logged at WARNING and skipped (they do
        not abort the build).

        Raises:
            FileNotFoundError: ``output_dir`` does not exist.
        """
        if not self.output_dir.exists():
            raise FileNotFoundError(
                f"Output directory does not exist: {self.output_dir}"
            )
        self.notes.clear()
        self.by_slug.clear()
        self.by_alias.clear()
        self.by_norm_title.clear()
        self.all_norm_titles.clear()

        md_files = sorted(p for p in self.output_dir.iterdir()
                          if p.is_file() and p.suffix.lower() == ".md")
        logger.debug("OutputIndex: scanning %d .md files in %s",
                     len(md_files), self.output_dir)

        for path in md_files:
            try:
                note = self._parse_note(path)
            except (OSError, UnicodeDecodeError) as e:
                logger.warning("OutputIndex: skip %s (read error: %s)",
                               path.name, e)
                continue
            self._register(note)

        logger.info(
            "OutputIndex: %d notes indexed (slugs=%d, aliases=%d, titles=%d)",
            len(self.notes), len(self.by_slug),
            len(self.by_alias), len(self.by_norm_title),
        )

    # ─── Convenience ─────────────────────────────────────────────────────

    def __len__(self) -> int:
        return len(self.notes)

    def __contains__(self, slug: str) -> bool:
        return slug.lower() in self.by_slug

    def status_of(self, path: Path) -> str:
        """Return the indexed status for a path, or empty string if not indexed."""
        for n in self.notes:
            if n.path == path:
                return n.status
        return ""

    # ─── Internals ───────────────────────────────────────────────────────

    def _parse_note(self, path: Path) -> IndexedNote:
        """Read the file, extract frontmatter fields we index on."""
        text = path.read_text(encoding="utf-8")
        fm = _extract_frontmatter(text)
        title = (fm.get("title") or "").strip().strip("\"'")
        status = (fm.get("status") or "").strip().strip("\"'").lower()
        aliases_raw = fm.get("aliases", [])
        aliases: tuple[str, ...]
        if isinstance(aliases_raw, list):
            aliases = tuple(
                str(a).strip().strip("\"'")
                for a in aliases_raw
                if str(a).strip().strip("\"'")
            )
        else:
            aliases = ()
        return IndexedNote(
            path=path,
            slug=path.stem.lower(),
            title=title,
            aliases=aliases,
            status=status,
        )

    def _register(self, note: IndexedNote) -> None:
        """Add one note to all relevant index dicts. Later wins on collision."""
        self.notes.append(note)
        self.by_slug[note.slug] = note.path
        if note.title:
            nt = normalize_title(note.title)
            if nt:
                self.by_norm_title[nt] = note.path
                self.all_norm_titles.append((nt, note.path))
        for alias in note.aliases:
            na = normalize_title(alias)
            if na:
                self.by_alias[na] = note.path


# ════════════════════════════════════════════════════════════════════════════
# Frontmatter extraction (minimal YAML parser — no PyYAML dependency)
# ════════════════════════════════════════════════════════════════════════════

def _extract_frontmatter(text: str) -> dict[str, object]:
    """Extract a minimal subset of YAML frontmatter as a dict.

    Handles the three field shapes V4 emits and we need to index:

    - ``title: "Some Title"`` (scalar, possibly quoted)
    - ``status: enriched``    (scalar, unquoted)
    - ``aliases:``            (block-style list with ``- "x"`` items)
    -   ``- "Alias 1"``
    -   ``- Alias 2``
    - ``aliases: [a, b]``     (inline list)

    Other fields are ignored. This is NOT a general YAML parser — it
    targets the V4 frontmatter shape exactly. If a future schema change
    breaks this, swap in PyYAML.
    """
    m = _FM_RE.match(text)
    if not m:
        return {}
    block = m.group(1)
    out: dict[str, object] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        # Top-level key (no leading whitespace)
        if not raw.startswith(" "):
            key, sep, val = raw.partition(":")
            key = key.strip().lower()
            val = val.strip()
            if key not in _INDEXED_FIELDS:
                i += 1
                continue
            if val:
                # Inline value — could be scalar or inline list "[a, b]"
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1].strip()
                    items = [x.strip().strip("\"'") for x in inner.split(",") if x.strip()]
                    out[key] = items
                else:
                    out[key] = val.strip().strip("\"'")
                i += 1
            else:
                # Block value follows on subsequent indented lines
                items: list[str] = []
                j = i + 1
                while j < len(lines):
                    nxt = lines[j]
                    if not nxt.strip():
                        j += 1
                        continue
                    if not nxt.startswith(" "):
                        break  # next top-level key
                    item_match = re.match(r"^\s*-\s*(.*)$", nxt)
                    if item_match:
                        items.append(item_match.group(1).strip().strip("\"'"))
                    j += 1
                out[key] = items
                i = j
        else:
            i += 1
    return out
