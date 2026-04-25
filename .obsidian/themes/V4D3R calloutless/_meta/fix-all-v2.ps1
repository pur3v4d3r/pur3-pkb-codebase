# Comprehensive fix script for V4D3R Crimson theme.css
# Fixes: garbled encoding, missing selectors, missing comment openers, orphan braces

$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

Write-Host "Characters before: $($content.Length)"

# ======================================================================
# STEP 1: Fix garbled box-drawing characters
# Garbled: U+00E2 U+2022 U+0090 -> should be U+2550 (BOX DRAWINGS DOUBLE HORIZONTAL)
# ======================================================================
Write-Host "`n--- STEP 1: Fix garbled encoding ---"

$garbled_box = [char]0x00E2 + [string][char]0x2022 + [string][char]0x0090
$correct_box = [string][char]0x2550

$countBefore = 0
$idx = 0
while (($idx = $content.IndexOf($garbled_box, $idx)) -ge 0) {
    $countBefore++
    $idx += $garbled_box.Length
}
Write-Host "  Garbled box sequences found: $countBefore"

$content = $content.Replace($garbled_box, $correct_box)

# Also fix garbled arrows: U+00E2 U+2020 U+2019 -> U+2192
$garbled_arrow = [char]0x00E2 + [string][char]0x2020 + [string][char]0x2019
$correct_arrow = [string][char]0x2192

$arrowCount = 0
$idx = 0
while (($idx = $content.IndexOf($garbled_arrow, $idx)) -ge 0) {
    $arrowCount++
    $idx += $garbled_arrow.Length
}
Write-Host "  Garbled arrow sequences found: $arrowCount"

$content = $content.Replace($garbled_arrow, $correct_arrow)

# Verify
$remainBox = 0
$idx = 0
while (($idx = $content.IndexOf($garbled_box, $idx)) -ge 0) { $remainBox++; $idx++ }
$remainArrow = 0
$idx = 0
while (($idx = $content.IndexOf($garbled_arrow, $idx)) -ge 0) { $remainArrow++; $idx++ }
Write-Host "  Remaining garbled: box=$remainBox arrow=$remainArrow"

# ======================================================================
# STEP 2: Fix PART 2 — remove broken comment fragment + add body selector
# ======================================================================
Write-Host "`n--- STEP 2: Fix PART 2 (body selector) ---"

# The pattern: /* ═══...═══\n\n\n\n/* ═══...═══\n   PART 2:
# Remove the first dangling "/* ═══..." that was never closed
# And add "body {" + "font-family" before the orphaned properties
$oldPart2 = @"
/* ═══════════════════════════════════════════════════════════════════════════



/* ═══════════════════════════════════════════════════════════════════════════
   PART 2: BASE TYPOGRAPHY [TYPE]
   Font families, sizes, weights for body text, editor, and interface
   ═══════════════════════════════════════════════════════════════════════════ */

     font-weight: var(--v4d3r-base-font-weight) !important;
"@

$newPart2 = @"
/* ═══════════════════════════════════════════════════════════════════════════
   PART 2: BASE TYPOGRAPHY [TYPE]
   Font families, sizes, weights for body text, editor, and interface
   ═══════════════════════════════════════════════════════════════════════════ */

   body {
     font-family: var(--font-text) !important;
     font-weight: var(--v4d3r-base-font-weight) !important;
"@

if ($content.Contains($oldPart2)) {
    $content = $content.Replace($oldPart2, $newPart2)
    Write-Host "  APPLIED: Removed fragment, added body selector + font-family"
} else {
    Write-Host "  SKIPPED: Pattern not found (may already be fixed or different whitespace)"
    # Try to find partial matches for debugging
    if ($content.Contains("/* ═══════════════════════════════════════════════════════════════════════════`n`n`n")) {
        Write-Host "  DEBUG: Found the dangling fragment but full pattern mismatch"
    }
}

# ======================================================================
# STEP 3: Fix PART 8 — add .menu-item selector
# ======================================================================
Write-Host "`n--- STEP 3: Fix PART 8 (.menu-item selector) ---"

$oldPart8 = @"
   ═══════════════════════════════════════════════════════════════════════════ */

     padding: var(--v4d3r-space-sm) var(--v4d3r-space-md) !important;
     border-radius: var(--v4d3r-radius-sm) !important;
     transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
   }
