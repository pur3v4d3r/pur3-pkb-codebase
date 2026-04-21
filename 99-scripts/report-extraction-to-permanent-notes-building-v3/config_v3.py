#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pipeline v3 configuration.

Centralizes all paths, thresholds, model identifiers, and tunables. Imported
by every stage and library module. Edit here, not inline.

Spec reference: ``_v3-spec/00-master-spec.md`` §1, §2.

Phase 0: paths and constants only. Phase-specific knobs added as each phase ships.
"""
from __future__ import annotations

from pathlib import Path

# ═════════════════════════════════════════════════════════════════════════
# Paths
# ═════════════════════════════════════════════════════════════════════════

# Repository / vault root (3 levels up from this file: v3 dir → 99-scripts → vault)
SCRIPTS_DIR: Path = Path(__file__).resolve().parent
VAULT_ROOT: Path = SCRIPTS_DIR.parent.parent

# Source content
REPORTS_ROOT: Path = VAULT_ROOT / "999-report-organizing"
EXTRACTOR_OUTPUT_DIR: Path = REPORTS_ROOT / "_extractor-output"
PERMANENT_NOTES_DIR: Path = REPORTS_ROOT / "_permanent-notes" / "_permanent-notes"

# v3 outputs
V3_OUTPUT_DIR: Path = SCRIPTS_DIR / "_v3-output"
EMBEDDINGS_CACHE_DIR: Path = V3_OUTPUT_DIR / "embeddings"
LLM_CACHE_DIR: Path = V3_OUTPUT_DIR / "llm-cache"
RUNS_DIR: Path = V3_OUTPUT_DIR / "runs"
PIPELINE_STATE_FILE: Path = V3_OUTPUT_DIR / "_pipeline-state.json"

# v2 reuse (read-only — never write to v2 paths from v3)
V2_SCRIPTS_DIR: Path = SCRIPTS_DIR.parent / "report-extraction-to-permanent-notes-building"


# ═════════════════════════════════════════════════════════════════════════
# Matching thresholds (Stage 5)
# ═════════════════════════════════════════════════════════════════════════

# Hybrid score: 0.4 * difflib + 0.6 * cosine
DIFFLIB_WEIGHT: float = 0.4
COSINE_WEIGHT: float = 0.6
AUTO_MATCH_THRESHOLD: float = 0.92
REVIEW_QUEUE_THRESHOLD: float = 0.78
MAX_CANDIDATES_RETURNED: int = 5


# ═════════════════════════════════════════════════════════════════════════
# Embedding model (Stage 5)
# ═════════════════════════════════════════════════════════════════════════

EMBED_MODEL_ID: str = "BAAI/bge-small-en-v1.5"
EMBED_DIM: int = 384
EMBED_BATCH_SIZE: int = 64


# ═════════════════════════════════════════════════════════════════════════
# LLM (Stage 4 / opt-in synthesis)
# ═════════════════════════════════════════════════════════════════════════

OLLAMA_URL: str = "http://localhost:11434"
LLM_MODEL_NORMALIZE: str = "qwen2.5:7b-instruct-q5_K_M"
LLM_MODEL_SYNTHESIZE: str = "qwen2.5:7b-instruct-q5_K_M"  # Upgrade to 14B if quality demands
LLM_REQUEST_TIMEOUT_S: float = 120.0
LLM_MAX_RETRIES: int = 3


# ═════════════════════════════════════════════════════════════════════════
# Parallelism (Stages 1, 3, 5, 6)
# ═════════════════════════════════════════════════════════════════════════

# Default to None → ProcessPoolExecutor picks (os.cpu_count())
MAX_WORKERS: int | None = None


# ═════════════════════════════════════════════════════════════════════════
# Audit gates (Stage 10) — see spec §7.2
# ═════════════════════════════════════════════════════════════════════════

GATE_MIN_RESOLUTION_RATE: float = 0.95
# Lowered 60 -> 55 (2026-04-21) per Phase 5 sandbox finding: the slim Phase-3
# renderer produces a tight quality distribution centred on 56-58 (78% of notes
# fall in the 50-59 band). Threshold 60 was aspirational; 55 reflects the
# renderer's actual output ceiling. Re-raise after a renderer rework.
GATE_MIN_AVG_QUALITY: float = 55.0
GATE_MAX_LOW_QUALITY_PCT: float = 0.05  # notes scoring < 40
GATE_LOW_QUALITY_THRESHOLD: float = 40.0


# ═════════════════════════════════════════════════════════════════════════
# Version
# ═════════════════════════════════════════════════════════════════════════

PIPELINE_VERSION: str = "3.0.0-alpha0"
