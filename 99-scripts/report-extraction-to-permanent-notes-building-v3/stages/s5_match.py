#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s5_match.py — Stage 5: hybrid (string + embedding) matcher.

For every Stage-3 :class:`Candidate`, computes a hybrid similarity score
against every existing permanent note in ``--target-dir``::

    score = 0.4 * difflib.SequenceMatcher.ratio(name_a, name_b)
          + 0.6 * cosine(emb(text_a), emb(text_b))

Routes each candidate into one of three bands (per spec §2.1):

    score ≥ 0.92            → ``matched``      (auto-update existing note)
    0.78 ≤ score < 0.92     → ``review_queue`` (human or LLM decision)
    score < 0.78            → ``new``          (create new note)

Writes a JSON match-report to ``<output-dir>/match-report.json`` so the
caller (pipeline_v3) can drive Stage 6 routing without re-running Stage 5.

Replaces v2's ``note_matcher.py``.

Usage:
    python -m stages.s5_match \
        --candidates _v3-output/phase-2-gate/_consolidated-candidates.json \
        --target-dir _v3-output/phase-3-sandbox \
        --output-dir _v3-output/runs/<run-id> \
        [--cache _v3-output/embeddings/notes.npz] \
        [--no-gpu]

Exit codes:
    0  success
    1  unexpected error
    2  input file/dir not found
    3  permission denied
    4  MatchError
    130 SIGINT
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import numpy as np

# ── sys.path injection so `python -m stages.s5_match` and pytest both
#    resolve the sibling `lib/` package without packaging fuss.
_HERE = Path(__file__).resolve().parent
_V3_ROOT = _HERE.parent
if str(_V3_ROOT) not in sys.path:
    sys.path.insert(0, str(_V3_ROOT))

from lib.candidate import Candidate  # noqa: E402
from lib.embeddings import (  # noqa: E402
    DEFAULT_BATCH_SIZE,
    EMBEDDING_DIM,
    EmbeddingItem,
    EmbeddingStore,
    cache_key,
    cosine_similarity,
    load_model,
)
from lib.frontmatter import parse_frontmatter  # noqa: E402

logger = logging.getLogger(__name__)

__version__ = "3.0.0-phase4"

# ── Match thresholds (per spec §2.1) ────────────────────────────────────
AUTO_MATCH_THRESHOLD = 0.92
REVIEW_QUEUE_THRESHOLD = 0.78
STRING_WEIGHT = 0.4
COSINE_WEIGHT = 0.6


class MatchError(Exception):
    """Raised for matcher-specific failures (corrupt input, etc.)."""


# ─────────────────────────────────────────────────────────────────────────
# Existing-note ingestion
# ─────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class ExistingNote:
    """A permanent note already on disk that candidates may match against."""

    path: Path
    mtime: float
    title: str
    aliases: tuple[str, ...]

    @property
    def text(self) -> str:
        """Embedding input text — title + aliases joined."""
        if self.aliases:
            return f"{self.title} ({'; '.join(self.aliases)})"
        return self.title

    @property
    def cache_key(self) -> str:
        return cache_key(self.path, self.mtime, self.title, self.aliases)


def load_existing_notes(target_dir: Path) -> list[ExistingNote]:
    """Scan ``target_dir`` for ``*.md`` notes and parse minimal frontmatter.

    Notes without parseable frontmatter are still indexed using the filename
    stem as the title (so the matcher can still surface a candidate).
    """
    if not target_dir.exists():
        return []
    out: list[ExistingNote] = []
    for path in sorted(target_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as e:
            logger.warning("Could not read %s: %s", path, e)
            continue
        fm, _body = parse_frontmatter(text)
        title = str(fm.get("title") or path.stem).strip()
        aliases_raw = fm.get("aliases") or []
        aliases = tuple(str(a).strip() for a in aliases_raw if str(a).strip())
        out.append(ExistingNote(
            path=path,
            mtime=path.stat().st_mtime,
            title=title,
            aliases=aliases,
        ))
    return out


# ─────────────────────────────────────────────────────────────────────────
# Candidate adapter
# ─────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class CandidateProbe:
    """The minimal projection of a Candidate used by the matcher."""

    primary_name: str
    aliases: tuple[str, ...]

    @classmethod
    def from_candidate(cls, c: Candidate) -> CandidateProbe:
        return cls(primary_name=c.primary_name, aliases=tuple(c.aliases))

    @property
    def text(self) -> str:
        if self.aliases:
            return f"{self.primary_name} ({'; '.join(self.aliases)})"
        return self.primary_name

    @property
    def cache_key(self) -> str:
        # Candidates have no filepath/mtime — synthesize a stable key from text.
        return cache_key("__candidate__", 0.0, self.primary_name, self.aliases)


# ─────────────────────────────────────────────────────────────────────────
# Scoring
# ─────────────────────────────────────────────────────────────────────────

def string_similarity(a: str, b: str) -> float:
    """Case-insensitive ``SequenceMatcher.ratio`` in [0, 1]."""
    return SequenceMatcher(None, a.casefold(), b.casefold()).ratio()


def hybrid_score(string_sim: float, cosine_sim: float) -> float:
    """Hybrid score per spec §2.1: ``0.4*string + 0.6*cosine``, clamped to [0, 1]."""
    s = STRING_WEIGHT * float(string_sim) + COSINE_WEIGHT * float(cosine_sim)
    return float(max(0.0, min(1.0, s)))


def classify(score: float) -> str:
    """Return one of ``"matched"``, ``"review_queue"``, ``"new"``."""
    if score >= AUTO_MATCH_THRESHOLD:
        return "matched"
    if score >= REVIEW_QUEUE_THRESHOLD:
        return "review_queue"
    return "new"


# ─────────────────────────────────────────────────────────────────────────
# Match decision
# ─────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class MatchDecision:
    """One candidate's routing decision."""

    candidate_name: str
    status: str  # matched | review_queue | new
    score: float
    string_sim: float
    cosine_sim: float
    matched_path: str | None  # filename of best existing note (if any)
    matched_title: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_name": self.candidate_name,
            "status": self.status,
            "score": round(self.score, 4),
            "string_sim": round(self.string_sim, 4),
            "cosine_sim": round(self.cosine_sim, 4),
            "matched_path": self.matched_path,
            "matched_title": self.matched_title,
        }


