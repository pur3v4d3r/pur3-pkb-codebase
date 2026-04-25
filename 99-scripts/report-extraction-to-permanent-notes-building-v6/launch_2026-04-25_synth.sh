#!/usr/bin/env bash
# Launch V6 pipeline across all 8 synthetic-seed batch dirs from 2026-04-25 rollout.
set +e
export PYTHONIOENCODING=utf-8
cd "$(dirname "$0")"
LOG=runs/2026-04-25-synthetic-seeds-batchloop.log
echo "=== V6 synthetic-seeds loop START $(date) ===" > "$LOG"
SEED_ROOT="/d/10_pur3v4d3r's-vault/999-report-organizing/_extractor-output/_synthetic-seeds"
for d in "$SEED_ROOT"/2026-04-25-2026-04-25-batch-1[1-8]-*; do
  base=$(basename "$d")
  win_d=$(cygpath -w "$d")
  echo "--- batch: $base ---" | tee -a "$LOG"
  echo "    input: $win_d" | tee -a "$LOG"
  python pipeline_v6.py \
    --input-dir "$win_d" \
    --report-runs "runs/2026-04-25-v6-${base}.json" \
    -v 2>&1 | tee -a "$LOG"
done
echo "=== V6 loop DONE $(date) ===" >> "$LOG"
