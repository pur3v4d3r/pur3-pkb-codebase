#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pytest configuration: inject V5 dir + V4 dir + V3 dir into sys.path."""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_V5_DIR = _HERE.parent
_V4_DIR = _V5_DIR.parent / "report-extraction-to-permanent-notes-building-v4"
_V3_DIR = _V5_DIR.parent / "report-extraction-to-permanent-notes-building-v3"

# Order matters: sys.path.insert(0, ...) is LIFO, so insert in reverse
# precedence order. V3 first (lowest precedence — shadowed by V4 / V5),
# then V4, then V5 last so V5's `lib/` package wins over V3's `lib/`.
for _p in (_V3_DIR, _V4_DIR, _V5_DIR):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
