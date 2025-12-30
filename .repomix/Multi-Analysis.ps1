function Generate-MultiAnalysis {
    param(
        [string]$BaseOutput = "analysis",
        [switch]$Verbose
    )
    
    $configs = @{
        "full" = @{
            include = @("00-meta/**", "999-codebase+pkb/**", "999-v4d3r/**", "99-scripts/**")
            output = "$BaseOutput-full.md"
            header = "# 🧠 Complete Vault Analysis"
        }
        "research" = @{
            include = @("02-projects/**", "03-notes/**", "04-library/**", "07-mocs/**")
            output = "$BaseOutput-research.md" 
            header = "# 📚 Research Content Analysis"
        }
        "system" = @{
            include = @("99-scripts/**", "99-system/**", "__agents/**")
            output = "$BaseOutput-system.md"
            header = "# ⚙️ System Architecture"
        }
        "prompts" = @{
            include = @("999-v4d3r/**", "__agents/**", "04-library/03-prompt-engineering/**")
            output = "$BaseOutput-prompts.md"
            header = "# 🎯 Prompt Engineering"
        }
    }
    
    Write-Host "🚀 Starting Multi-Analysis Generation..." -ForegroundColor Cyan
    
    foreach ($type in $configs.Keys) {
        $config = $configs[$type]
        Write-Host "📊 Generating $type analysis..." -ForegroundColor Yellow
        
        $includeArgs = $config.include | ForEach-Object { "--include", $_ }
        $args = @($includeArgs) + @("--output", $config.output)
        
        if ($Verbose) {
            $args += "--verbose"
        }
        
        & repomix @args
    }
    
    Write-Host "✅ Multi-analysis complete!" -ForegroundColor Green
    $configs.Values | ForEach-Object { 
        Write-Host "- $($_.output)" -ForegroundColor White 
    }
}

# Usage examples:
# Generate-MultiAnalysis
# Generate-MultiAnalysis -BaseOutput "vault-analysis" -Verbose