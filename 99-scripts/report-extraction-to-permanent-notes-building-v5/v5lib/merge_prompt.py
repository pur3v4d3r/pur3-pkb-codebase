#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_prompt — Prompt contract and response schema for V5 merges.

This module defines the LLM contract for *merging* an existing permanent note
with a new concept bundle. It is deliberately separate from V4's *condense*
prompt because the two tasks have different invariants:

    Condense (V4)  : "Given source material, write a permanent note."
    Merge    (V5)  : "Given an existing permanent note AND new source material,
                      reconcile them into a single note that PRESERVES the
                      existing note's wisdom and ADDS what the new material
                      contributes."

Because the contract differs, V5 ships its own ``PROMPT_CONTRACT_VERSION``
key — merges and condensations cache independently in ``LLM_CACHE_DIR``.
"""
from __future__ import annotations

import logging
from typing import Any

try:
    from pydantic import BaseModel, Field, field_validator
    _PYDANTIC_AVAILABLE = True
except ImportError:  # pragma: no cover - optional dep
    BaseModel = object  # type: ignore[assignment,misc]
    _PYDANTIC_AVAILABLE = False

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Bump when the merge prompt contract changes semantically. Cache isolation.
PROMPT_CONTRACT_VERSION: str = "v5-merge-v1"

#: Soft cap on the existing note body fed to the LLM. Notes longer than this
#: are truncated with an explicit ellipsis marker; the LLM is told this.
EXISTING_NOTE_MAX_CHARS: int = 8000

#: Soft cap on supporting callouts (mirrors V4's MAX_SUPPORT_CALLOUTS).
NEW_SUPPORT_MAX: int = 8


# ════════════════════════════════════════════════════════════════════════════
# Response schema
# ════════════════════════════════════════════════════════════════════════════

if _PYDANTIC_AVAILABLE:

    class MergeResponse(BaseModel):  # type: ignore[misc,valid-type]
        """Schema the LLM must conform to when merging an existing note.

        Fields:
            merged_definition: New canonical definition. Required.
                When in doubt, prefer the existing note's wording — only
                upgrade if the new material clearly improves precision.
            merged_explanation: 3–4 paragraph core explanation, integrating
                existing depth with new material's contributions.
            preserved_sections: Bullet list of sections/claims kept verbatim
                or near-verbatim from the existing note.
            new_content_summary: Bullet list of what the new bundle adds
                that wasn't in the existing note.
            preserved_wikilinks: Wiki-link targets present in the existing
                note that MUST appear in the merged output.
            new_wikilinks: Wiki-link targets contributed by the new material.
            change_summary: Two- or three-sentence human-readable diff.
                Goes into the note's ``provenance`` block.
            status_recommendation: Status the LLM thinks the merged note
                should carry. The pipeline only honors ``"keep"`` and
                ``"promote_to_enriched"``; other values are coerced to
                ``"keep"``.
            tensions_introduced: Optional list of contradictions the merge
                surfaced (existing said X, new material says Y).
            related_concepts: Cross-link suggestions — superset of preserved
                + new wikilinks plus any additional concepts the LLM
                identifies. Used to populate the ``related:`` frontmatter.
            practical_implications: Optional list of practical applications
                (mirrors V4's field). May be empty.
            key_distinctions: Optional list of distinctions to preserve.
            key_figures: Optional list of named figures.
            tensions_or_questions: Optional list of open questions.
        """
        merged_definition: str = Field(min_length=20, max_length=600)
        merged_explanation: list[str] = Field(default_factory=list)
        preserved_sections: list[str] = Field(default_factory=list)
        new_content_summary: list[str] = Field(default_factory=list)
        preserved_wikilinks: list[str] = Field(default_factory=list)
        new_wikilinks: list[str] = Field(default_factory=list)
        change_summary: str = Field(default="", max_length=500)
        status_recommendation: str = Field(default="keep")
        tensions_introduced: list[str] = Field(default_factory=list)
        related_concepts: list[str] = Field(default_factory=list)
        practical_implications: list[str] = Field(default_factory=list)
        key_distinctions: list[str] = Field(default_factory=list)
        key_figures: list[str] = Field(default_factory=list)
        tensions_or_questions: list[str] = Field(default_factory=list)

        @field_validator(
            "merged_explanation", "preserved_sections", "new_content_summary",
            "preserved_wikilinks", "new_wikilinks", "tensions_introduced",
            "related_concepts", "practical_implications", "key_distinctions",
            "key_figures", "tensions_or_questions",
            mode="before",
        )
        @classmethod
        def _coerce_to_list(cls, v: Any) -> list[str]:
            if v is None:
                return []
            if isinstance(v, str):
                return [v] if v.strip() else []
            if isinstance(v, list):
                return [str(x).strip() for x in v if str(x).strip()]
            return []

        @field_validator("status_recommendation", mode="before")
        @classmethod
        def _normalize_status_rec(cls, v: Any) -> str:
            if not isinstance(v, str):
                return "keep"
            s = v.strip().lower()
            if s in {"keep", "promote_to_enriched"}:
                return s
            return "keep"

else:  # pragma: no cover - pydantic missing path
    class MergeResponse:  # type: ignore[no-redef]
        """Fallback no-validation MergeResponse when pydantic is missing."""

        def __init__(self, **kw: Any) -> None:
            self.__dict__.update(kw)


# ════════════════════════════════════════════════════════════════════════════
# Prompt builders
# ════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT: str = (
    "You are a meticulous knowledge-base editor reconciling an EXISTING "
    "permanent note with NEW supporting material from a fresh extraction. "
    "Your job is NOT to rewrite the existing note from scratch. Your job is "
    "to PRESERVE its existing wisdom (definitions, distinctions, hand-edits, "
    "wiki-links) and ADD what the new material genuinely contributes. "
    "When the existing note and the new material agree, keep the existing "
    "wording. When they conflict, prefer the existing note and surface the "
    "tension in `tensions_introduced` rather than overwriting silently. "
    "Output STRICT JSON matching the provided schema. No prose outside the "
    "JSON object."
)


USER_PROMPT_TEMPLATE: str = """\
You are merging an existing permanent note with a fresh concept bundle.

# Concept
Title: {title}
Slug: {slug}
Domain: {domain}
Aliases: {aliases}
Match tier: {match_tier} (score={match_score:.3f})

# EXISTING NOTE (full text — preserve its wisdom)
```markdown
{existing_body}
```
{existing_truncated_note}

# NEW MATERIAL — Definition body
{definition_body}

# NEW MATERIAL — Supporting callouts
{support_block}

# Existing note's wikilinks (preserve unless clearly orphaned)
{existing_wikilinks}

# Hard rules
1. NEVER drop a wiki-link target that appears in `existing_wikilinks` unless
   the linked concept is genuinely irrelevant to the merged note.
2. NEVER demote the note's status. (Status promotion is allowed only
   stub/seedling -> enriched.)
