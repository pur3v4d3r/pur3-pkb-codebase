#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m5_merge.py — Phase 5: Execute accepted merges + vault-wide wikilink rewriting.

For each accepted cluster:
  1. Select primary (most source-reports; tie-break: alphabetical title)
  2. Merge YAML frontmatter (union aliases/tags/source-reports; primary scalars win)
  3. Merge content body (primary definition canonical; append new callouts; union links)
  4. Write merged file to primary path (atomic)
  5. Move non-primary files to TRASH_DIR

After all file merges:
  6. Build redirect map {old_title/alias → primary_title}
  7. Walk all vault .md files; rewrite stale wikilinks (atomic per file)

Use --dry-run to preview without writing anything.

Output: merge-state/05_merge_log.json
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import logging
import re
import shutil
import sys
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent.parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_merge
from lib.frontmatter import parse_frontmatter, merge_frontmatter, render_frontmatter
from lib.ui import console

logger = logging.getLogger(__name__)

# ─── Regex helpers ────────────────────────────────────────────────────────────

# Matches [!callout-type] blocks (one or more lines starting with >)
_CALLOUT_BLOCK_RE = re.compile(
    r"(?:^|\n)(> \[![^\]]+\][^\n]*(?:\n>[ \t]?[^\n]*)*)",
    re.MULTILINE,
)
_CALLOUT_PREFIX_RE = re.compile(r"^>\s?", re.MULTILINE)

# Matches **Related:** wikilinks
_RELATED_LINE_RE = re.compile(r"\*\*Related:\*\*\s*(.*?)(?=\n\n|\n```|\Z)", re.DOTALL)

# Matches [[target]] and [[target|display]]
_WIKILINK_RE = re.compile(r"\[\[([^\[\]|]+?)(?:\|[^\[\]]+?)?\]\]")
_WIKILINK_FULL_RE = re.compile(r"\[\[([^\[\]|]+?)((?:\|[^\[\]]+?)?)\]\]")

# Dataview block
_DATAVIEW_RE = re.compile(r"```dataview\n.*?```", re.DOTALL)

# Sources footer
_SOURCES_RE = re.compile(r"\n---\n\n\*\*Sources:\*\*.*$", re.DOTALL)


# ════════════════════════════════════════════════════════════════════════════
# Helpers: loading
# ════════════════════════════════════════════════════════════════════════════

