#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipeline_v3.py — Master orchestrator for the v3 report → permanent-notes pipeline.

Wires stages 1-10 (stage 4, the LLM normaliser, is opt-in and currently
skipped). Intermediate artefacts flow through a workspace directory laid
out as::

    <workspace>/
      extracted/       # Stage 1 output  — <batch>/<report>_extracted.json
      validated/       # Stage 2 output  — <batch>/<report>_validated.json
      consolidated/    # Stage 3 output  — _consolidated-candidates.json
      match/           # Stage 5 output  — match-report.json, embeddings.npz
      notes/           # Stage 6 output  — *.md  (== --target-dir for s7-s10)
      _audit/          # Stage 10 output — audit-report.{json,md}

Individual stage dirs may be overridden via CLI flag. If ``--workspace-dir``
is omitted, any per-stage dir the selected stages need must be supplied
explicitly.

Usage:
    # Phase 5 minimum (harden + audit an existing notes dir)
    python pipeline_v3.py --to-stage 10 --target-dir _v3-output/phase-5-sandbox

    # End-to-end from validation onward against an existing extracted corpus
    python pipeline_v3.py --from-stage 2 --to-stage 10 \
        --workspace-dir _v3-output/runs/2026-04-21 \
        --extracted-dir _v3-output/extracted-corpus \
        --execute

    # Full pipeline including extraction
    python pipeline_v3.py --to-stage 10 \
        --workspace-dir _v3-output/runs/2026-04-21 \
        --reports-to-extract 999-report-organizing/from-copilot \
        --execute

Exit codes:
    0   success
    1   uncaught error
    2   bad arguments / required dir missing
    3   stage 1 extractor subprocess failure
    5   stage 2 strict-links failure  OR  stage 3 evidence-loss checksum
    6   stage 10 gate failure
    130 KeyboardInterrupt

Spec reference: §5 Phases 1-5.

Version:
    3.1.0-phase5-wired
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import click

import config_v3  # noqa: F401  (kept for PIPELINE_VERSION surfacing)
from stages import (
    s2_validate,
    s3_consolidate,
    s5_match,
    s6_render,
    s7_stubs,
    s8_resolve_links,
    s9_normalize_links,
    s10_audit,
)


# ═════════════════════════════════════════════════════════════════════════
# Constants
# ═════════════════════════════════════════════════════════════════════════

__version__ = "3.1.0-phase5-wired"

# Stages wired in this dispatcher (stage 4 opt-in LLM, stages 11-12 deferred).
PIPELINE_STAGES: frozenset[int] = frozenset({1, 2, 3, 5, 6, 7, 8, 9, 10})

STAGES: tuple[tuple[int, str, str], ...] = (
    (1, "extract",         "Run pkb_extractor on report directories"),
    (2, "validate",        "Strip garbage links from extracted JSON"),
    (3, "consolidate",     "Merge candidates across batches"),
    (4, "normalize",       "[opt-in] LLM concept normalization (skipped)"),
    (5, "match",           "Embed + hybrid-score against existing notes"),
    (6, "render",          "Render slim template to permanent notes"),
    (7, "stubs",           "Generate stubs for unresolved real concepts"),
    (8, "resolve_links",   "Rewrite report wiki-links to resolved targets"),
    (9, "normalize_links", "Vault-wide wiki-link normalization"),
    (10, "audit",          "Resolution + quality scoring + gate enforcement"),
    (11, "moc",            "[deferred] Per-domain MOC + concept-graph generation"),
    (12, "commit",         "[deferred] Vault index, run report, optional git commit"),
)

# Path to the v2 extractor (stage 1 wraps it as a subprocess).
_V2_EXTRACTOR: Path = Path(__file__).resolve().parent.parent / "pkb_extractor.py"


# ═════════════════════════════════════════════════════════════════════════
# Workspace layout
# ═════════════════════════════════════════════════════════════════════════

def _resolve_paths(
    workspace: Path | None,
    *,
    extracted: Path | None,
    validated: Path | None,
    consolidated: Path | None,
    match_out: Path | None,
    target: Path | None,
    audit_out: Path | None,
) -> dict[str, Path | None]:
    """Resolve per-stage directories, deriving defaults from workspace if set."""
    def _fill(explicit: Path | None, subdir: str) -> Path | None:
        if explicit is not None:
            return explicit
        if workspace is not None:
            return workspace / subdir
        return None

    return {
        "extracted":    _fill(extracted,    "extracted"),
        "validated":    _fill(validated,    "validated"),
        "consolidated": _fill(consolidated, "consolidated"),
        "match":        _fill(match_out,    "match"),
        "target":       _fill(target,       "notes"),
        "audit":        _fill(audit_out,    "_audit"),
    }


