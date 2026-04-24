#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prompts — V6 two-pass prompt contracts + response schemas.

V6 swaps V4's single-pass condensation for a deliberate two-pass elaboration:

    Pass A (outline)    : Triage worthiness, pick canonical title, define
                          *boundary* and *parent concept*, plan section
                          intents and source hooks.
    Pass B (elaborate)  : Given the outline + same source bundle, write
                          long-form prose for every section the outline
                          requested. The renderer never touches narrative
                          content — it only frames what the LLM produces.

A third contract handles merges into existing V6 notes (re-runs).

All three contracts have isolated cache keys via PROMPT_CONTRACT_VERSION
constants. Bumping any one invalidates only that contract's cache.

Version:
    1.0.0
Python:
    >=3.10
"""
from __future__ import annotations

import logging
from typing import Any

try:
    from pydantic import BaseModel, Field, field_validator
    _PYDANTIC_AVAILABLE = True
except ImportError:  # pragma: no cover
    BaseModel = object  # type: ignore[assignment,misc]
    _PYDANTIC_AVAILABLE = False

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Contract version keys
# ════════════════════════════════════════════════════════════════════════════

#: Outline pass cache key. Bump on schema/prompt changes.
OUTLINE_CONTRACT_VERSION: str = "v6-outline-v1"
#: Elaboration pass cache key. Bump on schema/prompt changes.
ELABORATE_CONTRACT_VERSION: str = "v6-elaborate-v1"
#: Merge contract cache key. Bump on schema/prompt changes.
MERGE_CONTRACT_VERSION: str = "v6-merge-v1"

#: Soft cap on existing-note body fed to merge prompt.
EXISTING_NOTE_MAX_CHARS: int = 12000

#: Allowed `relation_type` values for related_concepts entries.
RELATION_TYPES: frozenset[str] = frozenset({
    "prerequisite", "sibling", "generalizes", "specializes",
    "contradicts", "applies-to", "formalizes", "instance-of",
    "supports", "refines", "contrasts-with",
})


# ════════════════════════════════════════════════════════════════════════════
# Schemas — Pass A (Outline)
# ════════════════════════════════════════════════════════════════════════════

if _PYDANTIC_AVAILABLE:

    class SectionPlan(BaseModel):  # type: ignore[misc,valid-type]
        """One planned section the elaboration pass should write."""
        section: str = Field(min_length=2, max_length=60)
        intent: str = Field(min_length=10, max_length=400)
        source_hooks: list[str] = Field(default_factory=list)

        @field_validator("source_hooks", mode="before")
        @classmethod
        def _coerce_hooks(cls, v: Any) -> list[str]:
            if v is None:
                return []
            if isinstance(v, str):
                return [v] if v.strip() else []
            return [str(x).strip() for x in v if str(x).strip()]


    class RelatedConcept(BaseModel):  # type: ignore[misc,valid-type]
        """Related concept with a typed relation."""
        concept: str = Field(min_length=2, max_length=120)
        relation: str = Field(default="sibling")
        rationale: str = Field(default="", max_length=300)

        @field_validator("relation", mode="before")
        @classmethod
        def _norm_relation(cls, v: Any) -> str:
            if not isinstance(v, str):
                return "sibling"
            r = v.strip().lower().replace("_", "-").replace(" ", "-")
            # Direct hit on canonical types.
            if r in RELATION_TYPES:
                return r
            # Common LLM synonym mappings → canonical relation types.
            synonyms: dict[str, str] = {
                # contrasts-with
                "contrast": "contrasts-with",
                "contrasts": "contrasts-with",
                "contrasted-with": "contrasts-with",
                "opposite": "contrasts-with",
                "opposed-to": "contrasts-with",
                "antithesis": "contrasts-with",
                # generalizes (this concept's PARENT)
                "broader": "generalizes",
                "broader-than": "generalizes",
                "parent": "generalizes",
                "parent-of": "generalizes",
                "supertype": "generalizes",
                "is-a": "generalizes",
                "is-kind-of": "generalizes",
                "subclass-of": "generalizes",
                "generalization": "generalizes",
                "generalization-of": "generalizes",
                # specializes (this concept's CHILD)
                "narrower": "specializes",
                "narrower-than": "specializes",
                "subtype": "specializes",
                "specialization": "specializes",
                "specialization-of": "specializes",
                "child": "specializes",
                "child-of": "specializes",
                # sibling
                "related": "sibling",
                "related-to": "sibling",
                "see-also": "sibling",
                "associated": "sibling",
                "associated-with": "sibling",
                "peer": "sibling",
                # prerequisite
                "depends-on": "prerequisite",
                "requires": "prerequisite",
                "required-by": "prerequisite",
                "foundational": "prerequisite",
                # contradicts
                "contradiction": "contradicts",
                "negates": "contradicts",
                "incompatible-with": "contradicts",
                # applies-to
                "applies": "applies-to",
                "applied-to": "applies-to",
                "used-in": "applies-to",
                "used-for": "applies-to",
                # supports
                "support": "supports",
                "supported-by": "supports",
                "evidence-for": "supports",
                # refines
                "refinement": "refines",
                "refinement-of": "refines",
                "extends": "refines",
                # formalizes
                "formalization": "formalizes",
                "formalization-of": "formalizes",
                # instance-of
                "instance": "instance-of",
                "example-of": "instance-of",
            }
            mapped = synonyms.get(r)
            return mapped if mapped else "sibling"


    class KeyFigurePlan(BaseModel):  # type: ignore[misc,valid-type]
        """Skeletal figure entry — elaboration pass will flesh out."""
        name: str = Field(min_length=2, max_length=120)
        role: str = Field(default="", max_length=200)


    class OutlineResponse(BaseModel):  # type: ignore[misc,valid-type]
        """Pass A output: the structural plan for the permanent note."""
        worthy: bool = True
        worthy_reason: str = ""
        canonical_title: str = Field(min_length=2, max_length=120)
        seed_definition: str = Field(min_length=10, max_length=600)
        definition_boundary: str = Field(default="", max_length=600)
        parent_concept: str = Field(default="", max_length=120)
        domain_hint: str = Field(default="", max_length=60)
        section_outline: list[SectionPlan] = Field(default_factory=list)
        related_concepts: list[RelatedConcept] = Field(default_factory=list)
        key_figures: list[KeyFigurePlan] = Field(default_factory=list)
        open_questions_seed: list[str] = Field(default_factory=list)
        key_distinctions_seed: list[str] = Field(default_factory=list)

        @field_validator(
            "section_outline", "related_concepts", "key_figures",
            "open_questions_seed", "key_distinctions_seed",
            mode="before",
        )
        @classmethod
        def _coerce_list(cls, v: Any) -> list[Any]:
            if v is None:
                return []
            if isinstance(v, str):
                return [v] if v.strip() else []
            return v if isinstance(v, list) else []

        @field_validator("key_figures", mode="before")
        @classmethod
        def _drop_unnamed_figures(cls, v: Any) -> list[Any]:
            """Drop figure entries with empty/missing names rather than failing."""
            if not isinstance(v, list):
                return v
            out = []
            for item in v:
                if isinstance(item, dict):
                    name = (item.get("name") or "").strip()
                    if len(name) >= 2:
                        out.append(item)
                else:
                    name = (getattr(item, "name", "") or "").strip()
                    if len(name) >= 2:
                        out.append(item)
            return out

        @field_validator("seed_definition")
        @classmethod
        def _def_nonblank(cls, v: str) -> str:
            v = v.strip()
            if not v:
                raise ValueError("seed_definition must not be blank")
            return v


    # ────────────────────────────────────────────────────────────────────
    # Schemas — Pass B (Elaborate)
    # ────────────────────────────────────────────────────────────────────

    class ImplicationBlock(BaseModel):  # type: ignore[misc,valid-type]
        """One elaborated practical-implication entry."""
        scenario: str = Field(min_length=2, max_length=120)
        body: str = Field(min_length=40, max_length=1500)


    class DistinctionBlock(BaseModel):  # type: ignore[misc,valid-type]
        """One key-distinction (X vs Y) elaborated entry."""
        contrast: str = Field(min_length=2, max_length=120)
        body: str = Field(min_length=30, max_length=1200)


    class FigureBlock(BaseModel):  # type: ignore[misc,valid-type]
        """Elaborated figure entry."""
        name: str = Field(min_length=2, max_length=120)
        contribution: str = Field(min_length=10, max_length=600)


    class OpenQuestionBlock(BaseModel):  # type: ignore[misc,valid-type]
        """Elaborated open-question entry."""
        question: str = Field(min_length=5, max_length=300)
        what_would_resolve_it: str = Field(default="", max_length=600)


    class ElaborateResponse(BaseModel):  # type: ignore[misc,valid-type]
        """Pass B output: the long-form material for every section."""
        elaborated_definition: str = Field(min_length=40, max_length=1500)
        core_explanation_paragraphs: list[str] = Field(default_factory=list)
        mechanism_paragraphs: list[str] = Field(default_factory=list)
        practical_implications: list[ImplicationBlock] = Field(default_factory=list)
        key_distinctions: list[DistinctionBlock] = Field(default_factory=list)
        key_figures: list[FigureBlock] = Field(default_factory=list)
        open_questions: list[OpenQuestionBlock] = Field(default_factory=list)
        synthesis_paragraphs: list[str] = Field(default_factory=list)
        evidence_narrative: str = Field(default="", max_length=2000)

        @field_validator(
            "core_explanation_paragraphs", "mechanism_paragraphs",
            "synthesis_paragraphs",
            mode="before",
        )
        @classmethod
        def _coerce_str_list(cls, v: Any) -> list[str]:
            if v is None:
                return []
            if isinstance(v, str):
                return [v] if v.strip() else []
            return [str(x).strip() for x in v if str(x).strip()]

        @field_validator(
            "practical_implications", "key_distinctions",
            "key_figures", "open_questions",
            mode="before",
        )
        @classmethod
        def _coerce_block_list(cls, v: Any) -> list[Any]:
            if v is None:
                return []
            if isinstance(v, list):
                return v
            return []

        @field_validator("key_figures", mode="before")
        @classmethod
        def _drop_unnamed_figures_e(cls, v: Any) -> list[Any]:
            """Drop figure entries with empty/missing names rather than failing."""
            if not isinstance(v, list):
                return v
            out = []
            for item in v:
                if isinstance(item, dict):
                    name = (item.get("name") or "").strip()
                    if len(name) >= 2:
                        out.append(item)
                else:
                    name = (getattr(item, "name", "") or "").strip()
                    if len(name) >= 2:
                        out.append(item)
            return out


    # ────────────────────────────────────────────────────────────────────
    # Schema — Merge contract
    # ────────────────────────────────────────────────────────────────────

    class MergeResponseV6(BaseModel):  # type: ignore[misc,valid-type]
        """Merge-pass schema: reconcile new bundle with existing V6 note."""
        merged_definition: str = Field(min_length=40, max_length=1500)
        merged_core_paragraphs: list[str] = Field(default_factory=list)
        merged_mechanism_paragraphs: list[str] = Field(default_factory=list)
        added_implications: list[ImplicationBlock] = Field(default_factory=list)
        added_distinctions: list[DistinctionBlock] = Field(default_factory=list)
        added_figures: list[FigureBlock] = Field(default_factory=list)
        added_open_questions: list[OpenQuestionBlock] = Field(default_factory=list)
        added_synthesis_paragraphs: list[str] = Field(default_factory=list)
        preserved_wikilinks: list[str] = Field(default_factory=list)
        new_wikilinks: list[str] = Field(default_factory=list)
        related_concepts: list[RelatedConcept] = Field(default_factory=list)
        change_summary: str = Field(default="", max_length=600)
        status_recommendation: str = Field(default="keep")
        tensions_introduced: list[str] = Field(default_factory=list)

        @field_validator(
            "merged_core_paragraphs", "merged_mechanism_paragraphs",
            "added_synthesis_paragraphs", "preserved_wikilinks",
            "new_wikilinks", "tensions_introduced",
            mode="before",
        )
        @classmethod
        def _coerce_str_list(cls, v: Any) -> list[str]:
            if v is None:
                return []
            if isinstance(v, str):
                return [v] if v.strip() else []
            return [str(x).strip() for x in v if str(x).strip()]

        @field_validator("status_recommendation", mode="before")
        @classmethod
        def _norm_status_rec(cls, v: Any) -> str:
            if not isinstance(v, str):
                return "keep"
            s = v.strip().lower()
            return s if s in {"keep", "promote_to_enriched"} else "keep"

else:  # pragma: no cover
    SectionPlan = None  # type: ignore[assignment,misc]
    RelatedConcept = None  # type: ignore[assignment,misc]
    KeyFigurePlan = None  # type: ignore[assignment,misc]
    OutlineResponse = None  # type: ignore[assignment,misc]
    ImplicationBlock = None  # type: ignore[assignment,misc]
    DistinctionBlock = None  # type: ignore[assignment,misc]
    FigureBlock = None  # type: ignore[assignment,misc]
    OpenQuestionBlock = None  # type: ignore[assignment,misc]
    ElaborateResponse = None  # type: ignore[assignment,misc]
    MergeResponseV6 = None  # type: ignore[assignment,misc]


# ════════════════════════════════════════════════════════════════════════════
# Pass A — Outline prompts
# ════════════════════════════════════════════════════════════════════════════

OUTLINE_SYSTEM_PROMPT: str = (
    "You are a meticulous knowledge-base architect planning ONE atomic "
    "permanent note about a single concept. Your job is structural: decide "
    "WHAT the note should contain, identify the concept's boundary and "
    "parent concept, and plan the sections the elaboration pass will "
    "write. Do not draft long prose yet — Pass B handles that. Reply "
    "with valid JSON only — no markdown fences, no commentary. Never "
    "invent citations, dates, or biographical claims absent from the "
    "supplied material."
)

OUTLINE_USER_TEMPLATE: str = """\
Concept: {title!r}
Source report: {report_title}
Primary domain: {domain}
Report aliases: {aliases}
Related wiki-links from report: {related_links}

