$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$lines = Get-Content $file -Encoding UTF8
Write-Host "Total lines: $($lines.Count)"

# Show context around each stale reference
$targets = @(780, 848, 885, 1564, 1728, 1740)

foreach ($lineNum in $targets) {
    $idx = $lineNum - 1
    Write-Host "`n=== LINE $lineNum ==="
    $start = [Math]::Max(0, $idx - 2)
    $end = [Math]::Min($lines.Count - 1, $idx + 2)
    for ($i = $start; $i -le $end; $i++) {
        $marker = if ($i -eq $idx) { ">>>" } else { "   " }
        $text = $lines[$i]
        if ($text.Length -gt 90) { $text = $text.Substring(0, 90) + "..." }
        Write-Host "$marker $($i+1): $text"
    }
}
