$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$lines = [System.Collections.ArrayList]@(Get-Content $file -Encoding UTF8)
Write-Host "Lines before: $($lines.Count)"

# Remove lines 708-717 (0-indexed: 707-716) — the old misplaced PART 7 header and orphaned CSS
# Line 708: /* box-drawing chars
# Line 709: PART 7: STATUS BAR [STATUS]
# Line 710: Status bar base, fade...
# Line 711: Each toggle section...
# Line 712: box-drawing chars */
# Line 713: (blank)
# Line 714: orphaned CSS color property
# Line 715: .status-bar-item:hover {
# Line 716: color: var(...)}
# Line 717: /* --- END TOGGLE: Status Bar Base --- */

$removeStart = 707  # 0-indexed line 708
$removeEnd = 716    # 0-indexed line 717
$removeCount = $removeEnd - $removeStart + 1

Write-Host "Removing lines $($removeStart+1) to $($removeEnd+1) ($removeCount lines)"
Write-Host "Content being removed:"
for ($i = $removeStart; $i -le $removeEnd; $i++) {
    Write-Host "  $($i+1): $($lines[$i])"
}

$lines.RemoveRange($removeStart, $removeCount)

Write-Host "`nLines after: $($lines.Count)"

# Verify the line before and after the removed section
Write-Host "`nContext after removal:"
for ($i = [Math]::Max(0, $removeStart-3); $i -le [Math]::Min($lines.Count-1, $removeStart+3); $i++) {
    Write-Host "  $($i+1): $($lines[$i].Substring(0, [Math]::Min(80, $lines[$i].Length)))"
}

# Write the file back
$lines | Set-Content $file -Encoding UTF8
Write-Host "`nFile saved successfully."
