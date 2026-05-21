#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pdf_to_markdown_pipeline.py — Four-phase PDF → Obsidian Markdown pipeline.

Converts a corpus of academic PDFs to structured Obsidian Markdown files using
Marker for raw conversion and a local Qwen LLM for YAML frontmatter generation.

Phases:
  dedupe   : (Optional) Hash-based duplicate detection — report only, no deletes
  triage   : Classify each PDF as "digital" (extractable text) or "scanned"
  convert  : Batch-convert digital PDFs via marker_single (GPU-accelerated)
  enrich   : Prepend LLM-generated YAML frontmatter to each Markdown file
  all      : Run triage → convert → enrich in sequence (recommended)

Usage:
    # Full pipeline — recommended first run
    python pdf_to_markdown_pipeline.py --phase all -v

    # Dry-run to preview what will happen without writing anything
    python pdf_to_markdown_pipeline.py --phase all --dry-run -v

    # Test on just 5 PDFs before committing to the full corpus
    python pdf_to_markdown_pipeline.py --phase all --limit 5 -v

    # Triage only (fast: ~5 min for 1000 PDFs)
    python pdf_to_markdown_pipeline.py --phase triage -v

    # Convert with 2 parallel workers (RTX 4090 can handle it)
    python pdf_to_markdown_pipeline.py --phase convert -w 2

    # Resume an interrupted run (skips already-completed files)
    python pdf_to_markdown_pipeline.py --phase all --resume -v

    # Find duplicate PDFs in the corpus
    python pdf_to_markdown_pipeline.py --phase dedupe -v

Version:
    1.0.0

Python:
    >=3.10

Dependencies:
    stdlib:      argparse, concurrent.futures, dataclasses, datetime, hashlib,
                 json, logging, pathlib, re, shutil, subprocess, sys
    third-party: pymupdf (fitz), ollama

Author:
    PDF-to-Markdown Pipeline v1.0.0
