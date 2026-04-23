#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merger — Orchestrate one merge of an existing note + new bundle via LLM.

Responsibilities:

1. Load and parse the existing note (frontmatter + body).
2. Enforce protect-status policy (skip if status is protected, unless force).
3. Extract existing wiki-links to feed the merge prompt.
4. Call the LLM with the merge prompt contract.
5. Render the merged note: NEW frontmatter (preserving protected fields like
   ``created``, ``mastery-stage``, ``importance``) + NEW body.
6. Atomic backup (timestamped sibling) → atomic write.

The merger never mutates the existing file in place without a backup.
``--no-backup`` is opt-in and surfaces a warning when used.
"""
from __future__ import annotations

import datetime as dt
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Local lib
from v5lib.merge_prompt import (
    PROMPT_CONTRACT_VERSION,
    SYSTEM_PROMPT,
    MergeResponse,
    build_user_prompt,
)
from v5lib.matcher import MatchResult

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Frontmatter delimiter regex.
_FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.DOTALL)

#: Wiki-link regex for harvesting existing-note wiki-links.
#: Matches ``[[Target]]`` and ``[[Target|Alias]]`` — captures Target only.
_WIKILINK_RE = re.compile(r"\[\[([^\[\]\n|]+?)(?:\|[^\[\]\n]+)?\]\]")

#: Frontmatter fields that must be preserved verbatim from the existing note
#: (the LLM cannot suggest changes to these — they are operator-managed).
_PRESERVED_FM_FIELDS: frozenset[str] = frozenset({
    "created", "mastery-stage", "importance", "review-frequency",
})

#: Status promotion ladder — strict lattice. Demotion is always rejected.
_STATUS_RANK: dict[str, int] = {
    "stub": 0, "seedling": 1, "enriched": 2, "budding": 3, "evergreen": 4,
}


# ════════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ════════════════════════════════════════════════════════════════════════════

class MergeProtectedError(Exception):
    """Raised when the existing note's status is in the protect set."""


class BackupError(Exception):
    """Raised when the pre-merge backup write fails."""


# ════════════════════════════════════════════════════════════════════════════
# Result type
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class MergeOutcome:
    """The result of one :meth:`Merger.merge` call.

    Attributes:
        path: The original note path (unchanged — merge writes back to it).
        ok: True if the merge succeeded (or was a dry-run preview).
        skipped: True if the merge was skipped (protected status, etc.).
        skipped_reason: Human-readable reason if ``skipped``.
        backup_path: Path of the backup file created, or None.
        change_summary: The LLM's change_summary string.
        cached: True if the LLM call hit cache.
        error: Error message if not ok and not skipped.
        rendered: Rendered file content (set when dry-run).
    """
    path: Path
    ok: bool = False
    skipped: bool = False
    skipped_reason: str = ""
    backup_path: Path | None = None
    change_summary: str = ""
    cached: bool = False
    error: str = ""
    rendered: str = ""
    match_tier: str = ""
    match_score: float = 0.0


# ════════════════════════════════════════════════════════════════════════════
# Public helpers (also used by tests)
# ════════════════════════════════════════════════════════════════════════════

def parse_existing(path: Path) -> tuple[dict[str, Any], str]:
    """Read an existing note and return (frontmatter_dict, body_text).

    The frontmatter dict mirrors what
    :func:`output_index._extract_frontmatter` returns — minimal YAML,
    targeting the V4 emission shape.

    Args:
        path: Note path to read.

    Returns:
        Tuple of (frontmatter dict, body text). Body text excludes the
        ``---...---`` block. If no frontmatter is found, returns
        ``({}, full_text)``.
    """
    from v5lib.output_index import _extract_frontmatter
    text = path.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    fm = _extract_frontmatter(text)
    body = m.group(2)
    return fm, body


