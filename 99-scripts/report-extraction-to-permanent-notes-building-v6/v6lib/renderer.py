#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""renderer — V6 rich-template markdown renderer.

Translates the (Outline + Elaborate) response pair into a single markdown
permanent note conforming to the V6 template:

    ---
    YAML frontmatter (V6 schema)
    ---

    # Title

    > [!definition] **Title**
    > <elaborated definition + boundary + falls-under [[Parent]]>

    ## Core Explanation
    <4–6 narrative paragraphs>

    ## Mechanism
    <0–3 paragraphs, optional>

    ## Practical Implications
    > [!example] **Application 1 — <scenario>**
    > <80–150 word body>
    (repeat per implication)

    ## Key Distinctions
    > [!key-distinction] **<contrast>**
    > <60–120 word body>
    (repeat)

    ## Key Figures
    - **<name>** — <30–80 word contribution>
    (repeat)

    ## Open Questions
    > [!open-question] **<question>**
    > <what would resolve it>
    (repeat)

    ## Synthesis
    <1–2 paragraphs>

    ## Evidence
    <optional 1 paragraph narrative>

    ## Connections & Context
    **Falls under:** [[Parent]]
    **Prerequisites:** ...
    **Sibling concepts:** ...
    **Specializes:** ...
    **Generalizes to:** ...
    **Applies to:** ...
    **Contrasts with:** ...

    **Source:** [[<report-stem>]]

The renderer is pure: it never calls the network and never writes to disk.

Version:
    1.0.0
Python:
    >=3.10
