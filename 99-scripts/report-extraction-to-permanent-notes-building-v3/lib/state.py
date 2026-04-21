#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""state.py — Pipeline state + per-stage hashes + diff-aware skipping.

Tracks:
- Processed batch fingerprints
- Per-stage input/output hashes
- Last successful stage per run (for ``--from-stage`` resume)

State persists in ``_v3-output/_pipeline-state.json``.

Used by all stages; consumed centrally by ``pipeline_v3.py``.

Phase 2 minimal version (track stage completion). Phase 10 expands to full
diff-aware incremental skipping.
"""
from __future__ import annotations

# Phase 0: stub. Minimal version in Phase 2; full diff-aware in Phase 10.
