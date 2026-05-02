#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""config_merge.py — Configuration for the stub-consolidation tool.

Imports shared paths/settings from config_v3 and adds merge-specific tunables.
Edit here to adjust thresholds, model names, or paths.
"""
from __future__ import annotations

from pathlib import Path

import config_v3 as _v3

# ─── Shared from v3 pipeline ────────────────────────────────────────────────

SCRIPTS_DIR: Path = _v3.SCRIPTS_DIR
VAULT_ROOT: Path = _v3.VAULT_ROOT
V3_OUTPUT_DIR: Path = _v3.V3_OUTPUT_DIR
OLLAMA_URL: str = _v3.OLLAMA_URL
LLM_CACHE_DIR: Path = _v3.LLM_CACHE_DIR
LLM_REQUEST_TIMEOUT_S: float = _v3.LLM_REQUEST_TIMEOUT_S
LLM_MAX_RETRIES: int = _v3.LLM_MAX_RETRIES
PIPELINE_VERSION: str = _v3.PIPELINE_VERSION

# ─── Stub source directory ───────────────────────────────────────────────────

STUBS_DIR: Path = (
    VAULT_ROOT
    / "999-report-organizing"
    / "_permanent-notes"
    / "v3-pipeline-permanent-notes"
)

# ─── State output directory (outside vault — avoids Obsidian indexer churn) ─

MERGE_STATE_DIR: Path = V3_OUTPUT_DIR / "merge-state"

# Embedding cache (.npz — separate dim/model from v3 pipeline cache)
MERGE_EMBED_CACHE: Path = MERGE_STATE_DIR / "merge-embeddings.npz"

# ─── Embedding model ─────────────────────────────────────────────────────────

EMBEDDING_MODEL: str = "nomic-embed-text"   # via Ollama /api/embed
EMBEDDING_DIM: int = 768                    # nomic-embed-text output dimension
EMBED_BATCH_SIZE: int = 32                  # texts per Ollama /api/embed request
EMBED_REQUEST_TIMEOUT_S: float = 180.0      # longer timeout for batch embedding

# ─── LLM verification ────────────────────────────────────────────────────────

LLM_MODEL_VERIFY: str = "qwen2.5:14b-instruct-q5_K_M"

#: Bump this string to invalidate all cached LLM verification results.
VERIFY_PROMPT_VERSION: str = "verify-v1"

# ─── Clustering thresholds ───────────────────────────────────────────────────

#: Cosine similarity ≥ this → cluster candidate (sent to LLM for verification).
SIMILARITY_THRESHOLD: float = 0.82

#: Cosine similarity ≥ this → auto-merge (skip LLM, skip review).
AUTO_MERGE_THRESHOLD: float = 0.95

#: Clusters with more members than this are discarded — Union-Find single-linkage
#: can chain unrelated stubs transitively. True duplicate groups are small (2–5),
#: occasionally larger for the same theory cited many ways (e.g. CLT ≈ 23).
MAX_CLUSTER_SIZE: int = 25

# ─── File operations ─────────────────────────────────────────────────────────

#: Non-primary stub files are moved here after merge (not deleted).
TRASH_DIR: Path = STUBS_DIR / ".trash"

# ─── State file names ────────────────────────────────────────────────────────

SCAN_STATE_FILE: str = "01_scan.json"
CLUSTER_STATE_FILE: str = "02_clusters.json"
VERIFIED_STATE_FILE: str = "03_verified.json"
DECISIONS_STATE_FILE: str = "04_decisions.json"
MERGE_LOG_FILE: str = "05_merge_log.json"