def harvest_wikilinks(body: str) -> list[str]:
    """Return the de-duplicated, order-preserved list of wiki-link targets in body.

    Args:
        body: Markdown body text.

    Returns:
        List of unique target strings, in order of first appearance.

    Example:
        >>> harvest_wikilinks("See [[Foo]] and [[Bar|alt]] and [[Foo]] again.")
        ['Foo', 'Bar']
    """
    seen: dict[str, None] = {}
    for m in _WIKILINK_RE.finditer(body or ""):
        target = m.group(1).strip()
        if target and target not in seen:
            seen[target] = None
    return list(seen.keys())


def resolve_status(existing_status: str, recommendation: str) -> str:
    """Apply the status-promotion lattice. Demotion is rejected.

    Args:
        existing_status: Current status from existing frontmatter (lowercased).
        recommendation: LLM's status_recommendation
            (``"keep"`` or ``"promote_to_enriched"``).

    Returns:
        The new status to write.

    Behavior:
        - ``recommendation == "keep"`` → existing status (or "enriched" if empty).
        - ``recommendation == "promote_to_enriched"``: promote only if
          existing rank < enriched rank. Otherwise keep existing.
    """
    cur = (existing_status or "").lower().strip() or "enriched"
    if recommendation == "promote_to_enriched":
        cur_rank = _STATUS_RANK.get(cur, 99)
        enriched_rank = _STATUS_RANK["enriched"]
        if cur_rank < enriched_rank:
            return "enriched"
    return cur


# ════════════════════════════════════════════════════════════════════════════
# Backup
# ════════════════════════════════════════════════════════════════════════════

def make_backup(path: Path, *, when: dt.datetime) -> Path:
    """Copy ``path`` to a sibling backup file. Return the backup Path.

    Backup naming: ``<original>.bak.YYYYMMDD-HHMMSS``.

    Raises:
        BackupError: If the read or write fails.
    """
    try:
        content = path.read_bytes()
    except OSError as e:
        raise BackupError(f"read failed for {path}: {e}") from e
    stamp = when.strftime("%Y%m%d-%H%M%S")
    bak = path.with_suffix(path.suffix + f".bak.{stamp}")
    try:
        bak.write_bytes(content)
    except OSError as e:
        raise BackupError(f"backup write failed for {bak}: {e}") from e
    return bak


# ════════════════════════════════════════════════════════════════════════════
# Frontmatter rendering for merged notes
# ════════════════════════════════════════════════════════════════════════════

def _quote(s: str) -> str:
    return s.replace("\\", "\\\\").replace("\"", "\\\"")


def _yaml_block_list(items: list[str], *, wikilink: bool = False) -> str:
    items = [str(x).strip() for x in items if str(x).strip()]
    if not items:
        return "  - \"\""
    out: list[str] = []
    for s in items:
        if wikilink:
            out.append(f"  - \"[[{s}]]\"")
        else:
            out.append(f"  - \"{_quote(s)}\"")
    return "\n".join(out)


def render_merged_frontmatter(
    *,
    title: str,
    aliases: list[str],
    new_status: str,
    existing_fm: dict[str, Any],
    domain: str,
    related: list[str],
    today: dt.date,
    source_reports: list[str],
    change_summary: str,
) -> str:
    """Compose the merged note's frontmatter, preserving operator-managed fields."""
    aliases_clean = list(dict.fromkeys([a for a in aliases if a]))[:8]
    related_clean = list(dict.fromkeys([r for r in related if r]))[:12]
    created = str(existing_fm.get("created") or today.isoformat()).strip().strip("\"'")
    mastery = str(existing_fm.get("mastery-stage") or "budding").strip().strip("\"'")
    importance = str(existing_fm.get("importance") or "medium").strip().strip("\"'")
    review = str(existing_fm.get("review-frequency") or "quarterly").strip().strip("\"'")
    domain_val = (domain or str(existing_fm.get("domain") or "other")).strip()

    lines = [
        "---",
        f"title: \"{_quote(title)}\"",
        "aliases:",
        _yaml_block_list(aliases_clean),
        "type: permanent-note",
        f"status: {new_status}",
        "confidence: high",
        "",
        "tags:",
        _yaml_block_list(["permanent-note", "v5-llm-merged", domain_val or "other"]),
        "",
        f"domain: {domain_val or 'other'}",
        "",
        f"created: {created}",
        f"updated: {today.isoformat()}",
        "",
        "source-type: report-extraction",
        "source-reports:",
        _yaml_block_list(source_reports) if source_reports else "  - \"\"",
        "evidence-quality: high",
        "extraction-method: \"pkb-extractor-v1 -> pipeline-v5-merger\"",
        "",
        "complexity-level: advanced-practitioner",
        "depth-level: condensed",
        "",
        "related:",
        _yaml_block_list(related_clean, wikilink=True) if related_clean else "  - \"[[]]\"",
        "see-also:",
        "  - \"[[]]\"",
        "broader:",
        "  - \"[[]]\"",
        "narrower:",
        "  - \"[[]]\"",
        "",
        f"review-frequency: {review}",
        f"mastery-stage: {mastery}",
        f"importance: {importance}",
        "",
        "provenance:",
        "  pipeline-version: \"v5.0.0\"",
        f"  prompt-contract: \"{PROMPT_CONTRACT_VERSION}\"",
        f"  last-merge: \"{today.isoformat()}\"",
        f"  change-summary: \"{_quote(change_summary[:300])}\"",
        "---",
    ]
    return "\n".join(lines)


