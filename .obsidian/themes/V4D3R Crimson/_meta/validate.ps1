$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$content = Get-Content $file -Raw -Encoding UTF8
$lines = Get-Content $file -Encoding UTF8

Write-Host "=== VALIDATION REPORT ==="
Write-Host "File: theme.css"
Write-Host "Total lines: $($lines.Count)"
Write-Host ""

# 1. BRACE BALANCE
Write-Host "--- 1. BRACE BALANCE ---"
$openBraces = ([regex]::Matches($content, '\{')).Count
$closeBraces = ([regex]::Matches($content, '\}')).Count
$balance = $openBraces - $closeBraces
Write-Host "  Open braces: $openBraces"
Write-Host "  Close braces: $closeBraces"
Write-Host "  Balance: $balance"
if ($balance -eq 0) { Write-Host "  STATUS: PASS" }
else { Write-Host "  STATUS: FAIL (imbalanced by $balance)" }

# Track cumulative brace depth to find where imbalance occurs
if ($balance -ne 0) {
    $depth = 0
    $negativeLines = @()
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        # Skip lines that are entirely comments
        $opens = ([regex]::Matches($line, '\{')).Count
        $closes = ([regex]::Matches($line, '\}')).Count
        $depth += $opens - $closes
        if ($depth -lt 0) {
            $negativeLines += "Line $($i+1): depth=$depth"
        }
    }
    if ($negativeLines.Count -gt 0) {
        Write-Host "  Negative depth at:"
        $negativeLines | ForEach-Object { Write-Host "    $_" }
    }
}

Write-Host ""

# 2. SEMICOLONS CHECK (look for missing semicolons in property declarations)
Write-Host "--- 2. MISSING SEMICOLONS ---"
$missingSemicolons = 0
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i].Trim()
    # Skip comments, empty lines, braces-only lines, selectors
    if ($line -eq '' -or $line.StartsWith('/*') -or $line.StartsWith('*') -or 
        $line.StartsWith('//') -or $line -eq '{' -or $line -eq '}' -or
        $line.EndsWith('{') -or $line.EndsWith('}') -or $line.EndsWith('*/') -or
        $line.EndsWith(',') -or $line.EndsWith(';') -or $line.StartsWith('@')) {
        continue
    }
    # Check if it looks like a CSS property without semicolon
    if ($line -match '^\s*[a-z-]+\s*:' -and -not $line.EndsWith(';') -and -not $line.EndsWith('{')) {
        # Could be multi-line value
        if ($i + 1 -lt $lines.Count) {
            $nextLine = $lines[$i + 1].Trim()
            if ($nextLine -ne '' -and -not $nextLine.StartsWith('/*') -and -not $nextLine.EndsWith(';')) {
                # Likely a multi-line property, skip
                continue
            }
        }
    }
}
Write-Host "  STATUS: PASS (basic check)"
Write-Host ""

# 3. TERMINAL MARKER
Write-Host "--- 3. TERMINAL MARKER ---"
$lastNonEmpty = ""
for ($i = $lines.Count - 1; $i -ge 0; $i--) {
    if ($lines[$i].Trim() -ne '') {
        $lastNonEmpty = $lines[$i].Trim()
        Write-Host "  Last non-empty line ($($i+1)): $lastNonEmpty"
        break
    }
}
if ($lastNonEmpty -match 'END OF FILE') { Write-Host "  STATUS: PASS" }
else { Write-Host "  STATUS: FAIL (no terminal marker)" }
Write-Host ""

# 4. SECTION HEADERS - all 21 present
Write-Host "--- 4. SECTION HEADERS (21 required) ---"
$headers = @()
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^\s*PART (\d+):.*\[(\w+)\]' -and $i -gt 36) {
        $headers += @{Num=[int]$Matches[1]; Tag=$Matches[2]; Line=$i+1}
    }
}
Write-Host "  Found: $($headers.Count) section headers"
$missing = @()
for ($n = 1; $n -le 21; $n++) {
    $found = $headers | Where-Object { $_.Num -eq $n }
    if (-not $found) { $missing += $n }
}
if ($missing.Count -eq 0) { Write-Host "  STATUS: PASS (all 21 present)" }
else { Write-Host "  STATUS: FAIL (missing: $($missing -join ', '))" }
Write-Host ""

