#!/usr/bin/env bash
# Run V6 elaboration over all 2026-04-26 custom batches except batch 16 (already done).
set -u
cd "/d/10_pur3v4d3r's-vault/99-scripts/report-extraction-to-permanent-notes-building-v6"
SEEDS_BASE="D:\\10_pur3v4d3r's-vault\\999-report-organizing\\_extractor-output\\_synthetic-seeds"
RUNS_DIR="runs"
mkdir -p "$RUNS_DIR"

BATCHES=(
  "2026-04-26-custom-01-logical-fallacies"
  "2026-04-26-custom-02-formal-reasoning"
  "2026-04-26-custom-03-memory-science"
  "2026-04-26-custom-04-learning-strategies"
  "2026-04-26-custom-05-neuroscience-of-learning"
  "2026-04-26-custom-06-positive-psychology"
  "2026-04-26-custom-07-social-psychology"
  "2026-04-26-custom-08-behavioral-economics"
  "2026-04-26-custom-09-epistemology"
  "2026-04-26-custom-10-instructional-design"
  "2026-04-26-custom-11-pkm-knowledge-work"
  "2026-04-26-custom-12-language-and-cognition"
  "2026-04-26-custom-13-developmental-psychology"
  "2026-04-26-custom-14-emotions-and-affect"
  "2026-04-26-custom-15-advanced-cognitive-science"
)

for batch in "${BATCHES[@]}"; do
  echo ""
  echo "############################################################"
  echo "# V6: $batch  ($(date +%H:%M:%S))"
  echo "############################################################"
  PYTHONUTF8=1 python pipeline_v6.py \
    --input-dir "${SEEDS_BASE}\\${batch}" \
    --report-runs "${RUNS_DIR}/${batch}-v6-log.json" \
    2>&1 | tail -15
done

echo ""
echo "############################################################"
echo "# ALL BATCHES COMPLETE  ($(date +%H:%M:%S))"
echo "############################################################"