def render_merged_body(
    *,
    title: str,
    response: MergeResponse,
    source_reports: list[str],
) -> str:
    """Render the merged markdown body."""
    definition = (getattr(response, "merged_definition", "") or "").strip()
    explanation = list(getattr(response, "merged_explanation", None) or [])
    practical = list(getattr(response, "practical_implications", None) or [])
    distinctions = list(getattr(response, "key_distinctions", None) or [])
    figures = list(getattr(response, "key_figures", None) or [])
    tensions_q = list(getattr(response, "tensions_or_questions", None) or [])
    tensions_intro = list(getattr(response, "tensions_introduced", None) or [])
    related = list(getattr(response, "related_concepts", None) or [])
    new_summary = list(getattr(response, "new_content_summary", None) or [])
    change_summary = (getattr(response, "change_summary", "") or "").strip()

    parts: list[str] = [f"# {title}", ""]

    parts.append(f"> [!definition] **{title}**")
    for line in definition.splitlines() or [""]:
        parts.append(f"> {line}".rstrip())
    parts.append("")

    if explanation:
        parts.append("## Core Explanation")
        parts.append("")
        for para in explanation:
            t = (para or "").strip()
            if t:
                parts.append(t)
                parts.append("")

    if practical:
        parts.append("## Practical Implications")
        parts.append("")
        for i, imp in enumerate(practical, start=1):
            t = (imp or "").strip()
            if t:
                parts.append(f"> [!example] **Application {i}**")
                for line in t.splitlines():
                    parts.append(f"> {line}".rstrip())
                parts.append("")

    if distinctions:
        parts.append("## Key Distinctions")
        parts.append("")
        for d in distinctions:
            t = (d or "").strip()
            if t:
                parts.append("> [!warning] **Distinction**")
                for line in t.splitlines():
                    parts.append(f"> {line}".rstrip())
                parts.append("")

    if figures:
        parts.append("## Key Figures")
        parts.append("")
        for f_ in figures:
            t = (f_ or "").strip()
            if t:
                parts.append(f"- {t}")
        parts.append("")

    if tensions_q:
        parts.append("## Open Threads")
        parts.append("")
        for q in tensions_q:
            t = (q or "").strip()
            if t:
                parts.append("> [!open-question] **Question**")
                for line in t.splitlines():
                    parts.append(f"> {line}".rstrip())
                parts.append("")

    if tensions_intro:
        parts.append("## Tensions Introduced by Merge")
        parts.append("")
        for t_ in tensions_intro:
            t = (t_ or "").strip()
            if t:
                parts.append("> [!tension] **Conflict**")
                for line in t.splitlines():
                    parts.append(f"> {line}".rstrip())
                parts.append("")

    if new_summary or change_summary:
        parts.append("## Merge Notes")
        parts.append("")
        if change_summary:
            parts.append(f"_{change_summary}_")
            parts.append("")
        if new_summary:
            parts.append("**New material added in this merge:**")
            for s in new_summary:
                t = (s or "").strip()
                if t:
                    parts.append(f"- {t}")
            parts.append("")

    parts.append("## Connections & Context")
    parts.append("")
    if related:
        link_str = " · ".join(f"[[{r}]]" for r in related[:12])
        parts.append(f"**Related:** {link_str}")
        parts.append("")
    if source_reports:
        src_str = " · ".join(f"[[{s}]]" for s in source_reports)
        parts.append(f"**Sources:** {src_str}")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


