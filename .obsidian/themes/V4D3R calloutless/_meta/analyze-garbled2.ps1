# Analyze garbled characters by examining specific known lines
$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$lines = Get-Content $file -Encoding UTF8

# Line 416 (0-indexed 415) should contain the garbled PART 2 header
# Line numbers from errors: 423 area
# Let's find lines containing "PART 2:" and look at surrounding lines
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match 'PART 2:') {
        Write-Host "Line $($i+1): $($lines[$i])"
        # Check the line above
        if ($i -gt 0) {
            $prevLine = $lines[$i-1]
            Write-Host "Line $i (prev): length=$($prevLine.Length)"
            $chars = $prevLine.ToCharArray()
            $nonAscii = @()
            for ($j = 0; $j -lt [Math]::Min(10, $chars.Count); $j++) {
                $cp = [int]$chars[$j]
                $nonAscii += "pos$j=U+$($cp.ToString('X4'))($([char]$cp))"
            }
            Write-Host "  First 10 chars: $($nonAscii -join ' ')"
        }
    }
}

# Also check what "good" box-drawing lines look like
Write-Host ""
Write-Host "--- Good box-drawing chars ---"
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match 'CARD MODE FOR WORKSPACE') {
        $headerLine = $lines[$i-1]
        Write-Host "Line $i (prev): length=$($headerLine.Length)"
        $chars = $headerLine.ToCharArray()
        $nonAscii = @()
        for ($j = 0; $j -lt [Math]::Min(15, $chars.Count); $j++) {
            $cp = [int]$chars[$j]
            $nonAscii += "pos$j=U+$($cp.ToString('X4'))($([char]$cp))"
        }
        Write-Host "  First 15 chars: $($nonAscii -join ' ')"
    }
}
