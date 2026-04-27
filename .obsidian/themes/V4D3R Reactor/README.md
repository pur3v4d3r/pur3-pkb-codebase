# V4D3R Reactor

**The cyberpunk/neon member of the V4D3R theme family.**

Void-black backgrounds. Neon red (#FF1E1E) accents. Static multi-layer glow effects on headings, code blocks, links, brackets, callouts, and active UI elements. No breathing animations — all glows are crisp and always-on.

> Companion themes: [V4D3R Sanguine](../V4D3R%20Sanguine/) (noir editorial) · [V4D3R Cinder](../V4D3R%20Cinder/) (polished card UI)

---

## Screenshots

> Add your own screenshots in `screenshots/` — `dark.png`, `light.png`, `headings.png`, `callouts.png`.

---

## Design Philosophy

Reactor commits to a single visual language: **neon over void**. The backgrounds push toward absolute black (#080A0D primary, #020204 for chrome), and the accent system uses fully-saturated neon red (#FF1E1E) exclusively. No desaturation, no pastels, no warm tones.

Glow effects are achieved through static `text-shadow` and `box-shadow` stacks — never `filter: brightness` or animations. The result is legible in normal use without the eye fatigue of pulsing effects.

Typography follows the V4D3R family convention: JetBrains Mono throughout all three font stacks (body, interface, monospace). Heading hierarchy is weight-based (bold → semibold → medium → normal) with neon intensity inversely matching depth (H1 = 4-layer glow, H6 = no glow).

---

## Installation

1. Open Obsidian → **Settings** → **Appearance**
2. Under **Themes**, click **Manage** → **Open themes folder**
3. Copy the entire `V4D3R Reactor/` folder into the themes folder
4. Return to **Settings** → **Appearance** → select **V4D3R Reactor**
5. Toggle **Dark mode** (recommended) or **Light mode**

---

## What It Does

| Feature | Detail |
|---------|--------|
| **Headings** | H1–H2 neon red with 3–4 layer `text-shadow` glow + left bar; H3 grey-frost + subtle glow; H4 italic + 1-layer; H5–H6 no glow |
| **Code blocks** | 3px neon red left rule with outward glow, graphite background, dark void shadows |
| **Inline code** | Neon red text on graphite, subtle glow, 2px border |
| **Wiki-link brackets** | Injected `[[` `]]` with neon red 2-layer glow via `::before`/`::after` |
| **Active nav item** | Red neon left border + inward glow + red text-shadow |
| **Active tab** | Neon red 2px bottom bar + neon box-shadow |
| **Callouts** | Neon left border, static 3-layer box-shadow glow, 14 type-specific color variants |
| **Scrollbars** | 6px pill, grey-deep default → red-ember hover → red-neon active |
| **Tags** | Dim red border, glows on hover |
| **HR** | Neon gradient line (transparent → red-neon → transparent) with glow |
| **Checkboxes** | Glowing neon border on check |
| **CTA Buttons** | Red-core background + neon border + glow |
| **Toggles** | Red-core when enabled + glow |

---

## Configuration — Top 10 Customizable Variables

Override any of these in a CSS snippet (`.obsidian/snippets/`) to customize Reactor without editing `theme.css`.

| Variable | Default | What It Controls |
|----------|---------|-----------------|
| `--vr-red-neon` | `#FF1E1E` | Primary accent color — all glows key off this |
| `--vr-red-core` | `#CC0A0A` | Left-bar borders on code, callouts, headings |
| `--vr-abyss` | `#080A0D` | Primary editor background |
| `--vr-graphite` | `#0F1115` | Sidebar, code block background |
| `--vr-grey-steel` | `#94A8BC` | Normal body text |
| `--vr-text-glow-h1` | (4-layer) | H1 text-shadow intensity — reduce all rgba() opacities |
| `--vr-glow-sm` | `0 0 4px rgba(255,30,30,0.50)` | Inner glow layer (tightest) |
| `--vr-glow-md` | `0 0 10px rgba(255,30,30,0.30)` | Mid glow layer |
| `--vr-font-mono` | JetBrains Mono | Font family for all text |
| `--vr-text-base` | `17px` | Base font size |

**Example snippet** — shift to orange neon:
```css
/* orange-reactor.css */
body {
  --vr-red-neon:  #FF6B1E;
  --vr-red-hot:   #FF8840;
  --vr-red-core:  #CC4A0A;
  --vr-red-ember: #8C3000;
  --vr-glow-sm:   0 0 4px  rgba(255, 107, 30, 0.50);
  --vr-glow-md:   0 0 10px rgba(255, 107, 30, 0.30);
  --vr-glow-lg:   0 0 22px rgba(255, 107, 30, 0.18);
}
```

---

## Plugin Compatibility Notes

| Plugin | Status | Notes |
|--------|--------|-------|
| **Dataview** | Works | Tables inherit Reactor's table styles |
| **Tasks** | Works | Checkboxes styled with neon glow |
| **Calendar** | Works | Uses Obsidian accent var (mapped to `--vr-red-neon`) |
| **Kanban** | Works | Cards use `--vr-slate` background |
| **Excalidraw** | Works | Draws on canvas, unaffected by theme |
| **Templater** | Works | No visual component |
| **QuickAdd** | Works | Modal uses Reactor styles |
| **Meta-Bind** | Works | Inputs styled with focus glow |
| **Breadcrumbs** | Works | Link colors apply |
| **Graph Analysis** | Works | Graph color tokens mapped |

---

## Troubleshooting

**Headings show no glow in Reading View**
Ensure you are viewing in Reading mode (Ctrl+E to toggle). Live Preview and Source mode use different selectors — both are covered, but check if a conflicting snippet overrides `text-shadow`.

**Glow effects feel too intense**
Reduce the `--vr-glow-sm` and `--vr-text-glow-h1` opacity values in a custom snippet. Start by halving all `rgba()` alpha values.

**Bracket injection (`[[` `]]`) appears doubled**
Another snippet may already be injecting brackets. Disable conflicting snippets like `square-bracket-glow.css` or `glowing-brackets-for-theme.css` when using Reactor (Reactor has its own bracket glow system).

**Light mode looks washed out**
Light mode is intentional — glow effects run at ~50% intensity on light surfaces. For full neon impact, use dark mode.

**Font doesn't look like JetBrains Mono**
Install [JetBrains Mono](https://www.jetbrains.com/lp/mono/) or [JetBrainsMono Nerd Font](https://www.nerdfonts.com/). Theme falls back to IBM Plex Mono → Consolas → system monospace.

---

## Credits

Part of the **V4D3R theme family** by [Pur3v4d3r](https://github.com/pur3v4d3r).

Neon glow technique adapted from vault snippets: `callout-mod-neon-red-shadow.css` and `01-glowing-headers.css`.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
