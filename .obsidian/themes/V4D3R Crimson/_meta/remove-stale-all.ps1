$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$lines = [System.Collections.ArrayList]@(Get-Content $file -Encoding UTF8)
Write-Host "Lines before: $($lines.Count)"

# Remove stale headers (work backwards to preserve indices)
# Each stale header is a 3-line block: preceding box line, text, following box line
# Plus surrounding blank lines where appropriate

# Targets (1-indexed line numbers of the text line):
# 1740: PART 26: GRAPH VIEW (lines 1739-1741)
# 1728: PART 22: HORIZONTAL RULES (lines 1727-1729)
# 1564: END OF SNIPPET (lines 1563-1565)
# 885: PART 12: SCROLLBARS (lines 884-886)
# 848: PART 11: BUTTONS & INTERACTIVE ELEMENTS (lines 847-849)
# 780: END OF PART 4 - Status Bar & Titlebar (lines 779-781)

# Work backwards to preserve line indices
$removals = @(
    @{Start=1739; Count=3; Desc="PART 26: GRAPH VIEW"},
    @{Start=1727; Count=3; Desc="PART 22: HORIZONTAL RULES"},
    @{Start=1563; Count=3; Desc="END OF SNIPPET"},
    @{Start=884; Count=3; Desc="PART 12: SCROLLBARS"},
    @{Start=847; Count=3; Desc="PART 11: BUTTONS & INTERACTIVE ELEMENTS"},
    @{Start=779; Count=3; Desc="END OF PART 4"}
)

foreach ($r in $removals) {
    $idx = $r.Start - 1  # Convert to 0-indexed
    Write-Host "Removing: $($r.Desc) (lines $($r.Start)-$($r.Start + $r.Count - 1))"
    Write-Host "  Content: $($lines[$idx]) | $($lines[$idx+1]) | $($lines[$idx+2])"
    $lines.RemoveRange($idx, $r.Count)
}

Write-Host "`nLines after: $($lines.Count)"

$lines | Set-Content $file -Encoding UTF8
Write-Host "File saved."