Source definition (from extracted [!definition] callout):
\"\"\"
{definition_body}
\"\"\"

Supporting callouts from the same report (use as evidence — do not invent
beyond them):
{support_block}

# YOUR TASK — Pass A: PLAN the permanent note

Step 1: Decide WORTHINESS.
A concept is WORTHY only if ALL hold:
  1. Named, teachable concept (theory, framework, principle, mechanism,
     technique, model, distinction) with explanatory power beyond one
     example.
  2. Re-usable across multiple contexts.
  3. The supplied material gives ENOUGH SUBSTANCE for a definition plus
     at least 3 paragraphs of core explanation.
  4. Not redundant with a more canonical concept already in
     `related_links` or `aliases`.

If unworthy, set worthy=false, give worthy_reason, set canonical_title
and seed_definition to brief placeholders, leave all list fields empty.

Step 2: If worthy, produce a PLAN with these fields:

  canonical_title         The concept's clean canonical title (Title Case).
                          Strip parentheticals like "(Sweller, 1988)".

  seed_definition         A 1–2 sentence neutral definition (NOT yet the
                          elaborated callout — Pass B writes that).

  definition_boundary     1–3 sentences: where this concept STOPS. What is
                          adjacent but EXCLUDED? What it should NOT be
                          confused with. (This becomes part of the
                          definition callout.)

  parent_concept          The single broader concept this falls under.
                          Use a short noun phrase (e.g., "Cognitive
                          Architecture", "Self-Regulated Learning").
                          Empty string if no clear parent exists.

  domain_hint             One of: cognitive-psychology, educational-
                          psychology, philosophy, neuroscience,
                          prompt-engineering, computer-science,
                          decision-science, epistemology, learning-
                          science, linguistics, mathematics,
                          systems-thinking, other.

  section_outline         List of {{section, intent, source_hooks}}. Plan
                          ONLY the sections the source material can
                          actually support. Standard sections (include
                          when warranted):

                            - "Core Explanation"  (always — 4–6 paragraphs)
                            - "Mechanism"         (when there's process/how-it-works detail)
                            - "Practical Implications"  (3–5 elaborated applications)
                            - "Key Distinctions"  (when contrasts exist)
                            - "Key Figures"       (when [!person] callouts attribute work)
                            - "Open Questions"    (when [!open-question] or [!tension] callouts exist)
                            - "Synthesis"         (always — 1–2 paragraph "why this matters")

                          For each section, write a 1–2 sentence INTENT
                          explaining what Pass B should cover, and list
                          the source-callout titles that should anchor it
                          (`source_hooks`).

  related_concepts        List of {{concept, relation, rationale}}. Choose
                          relation from: prerequisite, sibling,
                          generalizes, specializes, contradicts,
                          applies-to, formalizes, instance-of, supports,
                          refines, contrasts-with. 4–10 items typical.

  key_figures             List of {{name, role}}. Skeletal — Pass B
                          fleshes out contributions. Empty if no
                          [!person] callouts.

  open_questions_seed     List of question strings the source raises.

  key_distinctions_seed   List of distinction strings (e.g.,
                          "intrinsic vs extraneous load").

# OUTPUT — valid JSON only

{{
  "worthy":              true,
  "worthy_reason":       "<1 short sentence>",
  "canonical_title":     "<Title Case>",
  "seed_definition":     "<1–2 sentences>",
  "definition_boundary": "<1–3 sentences on what is excluded>",
  "parent_concept":      "<single broader concept noun phrase>",
  "domain_hint":         "<one of the allowed domains>",
  "section_outline":     [
    {{"section": "Core Explanation", "intent": "...", "source_hooks": ["..."]}},
    {{"section": "Mechanism",        "intent": "...", "source_hooks": ["..."]}},
    {{"section": "Practical Implications", "intent": "...", "source_hooks": ["..."]}},
    {{"section": "Key Distinctions", "intent": "...", "source_hooks": ["..."]}},
    {{"section": "Key Figures",      "intent": "...", "source_hooks": ["..."]}},
    {{"section": "Open Questions",   "intent": "...", "source_hooks": ["..."]}},
    {{"section": "Synthesis",        "intent": "...", "source_hooks": ["..."]}}
  ],
  "related_concepts": [
    {{"concept": "Working Memory", "relation": "prerequisite", "rationale": "..."}},
    {{"concept": "Worked Examples", "relation": "applies-to",  "rationale": "..."}}
  ],
  "key_figures": [
    {{"name": "John Sweller", "role": "originator (1988)"}}
  ],
  "open_questions_seed":   ["...", "..."],
  "key_distinctions_seed": ["intrinsic vs extraneous load", "..."]
}}

Hard rules:
- ALL keys MUST be present.
- "worthy" MUST be a boolean.
- "seed_definition" MUST NOT be empty even when worthy=false (one short sentence).
- Section names in `section_outline` MUST be unique.
- Do NOT include {title!r} itself in `related_concepts`.
- Do NOT include the parent_concept inside `related_concepts` (it's already promoted).
- Respond with ONE JSON object. No markdown fences. No prose.
"""


def build_outline_user_prompt(
    *,
    title: str,
    report_title: str,
    domain: str,
    aliases: list[str],
    related_links: list[str],
    definition_body: str,
    support_block: str,
) -> str:
    """Render the Pass A user prompt."""
    return OUTLINE_USER_TEMPLATE.format(
        title=title,
        report_title=report_title or "(unknown)",
        domain=domain or "(none)",
        aliases=", ".join(aliases) if aliases else "(none)",
        related_links=", ".join(related_links) if related_links else "(none)",
        definition_body=definition_body or "(no body)",
        support_block=support_block or "(no supporting callouts)",
    )


# ════════════════════════════════════════════════════════════════════════════
# Pass B — Elaborate prompts
# ════════════════════════════════════════════════════════════════════════════

ELABORATE_SYSTEM_PROMPT: str = (
    "You are a careful scholarly author writing the LONG-FORM body of an "
    "atomic permanent note. You receive: (1) the source material, and "
    "(2) an OUTLINE produced by an earlier planning pass. Your job is to "
    "write rich, integrated PROSE (not bullet lists) for every section "
    "the outline calls for. Synthesize evidence into a coherent narrative "
    "rather than restating callouts. Never invent citations, dates, or "
    "biographical claims absent from the source material. Reply with "
    "valid JSON only — no markdown fences."
)

ELABORATE_USER_TEMPLATE: str = """\
You are writing Pass B (elaboration) for a permanent note about {title!r}.

# OUTLINE FROM PASS A
{outline_block}

# SOURCE MATERIAL
Source report: {report_title}
Primary domain: {domain}

Source definition:
\"\"\"
{definition_body}
\"\"\"

Supporting callouts:
{support_block}

# YOUR TASK — Pass B: ELABORATE every planned section

Produce the rich body content. Follow the outline's section list and
intents. Write PROSE, not bullets. Synthesize across callouts — do not
just restate them in order.

Field-by-field requirements:

  elaborated_definition
      A 2–4 sentence integrated definition that combines:
        (a) the seed definition,
        (b) the boundary (what's excluded),
        (c) an embedded reference to the parent concept as
            "It falls under [[Parent-Concept]]" or similar.
      This is the body of the [!definition] callout. Write it as
      flowing prose, not a bulleted breakdown.

  core_explanation_paragraphs
      4–6 narrative paragraphs (each 80–180 words) covering:
        - foundational mechanism / core meaning
        - how it operates in practice
        - theoretical roots and conceptual nuances
        - empirical or historical grounding (if material supports it)
      INTEGRATE the supporting callouts. Do NOT enumerate them.

  mechanism_paragraphs
      0–3 paragraphs. Include ONLY if the source material describes a
      concrete process / how-it-works mechanism. Step-by-step or
      stage-by-stage prose.

  practical_implications
      3–5 entries. Each has:
        scenario : short label (e.g., "Instructional design")
        body     : 80–150 words elaborating one concrete application,
                   with a specific scenario, what the concept implies
                   for that scenario, and what would be observably
                   different from ignoring it.

  key_distinctions
      0–4 entries. Each has:
        contrast : short "X vs Y" or "X is not Y" label
        body     : 60–120 words explaining the distinction, why it
                   matters, and how to tell them apart in practice.

  key_figures
      Match the outline's key_figures list (or refine it). Each:
        name         : person's name
        contribution : 30–80 words on their specific contribution to
                       this concept (NOT a biography). Only include
                       facts present in the source material.

  open_questions
      Reflect outline's open_questions_seed and any from
      [!open-question] / [!tension] callouts. Each:
        question                : the question, framed precisely
        what_would_resolve_it   : 1–2 sentences on what evidence /
                                  argument / experiment would settle it.

  synthesis_paragraphs
      1–2 paragraphs (each 80–150 words) answering "why does this
      concept matter?" Connect it to broader implications across the
      domains in `related_concepts`. This is the take-home value.

  evidence_narrative
      Optional. 1 paragraph (≤200 words) weaving together the strongest
      evidence from the supporting callouts (especially [!evidence] and
      [!key-claim] callouts) into a coherent argument. Empty string if
      no evidence callouts exist.

# OUTPUT — valid JSON only

{{
  "elaborated_definition": "<2–4 sentences>",
  "core_explanation_paragraphs": ["<para 1>", "<para 2>", "<para 3>", "<para 4>"],
  "mechanism_paragraphs":        ["<optional para>", "..."],
  "practical_implications": [
    {{"scenario": "Instructional design", "body": "<80–150 words>"}},
    {{"scenario": "...", "body": "..."}}
  ],
  "key_distinctions": [
    {{"contrast": "Intrinsic vs Extraneous Load", "body": "<60–120 words>"}}
  ],
  "key_figures": [
    {{"name": "John Sweller", "contribution": "<30–80 words>"}}
  ],
  "open_questions": [
    {{"question": "...", "what_would_resolve_it": "..."}}
  ],
  "synthesis_paragraphs": ["<para 1>", "<optional para 2>"],
  "evidence_narrative": "<optional paragraph>"
}}

Hard rules:
- elaborated_definition MUST be 40+ chars and incorporate boundary + parent.
- core_explanation_paragraphs MUST contain at least 3 entries when the
  outline requested a Core Explanation section.
- All array fields MUST exist (even if empty arrays).
- Write PROSE for every body field. NO bulleted lists inside body strings.
- Do NOT include the title or parent_concept as their own related entries.
- Do NOT invent citations or dates. If unsure, omit.
- Respond with ONE JSON object. No markdown fences.
"""


def _format_outline_for_elaborate(outline: Any) -> str:
    """Render the OutlineResponse as a compact human-readable block.

    Args:
        outline: An ``OutlineResponse`` instance (or duck-type with the
            same attributes).

    Returns:
        Multi-line string the elaborator pass can read directly.
    """
    parts: list[str] = []
    parts.append(f"canonical_title: {getattr(outline, 'canonical_title', '')}")
    parts.append(f"seed_definition: {getattr(outline, 'seed_definition', '')}")
    boundary = getattr(outline, "definition_boundary", "")
    if boundary:
        parts.append(f"definition_boundary: {boundary}")
    parent = getattr(outline, "parent_concept", "")
    if parent:
        parts.append(f"parent_concept: {parent}")
    domain = getattr(outline, "domain_hint", "")
    if domain:
        parts.append(f"domain_hint: {domain}")
    def _g(obj: object, attr: str, default):
        """Attribute access that works for Pydantic models and dicts."""
        if isinstance(obj, dict):
            v = obj.get(attr, default)
        else:
            v = getattr(obj, attr, default)
        return default if v is None else v

    sections = getattr(outline, "section_outline", None) or []
    if sections:
        parts.append("section_outline:")
        for s in sections:
            sec = _g(s, "section", "")
            intent = _g(s, "intent", "")
            hooks = _g(s, "source_hooks", []) or []
            hk = ", ".join(hooks) if hooks else "(none)"
            parts.append(f"  - {sec}: {intent}  | hooks: {hk}")
    related = getattr(outline, "related_concepts", None) or []
    if related:
        parts.append("related_concepts:")
        for rc in related:
            c = _g(rc, "concept", "")
            r = _g(rc, "relation", "sibling")
            why = _g(rc, "rationale", "")
            parts.append(f"  - {c} [{r}] {why}".rstrip())
    figures = getattr(outline, "key_figures", None) or []
    if figures:
        parts.append("key_figures (skeletal):")
        for f in figures:
            n = _g(f, "name", "")
            r = _g(f, "role", "")
            parts.append(f"  - {n} — {r}".rstrip(" —"))
    oq = getattr(outline, "open_questions_seed", None) or []
    if oq:
        parts.append("open_questions_seed:")
        for q in oq:
            parts.append(f"  - {q}")
    kd = getattr(outline, "key_distinctions_seed", None) or []
    if kd:
        parts.append("key_distinctions_seed:")
        for d in kd:
            parts.append(f"  - {d}")
    return "\n".join(parts)


def build_elaborate_user_prompt(
    *,
    title: str,
    report_title: str,
    domain: str,
    definition_body: str,
    support_block: str,
    outline: Any,
) -> str:
    """Render the Pass B user prompt given the outline + source bundle."""
    outline_block = _format_outline_for_elaborate(outline)
    return ELABORATE_USER_TEMPLATE.format(
        title=title,
        report_title=report_title or "(unknown)",
        domain=domain or "(none)",
        definition_body=definition_body or "(no body)",
        support_block=support_block or "(no supporting callouts)",
        outline_block=outline_block,
    )


# ════════════════════════════════════════════════════════════════════════════
# Merge contract — V6 re-runs
# ════════════════════════════════════════════════════════════════════════════

MERGE_SYSTEM_PROMPT: str = (
    "You are a meticulous knowledge-base editor reconciling an EXISTING "
    "V6 permanent note with a NEW concept bundle from a fresh extraction. "
    "Preserve the existing note's wisdom (definition, paragraphs, "
    "wikilinks, hand-edits). Add ONLY what the new material genuinely "
    "contributes. When existing and new disagree, prefer the existing "
    "and surface the conflict in `tensions_introduced`. Never silently "
    "overwrite. Output valid JSON only."
)

MERGE_USER_TEMPLATE: str = """\
You are merging an existing V6 permanent note with a fresh concept bundle.

# Concept
Title:   {title}
Slug:    {slug}
Domain:  {domain}
Match:   tier={match_tier} score={match_score:.3f}

# EXISTING NOTE (preserve its wisdom)
```markdown
{existing_body}
```
{existing_truncated_note}

# NEW DEFINITION (from fresh extraction)
{definition_body}

# NEW SUPPORTING CALLOUTS
{support_block}

# Existing wikilinks (preserve unless clearly orphaned)
{existing_wikilinks}

# YOUR TASK

Produce a JSON object with these fields:

  merged_definition          The merged callout body. Default to existing
                             unless new material clearly improves it.
  merged_core_paragraphs     The merged core-explanation paragraphs.
                             Combine existing + additions. Preserve order
                             of existing paragraphs unless restructure
                             clearly improves clarity.
  merged_mechanism_paragraphs Same, for the Mechanism section.
  added_implications         NEW implications the bundle contributes.
                             Each: {{scenario, body (80–150 words)}}.
  added_distinctions         NEW distinctions. Each: {{contrast, body}}.
  added_figures              NEW figures only. Each: {{name, contribution}}.
  added_open_questions       NEW open questions.
  added_synthesis_paragraphs Optional: refined synthesis paragraphs.
  preserved_wikilinks        ALL wikilinks present in `existing_wikilinks`
                             that should remain (default: all of them).
  new_wikilinks              Wikilinks the new bundle adds.
  related_concepts           Updated list of {{concept, relation, rationale}}.
  change_summary             2–3 human-readable sentences describing what
                             changed. Goes into provenance.
  status_recommendation      "keep" or "promote_to_enriched".
  tensions_introduced        Conflicts between existing claims and new
                             material. Empty list if none.

Hard rules:
- NEVER drop a wikilink from `existing_wikilinks` unless the linked
  concept is genuinely irrelevant to the merged note.
- NEVER demote status. (Promotion only stub/seedling → enriched.)
- merged_definition MUST be ≥ 40 chars.
- All array fields MUST exist.
- Respond with ONE JSON object. No markdown fences.
"""


def build_merge_user_prompt(
    *,
    title: str,
    slug: str,
    domain: str,
    match_tier: str,
    match_score: float,
    existing_body: str,
    definition_body: str,
    support_block: str,
    existing_wikilinks: list[str],
) -> str:
    """Render the V6 merge user prompt."""
    truncated_note = ""
    if len(existing_body) > EXISTING_NOTE_MAX_CHARS:
        existing_body = existing_body[:EXISTING_NOTE_MAX_CHARS]
        truncated_note = (
            f"\n*(Existing note truncated at {EXISTING_NOTE_MAX_CHARS} chars "
            "— preserve everything visible above.)*\n"
        )
    return MERGE_USER_TEMPLATE.format(
        title=title,
        slug=slug,
        domain=domain or "(none)",
        match_tier=match_tier,
        match_score=match_score,
        existing_body=existing_body or "(empty)",
        existing_truncated_note=truncated_note,
        definition_body=definition_body or "(no body)",
        support_block=support_block or "(no supporting callouts)",
        existing_wikilinks=", ".join(existing_wikilinks)
            if existing_wikilinks else "(none)",
    )
