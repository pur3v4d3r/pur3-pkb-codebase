#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""enrich_stubs.py — Enrich permanent note stubs via local Ollama LLM.

Scans stub notes (status: stub or empty-body seedlings), calls Qwen2.5-7B
to generate a definition, core explanation, practical implications, and
related concepts, then writes enriched notes atomically back to disk.

Primary output: fills the [!definition] callout (mandatory).
Secondary output: Core Explanation, Practical Implications, Key Figures,
Open Threads, and Connections sections.

Usage:
    python enrich_stubs.py --dry-run --limit 3
    python enrich_stubs.py --limit 20 --output-dir D:/enrichment-preview
    python enrich_stubs.py --limit 50
    python enrich_stubs.py --strict

Exit codes:
    0   success
    1   uncaught error
    2   bad arguments / missing input dir
    4   no stubs found
    5   one or more enrichments failed (only with --strict)
    6   Ollama unreachable
    130 interrupted (SIGINT)

Version: 1.0.0
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ── sys.path injection ──────────────────────────────────────────────────────
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_v3  # noqa: E402
from lib.llm_client import (  # noqa: E402
    LLMError,
    OllamaClient,
    OllamaUnavailableError,
    StructuredOutputError,
)
from lib.frontmatter import parse_frontmatter, render_frontmatter  # noqa: E402
from lib.markdown import callout, join_wikilinks, safe_filename  # noqa: E402

logger = logging.getLogger(__name__)

__version__ = "1.0.0"


# ════════════════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════════════════

#: Bump this string when either prompt changes semantically. Invalidates cache.
PROMPT_CONTRACT_VERSION: str = "enrich-v1"

#: Body length threshold below which we consider the note effectively empty.
EMPTY_BODY_THRESHOLD: int = 80

#: Default directories to scan when --input-dir is not specified.
DEFAULT_SEARCH_DIRS: list[Path] = [
    config_v3.VAULT_ROOT / "999-report-organizing" / "_permanent-notes" / "v3-pipeline-permanent-notes",
    config_v3.VAULT_ROOT / "03-notes" / "01_permanent-notes",
]

#: Statuses that mean the note is already enriched — skip it.
ENRICHED_STATUSES: frozenset[str] = frozenset({"enriched", "budding", "evergreen"})

#: Regex that matches the v3 pipeline [!info] Stub placeholder callout.
_PLACEHOLDER_INFO_RE = re.compile(
    r">\s*\[!info\]\s*Stub.*?(?=\n(?!>)|\Z)", re.DOTALL | re.IGNORECASE
)

#: Regex that matches the v3 stub [!definition] placeholder body pattern.
_PLACEHOLDER_DEF_RE = re.compile(
    r">\s*\*Stub note\s*[—-]", re.IGNORECASE
)

SYSTEM_PROMPT: str = (
    "You are a knowledgeable academic knowledge base author. Your task is to "
    "enrich a stub note from a Personal Knowledge Base (PKB) by writing "
    "accurate, concise content about a concept. Write in a neutral, scholarly "
    "tone. Do not hallucinate citations, events, or biographical claims — if "
    "you are uncertain about a claim, omit it rather than guess. Reply with "
    "valid JSON only — no markdown code fences, no preamble."
)

