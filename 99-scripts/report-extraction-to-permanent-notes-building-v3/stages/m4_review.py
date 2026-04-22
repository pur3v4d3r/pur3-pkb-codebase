#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m4_review.py — Phase 4: Interactive review of verified merge candidates.

TIER-0 and auto_merge clusters are automatically accepted without review.
LLM-verified clusters are shown one at a time for human approval.

Progress is saved after every decision — interrupt and resume safely.
The session shows running totals at all times.

Output: merge-state/04_decisions.json
"""
from __future__ import annotations

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent.parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import config_merge
from lib.ui import console

from rich.panel import Panel
from rich.table import Table

logger = logging.getLogger(__name__)


# ════════════════════════════════════════════════════════════════════════════
# Helpers
# ════════════════════════════════════════════════════════════════════════════

def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Run previous phase first. Missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _build_stubs_index(scan: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {s["path"]: s for s in scan["stubs"]}


def _write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def _display_cluster(
    cluster: dict[str, Any],
    stubs_index: dict[str, dict[str, Any]],
    index: int,
    total: int,
    auto_accepted: int,
    accepted: int,
    rejected: int,
    skipped: int,
) -> None:
    """Render a cluster as a Rich table with LLM reasoning panel."""
    tier = cluster.get("tier", 1)
    auto = cluster.get("auto_merge", False)
    max_score = cluster.get("max_pair_score", 0)
    cid = cluster["cluster_id"]

    if tier == 0:
        badge = "[bold green]TIER-0 (exact name)[/bold green]"
    elif auto:
        badge = f"[bold yellow]AUTO-MERGE (score {max_score:.3f})[/bold yellow]"
    else:
        badge = f"[bold cyan]LLM VERIFIED (max score {max_score:.3f})[/bold cyan]"

    title = f"Cluster {cid} — {badge}  [{index}/{total} remaining]"

    table = Table(title=title, show_lines=True, expand=True)
    table.add_column("#", style="dim", width=3)
    table.add_column("Title", style="bold white", no_wrap=False, min_width=30)
    table.add_column("Domain", style="yellow", max_width=20)
    table.add_column("Sources", style="green", max_width=15)
    table.add_column("Definition (first 120 chars)", no_wrap=False)

    for i, m in enumerate(cluster["members"], 1):
        stub = stubs_index.get(m["path"], {})
        defn = (stub.get("definition_text") or "")[:120].replace("\n", " ")
        srcs = str(len(stub.get("source_reports", [])))
        table.add_row(
            str(i),
            stub.get("title", m["path"]),
            stub.get("domain", "?"),
            srcs,
            defn or "(no definition)",
        )

    console.print()
    console.print(table)

    reasoning = cluster.get("llm_reasoning", "")
    if reasoning and "TIER-0" not in reasoning and "Auto-merge" not in reasoning:
        console.print(Panel(reasoning, title="LLM Reasoning", style="dim italic"))

    # Running stats
    console.print(
        f"  Stats: [green]+{auto_accepted} auto[/green] | "
        f"[green]+{accepted} accepted[/green] | "
        f"[red]-{rejected} rejected[/red] | "
        f"[dim]{skipped} skipped[/dim]"
    )


def _prompt_decision(cluster_id: str) -> str:
    """Return one of: accept, reject, skip, view, quit."""
    console.print(
        "\n  [bold]\\[A]ccept · \\[R]eject · \\[S]kip · \\[V]iew full · \\[Q]uit[/bold]",
        highlight=False,
    )
    while True:
        try:
            key = input("> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            return "quit"
        mapping = {"a": "accept", "r": "reject", "s": "skip", "v": "view", "q": "quit"}
        if key in mapping:
            return mapping[key]
        console.print("  Enter A, R, S, V, or Q", style="red")


def _view_full(cluster: dict[str, Any], stubs_index: dict[str, dict[str, Any]]) -> None:
    """Display full content of each cluster member."""
    for m in cluster["members"]:
        stub = stubs_index.get(m["path"], {})
        path = Path(m["path"])
        console.print(f"\n{'-' * 60}")
        console.print(f"[bold]{stub.get('title', path.name)}[/bold]  ({path.name})")
        console.print(f"{'-' * 60}")
        try:
            text = path.read_text(encoding="utf-8")
            # Show first 80 lines only to avoid flooding terminal
            lines = text.splitlines()[:80]
            console.print("\n".join(lines))
            if len(text.splitlines()) > 80:
                console.print(f"\n  ... ({len(text.splitlines()) - 80} more lines)", style="dim")
        except OSError as e:
            console.print(f"  [red]Cannot read file: {e}[/red]")


# ════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════

def run(state_dir: Path | None = None) -> dict[str, Any]:
    """Interactive review loop; writes 04_decisions.json."""
    state_dir = state_dir or config_merge.MERGE_STATE_DIR

    scan = _load_json(state_dir / config_merge.SCAN_STATE_FILE)
    verified_data = _load_json(state_dir / config_merge.VERIFIED_STATE_FILE)
    stubs_index = _build_stubs_index(scan)

    all_clusters: list[dict[str, Any]] = verified_data["verified_clusters"]

    # Load existing decisions (resume support)
    decisions_path = state_dir / config_merge.DECISIONS_STATE_FILE
    if decisions_path.exists():
        decisions_state = json.loads(decisions_path.read_text(encoding="utf-8"))
        decisions: dict[str, Any] = decisions_state.get("decisions", {})
        logger.info("Resuming: %d clusters already decided.", len(decisions))
    else:
        decisions = {}

    # Auto-accept tier-0 and auto_merge clusters
    auto_accepted_count = 0
    for c in all_clusters:
        cid = c["cluster_id"]
        if cid in decisions:
            continue
        if c.get("tier") == 0 or c.get("auto_merge"):
            decisions[cid] = {
                "decision": "accept",
                "auto": True,
                "decided_at": datetime.now().isoformat(),
            }
            auto_accepted_count += 1

    if auto_accepted_count > 0:
        logger.info("Auto-accepted %d tier-0/auto-merge clusters.", auto_accepted_count)
        _save_decisions(decisions_path, decisions, all_clusters)

    # Determine clusters needing human review
    review_queue = [
        c for c in all_clusters
        if c["cluster_id"] not in decisions
        and not c.get("auto_merge")
        and c.get("tier", 1) != 0
    ]

    if not review_queue:
        console.print(
            "\n[bold green]All clusters already decided. Nothing to review.[/bold green]"
        )
        return _save_and_return(decisions_path, decisions, all_clusters, state_dir)

    console.print(
        f"\n[bold]Stub Consolidation Review[/bold]\n"
        f"  {len(review_queue)} clusters to review "
        f"({auto_accepted_count} auto-accepted)\n"
        f"  Press Ctrl-C or Q to save progress and exit."
    )

    accepted = sum(1 for v in decisions.values() if v["decision"] == "accept" and not v.get("auto"))
    rejected = sum(1 for v in decisions.values() if v["decision"] == "reject")
    skipped = sum(1 for v in decisions.values() if v["decision"] == "skip")

    for i, cluster in enumerate(review_queue):
        cid = cluster["cluster_id"]
        remaining = len(review_queue) - i

        while True:
            _display_cluster(
                cluster, stubs_index, remaining, len(review_queue),
                auto_accepted_count, accepted, rejected, skipped,
            )
            action = _prompt_decision(cid)

            if action == "view":
                _view_full(cluster, stubs_index)
                continue

            if action == "quit":
                console.print("\n[yellow]Saving progress and exiting...[/yellow]")
                _save_decisions(decisions_path, decisions, all_clusters)
                console.print(f"  Saved {len(decisions)} decisions to {decisions_path}")
                sys.exit(0)

            # Record decision
            decisions[cid] = {
                "decision": action,
                "auto": False,
                "decided_at": datetime.now().isoformat(),
            }

            if action == "accept":
                accepted += 1
            elif action == "reject":
                rejected += 1
            elif action == "skip":
                skipped += 1

            _save_decisions(decisions_path, decisions, all_clusters)
            break

    console.print(
        f"\n[bold green]Review complete![/bold green]"
        f"\n  Auto-accepted: {auto_accepted_count}"
        f"\n  Accepted:      {accepted}"
        f"\n  Rejected:      {rejected}"
        f"\n  Skipped:       {skipped}"
    )

    return _save_and_return(decisions_path, decisions, all_clusters, state_dir)


def _save_decisions(
    path: Path,
    decisions: dict[str, Any],
    all_clusters: list[dict[str, Any]],
) -> None:
    data = {
        "saved_at": datetime.now().isoformat(),
        "total_decided": len(decisions),
        "accepted": sum(1 for v in decisions.values() if v["decision"] == "accept"),
        "rejected": sum(1 for v in decisions.values() if v["decision"] == "reject"),
        "skipped": sum(1 for v in decisions.values() if v["decision"] == "skip"),
        "decisions": decisions,
    }
    _write_json_atomic(path, data)


def _save_and_return(
    path: Path,
    decisions: dict[str, Any],
    all_clusters: list[dict[str, Any]],
    state_dir: Path,
) -> dict[str, Any]:
    _save_decisions(path, decisions, all_clusters)
    logger.info("Phase 4 complete → %s", path)
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)