@dataclass
class MatchStats:
    """Aggregate stats for a Stage-5 run."""

    candidates_total: int = 0
    existing_notes: int = 0
    by_status: Counter[str] = field(default_factory=Counter)
    encoded_existing: int = 0
    encoded_candidates: int = 0
    elapsed_seconds: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidates_total": self.candidates_total,
            "existing_notes": self.existing_notes,
            "by_status": dict(self.by_status),
            "encoded_existing": self.encoded_existing,
            "encoded_candidates": self.encoded_candidates,
            "elapsed_seconds": round(self.elapsed_seconds, 3),
        }


# ─────────────────────────────────────────────────────────────────────────
# Core matcher
# ─────────────────────────────────────────────────────────────────────────

def match_candidates(
    candidates: Sequence[Candidate],
    existing: Sequence[ExistingNote],
    *,
    store: EmbeddingStore,
    model: Any,
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> tuple[list[MatchDecision], MatchStats]:
    """Compute hybrid scores and route each candidate.

    Encodes any missing keys into ``store`` (caller decides whether to save).
    Returns ``(decisions, stats)`` in candidate order.
    """
    stats = MatchStats(
        candidates_total=len(candidates),
        existing_notes=len(existing),
    )

    # Encode any missing existing-note vectors.
    existing_items = [EmbeddingItem(key=n.cache_key, text=n.text) for n in existing]
    stats.encoded_existing = store.encode_missing(existing_items, model, batch_size=batch_size)

    # Encode any missing candidate vectors.
    probes = [CandidateProbe.from_candidate(c) for c in candidates]
    cand_items = [EmbeddingItem(key=p.cache_key, text=p.text) for p in probes]
    stats.encoded_candidates = store.encode_missing(cand_items, model, batch_size=batch_size)

    if not existing:
        # No pre-existing notes → every candidate is "new" by definition.
        decisions = [
            MatchDecision(
                candidate_name=p.primary_name,
                status="new",
                score=0.0,
                string_sim=0.0,
                cosine_sim=0.0,
                matched_path=None,
                matched_title=None,
            )
            for p in probes
        ]
        for d in decisions:
            stats.by_status[d.status] += 1
        return decisions, stats

    # Build the existing-note matrix once.
    existing_keys = [n.cache_key for n in existing]
    existing_matrix = store.vectors_for(existing_keys)

    decisions: list[MatchDecision] = []
    for p in probes:
        cand_vec = store.vector_for(p.cache_key)
        if cand_vec is None:
            raise MatchError(f"missing cache entry for candidate: {p.primary_name}")

        # Cosine over the full existing matrix in one shot.
        cosines = cosine_similarity(cand_vec, existing_matrix)[0]  # shape (N,)

        # String similarity is cheap; compute over all existing notes (titles only).
        string_sims = np.array(
            [string_similarity(p.primary_name, n.title) for n in existing],
            dtype=np.float32,
        )

        scores = STRING_WEIGHT * string_sims + COSINE_WEIGHT * cosines.astype(np.float32)
        np.clip(scores, 0.0, 1.0, out=scores)

        best_idx = int(np.argmax(scores))
        best_score = float(scores[best_idx])
        best = existing[best_idx]
        status = classify(best_score)

        decisions.append(MatchDecision(
            candidate_name=p.primary_name,
            status=status,
            score=best_score,
            string_sim=float(string_sims[best_idx]),
            cosine_sim=float(cosines[best_idx]),
            matched_path=best.path.name if status != "new" else None,
            matched_title=best.title if status != "new" else None,
        ))
        stats.by_status[status] += 1

    return decisions, stats


# ─────────────────────────────────────────────────────────────────────────
# Report writer
# ─────────────────────────────────────────────────────────────────────────

def write_report(
    decisions: Sequence[MatchDecision],
    stats: MatchStats,
    output_dir: Path,
) -> Path:
    """Write ``match-report.json`` to ``output_dir`` and return its path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "version": __version__,
        "stats": stats.to_dict(),
        "thresholds": {
            "auto_match": AUTO_MATCH_THRESHOLD,
            "review_queue": REVIEW_QUEUE_THRESHOLD,
            "string_weight": STRING_WEIGHT,
            "cosine_weight": COSINE_WEIGHT,
        },
        "decisions": [d.to_dict() for d in decisions],
    }
    out = output_dir / "match-report.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


# ─────────────────────────────────────────────────────────────────────────
# Orchestration
# ─────────────────────────────────────────────────────────────────────────

def _load_candidates(path: Path) -> list[Candidate]:
    """Load candidates from a Stage-3 ``_consolidated-candidates.json`` file."""
    if not path.exists():
        raise FileNotFoundError(f"candidates file not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    cand_dicts = data.get("candidates")
    if not isinstance(cand_dicts, list):
        raise MatchError(f"{path} missing 'candidates' list")
    return [Candidate.from_dict(d) for d in cand_dicts]


def run_match(
    candidates_path: Path,
    target_dir: Path,
    output_dir: Path,
    *,
    cache_path: Path | None = None,
    device: str | None = None,
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> MatchStats:
    """High-level orchestration used by both the CLI and pipeline_v3."""
    t0 = time.perf_counter()
    candidates = _load_candidates(candidates_path)
    existing = load_existing_notes(target_dir)
    cache = cache_path or (output_dir / "embeddings.npz")
    store = EmbeddingStore.load(cache, dim=EMBEDDING_DIM)

    model = load_model(device=device)
    decisions, stats = match_candidates(
        candidates, existing, store=store, model=model, batch_size=batch_size,
    )
    store.save()

    write_report(decisions, stats, output_dir)
    stats.elapsed_seconds = time.perf_counter() - t0
    return stats


# ─────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """Build the argparse parser for ``s5_match``."""
    parser = argparse.ArgumentParser(
        prog="s5_match",
        description="Stage 5: hybrid string+embedding matcher for Stage-3 candidates.",
        epilog=(
            "Examples:\n"
            "  python -m stages.s5_match \\\n"
            "      --candidates _v3-output/phase-2-gate/_consolidated-candidates.json \\\n"
            "      --target-dir _v3-output/phase-3-sandbox \\\n"
            "      --output-dir _v3-output/runs/test-1\n"
            "  python -m stages.s5_match ... --no-gpu     # force CPU encoding\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--candidates", type=Path, required=True,
                        help="path to _consolidated-candidates.json from Stage 3")
    parser.add_argument("--target-dir", type=Path, required=True,
                        help="directory containing existing permanent notes")
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="directory to write match-report.json into")
    parser.add_argument("--cache", type=Path, default=None,
                        help="path to embeddings .npz cache (default: <output-dir>/embeddings.npz)")
    parser.add_argument("--no-gpu", action="store_true",
                        help="force CPU encoding (default: use CUDA when available)")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
                        help=f"encoding batch size (default {DEFAULT_BATCH_SIZE})")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-q", "--quiet", action="store_true")
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure root logger based on verbosity flags."""
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
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        stats = run_match(
            args.candidates,
            args.target_dir,
            args.output_dir,
            cache_path=args.cache,
            device="cpu" if args.no_gpu else None,
            batch_size=args.batch_size,
        )
        logger.warning(
            "Done. candidates=%d  existing=%d  matched=%d  review=%d  new=%d  encoded(e/c)=%d/%d  %.2fs",
            stats.candidates_total,
            stats.existing_notes,
            stats.by_status.get("matched", 0),
            stats.by_status.get("review_queue", 0),
            stats.by_status.get("new", 0),
            stats.encoded_existing,
            stats.encoded_candidates,
            stats.elapsed_seconds,
        )
        return 0
    except FileNotFoundError as e:
        logger.error("Input not found: %s", e)
        return 2
    except PermissionError as e:
        logger.error("Permission denied: %s", e)
        return 3
    except MatchError as e:
        logger.error("Match error: %s", e)
        return 4
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except Exception:
        logger.exception("Unexpected error")
        return 1


if __name__ == "__main__":
    sys.exit(main())

