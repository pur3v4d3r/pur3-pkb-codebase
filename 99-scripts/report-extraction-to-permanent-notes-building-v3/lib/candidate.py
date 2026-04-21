#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""candidate.py — Canonical ``Candidate`` model + JSON I/O.

A ``Candidate`` represents one extractable concept (e.g. "Self-Determination
Theory") with all the content the upstream report-extractor harvested for it,
*aggregated across every report that mentioned it*. Each Candidate carries:

- A primary name + every observed alias
- A definition body (first non-empty seen)
- Bucketed evidence items keyed by the originating callout type
- Provenance: every source report (batch / file / line) that contributed
- A deterministic content hash for diff-aware downstream stages

This module is pure (no I/O beyond JSON serialization, no external deps beyond
stdlib). Phase 2 ships the structural skeleton and the merge algebra; Phase 4
will fill ``canonical_name`` via an LLM normalizer (until then it equals
``primary_name``).

Spec: §3.1 (Candidate dataclass), §5 Phase 2 (consolidation).

Public API:
    EvidenceItem            — one bucketed content unit with provenance
    SourceReport            — provenance record (batch / file / line)
    Candidate               — full aggregated concept
    normalize_name(name)    — case/whitespace-insensitive grouping key
    callout_to_bucket(type) — maps callout ``type`` to a Candidate field name
    Candidate.from_callout(callout, source) — build from one callout
    Candidate.merge(other)  — combine two Candidates with the same key
    Candidate.to_dict() / Candidate.from_dict(d) — JSON round-trip

Phase 2 deliverable. See spec §5 Phase 2.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass, field, fields, replace
from typing import Any, Final, Literal


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Pipeline confidence values (spec §3.1).
Confidence = Literal["high", "medium", "low"]
Complexity = Literal["foundational", "intermediate", "advanced-practitioner", "expert"]
Importance = Literal["high", "medium", "low"]

#: Default values when frontmatter omits the corresponding key.
DEFAULT_CONFIDENCE: Final[Confidence] = "medium"
DEFAULT_COMPLEXITY: Final[Complexity] = "intermediate"
DEFAULT_IMPORTANCE: Final[Importance] = "medium"
DEFAULT_DOMAIN: Final[str] = "uncategorized"

#: Map a callout ``type`` (as produced by ``pkb_extractor.py``) to the
#: ``Candidate`` field-name that aggregates it. Unmapped callout types fall
#: into the generic ``evidence`` bucket so no content is silently dropped.
#:
#: Callout types observed in the real corpus (sample fixture probe):
#:   analytical-insight, ask-yourself-this, best-practice, cite,
#:   comparative-finding, connections-and-links, cross-domain-connection,
#:   definition, framework-profile, further-exploration, key-claim,
#:   methodology-and-sources, original-synthesis, reflection,
#:   tension-identified, warning, what-the-evidence-suggests
CALLOUT_TYPE_TO_BUCKET: Final[dict[str, str]] = {
    "definition":                   "_definition",   # special: feeds definition_body
    "key-claim":                    "evidence",
    "evidence":                     "evidence",
    "what-the-evidence-suggests":   "evidence",
    "comparative-finding":          "evidence",
    "framework-profile":            "evidence",
    "analytical-insight":           "insights",
    "original-synthesis":           "insights",
    "claude-insight":               "claude_insights",
    "best-practice":                "practices",
    "warning":                      "warnings",
    "reflection":                   "reflections",
    "ask-yourself-this":            "open_questions",
    "open-question":                "open_questions",
    "further-exploration":          "open_questions",
    "tension-identified":           "tensions",
    "tension":                      "tensions",
    "cross-domain-connection":      "far_transfers",
    "connections-and-links":        "far_transfers",
    "methodology-and-sources":      "methodology",
    "cite":                         "citations",
    "person":                       "persons",
    "flashcard":                    "flashcards",
    "protocol":                     "protocols",
    "diagram":                      "diagrams",
    "mermaid":                      "diagrams",
    "schema-activation":            "schema_activations",
    "active-reading":               "active_readings",
    "debate":                       "debates",
    "example":                      "examples",
    "section-summary":              "section_summaries",
}

#: Aggregation buckets on ``Candidate`` (every tuple-of-EvidenceItem field).
#: Order matters for to_dict / merge stability.
BUCKET_FIELDS: Final[tuple[str, ...]] = (
    "evidence", "insights", "practices", "warnings", "reflections",
    "persons", "tensions", "open_questions", "flashcards", "protocols",
    "diagrams", "citations", "methodology", "schema_activations",
    "active_readings", "far_transfers", "debates", "examples",
    "section_summaries", "claude_insights",
)

_WS = re.compile(r"\s+")


# ════════════════════════════════════════════════════════════════════════════
# Helpers
# ════════════════════════════════════════════════════════════════════════════

def normalize_name(name: str) -> str:
    """Return a stable grouping key for a concept name.

    The key is case-folded, NFKD-normalized (drops diacritics), with hyphens,
    underscores and runs of whitespace collapsed to a single space. Two names
    that differ only by capitalization, hyphenation, or accent share a key.

    Examples:
        >>> normalize_name("Self-Determination Theory")
        'self determination theory'
        >>> normalize_name("self_determination_theory")
        'self determination theory'
        >>> normalize_name("Pintrich's Motivational Integration")
        "pintrich's motivational integration"
    """
    if not name:
        return ""
    nfkd = unicodedata.normalize("NFKD", name)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    lowered = no_accents.casefold()
    flat = lowered.replace("-", " ").replace("_", " ")
    return _WS.sub(" ", flat).strip()


def callout_to_bucket(callout_type: str | None) -> str:
    """Map a callout ``type`` to the ``Candidate`` aggregation field-name.

    Unknown callout types fall into the generic ``evidence`` bucket so
    nothing is silently dropped.
    """
    if not callout_type:
        return "evidence"
    return CALLOUT_TYPE_TO_BUCKET.get(callout_type.strip().lower(), "evidence")


# ════════════════════════════════════════════════════════════════════════════
# Provenance + content types
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True, order=True)
class SourceReport:
    """Where a piece of content came from.

    Attributes:
        batch: The batch directory name (e.g. ``2026-04-20-srl-practice``).
        file:  The validated source filename (e.g. ``foo_validated.json``).
        line:  Best-effort line number in the original markdown (0 if unknown).
    """
    batch: str
    file: str
    line: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {"batch": self.batch, "file": self.file, "line": self.line}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> SourceReport:
        return cls(batch=str(d.get("batch", "")),
                   file=str(d.get("file", "")),
                   line=int(d.get("line", 0)))