# ═════════════════════════════════════════════════════════════════════════
# Stage dispatchers
# ═════════════════════════════════════════════════════════════════════════

def _run_stage_1(
    reports_to_extract: list[Path],
    extracted_dir: Path | None,
    *,
    execute: bool,
    verbose: int,
) -> None:
    """Stage 1: subprocess to v2 pkb_extractor for each report directory."""
    if not reports_to_extract:
        click.echo("\n[STAGE 1] SKIPPED — no --reports-to-extract provided.")
        return
    if not _V2_EXTRACTOR.exists():
        raise click.ClickException(f"pkb_extractor not found at {_V2_EXTRACTOR}")
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 1] extract ({mode}) → {extracted_dir}")
    if not execute:
        for rd in reports_to_extract:
            click.echo(f"  would extract: {rd}")
        return
    if extracted_dir is not None:
        extracted_dir.mkdir(parents=True, exist_ok=True)
    for rd in reports_to_extract:
        click.echo(f"  extracting: {rd}")
        cmd = [
            sys.executable, str(_V2_EXTRACTOR),
            "--input", str(rd),
            "--output", str(extracted_dir),
            "--recursive",
        ]
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            raise click.ClickException(
                f"pkb_extractor failed on {rd} (exit {e.returncode})"
            ) from e


def _run_stage_2(
    extracted_dir: Path | None,
    validated_dir: Path | None,
    *,
    execute: bool,
    strict_links: bool,
    verbose: int,
) -> None:
    """Stage 2: validate extracted JSON via s2_validate.main(argv)."""
    if extracted_dir is None or not extracted_dir.exists():
        click.echo(f"\n[STAGE 2] SKIPPED — extracted dir not found: {extracted_dir}")
        return
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 2] validate ({mode}) {extracted_dir} → {validated_dir}")
    argv: list[str] = [str(extracted_dir)]
    if validated_dir is not None:
        argv.extend(["-o", str(validated_dir)])
    if not execute:
        argv.append("--dry-run")
    if strict_links:
        argv.append("--strict-links")
    for _ in range(verbose):
        argv.append("-v")
    rc = s2_validate.main(argv)
    if rc != 0:
        raise click.ClickException(f"s2_validate exited {rc}")


def _run_stage_3(
    validated_dir: Path | None,
    consolidated_dir: Path | None,
    *,
    execute: bool,
    verbose: int,
) -> None:
    """Stage 3: consolidate via run_consolidation + write_output."""
    if validated_dir is None or not validated_dir.exists():
        click.echo(f"\n[STAGE 3] SKIPPED — validated dir not found: {validated_dir}")
        return
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 3] consolidate ({mode}) {validated_dir} → {consolidated_dir}")
    inputs = s3_consolidate.discover_inputs(validated_dir)
    if not inputs:
        click.echo(f"  no {s3_consolidate.VALIDATED_GLOB} files found — skipping")
        return
    click.echo(f"  discovered {len(inputs)} validated file(s)")
    _raw, consolidated, stats = s3_consolidate.run_consolidation(inputs)
    click.echo(
        f"  raw={stats['raw_candidates']} → "
        f"consolidated={stats['consolidated_candidates']} "
        f"(checksum={stats['evidence_loss_checksum']})"
    )
    if execute and consolidated_dir is not None:
        output_path = consolidated_dir / s3_consolidate.OUTPUT_FILENAME
        s3_consolidate.write_output(consolidated, stats, output_path)
        click.echo(f"  wrote {output_path}")
    else:
        click.echo("  (dry-run — snapshot not written)")


