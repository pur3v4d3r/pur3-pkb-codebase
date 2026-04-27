# V4D3R Obsidian

> The **card-deck** theme. Modern application surface — black canvas, floating graphite cards with clear elevation, vivid arterial-red signal accent. Where **V4D3R Sanguine** is a noir manuscript page, **V4D3R Obsidian** is a dashboard.

| | |
|---|---|
| **Version** | 1.0.0 |
| **Min Obsidian** | 1.5.0+ |
| **Mode** | Dark only |
| **Mobile** | Yes |
| **Translucency** | Yes (backdrop blur on cards) |
| **License** | MIT |

> [!important] Design intent
> V4D3R Obsidian deliberately does **not** look like V4D3R Sanguine or V4D3R Crimson. It shares only the Red / Black / Grey palette family. Geometry, typography, surface model, and accent intensity all change axis so the three themes feel like genuinely different tools, not recolors.

---

## Screenshots

> Add screenshots to `screenshots/` and they will render here.

- `screenshots/dark.png` — main editor view
- `screenshots/cards.png` — card-deck workspace layout
- `screenshots/callouts.png` — card-callout gallery
- `screenshots/settings.png` — settings modal

---

## Design Philosophy

**Three commitments make this theme feel different:**

1. **Cards, not surfaces.** Every workspace pane is a discrete elevated card with a 1px stroke, a 10px radius, and a soft drop shadow. The gutter between cards is real and visible. Hovering or activating a card lifts it with a stronger shadow. This is the single most important visual difference from the manuscript-page feel of Sanguine.

2. **Arterial red as a signal — not a body color.** The accent `#E5343A` is reserved for things that demand attention: the active tab bar, the active sidebar item, focus rings, primary CTA buttons, link hover, callout-error. Body text links use a calmer carmine `#C8474C` so reading prose doesn't feel like reading warning labels.

3. **Typographic split.** Inter for everything you read or click. JetBrains Mono for inline code, code blocks, and syntax tokens only. The ratio creates clear visual register switches between prose and code.

---

## Installation

1. Quit Obsidian (optional but recommended for first install).
2. Copy the entire `V4D3R Obsidian` folder into your vault's themes directory:
   ```
   <your-vault>/.obsidian/themes/V4D3R Obsidian/
   ```
3. Open Obsidian → **Settings → Appearance**.
4. Under **Themes**, pick **V4D3R Obsidian** from the dropdown.
5. Confirm **Base color scheme** is set to **Dark** (the theme is dark-only).

---

## Customization

All custom properties are prefixed `--vob-*` so you can override any of them in a personal CSS snippet without editing `theme.css`.

Create `<vault>/.obsidian/snippets/vob-overrides.css` and toggle it on under **Settings → Appearance → CSS snippets**.

### Top variables you'll most likely want to tweak

| Variable | Default | Controls |
|---|---|---|
| `--vob-red-arterial` | `#E5343A` | The signal accent — active tab bar, focus ring, primary button, link hover. The single most important color. |
| `--vob-red-carmine` | `#C8474C` | Body link color (calmer than arterial). |
| `--vob-red-signal` | `#FF3B41` | Hottest red — error edge, active hover on accent. |
| `--vob-black-canvas` | `#0A0A0B` | The workspace background (true canvas behind all cards). |
| `--vob-black-card` | `#181A1D` | Default card surface — every leaf, search hit, callout starts here. |
| `--vob-black-card-high` | `#242830` | Highest elevation — modals, popovers, the active-tab solid top. |
| `--vob-grey-fog` | `#B8BDC4` | Body text color. WCAG AAA on canvas. |
| `--vob-grey-frost` | `#ECEFF3` | Heading + emphasis text. |
| `--vob-radius-md` | `10px` | Default card radius. Drop to 6 for a tighter look, raise to 14 for softer. |
| `--vob-base-size` | `15.5px` | Editor + UI base font size. |
| `--vob-font-ui` | Inter stack | UI + body font. Swap for `-apple-system` or your preferred sans. |
| `--vob-font-mono` | JetBrains Mono | Code font. Swap for Fira Code, SF Mono, Cascadia, etc. |
| `--vob-shadow-rest` | 1px+1px shadow | Drop shadow on resting cards. Set to `none` for a flat variant. |

### Example override snippet

```css
/* vob-overrides.css — softer, larger, hotter accent */
body.theme-dark {
  --vob-red-arterial: #FF1F26;        /* hotter accent */
  --vob-radius-md:    14px;            /* softer corners */
  --vob-base-size:    16px;            /* a touch larger */
  --vob-shadow-rest:  none;            /* flat cards */
}
```

---

## Plugin Compatibility

| Plugin | Status | Notes |
|---|---|---|
| **Dataview** | ✅ Works | Tables inherit the card-table styling automatically. |
| **Tasks** | ✅ Works | Checkbox styling applies; task done state strikes through with rust color. |
| **Calendar** | ✅ Works | Day cells inherit `--background-modifier-*` and look at home. |
| **Excalidraw** | ✅ Works | Canvas chrome uses theme colors; drawings unaffected. |
| **Kanban** | ✅ Works | Card-on-card looks correct because we use card-high for elevated surfaces. |
| **Properties** | ✅ Native | Heavy customization in PART 16. |
| **Canvas (core)** | ✅ Works | PART 18 styles nodes + edges. |
| **Graph view (core)** | ✅ Works | PART 18 styles graph colors. |

If a plugin renders inside its own `.workspace-leaf-content[data-type="..."]` it should layer cleanly without further intervention.

---

## Troubleshooting

**The theme didn't appear in the dropdown.**
Make sure the folder is named exactly `V4D3R Obsidian` (with a space, no underscore) and contains both `manifest.json` and `theme.css`. Restart Obsidian.

**Tabs look strangely angled / clipped.**
The pill-tab redesign disables Obsidian's default skewed-corner pseudo-elements. If you also have a snippet that re-styles `.workspace-tab-header::before/::after`, disable it — it will conflict.

**Some buttons are too red / too quiet.**
The accent is intentionally vivid. Either drop it in `--vob-red-arterial` (e.g. `#B83840` for a calmer feel) or override `--vob-red-carmine` if it's body links you want to tone down.

**Headings have a small triangle (`▸`) before them.**
Intentional design accent on H3 only. Remove with:
```css
.markdown-preview-view h3::before { content: none; }
```

**Code blocks have a faint red gradient on top.**
Intentional accent bar. Disable with:
```css
.markdown-rendered pre::before { display: none; }
```

**Cards don't lift on hover.**
You probably have `prefers-reduced-motion: reduce` enabled at the OS level — the theme respects this. Disable in your OS accessibility settings if you want the lift back.

---

## Changelog

See [`CHANGELOG.md`](./CHANGELOG.md).

---

## Credits

- **Inter** typeface by Rasmus Andersson — `https://rsms.me/inter/`
- **JetBrains Mono** typeface by JetBrains — `https://www.jetbrains.com/lp/mono/`
- Geometry + elevation language inspired by modern application design (no specific theme borrowed from).
- Variable architecture and section organization mirror the V4D3R Sanguine pattern for cross-theme maintenance consistency.