"""
from __future__ import annotations

import datetime as dt
import logging
import re
from collections import defaultdict
from typing import Any, Iterable

from lib.markdown import callout, join_wikilinks, wikilink

from .prompts import RELATION_TYPES

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Pipeline-version tag stamped into provenance.
PIPELINE_VERSION: str = "v6.0.0"

#: Mapping from RELATION_TYPES → connection-section header label.
RELATION_LABELS: dict[str, str] = {
    "prerequisite":   "Prerequisites",
    "specializes":    "Specializes",
    "generalizes":    "Generalizes to",
    "sibling":        "Sibling concepts",
    "contradicts":    "Contradicts",
    "contrasts-with": "Contrasts with",
    "applies-to":     "Applies to",
    "formalizes":     "Formalizes",
    "instance-of":    "Instance of",
    "supports":       "Supports",
    "refines":        "Refines",
}

#: Display order in the Connections & Context block.
CONNECTION_ORDER: tuple[str, ...] = (
    "prerequisite", "specializes", "generalizes", "sibling",
    "contrasts-with", "contradicts", "applies-to",
    "formalizes", "instance-of", "supports", "refines",
)


# ════════════════════════════════════════════════════════════════════════════
# Small helpers
# ════════════════════════════════════════════════════════════════════════════

def _quote_yaml(s: str) -> str:
    """Escape a string for double-quoted YAML."""
    return (s or "").replace("\\", "\\\\").replace("\"", "\\\"")


def _yaml_block_list(items: Iterable[str], *, wikilink_wrap: bool = False,
                     quote: bool = True) -> str:
    """Render an iterable as a YAML block sequence (2-space indent)."""
    items = [s for s in (str(x).strip() for x in items) if s]
    if not items:
        return "  - \"\""
    out: list[str] = []
    for s in items:
        if wikilink_wrap:
            out.append(f"  - \"[[{_quote_yaml(s)}]]\"")
        elif quote:
            out.append(f"  - \"{_quote_yaml(s)}\"")
        else:
            out.append(f"  - {s}")
    return "\n".join(out)


def _attr(obj: Any, name: str, default: Any = None) -> Any:
    """Get attribute from a pydantic model OR a dict OR a fallback default."""
    if obj is None:
        return default
    if hasattr(obj, name):
        v = getattr(obj, name)
        return v if v is not None else default
    if isinstance(obj, dict):
        return obj.get(name, default)
    return default


_WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)(?:[#\|][^\]]*)?\]\]")


def harvest_wikilinks(text: str) -> list[str]:
    """Return ordered, deduped wikilink targets in ``text``."""
    seen: dict[str, None] = {}
    for m in _WIKILINK_RE.finditer(text or ""):
        target = m.group(1).strip()
        if target and target not in seen:
            seen[target] = None
    return list(seen.keys())


# ════════════════════════════════════════════════════════════════════════════
# Frontmatter
# ════════════════════════════════════════════════════════════════════════════

def render_frontmatter(
    bundle: Any,
    outline: Any,
    elaborate: Any,
    *,
    today: dt.date,
    outline_contract: str,
    elaborate_contract: str,
) -> str:
    """Render the V6 YAML frontmatter block.

    Args:
        bundle: V4 ConceptBundle.
        outline: Pass-A response.
        elaborate: Pass-B response (may be None for unworthy notes).
        today: Date stamp for created/updated.
        outline_contract: e.g. ``"v6-outline-v1"``.
        elaborate_contract: e.g. ``"v6-elaborate-v1"``.

    Returns:
        The frontmatter block (opening ``---`` through closing ``---``).
    """
    title = _attr(outline, "canonical_title", bundle.title) or bundle.title
    aliases_seq = list(dict.fromkeys([title, *getattr(bundle, "aliases", [])]))[:8]
    domain = (_attr(outline, "domain_hint", "")
              or getattr(bundle, "domain", "")
              or "other")
    parent = _attr(outline, "parent_concept", "") or ""

    # Bucket related concepts by relation for frontmatter richness.
    rel_buckets: dict[str, list[str]] = defaultdict(list)
    for rc in (_attr(outline, "related_concepts", []) or []):
        c = _attr(rc, "concept", "")
        r = _attr(rc, "relation", "sibling")
        if c:
            rel_buckets[r if r in RELATION_TYPES else "sibling"].append(c)

    related_flat: list[str] = []
    for r in CONNECTION_ORDER:
        related_flat.extend(rel_buckets.get(r, []))
    related_flat = list(dict.fromkeys(related_flat))[:12]

    confidence_map = {"high": "high", "medium": "medium", "low": "low"}
    confidence = confidence_map.get(
        (getattr(bundle, "confidence", "medium") or "medium").lower(),
        "medium",
    )

    fm = [
        "---",
        f"title: \"{_quote_yaml(title)}\"",
        "aliases:",
        _yaml_block_list(aliases_seq),
        "type: permanent-note",
        "status: enriched",
        f"confidence: {confidence}",
        "",
        "tags:",
        _yaml_block_list(
            ["permanent-note", "v6-llm-elaborated", domain],
            quote=False,
        ),
        "",
        f"domain: {domain}",
        "subdomains:",
        _yaml_block_list(getattr(bundle, "subdomains", [])[:4] or [""],
                         quote=False),
        "",
        f"created: {today.isoformat()}",
        f"updated: {today.isoformat()}",
        "",
        "source-type: report-extraction",
        "source-reports:",
        f"  - \"{_quote_yaml(getattr(bundle, 'report_stem', ''))}\"",
        f"evidence-quality: {confidence}",
        "extraction-method: \"pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)\"",
        "",
        "complexity-level: advanced-practitioner",
        "depth-level: elaborated",
        "",
        f"parent-concept: \"{_quote_yaml(parent)}\"" if parent
            else "parent-concept: \"\"",
        "",
        "related:",
        (_yaml_block_list(related_flat, wikilink_wrap=True)
            if related_flat else "  - \"[[]]\""),
    ]
    # Per-relation bucket fields for downstream Dataview queries.
    for r in CONNECTION_ORDER:
        items = rel_buckets.get(r, [])
        key = {
            "prerequisite":   "prerequisites",
            "specializes":    "specializes",
            "generalizes":    "broader",
            "sibling":        "see-also",
            "contradicts":    "contradicts",
            "contrasts-with": "contrasts-with",
            "applies-to":     "applies-to",
            "formalizes":     "formalizes",
            "instance-of":    "instance-of",
            "supports":       "supports",
            "refines":        "refines",
        }[r]
        fm.append(f"{key}:")
        fm.append(_yaml_block_list(items, wikilink_wrap=True)
                  if items else "  - \"[[]]\"")

    fm += [
        "",
        "review-frequency: quarterly",
        "mastery-stage: budding",
        "importance: medium",
        "",
        "provenance:",
        f"  pipeline-version: \"{PIPELINE_VERSION}\"",
        f"  outline-contract: \"{outline_contract}\"",
        f"  elaborate-contract: \"{elaborate_contract}\"",
        "  passes: 2",
        "---",
    ]
    return "\n".join(fm)


# ════════════════════════════════════════════════════════════════════════════
# Body sections
# ════════════════════════════════════════════════════════════════════════════

def _section_header(title: str) -> list[str]:
    return [f"## {title}", ""]


def _para_block(paragraphs: Iterable[str]) -> list[str]:
    """Render a list of paragraphs separated by blank lines."""
    out: list[str] = []
    for p in paragraphs:
        text = (p or "").strip()
        if text:
            out.append(text)
            out.append("")
    return out


def render_definition_callout(
    title: str,
    elaborated_definition: str,
    parent: str,
) -> str:
    """Render the headline [!definition] callout.

    If the LLM didn't already weave the parent reference into the body,
    we append a short ``Falls under [[Parent]].`` sentence so the link is
    always present.
    """
    body = (elaborated_definition or "").strip()
    if parent:
        # Detect whether the LLM already referenced the parent (by name OR
        # as a wiki-link). If not, append a fallback sentence.
        target_norm = parent.lower().replace("[[", "").replace("]]", "")
        if target_norm not in body.lower():
            link = f"[[{parent}]]"
            body = f"{body} It falls under {link}." if body else \
                   f"It falls under {link}."
    return callout("definition", f"**{title}**", body)


def render_implications(impls: list[Any]) -> list[str]:
    """Render the Practical Implications section."""
    if not impls:
        return []
    out = _section_header("Practical Implications")
    for i, imp in enumerate(impls, start=1):
        scenario = (_attr(imp, "scenario", "") or "").strip()
        body = (_attr(imp, "body", "") or "").strip()
        if not body:
            continue
        head = f"**Application {i} — {scenario}**" if scenario \
               else f"**Application {i}**"
        out.append(callout("example", head, body))
        out.append("")
    return out


def render_distinctions(dists: list[Any]) -> list[str]:
    """Render the Key Distinctions section."""
    if not dists:
        return []
    out = _section_header("Key Distinctions")
    for d in dists:
        contrast = (_attr(d, "contrast", "") or "").strip()
        body = (_attr(d, "body", "") or "").strip()
        if not body:
            continue
        head = f"**{contrast}**" if contrast else "**Distinction**"
        out.append(callout("key-distinction", head, body))
        out.append("")
    return out


def render_figures(figures: list[Any]) -> list[str]:
    """Render the Key Figures section."""
    if not figures:
        return []
    out = _section_header("Key Figures")
    for f in figures:
        name = (_attr(f, "name", "") or "").strip()
        contrib = (_attr(f, "contribution", "") or "").strip()
        if not name:
            continue
        if contrib:
            out.append(f"- **{name}** — {contrib}")
        else:
            out.append(f"- **{name}**")
    out.append("")
    return out


def render_open_questions(oqs: list[Any]) -> list[str]:
    """Render the Open Questions section."""
    if not oqs:
        return []
    out = _section_header("Open Questions")
    for oq in oqs:
        q = (_attr(oq, "question", "") or "").strip()
        resolve = (_attr(oq, "what_would_resolve_it", "") or "").strip()
        if not q:
            continue
        body = q
        if resolve:
            body = f"{q}\n\n*What would resolve it:* {resolve}"
        out.append(callout("open-question", "**Question**", body))
        out.append("")
    return out


def render_connections(
    bundle: Any,
    outline: Any,
) -> list[str]:
    """Render the final Connections & Context section."""
    out = _section_header("Connections & Context")

    parent = _attr(outline, "parent_concept", "") or ""
    if parent:
        out.append(f"**Falls under:** [[{parent}]]")
        out.append("")

    # Bucket related concepts by relation.
    rel_buckets: dict[str, list[str]] = defaultdict(list)
    for rc in (_attr(outline, "related_concepts", []) or []):
        c = _attr(rc, "concept", "")
        r = _attr(rc, "relation", "sibling")
        if c:
            rel_buckets[r if r in RELATION_TYPES else "sibling"].append(c)

    for r in CONNECTION_ORDER:
        items = rel_buckets.get(r, [])
        if not items:
            continue
        label = RELATION_LABELS[r]
        out.append(f"**{label}:** " + join_wikilinks(items))
        out.append("")

    report_stem = getattr(bundle, "report_stem", "")
    if report_stem:
        out.append(f"**Source:** {wikilink(report_stem)}")
        out.append("")
    return out


# ════════════════════════════════════════════════════════════════════════════
# Top-level body assembly
# ════════════════════════════════════════════════════════════════════════════

def render_body(
    bundle: Any,
    outline: Any,
    elaborate: Any,
) -> str:
    """Assemble the full markdown body (no frontmatter)."""
    title = _attr(outline, "canonical_title", bundle.title) or bundle.title
    parent = _attr(outline, "parent_concept", "") or ""

    parts: list[str] = [f"# {title}", ""]

    # Definition callout — always present.
    elaborated_def = _attr(elaborate, "elaborated_definition", "") \
        or _attr(outline, "seed_definition", "") \
        or ""
    parts.append(render_definition_callout(title, elaborated_def, parent))
    parts.append("")

    # Boundary callout — only when LLM provided one and it's not already
    # subsumed by the elaborated definition.
    boundary = (_attr(outline, "definition_boundary", "") or "").strip()
    if boundary and boundary.lower() not in elaborated_def.lower():
        parts.append(callout("attention", "**Boundary**", boundary))
        parts.append("")

    # Core Explanation.
    core = list(_attr(elaborate, "core_explanation_paragraphs", []) or [])
    if core:
        parts += _section_header("Core Explanation")
        parts += _para_block(core)

    # Mechanism.
    mech = list(_attr(elaborate, "mechanism_paragraphs", []) or [])
    if mech:
        parts += _section_header("Mechanism")
        parts += _para_block(mech)

    # Practical Implications.
    parts += render_implications(
        list(_attr(elaborate, "practical_implications", []) or [])
    )

    # Key Distinctions.
    parts += render_distinctions(
        list(_attr(elaborate, "key_distinctions", []) or [])
    )

    # Key Figures.
    parts += render_figures(
        list(_attr(elaborate, "key_figures", []) or [])
    )

    # Open Questions.
    parts += render_open_questions(
        list(_attr(elaborate, "open_questions", []) or [])
    )

    # Synthesis.
    syn = list(_attr(elaborate, "synthesis_paragraphs", []) or [])
    if syn:
        parts += _section_header("Synthesis")
        parts += _para_block(syn)

    # Evidence narrative (single paragraph).
    evidence = (_attr(elaborate, "evidence_narrative", "") or "").strip()
    if evidence:
        parts += _section_header("Evidence")
        parts.append(evidence)
        parts.append("")

    # Connections & Context.
    parts += render_connections(bundle, outline)

    return "\n".join(parts).rstrip() + "\n"


# ════════════════════════════════════════════════════════════════════════════
# Top-level: full note
# ════════════════════════════════════════════════════════════════════════════

def render_note(
    bundle: Any,
    outline: Any,
    elaborate: Any,
    *,
    today: dt.date,
    outline_contract: str,
    elaborate_contract: str,
) -> str:
    """Render frontmatter + body as a single string (the final file content)."""
    fm = render_frontmatter(
        bundle, outline, elaborate,
        today=today,
        outline_contract=outline_contract,
        elaborate_contract=elaborate_contract,
    )
    body = render_body(bundle, outline, elaborate)
    return f"{fm}\n\n{body}"


__all__ = [
    "PIPELINE_VERSION",
    "RELATION_LABELS",
    "CONNECTION_ORDER",
    "harvest_wikilinks",
    "render_frontmatter",
    "render_definition_callout",
    "render_implications",
    "render_distinctions",
    "render_figures",
    "render_open_questions",
    "render_connections",
    "render_body",
    "render_note",
]