"""
from __future__ import annotations

# ─── Standard library ────────────────────────────────────────────────────────
import argparse
import concurrent.futures
import hashlib
import json
import logging
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Literal

# ─── Third-party (validated at runtime via preflight()) ──────────────────────
try:
    import fitz  # PyMuPDF
    _FITZ_OK = True
except ImportError:
    _FITZ_OK = False

try:
    import ollama as _ollama_lib
    _OLLAMA_OK = True
except ImportError:
    _ollama_lib = None  # type: ignore[assignment]
    _OLLAMA_OK = False


# ═════════════════════════════════════════════════════════════════════════════
# Module-level constants
# ═════════════════════════════════════════════════════════════════════════════

__version__ = "1.0.0"

# ── Default paths ──────────────────────────────────────────────────────────
_VAULT = Path(r"D:\10_pur3v4d3r's-vault")

DEFAULT_PDF_DIR: Path = (
    _VAULT / "999-v4d3r" / "__prompt-engineering-guidance"
    / "research-papers" / "pdf"
)
DEFAULT_OUTPUT_DIR: Path = _VAULT / "999-report-organizing" / "pdf-to-markdown"
DEFAULT_LOG_DIR: Path = _VAULT / "99-scripts"

# ── Conversion defaults ────────────────────────────────────────────────────
DEFAULT_WORKERS: int = 1            # Parallel marker_single workers
DEFAULT_BATCH_MULTIPLIER: int = 2   # legacy; kept for log banner compat
DEFAULT_LAYOUT_BATCH_SIZE: int = 8  # pages processed in parallel by layout model (RTX 4090: 8–16 safe)
DEFAULT_DETECTION_BATCH_SIZE: int = 8  # pages processed in parallel by detection model
DEFAULT_DISABLE_OCR: bool = True    # skip OCR for digital PDFs (set False for scanned)
DEFAULT_DISABLE_IMAGES: bool = False  # keep extracted figures (per-paper folder keeps 12k imgs organised)
DEFAULT_MODEL: str = "qwen2.5:14b-instruct-q5_K_M"

# ── Triage threshold ───────────────────────────────────────────────────────
# PDFs with fewer extractable chars on page-0 are classified as "scanned"
SCANNED_TEXT_THRESHOLD: int = 100

# ── LLM context window budget ─────────────────────────────────────────────
LLM_CONTEXT_CHARS: int = 5_500   # First N chars of converted .md fed to LLM
LLM_TEMPERATURE: float = 0.15    # Low temperature = deterministic YAML output

# ── Log file names ─────────────────────────────────────────────────────────
_LOG_DEDUPE    = "pdf_pipeline_dedupe.json"
_LOG_TRIAGE    = "pdf_pipeline_triage.json"
_LOG_CONVERT   = "pdf_pipeline_convert.json"
_LOG_ENRICH    = "pdf_pipeline_enrich.json"

# ── Fallback marker_single path (if not in PATH) ──────────────────────────
_MARKER_FALLBACK = Path(
    r"C:\Users\pur3v4d3rpk\AppData\Local\Programs"
    r"\Python\Python313\Scripts\marker_single.exe"
)


# ═════════════════════════════════════════════════════════════════════════════
# Logging
# ═════════════════════════════════════════════════════════════════════════════

logger = logging.getLogger(__name__)


# ═════════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ═════════════════════════════════════════════════════════════════════════════

class PipelineError(Exception):
    """Base exception for pipeline-specific failures."""


class MarkerNotFoundError(PipelineError):
    """Raised when the marker_single executable cannot be located."""


class OllamaCallError(PipelineError):
    """Raised when the Ollama LLM call fails or returns empty output."""


# ═════════════════════════════════════════════════════════════════════════════
# Data types
# ═════════════════════════════════════════════════════════════════════════════

@dataclass
class ConversionResult:
    """Outcome of a single PDF → Markdown conversion attempt."""
    pdf_path: Path
    md_path: Path | None
    status: Literal["success", "failed", "skipped"]
    error: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "pdf_path": str(self.pdf_path),
            "md_path": str(self.md_path) if self.md_path else None,
            "status": self.status,
            "error": self.error,
            "timestamp": self.timestamp,
        }


@dataclass
class EnrichResult:
    """Outcome of a single Markdown enrichment (YAML frontmatter) attempt."""
    md_path: Path
    status: Literal["success", "failed", "skipped"]
    error: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "md_path": str(self.md_path),
            "status": self.status,
            "error": self.error,
            "timestamp": self.timestamp,
        }


# ═════════════════════════════════════════════════════════════════════════════
# Shared utilities
# ═════════════════════════════════════════════════════════════════════════════

def load_log(log_path: Path) -> list[dict]:
    """Load a JSON log file; return empty list if missing or corrupt.

    Args:
        log_path: Path to the JSON log file.

    Returns:
        Parsed list of log entries, or [] on any read/parse error.
    """
    if not log_path.exists():
        return []
    try:
        return json.loads(log_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Could not read log %s: %s", log_path, exc)
        return []


def save_log(log_path: Path, data: list[dict], dry_run: bool = False) -> None:
    """Persist a JSON log file via atomic write-rename.

    Args:
        log_path: Destination path.
        data: List of dicts to serialise.
        dry_run: If True, skip writing.
    """
    if dry_run:
        return
    log_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = log_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(log_path)


def slugify(text: str, max_len: int = 80) -> str:
    """Convert arbitrary text to a filesystem-safe, lowercase slug.

    Args:
        text: Input string.
        max_len: Maximum output length.

    Returns:
        A slug string safe for file IDs.

    Example:
        >>> slugify("Chain-of-Thought Prompting (2022)")
        'chain_of_thought_prompting__2022_'
    """
    slug = re.sub(r"[^\w\-]", "_", text.lower())
    return slug[:max_len]


def find_marker_output(output_dir: Path, pdf_stem: str) -> Path | None:
    """Locate the Markdown file produced by marker_single for a given PDF stem.

    marker_single creates: <output_dir>/<pdf_stem>/<pdf_stem>.md

    Args:
        output_dir: The root output directory passed to marker_single.
        pdf_stem: Stem of the source PDF (filename without .pdf).

    Returns:
        Path to the .md file if found, otherwise None.
    """
    # Primary expected location
    primary = output_dir / pdf_stem / f"{pdf_stem}.md"
    if primary.exists():
        return primary

    # Fallback: search subdirectory for any .md
    sub_dir = output_dir / pdf_stem
    if sub_dir.is_dir():
        candidates = [p for p in sub_dir.glob("*.md") if ".original" not in p.name]
        if candidates:
            return candidates[0]

    # Last resort: direct child .md (some marker versions write here)
    direct = output_dir / f"{pdf_stem}.md"
    if direct.exists():
        return direct

    return None


# ═════════════════════════════════════════════════════════════════════════════
# Phase 0: Deduplication (optional, report only — no files deleted)
# ═════════════════════════════════════════════════════════════════════════════

def _hash_file(path: Path, chunk_size: int = 65_536) -> str:
    """Compute MD5 hash of a file using buffered reads.

    Args:
        path: File to hash.
        chunk_size: Read buffer in bytes (default 64 KB).

    Returns:
        Hexadecimal MD5 digest.

    Raises:
        OSError: If the file cannot be opened or read.
    """
    hasher = hashlib.md5()
    with path.open("rb") as fh:
        while chunk := fh.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()


def deduplicate_corpus(
    pdf_dir: Path,
    log_path: Path,
    dry_run: bool = False,
) -> dict[str, list[Path]]:
    """Identify duplicate PDFs by content hash.

    This phase is report-only — it never deletes or moves files.
    Review the generated log to decide which duplicates to remove manually.

    Args:
        pdf_dir: Directory containing source PDFs.
        log_path: Where to write the JSON deduplication report.
        dry_run: If True, print findings but skip writing the report.

    Returns:
        Dict mapping MD5 hash to list of duplicate paths.
        Only hashes with more than one file are included.
    """
    logger.info("Phase 0 (dedupe): scanning %s", pdf_dir)
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    logger.info("  Found %d PDFs total", len(pdfs))

    hashes: dict[str, list[Path]] = defaultdict(list)
    for i, pdf in enumerate(pdfs, 1):
        try:
            h = _hash_file(pdf)
            hashes[h].append(pdf)
        except OSError as exc:
            logger.warning("  Cannot hash %s: %s", pdf.name, exc)
        if i % 200 == 0:
            logger.info("  Hashed %d/%d…", i, len(pdfs))

    duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    redundant_count = sum(len(v) - 1 for v in duplicates.values())
    logger.info(
        "  Dedup result: %d duplicate groups → %d redundant files",
        len(duplicates),
        redundant_count,
    )

    if not dry_run:
        report = [
            {
                "hash": h,
                "canonical": str(paths[0]),
                "duplicates": [str(p) for p in paths[1:]],
            }
            for h, paths in duplicates.items()
        ]
        save_log(log_path, report)
        logger.info("  Dedup report → %s", log_path)

    return duplicates


# ═════════════════════════════════════════════════════════════════════════════
# Phase 1: Triage (digital vs scanned)
# ═════════════════════════════════════════════════════════════════════════════

def _classify_pdf(pdf_path: Path) -> Literal["digital", "scanned"]:
    """Classify a single PDF as digitally-born or scanned.

    Extracts text from the first page and compares character count against
    SCANNED_TEXT_THRESHOLD. Near-zero text = scanned (OCR required).

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        "digital" if text is extractable, otherwise "scanned".

    Raises:
        Exception: Any fitz error (corrupt PDF, encrypted, etc.).
    """
    doc = fitz.open(str(pdf_path))  # type: ignore[name-defined]
    try:
        page = doc[0]
        text = page.get_text()
        return "digital" if len(text.strip()) >= SCANNED_TEXT_THRESHOLD else "scanned"
    finally:
        doc.close()


def triage_corpus(
    pdf_dir: Path,
    log_path: Path,
    limit: int = 0,
    resume: bool = False,
    dry_run: bool = False,
    filter_terms: list[str] | None = None,
) -> tuple[list[Path], list[Path]]:
    """Classify all PDFs as "digital" or "scanned".

    Digital PDFs have extractable text and go to Phase 2 (Marker conversion).
    Scanned PDFs are logged for manual review / vision-LLM processing later.

    Args:
        pdf_dir: Directory containing source PDFs.
        log_path: Path to write/read the triage JSON log.
        limit: If > 0, process at most this many PDFs (useful for testing).
        resume: If True, skip PDFs already classified in an existing log.
        dry_run: Classify but do not write the log.
        filter_terms: If provided, only include PDFs whose filename stem contains
            at least one term (case-insensitive OR match).  Applied before limit.

    Returns:
        (digital_paths, scanned_paths) — lists of Path objects.
    """
    logger.info("Phase 1 (triage): classifying PDFs in %s", pdf_dir)
    all_pdfs = sorted(pdf_dir.glob("*.pdf"))

    if filter_terms:
        terms_lower = [t.lower() for t in filter_terms]
        all_pdfs = [p for p in all_pdfs if any(t in p.stem.lower() for t in terms_lower)]
        logger.info(
            "  --filter applied (%s): %d PDFs match",
            ", ".join(filter_terms), len(all_pdfs),
        )

    if limit > 0:
        all_pdfs = all_pdfs[:limit]
        logger.info("  --limit %d applied; processing %d PDFs", limit, len(all_pdfs))
    else:
        logger.info("  Found %d PDFs to classify", len(all_pdfs))

    # Build resume lookup from existing log
    already_done: dict[str, str] = {}
    if resume:
        for entry in load_log(log_path):
            already_done[entry["path"]] = entry["category"]
        logger.info("  Resume: %d already classified", len(already_done))

    log_data: list[dict] = list(load_log(log_path)) if resume else []
    digital: list[Path] = []
    scanned: list[Path] = []

    for i, pdf in enumerate(all_pdfs, 1):
        key = str(pdf)

        if resume and key in already_done:
            cat = already_done[key]
            (digital if cat == "digital" else scanned).append(pdf)
            continue

        try:
            cat = _classify_pdf(pdf)
        except Exception as exc:
            logger.warning("  [%d/%d] classify failed for %s: %s", i, len(all_pdfs), pdf.name, exc)
            # Treat unreadable PDFs conservatively as scanned
            cat = "scanned"

        (digital if cat == "digital" else scanned).append(pdf)
        log_data.append({"path": key, "category": cat})

        if i % 100 == 0:
            logger.info(
                "  [%d/%d] digital=%d, scanned=%d",
                i, len(all_pdfs), len(digital), len(scanned),
            )

    logger.info(
        "  Triage complete: %d digital, %d scanned",
        len(digital), len(scanned),
    )

    save_log(log_path, log_data, dry_run=dry_run)
    if not dry_run:
        logger.info("  Triage log → %s", log_path)

    return digital, scanned


# ═════════════════════════════════════════════════════════════════════════════
# Phase 2: Batch conversion via marker_single
# ═════════════════════════════════════════════════════════════════════════════

def _find_marker() -> str:
    """Locate the marker_single executable.

    Checks PATH first, then falls back to the known system-Python location.

    Returns:
        Full path string to marker_single.

    Raises:
        MarkerNotFoundError: If marker_single cannot be found anywhere.
    """
    found = shutil.which("marker_single")
    if found:
        return found
    if _MARKER_FALLBACK.exists():
        return str(_MARKER_FALLBACK)
    raise MarkerNotFoundError(
        "marker_single not found in PATH or at "
        f"{_MARKER_FALLBACK}. Install with: pip install marker-pdf"
    )


def _convert_single_pdf(
    pdf_path: Path,
    output_dir: Path,
    batch_multiplier: int,
    dry_run: bool,
    layout_batch_size: int = DEFAULT_LAYOUT_BATCH_SIZE,
    detection_batch_size: int = DEFAULT_DETECTION_BATCH_SIZE,
    disable_ocr: bool = DEFAULT_DISABLE_OCR,
    disable_images: bool = DEFAULT_DISABLE_IMAGES,
) -> ConversionResult:
    """Convert one PDF to Markdown using marker_single.

    marker_single output layout:
        <output_dir>/<pdf_stem>/<pdf_stem>.md

    Args:
        pdf_path: Source PDF file.
        output_dir: Root directory for all Markdown output.
        batch_multiplier: Unused in marker v1.x; kept for signature compat.
        dry_run: If True, skip conversion and return a "skipped" result.
        layout_batch_size: Pages processed in parallel by the layout model.
            RTX 4090 (24 GB VRAM): 8–16 is safe.  Default 8.
        detection_batch_size: Pages processed in parallel by the detection
            model.  RTX 4090: 8–16 is safe.  Default 8.
        disable_ocr: If True, pass --disable_ocr to skip the Surya OCR model.
            Safe for digital PDFs where text is already embedded.  Speeds up
            conversion by ~40–60 %%.  Set False only for scanned documents.
        disable_images: If True, pass --disable_image_extraction to suppress
            JPEG output.  Default False — images stay alongside each paper's
            .md in its own subfolder, which is manageable in Obsidian.

    Returns:
        ConversionResult describing the outcome.
    """
    pdf_stem = pdf_path.stem

    # Check if already converted (idempotent)
    existing = find_marker_output(output_dir, pdf_stem)
    if existing:
        logger.debug("  Already converted: %s", pdf_path.name)
        return ConversionResult(pdf_path=pdf_path, md_path=existing, status="skipped")

    if dry_run:
        expected = output_dir / pdf_stem / f"{pdf_stem}.md"
        logger.info("  [DRY-RUN] Would convert: %s → %s", pdf_path.name, expected)
        return ConversionResult(pdf_path=pdf_path, md_path=expected, status="skipped")

    try:
        marker_exe = _find_marker()
    except MarkerNotFoundError as exc:
        return ConversionResult(pdf_path=pdf_path, md_path=None, status="failed", error=str(exc))

    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        marker_exe,
        str(pdf_path),
        "--output_dir", str(output_dir),
        "--layout_batch_size", str(layout_batch_size),
        "--detection_batch_size", str(detection_batch_size),
    ]
    if disable_ocr:
        cmd.append("--disable_ocr")
    if disable_images:
        cmd.append("--disable_image_extraction")

    logger.debug("  CMD: %s", " ".join(cmd))
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600,   # 10-minute hard cap per PDF
        )
    except subprocess.TimeoutExpired:
        return ConversionResult(
            pdf_path=pdf_path, md_path=None, status="failed",
            error="marker_single timed out after 600s",
        )
    except OSError as exc:
        return ConversionResult(pdf_path=pdf_path, md_path=None, status="failed", error=str(exc))

    if proc.returncode != 0:
        err = (proc.stderr or "").strip()[:400]
        logger.warning("  FAILED: %s | %s", pdf_path.name, err)
        return ConversionResult(pdf_path=pdf_path, md_path=None, status="failed", error=err)

    # Locate the .md output — marker may put it in different places across versions
    md_path = find_marker_output(output_dir, pdf_stem)
    if md_path is None:
        return ConversionResult(
            pdf_path=pdf_path, md_path=None, status="failed",
            error="marker_single returned 0 but no .md file found",
        )

    return ConversionResult(pdf_path=pdf_path, md_path=md_path, status="success")


def batch_convert(
    digital_pdfs: list[Path],
    output_dir: Path,
    log_path: Path,
    workers: int = DEFAULT_WORKERS,
    batch_multiplier: int = DEFAULT_BATCH_MULTIPLIER,
    limit: int = 0,
    resume: bool = False,
    dry_run: bool = False,
    layout_batch_size: int = DEFAULT_LAYOUT_BATCH_SIZE,
    detection_batch_size: int = DEFAULT_DETECTION_BATCH_SIZE,
    disable_ocr: bool = DEFAULT_DISABLE_OCR,
    disable_images: bool = DEFAULT_DISABLE_IMAGES,
) -> list[ConversionResult]:
    """Convert all digital PDFs to Markdown in batch.

    Uses ThreadPoolExecutor for optional parallelism, but defaults to
    workers=1 (sequential) because marker_single is GPU-bound — running
    multiple instances simultaneously competes for VRAM.

    With RTX 4090 (24 GB VRAM) + disable_ocr=True:
        workers=1, layout/detection_batch_size=8   →  safe, ~1-2 min/PDF
        workers=1, layout/detection_batch_size=16  →  more VRAM, monitor
        workers=2, layout/detection_batch_size=8   →  double throughput, feasible

    Args:
        digital_pdfs: List of digital PDF paths from Phase 1.
        output_dir: Root output directory for Markdown files.
        log_path: Path to conversion progress JSON log.
        workers: Number of parallel marker_single processes.
        batch_multiplier: Legacy; unused in marker v1.x.
        limit: If > 0, process at most this many PDFs.
        resume: Skip PDFs already logged as "success".
        dry_run: Preview without converting.
        layout_batch_size: Pages in parallel for layout model.
        detection_batch_size: Pages in parallel for detection model.
        disable_ocr: Skip Surya OCR (recommended for digital PDFs).

    Returns:
        List of ConversionResult for each processed PDF.
    """
    if limit > 0:
        digital_pdfs = digital_pdfs[:limit]

    logger.info(
        "Phase 2 (convert): %d PDFs | workers=%d | layout_batch=%d | detection_batch=%d"
        " | disable_ocr=%s | disable_images=%s",
        len(digital_pdfs), workers, layout_batch_size, detection_batch_size,
        disable_ocr, disable_images,
    )

    # Build resume skip-set
    done_set: set[str] = set()
    if resume:
        for entry in load_log(log_path):
            if entry.get("status") == "success":
                done_set.add(entry["pdf_path"])
        logger.info("  Resume: %d already converted", len(done_set))

    to_convert = [p for p in digital_pdfs if str(p) not in done_set]
    logger.info("  %d PDFs to convert", len(to_convert))

    log_data: list[dict] = list(load_log(log_path)) if resume else []
    results: list[ConversionResult] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                _convert_single_pdf, p, output_dir, batch_multiplier, dry_run,
                layout_batch_size, detection_batch_size, disable_ocr, disable_images,
            ): p
            for p in to_convert
        }
        total = len(futures)
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            results.append(result)
            log_data.append(result.to_dict())
            logger.info(
                "  [%d/%d] %-50s → %s",
                i, total,
                futures[future].name[:50],
                result.status,
            )
            # Checkpoint: persist log every 10 completions to survive interruptions
            if i % 10 == 0:
                save_log(log_path, log_data, dry_run=dry_run)

    save_log(log_path, log_data, dry_run=dry_run)

    success = sum(1 for r in results if r.status == "success")
    failed  = sum(1 for r in results if r.status == "failed")
    skipped = sum(1 for r in results if r.status == "skipped")
    logger.info(
        "  Convert done: success=%d  failed=%d  skipped=%d  (previously_done=%d)",
        success, failed, skipped, len(done_set),
    )
    if not dry_run:
        logger.info("  Conversion log → %s", log_path)

    return results


# ═════════════════════════════════════════════════════════════════════════════
# Phase 3: LLM metadata enrichment (YAML frontmatter)
# ═════════════════════════════════════════════════════════════════════════════

# NOTE: Prompt instructs the model to output ONLY a YAML block.
# Lower temperature (0.15) produces more deterministic, schema-compliant YAML.
_FRONTMATTER_SYSTEM = (
    "You are a PKB (Personal Knowledge Base) metadata architect for an Obsidian vault. "
    "You generate accurate, structured YAML frontmatter for academic papers. "
    "You ALWAYS output ONLY the YAML block (between --- markers) and nothing else."
)

_FRONTMATTER_PROMPT = """\
Generate YAML frontmatter for the academic paper below.