# ════════════════════════════════════════════════════════════════════════════
# Atomic write
# ════════════════════════════════════════════════════════════════════════════

def write_atomic(path: Path, content: str) -> None:
    """Write ``content`` to ``path`` atomically via .tmp + replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


# ════════════════════════════════════════════════════════════════════════════
# Merger
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class Merger:
    """Orchestrate one merge.

    Attributes:
        client: An :class:`OllamaClient` (passed in by pipeline_v5).
        model: Model identifier for the merge call.
        protect_statuses: Statuses that block merging unless ``force``.
        force: Override ``protect_statuses``.
        backup: When True, write a ``.bak.<timestamp>`` sibling before
            overwriting the original.
        bypass_cache: Force a live LLM call.
    """
    client: Any  # OllamaClient — typed Any to avoid hard import in lib
    model: str
    protect_statuses: frozenset[str] = field(
        default_factory=lambda: frozenset({"evergreen", "budding"})
    )
    force: bool = False
    backup: bool = True
    bypass_cache: bool = False

    def merge(
        self,
        *,
        bundle: Any,             # ConceptBundle from pipeline_v4
        match: MatchResult,
        today: dt.date,
        dry_run: bool = False,
    ) -> MergeOutcome:
        """Merge one bundle into one existing note.

        Args:
            bundle: V4 :class:`ConceptBundle` carrying new material.
            match: The :class:`MatchResult` produced by :class:`Matcher`.
            today: Date stamp for the merged note's ``updated`` field.
            dry_run: When True, render the merged note but do not write
                or back up. The rendered content is returned in
                :attr:`MergeOutcome.rendered`.

        Returns:
            :class:`MergeOutcome` describing the operation.
        """
        path = match.path
        outcome = MergeOutcome(
            path=path, match_tier=match.tier, match_score=match.score,
        )

        # ── 1. Load existing ────────────────────────────────────────────
        try:
            existing_fm, existing_body = parse_existing(path)
        except OSError as e:
            outcome.error = f"read failed: {e}"
            return outcome

        existing_status = str(existing_fm.get("status") or "").strip().strip("\"'").lower()

        # ── 2. Protect-status gate ──────────────────────────────────────
        if existing_status in self.protect_statuses and not self.force:
            outcome.ok = True
            outcome.skipped = True
            outcome.skipped_reason = (
                f"protected status '{existing_status}' (use --force-merge to override)"
            )
            return outcome

        # ── 3. Harvest existing wiki-links + aliases ───────────────────
        existing_links = harvest_wikilinks(existing_body)
        existing_aliases_raw = existing_fm.get("aliases", []) or []
        if isinstance(existing_aliases_raw, list):
            existing_aliases = [str(a).strip().strip("\"'")
                                for a in existing_aliases_raw if str(a).strip()]
        else:
            existing_aliases = []
        # Combine: existing aliases first, then bundle aliases
        bundle_aliases = list(getattr(bundle, "aliases", ()) or ())
        merged_aliases_in: list[str] = []
        seen = set()
        for a in [bundle.title, *existing_aliases, *bundle_aliases]:
            key = a.lower()
            if a and key not in seen:
                seen.add(key)
                merged_aliases_in.append(a)

        # ── 4. Build prompt + call LLM ─────────────────────────────────
        support_lines = []
        for sc in (getattr(bundle, "support", ()) or ()):
            head = f"- [{sc.type}] {sc.title}".strip()
            body = sc.body.replace("\n", " ").strip() if sc.body else ""
            if body:
                head += f": {body}"
            support_lines.append(head)
        support_block = "\n".join(support_lines) if support_lines else ""

        user_prompt = build_user_prompt(
            title=bundle.title,
            slug=bundle.filename_stem,
            domain=getattr(bundle, "domain", "") or "",
            aliases=merged_aliases_in,
            match_tier=match.tier,
            match_score=match.score,
            existing_body=existing_body,
            definition_body=getattr(bundle, "definition_body", "") or "",
            support_block=support_block,
            existing_wikilinks=existing_links,
        )

        try:
            rsp = self.client.chat_json(
                system=SYSTEM_PROMPT,
                user=user_prompt,
                schema=MergeResponse if MergeResponse is not object else None,
                model=self.model,
                cache_key_inputs=(
                    PROMPT_CONTRACT_VERSION,
                    self.model,
                    bundle.title.lower(),
                    bundle.report_stem,
                    str(path.name),
                    (existing_body or "")[:400],
                    (bundle.definition_body or "")[:300],
                ),
                bypass_cache=self.bypass_cache,
            )
        except Exception as e:  # noqa: BLE001 — surface LLM errors
            outcome.error = f"{type(e).__name__}: {e}"
            return outcome

        outcome.cached = bool(getattr(rsp, "cached", False))
        response = rsp.parsed
        outcome.change_summary = str(getattr(response, "change_summary", "") or "")

        # ── 5. Status promotion ────────────────────────────────────────
        rec = str(getattr(response, "status_recommendation", "keep") or "keep")
        new_status = resolve_status(existing_status, rec)

        # ── 6. Compute combined related links ──────────────────────────
        preserved = list(getattr(response, "preserved_wikilinks", None) or [])
        new_wl = list(getattr(response, "new_wikilinks", None) or [])
        related_concepts = list(getattr(response, "related_concepts", None) or [])
        combined_related: list[str] = []
        seen_r: set[str] = set()
        for r in [*preserved, *new_wl, *related_concepts, *existing_links]:
            r_clean = (r or "").strip().strip("[]")
            if r_clean and r_clean.lower() not in seen_r:
                seen_r.add(r_clean.lower())
                combined_related.append(r_clean)

        # ── 7. Source-reports merging ──────────────────────────────────
        existing_sources_raw = existing_fm.get("source-reports", []) or []
        if isinstance(existing_sources_raw, list):
            existing_sources = [str(s).strip().strip("\"'")
                                for s in existing_sources_raw if str(s).strip()]
        else:
            existing_sources = []
        bundle_source = getattr(bundle, "report_stem", "") or ""
        merged_sources: list[str] = []
        seen_s: set[str] = set()
        for s in [*existing_sources, bundle_source]:
            if s and s.lower() not in seen_s:
                seen_s.add(s.lower())
                merged_sources.append(s)

        # ── 8. Render merged note ──────────────────────────────────────
        fm = render_merged_frontmatter(
            title=bundle.title,
            aliases=merged_aliases_in,
            new_status=new_status,
            existing_fm=existing_fm,
            domain=getattr(bundle, "domain", "") or "",
            related=combined_related,
            today=today,
            source_reports=merged_sources,
            change_summary=outcome.change_summary,
        )
        body = render_merged_body(
            title=bundle.title,
            response=response,
            source_reports=merged_sources,
        )
        rendered = f"{fm}\n\n{body}"
        outcome.rendered = rendered

        if dry_run:
            outcome.ok = True
            outcome.skipped_reason = "dry-run"
            return outcome

        # ── 9. Backup + write ──────────────────────────────────────────
        if self.backup:
            try:
                outcome.backup_path = make_backup(
                    path, when=dt.datetime.now(),
                )
            except BackupError as e:
                outcome.error = f"BackupError: {e}"
                return outcome
        try:
            write_atomic(path, rendered)
        except OSError as e:
            outcome.error = f"OSError on write: {e}"
            return outcome

        outcome.ok = True
        return outcome
