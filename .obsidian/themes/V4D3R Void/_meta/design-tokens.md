# V4D3R Void — Design Token Inventory

Complete annotated reference for all `--vvd-*` custom properties.
Override any of these in a CSS snippet to customize the theme.

---

## Red Spectrum

| Token | Value | Role |
|---|---|---|
| `--vvd-red-void` | `#1A0006` | Near-invisible red tint — extreme depth, rarely visible |
| `--vvd-red-blood` | `#500012` | Deep blood — background tints, shadow accents |
| `--vvd-red-dark` | `#750018` | Dark rule red — inactive borders, list markers |
| `--vvd-red-base` | `#9E001F` | **PRIMARY ACCENT** — headings, links, active states, callout rules |
| `--vvd-red-mid` | `#C2002A` | Hover accent — link hover, callout titles, interactive hover |
| `--vvd-red-bright` | `#E80034` | Critical / warning — error states, danger callouts |
| `--vvd-red-glow` | `#FF1A45` | Maximum — focus rings only (accessibility) |
| `--vvd-red-alpha-08` | `rgba(158,0,31,0.08)` | Subtle tint — active file bg, hover states |
| `--vvd-red-alpha-15` | `rgba(158,0,31,0.15)` | Selection background, highlight |
| `--vvd-red-alpha-25` | `rgba(158,0,31,0.25)` | Stronger selection, mark/highlight |
| `--vvd-red-alpha-40` | `rgba(158,0,31,0.40)` | Heavy overlay |
| `--vvd-red-alpha-60` | `rgba(158,0,31,0.60)` | Near-opaque red layer |

---

## Black Spectrum

| Token | Value | Role |
|---|---|---|
| `--vvd-black-pure` | `#000000` | True void — workspace root background |
| `--vvd-black-abyss` | `#030303` | **PRIMARY BACKGROUND** — main content area |
| `--vvd-black-deep` | `#080808` | Elevated surface — tab headers, view headers |
| `--vvd-black-shade` | `#0F0F0F` | More elevated — modals (solid), code blocks, metadata |
| `--vvd-black-lift` | `#171717` | Highest elevation — modal panels, popovers |
| `--vvd-black-alpha-40` | `rgba(0,0,0,0.40)` | Light shadow |
| `--vvd-black-alpha-60` | `rgba(0,0,0,0.60)` | Medium shadow |
| `--vvd-black-alpha-80` | `rgba(0,0,0,0.80)` | Modal overlay, heavy shadow |
| `--vvd-black-alpha-92` | `rgba(0,0,0,0.92)` | Near-opaque overlay |

---

## Grey Spectrum (Cool Silver — subtle violet tint)

| Token | Value | Role |
|---|---|---|
| `--vvd-grey-shadow` | `#1E1E22` | **Borders and separators** — darkest visible grey |
| `--vvd-grey-dark` | `#2E2E35` | Inactive controls, toggle off state |
| `--vvd-grey-mid` | `#4A4A55` | Disabled states, faint structure |
| `--vvd-grey-dusk` | `#6A6A78` | Faint text — metadata values, comments |
| `--vvd-grey-silver` | `#9898AA` | **Muted text** — nav items, status bar |
| `--vvd-grey-light` | `#C0C0D0` | **NORMAL BODY TEXT** — WCAG AA on `#030303` (7.1:1) |
| `--vvd-grey-pale` | `#D8D8E8` | Emphasis text — H2, bold, selected |
| `--vvd-grey-frost` | `#EEEEF6` | Maximum emphasis — H1, text-on-accent, inline title |
| `--vvd-grey-alpha-05` | `rgba(192,192,208,0.05)` | Ghost hover background |
| `--vvd-grey-alpha-10` | `rgba(192,192,208,0.10)` | Subtle surface tint |
| `--vvd-grey-alpha-20` | `rgba(192,192,208,0.20)` | Moderate surface tint |

---

## Glass Spectrum (Translucency System)

