# V4D3R Forge

> Industrial brutalist Obsidian theme — Red / Black / Grey, JetBrains Mono everywhere, full-width canvas.

## Identity

The third sibling to the V4D3R family:

| Theme | Voice |
|-------|-------|
| **V4D3R Crimson** | Cyberpunk terminal — glow, uppercase, neon energy |
| **V4D3R Sanguine** | Editorial manuscript — serif feel, drop-cap, oldstyle |
| **V4D3R Forge** | Industrial brutalist — slab geometry, hammered steel, oxide red |

## Design Decisions

- **Palette**: Oxide red (`#8C1822`) on cool gunmetal (`#0D0E11`) with neutral steel greys (`#A0A8B0` body text, WCAG AAA on onyx).
- **Typography**: JetBrains Mono (or JetBrainsMono Nerd Font) routed to **every** font slot — text, UI, headings, code. No serif. No sans fallback for body.
- **Reading width**: **No cap.** `--vsf-reading-max-width: none` and `--file-line-width: 100%`, with `!important` overrides for `.is-readable-line-width`. Content fills the leaf regardless of Obsidian's "Readable line length" setting.
- **Headings**: H1 is a solid red slab block with a 4px anvil-red left bar. H2–H4 progressively decay through bold left bars. No glow, no small-caps, no manuscript decoration.
- **Callouts**: Square card with 3px oxide left rule. Title is a `[ TYPE ]` bracketed chip (visual brackets injected via `::before`/`::after`).
- **Lists**: `▸ ▹ ›` chevron decay through nesting levels.
- **HR**: Hairline grey bar with a 40px oxide-red center marker.
- **Tables**: Riveted-steel headers in uppercase tracking, zebra rows in slate.
- **Tags**: Square monospace pills with 1px faded-red border.

## Installation

The theme is already in `.obsidian/themes/V4D3R Forge/`. To activate:

1. Open Obsidian Settings → **Appearance**.
2. Under **Themes**, select **V4D3R Forge** from the dropdown.
3. (Optional) Install **JetBrains Mono** system-wide for best fidelity. Falls back gracefully to Fira Code → Consolas → system mono.

## Customization

All design tokens live in `PART 1` of `theme.css` under the `--vsf-*` prefix. To override without editing the theme, drop a CSS snippet into `.obsidian/snippets/` with rules like:

```css
.theme-dark {
  --vsf-red-oxide: #C0392B;          /* swap accent to a brighter red */
  --vsf-base-size: 16px;             /* bump body size */
  --vsf-reading-max-width: 900px;    /* re-enable a width cap */
}
```

## Contrast Verification

| Pair | Ratio | WCAG |
|------|-------|------|
| `--vsf-grey-nickel` (#A0A8B0) on `--vsf-black-onyx` (#0D0E11) | ≈ 9.7:1 | AAA |
| `--vsf-grey-silver` (#C8CFD6) on `--vsf-black-onyx` | ≈ 13.5:1 | AAA |
| `--vsf-red-oxide` (#8C1822) on `--vsf-grey-platinum` (#E4E9EE) | ≈ 6.4:1 | AA Large |
| `--vsf-grey-platinum` on `--vsf-red-oxide` (H1 slab) | ≈ 6.4:1 | AA Large |

## License

MIT — Pur3v4d3r
