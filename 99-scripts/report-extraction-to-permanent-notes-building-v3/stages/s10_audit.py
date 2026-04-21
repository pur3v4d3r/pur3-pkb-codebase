#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s10_audit.py — Stage 10: resolution audit + quality scoring + gate enforcement.

Wraps v2's ``audit_notes.run_audit`` and ``note_quality_scorer.score_all_notes``,
runs both against an arbitrary notes directory (sandbox or production), produces
a structured JSON report, and enforces the four spec §7.2 gates:

    1. Resolution rate            >= GATE_MIN_RESOLUTION_RATE         (default 0.95)
    2. Average quality score      >= GATE_MIN_AVG_QUALITY             (default 60)
    3. Low-quality note fraction  <= GATE_MAX_LOW_QUALITY_PCT         (default 5%)
       (notes scoring < GATE_LOW_QUALITY_THRESHOLD = 40)
    4. Missing-concepts list      <= MISSING_CONCEPTS_GATE            (default 200)

Exit codes:
    0   all gates pass
    1   uncaught error
    2   notes_dir missing
    4   bad arguments
    6   one or more gates failed
    130 KeyboardInterrupt

Usage:
    python -m stages.s10_audit --notes-dir _v3-output/phase-3-sandbox
    python -m stages.s10_audit --notes-dir _v3-output/phase-3-sandbox \
                                --output-dir _v3-output/runs/<run-id>
    python -m stages.s10_audit --notes-dir <dir> --markdown   # also write .md report
    python -m stages.s10_audit --notes-dir <dir> --no-fail    # report only, exit 0

Spec reference: §5 Phase 5 deliverable; §7.2 gates.

Version:
    1.0.0
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ─── sys.path so `python -m stages.s10_audit` and pytest both work ──────────
_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
_V2_DIR = _V3_ROOT.parent / "report-extraction-to-permanent-notes-building"
for _p in (_V3_ROOT, _V2_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import config_v3  # noqa: E402

# v2 imports — read-only function calls, no side effects on import
import audit_notes  # noqa: E402
import note_quality_scorer  # noqa: E402
from lib import link_validator  # noqa: E402


__version__ = "1.0.0"

logger = logging.getLogger(__name__)

# Spec §5 Phase 5 gate (lines 491-494). The other three (resolution rate,
# avg quality, low-quality fraction) come from config_v3.
MISSING_CONCEPTS_GATE: int = 200


# ═════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ═════════════════════════════════════════════════════════════════════════

class AuditError(Exception):
    """Base exception for s10_audit-specific errors."""


class GateFailure(AuditError):
    """Raised by ``enforce_gates`` when one or more gates fail."""


# ═════════════════════════════════════════════════════════════════════════
# Stub detection
# ═════════════════════════════════════════════════════════════════════════

_STUB_FRONTMATTER_MARKER = "source-type: stub-generation"


def _is_stub_note(filepath: Path) -> bool:
    """Return True if ``filepath`` is an auto-generated stub note.

    Stubs are identified by the ``source-type: stub-generation`` frontmatter
    field emitted by ``generate_stubs.build_stub_note``. We read at most the
    first 2 KiB of each file (frontmatter is always near the top).
    """
    try:
        with filepath.open("r", encoding="utf-8", errors="replace") as fh:
            head = fh.read(2048)
    except OSError:
        return False
    return _STUB_FRONTMATTER_MARKER in head


# ═════════════════════════════════════════════════════════════════════════
# Data types
# ═════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class GateResult:
    """Outcome of a single audit gate check."""
    name: str
    measured: float
    target: float
    comparator: str          # ">=" or "<="
    passed: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "measured": round(self.measured, 4),
            "target": round(self.target, 4),
            "comparator": self.comparator,
            "passed": self.passed,
        }


