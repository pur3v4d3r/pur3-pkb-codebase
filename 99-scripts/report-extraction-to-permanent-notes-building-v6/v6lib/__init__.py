"""v6lib — V6 elaboration pipeline package.

Provides the V6-specific machinery layered on top of V4 (discovery,
bundling, LLM client) and V5 (output index, matcher).

Public modules:
    prompts        — Two-pass prompt contracts + Pydantic schemas.
    elaborator     — Two-pass orchestrator (outline → elaborate).
    renderer       — Rich markdown renderer for the V6 template.
    merger_v6      — Merge-aware writer for re-runs.
"""
__version__ = "1.0.0"
