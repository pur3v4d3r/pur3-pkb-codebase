# Changelog

All notable changes to V4D3R Sanguine will be documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

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

[1.0.0]: #100--2026-04-26