def _run_stage_5(
    consolidated_dir: Path | None,
    target_dir: Path | None,
    match_output_dir: Path | None,
    *,
    execute: bool,
    verbose: int,
) -> None:
    """Stage 5: embedding + hybrid match via run_match.

    Produces a match-report for human review; does not modify target-dir.
    """
    if consolidated_dir is None:
        click.echo("\n[STAGE 5] SKIPPED — --consolidated-dir not set.")
        return
    candidates_path = consolidated_dir / s3_consolidate.OUTPUT_FILENAME
    if not candidates_path.exists():
        click.echo(
            f"\n[STAGE 5] SKIPPED — consolidated candidates not found: {candidates_path}"
        )
        return
    if target_dir is None or not target_dir.exists():
        click.echo(
            f"\n[STAGE 5] SKIPPED — target-dir (existing notes) not found: {target_dir}"
        )
        return
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 5] match ({mode}) → {match_output_dir}")
    if not execute:
        click.echo("  (dry-run — skipping embedding computation)")
        return
    if match_output_dir is None:
        raise click.ClickException("stage 5 execute requires --match-output-dir or --workspace-dir")
    match_output_dir.mkdir(parents=True, exist_ok=True)
    stats = s5_match.run_match(candidates_path, target_dir, match_output_dir)
    click.echo(
        f"  matched={stats.by_status.get('matched', 0)}"
        f" review={stats.by_status.get('review_queue', 0)}"
        f" new={stats.by_status.get('new', 0)}"
        f" elapsed={stats.elapsed_seconds:.1f}s"
    )


def _run_stage_6(
    consolidated_dir: Path | None,
    target_dir: Path | None,
    *,
    execute: bool,
    verbose: int,
) -> None:
    """Stage 6: render slim template to permanent notes via run_render."""
    if consolidated_dir is None:
        click.echo("\n[STAGE 6] SKIPPED — --consolidated-dir not set.")
        return
    if target_dir is None:
        raise click.ClickException("stage 6 requires --target-dir or --workspace-dir")
    candidates_path = consolidated_dir / s3_consolidate.OUTPUT_FILENAME
    if not candidates_path.exists():
        if not consolidated_dir.is_dir():
            click.echo(
                f"\n[STAGE 6] SKIPPED — consolidated candidates not found: {candidates_path}"
            )
            return
        candidates_path = consolidated_dir
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 6] render ({mode}) {candidates_path} → {target_dir}")
    stats = s6_render.run_render(candidates_path, target_dir, dry_run=not execute)
    click.echo(
        f"  total={stats.notes_total} created={stats.notes_created} "
        f"updated={stats.notes_updated} bytes={stats.bytes_written:,}"
    )


def _run_stage_7(target_dir: Path, *, execute: bool, verbose: int) -> None:
    """Stage 7: hardened stub generation."""
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 7] stubs ({mode}) {target_dir}")
    stats = s7_stubs.generate_stubs_filtered(target_dir, execute=execute)
    click.echo(
        f"  raw={stats.raw_missing} accepted={stats.accepted} "
        f"rejected={stats.rejected} planned={stats.plans} written={stats.written}"
    )


def _run_stage_8(
    target_dir: Path,
    reports_dirs: list[Path],
    *,
    execute: bool,
    verbose: int,
) -> None:
    """Stage 8: rewrite wiki-links inside source reports."""
    if not reports_dirs:
        click.echo("\n[STAGE 8] SKIPPED — no --reports-dir provided.")
        return
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(
        f"\n[STAGE 8] resolve-links ({mode}) across {len(reports_dirs)} report dir(s)"
    )
    stats = s8_resolve_links.resolve_report_links(
        target_dir, reports_dirs, execute=execute, verbose=verbose >= 1,
    )
    click.echo(
        f"  scanned={stats.files_scanned} changed={stats.files_changed} "
        f"rewrites={stats.total_rewrites} unresolved={len(stats.unresolved)}"
    )


def _run_stage_9(target_dir: Path, *, execute: bool, verbose: int) -> None:
    """Stage 9: vault-wide wiki-link pipe-syntax normalization."""
    mode = "EXECUTE" if execute else "DRY-RUN"
    click.echo(f"\n[STAGE 9] normalize-links ({mode}) {target_dir}")
    stats = s9_normalize_links.normalize_notes(target_dir, execute=execute)
    click.echo(
        f"  scanned={stats.files_scanned} changed={stats.files_changed} "
        f"rewrites={stats.total_rewrites}"
    )


