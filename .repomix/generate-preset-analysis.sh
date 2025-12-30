#!/bin/bash
# Preset-Based Multi-Analysis Generator

echo "🎯 Using Configuration Presets for Multi-Analysis..."

# Extract presets from main config and generate targeted analyses
echo "📊 Core PKB Analysis..."
jq -r '._presets.core_pkb[]' repomix.config.json | while read pattern; do
    INCLUDE_ARGS="$INCLUDE_ARGS --include \"$pattern\""
done
eval "repomix $INCLUDE_ARGS --output analysis-core-pkb.md"

echo "📚 Research Content Analysis..." 
RESEARCH_INCLUDES=""
for pattern in "02-projects/**" "03-notes/**" "04-library/**"; do
    RESEARCH_INCLUDES="$RESEARCH_INCLUDES --include \"$pattern\""
done
eval "repomix $RESEARCH_INCLUDES --output analysis-research.md"

echo "🎯 Prompt Engineering Analysis..."
PE_INCLUDES=""
for pattern in "999-v4d3r/**" "__agents/**" "04-library/03-prompt-engineering/**"; do
    PE_INCLUDES="$PE_INCLUDES --include \"$pattern\""
done
eval "repomix $PE_INCLUDES --output analysis-prompt-engineering.md"

echo "✅ Preset-based analysis complete!"