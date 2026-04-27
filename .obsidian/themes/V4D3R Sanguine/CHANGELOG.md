# Changelog

All notable changes to V4D3R Sanguine will be documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [1.0.2] — 2026-04-27

### Fixed
- **Indent runaway (real fix)**: 1.0.1 targeted `.nav-folder-children`, but Obsidian 1.5+ applies the inline indentation via `style="margin-inline-start:-Xpx !important; padding-inline-start:Ypx !important"` on `.tree-item-self` (negative-margin + positive-padding pattern for full-width hover). 1.0.2 overrides `.tree-item-self` directly with `!important` and zeroes the negative margin so deep paths stop drifting right.
- Set `--nav-indentation-width` on `body` (was scoped only to `.workspace-leaf-content[data-type="file-explorer"]`, which Obsidian's calc bypasses for inline styles).

### Removed
- **Vertical indent-guide hairline** (`.nav-folder-children::before`). Stacked across nested wrappers it read as extra indent and added visual noise. Restore the block from 1.0.1 if you want them back.

## [1.0.1] — 2026-04-27

### Fixed
- **File explorer indentation runaway**: deep folder trees (4+ levels) pushed nested items far off to the right, leaving most of the pane as empty whitespace. Reduced per-level indent from Obsidian's default ~17 px to 12 px via `--nav-indentation-width`, `--nav-item-children-padding-start`, and an explicit `.nav-folder-children { padding-inline-start: 12px }` override (needed because Obsidian sets this inline on every wrapper, so it compounds recursively).
- **Long file/folder names overflowing the pane**: added `white-space: nowrap; overflow: hidden; text-overflow: ellipsis` to `.nav-folder-title`, `.nav-file-title`, and their inner `-content` spans so long names truncate instead of forcing the explorer wider.
- Added `.tree-item-children` parity rule for Obsidian 1.5+ which uses both `.nav-folder-*` and `.tree-item-*` selectors in the file explorer.

## [1.0.0] — 2026-04-26

### Added
- Initial release of V4D3R Sanguine.
- Full coverage across 21 component sections, mirroring V4D3R Crimson's structural parity.
- Three-typeface system: IBM Plex Serif (body), Plex Sans (UI), Plex Mono (code) with system fallbacks.
- Oxblood / Garnet / Rust / Cinnabar red spectrum (desaturated, scholarly).
- Warm carbon black spectrum: Ink → Carbon → Soot → Ash.
- Warm parchment grey spectrum: Stone → Iron → Bone → Parchment → Vellum → Chalk.
- **Manuscript Ribbon** callout system with hanging icons, hairline rules, serif titles, per-type title color shifts.
- Editorial heading hierarchy: serif true-small-caps with hairline underlines and **drop cap on H1**.
- Square code blocks with 3px oxblood left rule and filename badge.
- Typographic list markers: `§ ¶ ·` (oxblood) instead of arrows.
- Subtle oxblood `[[wiki-link]]` brackets via pseudo-elements (no glow).
- Editorial table styling: small-caps oxblood headers, zebra rows, hairline grid.
- Manuscript-margin tags: italic serif pills.
- Translucency-aware modals (uses `backdrop-filter` only when `body.is-translucent`).
- Mobile responsive adjustments via `body.is-mobile`.
- Accessibility: WCAG AA verified; `prefers-reduced-motion` and `prefers-contrast: more` media queries.
- All custom properties prefixed `--vsg-*` and classes prefixed `.vsg-*` to coexist with V4D3R Crimson.

[1.0.2]: #102--2026-04-27
[1.0.1]: #101--2026-04-27
[1.0.0]: #100--2026-04-26
