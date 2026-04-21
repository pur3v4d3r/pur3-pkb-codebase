#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s4_normalize.py — Stage 4 (opt-in): LLM concept normalization + alias mining.

For each consolidated Candidate, calls Ollama with structured-output prompt
to return ``(canonical_name, aliases, definition_suggestion, domain_suggestion)``.
Cached by content hash; re-runs are free for unchanged candidates.

Inserted between Stage 3 and Stage 5 only when ``--llm-normalize`` is passed.

Phase 7 deliverable. See spec §5 Phase 7.
Phase 0: stub.
"""
from __future__ import annotations
