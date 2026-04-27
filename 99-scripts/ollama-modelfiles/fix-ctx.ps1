# fix-ctx.ps1 — Apply sane context limits to your Ollama models
# Run this in PowerShell: .\fix-ctx.ps1
# 
# RTX 4090 (24 GB VRAM) — KV cache math:
#   14B model  @ 8K ctx  -> ~2 GB KV  -> ~11 GB total  -> GPU ONLY  ✓
#   14B model  @ 16K ctx -> ~5 GB KV  -> ~14 GB total  -> GPU ONLY  ✓
#   30B model  @ 8K ctx  -> ~4 GB KV  -> ~22 GB total  -> GPU ONLY  ✓  (tight)
#   30B model  @ 16K ctx -> ~8 GB KV  -> ~26 GB total  -> SPLIT     ✗
#   30B model  @ 256K ctx -> enormous  -> FAILS / CRAWLS ✗

Write-Host "=== Fixing Ollama context windows for RTX 4090 (24 GB) ===" -ForegroundColor Cyan

$models = @(
    @{ name = "qwen2.5:14b";           base = "qwen2.5:14b";           ctx = 8192;  alias = "qwen2.5:14b-8k"  },
    @{ name = "qwen2.5-coder:14b";     base = "qwen2.5-coder:14b";     ctx = 8192;  alias = "qwen2.5-coder:14b-8k" },
    @{ name = "qwen3:14b";             base = "qwen3:14b";             ctx = 8192;  alias = "qwen3:14b-8k"    },
    @{ name = "qwen3:30b";             base = "qwen3:30b";             ctx = 8192;  alias = "qwen3:30b-8k"    },
    @{ name = "qwen3.6:27b";           base = "qwen3.6:27b";           ctx = 8192;  alias = "qwen3.6:27b-8k"  },
    @{ name = "qwen2.5-coder:32b";     base = "qwen2.5-coder:32b";     ctx = 4096;  alias = "qwen2.5-coder:32b-4k" },
    @{ name = "qwen3-coder:latest";    base = "qwen3-coder:latest";    ctx = 4096;  alias = "qwen3-coder-4k"  },
    @{ name = "deepseek-coder:33b";    base = "deepseek-coder:33b";    ctx = 4096;  alias = "deepseek-coder:33b-4k" },
    @{ name = "gemma3:27b-it-qat";     base = "gemma3:27b-it-qat";     ctx = 4096;  alias = "gemma3:27b-4k"   }
)

$tmpDir = "$env:TEMP\ollama-modelfiles"
New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null

foreach ($m in $models) {
    $mfPath = "$tmpDir\Modelfile_$($m.alias -replace '[:/]','-')"
    $content = @"
FROM $($m.base)
PARAMETER num_ctx $($m.ctx)
"@
    Set-Content -Path $mfPath -Value $content
    Write-Host "Creating $($m.alias) (ctx=$($m.ctx))..." -ForegroundColor Yellow
    & ollama create $($m.alias) -f $mfPath
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK: $($m.alias)" -ForegroundColor Green
    } else {
        Write-Host "  SKIP: $($m.base) not pulled yet" -ForegroundColor DarkGray
    }
}

Write-Host ""
Write-Host "=== Done! Run models with the -8k or -4k aliases ===" -ForegroundColor Cyan
Write-Host "  ollama run qwen3:30b-8k"
Write-Host "  ollama run qwen2.5:14b-8k"
Write-Host "  ollama run qwen2.5-coder:14b-8k"
Write-Host ""
Write-Host "Or set context per-session via environment var (Ollama 0.6+):"
Write-Host '  $env:OLLAMA_CONTEXT_LENGTH = "8192"'
Write-Host "  ollama run qwen3:30b"
