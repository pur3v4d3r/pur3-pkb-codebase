## V4D3R Crimson Theme Reorganizer
## Reads backup, extracts sections in order, removes duplicates, writes clean theme.css

$backupPath = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\_meta\theme.css.bak"
$outputPath = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"

# Read all lines from backup
$lines = Get-Content -Path $backupPath -Encoding UTF8

# Helper: extract line range (1-indexed, inclusive)
function Get-Lines {
    param([int]$start, [int]$end)
    $lines[($start-1)..($end-1)]
}

# Helper: trim excessive blank lines (max 2 consecutive)
function Trim-Blanks {
    param([string[]]$content)
    $result = @()
    $blankCount = 0
    foreach ($line in $content) {
        if ($line.Trim() -eq '') {
            $blankCount++
            if ($blankCount -le 2) { $result += $line }
        } else {
            $blankCount = 0
            $result += $line
        }
    }
    # Trim trailing blanks
    while ($result.Count -gt 0 -and $result[-1].Trim() -eq '') {
        $result = $result[0..($result.Count-2)]
    }
    return $result
}

# Build the new theme file
$output = @()

# ═══════════════════════════════════════════════════════════════════════════
# MASTER HEADER
# ═══════════════════════════════════════════════════════════════════════════
$output += @"
/* ═══════════════════════════════════════════════════════════════════════════
   V4D3R CRIMSON THEME v1.1.0
   Author: Pur3v4d3r
   License: MIT
   Min Obsidian: 1.5.0+

   A dark theme featuring a Red/Black/Grey color palette with JetBrains Mono
   typography, glowing headers, enhanced code blocks, and the Ultimate
   Callout System v5.0 (150+ callout types).

   ═══════════════════════════════════════════════════════════════════════════
   TABLE OF CONTENTS
   ═══════════════════════════════════════════════════════════════════════════
   PART 1:  Foundation Variables ...................... [VARS]
   PART 2:  Base Typography ........................... [TYPE]
   PART 3:  Reading Width & Text Formatting ........... [TEXT]
   PART 4:  Workspace & Layout ........................ [LAYOUT]
   PART 5:  File Explorer ............................. [EXPLORER]
   PART 6:  Sidebars & Navigation .................... [NAV]
   PART 7:  Status Bar ................................ [STATUS]
   PART 8:  Modals, Popovers & Notices ............... [MODALS]
   PART 9:  Buttons & Interactive Elements ........... [BUTTONS]
   PART 10: Scrollbars ................................ [SCROLL]
   PART 11: Search .................................... [SEARCH]
   PART 12: Headings (Glowing Headers) ............... [HEADINGS]
   PART 13: Inline Code ............................... [INLINE]
   PART 14: Code Blocks ............................... [CODE]
   PART 15: Glowing Brackets ......................... [BRACKETS]
   PART 16: Tables .................................... [TABLES]
   PART 17: Lists (Ordered & Unordered) .............. [LISTS]
   PART 18: Horizontal Rules, Graph & Card Mode ...... [MISC]
   PART 19: Metadata Container ....................... [META]
   PART 20: Callout System (Ultimate v5.0) ........... [CALLOUTS]
   PART 21: Accessibility & Reduced Motion ........... [A11Y]
   ═══════════════════════════════════════════════════════════════════════════ */

"@


# ═══════════════════════════════════════════════════════════════════════════
# PART 1: Foundation Variables [VARS]
# Source: Lines 1-388 (Block 1, the detailed version)
# Removed: Lines 389-560 (duplicate Block 2 with conflicting values)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 1: FOUNDATION VARIABLES [VARS]
   Single source of truth for all theme variables
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 1 388)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 2: Base Typography [TYPE]
# Source: Lines 561-610
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 2: BASE TYPOGRAPHY [TYPE]
   Font families, sizes, weights for body text, editor, and interface
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 561 610)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 3: Reading Width & Text Formatting [TEXT]
# Source: Lines 4210-4248 (reading width + bold/italic)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 3: READING WIDTH & TEXT FORMATTING [TEXT]
   Line width limits and bold/italic styling
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 4210 4248)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 4: Workspace & Layout [LAYOUT]
# Source: Lines 611-640
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 4: WORKSPACE & LAYOUT [LAYOUT]
   Workspace containers, canvas background, split panes
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 611 640)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 5: File Explorer [EXPLORER]
# Source: Lines 661-750
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 5: FILE EXPLORER [EXPLORER]
   File tree, folder icons, nav items
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 661 750)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 6: Sidebars & Navigation [NAV]
# Source: Lines 641-660 (sidebars) + 4608-4660 (vertical nav + tab close)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 6: SIDEBARS & NAVIGATION [NAV]
   Sidebar tab headers, vertical label navigation, tab close button
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 641 660)
$output += ""
$output += Trim-Blanks (Get-Lines 4608 4660)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 7: Status Bar [STATUS]
# Source: Lines 4660-4780 (the toggle-based version from PART 4)
# Removed: Lines 751-810 (duplicate basic version from PART 3)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 7: STATUS BAR [STATUS]
   Status bar base, fade, hidden, minimal, accent, and word count variants
   Each toggle section can be commented out independently
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 4660 4780)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 8: Modals, Popovers & Notices [MODALS]
# Source: Lines 811-870 (modals) + 4780-4810 (notices)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 8: MODALS, POPOVERS & NOTICES [MODALS]
   Modal dialogs, suggestion containers, notification styling
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 811 870)
$output += ""
$output += Trim-Blanks (Get-Lines 4780 4810)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 9: Buttons & Interactive Elements [BUTTONS]
# Source: Lines 4810-4850 (the later, cleaner button section)
# Removed: Lines 871-930 (duplicate earlier version)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 9: BUTTONS & INTERACTIVE ELEMENTS [BUTTONS]
   Button base, hover, warning variants
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 4810 4850)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 10: Scrollbars [SCROLL]
# Source: Lines 931-960
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 10: SCROLLBARS [SCROLL]
   Scrollbar track and thumb styling
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 931 960)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 11: Search [SEARCH]
# Source: Lines 961-1000
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 11: SEARCH [SEARCH]
   Search input, results, and match highlighting
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 961 1000)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 12: Headings [HEADINGS]
# Source: Lines 1870-2035 (Glowing Headers)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 12: HEADINGS - GLOWING HEADERS [HEADINGS]
   H1-H6 with red glow effects, both Live Preview and Reading View
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 1870 2035)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 13: Inline Code [INLINE]
# Source: Lines 1497-1510 (variable-based version)
# Removed: Lines 938-980 (hardcoded color version)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 13: INLINE CODE [INLINE]
   Inline code styling using theme variables
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 1497 1515)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 14: Code Blocks [CODE]
# Source: Lines 1170-1490
# Transform: Remove snippet installation header
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 14: CODE BLOCKS [CODE]
   Syntax highlighting, language badges, line numbers, window chrome
   ═══════════════════════════════════════════════════════════════════════════ */

