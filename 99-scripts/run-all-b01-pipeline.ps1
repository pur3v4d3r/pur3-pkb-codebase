#!/usr/bin/env pwsh
# Run pipeline_v6.py on all 11 b01 seed batches sequentially
# NO DRY RUN - default --mode skip auto-skips existing notes

$PYTHON = "D:\10_pur3v4d3r's-vault\.venv\Scripts\python.exe"
$PIPELINE_DIR = "D:\10_pur3v4d3r's-vault\99-scripts\report-extraction-to-permanent-notes-building-v6"
$SEEDS_BASE = "D:\10_pur3v4d3r's-vault\999-report-organizing\_extractor-output\_synthetic-seeds"
$RUNS_DIR = "$PIPELINE_DIR\runs"

# Ensure runs directory exists
New-Item -ItemType Directory -Force -Path $RUNS_DIR | Out-Null

Set-Location $PIPELINE_DIR

$batches = @(
    "2026-05-21-b01-01-finetuning-adaptation",
    "2026-05-21-b01-02-alignment-safety",
    "2026-05-21-b01-03-decoding-sampling",
    "2026-05-21-b01-04-context-memory",
    "2026-05-21-b01-05-multimodal",
    "2026-05-21-b01-06-structured-output",
    "2026-05-21-b01-07-evaluation",
    "2026-05-21-b01-08-agents-tools",
    "2026-05-21-b01-09-security",
    "2026-05-21-b01-10-theoretical",
    "2026-05-21-b01-11-system-design"
)

$total_batches = $batches.Count
$batch_num = 0

foreach ($batch in $batches) {
    $batch_num++
    $input_dir = "$SEEDS_BASE\$batch"
    $log_file = "$RUNS_DIR\$batch-log.json"
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "BATCH $batch_num/${total_batches}: $batch" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Input: $input_dir"
    Write-Host "Log:   $log_file"
    Write-Host ""
    
    if (-not (Test-Path $input_dir)) {
        Write-Host "WARNING: Input directory not found, skipping: $input_dir" -ForegroundColor Yellow
        continue
    }
    
    & $PYTHON pipeline_v6.py `
        --input-dir $input_dir `
        --report-runs $log_file `
        -v
    
    $exit_code = $LASTEXITCODE
    if ($exit_code -eq 0) {
        Write-Host "BATCH $batch_num COMPLETE: $batch" -ForegroundColor Green
    } else {
        Write-Host "BATCH $batch_num FAILED (exit $exit_code): $batch" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ALL BATCHES COMPLETE" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
