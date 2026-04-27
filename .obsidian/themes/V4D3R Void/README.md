# V4D3R Void

**The void through glass.** Fourth member of the V4D3R theme family for Obsidian.

Pure black foundations. Translucent sidebar and chrome panels revealing depth via `backdrop-filter`. Blood-red accent — the deepest, most desaturated red in the V4D3R family. Cool silver-grey typography with a subtle violet tint. Near-invisible chrome that reveals itself only on interaction.

---

## What It Does

V4D3R Void is built around four design commitments:

1. **True void black** — `#030303` primary background, `#000000` workspace root. No warm greys, no softened blacks. The darkest baseline in the V4D3R family.
2. **Translucency-first** — When Obsidian's window translucency is enabled, the sidebar, ribbon, tab bar, status bar, and modals become glass panels with `backdrop-filter: blur(12px)`. Every glass rule has a solid fallback for non-translucent mode.
3. **Blood-red accent** — `#9E001F` as the primary accent. Deeper and more desaturated than Crimson (`#DC143A`) and Sanguine (`#7A0F1A`). Used sparingly — headings, active states, link colors, callout rules.
4. **Ghost chrome** — file explorer items, tab close buttons, and action buttons are invisible until hovered. The workspace recedes; your content dominates.

### Design Contrast from V4D3R Siblings

| | Crimson | Sanguine | Cinder | **Void** |
|---|---|---|---|---|
| **Archetype** | Cyberpunk glow | Scholarly editorial | Card design system | **Glass / translucent** |
| **Red** | Bright `#DC143A` | Oxblood `#7A0F1A` | Vivid `#8F1622` | **Blood `#9E001F`** |
| **Greys** | Warm charcoal | Warm ochre-parchment | Cool blue-grey | **Cool violet-silver** |
| **Headings** | Glowing text-shadow | Drop-cap + double-rule | Left accent bars | **Thin weight + left tick** |
| **Callouts** | Terminal style | Manuscript ribbon | Card elevation | **Glass panels** |
| **Chrome** | Always visible | Always visible | Card surfaces | **Ghost — reveals on hover** |

---

## Screenshots

> Add screenshots here: `screenshots/dark.png`, `screenshots/translucent.png`

---

## Installation

1. Open Obsidian → **Settings** → **Appearance**
2. Under **Themes**, click **Manage**
3. Or install manually:
   - Copy the `V4D3R Void/` folder to `.obsidian/themes/` in your vault
   - Back in **Appearance**, select **V4D3R Void** from the theme dropdown

**Recommended:** Enable **Translucent window** in Settings → Appearance to activate the glass surfaces.

---

## Configuration

All variables are prefixed `--vvd-*` and declared in PART 1 of `theme.css`. Override any of them in a CSS snippet without editing this file.

### Most Commonly Overridden Variables

| Variable | Default | Controls |
|---|---|---|
| `--vvd-glass-blur` | `12px` | Blur radius on all glass surfaces |
| `--vvd-glass-sidebar` | `rgba(8,8,8,0.55)` | Sidebar panel background opacity |
| `--vvd-red-base` | `#9E001F` | Primary accent — links, headings, active states |
| `--vvd-red-mid` | `#C2002A` | Hover accent — link hover, callout titles |
| `--vvd-grey-light` | `#C0C0D0` | Normal body text color |
| `--vvd-black-abyss` | `#030303` | Primary background |
| `--vvd-heading-tick-width` | `3px` | Heading left-tick rule width |
| `--vvd-heading-tick-color` | `#9E001F` | Heading left-tick rule color |
| `--vvd-callout-rule-color` | `#9E001F` | Callout left border color |
| `--vvd-lh-normal` | `1.60` | Body line height |

**Example override snippet** (create as `.obsidian/snippets/void-overrides.css`):

```css
/* Softer glass blur */
:root { --vvd-glass-blur: 8px; }

/* Slightly warmer accent */
:root { --vvd-red-base: #B5001F; }

/* Tighter sidebar opacity */
:root { --vvd-glass-sidebar: rgba(8, 8, 8, 0.75); }
```

### Full Variable Inventory

See `_meta/design-tokens.md` for the complete annotated list of every `--vvd-*` variable.

---

## Examples

Paste these into a note to preview the theme's key surfaces:

```markdown
# H1 Heading — thin weight, blood-red left tick
## H2 Heading
### H3 Heading

Normal body text with [[internal links]] and [external links](https://example.com).
**Bold text** and *italic text* and ==highlighted text==.

`inline code`

> [!note] Glass Callout
> This is a glass void callout. The panel is a dark translucent red-tinted surface
> with a blood-red left border.

> [!warning] Warning Callout
> Brighter red border for cautions.

> [!danger] Danger Callout
> Maximum red — for critical alerts only.

| Column A | Column B | Column C |
|---|---|---|
| Row 1 | Data | Value |
| Row 2 | Data | Value |
```

---

## Compatibility

| Item | Status |
|---|---|
| Obsidian | 1.5.0+ |
| Dark mode | Full support |
| Light mode | Minimal passthrough (unstyled) |
| Mobile | Yes — glass degrades gracefully (no backdrop-filter on mobile) |
| Translucency | Designed for it; solid fallback included |
| Dataview | Compatible (no custom styling; uses theme base) |
| Tasks | Compatible |
| Calendar | Compatible |
| Excalidraw | Compatible (canvas uses `--canvas-background`) |
| Kanban | Compatible |
| V4D3R snippets | Designed to layer on top |

---

## Troubleshooting

**Glass effect not showing**
→ Enable *Translucent window* in Settings → Appearance. The glass surfaces only activate when `body.is-translucent` is present.

**Sidebar looks solid black instead of glass**
→ Same as above — translucency must be enabled in Obsidian's appearance settings.

**Text contrast seems low**
→ Override `--vvd-grey-light` to a brighter value, e.g. `#D0D0E0`. Current default passes WCAG AA on `#030303`.

**Headings appear too thin**
→ Override heading weights: `:root { --vvd-weight-thin: 400; }` to use normal weight for H1/H2.

**Callout glass blurs too aggressively**
→ Reduce blur: `:root { --vvd-glass-blur: 6px; }` or `:root { --vvd-glass-blur: 0px; }` to disable blur while keeping opacity.

**Theme looks identical to non-translucent mode**
→ Check that *Translucent window* is enabled. On some systems, the OS compositor must also support window transparency.

---

## Credits

- Part of the **V4D3R** theme family by Pur3v4d3r
- Typography: [JetBrains Mono](https://www.jetbrains.com/legalnotice/fonts/) (falls back to system monospace — no external loading)
- Built to the [Obsidian Snippet & Theme Expert v1.0.0](../.github/agents/_obsidian-snippet-theme-expert-v1.0.0.md) specification

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