"@
# Skip the snippet header (roughly lines 1170-1185 area), start from actual CSS
# Find where the actual CSS rules begin after the snippet header comment
$codeBlockLines = Get-Lines 1170 1490
# Filter out the "Place in .obsidian/snippets/" comment block at the start
$inCode = $false
$filteredCode = @()
foreach ($line in $codeBlockLines) {
    if ($line -match 'Place in \.obsidian/snippets/') { continue }
    if ($line -match 'Installation:.*snippets') { continue }
    $filteredCode += $line
}
$output += Trim-Blanks $filteredCode
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 15: Glowing Brackets [BRACKETS]
# Source: Lines 1005-1066 (single copy)
# Removed: Lines 1113-1162 (duplicate copy)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 15: GLOWING BRACKETS [BRACKETS]
   Matching bracket highlighting with glow effects
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 1005 1110)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 16: Tables [TABLES]
# Source: Lines 1763-1848 (correct variables version)
# Removed: Lines 1517-1760 (references non-existent variables)
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 16: TABLES [TABLES]
   Table styling with theme variables
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 1763 1848)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 17: Lists [LISTS]
# Source: Lines 4248-4607 (ordered + unordered)
# Transform: Remove snippet headers
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 17: LISTS - ORDERED & UNORDERED [LISTS]
   Custom list markers with color-coded nesting levels
   Ordered: Numbers → Arrow → Dash → Plus
   Unordered: Arrow → Dash → Plus
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$listLines = Get-Lines 4248 4607
# Filter out snippet installation comment lines
$filteredList = @()
foreach ($line in $listLines) {
    if ($line -match 'Place in \.obsidian/snippets/') { continue }
    if ($line -match 'Installation:.*snippets') { continue }
    if ($line -match 'Custom Snippet:') { continue }
    $filteredList += $line
}
$output += Trim-Blanks $filteredList
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 18: Horizontal Rules, Graph & Card Mode [MISC]
# Source: Lines 1848-1870
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 18: HORIZONTAL RULES, GRAPH VIEW & CARD MODE [MISC]
   HR styling, graph view colors, card mode layout
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 1848 1870)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 19: Metadata Container [META]
# Source: Lines 4850-5201
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 19: METADATA CONTAINER [META]
   YAML frontmatter property display styling
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 4850 5201)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 20: Callout System [CALLOUTS]
# Source: Lines 2858-4200 (Ultimate Callout System v5.0)
# Removed: Lines 2040-2846 (Neon Red Shadow Callout Mod - superseded)
# Also include the callout accessibility section from ~2847-2858
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 20: CALLOUT SYSTEM - ULTIMATE v5.0 [CALLOUTS]
   150+ callout types across 14 sections with Imperial Red/Black/Grey palette
   ═══════════════════════════════════════════════════════════════════════════ */

"@
$output += Trim-Blanks (Get-Lines 2858 4200)
$output += ""
$output += ""


# ═══════════════════════════════════════════════════════════════════════════
# PART 21: Accessibility [A11Y]
# Source: Extracted from callout system accessibility section
# ═══════════════════════════════════════════════════════════════════════════
$output += @"

/* ═══════════════════════════════════════════════════════════════════════════
   PART 21: ACCESSIBILITY & REDUCED MOTION [A11Y]
   Respects user motion preferences and print media
   ═══════════════════════════════════════════════════════════════════════════ */

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}

@media print {
  .callout {
    box-shadow: none !important;
    border: 1px solid #666 !important;
    border-left: 4px solid #333 !important;
    background: #fff !important;
  }
  .callout-title {
    background: #f0f0f0 !important;
    color: #333 !important;
  }
  .callout-content {
    color: #000 !important;
  }
}

"@


# ═══════════════════════════════════════════════════════════════════════════
# TERMINAL MARKER
# ═══════════════════════════════════════════════════════════════════════════
$output += "/* === END OF FILE: theme.css === */"


# Write the output
$output | Set-Content -Path $outputPath -Encoding UTF8

# Report
$originalCount = $lines.Count
$newCount = $output.Count
Write-Host "=== V4D3R Crimson Theme Reorganization Complete ==="
Write-Host "Original: $originalCount lines"
Write-Host "New:      $newCount lines"
Write-Host "Removed:  $($originalCount - $newCount) lines"
Write-Host "Output:   $outputPath"