"@

$newPart8 = @"
   ═══════════════════════════════════════════════════════════════════════════ */

   .menu-item {
     color: var(--v4d3r-grey-light) !important;
     padding: var(--v4d3r-space-sm) var(--v4d3r-space-md) !important;
     border-radius: var(--v4d3r-radius-sm) !important;
     transition: all var(--v4d3r-transition-fast) var(--v4d3r-ease-default) !important;
   }
"@

# This pattern appears in PART 8 context - need to be precise
# Find it after "PART 8:" text
$part8Idx = $content.IndexOf("PART 8: MODALS")
if ($part8Idx -ge 0) {
    $afterPart8 = $content.Substring($part8Idx)
    $searchStr = "*/`n`n     padding: var(--v4d3r-space-sm)"
    $replStr  = "*/`n`n   .menu-item {`n     color: var(--v4d3r-grey-light) !important;`n     padding: var(--v4d3r-space-sm)"
    
    if ($afterPart8.Contains($searchStr)) {
        $fixed = $afterPart8.Replace($searchStr, $replStr)
        $content = $content.Substring(0, $part8Idx) + $fixed
        Write-Host "  APPLIED: Added .menu-item selector + color property"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 8"
    }
} else {
    Write-Host "  SKIPPED: PART 8 header not found"
}

# ======================================================================
# STEP 4: Fix PART 12 — add /* before snippet metadata
# ======================================================================
Write-Host "`n--- STEP 4: Fix PART 12 (comment opener) ---"

$part12Idx = $content.IndexOf("PART 12: HEADINGS")
if ($part12Idx -ge 0) {
    $searchStr12 = "*/`n`n Created: 2025-12-29"
    $replStr12 = "*/`n`n/*`n Created: 2025-12-29"
    
    $afterPart12 = $content.Substring($part12Idx)
    if ($afterPart12.Contains($searchStr12)) {
        $fixed = $afterPart12.Replace($searchStr12, $replStr12)
        $content = $content.Substring(0, $part12Idx) + $fixed
        Write-Host "  APPLIED: Added /* before snippet metadata"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 12"
    }
} else {
    Write-Host "  SKIPPED: PART 12 header not found"
}

# ======================================================================
# STEP 5: Fix PART 13 — add code { selector
# ======================================================================
Write-Host "`n--- STEP 5: Fix PART 13 (code selector) ---"

$part13Idx = $content.IndexOf("PART 13: INLINE CODE")
if ($part13Idx -ge 0) {
    $searchStr13 = "*/`n`n     padding: 2px 6px !important;"
    $replStr13 = "*/`n`n   code {`n     background-color: var(--v4d3r-grey-dark) !important;`n     color: var(--v4d3r-red-bright) !important;`n     padding: 2px 6px !important;"
    
    $afterPart13 = $content.Substring($part13Idx)
    if ($afterPart13.Contains($searchStr13)) {
        $fixed = $afterPart13.Replace($searchStr13, $replStr13)
        $content = $content.Substring(0, $part13Idx) + $fixed
        Write-Host "  APPLIED: Added code selector + bg/color properties"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 13"
    }
} else {
    Write-Host "  SKIPPED: PART 13 header not found"
}

# ======================================================================
# STEP 6: Fix PART 14 — add /* before snippet metadata
# ======================================================================
Write-Host "`n--- STEP 6: Fix PART 14 (comment opener) ---"

