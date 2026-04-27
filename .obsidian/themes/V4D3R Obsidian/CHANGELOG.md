# Changelog

All notable changes to **V4D3R Obsidian** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-04-27

### Added
- Initial release of **V4D3R Obsidian** — the "card-deck" theme.
- Full Red / Black / Grey palette using arterial red `#E5343A` as the signal accent and carmine `#C8474C` for body links.
- 3-tier elevation system (rest / hover / active) with shadow + radius scale.
- Pill-tab system with red active-bar.
- Card-style file explorer with red active-flag and indent guides.
- Card-style callouts with type-specific tint overlay (note/info, success, warn, error, example, definition).
- Card-style tables with zebra rows and uppercase header chips.
- Inter (UI/body) + JetBrains Mono (code only) typographic split.
- Full coverage of: workspace layout, tabs, file explorer, sidebars, status/title bars, modals, popovers, suggestions, notices, tooltips, buttons, inputs, scrollbars, search results, headings (H1–H6 in Live Preview + Reading View), inline + block code with copy button, syntax tokens, tables, lists, task lists, HR, tags, internal/external links, properties/metadata, callouts (15+ types), graph view, canvas, mobile, translucency, accessibility (reduced motion + print).
- `body.is-translucent` backdrop-blur on cards with solid fallback.
- `body.is-mobile` reduced-shadow + tightened-gutter pass.
- `prefers-reduced-motion` and `prefers-contrast: more` media-query support.
- Print stylesheet that strips chrome and renders content monochrome.

### Notes
- Dark-mode only by design (matches V4D3R Sanguine convention).
- Differentiation from V4D3R Sanguine: rounded geometry vs sharp, elevated cards vs flat, Inter+Mono vs all-mono, vivid arterial accent vs scholarly oxblood, card-callouts vs manuscript-ribbon.
