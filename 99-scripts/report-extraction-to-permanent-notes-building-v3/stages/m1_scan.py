#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m1_scan.py — Phase 1: Scan stub directory, extract metadata, detect TIER-0 duplicates.

TIER-0 duplicates: stubs whose titles share the same normalize_name() key —
exact conceptual duplicates that need no embedding or LLM to detect.

Output: merge-state/01_scan.json
"""
from __future__ import annotations

import json
import logging
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

# Ensure v3 root is importable
_HERE = Path(__file__).resolve().parent.parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_merge
from lib.frontmatter import parse_frontmatter
from lib.candidate import normalize_name

logger = logging.getLogger(__name__)

# ─── Regex helpers ────────────────────────────────────────────────────────────

_DEF_CALLOUT_RE = re.compile(
    r">\s*\[!definition\][^\n]*\n((?:>[ \t]?[^\n]*\n?)*)",
    re.IGNORECASE,
)
_CALLOUT_PREFIX_RE = re.compile(r"^>\s?", re.MULTILINE)
_STUB_PLACEHOLDER_RE = re.compile(
    r"^\*(?:Definition pending|Stub note)",
    re.IGNORECASE,
)


# ════════════════════════════════════════════════════════════════════════════
# Helpers
# ════════════════════════════════════════════════════════════════════════════

def extract_definition_text(body: str, max_chars: int = 300) -> str:
    """Extract first [!definition] callout body; returns '' for stub placeholders."""
    m = _DEF_CALLOUT_RE.search(body)
    if not m:
        return ""
    raw = m.group(1)
    cleaned = _CALLOUT_PREFIX_RE.sub("", raw).strip()
    if _STUB_PLACEHOLDER_RE.match(cleaned):
        return ""
    return cleaned[:max_chars]


def scan_stub(path: Path) -> dict[str, Any] | None:
    """Parse one stub file; returns None on read/parse failure."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            logger.warning("Cannot read %s: %s", path, e)
            return None
    except OSError as e:
        logger.warning("Cannot read %s: %s", path, e)
        return None

    fm, body = parse_frontmatter(text)

    title = str(fm.get("title", "")).strip('"\'') or path.stem
    aliases = [str(a) for a in (fm.get("aliases") or []) if a]
    domain = str(fm.get("domain", ""))
    subdomains = [str(s) for s in (fm.get("subdomains") or [])]

    provenance = fm.get("provenance") or {}
    source_reports = [str(s) for s in (provenance.get("source-reports") or [])]
    source_type = str(provenance.get("source-type", "unknown"))

    tags = [str(t) for t in (fm.get("tags") or [])]
    created = str(fm.get("created", ""))

    return {
        "path": str(path),
        "title": title,
        "norm_key": normalize_name(title),
        "aliases": aliases,
        "domain": domain,
        "subdomains": subdomains,
        "source_reports": source_reports,
        "source_type": source_type,
        "tags": tags,
        "definition_text": extract_definition_text(body),
        "created": created,
    }


def find_tier0_clusters(stubs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Group stubs by norm_key; return clusters with 2+ members."""
    groups: dict[str, list[str]] = defaultdict(list)
    for s in stubs:
        groups[s["norm_key"]].append(s["path"])

    clusters = []
    for norm_key, paths in sorted(groups.items()):
        if len(paths) >= 2:
            clusters.append({
                "cluster_id": f"t0-{len(clusters):04d}",
                "tier": 0,
                "norm_key": norm_key,
                "auto_merge": True,
                "members": [{"path": p} for p in sorted(paths)],
            })
    return clusters


# ════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════

def run(
    stubs_dir: Path | None = None,
    state_dir: Path | None = None,
) -> dict[str, Any]:
    """Scan stubs directory and write 01_scan.json."""
    stubs_dir = stubs_dir or config_merge.STUBS_DIR
    state_dir = state_dir or config_merge.MERGE_STATE_DIR

    if not stubs_dir.exists():
        raise FileNotFoundError(f"Stubs directory not found: {stubs_dir}")

    logger.info("Scanning: %s", stubs_dir)
    paths = sorted(p for p in stubs_dir.glob("*.md") if not p.name.startswith("."))

    stubs: list[dict[str, Any]] = []
    skipped = 0

    for i, path in enumerate(paths):
        if i % 200 == 0 and i > 0:
            logger.info("  %d / %d scanned...", i, len(paths))
        result = scan_stub(path)
        if result is None:
            skipped += 1
        else:
            stubs.append(result)

    logger.info("Scanned %d stubs (%d skipped)", len(stubs), skipped)

    tier0 = find_tier0_clusters(stubs)
    logger.info("TIER-0 clusters (exact normalized name): %d", len(tier0))

    output: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(),
        "stubs_dir": str(stubs_dir),
        "total_scanned": len(stubs),
        "skipped": skipped,
        "tier0_groups": len(tier0),
        "stubs": stubs,
        "tier0_clusters": tier0,
    }

    out_path = state_dir / config_merge.SCAN_STATE_FILE
    _write_json_atomic(out_path, output)
    logger.info("Phase 1 complete → %s", out_path)
    return output


def _write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)
