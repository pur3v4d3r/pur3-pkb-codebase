# Multi-Version Repomix Analysis Script (PowerShell)

Write-Host "🚀 Starting Multi-Version Analysis..." -ForegroundColor Cyan

# Version 1: Core PKB System Analysis
Write-Host "📊 Generating Core PKB Analysis..." -ForegroundColor Yellow
repomix --config repomix-system.config.json

# Version 2: Research Content Analysis  
Write-Host "📚 Generating Research Content Analysis..." -ForegroundColor Yellow
repomix --config repomix-research.config.json

# Version 3: Full AI-Optimized Analysis
Write-Host "🧠 Generating Full AI Analysis..." -ForegroundColor Yellow
repomix

# Version 4: Prompt Engineering Focus
Write-Host "🎯 Generating Prompt Engineering Analysis..." -ForegroundColor Yellow
repomix --include "999-v4d3r/**" --include "__agents/**" --include "04-library/03-prompt-engineering/**" --output "prompt-engineering-analysis.md"

# Version 5: Scripts & Automation Focus
Write-Host "⚙️ Generating Scripts Analysis..." -ForegroundColor Yellow
repomix --include "99-scripts/**" --include "99-system/**" --include "**/*.js" --include "**/*.py" --output "scripts-analysis.md"

Write-Host "✅ All analyses complete! Generated files:" -ForegroundColor Green
Write-Host "- ai-code-analysis.md (Full analysis)" -ForegroundColor White
Write-Host "- system-analysis.md (Core PKB)" -ForegroundColor White
Write-Host "- research-analysis.md (Research content)" -ForegroundColor White  
Write-Host "- prompt-engineering-analysis.md (PE focus)" -ForegroundColor White
Write-Host "- scripts-analysis.md (Automation focus)" -ForegroundColor White