@dataclass
class AuditSummary:
    """Numerical summary of one audit run.

    Aggregates the most-load-bearing fields from ``audit_notes.AuditResult``
    and the per-note score list from ``note_quality_scorer``. Designed to be
    JSON-serializable.
    """
    notes_dir: str
    total_notes: int
    unique_targets: int
    resolved_targets: int
    unresolved_targets: int
    placeholder_targets: int
    report_targets: int
    missing_concepts: int
    real_missing_concepts: int
    resolution_rate: float
    orphan_count: int
    well_connected_count: int
    quality_avg: float
    quality_median: float
    quality_min: int
    quality_max: int
    low_quality_count: int
    low_quality_fraction: float
    low_quality_threshold: float
    # Non-stub partition (stubs identified by `source-type: stub-generation` in frontmatter)
    stub_count: int = 0
    non_stub_count: int = 0
    quality_avg_non_stub: float = 0.0
    quality_median_non_stub: float = 0.0
    gates: list[GateResult] = field(default_factory=list)

    @property
    def all_gates_passed(self) -> bool:
        return all(g.passed for g in self.gates) if self.gates else False

    def to_dict(self) -> dict[str, Any]:
        d = {k: v for k, v in self.__dict__.items() if k != "gates"}
        d["gates"] = [g.to_dict() for g in self.gates]
        d["all_gates_passed"] = self.all_gates_passed
        return d


# ═════════════════════════════════════════════════════════════════════════
# Core audit
# ═════════════════════════════════════════════════════════════════════════

def _percentile(values: list[float], pct: float) -> float:
    """Return the ``pct`` percentile of ``values`` via linear interpolation.

    Self-contained to avoid pulling in numpy at import time. ``values`` need
    not be sorted; this function copies and sorts internally.
    """
    if not values:
        return 0.0
    sv = sorted(values)
    if len(sv) == 1:
        return float(sv[0])
    pos = (len(sv) - 1) * pct / 100.0
    lo = int(pos)
    hi = min(lo + 1, len(sv) - 1)
    frac = pos - lo
    return float(sv[lo] * (1 - frac) + sv[hi] * frac)


def run_resolution_audit(notes_dir: Path) -> audit_notes.AuditResult:
    """Run v2's resolution audit and return the raw ``AuditResult``."""
    if not notes_dir.is_dir():
        raise AuditError(f"notes_dir does not exist or is not a directory: {notes_dir}")
    logger.info("Running resolution audit on %s", notes_dir)
    return audit_notes.run_audit(notes_dir=notes_dir)


def run_quality_audit(notes_dir: Path) -> list[note_quality_scorer.NoteScore]:
    """Run v2's quality scorer and return the per-note list."""
    if not notes_dir.is_dir():
        raise AuditError(f"notes_dir does not exist or is not a directory: {notes_dir}")
    logger.info("Running quality audit on %s", notes_dir)
    return note_quality_scorer.score_all_notes(notes_dir)


