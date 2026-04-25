# V4D3R Crimson Theme — Architecture Plan

**Date**: 2026-07-16  
**Mode**: AUDIT → REORGANIZE  

---

## Target Structure (Single `theme.css`)

```
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
```

## Decisions Made

| Decision | Choice | Rationale |
|---|---|---|
| Foundation Variables | Keep Block 1 (detailed) | Matches README, well-documented, 300 weight |
| Callout System | Keep Ultimate v5.0 only | More comprehensive, better organized, has layouts/modifiers |
| Tables | Keep correct-variable version | Other version references non-existent variables |
| Inline Code | Keep variable-based version | Proper use of theme variables |
| Glowing Brackets | Keep single copy | Exact duplicate |
| Status Bar | Merge both versions | Toggle-based structure from later version |
| Buttons | Merge both versions | Combine unique rules |
| `!important` usage | Keep as-is | Removing requires visual testing |
| Variable naming (`purple`) | Keep as-is | Renaming is design change, not cleanup |
| Hardcoded colors | Document, keep | Would need user input to pick variable alternatives |

## Source Mapping (Current Line → New Part)

| New Part | Source Lines | Transforms |
|---|---|---|
| 1 | 1–388 | Remove Block 2 duplicate |
| 2 | 561–610, 1497–1510 | Merge typography + inline code |
| 3 | 4210–4248 | Reading width + bold/italic |
| 4 | 611–640 | Clean |
| 5 | 661–750 | Clean |
| 6 | 641–660, 4608–4660 | Merge sidebar + vertical nav + tab close |
| 7 | 751–810 + 4660–4780 | Merge, keep toggle structure |
| 8 | 811–870, 4780–4810 | Merge modals + notices |
| 9 | 871–930 + 4810–4850 | Merge both button sections |
| 10 | 931–960 | Clean |
| 11 | 961–1000 | Clean |
| 12 | 1870–2035 | Clean |
| 13 | 1497–1510 | Variable-based version |
| 14 | 1170–1490 | Remove snippet header |
| 15 | 1005–1066 | Single copy |
| 16 | 1763–1848 | Correct-variable version |
| 17 | 4248–4607 | Remove snippet headers, integrate |
| 18 | 1848–1870 | Clean |
| 19 | 4850–5201 | Clean |
| 20 | 2858–4200 | Complete Ultimate Callout System |
| 21 | Callout a11y section | Extract from callout system |

## REMOVED (Dead Code)
- Lines 389–560: Duplicate Foundation Variables Block 2
- Lines 938–980: Hardcoded inline code (duplicate)
- Lines 1067–1112: Gap/extra content between bracket duplicates
- Lines 1113–1162: Duplicate glowing brackets
- Lines 1517–1760: Tables with wrong variables
- Lines 2040–2846: Entire Neon Red Shadow Callout System
- ~200 lines of excessive blank lines