3. The merged_definition must be at least as informative as the existing
   definition. If the new material doesn't improve it, keep the existing one.
4. Surface any factual contradictions in `tensions_introduced`. Do NOT
   silently overwrite the existing claim with the new one.
5. `change_summary` must be 2-3 sentences a human can read in 10 seconds.

Return STRICT JSON matching the schema:
{{
  "merged_definition":         "<string, 20-600 chars>",
  "merged_explanation":        ["<paragraph 1>", "<paragraph 2>", ...],
  "preserved_sections":        ["<bullet>", ...],
  "new_content_summary":       ["<bullet>", ...],
  "preserved_wikilinks":       ["<wikilink target>", ...],
  "new_wikilinks":             ["<wikilink target>", ...],
  "change_summary":            "<2-3 sentence diff>",
  "status_recommendation":     "keep" | "promote_to_enriched",
  "tensions_introduced":       ["<conflict description>", ...],
  "related_concepts":          ["<concept>", ...],
  "practical_implications":    ["<application>", ...],
  "key_distinctions":          ["<distinction>", ...],
  "key_figures":               ["<figure>", ...],
  "tensions_or_questions":     ["<open question>", ...]
}}
"""


def build_user_prompt(
    *,
    title: str,
    slug: str,
    domain: str,
    aliases: list[str],
    match_tier: str,
    match_score: float,
    existing_body: str,
    definition_body: str,
    support_block: str,
    existing_wikilinks: list[str],
) -> str:
    """Render the merge user-prompt from its inputs.

    Args:
        title: Cleaned concept title.
        slug: Filename stem of the existing note.
        domain: Primary domain (kebab-case).
        aliases: Existing-note aliases (preserved + new bundle aliases).
        match_tier: Which matcher tier produced the hit.
        match_score: Match score (1.0 for exact tiers; 0..1 for fuzzy).
        existing_body: Full existing-note body (frontmatter optional).
            Truncated at :data:`EXISTING_NOTE_MAX_CHARS`.
        definition_body: New definition callout body.
        support_block: Pre-formatted block of supporting callouts.
        existing_wikilinks: Wiki-link targets parsed from existing body.

    Returns:
        The fully-rendered user prompt string.
    """
    truncated_note = ""
    if len(existing_body) > EXISTING_NOTE_MAX_CHARS:
        existing_body = existing_body[:EXISTING_NOTE_MAX_CHARS]
        truncated_note = (
            f"\n*(Existing note truncated at {EXISTING_NOTE_MAX_CHARS} chars "
            "for prompt budget — preserve everything visible above.)*\n"
        )
    return USER_PROMPT_TEMPLATE.format(
        title=title,
        slug=slug,
        domain=domain or "(none)",
        aliases=", ".join(aliases) if aliases else "(none)",
        match_tier=match_tier,
        match_score=match_score,
        existing_body=existing_body or "(empty existing body)",
        existing_truncated_note=truncated_note,
        definition_body=definition_body
            or "(no body — use only title + supporting callouts)",
        support_block=support_block or "(no additional supporting callouts)",
        existing_wikilinks=", ".join(existing_wikilinks)
            if existing_wikilinks else "(none parsed)",
    )
