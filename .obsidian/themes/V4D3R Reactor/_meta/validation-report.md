# V4D3R Reactor — Phase 5 Validation Report

**Date:** 2026-04-27
**Version:** 1.0.0
**Validator:** Static analysis (CSS parse + Python script)

---

## Results Summary

**19 PASS · 0 FAIL · 0 WARN**

---

## Per-Check Results

| # | Check | Status | Detail |
|---|-------|--------|--------|
| 1 | Terminal marker present (`=== END OF FILE: theme.css ===`) | PASS | Line 1917 |
| 2 | All 24 section markers present | PASS | 24 found |
| 3 | Braces balanced | PASS | 213 open / 213 close |
| 4 | No undefined `--vr-` `var()` references | PASS | All 617 resolve internally |
| 5 | All `!important` have inline justification comment | PASS | 6 occurrences, all commented |
| 6 | `manifest.json` valid JSON | PASS | |
| 7 | `manifest.json` name field | PASS | "V4D3R Reactor" |
| 8 | `manifest.json` version (semver) | PASS | "1.0.0" |
| 9 | `manifest.json` minAppVersion | PASS | "1.4.0" |
| 10 | README references `--vr-red-neon` | PASS | |
| 11 | README references `--vr-font-mono` | PASS | |
| 12 | README references `--vr-text-base` | PASS | |
| 13 | README references `--vr-abyss` | PASS | |
| 14 | CHANGELOG has [1.0.0] entry | PASS | |
| 15 | No `*` selector on `.cm-line` or `.cm-content` | PASS | None found |
| 16 | Live Preview headers styled (`.HyperMD-header-*`) | PASS | H1–H6 covered |
| 17 | Reading View headers styled (`.markdown-preview-view h*`) | PASS | H1–H6 covered |
| 18 | `prefers-reduced-motion` block present | PASS | Part 22 |
| 19 | Mobile (`is-mobile`) adjustments present | PASS | Part 22 |

---

## !important Inventory

| Line | Property | Justification |
|------|----------|---------------|
| 259 | `font-family` on `code, pre, kbd, samp` | Browser UA sets monospace; override for JetBrains Mono |
| ~261 | `font-family` on `.cm-editor` | CodeMirror sets its own font-family inline |
| ~428 | `background` on `.cm-line ::selection` | CodeMirror 6 applies its own `::selection`; override required |
| ~1252 | `color` on `.cm-formatting-link` | CM6 formats link punctuation as `--text-normal`; override for neon |
| 1705–1707 | `transition-duration`, `animation-duration`, `animation-iteration-count` | Inside `prefers-reduced-motion: reduce` block; `!important` required to override all specificity levels |

---

## Notes

- No external assets loaded (`@import`, `url()` with `http`)
- No `filter:` on hot-path editor elements (glows use `box-shadow` / `text-shadow`)
- All animations in this theme are transition-based only (no `@keyframes`) — `prefers-reduced-motion` collapses transition durations
- Variable prefix `--vr-*` has no known collision with `--vsg-*` (Sanguine) or `--vc-*` (Cinder)
- Light theme scoped to `.theme-light` selector; all glow values reduced to ~50% opacity
- Mobile adjustments scoped to `body.is-mobile` selector; hover glows disabled for touch

---

## Static Validation Limitations

This report covers static analysis only. The following require manual verification in Obsidian:
- Actual rendering of glow effects in dark mode
- Light mode glow visibility
- Plugin compatibility (Dataview, Tasks, Kanban, Excalidraw)
- Mobile layout on iOS/Android
- Translucency mode (`body.is-translucent`) — theme does not use `backdrop-filter`, so no concern