def summarize_audit(
    notes_dir: Path,
    audit: audit_notes.AuditResult,
    scores: list[note_quality_scorer.NoteScore],
    *,
    low_quality_threshold: float = config_v3.GATE_LOW_QUALITY_THRESHOLD,
) -> AuditSummary:
    """Combine raw audit + scores into an ``AuditSummary``.

    The resolution rate is computed as ``resolved / unique_targets`` to match
    v2's reporting convention; placeholder/report references count toward the
    denominator.
    """
    total_targets = audit.unique_targets
    resolved = len(audit.resolved)
    unresolved = len(audit.unresolved)
    resolution_rate = (resolved / total_targets) if total_targets else 0.0

    score_values = [float(s.total_score) for s in scores]
    if score_values:
        avg = sum(score_values) / len(score_values)
        med = _percentile(score_values, 50.0)
        smin = min(int(s.total_score) for s in scores)
        smax = max(int(s.total_score) for s in scores)
        low_count = sum(1 for s in scores if s.total_score < low_quality_threshold)
        low_frac = low_count / len(scores)
    else:
        avg = med = 0.0
        smin = smax = low_count = 0
        low_frac = 0.0

    # Stub vs non-stub partition. Stubs are scaffolding (auto-generated, intentionally
    # minimal); the avg-quality gate applies to *first-class* permanent notes only.
    stub_scores: list[float] = []
    non_stub_scores: list[float] = []
    for s in scores:
        if _is_stub_note(s.filepath):
            stub_scores.append(float(s.total_score))
        else:
            non_stub_scores.append(float(s.total_score))
    if non_stub_scores:
        avg_ns = sum(non_stub_scores) / len(non_stub_scores)
        med_ns = _percentile(non_stub_scores, 50.0)
    else:
        avg_ns = med_ns = 0.0

    # Spec §7.2: gate measures *real* missing concepts (validator-accepted),
    # so garbage links don't pollute the count.
    real_missing = sum(
        1 for name in audit.missing_concepts
        if link_validator.is_valid_concept(name)[0]
    )

    return AuditSummary(
        notes_dir=str(notes_dir),
        total_notes=audit.total_notes,
        unique_targets=total_targets,
        resolved_targets=resolved,
        unresolved_targets=unresolved,
        placeholder_targets=len(audit.placeholders),
        report_targets=len(audit.report_refs),
        missing_concepts=len(audit.missing_concepts),
        real_missing_concepts=real_missing,
        resolution_rate=resolution_rate,
        orphan_count=len(audit.orphans),
        well_connected_count=len(audit.well_connected),
        quality_avg=avg,
        quality_median=med,
        quality_min=smin,
        quality_max=smax,
        low_quality_count=low_count,
        low_quality_fraction=low_frac,
        low_quality_threshold=low_quality_threshold,
        stub_count=len(stub_scores),
        non_stub_count=len(non_stub_scores),
        quality_avg_non_stub=avg_ns,
        quality_median_non_stub=med_ns,
    )


# ═════════════════════════════════════════════════════════════════════════
# Gate enforcement
# ═════════════════════════════════════════════════════════════════════════

def evaluate_gates(
    summary: AuditSummary,
    *,
    min_resolution_rate: float = config_v3.GATE_MIN_RESOLUTION_RATE,
    min_avg_quality: float = config_v3.GATE_MIN_AVG_QUALITY,
    max_low_quality_pct: float = config_v3.GATE_MAX_LOW_QUALITY_PCT,
    max_missing_concepts: int = MISSING_CONCEPTS_GATE,
) -> list[GateResult]:
    """Compute the four §7.2 gate results without raising."""
    return [
        GateResult(
            name="resolution_rate",
            measured=summary.resolution_rate,
            target=min_resolution_rate,
            comparator=">=",
            passed=summary.resolution_rate >= min_resolution_rate,
        ),
        GateResult(
            # Spec §7.2: gate measures permanent notes only, excluding stubs which
            # are intentionally minimal scaffolding.
            name="avg_quality_non_stub",
            measured=summary.quality_avg_non_stub,
            target=min_avg_quality,
            comparator=">=",
            passed=summary.quality_avg_non_stub >= min_avg_quality,
        ),
        GateResult(
            name="low_quality_fraction",
            measured=summary.low_quality_fraction,
            target=max_low_quality_pct,
            comparator="<=",
            passed=summary.low_quality_fraction <= max_low_quality_pct,
        ),
        GateResult(
            name="missing_concepts",
            measured=float(summary.real_missing_concepts),
            target=float(max_missing_concepts),
            comparator="<=",
            passed=summary.real_missing_concepts <= max_missing_concepts,
        ),
    ]


def enforce_gates(summary: AuditSummary, *, fail_on_violation: bool = True) -> AuditSummary:
    """Attach gate results to ``summary``; raise ``GateFailure`` if any failed.

    Args:
        summary: Audit summary to enforce against.
        fail_on_violation: If True (default), raise ``GateFailure`` on any
            failed gate. If False, attach results and return without raising
            (for report-only mode).

    Returns:
        The same ``summary`` instance with ``gates`` populated.

    Raises:
        GateFailure: If ``fail_on_violation`` is True and any gate failed.
    """
    summary.gates = evaluate_gates(summary)
    failed = [g for g in summary.gates if not g.passed]
    if failed and fail_on_violation:
        names = ", ".join(g.name for g in failed)
        raise GateFailure(f"Gate(s) failed: {names}")
    return summary


