#!/usr/bin/env python3
"""
batch_tracker.py — Diff-Aware Batch Processing Tracker
═══════════════════════════════════════════════════════════════════════════════
Tracks which report directories have been fully processed by the pipeline,
enabling diff-aware runs that skip already-processed content.

USAGE:
  from batch_tracker import mark_batch_processed, is_batch_processed, get_all_processed

  # After successful extraction of a directory:
  mark_batch_processed(report_dir, batch_name="2026-01-15-cognitive-psychology")

  # Check before re-processing:
  if not is_batch_processed(report_dir):
      run_extraction(report_dir)

  python batch_tracker.py                    # Show all tracked batches
  python batch_tracker.py --reset            # Clear all tracking data

REQUIRES: Python 3.10+ (stdlib only)
"""

import json
import sys
import argparse
import datetime
from pathlib import Path
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent))

from config import EXTRACTOR_OUTPUT_ROOT

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

PIPELINE_OUTPUT_DIR = Path(__file__).parent / "_pipeline-output"
TRACKER_FILE = PIPELINE_OUTPUT_DIR / "_processed-batches.json"


# ══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class BatchRecord:
    """Record of a processed batch."""
    dir_name: str
    batch_name: str
    processed_at: str
    note_count: int = 0
    status: str = "complete"


# ══════════════════════════════════════════════════════════════════════════════
# CORE FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def _load_tracker() -> dict:
    """Load tracker data from disk."""
    if TRACKER_FILE.exists():
        try:
            return json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"processed_dirs": [], "batches": []}


def _save_tracker(data: dict) -> None:
    """Persist tracker data to disk."""
    TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKER_FILE.write_text(
        json.dumps(data, indent=2, default=str), encoding="utf-8"
    )


def mark_batch_processed(report_dir: Path,
                         batch_name: str = "",
                         note_count: int = 0) -> None:
    """
    Mark a report directory as fully processed.

    Args:
        report_dir: The report directory that was extracted.
        batch_name: The extraction batch name (if known).
        note_count: Number of notes produced from this batch.
    """
    data = _load_tracker()
    dir_name = report_dir.name

    # Add to processed_dirs set (for discover_unprocessed compatibility)
    if dir_name not in data["processed_dirs"]:
        data["processed_dirs"].append(dir_name)

    # Add detailed record
    record = BatchRecord(
        dir_name=dir_name,
        batch_name=batch_name or dir_name,
        processed_at=datetime.datetime.now().isoformat(),
        note_count=note_count,
        status="complete",
    )

    # Replace existing record for same dir, or append
    batches = data.get("batches", [])
    batches = [b for b in batches if b.get("dir_name") != dir_name]
    batches.append(asdict(record))
    data["batches"] = batches

    _save_tracker(data)


def is_batch_processed(report_dir: Path) -> bool:
    """Check if a report directory has already been processed."""
    data = _load_tracker()
    return report_dir.name in data.get("processed_dirs", [])


def get_all_processed() -> list[dict]:
    """Return all processed batch records."""
    data = _load_tracker()
    return data.get("batches", [])


def reset_tracker() -> None:
    """Clear all tracking data."""
    _save_tracker({"processed_dirs": [], "batches": []})


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="View and manage the batch processing tracker"
    )
    parser.add_argument("--reset", action="store_true", default=False,
                        help="Clear all tracking data")
    args = parser.parse_args()

    if args.reset:
        reset_tracker()
        print("  Tracker reset. All batch records cleared.")
        return

    records = get_all_processed()
    if not records:
        print("  No batches have been tracked yet.")
        return

    print("=" * 72)
    print("  PROCESSED BATCH TRACKER")
    print("=" * 72)
    print(f"\n  Total tracked: {len(records)}\n")

    for rec in records:
        status = rec.get("status", "?")
        emoji = "✅" if status == "complete" else "⚠️"
        print(f"  {emoji} {rec.get('dir_name', '?')}")
        print(f"     Batch:  {rec.get('batch_name', '?')}")
        print(f"     Time:   {rec.get('processed_at', '?')}")
        print(f"     Notes:  {rec.get('note_count', '?')}")
        print()

    print(f"{'=' * 72}")


if __name__ == "__main__":
    main()