@dataclass(frozen=True, order=True)
class EvidenceItem:
    """One bucketed content unit with full attribution.

    Attribute order matches the spec's "no anonymous content" mandate: every
    body is paired with provenance.

    Attributes:
        body:         The callout body text (markdown).
        title:        The callout title (the concept name in most cases).
        callout_type: The originating callout type slug.
        source:       Where this body came from.
    """
    body: str
    title: str
    callout_type: str
    source: SourceReport

    def to_dict(self) -> dict[str, Any]:
        return {
            "body": self.body,
            "title": self.title,
            "callout_type": self.callout_type,
            "source": self.source.to_dict(),
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> EvidenceItem:
        return cls(
            body=str(d.get("body", "")),
            title=str(d.get("title", "")),
            callout_type=str(d.get("callout_type", "")),
            source=SourceReport.from_dict(d.get("source", {})),
        )


# ════════════════════════════════════════════════════════════════════════════
# Candidate
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class Candidate:
    """One concept, aggregated across every report that mentions it.

    The grouping key is :func:`normalize_name` of ``primary_name``.
    ``canonical_name`` equals ``primary_name`` until Stage 4 (LLM normalizer)
    refines it.

    See spec §3.1 for the full field inventory.
    """
    canonical_name: str
    primary_name: str
    aliases: tuple[str, ...] = ()
    domain: str = DEFAULT_DOMAIN
    subdomains: tuple[str, ...] = ()
    definition_body: str = ""
    confidence: Confidence = DEFAULT_CONFIDENCE
    complexity: Complexity = DEFAULT_COMPLEXITY
    importance: Importance = DEFAULT_IMPORTANCE

    # Aggregated content buckets — every tuple-of-EvidenceItem field.
    evidence: tuple[EvidenceItem, ...] = ()
    insights: tuple[EvidenceItem, ...] = ()
    practices: tuple[EvidenceItem, ...] = ()
    warnings: tuple[EvidenceItem, ...] = ()
    reflections: tuple[EvidenceItem, ...] = ()
    persons: tuple[EvidenceItem, ...] = ()
    tensions: tuple[EvidenceItem, ...] = ()
    open_questions: tuple[EvidenceItem, ...] = ()
    flashcards: tuple[EvidenceItem, ...] = ()
    protocols: tuple[EvidenceItem, ...] = ()
    diagrams: tuple[EvidenceItem, ...] = ()
    citations: tuple[EvidenceItem, ...] = ()
    methodology: tuple[EvidenceItem, ...] = ()
    schema_activations: tuple[EvidenceItem, ...] = ()
    active_readings: tuple[EvidenceItem, ...] = ()
    far_transfers: tuple[EvidenceItem, ...] = ()
    debates: tuple[EvidenceItem, ...] = ()
    examples: tuple[EvidenceItem, ...] = ()
    section_summaries: tuple[EvidenceItem, ...] = ()
    claude_insights: tuple[EvidenceItem, ...] = ()

    # Provenance
    source_reports: tuple[SourceReport, ...] = ()
    wiki_links_seen: tuple[str, ...] = ()
    extraction_hash: str = ""

    # ─── Derived ────────────────────────────────────────────────────────

    @property
    def grouping_key(self) -> str:
        """Stable key used for cross-batch grouping."""
        return normalize_name(self.primary_name)

    def all_items(self) -> tuple[EvidenceItem, ...]:
        """Every EvidenceItem across every bucket, in stable order."""
        out: list[EvidenceItem] = []
        for bf in BUCKET_FIELDS:
            out.extend(getattr(self, bf))
        return tuple(out)

    # ─── Construction ───────────────────────────────────────────────────

    @classmethod
    def from_callout(
        cls,
        callout: dict[str, Any],
        source: SourceReport,
        *,
        domain: str = DEFAULT_DOMAIN,
        subdomains: tuple[str, ...] = (),
        confidence: Confidence = DEFAULT_CONFIDENCE,
        complexity: Complexity = DEFAULT_COMPLEXITY,
        importance: Importance = DEFAULT_IMPORTANCE,
        wiki_links_seen: tuple[str, ...] = (),
    ) -> Candidate:
        """Build a single-callout Candidate.

        The callout's ``title`` becomes ``primary_name`` (and
        ``canonical_name`` until Stage 4). When the callout type is
        ``definition``, the body becomes ``definition_body``; otherwise the
        body is filed into the bucket given by :data:`CALLOUT_TYPE_TO_BUCKET`.
        """
        title = str(callout.get("title", "")).strip()
        body = str(callout.get("body", "")).strip()
        ctype = str(callout.get("type", "")).strip().lower()

        bucket = callout_to_bucket(ctype)
        item = EvidenceItem(
            body=body, title=title, callout_type=ctype, source=source,
        )

        # Definition flows to definition_body, not a content bucket.
        kwargs: dict[str, Any] = {}
        definition_body = ""
        if bucket == "_definition":
            definition_body = body
            # Still record the definition as evidence so provenance is preserved.
            kwargs["evidence"] = (item,)
        else:
            kwargs[bucket] = (item,)

        cand = cls(
            canonical_name=title,
            primary_name=title,
            aliases=(),
            domain=domain,
            subdomains=subdomains,
            definition_body=definition_body,
            confidence=confidence,
            complexity=complexity,
            importance=importance,
            source_reports=(source,),
            wiki_links_seen=wiki_links_seen,
            **kwargs,
        )
        return replace(cand, extraction_hash=cand._compute_hash())

    # ─── Merge algebra ──────────────────────────────────────────────────

    def merge(self, other: Candidate) -> Candidate:
        """Combine two Candidates that share the same grouping key.

        Merge rules:
            - ``primary_name``: the shorter of the two (canonical-ish).
            - ``aliases``: union of both sides' (primary_name, aliases).
            - ``definition_body``: first non-empty wins (self preferred).
            - Bucket tuples: concatenated (self ++ other), de-duplicated by
              ``(body, source.batch, source.file, source.line)``.
            - ``source_reports``: union, sorted.
            - ``wiki_links_seen``: union (case-sensitive), sorted.
            - Scalar metadata (domain, confidence, complexity, importance):
              self wins; other contributes only if self has a default.
            - ``extraction_hash``: recomputed.

        Raises:
            ValueError: if ``self.grouping_key != other.grouping_key``.
        """
        if self.grouping_key != other.grouping_key:
            raise ValueError(
                f"cannot merge candidates with different grouping keys: "
                f"{self.grouping_key!r} vs {other.grouping_key!r}"
            )

        # primary_name: prefer the shorter (less qualified) form
        if len(other.primary_name) < len(self.primary_name) and other.primary_name:
            primary = other.primary_name
            aliases_seed = (self.primary_name,)
        else:
            primary = self.primary_name
            aliases_seed = (other.primary_name,) if other.primary_name != primary else ()

        all_aliases = (*self.aliases, *other.aliases, *aliases_seed)
        aliases = tuple(_unique_preserve(a for a in all_aliases if a and a != primary))

        # definition_body: first non-empty wins
        definition = self.definition_body or other.definition_body

        # scalar metadata: self wins unless it's the default
        domain = self.domain if self.domain != DEFAULT_DOMAIN else other.domain
        confidence = self.confidence if self.confidence != DEFAULT_CONFIDENCE else other.confidence
        complexity = self.complexity if self.complexity != DEFAULT_COMPLEXITY else other.complexity
        importance = self.importance if self.importance != DEFAULT_IMPORTANCE else other.importance

        subdomains = tuple(_unique_preserve((*self.subdomains, *other.subdomains)))

        # buckets: concat + dedupe
        bucket_kwargs: dict[str, Any] = {}
        for bf in BUCKET_FIELDS:
            merged = _dedupe_items((*getattr(self, bf), *getattr(other, bf)))
            bucket_kwargs[bf] = merged

        sources = tuple(sorted(set((*self.source_reports, *other.source_reports))))
        wiki_links = tuple(sorted(set((*self.wiki_links_seen, *other.wiki_links_seen))))

        merged = Candidate(
            canonical_name=primary,
            primary_name=primary,
            aliases=aliases,
            domain=domain,
            subdomains=subdomains,
            definition_body=definition,
            confidence=confidence,
            complexity=complexity,
            importance=importance,
            source_reports=sources,
            wiki_links_seen=wiki_links,
            **bucket_kwargs,
        )
        return replace(merged, extraction_hash=merged._compute_hash())

    # ─── Hashing ────────────────────────────────────────────────────────

    def _compute_hash(self) -> str:
        """Deterministic content hash over (primary_name, definition,
        every (callout_type, body) pair).

        Used by Phase 2 gate (no-evidence-loss checksum) and by downstream
        diff-aware re-runs.
        """
        h = hashlib.sha256()
        h.update(self.grouping_key.encode("utf-8"))
        h.update(b"\x00")
        h.update(self.definition_body.encode("utf-8"))
        h.update(b"\x00")
        for it in self.all_items():
            h.update(it.callout_type.encode("utf-8"))
            h.update(b"\x01")
            h.update(it.body.encode("utf-8"))
            h.update(b"\x02")
        return h.hexdigest()

    # ─── JSON I/O ───────────────────────────────────────────────────────

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a JSON-safe dict (round-trips via :meth:`from_dict`)."""
        out: dict[str, Any] = {
            "canonical_name": self.canonical_name,
            "primary_name": self.primary_name,
            "aliases": list(self.aliases),
            "domain": self.domain,
            "subdomains": list(self.subdomains),
            "definition_body": self.definition_body,
            "confidence": self.confidence,
            "complexity": self.complexity,
            "importance": self.importance,
            "source_reports": [s.to_dict() for s in self.source_reports],
            "wiki_links_seen": list(self.wiki_links_seen),
            "extraction_hash": self.extraction_hash,
        }
        for bf in BUCKET_FIELDS:
            out[bf] = [it.to_dict() for it in getattr(self, bf)]
        return out

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Candidate:
        """Inverse of :meth:`to_dict`."""
        bucket_kwargs: dict[str, Any] = {}
        for bf in BUCKET_FIELDS:
            raw = d.get(bf, []) or []
            bucket_kwargs[bf] = tuple(EvidenceItem.from_dict(x) for x in raw)
        return cls(
            canonical_name=str(d.get("canonical_name", "")),
            primary_name=str(d.get("primary_name", "")),
            aliases=tuple(d.get("aliases", []) or []),
            domain=str(d.get("domain", DEFAULT_DOMAIN)),
            subdomains=tuple(d.get("subdomains", []) or []),
            definition_body=str(d.get("definition_body", "")),
            confidence=d.get("confidence", DEFAULT_CONFIDENCE),  # type: ignore[arg-type]
            complexity=d.get("complexity", DEFAULT_COMPLEXITY),  # type: ignore[arg-type]
            importance=d.get("importance", DEFAULT_IMPORTANCE),  # type: ignore[arg-type]
            source_reports=tuple(
                SourceReport.from_dict(x) for x in (d.get("source_reports", []) or [])
            ),
            wiki_links_seen=tuple(d.get("wiki_links_seen", []) or []),
            extraction_hash=str(d.get("extraction_hash", "")),
            **bucket_kwargs,
        )


# ════════════════════════════════════════════════════════════════════════════
# Internals
# ════════════════════════════════════════════════════════════════════════════

def _unique_preserve(seq: Any) -> list[str]:
    """Return ``seq`` deduplicated, preserving first-seen order."""
    seen: set[str] = set()
    out: list[str] = []
    for x in seq:
        if x in seen:
            continue
        seen.add(x)
        out.append(x)
    return out


def _dedupe_items(items: tuple[EvidenceItem, ...]) -> tuple[EvidenceItem, ...]:
    """Deduplicate EvidenceItems by (body, source.batch, source.file, source.line).

    Two callouts with identical bodies emitted from the same line of the same
    file are the same callout — keep one. Same body from different files /
    lines is preserved (legitimate corroboration).
    """
    seen: set[tuple[str, str, str, int]] = set()
    out: list[EvidenceItem] = []
    for it in items:
        key = (it.body, it.source.batch, it.source.file, it.source.line)
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return tuple(out)
