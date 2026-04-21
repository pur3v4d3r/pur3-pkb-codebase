#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipeline_v3.py — Master orchestrator for the v3 report → permanent-notes pipeline.

Phase 5 status:
  Stages 7, 8, 9, 10 are wired and runnable end-to-end against a target
  notes directory (e.g. the Phase-3 sandbox). Stages 1-6 produce that
  directory and remain available as standalone modules under ``stages/``;
  full 1->10 orchestration ships in a later phase.

Usage:
    # Phase 5 minimum: harden + audit an existing notes dir
    python pipeline_v3.py --to-stage 10 --target-dir _v3-output/phase-5-sandbox
    python pipeline_v3.py --to-stage 10 --target-dir <dir> --execute
    python pipeline_v3.py --from-stage 7 --target-dir <dir> --execute
    python pipeline_v3.py --to-stage 10 --target-dir <dir> \
        --reports-dir 999-report-organizing/from-copilot --execute

Exit codes:
    0   success (all requested stages succeeded; gates pass if Stage 10 ran)
    1   uncaught error
    2   bad arguments / target-dir missing
    6   Stage 10 gate failure
    130 KeyboardInterrupt

Spec reference: §5 Phase 5 (lines 480-494).

Version:
    3.0.0-phase5
"""
from __future__ import annotations

import sys
from pathlib import Path

import click

import config_v3
from stages import s7_stubs, s8_resolve_links, s9_normalize_links, s10_audit


STAGES: tuple[tuple[int, str, str], ...] = (
    (1, "extract",          "Run pkb_extractor on unprocessed report directories"),
    (2, "validate",         "Strip garbage links, sanitize extracted JSON"),
    (3, "consolidate",      "Merge candidates across batches into super-candidates"),
    (4, "normalize",        "[opt-in] LLM concept normalization + alias mining"),
    (5, "match",            "Embed + hybrid-score against existing notes"),
    (6, "render",           "Render slim conditional template to permanent notes"),
    (7, "stubs",            "Generate stubs for unresolved real concepts"),
    (8, "resolve_links",    "Rewrite report wiki-links to resolved targets"),
    (9, "normalize_links",  "Vault-wide wiki-link normalization"),
    (10, "audit",           "Resolution + quality scoring + gate enforcement"),
    (11, "moc",             "Per-domain MOC + concept-graph generation"),
    (12, "commit",          "Vault index, run report, optional git commit"),
)


# Stages implemented in this phase. Stages 1-6 remain individually runnable.
PHASE5_STAGES: frozenset[int] = frozenset({7, 8, 9, 10})


def _select_stage_range(to_stage: int | None, from_stage: int | None) -> list[int]:
    """Resolve --from/--to flags into the ordered list of stage numbers to run."""
    lo = from_stage if from_stage is not None else 7
    hi = to_stage if to_stage is not None else 10
    if lo > hi:
        raise click.BadParameter(f"--from-stage ({lo}) > --to-stage ({hi})")
    return [n for n in range(lo, hi + 1) if n in PHASE5_STAGES]


def _run_stage_7(target_dir: Path, *, execute: bool, verbose: int) -> None:
    """Stage 7: hardened stub generation."""
    click.echo(f"\n[STAGE 7] s7_stubs --notes-dir {target_dir} {'--execute' if execute else '(dry-run)'}")
    stats = s7_stubs.generate_stubs_filtered(target_dir, execute=execute)
    click.echo(f"  raw={stats.raw_missing} accepted={stats.accepted} rejected={stats.rejected}")
    click.echo(f"  planned={stats.plans} written={stats.written}")


def _run_stage_8(target_dir: Path, reports_dirs: list[Path], *,
                 execute: bool, verbose: int) -> None:
    """Stage 8: rewrite wiki-links inside source reports."""
    if not reports_dirs:
        click.echo("\n[STAGE 8] SKIPPED — no --reports-dir provided.")
        return
    click.echo(f"\n[STAGE 8] s8_resolve_links across {len(reports_dirs)} report dir(s) "
               f"{'--execute' if execute else '(dry-run)'}")
    stats = s8_resolve_links.resolve_report_links(
        target_dir, reports_dirs, execute=execute, verbose=verbose >= 1,
    )
    click.echo(f"  scanned={stats.files_scanned} changed={stats.files_changed} "
               f"rewrites={stats.total_rewrites} unresolved={len(stats.unresolved)}")


def _run_stage_9(target_dir: Path, *, execute: bool, verbose: int) -> None:
    """Stage 9: vault-wide wiki-link pipe-syntax normalization."""
    click.echo(f"\n[STAGE 9] s9_normalize_links --notes-dir {target_dir} "
               f"{'--execute' if execute else '(dry-run)'}")
    stats = s9_normalize_links.normalize_notes(target_dir, execute=execute)
    click.echo(f"  scanned={stats.files_scanned} changed={stats.files_changed} "
               f"rewrites={stats.total_rewrites}")


def _run_stage_10(target_dir: Path, output_dir: Path, *,
                  fail_on_violation: bool) -> bool:
    """Stage 10: audit + gate enforcement. Returns True if gates passed."""
    click.echo(f"\n[STAGE 10] s10_audit --notes-dir {target_dir} --output-dir {output_dir}")
    summary = s10_audit.run_audit_stage(
        target_dir, output_dir,
        fail_on_violation=False,  # we surface the result ourselves
        write_markdown=True,
    )
    s10_audit.print_gate_summary(summary)
    if not summary.all_gates_passed and fail_on_violation:
        return False
    return True


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--to-stage", type=int, default=None, help="Run stages 1..N inclusive (Phase 5 supports 7-10).")
@click.option("--from-stage", type=int, default=None, help="Resume starting at stage N.")
@click.option("--target-dir", type=click.Path(path_type=Path), default=None,
              help="Notes directory to operate on (required for stages 7-10).")
@click.option("--reports-dir", type=click.Path(path_type=Path), multiple=True,
              help="Report directory for Stage 8. Repeatable. If omitted, Stage 8 is skipped.")
@click.option("--audit-output-dir", type=click.Path(path_type=Path), default=None,
              help="Where Stage 10 writes its report (default: <target-dir>/_audit).")
@click.option("--rebuild", is_flag=True, help="Delete _permanent-notes/ before running. Requires --execute.")
@click.option("--execute", is_flag=True, help="Apply changes (default: dry-run).")
@click.option("--llm-normalize", is_flag=True, help="Enable Stage 4 LLM normalization (not in Phase 5).")
@click.option("--llm-synthesize", is_flag=True, help="Enable LLM synthesis pass (not in Phase 5).")
@click.option("--incremental", is_flag=True, help="Skip stages whose inputs are unchanged (not in Phase 5).")
@click.option("--strict-links", is_flag=True, help="Fail (exit 5) on any garbage link.")
@click.option("--no-fail-gates", is_flag=True, help="Stage 10 reports gate results but does not fail the run.")
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet", is_flag=True)
@click.version_option(config_v3.PIPELINE_VERSION)
def main(  # noqa: PLR0913
    to_stage: int | None,
    from_stage: int | None,
    target_dir: Path | None,
    reports_dir: tuple[Path, ...],
    audit_output_dir: Path | None,
    rebuild: bool,
    execute: bool,
    llm_normalize: bool,
    llm_synthesize: bool,
    incremental: bool,
    strict_links: bool,
    no_fail_gates: bool,
    verbose: int,
    quiet: bool,
) -> int:
    """Orchestrate Phase 5 stages 7-10 against a target notes directory."""
    click.echo(f"pipeline_v3 v{config_v3.PIPELINE_VERSION}\n")

    stages_to_run = _select_stage_range(to_stage, from_stage)
    if not stages_to_run:
        click.echo("No Phase-5 stages selected. Use --to-stage 10 (default range covers 7-10).")
        return 0

    if any(s in stages_to_run for s in (7, 8, 9, 10)):
        if target_dir is None:
            click.echo("ERROR: --target-dir is required for stages 7-10.", err=True)
            return 2
        if not target_dir.is_dir():
            click.echo(f"ERROR: target-dir does not exist: {target_dir}", err=True)
            return 2

    output_dir = audit_output_dir or (target_dir / "_audit") if target_dir else None

    click.echo(f"Running stages: {stages_to_run}")
    click.echo(f"Target dir:     {target_dir}")
    click.echo(f"Reports dirs:   {list(reports_dir) or '(none)'}")
    click.echo(f"Mode:           {'EXECUTE' if execute else 'DRY-RUN'}")
    click.echo(f"Audit output:   {output_dir}")

    try:
        for n in stages_to_run:
            if n == 7:
                _run_stage_7(target_dir, execute=execute, verbose=verbose)
            elif n == 8:
                _run_stage_8(target_dir, list(reports_dir),
                             execute=execute, verbose=verbose)
            elif n == 9:
                _run_stage_9(target_dir, execute=execute, verbose=verbose)
            elif n == 10:
                ok = _run_stage_10(target_dir, output_dir,
                                   fail_on_violation=not no_fail_gates)
                if not ok:
                    click.echo("\nGate(s) failed. See audit-report.{json,md} for details.", err=True)
                    return 6
    except KeyboardInterrupt:
        click.echo("\nInterrupted.", err=True)
        return 130
    except Exception as e:  # noqa: BLE001
        click.echo(f"\nUnexpected error: {e}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        return 1

    click.echo("\nAll requested stages completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # type: ignore[no-untyped-call]
