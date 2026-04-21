#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""s1_extract.py — Stage 1: parallel report extraction.

Wraps v2's ``pkb_extractor.py`` (left untouched). Discovers unprocessed
report directories and dispatches extraction across worker processes.

Output: ``<batch>/<report_stem>_extracted.json`` per report.

Phase 2 deliverable (parallelism added when consolidation lands).
Phase 0: stub.
"""
from __future__ import annotations
