#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""frontmatter.py — Slim-style YAML frontmatter for v3 permanent notes.

Emits the ≤25-line frontmatter described in spec §3.2:

    title:        canonical concept name
    aliases:      inline list
    type, status, confidence
    domain, subdomains, tags
    created, updated
    complexity, importance
    review-frequency, mastery-stage
    provenance:   { source-type, pipeline-version, source-reports[],
                    extraction-method }
    relationships: { related[], see-also[], builds-on[], enables[] }

Public API:
    build_frontmatter(candidate, *, today, ...) -> dict
    render_frontmatter(data) -> str
    parse_frontmatter(text) -> tuple[dict, str]   # (data, body_after_yaml)
    merge_frontmatter(existing, fresh) -> dict    # update path: preserve user edits

Phase 3 deliverable. Spec §3.2.
"""
from __future__ import annotations

import datetime as dt
import io
import re
from typing import Any, Iterable

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

from lib.candidate import Candidate
from lib.markdown import to_kebab


def _flow(items: Iterable[Any]) -> CommentedSeq:
    """Return a YAML sequence rendered in flow (inline) style."""
    seq = CommentedSeq(list(items))
    seq.fa.set_flow_style()
    return seq

#: User-editable scalar fields (preserved during update merges).
USER_EDITABLE_SCALARS: frozenset[str] = frozenset({
    "status", "mastery-stage", "review-frequency", "next-review",
})

#: User-editable list fields (preserved as a union with fresh values).
USER_EDITABLE_LISTS: frozenset[str] = frozenset({
    "tags", "aliases",
})

#: Default tag set added to every note (after domain-derived tags).
BASE_TAGS: tuple[str, ...] = ("permanent-note",)

#: Front-matter delimiter regex.
_FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)

_yaml = YAML()
_yaml.default_flow_style = False
_yaml.indent(mapping=2, sequence=4, offset=2)
_yaml.width = 4096  # don't soft-wrap


# ════════════════════════════════════════════════════════════════════════════
# Build
# ════════════════════════════════════════════════════════════════════════════

def _stem(name: str) -> str:
    """Stem used inside source-report wiki-links."""
    return name.rsplit("_validated", 1)[0].removesuffix(".json")


def _domain_tags(domain: str, subdomains: Iterable[str]) -> list[str]:
    out = [to_kebab(domain)] if domain else []
    for s in subdomains:
        kebab = to_kebab(s)
        if kebab and kebab not in out:
            out.append(kebab)
    return out


def build_frontmatter(
    cand: Candidate,
    *,
    today: dt.date,
    pipeline_version: str = "3.0.0",
    extraction_method: str = "pkb-extractor-v1 → pipeline-v3",
    related: Iterable[str] = (),
    see_also: Iterable[str] = (),
    builds_on: Iterable[str] = (),
    enables: Iterable[str] = (),
) -> dict[str, Any]:
    """Construct the dict that will be serialized as YAML frontmatter.

    The dict is ordered to match spec §3.2 layout. Empty optional sections
    (e.g. ``relationships`` when no edges exist) are omitted.
    """
    aliases_clean = [a for a in (cand.aliases or ()) if a and a != cand.primary_name]
    tags = list(BASE_TAGS) + _domain_tags(cand.domain, cand.subdomains)

    source_reports = sorted({_stem(s.file) for s in cand.source_reports})

    fm: dict[str, Any] = {
        "title": DoubleQuotedScalarString(cand.primary_name),
        "aliases": _flow(aliases_clean),
        "type": "permanent-note",
        "status": "evergreen",
        "confidence": cand.confidence,
        "domain": cand.domain,
        "subdomains": _flow(cand.subdomains),
        "tags": _flow(tags),
        "created": today.isoformat(),
        "updated": today.isoformat(),
        "complexity": cand.complexity,
        "importance": cand.importance,
        "review-frequency": "quarterly",
        "mastery-stage": "seedling",
        "provenance": {
            "source-type": "report-extraction",
            "pipeline-version": DoubleQuotedScalarString(pipeline_version),
            "source-reports": _flow(source_reports),
            "extraction-method": extraction_method,
        },
    }

    # Relationships only included when at least one edge exists.
    rels: dict[str, Any] = {}
    if related:
        rels["related"] = _flow(f"[[{x}]]" for x in related)
    if see_also:
        rels["see-also"] = _flow(f"[[{x}]]" for x in see_also)
    if builds_on:
        rels["builds-on"] = _flow(f"[[{x}]]" for x in builds_on)
    if enables:
        rels["enables"] = _flow(f"[[{x}]]" for x in enables)
    if rels:
        fm["relationships"] = rels

    return fm


# ════════════════════════════════════════════════════════════════════════════
# Render
# ════════════════════════════════════════════════════════════════════════════

def render_frontmatter(data: dict[str, Any]) -> str:
    """Serialize ``data`` to a `---\\n…\\n---\\n` YAML block."""
    buf = io.StringIO()
    _yaml.dump(data, buf)
    yaml_body = buf.getvalue().rstrip("\n")
    return f"---\n{yaml_body}\n---\n"


# ════════════════════════════════════════════════════════════════════════════
# Parse + merge (update path)
# ════════════════════════════════════════════════════════════════════════════

def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Split a markdown document into ``(frontmatter_dict, body)``.

    If the document has no frontmatter, returns ``({}, text)``.
    """
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    yaml_block = m.group(1)
    body = m.group(2)
    try:
        data = _yaml.load(yaml_block) or {}
    except Exception:
        return {}, text
    if not isinstance(data, dict):
        return {}, text
    return dict(data), body


