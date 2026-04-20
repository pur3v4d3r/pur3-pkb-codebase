$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"

# Read file as raw bytes, decode as UTF-8
$bytes = [System.IO.File]::ReadAllBytes($file)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)
$lines = $content -split "`n"

Write-Host "Lines before: $($lines.Count)"
Write-Host ""

# ======================================================================
# FIX 1: Global encoding fix — replace garbled box-drawing characters
# â• (0xE2 0x95 interpreted as latin chars) should be ═ (U+2550)
# â†' should be → (U+2192)
# ======================================================================
Write-Host "--- FIX 1: Encoding fixes ---"

# Count garbled sequences
$garbledBox = ([regex]::Matches($content, 'â•')).Count
$garbledArrow = ([regex]::Matches($content, 'â†'')).Count
Write-Host "  Garbled box chars (â•): $garbledBox"
Write-Host "  Garbled arrows (â†'): $garbledArrow"

# The garbled pattern "â•" is actually the bytes E2 95 being interpreted differently
# In the file, these appear as the UTF-8 sequence for various box-drawing chars
# â• can map to several: â•═ â•â• â•â•â• etc.
# Let me do a more targeted replacement

# Replace full garbled comment line patterns
# Pattern: â•â•â•... (repeating) = ═══... (repeating U+2550)
$content = $content -replace 'â•', '═'
$content = $content -replace 'â†'', '→'

# Verify
$remaining = ([regex]::Matches($content, 'â•|â†'')).Count
Write-Host "  Remaining garbled: $remaining"

# ======================================================================
# FIX 2: PART 2 — Remove broken fragment + add missing selector
# Line ~413 has a truncated "/* ═══..." that never closes
# Lines ~422-426 are orphaned properties missing "body {" selector
# ======================================================================
Write-Host "--- FIX 2: PART 2 body selector ---"

# Remove the dangling "/* ═══════════════════════════════════════════════════════════════════════════" fragment
# It appears right before the PART 2 header
$content = $content -replace '(?m)^/\* ═{50,}\s*\n\s*\n\s*\n\s*\n/\* ═{50,}\s*\n\s+PART 2:', "/* ═══════════════════════════════════════════════════════════════════════════`n   PART 2:"

# Now fix: after PART 2 header closes, add "body {" + font-family before font-weight
$content = $content -replace '(PART 2: BASE TYPOGRAPHY \[TYPE\]\s*\n\s+Font families.*?\n\s+═{50,} \*/)\s*\n\s*\n\s+(font-weight: var\(--v4d3r-base-font-weight\))', "`$1`n`n   body {`n     font-family: var(--font-text) !important;`n     `$3"

Write-Host "  Applied"

# ======================================================================
# FIX 3: PART 8 — Add missing .menu-item selector
# Lines ~829-831 are orphaned properties missing ".menu-item {" selector
# ======================================================================
Write-Host "--- FIX 3: PART 8 .menu-item selector ---"

$content = $content -replace '(PART 8: MODALS, POPOVERS & NOTICES \[MODALS\]\s*\n\s+Modal dialogs.*?\n\s+═{50,} \*/)\s*\n\s*\n\s+(padding: var\(--v4d3r-space-sm\) var\(--v4d3r-space-md\))', "`$1`n`n   .menu-item {`n     color: var(--v4d3r-grey-light) !important;`n     `$3"

Write-Host "  Applied"

# ======================================================================
# FIX 4: PART 12 — Add missing /* before snippet metadata
# Lines ~1051-1070 are snippet metadata outside a comment
# ======================================================================
Write-Host "--- FIX 4: PART 12 snippet metadata comment ---"

$content = $content -replace '(PART 12: HEADINGS.*?\n\s+H1-H6.*?\n\s+═{50,} \*/)\s*\n\s*\n\s(Created: 2025)', "`$1`n`n/*`n `$2"

Write-Host "  Applied"

# ======================================================================
# FIX 5: PART 13 — Add missing code { selector
# Lines ~1223-1227 are orphaned properties missing "code {" selector
# ======================================================================
Write-Host "--- FIX 5: PART 13 code selector ---"

$content = $content -replace '(PART 13: INLINE CODE \[INLINE\]\s*\n\s+Inline code.*?\n\s+═{50,} \*/)\s*\n\s*\n\s+(padding: 2px 6px)', "`$1`n`n   code {`n     background-color: var(--v4d3r-grey-dark) !important;`n     color: var(--v4d3r-red-bright) !important;`n     `$2"

Write-Host "  Applied"

# ======================================================================
# FIX 6: PART 14 — Add missing /* before snippet metadata
# Lines ~1244-1256 snippet metadata outside a comment
# ======================================================================
Write-Host "--- FIX 6: PART 14 snippet metadata comment ---"

$content = $content -replace '(PART 14: CODE BLOCKS \[CODE\]\s*\n\s+Syntax highlighting.*?\n\s+═{50,} \*/)\s*\n\s*\n\s+(SNIPPET NAME:)', "`$1`n`n   /*`n    `$2"

Write-Host "  Applied"

# ======================================================================
# FIX 7: PART 17 — Add missing /* before snippet metadata
# Lines ~1759-1773 snippet metadata outside a comment
# ======================================================================
Write-Host "--- FIX 7: PART 17 snippet metadata comment ---"

$content = $content -replace '(PART 17: LISTS.*?═{50,} \*/)\s*\n\s*\n\s(SNIPPET NAME: Custom Ordered)', "`$1`n`n/*`n `$2"

Write-Host "  Applied"

# ======================================================================
# FIX 8: PART 18 area — Remove dangling /* fragment
# Line ~2119 has a lone "   /*" that wraps around the card mode header
# ======================================================================
Write-Host "--- FIX 8: PART 18 dangling comment ---"

$content = $content -replace '(═{50,} \*/)\s*\n\s*\n\s+/\*\s*\n\s*\n(/\* ═{40,}\s*\n\s+CARD MODE)', "`$1`n`n`$2"

Write-Host "  Applied"

# ======================================================================
# FIX 9: PART 19 area — Remove orphaned }
# Line ~2148 has an orphaned closing brace after the header comment
# ======================================================================
Write-Host "--- FIX 9: Orphaned closing brace ---"

$content = $content -replace '(PART 19: METADATA CONTAINER \[META\]\s*\n\s+YAML frontmatter.*?\n\s+═{50,} \*/)\s*\n\s*\n\}', "`$1"

Write-Host "  Applied"

# ======================================================================
# Write the fixed file
# ======================================================================

# Normalize line endings
$content = $content -replace "`r`n", "`n"
$content = $content -replace "`r", "`n"

# Write back as UTF-8 with BOM (Obsidian handles both, BOM ensures proper encoding)
[System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)

$newLines = ($content -split "`n").Count
Write-Host ""
Write-Host "Lines after: $newLines"
Write-Host "File saved with UTF-8 encoding."
