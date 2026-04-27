# Changelog — V4D3R Reactor

All notable changes follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2026-04-27

### Added

- Full 24-part theme covering: Variables, Typography, Obsidian Variable Overrides, Text, Layout, File Explorer, Sidebars, Status Bar, Modals, Buttons, Scrollbars, Search, Headings, Inline Code, Code Blocks, Brackets, Tables, Lists, HR/Graph/Canvas, Metadata, Callouts, Accessibility, Light Theme, Settings
- Neon red (#FF1E1E) primary accent with static 4-layer glow system (`--vr-glow-sm/md/lg/xl/depth`)
- Per-heading text-shadow cascade (H1 = 4-layer, H2 = 3-layer, H3 = 2-layer, H4 = 1-layer, H5–H6 = none)
- Neon left-bar glow on H1 and H2 headings (3px `--vr-red-neon` / `--vr-red-core` with outward box-shadow)
- `[[` `]]` bracket injection via `::before`/`::after` on `.internal-link` (Reading View) and `.cm-formatting-link` (Live Preview)
- 3px neon red left rule on code blocks with outward glow in both Live Preview and Reading View
- Static 3-layer box-shadow on callout containers with 4-layer on hover; 14 callout type overrides
- Full Obsidian native variable mapping (`--color-accent`, `--background-primary`, `--text-*`, etc.) for plugin compatibility
- Complete light theme with 50%-intensity glows
- `@media (prefers-reduced-motion: reduce)` — collapses all transition durations
- `@media (forced-colors: active)` — high contrast mode support
- Mobile adjustments: smaller base font, reduced heading sizes, scrollable tables, no hover glows on touch
- Variable prefix: `--vr-*` (no collision with `--vsg-*` Sanguine or `--vc-*` Cinder)
- All 617 `--vr-` references resolve to definitions within the same file
- Braces: 213 open, 213 close (balanced)
- Terminal marker: `/* === END OF FILE: theme.css === */`
