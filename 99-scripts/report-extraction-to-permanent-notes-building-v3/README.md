# Pipeline v3

**Status:** Phase 0 — scaffolding complete, awaiting Phase 1 implementation.
**Spec:** [`../report-extraction-to-permanent-notes-building/_v3-spec/00-master-spec.md`](../report-extraction-to-permanent-notes-building/_v3-spec/00-master-spec.md)

A rewrite of the report-extraction → permanent-notes pipeline. v2 lives untouched in
the sibling `report-extraction-to-permanent-notes-building/` directory and remains
the production pipeline until v3 ships through Phase 6 cutover.

## Quickstart (once Phase 1+ ships)

```bash
# Activate venv
source ../../.venv/Scripts/activate

# Install v3 dependencies
pip install -r requirements-v3.txt

# Verify environment
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
curl -s http://localhost:11434/api/tags

# Dry-run to sandbox (Phase 3+)
python pipeline_v3.py --to-stage 6 --target-dir _sandbox-rebuild

# Full rebuild (Phase 6+)
python pipeline_v3.py --rebuild --execute
```

## Layout

```
pipeline_v3.py          # Master orchestrator (Phase 0: stub)
config_v3.py            # Paths, thresholds, model configs
requirements-v3.txt     # Pinned dependencies
stages/                 # One module per pipeline stage
lib/                    # Shared utilities
templates/              # Jinja2 templates for note rendering
tests/                  # pytest suite + fixtures
_v3-output/             # Run logs, embeddings cache, LLM cache
```

## Phase rollout

See the master spec, §5. Phase order is strict; each phase must clear its gate
before the next begins. Current phase: **Phase 0 (scaffolding)**.

## Decisions locked

- **LLM runner:** Ollama (already running locally)
- **Models:** `qwen2.5:7b-instruct-q5_K_M` (LLM), `BAAI/bge-small-en-v1.5` (embeddings)
- **Data model:** pydantic v2
- **Templates:** Separate `.j2` files in `templates/`
- **`## Synthesis`:** Opt-in via `--llm-synthesize`
- **MOCs:** Per-domain only (initially)
- **`_Master-*-Index.md`:** Retired in favor of MOCs
