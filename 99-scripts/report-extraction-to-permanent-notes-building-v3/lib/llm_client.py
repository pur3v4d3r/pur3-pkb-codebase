#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""llm_client.py — Ollama HTTP client + structured-output validation + cache.

Thin wrapper around ``http://localhost:11434/api/chat`` with:
- Content-hash keyed JSON cache in ``_v3-output/llm-cache/``
- Retry with exponential backoff
- Post-hoc structured-output validation via ``outlines``
- Sequential dispatch (Ollama is single-tenant)

Used by Stage 4 (normalize) and the opt-in synthesis pass.

Phase 7 deliverable. See spec §5 Phase 7.
"""
from __future__ import annotations

# Phase 0: stub. Implemented in Phase 7.