$part14Idx = $content.IndexOf("PART 14: CODE BLOCKS")
if ($part14Idx -ge 0) {
    $searchStr14 = "*/`n`n    SNIPPET NAME:"
    $replStr14 = "*/`n`n   /*`n    SNIPPET NAME:"
    
    $afterPart14 = $content.Substring($part14Idx)
    if ($afterPart14.Contains($searchStr14)) {
        $fixed = $afterPart14.Replace($searchStr14, $replStr14)
        $content = $content.Substring(0, $part14Idx) + $fixed
        Write-Host "  APPLIED: Added /* before snippet metadata"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 14"
    }
} else {
    Write-Host "  SKIPPED: PART 14 header not found"
}

# ======================================================================
# STEP 7: Fix PART 17 — add /* before snippet metadata
# ======================================================================
Write-Host "`n--- STEP 7: Fix PART 17 (comment opener) ---"

$part17Idx = $content.IndexOf("PART 17: LISTS")
if ($part17Idx -ge 0) {
    $searchStr17 = "*/`n`n SNIPPET NAME: Custom Ordered"
    $replStr17 = "*/`n`n/*`n SNIPPET NAME: Custom Ordered"
    
    $afterPart17 = $content.Substring($part17Idx)
    if ($afterPart17.Contains($searchStr17)) {
        $fixed = $afterPart17.Replace($searchStr17, $replStr17)
        $content = $content.Substring(0, $part17Idx) + $fixed
        Write-Host "  APPLIED: Added /* before snippet metadata"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 17"
    }
} else {
    Write-Host "  SKIPPED: PART 17 header not found"
}

# ======================================================================
# STEP 8: Fix PART 18 — remove dangling /* fragment
# ======================================================================
Write-Host "`n--- STEP 8: Fix PART 18 (dangling /*) ---"

$part18Idx = $content.IndexOf("PART 18: HORIZONTAL")
if ($part18Idx -ge 0) {
    # After the PART 18 header close, there's:   /*   \n\n/* ═══...CARD MODE
    # Remove the lone "   /*"
    $searchStr18 = "*/`n`n`n   /*`n`n/* ═"
    $replStr18 = "*/`n`n/* ═"
    
    $afterPart18 = $content.Substring($part18Idx)
    if ($afterPart18.Contains($searchStr18)) {
        $fixed = $afterPart18.Replace($searchStr18, $replStr18)
        $content = $content.Substring(0, $part18Idx) + $fixed
        Write-Host "  APPLIED: Removed dangling /* fragment"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 18"
    }
} else {
    Write-Host "  SKIPPED: PART 18 header not found"
}

# ======================================================================
# STEP 9: Fix PART 19 — remove orphaned }
# ======================================================================
Write-Host "`n--- STEP 9: Fix orphaned closing brace ---"

$part19Idx = $content.IndexOf("PART 19: METADATA")
if ($part19Idx -ge 0) {
    $searchStr19 = "*/`n`n}`n`n.metadata-property-value"
    $replStr19 = "*/`n`n.metadata-property-value"
    
    $afterPart19 = $content.Substring($part19Idx)
    if ($afterPart19.Contains($searchStr19)) {
        $fixed = $afterPart19.Replace($searchStr19, $replStr19)
        $content = $content.Substring(0, $part19Idx) + $fixed
        Write-Host "  APPLIED: Removed orphaned closing brace"
    } else {
        Write-Host "  SKIPPED: Pattern not found after PART 19"
    }
} else {
    Write-Host "  SKIPPED: PART 19 header not found"
}

# ======================================================================
# SAVE
# ======================================================================
Write-Host "`n--- SAVING ---"
[System.IO.File]::WriteAllText($file, $content, (New-Object System.Text.UTF8Encoding $false))

$lineCount = ($content -split "`n").Count
Write-Host "Lines after: $lineCount"
Write-Host "File saved (UTF-8 no BOM)."
