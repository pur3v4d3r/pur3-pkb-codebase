#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ui.py — rich console helpers.

Centralizes ``rich.Console`` instances, common styles, and per-stage banner
rendering. Used by every stage and by ``pipeline_v3.py``.

Phase 0: minimal — exposes a shared Console.
"""
from __future__ import annotations

from rich.console import Console

console: Console = Console()
err_console: Console = Console(stderr=True)