USER_PROMPT_TEMPLATE: str = """\
Enriching stub note for concept: {title!r}

Domain: {domain}
Type: {note_type}
Aliases: {aliases}
Existing wiki-links: {existing_links}

{context_block}

Return a JSON object with EXACTLY these fields:
{{
  "definition": "1-2 sentence plain-English definition of {title!r}. \
This field is REQUIRED — never leave it empty or null.",

  "core_explanation": [
    "Paragraph 1: foundational context and core mechanism.",
    "Paragraph 2: how it works or is applied in practice.",
    "Paragraph 3: key nuances, sub-variants, or theoretical roots.",
    "(Optional paragraph 4: historical development or origin.)",
    "(Optional paragraph 5: relationship to neighboring concepts.)"
  ],

  "practical_implications": [
    "Implication 1: concrete application or real-world consequence.",
    "Implication 2: a second distinct application.",
    "(Optional implication 3: a cautionary note or known limitation.)"
  ],

  "key_figures": [
    "Person Name — role or contribution (only if well-attested; \
leave empty array if none or uncertain)"
  ],

  "related_concepts": [
    "Concept Name A",
    "Concept Name B",
    "Concept Name C"
  ],

  "tensions_or_questions": [
    "(Optional) An open debate, unresolved tension, or key open question."
  ],

  "domain": "(Optional) Corrected kebab-case domain if {domain!r} is \
wrong or too generic — e.g. 'cognitive-psychology'. Null if current is correct."
}}

Rules:
- ALL seven field keys MUST be present in your JSON response.
- "definition" MUST NOT be empty or null. This is the most important field.
- Array fields may contain empty arrays [] but must exist as JSON arrays.
- "related_concepts" should be concept names only (not sentences).
- Do NOT include {title!r} itself in "related_concepts".
- Do NOT invent citations or unverified historical claims.
- Respond with a single JSON object only. No markdown fences.
"""


# ════════════════════════════════════════════════════════════════════════════
# Pydantic schema (optional — graceful fallback if pydantic unavailable)
# ════════════════════════════════════════════════════════════════════════════

try:
    from pydantic import BaseModel, Field, field_validator  # noqa: E402

    class EnrichmentResponse(BaseModel):
        definition: str = Field(description="1-2 sentence definition. Required.", min_length=1)
        core_explanation: list[str] = Field(default_factory=list)
        practical_implications: list[str] = Field(default_factory=list)
        key_figures: list[str] = Field(default_factory=list)
        related_concepts: list[str] = Field(default_factory=list)
        tensions_or_questions: list[str] = Field(default_factory=list)
        domain: str | None = Field(default=None)

        @field_validator("definition")
        @classmethod
        def definition_not_empty(cls, v: str) -> str:
            stripped = v.strip()
            if not stripped:
                raise ValueError("definition must not be empty")
            return stripped

        @field_validator(
            "core_explanation", "practical_implications",
            "key_figures", "related_concepts", "tensions_or_questions",
            mode="before",
        )
        @classmethod
        def coerce_list(cls, v: Any) -> list[Any]:
            if v is None:
                return []
            if isinstance(v, str):
                return [v] if v.strip() else []
            return v if isinstance(v, list) else []

    _PYDANTIC_AVAILABLE = True

except ImportError:
    EnrichmentResponse = None  # type: ignore[assignment,misc]
    _PYDANTIC_AVAILABLE = False
    logger.warning("pydantic not available — schema validation disabled")


# ════════════════════════════════════════════════════════════════════════════
# Data models
# ════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class StubNote:
    """Parsed stub file ready for enrichment."""

    path: Path
    title: str
    domain: str
    note_type: str
    status: str
    maturity: str
    aliases: list[str]
    source_reports: list[str]
    referenced_by: list[str]
    body_text: str
    raw_frontmatter: dict[str, Any]

    @property
    def file_hash(self) -> str:
        """Stable SHA-1 key: title + domain + first 200 chars of body."""
        payload = f"{self.title}\x00{self.domain}\x00{self.body_text[:200]}"
        return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


@dataclass(frozen=True)
class EnrichmentResult:
    """Outcome of enriching a single stub."""

    stub: StubNote
    ok: bool
    cached: bool
    response: Any  # EnrichmentResponse | dict | None
    error: str = ""


# ════════════════════════════════════════════════════════════════════════════
# Stub detection helpers
# ════════════════════════════════════════════════════════════════════════════