# ═════════════════════════════════════════════════════════════════════════
# Reporting
# ═════════════════════════════════════════════════════════════════════════

def write_json_report(
    summary: AuditSummary,
    audit: audit_notes.AuditResult,
    output_dir: Path,
) -> Path:
    """Write a structured ``audit-report.json`` and return its path.

    Includes the summary plus the top-50 missing concepts and unresolved
    targets so downstream tooling can act without re-running the audit.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "audit-report.json"

    # Top-N missing concepts by reference frequency (matches v2 markdown report).
    missing_top = sorted(
        ((name, len(srcs)) for name, srcs in audit.missing_concepts.items()),
        key=lambda kv: -kv[1],
    )[:50]
    unresolved_top = sorted(
        ((name, len(srcs)) for name, srcs in audit.unresolved.items()),
        key=lambda kv: -kv[1],
    )[:50]

    payload = {
        "version": __version__,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": summary.to_dict(),
        "missing_concepts_top_50": [
            {"concept": name, "ref_count": count} for name, count in missing_top
        ],
        "unresolved_top_50": [
            {"target": name, "ref_count": count} for name, count in unresolved_top
        ],
    }
    out.write_text(json.dumps(payload, indent=2, sort_keys=False), encoding="utf-8")
    logger.info("Wrote JSON report: %s", out)
    return out


def write_markdown_report(
    summary: AuditSummary,
    audit: audit_notes.AuditResult,
    output_dir: Path,
) -> Path:
    """Write a human-readable ``audit-report.md``. Delegates to v2's renderer."""
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / "audit-report.md"
    body = audit_notes.generate_markdown_report(audit, top_n=50)
    # Prepend the gate verdict block so reviewers see pass/fail first.
    verdict = ["# Audit Report", "", f"**Notes dir:** `{summary.notes_dir}`", ""]
    verdict.append("## Gate Results")
    verdict.append("")
    verdict.append("| Gate | Measured | Target | Verdict |")
    verdict.append("|------|----------|--------|---------|")
    for g in summary.gates:
        v = "PASS" if g.passed else "FAIL"
        verdict.append(f"| {g.name} | {g.measured:.4f} | {g.comparator} {g.target:.4f} | **{v}** |")
    verdict.append("")
    out.write_text("\n".join(verdict) + "\n" + body, encoding="utf-8")
    logger.info("Wrote markdown report: %s", out)
    return out


def print_gate_summary(summary: AuditSummary) -> None:
    """Print a one-screen gate summary to stdout."""
    print("=" * 64)
    print(f"  AUDIT SUMMARY — {summary.notes_dir}")
    print("=" * 64)
    print(f"  Total notes:           {summary.total_notes}")
    print(f"  Unique link targets:   {summary.unique_targets}")
    print(f"  Resolved:              {summary.resolved_targets}")
    print(f"  Unresolved:            {summary.unresolved_targets}")
    print(f"  Missing concepts:      {summary.missing_concepts}")
    print(f"  Real missing (gate):   {summary.real_missing_concepts}")
    print(f"  Resolution rate:       {summary.resolution_rate * 100:.2f} %")
    print(f"  Quality avg:           {summary.quality_avg:.2f}")
    print(f"  Quality median:        {summary.quality_median:.2f}")
    print(f"  Stubs / non-stubs:     {summary.stub_count} / {summary.non_stub_count}")
    print(f"  Quality avg non-stub:  {summary.quality_avg_non_stub:.2f}  (gate)")
    print(f"  Low-quality (< {int(summary.low_quality_threshold)}):    "
          f"{summary.low_quality_count} ({summary.low_quality_fraction * 100:.2f} %)")
    print("-" * 64)
    print("  Gate                    Measured       Target    Verdict")
    print("-" * 64)
    for g in summary.gates:
        verdict = "PASS" if g.passed else "FAIL"
        print(f"  {g.name:<22s}  {g.measured:>10.4f}  {g.comparator} {g.target:>7.4f}    {verdict}")
    print("-" * 64)
    overall = "PASS" if summary.all_gates_passed else "FAIL"
    print(f"  OVERALL: {overall}")
    print("=" * 64)