def merge_frontmatter(
    existing: dict[str, Any],
    fresh: dict[str, Any],
) -> dict[str, Any]:
    """Combine an existing note's frontmatter with freshly-built data.

    Rules:
        - User-editable scalars (USER_EDITABLE_SCALARS): existing wins.
        - User-editable lists (USER_EDITABLE_LISTS): union, existing-first order.
        - ``provenance.source-reports``: union, sorted.
        - ``relationships.<key>``: union, deduped.
        - Other scalars/lists: fresh wins (canonical source).
        - ``created``: existing wins (preserve birthdate).
        - ``updated``: fresh wins.
    """
    out = dict(fresh)

    # Preserve user-editable scalars
    for k in USER_EDITABLE_SCALARS:
        if k in existing:
            out[k] = existing[k]

    # Union user-editable lists (kept in flow style)
    for k in USER_EDITABLE_LISTS:
        ex = list(existing.get(k) or [])
        fr = list(out.get(k) or [])
        out[k] = _flow(_union_preserve(ex, fr))

    # Preserve creation date
    if "created" in existing:
        out["created"] = existing["created"]

    # Provenance: union of source-reports
    ex_prov = existing.get("provenance") or {}
    fr_prov = dict(out.get("provenance") or {})
    if ex_prov.get("source-reports") or fr_prov.get("source-reports"):
        srcs = sorted(set(
            list(ex_prov.get("source-reports") or [])
            + list(fr_prov.get("source-reports") or [])
        ))
        fr_prov["source-reports"] = _flow(srcs)
    out["provenance"] = fr_prov

    # Relationships: union per edge type
    ex_rels = existing.get("relationships") or {}
    fr_rels = dict(out.get("relationships") or {})
    edge_keys = set(ex_rels) | set(fr_rels)
    if edge_keys:
        merged_rels: dict[str, Any] = {}
        for ek in sorted(edge_keys):
            merged_rels[ek] = _flow(_union_preserve(
                list(ex_rels.get(ek) or []),
                list(fr_rels.get(ek) or []),
            ))
        out["relationships"] = merged_rels

    return out


def _union_preserve(a: list[Any], b: list[Any]) -> list[Any]:
    """Return ``a`` then ``b``, deduped, preserving first-seen order."""
    seen: set[Any] = set()
    out: list[Any] = []
    for x in (*a, *b):
        key = str(x)
        if key in seen:
            continue
        seen.add(key)
        out.append(x)
    return out