def _strip_boilerplate(body: str) -> str:
    """Remove placeholder callouts and whitespace; return residual body."""
    cleaned = _PLACEHOLDER_INFO_RE.sub("", body)
    # Also strip the v3 auto-generated stub notice line
    cleaned = re.sub(r"\*Auto-generated stub[^*\n]*\*", "", cleaned, flags=re.IGNORECASE)
    # Strip the ## Referenced By section (not meaningful content)
    cleaned = re.sub(r"## Referenced By\s*\n(?:- \[\[.*?\]\]\s*\n)*", "", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def _has_placeholder_definition(body: str) -> bool:
    """Return True if the [!definition] callout contains only stub placeholder text."""
    return bool(_PLACEHOLDER_DEF_RE.search(body))


def is_stub(fm: dict[str, Any], body: str) -> bool:
    """Return True if the note qualifies as a stub needing enrichment."""
    status = str(fm.get("status", "")).lower()
    maturity = str(fm.get("maturity", "")).lower()
    mastery = str(fm.get("mastery-stage", "")).lower()
    tags = [str(t).lower() for t in (fm.get("tags") or [])]

    # Explicit stub status (v2 template stubs)
    if status == "stub":
        return True

    # v3 pipeline stubs: status=seedling + concept-stub tag (or placeholder definition)
    if status == "seedling" or mastery == "seedling":
        if "concept-stub" in tags:
            return True
        if _has_placeholder_definition(body):
            return True
        if len(_strip_boilerplate(body)) < EMPTY_BODY_THRESHOLD:
            return True

    # Older-style: maturity=seedling, active status, body has no real H2 sections
    if maturity == "seedling" and status in ("active", "stub", "seedling", ""):
        residual = _strip_boilerplate(body)
        has_h2 = bool(re.search(r"^##\s+\S", body, re.MULTILINE))
        has_real_definition = "!definition" in body.lower() and not _has_placeholder_definition(body)
        if not has_h2 and not has_real_definition and len(residual) < EMPTY_BODY_THRESHOLD:
            return True

    return False


def _already_enriched(fm: dict[str, Any]) -> bool:
    """Return True if the note has already been enriched — skip it."""
    status = str(fm.get("status", "")).lower()
    return status in ENRICHED_STATUSES


# ════════════════════════════════════════════════════════════════════════════
# Stub parsing
# ════════════════════════════════════════════════════════════════════════════

def _extract_source_reports(fm: dict[str, Any]) -> list[str]:
    """Pull source report names from various frontmatter locations."""
    reports: list[str] = []

    # v3 format: provenance.source-reports
    prov = fm.get("provenance") or {}
    if isinstance(prov, dict):
        for r in prov.get("source-reports", []) or []:
            s = str(r).strip().strip("[]").strip()
            if s:
                reports.append(s)

    # Older format: source field
    src = fm.get("source", "")
    if src and isinstance(src, str) and src.strip():
        s = src.strip()
        if s not in reports:
            reports.append(s)

    return reports[:10]


def _extract_referenced_by(fm: dict[str, Any], body: str) -> list[str]:
    """Pull existing wiki-link targets from frontmatter relationship fields."""
    seen: set[str] = set()
    out: list[str] = []

    def _add(raw: Any) -> None:
        for item in (raw if isinstance(raw, list) else [raw]):
            s = str(item).strip()
            # Strip [[...]] wrapper
            s = re.sub(r"^\[\[|\]\]$", "", s).split("|")[0].strip()
            if s and s.lower() not in seen:
                seen.add(s.lower())
                out.append(s)

    # Frontmatter relationship fields
    for key in ("link-related", "link-up", "see-also"):
        _add(fm.get(key) or [])

    rels = fm.get("relationships") or {}
    if isinstance(rels, dict):
        for key in ("related", "see-also", "builds-on", "enables"):
            _add(rels.get(key) or [])

    # Body [[wiki-links]] — only grab the first 10 to avoid noise
    for match in re.finditer(r"\[\[([^\]|#]+)", body):
        target = match.group(1).strip()
        if target and target.lower() not in seen:
            seen.add(target.lower())
            out.append(target)
        if len(out) >= 10:
            break

    return out[:10]


def _try_parse_stub(path: Path) -> StubNote | None:
    """Parse one Markdown file into a StubNote, or return None."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    fm, body = parse_frontmatter(text)
    if not fm:
        return None
    if _already_enriched(fm):
        return None
    if not is_stub(fm, body):
        return None

    # Fall back to filename stem when title field is absent or empty
    raw_title = str(fm.get("title", "")).strip().strip('"').strip()
    title = raw_title if raw_title else path.stem

    subdomains = fm.get("subdomains") or []
    first_subdomain = subdomains[0] if isinstance(subdomains, list) and subdomains else ""
    domain = str(fm.get("domain", first_subdomain) or "").strip()
    if not domain or domain in ("[]", "uncategorized", ""):
        domain = "uncategorized"

    return StubNote(
        path=path,
        title=title,
        domain=domain,
        note_type=str(fm.get("type", "permanent-note")),
        status=str(fm.get("status", "")),
        maturity=str(fm.get("maturity", fm.get("mastery-stage", ""))),
        aliases=[str(a) for a in (fm.get("aliases") or []) if str(a).strip()],
        source_reports=_extract_source_reports(fm),
        referenced_by=_extract_referenced_by(fm, body),
        body_text=body,
        raw_frontmatter=fm,
    )


# ════════════════════════════════════════════════════════════════════════════
# Scanning
# ════════════════════════════════════════════════════════════════════════════

def scan_stubs(
    search_dirs: list[Path],
    *,
    skip_enriched: bool = True,
    limit: int = 0,
) -> list[StubNote]:
    """Recursively scan directories and return qualifying stub notes."""
    found: list[StubNote] = []
    seen_paths: set[Path] = set()

    for search_dir in search_dirs:
        if not search_dir.is_dir():
            logger.warning("Search dir not found, skipping: %s", search_dir)
            continue
        for md_path in sorted(search_dir.rglob("*.md")):
            if md_path in seen_paths:
                continue
            seen_paths.add(md_path)
            stub = _try_parse_stub(md_path)
            if stub is None:
                continue
            found.append(stub)
            if limit and len(found) >= limit:
                break
        if limit and len(found) >= limit:
            break

    logger.info("Found %d stub(s) to enrich", len(found))
    return found


# ════════════════════════════════════════════════════════════════════════════
# Prompt construction
# ════════════════════════════════════════════════════════════════════════════

def _build_context_block(stub: StubNote) -> str:
    """Build the optional context section injected into the user prompt."""
    parts: list[str] = []

    if stub.referenced_by:
        refs = stub.referenced_by[:8]
        parts.append(
            "This concept is referenced by these existing notes in the PKB:\n"
            + "\n".join(f"  - {r}" for r in refs)
        )

    residual_body = _strip_boilerplate(stub.body_text)
    if len(residual_body) > 30:
        excerpt = residual_body[:600]
        if len(residual_body) > 600:
            excerpt += "…"
        parts.append(f"Existing body text (partial):\n{excerpt}")

    if stub.source_reports:
        parts.append(
            "Source reports that mention this concept:\n"
            + "\n".join(f"  - {r}" for r in stub.source_reports)
        )

    return "\n\n".join(parts) if parts else "(No additional context available.)"


def _build_user_prompt(stub: StubNote) -> str:
    """Render the enrichment user prompt for one stub."""
    aliases_str = ", ".join(stub.aliases) if stub.aliases else "(none)"
    links_str = ", ".join(stub.referenced_by[:5]) if stub.referenced_by else "(none)"
    context_block = _build_context_block(stub)

    return USER_PROMPT_TEMPLATE.format(
        title=stub.title,
        domain=stub.domain,
        note_type=stub.note_type,
        aliases=aliases_str,
        existing_links=links_str,
        context_block=context_block,
    )


# ════════════════════════════════════════════════════════════════════════════
# LLM call
# ════════════════════════════════════════════════════════════════════════════

def enrich_stub(
    stub: StubNote,
    client: OllamaClient,
    *,
    model: str | None = None,
    bypass_cache: bool = False,
) -> EnrichmentResult:
    """Call the LLM for one stub. Non-fatal on failure."""
    user_prompt = _build_user_prompt(stub)
    cache_key = (PROMPT_CONTRACT_VERSION, model or client.model, stub.title, stub.file_hash)

    schema = EnrichmentResponse if _PYDANTIC_AVAILABLE else None

    try:
        rsp = client.chat_json(
            system=SYSTEM_PROMPT,
            user=user_prompt,
            schema=schema,
            cache_key_inputs=cache_key,
            model=model,
            bypass_cache=bypass_cache,
            num_ctx=12288,
        )
    except StructuredOutputError as e:
        logger.warning("Schema validation failed for %r: %s", stub.title, e)
        return EnrichmentResult(stub=stub, ok=False, cached=False, response=None, error=str(e))
    except OllamaUnavailableError as e:
        logger.warning("Ollama unavailable for %r: %s", stub.title, e)
        return EnrichmentResult(stub=stub, ok=False, cached=False, response=None, error=str(e))
    except LLMError as e:
        logger.warning("LLM error for %r: %s", stub.title, e)
        return EnrichmentResult(stub=stub, ok=False, cached=False, response=None, error=str(e))

    response = rsp.parsed
    if response is None:
        return EnrichmentResult(stub=stub, ok=False, cached=rsp.cached, response=None,
                                error="parsed response was None")

    # When pydantic is unavailable, validate the definition manually.
    if not _PYDANTIC_AVAILABLE:
        if not isinstance(response, dict) or not str(response.get("definition", "")).strip():
            return EnrichmentResult(stub=stub, ok=False, cached=rsp.cached, response=None,
                                    error="definition field missing or empty in raw dict response")

    return EnrichmentResult(stub=stub, ok=True, cached=rsp.cached, response=response)


# ════════════════════════════════════════════════════════════════════════════
# Markdown body assembly
# ════════════════════════════════════════════════════════════════════════════

def _get(response: Any, field: str, default: Any = None) -> Any:
    """Get a field from either a pydantic model instance or a plain dict."""
    if _PYDANTIC_AVAILABLE and isinstance(response, EnrichmentResponse):
        return getattr(response, field, default)
    if isinstance(response, dict):
        return response.get(field, default)
    return default


def build_enriched_body(stub: StubNote, response: Any) -> str:
    """Assemble the full enriched note body from an enrichment response."""
    definition = str(_get(response, "definition", "")).strip()
    core_explanation: list[str] = list(_get(response, "core_explanation") or [])
    practical_implications: list[str] = list(_get(response, "practical_implications") or [])
    key_figures: list[str] = list(_get(response, "key_figures") or [])
    related_concepts: list[str] = list(_get(response, "related_concepts") or [])
    tensions: list[str] = list(_get(response, "tensions_or_questions") or [])

    lines: list[str] = []

    # ── Title ──────────────────────────────────────────────────────────────
    lines.append(f"# {stub.title}")
    lines.append("")

    # ── Definition callout (MANDATORY) ────────────────────────────────────
    def_body = (
        f"- **Key-Term**: [[{stub.title}]]\n"
        f"- **Definition**: {definition}\n"
        f"- **Domain**: {stub.domain}\n"
        f"- **Status**: \U0001f331 budding | Confidence: speculative"
    )
    lines.append(callout("definition", stub.title, def_body))
    lines.append("")

    # ── Core Explanation ──────────────────────────────────────────────────
    if core_explanation:
        lines.append("## Core Explanation")
        lines.append("")
        for i, para in enumerate(core_explanation[:5]):
            para = para.strip()
            if not para:
                continue
            title_str = "Core Explanation" if i == 0 else f"Explanation {i + 1}"
            lines.append(callout("analytical-insight", title_str, para))
            lines.append("")

    # ── Practical Implications ────────────────────────────────────────────
    if practical_implications:
        lines.append("## Practical Implications")
        lines.append("")
        for impl in practical_implications[:4]:
            impl = impl.strip()
            if not impl:
                continue
            lines.append(callout("example", "Application", impl))
            lines.append("")

    # ── Key Figures ───────────────────────────────────────────────────────
    if key_figures:
        lines.append("## Key Figures")
        lines.append("")
        for person in key_figures[:5]:
            person = person.strip()
            if not person:
                continue
            # Split "Name — role" if present
            parts = re.split(r"\s*[—–-]\s*", person, maxsplit=1)
            person_name = safe_filename(parts[0].strip())
            person_body = parts[1].strip() if len(parts) > 1 else ""
            lines.append(callout("person", person_name, person_body))
            lines.append("")

    # ── Open Threads ──────────────────────────────────────────────────────
    if tensions:
        lines.append("## Open Threads")
        lines.append("")
        for t in tensions[:3]:
            t = t.strip()
            if not t:
                continue
            lines.append(callout("open-question", "Question", t))
            lines.append("")

    # ── Connections ───────────────────────────────────────────────────────
    lines.append("## Connections")
    lines.append("")

    if related_concepts:
        safe_links = [safe_filename(c) for c in related_concepts[:8] if c.strip()]
        if safe_links:
            lines.append(f"**Related:** {join_wikilinks(safe_links)}")
            lines.append("")

    # Preserve existing link-related / see-also from the stub frontmatter
    existing_rels = (
        list(stub.raw_frontmatter.get("link-related") or [])
        + list(stub.raw_frontmatter.get("see-also") or [])
    )
    existing_rels = [str(r).strip() for r in existing_rels if str(r).strip()]
    if existing_rels:
        lines.append("**See Also (existing):**")
        for lnk in existing_rels[:8]:
            lines.append(f"- {lnk}")
        lines.append("")

    # Dataview backlinks query
    stem = safe_filename(stub.title)
    lines.append("```dataview")
    lines.append(f"LIST FROM [[{stem}]]")
    lines.append("WHERE file.path != this.file.path")
    lines.append("SORT file.mtime DESC")
    lines.append("LIMIT 10")
    lines.append("```")
    lines.append("")

    # ── Sources footer ────────────────────────────────────────────────────
    lines.append("---")
    lines.append("")
    if stub.source_reports:
        lines.append(f"**Sources:** {join_wikilinks(stub.source_reports)}")
    else:
        lines.append("**Sources:** *(auto-enriched from domain knowledge)*")

    return "\n".join(lines)


# ════════════════════════════════════════════════════════════════════════════
# Frontmatter update
# ════════════════════════════════════════════════════════════════════════════

def update_frontmatter(fm: dict[str, Any], response: Any) -> dict[str, Any]:
    """Return an updated frontmatter dict. Preserves all unrelated fields."""
    updated = dict(fm)

    # Status promotion
    current_status = str(updated.get("status", "")).lower()
    if current_status in ("stub", "seedling", "active", ""):
        updated["status"] = "enriched"

    # Maturity promotion
    current_maturity = str(updated.get("maturity", "")).lower()
    if current_maturity in ("seedling", ""):
        updated["maturity"] = "budding"

    # mastery-stage (v3 format)
    current_mastery = str(updated.get("mastery-stage", "")).lower()
    if current_mastery in ("seedling", ""):
        updated["mastery-stage"] = "budding"

    # Domain correction — only if LLM provides one and current is a placeholder
    corrected_domain = str(_get(response, "domain") or "").strip()
    if corrected_domain and str(updated.get("domain", "")).lower() in (
        "other", "uncategorized", "unknown", ""
    ):
        updated["domain"] = corrected_domain

    # Timestamps
    updated["updated"] = dt.date.today().isoformat()

    # Provenance
    prov = dict(updated.get("provenance") or {})
    prov["enrichment-method"] = "enrich_stubs-v1"
    prov["enrichment-model"] = config_v3.LLM_MODEL_SYNTHESIZE
    updated["provenance"] = prov

    return updated


# ════════════════════════════════════════════════════════════════════════════
# File I/O
# ════════════════════════════════════════════════════════════════════════════

def write_note_atomic(path: Path, content: str) -> None:
    """Write content to path atomically via a .tmp sibling."""
    tmp = path.with_suffix(".md.tmp")
    try:
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(path)
    except OSError:
        tmp.unlink(missing_ok=True)
        raise


def _output_path_for(stub: StubNote, search_roots: list[Path], output_dir: Path) -> Path:
    """Compute mirrored output path preserving relative directory structure."""
    for root in search_roots:
        try:
            rel = stub.path.relative_to(root)
            dest = output_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            return dest
        except ValueError:
            continue
    # Fallback: flat output dir
    dest = output_dir / stub.path.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    return dest


def _write_enriched_note(
    result: EnrichmentResult,
    output_dir: Path | None,
    search_roots: list[Path],
) -> None:
    """Assemble and write the enriched note to disk."""
    body = build_enriched_body(result.stub, result.response)
    fm = update_frontmatter(result.stub.raw_frontmatter, result.response)
    content = render_frontmatter(fm) + "\n" + body

    if output_dir is not None:
        dest = _output_path_for(result.stub, search_roots, output_dir)
    else:
        dest = result.stub.path

    write_note_atomic(dest, content)
    logger.debug("Wrote enriched note: %s", dest)


# ════════════════════════════════════════════════════════════════════════════
# Main processing loop
# ════════════════════════════════════════════════════════════════════════════

def enrich_all(
    stubs: list[StubNote],
    client: OllamaClient,
    *,
    model: str | None = None,
    bypass_cache: bool = False,
    dry_run: bool = False,
    output_dir: Path | None = None,
    search_roots: list[Path] | None = None,
) -> tuple[list[EnrichmentResult], dict[str, Any]]:
    """Sequentially enrich all stubs. Returns (results, stats_dict)."""
    import time as _time

    results: list[EnrichmentResult] = []
    n_ok = n_cached = n_written = n_failed = n_skipped = 0
    roots = search_roots or DEFAULT_SEARCH_DIRS
    total = len(stubs)
    t_start = _time.monotonic()

    def _p(msg: str) -> None:
        # ASCII-safe print — avoids Windows cp1252 encoding failures.
        print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)

    def _progress_bar(i: int) -> None:
        elapsed = _time.monotonic() - t_start
        pct = int(100 * i / total) if total else 0
        filled = pct // 5
        bar = "[" + "#" * filled + "-" * (20 - filled) + "]"
        _p(f"  {bar} {i}/{total} ({pct}%)  ok={n_ok} cached={n_cached} "
           f"written={n_written} failed={n_failed}  {elapsed:.0f}s elapsed")

    for i, stub in enumerate(stubs):
        _p(f"[{i+1}/{total}] {stub.title[:60]}")

        result = enrich_stub(stub, client, model=model, bypass_cache=bypass_cache)
        results.append(result)

        if result.ok:
            n_ok += 1
            if result.cached:
                n_cached += 1

            if dry_run and n_ok == 1:
                preview = build_enriched_body(result.stub, result.response)
                _p("\n--- DRY-RUN PREVIEW (first successful stub) ---")
                _p(preview[:2500])
                _p("--- END PREVIEW ---\n")

            if not dry_run:
                try:
                    _write_enriched_note(result, output_dir, roots)
                    n_written += 1
                except OSError as e:
                    logger.error("Write failed for %r: %s", stub.title, e)
                    n_failed += 1
            else:
                n_skipped += 1
        else:
            n_failed += 1
            _p(f"  FAILED: {result.error[:120]}")

        if (i + 1) % 10 == 0 or i + 1 == total:
            _progress_bar(i + 1)

    stats: dict[str, Any] = {
        "total": len(stubs),
        "ok": n_ok,
        "cached": n_cached,
        "written": n_written,
        "failed": n_failed,
        "skipped_dry_run": n_skipped,
        "model": model or client.model,
        "prompt_contract_version": PROMPT_CONTRACT_VERSION,
    }
    return results, stats


# ════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enrich_stubs",
        description="Enrich permanent note stubs via local Ollama LLM.",
        epilog=(
            "Examples:\n"
            "  python enrich_stubs.py --dry-run --limit 3\n"
            "  python enrich_stubs.py --limit 20 --output-dir D:/enrichment-preview\n"
            "  python enrich_stubs.py --limit 50\n"
            "  python enrich_stubs.py --strict\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        action="append",
        dest="input_dirs",
        metavar="PATH",
        help=(
            "Directory to scan for stubs (repeatable). "
            "Default: v3 pipeline dir + 03-notes/01_permanent-notes."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        metavar="PATH",
        help=(
            "Write enriched notes here instead of in-place. "
            "Mirrors input directory structure for easy diff."
        ),
    )
    parser.add_argument(
        "-n", "--dry-run",
        action="store_true",
        help="Run LLM calls (cached) but write no files. Prints a preview of the first stub.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        metavar="N",
        help="Process only the first N stubs (0 = no limit).",
    )
    parser.add_argument(
        "--bypass-cache",
        action="store_true",
        help="Force live LLM calls, ignoring cached responses.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=config_v3.LLM_MODEL_SYNTHESIZE,
        help=f"Ollama model ID (default: {config_v3.LLM_MODEL_SYNTHESIZE}).",
    )
    parser.add_argument(
        "--ollama-url",
        type=str,
        default=config_v3.OLLAMA_URL,
        metavar="URL",
        help=f"Ollama base URL (default: {config_v3.OLLAMA_URL}).",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=config_v3.LLM_CACHE_DIR,
        metavar="PATH",
        help="Directory for LLM response cache.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero (code 5) if any stub enrichment fails.",
    )
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--version", action="version", version=f"enrich_stubs {__version__}")
    return parser


def _configure_logging(verbosity: int, quiet: bool) -> None:
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _configure_logging(args.verbose, args.quiet)

    search_dirs = list(args.input_dirs) if args.input_dirs else list(DEFAULT_SEARCH_DIRS)

    # Validate input dirs
    valid_dirs = [d for d in search_dirs if d.is_dir()]
    if not valid_dirs:
        logger.error("No valid input directories found: %s", search_dirs)
        return 2

    # Validate output dir (create if necessary)
    if args.output_dir is not None:
        try:
            args.output_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            logger.error("Cannot create output dir %s: %s", args.output_dir, e)
            return 2

    # Scan stubs
    stubs = scan_stubs(valid_dirs, limit=args.limit)
    if not stubs:
        logger.warning("No stubs found in: %s", valid_dirs)
        return 4

    print(f"Found {len(stubs)} stub(s). Model: {args.model}")
    if args.dry_run:
        print("DRY-RUN mode — no files will be written.")
    if args.output_dir:
        print(f"Output dir: {args.output_dir}")

    # Ping Ollama before starting
    with OllamaClient(
        model=args.model,
        url=args.ollama_url,
        cache_dir=args.cache_dir,
        timeout_s=config_v3.LLM_REQUEST_TIMEOUT_S,
    ) as client:
        if not client.ping():
            logger.error("Ollama not reachable at %s", args.ollama_url)
            return 6

        try:
            results, stats = enrich_all(
                stubs,
                client,
                model=args.model,
                bypass_cache=args.bypass_cache,
                dry_run=args.dry_run,
                output_dir=args.output_dir,
                search_roots=search_dirs,
            )
        except KeyboardInterrupt:
            print("\nInterrupted.")
            return 130

    # Summary
    print(
        f"\nDone. total={stats['total']}  ok={stats['ok']}  "
        f"cached={stats['cached']}  written={stats['written']}  "
        f"failed={stats['failed']}"
    )

    if args.strict and stats["failed"] > 0:
        return 5

    return 0


if __name__ == "__main__":
    sys.exit(main())
