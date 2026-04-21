#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""parallel.py — ProcessPoolExecutor wrapper with rich progress.

Provides ``map_parallel(fn, items, *, workers=None, desc="")`` that wraps
``concurrent.futures.ProcessPoolExecutor`` and reports progress through
``rich.progress``.

Used by Stages 1, 3, 5, 6.

Phase 2 deliverable (introduced when consolidation lands).
"""
from __future__ import annotations

# Phase 0: stub. Implemented in Phase 2.