# ═════════════════════════════════════════════════════════════════════════
# Orchestration
# ═════════════════════════════════════════════════════════════════════════

def run_audit_stage(
    notes_dir: Path,
    output_dir: Path,
    *,
    fail_on_violation: bool = True,
    write_markdown: bool = False,
) -> AuditSummary:
    """Full Stage 10 orchestration: audit + score + summarize + gate + report.

    Args:
        notes_dir: Directory of permanent notes to audit.
        output_dir: Where to write ``audit-report.json`` (and ``.md`` if
            ``write_markdown``).
        fail_on_violation: If True (default), raise ``GateFailure`` after
            writing the report when any gate fails. If False, write report
            and return without raising.
        write_markdown: Also write a markdown report using v2's renderer.

    Returns:
        The populated ``AuditSummary``.

    Raises:
        AuditError: If ``notes_dir`` is missing.
        GateFailure: If gates failed and ``fail_on_violation`` is True. The
            report is written *before* the exception is raised so it is
            always available for review.
    """
    audit = run_resolution_audit(notes_dir)
    scores = run_quality_audit(notes_dir)
    summary = summarize_audit(notes_dir, audit, scores)
    # Compute gates without raising so we always write the report.
    summary.gates = evaluate_gates(summary)
    write_json_report(summary, audit, output_dir)
    if write_markdown:
        write_markdown_report(summary, audit, output_dir)
    failed = [g for g in summary.gates if not g.passed]
    if failed and fail_on_violation:
        names = ", ".join(g.name for g in failed)
        raise GateFailure(f"Gate(s) failed: {names}")
    return summary


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="s10_audit",
        description="Stage 10: resolution audit + quality scoring + gate enforcement.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s10_audit --notes-dir _v3-output/phase-3-sandbox\n"
            "  python -m stages.s10_audit --notes-dir <dir> --output-dir _v3-output/runs/r1\n"
            "  python -m stages.s10_audit --notes-dir <dir> --markdown\n"
            "  python -m stages.s10_audit --notes-dir <dir> --no-fail   # report only\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--notes-dir", type=Path, required=True,
                        help="Directory of permanent notes to audit (required).")
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="Where to write audit-report.json (default: <notes-dir>/_audit).")
    parser.add_argument("--markdown", action="store_true",
                        help="Also write audit-report.md alongside the JSON.")
    parser.add_argument("--no-fail", action="store_true",
                        help="Report only; exit 0 even if gates fail (gates still recorded).")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Increase logging verbosity (-v INFO, -vv DEBUG).")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Suppress non-error output.")
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure root logger based on CLI verbosity flags."""
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
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    notes_dir: Path = args.notes_dir
    output_dir: Path = args.output_dir or (notes_dir / "_audit")

    try:
        summary = run_audit_stage(
            notes_dir,
            output_dir,
            fail_on_violation=False,  # always write report; we exit ourselves
            write_markdown=args.markdown,
        )
    except AuditError as e:
        logger.error("Audit failed: %s", e)
        return 2
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except Exception:
        logger.exception("Unexpected error")
        return 1

    if not args.quiet:
        print_gate_summary(summary)

    if summary.all_gates_passed:
        return 0
    if args.no_fail:
        logger.warning("Gates failed but --no-fail set; exiting 0.")
        return 0
    return 6


if __name__ == "__main__":
    sys.exit(main())
