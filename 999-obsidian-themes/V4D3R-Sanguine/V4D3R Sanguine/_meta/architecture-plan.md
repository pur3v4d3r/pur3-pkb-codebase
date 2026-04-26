# V4D3R Sanguine — Architecture Plan

**Mode:** CREATE
**Output structure:** C (Full Theme)
**Date:** 2026-04-26
**Status:** Approved by user (option 1, as-is)

## Design Thesis

Scholarly editorial counterpart to V4D3R Crimson. Same Red/Black/Grey palette, fundamentally different emotional register: noir manuscript instead of cyberpunk terminal.

## Token Prefix

- Custom properties: `--vsg-*`
- Class names: `.vsg-*`
- Coexists cleanly with `--v4d3r-*` from Crimson.

## Typography Stack

- Body: `"IBM Plex Serif", Georgia, "Iowan Old Style", serif`
- UI: `"IBM Plex Sans", system-ui, -apple-system, sans-serif`
- Code: `"IBM Plex Mono", "JetBrains Mono", Consolas, monospace`

## File Tree

```
V4D3R Sanguine/
├── manifest.json
├── theme.css
├── README.md
├── CHANGELOG.md
└── _meta/
    ├── architecture-plan.md   ← this file
    ├── design-tokens.md
    └── validation-report.md
```

## Section Map (21 parts, parity with Crimson)

1. Foundation Variables
2. Base Typography
3. Reading Width & Text Formatting
4. Workspace & Layout
5. File Explorer
6. Sidebars & Navigation
7. Status Bar
8. Modals, Popovers, Notices
9. Buttons & Interactive
10. Scrollbars
11. Search
12. Headings (editorial small-caps + drop cap)
13. Inline Code
14. Code Blocks (square + left rule + filename badge)
15. Brackets (subtle, no glow)
16. Tables (editorial)
17. Lists (typographic markers § ¶ ·)
18. Horizontal Rules / Graph / Card Mode
19. Metadata Container
20. Callout System (Manuscript Ribbon)
21. Accessibility & Reduced Motion

## Compatibility

- Min Obsidian: 1.5.0
- Live Preview AND Reading View parity for headings, callouts, lists, code, brackets
- Mobile: yes (`body.is-mobile` adjustments)
- Translucency: enhanced when `body.is-translucent`, solid fallback otherwise
- No remote assets — all fonts local with system fallbacks
- No conflicts with V4D3R Crimson (different prefixes; only one theme active at a time anyway)