def _run_stage_10(
    target_dir: Path,
    output_dir: Path,
    *,
    fail_on_violation: bool,
) -> bool:
    """Stage 10: audit + gate enforcement. Returns True if gates passed."""
    click.echo(f"\n[STAGE 10] audit {target_dir} → {output_dir}")
    summary = s10_audit.run_audit_stage(
        target_dir, output_dir,
        fail_on_violation=False,  # surface the result via the return value
        write_markdown=True,
    )
    s10_audit.print_gate_summary(summary)
    if not summary.all_gates_passed and fail_on_violation:
        return False
    return True


# ═════════════════════════════════════════════════════════════════════════
# Stage selection
# ═════════════════════════════════════════════════════════════════════════

def _select_stage_range(to_stage: int | None, from_stage: int | None) -> list[int]:
    """Resolve --from/--to flags into the ordered list of stage numbers to run."""
    lo = from_stage if from_stage is not None else min(PIPELINE_STAGES)
    hi = to_stage if to_stage is not None else max(PIPELINE_STAGES)
    if lo > hi:
        raise click.BadParameter(f"--from-stage ({lo}) > --to-stage ({hi})")
    return [n for n in range(lo, hi + 1) if n in PIPELINE_STAGES]


def _stages_require_target_dir(stages: list[int]) -> bool:
    """True if any selected stage operates directly on the notes dir."""
    return bool({5, 6, 7, 8, 9, 10} & set(stages))


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--to-stage", type=int, default=None,
              help="Run stages 1..N inclusive (default: full pipeline).")
@click.option("--from-stage", type=int, default=None,
              help="Resume starting at stage N.")
# Workspace + per-stage dirs
@click.option("--workspace-dir", type=click.Path(path_type=Path), default=None,
              help="Root for intermediate artefacts (derives per-stage dirs).")
@click.option("--extracted-dir", type=click.Path(path_type=Path), default=None,
              help="Stage 1 output / Stage 2 input.")
@click.option("--validated-dir", type=click.Path(path_type=Path), default=None,
              help="Stage 2 output / Stage 3 input.")
@click.option("--consolidated-dir", type=click.Path(path_type=Path), default=None,
              help="Stage 3 output / Stage 5+6 input.")
@click.option("--match-output-dir", type=click.Path(path_type=Path), default=None,
              help="Stage 5 output (match-report + embedding cache).")
@click.option("--target-dir", type=click.Path(path_type=Path), default=None,
              help="Notes directory. Stage 6 output; Stages 7-10 input.")
@click.option("--audit-output-dir", type=click.Path(path_type=Path), default=None,
              help="Stage 10 report dir (default: <target-dir>/_audit).")
# Stage-specific inputs
@click.option("--reports-to-extract", type=click.Path(path_type=Path), multiple=True,
              help="Report directories for Stage 1. Repeatable.")
@click.option("--reports-dir", type=click.Path(path_type=Path), multiple=True,
              help="Report directories for Stage 8 link rewriting. Repeatable.")
# Modes
@click.option("--execute", is_flag=True,
              help="Apply changes (default: dry-run).")
@click.option("--rebuild", is_flag=True,
              help="[Phase 6] Delete --target-dir before running. Not yet enabled.")
@click.option("--strict-links", is_flag=True,
              help="Stage 2: fail on any garbage link.")
@click.option("--no-fail-gates", is_flag=True,
              help="Stage 10 reports gate results but does not fail the run.")
@click.option("--skip-stubs", is_flag=True,
              help="Skip Stage 7 (stub generation). WARNING: the resolution-rate "
                   "gate lift (~84%→97%) comes from stubs; expect "
                   "GATE_MIN_RESOLUTION_RATE to fail unless --no-fail-gates is set.")
@click.option("--llm-normalize", is_flag=True,
              help="Enable Stage 4 LLM normalization (not yet implemented).")
@click.option("--llm-synthesize", is_flag=True,
              help="Enable LLM synthesis pass (not yet implemented).")
