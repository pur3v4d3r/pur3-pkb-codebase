#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""matcher — Tiered concept-to-existing-note matching.

The matcher decides whether an incoming concept (from a fresh extraction)
already has a permanent note in the output directory. It does so via a
deterministic tier cascade — each tier is tried in order and the first hit
wins:

    1. exact_slug        — incoming kebab-case slug equals an existing slug
    2. alias             — incoming title (normalized) equals an existing alias
    3. normalized_title  — normalized title equals an indexed normalized title
    4. fuzzy             — Levenshtein ratio against all indexed titles
                           must meet or exceed ``threshold`` (default 0.92)

Tier 4 uses ``difflib.SequenceMatcher`` (stdlib) — no third-party fuzzy
matching dependency. The threshold is exposed via the CLI and defaults to
0.92, chosen to err toward false negatives over false positives. Two
or more fuzzy hits at exactly the same top score are reported as
:class:`AmbiguousMatchError` (caller decides skip vs. force).
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Literal

from v5lib.output_index import OutputIndex, normalize_title

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Default fuzzy match threshold. Tuned to prefer false-negatives over
#: false-positives; lower at your own risk.
DEFAULT_THRESHOLD: float = 0.92

#: Type alias for the four match tiers.
MatchTier = Literal["exact_slug", "alias", "normalized_title", "fuzzy"]


# ════════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ════════════════════════════════════════════════════════════════════════════

class AmbiguousMatchError(Exception):
    """Raised when fuzzy matching finds two or more hits with identical top scores.

    The caller should typically skip this concept (writing to ``--report-merges``
    for human review) rather than guessing. A future ``--interactive`` mode
    could prompt for resolution.
    """

    def __init__(self, concept_title: str, candidates: list[Path], score: float) -> None:
        self.concept_title = concept_title
        self.candidates = candidates
        self.score = score
        super().__init__(
            f"Ambiguous fuzzy match for {concept_title!r} (score={score:.3f}): "
            f"{[p.name for p in candidates]}"
        )


# ════════════════════════════════════════════════════════════════════════════
# Data types
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class MatchResult:
    """Outcome of a successful match.

    Attributes:
        path: Absolute path to the existing note file.
        tier: Which tier produced the hit.
        score: 1.0 for exact tiers; ratio in [threshold, 1.0] for fuzzy.
        matched_against: The exact key in the index that matched (the
            normalized form of the incoming title for ``alias`` and
            ``normalized_title``; the slug for ``exact_slug``; the
            normalized title of the matched note for ``fuzzy``).
    """
    path: Path
    tier: MatchTier
    score: float
    matched_against: str


# ════════════════════════════════════════════════════════════════════════════
# Matcher
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class Matcher:
    """Resolve a concept-title-and-slug to an existing note via tiered match.

    Attributes:
        index: A built :class:`OutputIndex`.
        threshold: Minimum SequenceMatcher ratio for fuzzy hits.

    Example:
        >>> idx = OutputIndex(output_dir=Path("./notes"))
        >>> idx.build()
        >>> m = Matcher(index=idx)
        >>> hit = m.find("Cognitive Load Theory", "cognitive-load-theory")
        >>> hit.tier if hit else None
        'exact_slug'
    """
    index: OutputIndex
    threshold: float = DEFAULT_THRESHOLD

    def find(self, concept_title: str, slug: str) -> MatchResult | None:
        """Run the four-tier cascade. Return the first hit, or ``None``.

        Args:
            concept_title: The cleaned concept name from the bundle.
            slug: The kebab-case filename stem the bundle would produce.

        Returns:
            A :class:`MatchResult` on hit, or ``None`` if all tiers miss.

        Raises:
            AmbiguousMatchError: When two or more fuzzy candidates tie for
                the top score above ``threshold``.
        """
        # ── Tier 1: exact slug ───────────────────────────────────────────
        slug_lc = (slug or "").lower()
        if slug_lc and slug_lc in self.index.by_slug:
            return MatchResult(
                path=self.index.by_slug[slug_lc],
                tier="exact_slug",
                score=1.0,
                matched_against=slug_lc,
            )

        # ── Tier 2 & 3: normalize incoming title once ────────────────────
        norm = normalize_title(concept_title)
        if not norm:
            return None

        if norm in self.index.by_alias:
            return MatchResult(
                path=self.index.by_alias[norm],
                tier="alias",
                score=1.0,
                matched_against=norm,
            )
        if norm in self.index.by_norm_title:
            return MatchResult(
                path=self.index.by_norm_title[norm],
                tier="normalized_title",
                score=1.0,
                matched_against=norm,
            )

        # ── Tier 4: fuzzy ────────────────────────────────────────────────
        if not self.index.all_norm_titles:
            return None
        scored = [
            (SequenceMatcher(a=norm, b=t).ratio(), t, p)
            for (t, p) in self.index.all_norm_titles
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        top_score, top_title, top_path = scored[0]
        if top_score < self.threshold:
            return None
        # Check for ties at the top score (within float epsilon)
        ties = [s for s in scored if abs(s[0] - top_score) < 1e-9]
        if len(ties) > 1:
            # Distinct paths only — duplicate index entries shouldn't tie
            distinct = sorted({s[2] for s in ties})
            if len(distinct) > 1:
                raise AmbiguousMatchError(
                    concept_title=concept_title,
                    candidates=distinct,
                    score=top_score,
                )
        return MatchResult(
            path=top_path,
            tier="fuzzy",
            score=top_score,
            matched_against=top_title,
        )