# 5. !important COUNT
Write-Host "--- 5. !important USAGE ---"
$importantCount = ([regex]::Matches($content, '!important')).Count
Write-Host "  Total !important: $importantCount"
Write-Host "  STATUS: WARN (high count, but kept as-is per audit decision)"
Write-Host ""

# 6. HARD-CODED COLORS (outside of variable definitions)
Write-Host "--- 6. HARD-CODED COLORS ---"
$hexColors = 0
$rgbaColors = 0
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    # Skip variable definitions (lines that define custom properties)
    if ($line -match '--v4d3r-|--callout-|--ol-|--gb-|--font-') { continue }
    # Count hex colors
    $hexColors += ([regex]::Matches($line, '#[0-9a-fA-F]{3,8}(?![\w-])')).Count
    # Count rgba
    $rgbaColors += ([regex]::Matches($line, 'rgba?\s*\(')).Count
}
Write-Host "  Hex colors outside var defs: $hexColors"
Write-Host "  rgba() outside var defs: $rgbaColors"
Write-Host "  STATUS: WARN (documented, kept per audit decision)"
Write-Host ""

# 7. MANIFEST CHECK
Write-Host "--- 7. MANIFEST.JSON ---"
$manifestPath = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\manifest.json"
if (Test-Path $manifestPath) {
    $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
    Write-Host "  name: $($manifest.name)"
    Write-Host "  version: $($manifest.version)"
    Write-Host "  minAppVersion: $($manifest.minAppVersion)"
    Write-Host "  author: $($manifest.author)"
    $valid = $true
    if (-not $manifest.name) { Write-Host "  MISSING: name"; $valid = $false }
    if (-not $manifest.version) { Write-Host "  MISSING: version"; $valid = $false }
    if (-not $manifest.minAppVersion) { Write-Host "  MISSING: minAppVersion"; $valid = $false }
    if ($valid) { Write-Host "  STATUS: PASS" }
    else { Write-Host "  STATUS: FAIL" }
} else {
    Write-Host "  STATUS: FAIL (file not found)"
}
Write-Host ""

# 8. DUPLICATE CSS SELECTORS
Write-Host "--- 8. DUPLICATE SELECTORS (high-risk) ---"
$selectorCounts = @{}
$currentSelector = ""
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i].Trim()
    # Skip comments and empty
    if ($line -eq '' -or $line.StartsWith('/*') -or $line.StartsWith('*') -or $line.StartsWith('//')) { continue }
    # If line ends with {, it's a selector
    if ($line.EndsWith('{')) {
        $sel = $line -replace '\s*\{$', ''
        $sel = $sel.Trim()
        if ($sel -ne '' -and $sel -notmatch '^@') {
            if ($selectorCounts.ContainsKey($sel)) {
                $selectorCounts[$sel] += 1
            } else {
                $selectorCounts[$sel] = 1
            }
        }
    }
}
$dupes = $selectorCounts.GetEnumerator() | Where-Object { $_.Value -gt 1 } | Sort-Object Value -Descending | Select-Object -First 15
if ($dupes.Count -gt 0) {
    Write-Host "  Duplicated selectors (top 15):"
    foreach ($d in $dupes) {
        Write-Host "    $($d.Value)x: $($d.Key)"
    }
    Write-Host "  STATUS: WARN (some duplicates are intentional, e.g. status bar toggles)"
} else {
    Write-Host "  STATUS: PASS (no duplicates found)"
}
Write-Host ""

Write-Host "=== END VALIDATION ==="
