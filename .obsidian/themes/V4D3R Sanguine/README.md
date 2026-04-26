# V4D3R Sanguine

A scholarly, editorial dark theme for Obsidian — the **noir-manuscript counterpart** to V4D3R Crimson. Same **Red / Black / Grey** palette, fundamentally different voice.

## Design Philosophy

Where Crimson screams *neon arcade* — saturated reds, glowing borders, all-caps mono — Sanguine whispers *leather-bound dossier*: deep oxblood, warm carbon blacks, parchment greys, true serif body, hairline rules instead of glows, sharp corners instead of rounded ones, manuscript-ribbon callouts instead of neon-shadow callouts.

You install Sanguine when you want to **read deeply** instead of **operate intensely**.

## Palette

| Role | Color | Hex |
|---|---|---|
| Primary accent | Oxblood | `#7A0F1A` |
| Deepest red | Garnet | `#5C0A14` |
| Secondary red | Rust | `#A33A3A` |
| Highlight red | Cinnabar | `#C46B5C` |
| Primary background | Carbon | `#14110F` |
| Secondary surface | Soot | `#1C1815` |
| Elevated surface | Ash | `#26211D` |
| Body text | Parchment | `#B8AFA6` |
| Emphasis text | Vellum | `#D4CDC4` |
| Drop-cap / max emphasis | Chalk | `#ECE7E0` |

All warm-toned. The greys carry a faint ochre-brown bias rather than blue-neutral.

## Typography

- **Body / Reading:** IBM Plex Serif → fallback `Georgia, "Iowan Old Style", serif`
- **UI / Interface:** IBM Plex Sans → fallback `system-ui, sans-serif`
- **Code / Editor:** IBM Plex Mono → fallback `"JetBrains Mono", Consolas, monospace`
- **Headings:** IBM Plex Serif, true small-caps via `font-variant-caps`
- **Drop cap on H1** (Reading View only, desktop)

If you don't have IBM Plex installed, the fallback chain is fine. To install:
- Windows: https://www.ibm.com/plex/ → download the Plex bundle → install Serif, Sans, Mono families
- Or via npm: `npm i @fontsource/ibm-plex-serif @fontsource/ibm-plex-sans @fontsource/ibm-plex-mono`

## Installation

1. Copy this folder (`V4D3R Sanguine`) into `<YourVault>/.obsidian/themes/`
2. Open Obsidian → **Settings → Appearance → Themes** → select **V4D3R Sanguine**

> A live copy is already installed in this vault at `.obsidian/themes/V4D3R Sanguine/`.

## Comparison vs V4D3R Crimson

| Dimension | Crimson | Sanguine |
|---|---|---|
| Voice | Cyberpunk terminal | Scholarly noir |
| Reds | Bright crimson + neon `#FF0000` | Oxblood, rust, garnet |
| Type | JBM Mono everywhere, Light 300 | Plex Serif body / Sans UI / Mono code |
| Headings | Black + intense red glow, all-small-caps | Oxblood serif small-caps, hairline rule, **drop cap on H1** |
| Bold | Pure red, **uppercase forced** | Oxblood, weight 600, case preserved |
| Italic | Red, weight 100 | Garnet, true serif italic |
| Corners | 12–15px rounded | 0–2px sharp |
| Borders | Glowing red halos | 1px hairline / double-rule |
| Shadows | Red neon glows | Soft true-black drops |
| Code blocks | Rounded gradient + glow | Square, soot bg, **3px left oxblood rule** |
| Inline code | Uppercase red, thick black border | Oxblood, thin underline, case preserved |
| Callouts | Black bg + neon border + red glow ("Neon Red Shadow") | Manuscript ribbon: 3px oxblood left rule, hanging icon, serif title |
| Lists | `→ - +` deep red | `§ ¶ ·` typographic markers |
| Brackets | Glowing pseudo-elements | Subtle oxblood, no glow |
| Tags | (default) | Manuscript-margin pills, italic serif on parchment-ash |

## Customization

Every color is a CSS custom property prefixed `--vsg-*`. Open `theme.css`, find the `1.1 COLOR PALETTE` block at the top, and override any value. Common tweaks:

```css
/* Brighten the accent red — picks up rust hover too */
:root { --vsg-red-oxblood: #8E1421; }

/* Cooler greys (less warm) */
:root {
  --vsg-grey-parchment: #B0B0AA;
  --vsg-grey-vellum:    #D0D0CA;
}

/* Disable drop cap on H1 */
:root { --vsg-dropcap-display: none; }

/* Tighten reading width */
:root { --vsg-reading-max-width: 80ch; }
```

## Plugin Compatibility Notes

- **Dataview** — table rules inherit; use the table styling block at PART 16 to adjust.
- **Tasks** — checkboxes restyled in PART 17 list section.
- **Calendar** — cell hover uses `--vsg-red-alpha-15`.
- **Excalidraw** — canvas background passthrough, no theme override.
- **Kanban** — card bg = `--vsg-black-soot`, border = hairline oxblood.

## Accessibility

- All text combinations validated WCAG AA minimum, most AAA.
- `parchment on carbon` ≈ 8.4:1 (AAA)
- `oxblood on parchment` ≈ 5.1:1 (AA)
- `prefers-reduced-motion: reduce` honored — all transitions disabled.
- `prefers-contrast: more` honored — text bumps to chalk, borders thicken.
- Mobile: drop cap auto-hidden on `body.is-mobile`, touch targets ≥ 44px.

## Credits

Built by **Pur3v4d3r** as the editorial counterpart to V4D3R Crimson. Inspired by manuscript typography, classic typeset book design, and the chiaroscuro aesthetic of noir film stills.

## License

MIT.

See `CHANGELOG.md` for version history.
