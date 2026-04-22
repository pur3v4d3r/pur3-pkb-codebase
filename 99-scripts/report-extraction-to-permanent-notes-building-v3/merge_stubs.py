#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_stubs.py - Permanent note stub consolidation tool.

Identifies duplicate permanent note stubs (created from different reports but
describing the same concept) using Ollama embeddings + Qwen LLM verification,
then merges them with an interactive review interface.

Phases:
    1 --scan      Parse all stubs, detect exact-name duplicates (TIER-0)
    2 --cluster   Generate Ollama embeddings, compute cosine similarity, cluster
    3 --verify    Use Qwen2.5-7B to verify each cluster is a true duplicate
    4 --review    Interactive TUI: accept/reject each suggested merge
    5 --merge     Execute accepted merges + vault-wide wikilink rewriting

Usage:
    cd 99-scripts/report-extraction-to-permanent-notes-building-v3
    python merge_stubs.py --scan
    python merge_stubs.py --cluster
    python merge_stubs.py --verify
    python merge_stubs.py --review
    python merge_stubs.py --merge [--dry-run]
    python merge_stubs.py --all [--dry-run]
    python merge_stubs.py --status
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

# Ensure v3 root is importable (handles running from any directory)
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import click

import config_merge
from lib.ui import console

logger = logging.getLogger(__name__)


# ============================================================================
# Logging setup
# ============================================================================

def _setup_logging(verbosity: int) -> None:
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG
    logging.basicConfig(
        format="%(levelname)-8s %(name)s - %(message)s",
        level=level,
    )


# ============================================================================
# Status helpers
# ============================================================================

def _phase_status() -> None:
    """Print a summary of each phase's output file."""
    state_dir = config_merge.MERGE_STATE_DIR
    phases = [
        ("Phase 1 - Scan",    config_merge.SCAN_STATE_FILE,      "total_scanned",  "stubs"),
        ("Phase 2 - Cluster", config_merge.CLUSTER_STATE_FILE,   "total_clusters", "clusters"),
        ("Phase 3 - Verify",  config_merge.VERIFIED_STATE_FILE,  "total_verified", "verified clusters"),
        ("Phase 4 - Review",  config_merge.DECISIONS_STATE_FILE, "total_decided",  "decisions"),
        ("Phase 5 - Merge",   config_merge.MERGE_LOG_FILE,       "clusters_merged","merges"),
    ]
    console.print("\n[bold]Merge-Stubs Phase Status[/bold]")
    console.print(f"  State dir: {state_dir}\n")
    for label, fname, count_key, unit in phases:
        fpath = state_dir / fname
        if fpath.exists():
            try:
                data = json.loads(fpath.read_text(encoding="utf-8"))
                count = data.get(count_key, "?")
                gen = (
                    data.get("generated_at")
                    or data.get("saved_at")
                    or data.get("executed_at")
                    or ""
                )
                gen_short = gen[:19] if gen else ""
                console.print(
                    f"  [green]OK[/green] {label}: [bold]{count}[/bold] {unit}  ({gen_short})"
                )
            except Exception as e:
                console.print(
                    f"  [yellow]?[/yellow] {label}: file exists but unreadable ({e})"
                )
        else:
            console.print(f"  [dim]--[/dim] {label}: not yet run")
    console.print()


# ============================================================================
# CLI
# ============================================================================

@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--scan",    is_flag=True, help="Phase 1: scan stubs directory")
@click.option("--cluster", is_flag=True, help="Phase 2: embed + cluster")
@click.option("--verify",  is_flag=True, help="Phase 3: LLM verification")
@click.option("--review",  is_flag=True, help="Phase 4: interactive review TUI")
@click.option("--merge",   is_flag=True, help="Phase 5: execute merges + wikilink rewriting")
@click.option("--all", "run_all", is_flag=True, help="Run phases 1-5 sequentially")
@click.option("--dry-run", is_flag=True, help="Phase 5: preview actions without writing")
@click.option("--status",  is_flag=True, help="Show current state of each phase output")
@click.option("-v", "--verbose", count=True, help="-v = INFO, -vv = DEBUG")
def main(
    scan: bool,
    cluster: bool,
    verify: bool,
    review: bool,
    merge: bool,
    run_all: bool,
    dry_run: bool,
    status: bool,
    verbose: int,
) -> None:
    """Consolidate duplicate permanent note stubs using Ollama + interactive review."""
    _setup_logging(verbose)

    if status:
        _phase_status()
        return

    if not any([scan, cluster, verify, review, merge, run_all]):
        click.echo(
            "No phase selected. Use --scan, --cluster, --verify, --review, --merge, "
            "--all, or --status.\nRun with -h for help.",
            err=True,
        )
        sys.exit(1)

    state_dir = config_merge.MERGE_STATE_DIR

    if scan or run_all:
        _run_phase("Phase 1 - Scan", lambda: _import_and_run("m1_scan", state_dir=state_dir))

    if cluster or run_all:
        _run_phase("Phase 2 - Cluster", lambda: _import_and_run("m2_cluster", state_dir=state_dir))

    if verify or run_all:
        _run_phase("Phase 3 - Verify", lambda: _import_and_run("m3_verify", state_dir=state_dir))

    if review or run_all:
        _run_phase("Phase 4 - Review", lambda: _import_and_run("m4_review", state_dir=state_dir))

    if merge or run_all:
        _run_phase(
            "Phase 5 - Merge",
            lambda: _import_and_run("m5_merge", state_dir=state_dir, dry_run=dry_run),
        )


def _import_and_run(module_name: str, **kwargs: object) -> None:
    """Import a stage module and call its run() function."""
    import importlib
    mod = importlib.import_module(f"stages.{module_name}")
    mod.run(**kwargs)


def _run_phase(label: str, fn: object) -> None:
    console.print(f"\n[bold blue]== {label} ==[/bold blue]")
    try:
        fn()
        console.print(f"[green]DONE: {label}[/green]")
    except FileNotFoundError as e:
        console.print(f"[red]FAIL: {label}[/red] {e}")
        sys.exit(1)
    except RuntimeError as e:
        console.print(f"[red]FAIL: {label}[/red] {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print(f"\n[yellow]Interrupted during {label}.[/yellow]")
        sys.exit(0)


if __name__ == "__main__":
    main()
