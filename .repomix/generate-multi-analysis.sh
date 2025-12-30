#!/bin/bash
# Multi-Version Repomix Analysis Script

echo "🚀 Starting Multi-Version Analysis..."

# Version 1: Core PKB System Analysis
echo "📊 Generating Core PKB Analysis..."
repomix --config repomix-system.config.json

# Version 2: Research Content Analysis  
echo "📚 Generating Research Content Analysis..."
repomix --config repomix-research.config.json

# Version 3: Full AI-Optimized Analysis
echo "🧠 Generating Full AI Analysis..."
repomix

# Version 4: Prompt Engineering Focus
echo "🎯 Generating Prompt Engineering Analysis..."
repomix --include "999-v4d3r/**" --include "__agents/**" --include "04-library/03-prompt-engineering/**" --output "prompt-engineering-analysis.md"

# Version 5: Scripts & Automation Focus
echo "⚙️ Generating Scripts Analysis..."
repomix --include "99-scripts/**" --include "99-system/**" --include "**/*.js" --include "**/*.py" --output "scripts-analysis.md"

echo "✅ All analyses complete! Generated files:"
echo "- ai-code-analysis.md (Full analysis)"
echo "- system-analysis.md (Core PKB)"  
echo "- research-analysis.md (Research content)"
echo "- prompt-engineering-analysis.md (PE focus)"
echo "- scripts-analysis.md (Automation focus)"