@click.option("--incremental", is_flag=True,
              help="Skip stages whose inputs are unchanged (not yet implemented).")
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet", is_flag=True)
@click.version_option(__version__)
def main(  # noqa: PLR0912, PLR0913, PLR0915
    to_stage: int | None,
    from_stage: int | None,
    workspace_dir: Path | None,
    extracted_dir: Path | None,
    validated_dir: Path | None,
    consolidated_dir: Path | None,
    match_output_dir: Path | None,
    target_dir: Path | None,
    audit_output_dir: Path | None,
    reports_to_extract: tuple[Path, ...],
    reports_dir: tuple[Path, ...],
    execute: bool,
    rebuild: bool,
    strict_links: bool,
    no_fail_gates: bool,
    skip_stubs: bool,
    llm_normalize: bool,
    llm_synthesize: bool,
    incremental: bool,
    verbose: int,
    quiet: bool,
) -> int:
    """Orchestrate the v3 pipeline (stages 1-10; stage 4 opt-in LLM skipped)."""
    click.echo(f"pipeline_v3 v{__version__}")

    for flag, label in (
        (llm_normalize, "--llm-normalize"),
        (llm_synthesize, "--llm-synthesize"),
        (incremental, "--incremental"),
    ):
        if flag:
            click.echo(f"  NOTE: {label} is not yet wired; flag ignored.", err=True)

    stages_to_run = _select_stage_range(to_stage, from_stage)
    if skip_stubs and 7 in stages_to_run:
        stages_to_run = [n for n in stages_to_run if n != 7]
        click.echo("  NOTE: --skip-stubs → Stage 7 removed from run.", err=True)
    if not stages_to_run:
        click.echo("No stages selected.")
        return 0

    paths = _resolve_paths(
        workspace_dir,
        extracted=extracted_dir,
        validated=validated_dir,
        consolidated=consolidated_dir,
        match_out=match_output_dir,
        target=target_dir,
        audit_out=audit_output_dir,
    )
    if audit_output_dir is None and paths["target"] is not None and paths["audit"] is None:
        paths["audit"] = paths["target"] / "_audit"

    if _stages_require_target_dir(stages_to_run) and paths["target"] is None:
        click.echo(
            "ERROR: --target-dir (or --workspace-dir) is required for stages 5-10.",
            err=True,
        )
        return 2

    if rebuild:
        if not execute:
            click.echo("ERROR: --rebuild requires --execute.", err=True)
            return 2
        tgt = paths["target"]
        click.echo(
            f"\n[REBUILD] refusing to delete {tgt} — Phase 6 cutover gate is not yet open.",
            err=True,
        )
        return 2

    click.echo(f"\nStages:         {stages_to_run}")
    click.echo(f"Workspace:      {workspace_dir}")
    click.echo(f"  extracted:    {paths['extracted']}")
    click.echo(f"  validated:    {paths['validated']}")
    click.echo(f"  consolidated: {paths['consolidated']}")
    click.echo(f"  match:        {paths['match']}")
    click.echo(f"  target:       {paths['target']}")
    click.echo(f"  audit:        {paths['audit']}")
    click.echo(f"Mode:           {'EXECUTE' if execute else 'DRY-RUN'}")

    try:
        for n in stages_to_run:
            if n == 1:
                _run_stage_1(
                    list(reports_to_extract), paths["extracted"],
                    execute=execute, verbose=verbose,
                )
            elif n == 2:
                _run_stage_2(
                    paths["extracted"], paths["validated"],
                    execute=execute, strict_links=strict_links, verbose=verbose,
                )
            elif n == 3:
                _run_stage_3(
                    paths["validated"], paths["consolidated"],
                    execute=execute, verbose=verbose,
                )
            elif n == 5:
                _run_stage_5(
                    paths["consolidated"], paths["target"], paths["match"],
                    execute=execute, verbose=verbose,
                )
            elif n == 6:
                _run_stage_6(
                    paths["consolidated"], paths["target"],
                    execute=execute, verbose=verbose,
                )
            elif n == 7:
                _run_stage_7(paths["target"], execute=execute, verbose=verbose)
            elif n == 8:
                _run_stage_8(
                    paths["target"], list(reports_dir),
                    execute=execute, verbose=verbose,
                )
            elif n == 9:
                _run_stage_9(paths["target"], execute=execute, verbose=verbose)
            elif n == 10:
                ok = _run_stage_10(
                    paths["target"], paths["audit"],
                    fail_on_violation=not no_fail_gates,
                )
                if not ok:
                    click.echo(
                        "\nGate(s) failed. See audit-report.{json,md} for details.",
                        err=True,
                    )
                    return 6
    except KeyboardInterrupt:
        click.echo("\nInterrupted.", err=True)
        return 130
    except click.ClickException:
        raise
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