RULES:
- Output ONLY the YAML block starting with --- and ending with ---.
- No prose, no explanation, no code fences — just the raw YAML.
- Fill every field using information extracted directly from the paper.
- For fields you cannot determine from the text, use sensible defaults.
- Tags: lowercase with hyphens, e.g. ["#prompt-engineering", "#few-shot-learning"].
- summary: 2-4 sentences stating the paper's core contribution and findings.
- related_concepts: key concepts, models, or methods mentioned prominently.

YAML TEMPLATE (fill in all placeholder values):
---
doc_id: "{doc_id}"
doc_type: "academic-paper"
doc_created: "{today}"
doc_modified: "{today}"

title: ""
author: ""
year: ""
venue: ""

primary_domain: ""
secondary_domains: []

knowledge_level: "technical-research"
tags: []

status: "seedling"
confidence: "medium"
epistemic_status: ""

source: "academic-paper"

related_concepts: []
prerequisites: []
builds_on: []

aliases: []

summary: ""
keywords: []
---

PAPER CONTENT (first section):
{content}
"""


def _call_ollama(
    prompt: str,
    model: str = DEFAULT_MODEL,
    temperature: float = LLM_TEMPERATURE,
) -> str:
    """Call the local Ollama LLM and return the text response.

    Args:
        prompt: Full prompt string.
        model: Ollama model tag to use.
        temperature: Sampling temperature. Lower = more deterministic.

    Returns:
        The model's generated text.

    Raises:
        OllamaCallError: If the call fails or returns empty output.
    """
    if not _OLLAMA_OK:
        raise OllamaCallError(
            "ollama Python package not installed. Run: pip install ollama"
        )

    try:
        response = _ollama_lib.generate(  # type: ignore[union-attr]
            model=model,
            prompt=prompt,
            system=_FRONTMATTER_SYSTEM,
            options={
                "temperature": temperature,
                "num_ctx": 8192,
                "num_predict": 1024,  # YAML block should fit in ~1024 tokens
            },
        )
        # GenerateResponse exposes .response attribute (ollama-python >=0.2)
        text: str = (
            response.response
            if hasattr(response, "response")
            else response.get("response", "")
        )
        if not text.strip():
            raise OllamaCallError("Ollama returned an empty response")
        return text

    except OllamaCallError:
        raise
    except Exception as exc:
        raise OllamaCallError(f"Ollama generate() failed: {exc}") from exc


def _extract_yaml_block(raw: str) -> str:
    """Pull the YAML block out of the LLM's raw response.

    Handles cases where the model includes preamble text or extra trailing content.

    Args:
        raw: Raw LLM response text.

    Returns:
        A YAML string bounded by --- markers on its own lines.
    """
    # Primary: extract first --- ... --- block
    match = re.search(r"(---\s*\n.*?---\s*(?:\n|$))", raw, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fallback A: response begins with --- (model omitted closing ---)
    if raw.strip().startswith("---"):
        block = raw.strip()
        if not block.endswith("---"):
            block += "\n---"
        return block

    # Fallback B: wrap the whole thing
    return f"---\n{raw.strip()}\n---"


def _generate_frontmatter(
    md_path: Path,
    model: str = DEFAULT_MODEL,
) -> str:
    """Generate YAML frontmatter for a converted Markdown file via the LLM.

    Reads the first LLM_CONTEXT_CHARS characters of the file as context.

    Args:
        md_path: Path to the Markdown file.
        model: Ollama model to use.

    Returns:
        YAML frontmatter string (--- ... ---).

    Raises:
        OllamaCallError: If the LLM call fails.
        OSError: If the file cannot be read.
    """
    content = md_path.read_text(encoding="utf-8", errors="replace")
    sample = content[:LLM_CONTEXT_CHARS]

    prompt = _FRONTMATTER_PROMPT.format(
        doc_id=slugify(md_path.stem),
        today=date.today().isoformat(),
        content=sample,
    )

    logger.debug("  LLM call for: %s", md_path.name)
    raw = _call_ollama(prompt, model=model)
    return _extract_yaml_block(raw)


def _enrich_single(
    md_path: Path,
    model: str = DEFAULT_MODEL,
    dry_run: bool = False,
) -> EnrichResult:
    """Prepend LLM-generated YAML frontmatter to a Markdown file.

    Creates a backup at <stem>.original.md before modifying the file.
    Skips files that already start with --- (already enriched).

    Args:
        md_path: Path to the Markdown file to enrich.
        model: Ollama model tag.
        dry_run: If True, generate frontmatter but do not write.

    Returns:
        EnrichResult describing the outcome.
    """
    if not md_path.exists():
        return EnrichResult(md_path=md_path, status="failed", error="File not found")

    try:
        existing_content = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return EnrichResult(md_path=md_path, status="failed", error=str(exc))

    # Skip if already enriched (idempotent)
    if existing_content.lstrip().startswith("---"):
        logger.debug("  Already enriched (skipping): %s", md_path.name)
        return EnrichResult(md_path=md_path, status="skipped")

    try:
        frontmatter = _generate_frontmatter(md_path, model=model)
    except OllamaCallError as exc:
        logger.error("  LLM failed for %s: %s", md_path.name, exc)
        return EnrichResult(md_path=md_path, status="failed", error=str(exc))
    except OSError as exc:
        return EnrichResult(md_path=md_path, status="failed", error=str(exc))

    if dry_run:
        logger.info("  [DRY-RUN] Would enrich: %s", md_path.name)
        return EnrichResult(md_path=md_path, status="skipped")

    # INVARIANT: Always back up the original before overwriting
    backup = md_path.with_stem(md_path.stem + ".original")
    shutil.copy2(md_path, backup)

    enriched_text = f"{frontmatter}\n\n{existing_content}"
    md_path.write_text(enriched_text, encoding="utf-8")

    logger.info("  Enriched: %s", md_path.name)
    return EnrichResult(md_path=md_path, status="success")


def batch_enrich(
    output_dir: Path,
    log_path: Path,
    model: str = DEFAULT_MODEL,
    limit: int = 0,
    resume: bool = False,
    dry_run: bool = False,
) -> list[EnrichResult]:
    """Enrich all converted Markdown files with LLM-generated YAML frontmatter.

    Discovers .md files recursively under output_dir, excluding .original.md backups.

    Args:
        output_dir: Root directory containing converted Markdown files.
        log_path: Path to enrichment progress JSON log.
        model: Ollama model tag.
        limit: If > 0, process at most this many files.
        resume: Skip files already logged as "success".
        dry_run: Preview without writing.

    Returns:
        List of EnrichResult for each file processed.
    """
    # Discover all .md files, excluding backups
    md_files = sorted(
        p for p in output_dir.rglob("*.md")
        if ".original" not in p.name
    )

    if limit > 0:
        md_files = md_files[:limit]

    logger.info(
        "Phase 3 (enrich): %d Markdown files | model=%s",
        len(md_files), model,
    )

    done_set: set[str] = set()
    if resume:
        for entry in load_log(log_path):
            if entry.get("status") == "success":
                done_set.add(entry["md_path"])
        logger.info("  Resume: %d already enriched", len(done_set))

    to_enrich = [p for p in md_files if str(p) not in done_set]
    logger.info("  %d files to enrich", len(to_enrich))

    log_data: list[dict] = list(load_log(log_path)) if resume else []
    results: list[EnrichResult] = []

    for i, md_path in enumerate(to_enrich, 1):
        result = _enrich_single(md_path, model=model, dry_run=dry_run)
        results.append(result)
        log_data.append(result.to_dict())
        logger.info(
            "  [%d/%d] %-50s → %s",
            i, len(to_enrich), md_path.name[:50], result.status,
        )
        # Checkpoint every 20 files
        if i % 20 == 0:
            save_log(log_path, log_data, dry_run=dry_run)

    save_log(log_path, log_data, dry_run=dry_run)

    success = sum(1 for r in results if r.status == "success")
    failed  = sum(1 for r in results if r.status == "failed")
    skipped = sum(1 for r in results if r.status == "skipped")
    logger.info(
        "  Enrich done: success=%d  failed=%d  skipped=%d  (previously_done=%d)",
        success, failed, skipped, len(done_set),
    )
    if not dry_run:
        logger.info("  Enrich log → %s", log_path)

    return results


# ═════════════════════════════════════════════════════════════════════════════
# Preflight validation
# ═════════════════════════════════════════════════════════════════════════════

def preflight(
    phase: str,
    pdf_dir: Path,
    output_dir: Path,
    log_dir: Path,
) -> None:
    """Validate that required tools, directories, and packages are available.

    Checks are scoped to the requested phase to avoid irrelevant errors
    (e.g. don't require marker_single when running enrich-only).

    Args:
        phase: The phase about to be run.
        pdf_dir: Source PDF directory.
        output_dir: Markdown output directory.
        log_dir: Log file directory.

    Raises:
        PipelineError: If a required tool or package is missing.
        SystemExit(2): If pdf_dir does not exist.
    """
    needs_pdfs    = phase in ("dedupe", "triage", "convert", "all")
    needs_fitz    = phase in ("triage", "all")
    needs_marker  = phase in ("convert", "all")
    needs_ollama  = phase in ("enrich", "all")

    if needs_pdfs and not pdf_dir.exists():
        logger.error("PDF source directory not found: %s", pdf_dir)
        sys.exit(2)

    if needs_fitz and not _FITZ_OK:
        raise PipelineError(
            "PyMuPDF not installed. Activate the venv and run: pip install pymupdf"
        )

    if needs_marker:
        try:
            exe = _find_marker()
            logger.debug("  marker_single found: %s", exe)
        except MarkerNotFoundError as exc:
            raise PipelineError(str(exc)) from exc

    if needs_ollama and not _OLLAMA_OK:
        raise PipelineError(
            "ollama Python package not installed. Run: pip install ollama"
        )

    # Ensure output and log directories exist
    output_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)


# ═════════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser.

    Returns:
        Fully configured ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        prog="pdf_to_markdown_pipeline",
        description=(
            "PDF → Obsidian Markdown pipeline.\n"
            "Four phases: dedupe → triage → convert → enrich."
        ),
        epilog=(
            "Examples:\n"
            "  %(prog)s --phase all -v              # Full pipeline, verbose\n"
            "  %(prog)s --phase all --dry-run -v    # Preview without writing\n"
            "  %(prog)s --phase all --limit 5 -v    # Test on 5 PDFs\n"
            "  %(prog)s --phase triage -v            # Classify only\n"
            "  %(prog)s --phase convert -w 2         # Convert, 2 workers\n"
            "  %(prog)s --phase enrich --resume      # Resume enrichment\n"
            "  %(prog)s --phase dedupe -v             # Find duplicates\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Verbosity: -v = INFO, -vv = DEBUG")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Suppress non-error output")
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="Preview actions; write nothing")

    parser.add_argument(
        "--phase",
        choices=["all", "dedupe", "triage", "convert", "enrich"],
        default="all",
        help="Which phase(s) to run (default: all = triage+convert+enrich)",
    )
    parser.add_argument(
        "--pdf-dir", type=Path, default=DEFAULT_PDF_DIR,
        metavar="DIR",
        help=f"Source PDF directory (default: {DEFAULT_PDF_DIR})",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
        metavar="DIR",
        help=f"Markdown output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--log-dir", type=Path, default=DEFAULT_LOG_DIR,
        metavar="DIR",
        help=f"Directory for JSON log files (default: {DEFAULT_LOG_DIR})",
    )
    parser.add_argument(
        "-w", "--workers", type=int, default=DEFAULT_WORKERS, metavar="N",
        help=(
            f"Parallel marker_single processes for Phase 2 (default: {DEFAULT_WORKERS}). "
            "RTX 4090: up to 2 is safe; more may exhaust VRAM."
        ),
    )
    parser.add_argument(
        "--batch-multiplier", type=int, default=DEFAULT_BATCH_MULTIPLIER, metavar="N",
        help="Legacy flag (no-op in marker v1.x); kept for backwards compat.",
    )
    parser.add_argument(
        "--layout-batch-size", type=int, default=DEFAULT_LAYOUT_BATCH_SIZE, metavar="N",
        help=(
            f"Pages processed in parallel by marker layout model (default: {DEFAULT_LAYOUT_BATCH_SIZE}). "
            "RTX 4090: 8–16 is safe.  Higher = more VRAM, faster throughput."
        ),
    )
    parser.add_argument(
        "--detection-batch-size", type=int, default=DEFAULT_DETECTION_BATCH_SIZE, metavar="N",
        help=(
            f"Pages processed in parallel by marker detection model (default: {DEFAULT_DETECTION_BATCH_SIZE}). "
            "RTX 4090: 8–16 is safe."
        ),
    )
    parser.add_argument(
        "--no-disable-ocr", dest="disable_ocr", action="store_false",
        default=True,
        help=(
            "Re-enable OCR even for digital PDFs.  By default OCR is disabled "
            "for digital PDFs (--disable_ocr passed to marker) — skipping it "
            "cuts per-PDF time by ~40–60 %%.  Use this flag only for scanned docs."
        ),
    )
    parser.add_argument(
        "--no-images", dest="disable_images", action="store_true",
        default=False,
        help=(
            "Suppress image extraction (pass --disable_image_extraction to marker). "
            "By default images ARE extracted — each paper gets its own subfolder so "
            "~15 figures per paper stay organised alongside the .md file.  Use this "
            "flag if you genuinely do not want any JPEGs on disk."
        ),
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"Ollama model for Phase 3 frontmatter generation (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--limit", type=int, default=0, metavar="N",
        help="Process at most N PDFs per phase (0 = unlimited). Useful for testing.",
    )
    parser.add_argument(
        "--resume", action="store_true",
        help="Skip files already completed according to existing log files.",
    )
    parser.add_argument(
        "--filter", dest="filter_terms", default="",
        metavar="KEYWORDS",
        help=(
            "Comma-separated keywords to filter PDFs by filename stem "
            "(case-insensitive OR match).  E.g. --filter 'transformer,attention' "
            "processes only PDFs whose names contain 'transformer' OR 'attention'. "
            "Applied before --limit."
        ),
    )
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure the root logger based on CLI verbosity flags.

    Args:
        verbosity: Count of -v flags (0 = WARNING, 1 = INFO, 2+ = DEBUG).
        quiet: If True, suppress everything below ERROR.
    """
    level = (
        logging.ERROR   if quiet
        else logging.DEBUG   if verbosity >= 2
        else logging.INFO    if verbosity >= 1
        else logging.WARNING
    )
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)-7s] %(message)s",
        datefmt="%H:%M:%S",
    )


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the pipeline.

    Args:
        argv: Argument vector; defaults to sys.argv[1:].

    Returns:
        Exit code: 0 = success, 1 = pipeline error, 2 = bad config.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    if args.dry_run:
        logger.warning("DRY-RUN mode active — no files will be written")

    # Parse --filter into a list of lowercase keyword strings
    filter_terms: list[str] = (
        [t.strip() for t in args.filter_terms.split(",") if t.strip()]
        if args.filter_terms else []
    )

    # Build per-phase log paths from the log directory
    logs = {
        "dedupe":  args.log_dir / _LOG_DEDUPE,
        "triage":  args.log_dir / _LOG_TRIAGE,
        "convert": args.log_dir / _LOG_CONVERT,
        "enrich":  args.log_dir / _LOG_ENRICH,
    }

    # Preflight: validate tools and paths
    try:
        preflight(args.phase, args.pdf_dir, args.output_dir, args.log_dir)
    except PipelineError as exc:
        logger.error("Preflight failed: %s", exc)
        return 1

    # Print confirmed config so user can verify before a long run
    logger.info("═" * 65)
    logger.info("PDF Pipeline v%s", __version__)
    logger.info("  phase      : %s", args.phase)
    logger.info("  pdf_dir    : %s", args.pdf_dir)
    logger.info("  output_dir : %s", args.output_dir)
    logger.info("  log_dir    : %s", args.log_dir)
    logger.info("  model      : %s", args.model)
    logger.info("  workers    : %d", args.workers)
    logger.info("  batch_mult : %d", args.batch_multiplier)
    logger.info("  limit      : %s", args.limit if args.limit > 0 else "none")
    logger.info("  filter     : %s", ", ".join(filter_terms) if filter_terms else "none")
    logger.info("  resume     : %s", args.resume)
    logger.info("  dry_run    : %s", args.dry_run)
    logger.info("═" * 65)

    # ── dedupe only ────────────────────────────────────────────────────────
    if args.phase == "dedupe":
        deduplicate_corpus(args.pdf_dir, logs["dedupe"], dry_run=args.dry_run)

    # ── triage only ────────────────────────────────────────────────────────
    elif args.phase == "triage":
        triage_corpus(
            args.pdf_dir, logs["triage"],
            limit=args.limit, resume=args.resume, dry_run=args.dry_run,
            filter_terms=filter_terms or None,
        )

    # ── convert only ───────────────────────────────────────────────────────
    elif args.phase == "convert":
        # Load triage results; run triage on-the-fly if not done yet
        triage_entries = load_log(logs["triage"])
        if triage_entries:
            digital = [
                Path(e["path"]) for e in triage_entries
                if e.get("category") == "digital"
            ]
            logger.info("Loaded %d digital PDFs from triage log", len(digital))
            if filter_terms:
                terms_lower = [t.lower() for t in filter_terms]
                digital = [p for p in digital if any(t in p.stem.lower() for t in terms_lower)]
                logger.info(
                    "  --filter applied (%s): %d PDFs match",
                    ", ".join(filter_terms), len(digital),
                )
        else:
            logger.warning("No triage log found — running triage first…")
            digital, _ = triage_corpus(
                args.pdf_dir, logs["triage"],
                limit=args.limit, resume=args.resume, dry_run=args.dry_run,
                filter_terms=filter_terms or None,
            )

        batch_convert(
            digital, args.output_dir, logs["convert"],
            workers=args.workers,
            batch_multiplier=args.batch_multiplier,
            limit=args.limit,
            resume=args.resume,
            dry_run=args.dry_run,
            layout_batch_size=args.layout_batch_size,
            detection_batch_size=args.detection_batch_size,
            disable_ocr=args.disable_ocr,
            disable_images=args.disable_images,
        )

    # ── enrich only ────────────────────────────────────────────────────────
    elif args.phase == "enrich":
        batch_enrich(
            args.output_dir, logs["enrich"],
            model=args.model,
            limit=args.limit,
            resume=args.resume,
            dry_run=args.dry_run,
        )

    # ── all: triage → convert → enrich ────────────────────────────────────
    elif args.phase == "all":
        digital, scanned = triage_corpus(
            args.pdf_dir, logs["triage"],
            limit=args.limit, resume=args.resume, dry_run=args.dry_run,
            filter_terms=filter_terms or None,
        )

        if scanned:
            scanned_sample = "\n    ".join(p.name for p in scanned[:8])
            logger.warning(
                "%d scanned PDFs will be SKIPPED (manual/vision-LLM review needed):\n    %s%s",
                len(scanned),
                scanned_sample,
                "\n    ..." if len(scanned) > 8 else "",
            )

        batch_convert(
            digital, args.output_dir, logs["convert"],
            workers=args.workers,
            batch_multiplier=args.batch_multiplier,
            limit=args.limit,
            resume=args.resume,
            dry_run=args.dry_run,
            layout_batch_size=args.layout_batch_size,
            detection_batch_size=args.detection_batch_size,
            disable_ocr=args.disable_ocr,
            disable_images=args.disable_images,
        )

        batch_enrich(
            args.output_dir, logs["enrich"],
            model=args.model,
            limit=args.limit,
            resume=args.resume,
            dry_run=args.dry_run,
        )

        logger.info("═" * 65)
        logger.info("Pipeline complete.")
        logger.info("  Markdown files → %s", args.output_dir)
        logger.info("  Logs           → %s", args.log_dir)
        logger.info("═" * 65)

    return 0


# ═════════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
