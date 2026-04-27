# Changelog

All notable changes to V4D3R Void are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2026-04-26

### Added
- Initial release of V4D3R Void theme
- 22-part `theme.css` architecture (1688 lines)
- Full `--vvd-*` custom property system (PART 1)
  - Red spectrum: 7 named tokens + 5 alpha variants
  - Black spectrum: 5 named tokens + 4 alpha variants
  - Grey spectrum: 8 named tokens + 3 alpha variants
  - Glass spectrum: 6 translucency tokens (unique to Void)
- Obsidian core variable overrides (PART 2)
- JetBrains Mono typography stack (PART 3)
- Reading width constraint at 108ch (PART 4)
- Workspace and tab layout (PART 5)
- Translucency system with `backdrop-filter` gating on `body.is-translucent` (PART 6)
  - Glass surfaces: sidebar, leaf content, status bar, ribbon, tab header, titlebar, modals, callouts
  - Solid fallbacks for all glass rules (`body:not(.is-translucent)`)
  - Mobile disables all `backdrop-filter` for performance
- File explorer ghost-chrome pattern (PART 7)
- Sidebar navigation styling (PART 8)
- Minimal status bar (PART 9)
- Glass modals, command palette, notices, hover popovers (PART 10)
- Buttons, checkboxes, toggles, text inputs (PART 11)
- Minimal webkit scrollbars (PART 12)
- Search results styling (PART 13)
- Void headings — thin weight, 3px blood-red left tick (PART 14)
  - Full parity: `.HyperMD-header-*` (Live Preview) + `.markdown-preview-view h*` (Reading View)
- Inline code styling (PART 15)
- Code blocks with glass panels and left rule (PART 16)
  - Full parity: `.HyperMD-codeblock*` (LP) + `.markdown-preview-view pre` (RV)
- Bracket matching — subtle, no glow (PART 17)
- Minimal glass tables with zebra stripes (PART 18)
- Em-dash / mid-dot list markers (PART 19)
- Graph view, Canvas, HR styling (PART 20)
- Metadata container (frontmatter panel) with glass variant (PART 21)
- Glass Void callouts with semantic type overrides (PART 22)
  - 8 semantic types: note/info, warning/caution, danger/error/bug, success/tip, quote/cite, abstract/summary/tldr
  - Glass panel on `.is-translucent`, solid fallback on `body:not(.is-translucent)`
  - Mobile: no backdrop-filter
- Accessibility: reduced-motion media query, focus-visible ring, touch target minimums (A11Y)
- Light-mode passthrough stub (documented as unsupported)
- `manifest.json` with valid semver and `minAppVersion: "1.5.0"`
- `README.md` with full documentation
- `_meta/design-tokens.md` — complete variable inventory
- `_meta/build-log.md` — write + verification log
- `LICENSE` (MIT)
