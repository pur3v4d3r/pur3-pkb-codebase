$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$lines = Get-Content $file -Encoding UTF8
$depth = 0
$inComment = $false
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    
    # Handle multi-line comments (skip braces inside comments)
    if ($inComment) {
        if ($line -match '\*/') {
            $inComment = $false
        }
        continue
    }
    if ($line -match '/\*' -and $line -notmatch '\*/') {
        $inComment = $true
        # Still count braces before the comment start on this line
        $beforeComment = $line.Substring(0, $line.IndexOf('/*'))
        $opens = ([regex]::Matches($beforeComment, '\{')).Count
        $closes = ([regex]::Matches($beforeComment, '\}')).Count
        $depth += $opens - $closes
        continue
    }
    
    # For non-comment lines, strip inline comments
    $cleaned = $line
    if ($cleaned -match '/\*.*\*/') {
        $cleaned = $cleaned -replace '/\*.*?\*/', ''
    }
    
    $opens = ([regex]::Matches($cleaned, '\{')).Count
    $closes = ([regex]::Matches($cleaned, '\}')).Count
    $prevDepth = $depth
    $depth += $opens - $closes
    
    if ($depth -lt 0) {
        Write-Host "NEGATIVE at line $($i+1): depth=$depth (was $prevDepth) | $($line.Trim().Substring(0, [Math]::Min(80, $line.Trim().Length)))"
    }
    if ($depth -lt $prevDepth -and $prevDepth -eq 0 -and $depth -lt 0) {
        Write-Host "  >>> EXTRA CLOSING BRACE <<<"
    }
}
Write-Host "`nFinal depth: $depth"
