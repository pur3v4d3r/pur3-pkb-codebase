# V4D3R Obsidian — Architecture Plan (frozen as built)

## Identity
- **Name:** V4D3R Obsidian
- **Family:** V4D3R Red/Black/Grey theme trio (siblings: Crimson, Sanguine)
- **Voice:** Modern application surface — black canvas, floating graphite cards, vivid arterial-red signal accent.
- **Mode:** Dark only.
- **Min Obsidian:** 1.5.0+

## Differentiation matrix vs siblings

| Axis | Sanguine (sibling) | **V4D3R Obsidian** |
|---|---|---|
| Geometry | Sharp 0px corners | Rounded 4/6/10/14/20px scale |
| Surface model | Flat manuscript page | Elevated cards with 3-tier shadow system |
| Typography | All JetBrains Mono | Inter (UI/body) + JetBrains Mono (code only) |
| Accent | Oxblood `#7A0F1A` (scholarly) | Arterial red `#E5343A` (signal) |
| Body link color | Same as accent (intense) | Carmine `#C8474C` (calmer) |
| Tabs | Square sharp | Pill with rounded top + red bottom-bar |
| Callouts | Manuscript ribbon left edge | Full tinted card + 3px bar + soft fill overlay |
| File explorer | Quiet hairline rows | Card-row hover + active red flag + indent guides |
| Code blocks | Sharp panel | Rounded card with red gradient top accent |
| Headings | Drop cap on H1 | Red bottom-border accent flourish on H1, ▸ marker on H3 |

## Output structure (Structure C — Full Theme)

```
<vault>/.obsidian/themes/V4D3R Obsidian/
├── manifest.json
├── theme.css                ← single concatenated file (2251 lines)
├── README.md
├── CHANGELOG.md
├── LICENSE                  ← MIT
└── _meta/
    ├── architecture-plan.md ← this file
    ├── build-log.md
    └── validation-report.md
```

## theme.css section map (as built)

| Part | Lines (approx) | Section | Coverage |
|---|---|---|---|
| 1 | 1–250  | [VARS]      | Color palette, geometry tokens, native overrides, typography vars |
| 2 | 251–290 | [TYPE]      | Base typography, bold/italic/highlight/strikethrough/selection |
| 3 | 291–360 | [TEXT]      | Reading width 760px, paragraph rhythm, inline title, blockquotes |
| 4 | 361–470 | [LAYOUT]    | Workspace canvas, card surfaces, ribbon, view headers |
| 5 | 471–560 | [TABS]      | Pill tabs with red bottom-bar on active |
| 6 | 561–700 | [EXPLORER]  | Folder/file titles, card-row hover, indent guides, file-type pills |
| 7 | 701–880 | [NAV]       | Sidebar tree-items, backlinks, search match highlights |
| 8 | 881–940 | [CHROME]    | Status bar, title bar, frameless titlebar buttons |
| 9 | 941–1130 | [MODALS]   | Modals, settings sidebar nav, suggestions, palette, menus, notices, tooltips |
| 10 | 1131–1300 | [BUTTONS] | Default button, mod-cta, mod-warning, inputs, toggles, slider, focus ring |
| 11 | 1301–1400 | [SCROLL]  | Scrollbars (10px), search-result mini-cards |
| 12 | 1401–1510 | [HEADINGS] | Inter stepped scale, H1–H6 in BOTH Live Preview + Reading View |
| 13 | 1511–1620 | [CODE]    | Inline pill, full-card code blocks, copy button, syntax tokens |
| 14 | 1621–1700 | [TABLES]  | Card-table with rounded border, zebra rows, uppercase header chips |
| 15 | 1701–1830 | [MISC]    | Lists, task checkboxes, HR gradient, tags, internal/external links |
| 16 | 1831–1920 | [META]    | Properties / metadata frontmatter card |
| 17 | 1921–2080 | [CALLOUTS] | Card callouts with 3px tinted bar + tinted fill overlay, 8 type groups |
| 18 | 2081–2160 | [GRAPH]   | Graph view colors, canvas node cards |
| 19 | 2161–2200 | [MOBILE]  | `is-mobile` reduced shadows + gutter, `is-translucent` backdrop blur |
| 20 | 2201–2251 | [A11Y]    | `prefers-reduced-motion`, `prefers-contrast: more`, print stylesheet |

## Conventions

- All custom properties prefixed `--vob-*`.
- All custom classes (none introduced — theme styles native Obsidian classes only) would be prefixed `vob-`.
- File ends with `/* === END OF FILE: theme.css === */`.
- Every part closes with `/* --- SECTION END: PART <n> [<NAME>] --- */`.
- Hard-coded colors permitted only inside PART 1 (variable declarations) and the print stylesheet (intentional `#999`/`white`/`black`).
- `!important` permitted only with inline-comment justification.

## Compatibility

- Tested-against (mentally): Dataview, Tasks, Calendar, Excalidraw, Kanban, Properties (core), Canvas (core), Graph (core).
- Mobile: yes — reduced shadow pass, no hover-lift on touch.
- Translucency: yes — backdrop-blur cards with solid fallback.
- Conflicts known: any user snippet that re-skews tab pseudo-elements will fight PART 5.
