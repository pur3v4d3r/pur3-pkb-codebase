$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$lines = Get-Content $file -Encoding UTF8
Write-Host "Total lines: $($lines.Count)"

# Find ALL lines containing 'PART 7' or 'PART' with box drawing characters
$toRemove = @()
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    # Find the OLD PART 7 header (the one with box drawing characters, not ═)
    if ($line -match '═══.*PART 7.*═══') {
        # This uses the Unicode box drawing char U+2550
        # Check if it's the one we WANT to keep (the new one at line ~690) or the OLD one
        # The new one uses ═══════ (regular equals-like box drawing)
        # The old one was inserted by the reorganize script and uses the same chars
        Write-Host "Found PART 7 box-drawing header at line $($i+1)"
    }
}

# Find lines with garbled characters that represent box drawing
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    if ($line -match 'PART 7: STATUS BAR' -and $i -gt 700) {
        Write-Host "PART 7 reference at line $($i+1): $($line.Substring(0, [Math]::Min(70, $line.Length)))"
        # Show surrounding lines
        for ($j = [Math]::Max(0, $i-2); $j -le [Math]::Min($lines.Count-1, $i+8); $j++) {
            $marker = if ($j -eq $i) { ">>>" } else { "   " }
            Write-Host "$marker $($j+1): $($lines[$j].Substring(0, [Math]::Min(80, $lines[$j].Length)))"
        }
        Write-Host "---"
    }
}
