# V4D3R Reactor — Architecture Plan

**Theme family member:** Third in the V4D3R series (after Sanguine and Cinder)
**Variable prefix:** `--vr-*`
**Archetype:** Cyberpunk / Neon — static glows, void black, neon red (#FF1E1E)

## Color Palette Summary

| Role | Variable | Hex |
|------|----------|-----|
| Primary neon | `--vr-red-neon` | #FF1E1E |
| Secondary | `--vr-red-hot` | #FF4040 |
| Deep rule | `--vr-red-core` | #CC0A0A |
| Inactive | `--vr-red-ember` | #8C0000 |
| Primary bg | `--vr-abyss` | #080A0D |
| Secondary bg | `--vr-graphite` | #0F1115 |
| Card layer | `--vr-slate` | #171B21 |
| Body text | `--vr-grey-steel` | #94A8BC |

## Glow System (all static)

- 3-layer: sm + md + lg + depth
- 4-layer (intense): sm + md + lg + xl + depth
- Text glow H1: 4-layer shadow, H2: 3-layer, H3: 2-layer, H4: 1-layer

## File Structure

```
V4D3R Reactor/
├── manifest.json
├── theme.css          (~2000 lines, 24 parts)
├── README.md
├── CHANGELOG.md
└── _meta/
    ├── architecture-plan.md  (this file)
    └── validation-report.md
```

## theme.css Parts

1. Foundation Variables [VARS]
2. Base Typography [TYPE]
3. Obsidian Variable Overrides [OVRD]
4. Reading Width & Text Formatting [TEXT]
5. Workspace & Layout [LAYOUT]
6. File Explorer [EXPLORER]
7. Sidebars & Navigation [NAV]
8. Status Bar [STATUS]
9. Modals, Popovers, Notices [MODALS]
10. Buttons & Interactive [BUTTONS]
11. Scrollbars [SCROLL]
12. Search [SEARCH]
13. Headings — Neon Glow [HEADINGS]
14. Inline Code [INLINE]
15. Code Blocks — Neon Left Rule [CODE]
16. Brackets — Neon Glow [BRACKETS]
17. Tables [TABLES]
18. Lists [LISTS]
19. HR, Graph, Canvas [MISC]
20. Metadata Container [META]
21. Callouts — Neon Border [CALLOUTS]
22. Accessibility & Reduced Motion [A11Y]
23. Light Theme [LIGHT]
24. Settings Page [SETTINGS]
