# Fix all CSS errors in V4D3R Crimson theme
# Uses byte-level matching to avoid encoding issues

$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"

# Read as raw bytes
$bytes = [System.IO.File]::ReadAllBytes($file)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)

Write-Host "Characters before: $($content.Length)"

# ======================================================================
# STEP 1: Fix garbled box-drawing characters
# The garbled sequence for U+2550 (DOUBLE HORIZONTAL) shows as 3-byte garbage
# We need to find and replace the garbled UTF-8 sequences
# ======================================================================

# Approach: Find lines containing the garbled pattern and replace the entire line
# The garbled chars show as sequences that aren't valid box-drawing
# Let's identify them by looking for the pattern in the actual bytes

# First, let's see what the garbled chars actually are in the string
$lines = $content -split "`n"
$garbledLines = @()
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    # Check for garbled box chars - they contain char 0x2551 or sequences with char 9552+
    # The garbled "a with circumflex" (U+00E2) followed by bullet (U+2022 or similar)
    if ($line -match '\xE2\x95') {
        # This matches the raw UTF-8 bytes for box-drawing chars being double-decoded
        $garbledLines += $i
    }
}

Write-Host "Found garbled lines by byte pattern: $($garbledLines.Count)"

# Alternative: just replace at string level
# The garbled chars appear as specific Unicode sequences
# Let's check what codepoints they actually are
$sampleLine = $lines[0]
foreach ($idx in $garbledLines | Select-Object -First 1) {
    $sampleLine = $lines[$idx]
    $chars = $sampleLine.ToCharArray()
    $nonAscii = @()
    foreach ($c in $chars) {
        $cp = [int]$c
        if ($cp -gt 127) {
            $nonAscii += "U+$($cp.ToString('X4'))"
        }
    }
    Write-Host "Non-ASCII chars in garbled line $idx : $($nonAscii -join ' ')"
}

Write-Host "Done analyzing"