Active only when `body.is-translucent` is present (Obsidian's translucent window mode).

| Token | Value | Role |
|---|---|---|
| `--vvd-glass-sidebar` | `rgba(8,8,8,0.55)` | Left/right sidebar panels |
| `--vvd-glass-leaf` | `rgba(3,3,3,0.85)` | Content leaf area |
| `--vvd-glass-modal` | `rgba(15,15,15,0.92)` | Modals and command palette |
| `--vvd-glass-callout` | `rgba(9,0,2,0.45)` | Callout panels — dark translucent red-void tint |
| `--vvd-glass-code` | `rgba(8,8,8,0.80)` | Code block panels |
| `--vvd-glass-blur` | `12px` | `backdrop-filter: blur()` radius — reduce for performance |

---

## Typography Tokens

| Token | Value | Role |
|---|---|---|
| `--vvd-font-mono` | JetBrains Mono stack | All text — interface, editor, reading |
| `--vvd-weight-thin` | `300` | H1, H2 headings |
| `--vvd-weight-normal` | `400` | Body, H3–H6 |
| `--vvd-weight-medium` | `500` | Nav folders, CTA buttons |
| `--vvd-weight-semibold` | `600` | Available for override |
| `--vvd-weight-bold` | `700` | Bold text (`strong`) |
| `--vvd-base-size` | `16px` | Base font size |
| `--vvd-ui-small` | `11px` | Status bar, labels |
| `--vvd-ui-medium` | `12px` | Nav items, interface |
| `--vvd-ui-large` | `14px` | View header title |
| `--vvd-lh-tight` | `1.30` | Headings, code blocks |
| `--vvd-lh-normal` | `1.60` | Body prose |
| `--vvd-lh-relaxed` | `1.80` | Available for override |

---

## Spacing, Radius, Border, Shadow, Transition Tokens

| Token | Value | Role |
|---|---|---|
| `--vvd-space-2xs` | `2px` | Micro gap |
| `--vvd-space-xs` | `4px` | Compact padding |
| `--vvd-space-sm` | `8px` | Standard element padding |
| `--vvd-space-md` | `14px` | Section padding |
| `--vvd-space-lg` | `22px` | Between sections |
| `--vvd-space-xl` | `32px` | Large gaps |
| `--vvd-radius-none` | `0` | Sharp corners (default everywhere) |
| `--vvd-radius-sm` | `1px` | Modal corners (subtle) |
| `--vvd-radius-md` | `2px` | Toggle, rare use |
| `--vvd-border-hair` | `1px` | Standard borders |
| `--vvd-border-rule` | `2px` | Active tab border |
| `--vvd-border-thick` | `3px` | Heading ticks, callout rules |
| `--vvd-shadow-sm` | black drop 1px | Subtle elevation |
| `--vvd-shadow-md` | black drop 3px | Moderate elevation |
| `--vvd-shadow-lg` | black drop 8px | Modals, strong elevation |
| `--vvd-t-fast` | `100ms ease` | Tab hover, icon reveal |
| `--vvd-t-normal` | `200ms ease` | Standard interactions |
| `--vvd-t-slow` | `360ms ease` | Available for override |

---

## Component Tokens

| Token | Value | Role |
|---|---|---|
| `--vvd-reading-max-width` | `108ch` | Reading view / LP content width |
| `--vvd-heading-tick-width` | `3px` | Heading left-border rule width |
| `--vvd-heading-tick-color` | `#9E001F` | Heading left-border rule color |
| `--vvd-code-rule-width` | `3px` | Code block left border width |
| `--vvd-code-rule-color` | `#9E001F` | Code block left border color |
| `--vvd-callout-rule-width` | `3px` | Callout left border width |
| `--vvd-callout-rule-color` | `#9E001F` | Callout left border color |
| `--vvd-table-header-bg` | `#0F0F0F` | Table header row background |
| `--vvd-table-header-fg` | `#9E001F` | Table header text color |
| `--vvd-table-zebra-bg` | `#080808` | Alternate table row background |
| `--vvd-table-grid` | `#1E1E22` | Table border / grid color |
| `--vvd-tag-bg` | `#0F0F0F` | Tag pill background |
| `--vvd-tag-fg` | `#C2002A` | Tag pill text |
| `--vvd-tag-border` | `#750018` | Tag pill border |