def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Run previous phase first. Missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _build_stubs_index(scan: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {s["path"]: s for s in scan["stubs"]}


def _safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


# ════════════════════════════════════════════════════════════════════════════
# Primary selection
# ════════════════════════════════════════════════════════════════════════════

def select_primary(
    cluster: dict[str, Any],
    stubs_index: dict[str, dict[str, Any]],
) -> str:
    """Return the path of the primary stub for this cluster."""
    # Honour LLM's title suggestion if it matches a member
    llm_title = cluster.get("llm_primary_title")
    if llm_title:
        for m in cluster["members"]:
            stub = stubs_index.get(m["path"], {})
            if stub.get("title") == llm_title:
                return m["path"]

    # Fallback: most source-reports → alphabetical title
    def _sort_key(m: dict[str, Any]) -> tuple[int, str]:
        stub = stubs_index.get(m["path"], {})
        n_sources = len(stub.get("source_reports") or [])
        title = stub.get("title", "")
        return (-n_sources, title)

    return min(cluster["members"], key=_sort_key)["path"]


# ════════════════════════════════════════════════════════════════════════════
# Frontmatter merge
# ════════════════════════════════════════════════════════════════════════════

def build_merged_frontmatter(
    primary_fm: dict[str, Any],
    secondary_fms: list[dict[str, Any]],
    today: dt.date,
) -> dict[str, Any]:
    """Union source-reports, aliases, tags across all stubs; primary scalars win."""
    # Collect all sources, aliases, tags from non-primaries
    all_sources: list[str] = list(
        (primary_fm.get("provenance") or {}).get("source-reports") or []
    )
    extra_aliases: list[str] = []
    extra_tags: list[str] = []

    for sfm in secondary_fms:
        prov = sfm.get("provenance") or {}
        for s in (prov.get("source-reports") or []):
            if str(s) not in all_sources:
                all_sources.append(str(s))
        for a in (sfm.get("aliases") or []):
            if str(a) not in extra_aliases:
                extra_aliases.append(str(a))
        for t in (sfm.get("tags") or []):
            if str(t) not in extra_tags:
                extra_tags.append(str(t))

    # Build "fresh" dict: primary values but with enriched provenance
    fresh = dict(primary_fm)
    fresh["updated"] = today.isoformat()

    fr_prov = dict(fresh.get("provenance") or {})
    fr_prov["source-reports"] = sorted(set(str(s) for s in all_sources))
    fresh["provenance"] = fr_prov

    # Add extra aliases/tags from non-primaries (merge_frontmatter unions them)
    fresh["aliases"] = list(fresh.get("aliases") or []) + extra_aliases
    fresh["tags"] = list(fresh.get("tags") or []) + extra_tags

    # merge_frontmatter(existing=primary, fresh=enriched_primary):
    # - Preserves primary's user-editable scalars (status, mastery-stage, etc.)
    # - Unions aliases and tags (existing-first)
    # - Unions provenance.source-reports
    # - Preserves primary's created date
    return merge_frontmatter(primary_fm, fresh)


# ════════════════════════════════════════════════════════════════════════════
# Body merge
# ════════════════════════════════════════════════════════════════════════════

def _callout_hash(block: str) -> str:
    body = _CALLOUT_PREFIX_RE.sub("", block).strip()
    return hashlib.sha1(body.encode("utf-8")).hexdigest()


def _extract_callout_blocks(text: str) -> list[str]:
    return [m.group(1).strip() for m in _CALLOUT_BLOCK_RE.finditer(text)]


def _extract_related_links(body: str) -> list[str]:
    """Extract wikilink targets from **Related:** line(s)."""
    m = _RELATED_LINE_RE.search(body)
    if not m:
        return []
    return _WIKILINK_RE.findall(m.group(1))


def _dedup_list(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def _extract_dataview_block(body: str) -> str:
    m = _DATAVIEW_RE.search(body)
    return m.group(0).strip() if m else ""


def _strip_tail(body: str) -> str:
    """Remove ## Connections, dataview block, and Sources footer from body."""
    # Strip ## Connections and everything after
    conn = body.find("\n## Connections")
    if conn >= 0:
        body = body[:conn]
    # Strip dataview
    dv = body.find("\n```dataview")
    if dv >= 0:
        body = body[:dv]
    # Strip Sources footer
    m = _SOURCES_RE.search(body)
    if m:
        body = body[:m.start()]
    return body.rstrip()


def merge_bodies(
    primary_body: str,
    secondary_bodies: list[str],
    all_source_reports: list[str],
    merged_title: str,
) -> str:
    """Combine primary body with non-primary content blocks."""
    # Primary's content area (before Connections/dataview/Sources)
    primary_content = _strip_tail(primary_body)

    # Collect hashes of primary's callout blocks (dedup baseline)
    primary_callouts = _extract_callout_blocks(primary_content)
    seen_hashes = {_callout_hash(b) for b in primary_callouts}

    # Collect new callout blocks from non-primaries
    new_blocks: list[str] = []
    for sbody in secondary_bodies:
        content_area = _strip_tail(sbody)
        for block in _extract_callout_blocks(content_area):
            h = _callout_hash(block)
            if h not in seen_hashes:
                seen_hashes.add(h)
                new_blocks.append(block)

    # Union Related wikilinks (deduplicated)
    all_links = _extract_related_links(primary_body)
    seen_links: set[str] = set(all_links)
    for sbody in secondary_bodies:
        for link in _extract_related_links(sbody):
            if link not in seen_links:
                seen_links.add(link)
                all_links.append(link)
    deduped_links = _dedup_list(all_links)

    # Dataview block from primary
    dataview_block = _extract_dataview_block(primary_body)

    # Assemble merged body
    result = primary_content

    if new_blocks:
        result += "\n\n## Additional Material (Merged)\n"
        for block in new_blocks:
            result += "\n" + block + "\n"

    # Connections section
    result += "\n\n## Connections\n"
    if deduped_links:
        links_str = " · ".join(f"[[{link}]]" for link in deduped_links)
        result += f"\n**Related:** {links_str}"

    # Dataview block
    if dataview_block:
        result += f"\n\n{dataview_block}"

    # Sources footer
    if all_source_reports:
        sources_str = " · ".join(f"[[{s}]]" for s in sorted(set(all_source_reports)))
        result += f"\n\n---\n\n**Sources:** {sources_str}\n"

    return result


# ════════════════════════════════════════════════════════════════════════════
# File operations
# ════════════════════════════════════════════════════════════════════════════

def _write_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def _move_to_trash(path: Path, trash_dir: Path, *, dry_run: bool) -> Path | None:
    if not path.exists():
        logger.debug("Skipping trash move for already-absent file: %s", path)
        return None
    trash_dir.mkdir(parents=True, exist_ok=True)
    dest = trash_dir / path.name
    suffix = 1
    while dest.exists():
        dest = trash_dir / f"{path.stem}_{suffix}{path.suffix}"
        suffix += 1
    if not dry_run:
        shutil.move(str(path), str(dest))
    return dest


def _write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


# ════════════════════════════════════════════════════════════════════════════
# Wikilink rewriting
# ════════════════════════════════════════════════════════════════════════════

def build_redirect_map(
    accepted_clusters_with_primary: list[dict[str, Any]],
    stubs_index: dict[str, dict[str, Any]],
) -> dict[str, str]:
    """Build {old_title_or_alias: primary_title} for every absorbed stub."""
    redirect: dict[str, str] = {}
    for entry in accepted_clusters_with_primary:
        primary_path = entry["primary_path"]
        primary_title = stubs_index.get(primary_path, {}).get("title", "")
        if not primary_title:
            continue
        for m in entry["cluster"]["members"]:
            if m["path"] == primary_path:
                continue
            stub = stubs_index.get(m["path"], {})
            old_title = stub.get("title", "")
            if old_title and old_title != primary_title:
                redirect[old_title] = primary_title
            for alias in stub.get("aliases") or []:
                alias = str(alias).strip()
                if alias and alias != primary_title:
                    redirect[alias] = primary_title
    return redirect


def rewrite_file_wikilinks(
    path: Path,
    redirect_map: dict[str, str],
    *,
    dry_run: bool,
) -> int:
    """Rewrite stale wikilinks in one file; returns count of rewrites made."""
    try:
        text = _safe_read(path)
    except OSError:
        return 0

    # Quick pre-filter: skip file if none of the old titles appear in it
    if not any(old in text for old in redirect_map):
        return 0

    rewrites = 0

    def _replacer(m: re.Match) -> str:
        nonlocal rewrites
        target = m.group(1)
        display_part = m.group(2)  # e.g. "|display text" or ""
        new_target = redirect_map.get(target)
        if new_target is None:
            return m.group(0)
        rewrites += 1
        return f"[[{new_target}{display_part}]]"

    new_text = _WIKILINK_FULL_RE.sub(_replacer, text)

    if rewrites > 0 and not dry_run:
        _write_atomic(path, new_text)

    return rewrites


# ════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════

def run(
    state_dir: Path | None = None,
    *,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Execute all accepted merges and update vault wikilinks."""
    state_dir = state_dir or config_merge.MERGE_STATE_DIR
    today = dt.date.today()

    scan = _load_json(state_dir / config_merge.SCAN_STATE_FILE)
    verified_data = _load_json(state_dir / config_merge.VERIFIED_STATE_FILE)
    decisions_data = _load_json(state_dir / config_merge.DECISIONS_STATE_FILE)

    stubs_index = _build_stubs_index(scan)
    decisions: dict[str, Any] = decisions_data.get("decisions", {})
    verified_clusters: list[dict[str, Any]] = verified_data["verified_clusters"]

    # Build lookup: cluster_id → cluster
    cluster_map: dict[str, dict[str, Any]] = {
        c["cluster_id"]: c for c in verified_clusters
    }

    # Determine accepted clusters
    accepted_ids = [
        cid for cid, d in decisions.items()
        if d.get("decision") == "accept" and cid in cluster_map
    ]

    console.print(
        f"\n[bold]Phase 5 — Execute Merges[/bold]  "
        f"({'DRY RUN' if dry_run else 'LIVE'})\n"
        f"  {len(accepted_ids)} clusters to merge"
    )

    merge_log: list[dict[str, Any]] = []
    accepted_with_primary: list[dict[str, Any]] = []
    total_absorbed = 0

    for cid in accepted_ids:
        cluster = cluster_map[cid]
        primary_path = select_primary(cluster, stubs_index)
        primary_stub = stubs_index.get(primary_path, {})
        primary_title = primary_stub.get("title", Path(primary_path).stem)

        non_primary_paths = [
            m["path"] for m in cluster["members"] if m["path"] != primary_path
        ]

        logger.debug("Merging cluster %s → primary: %s", cid, primary_title)

        # Read all files
        try:
            primary_text = _safe_read(Path(primary_path))
        except OSError as e:
            logger.warning("Cannot read primary %s: %s — skipping cluster %s", primary_path, e, cid)
            continue

        primary_fm, primary_body = parse_frontmatter(primary_text)
        secondary_fms: list[dict[str, Any]] = []
        secondary_bodies: list[str] = []

        for sp in non_primary_paths:
            try:
                s_text = _safe_read(Path(sp))
            except OSError as e:
                logger.warning("Cannot read %s: %s", sp, e)
                continue
            s_fm, s_body = parse_frontmatter(s_text)
            secondary_fms.append(s_fm)
            secondary_bodies.append(s_body)

        # Merged frontmatter
        merged_fm = build_merged_frontmatter(primary_fm, secondary_fms, today)
        all_sources: list[str] = list(
            (merged_fm.get("provenance") or {}).get("source-reports") or []
        )

        # Merged body
        merged_body = merge_bodies(primary_body, secondary_bodies, all_sources, primary_title)

        # Merged content
        merged_text = render_frontmatter(merged_fm) + "\n" + merged_body

        if dry_run:
            console.print(
                f"  [dim]DRY RUN[/dim] Would merge cluster {cid}: "
                f"primary={primary_title!r}, absorbing {len(non_primary_paths)} stub(s)"
            )
        else:
            _write_atomic(Path(primary_path), merged_text)

        # Move non-primaries to trash
        trashed: list[str] = []
        for sp in non_primary_paths:
            dest = _move_to_trash(Path(sp), config_merge.TRASH_DIR, dry_run=dry_run)
            if dest is not None:
                trashed.append(str(dest))

        log_entry: dict[str, Any] = {
            "cluster_id": cid,
            "primary_path": primary_path,
            "primary_title": primary_title,
            "absorbed_paths": non_primary_paths,
            "trashed_paths": trashed,
            "source_reports_count": len(all_sources),
            "new_callout_blocks": 0,  # populated below if needed
        }
        merge_log.append(log_entry)
        accepted_with_primary.append({"cluster": cluster, "primary_path": primary_path})
        total_absorbed += len(non_primary_paths)

    console.print(
        f"\n  Merged {len(merge_log)} clusters, absorbed {total_absorbed} stubs."
    )

    # ── Vault-wide wikilink rewriting ──────────────────────────────────────

    redirect_map = build_redirect_map(accepted_with_primary, stubs_index)

    if redirect_map:
        console.print(
            f"\n  Rewriting wikilinks for {len(redirect_map)} redirected title(s)..."
        )
        vault_md_files = list(config_merge.VAULT_ROOT.rglob("*.md"))
        total_rewrites = 0
        rewritten_files: list[str] = []

        for md_path in vault_md_files:
            # Skip trash directory
            if ".trash" in md_path.parts:
                continue
            count = rewrite_file_wikilinks(md_path, redirect_map, dry_run=dry_run)
            if count > 0:
                total_rewrites += count
                rewritten_files.append(str(md_path))

        console.print(
            f"  Wikilinks rewritten: {total_rewrites} in {len(rewritten_files)} file(s)"
        )
    else:
        total_rewrites = 0
        rewritten_files = []
        console.print("  No wikilinks to redirect.")

    output: dict[str, Any] = {
        "executed_at": dt.datetime.now().isoformat(),
        "dry_run": dry_run,
        "clusters_merged": len(merge_log),
        "stubs_absorbed": total_absorbed,
        "wikilinks_rewritten": total_rewrites,
        "files_with_rewrites": len(rewritten_files),
        "merges": merge_log,
        "rewritten_files": rewritten_files[:500],  # cap log size
    }

    out_path = state_dir / config_merge.MERGE_LOG_FILE
    _write_json_atomic(out_path, output)
    logger.info("Phase 5 complete → %s", out_path)
    return output
