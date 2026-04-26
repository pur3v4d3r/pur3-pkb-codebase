# V4D3R Cinder

Third theme in the V4D3R family. Industrial card-system dark theme for Obsidian.

**Aesthetic voice:** Polished design system / dark UI component library.

---

## What It Does

Cinder is intentionally different from V4D3R Sanguine and V4D3R Crimson:

| | Sanguine / Crimson | Cinder |
|---|---|---|
| **Reds** | Deep oxblood `#7A0F1A` | Vivid crimson `#8F1622` |
| **Greys** | Warm ochre-parchment | Cool blue-grey slate |
| **Corners** | 0–1px brutalist | 3px card rounding |
| **Typography** | Small-caps, editorial markers | Weight-based, clean hierarchy |
| **Cards** | Flat, implicit | Explicit box-shadow elevation |
| **List markers** | § ¶ · ornamental | — › · structural |
| **Headings** | Double-rule borders | Colored left accent bars |

---

## Installation

1. Copy the `V4D3R Cinder` folder to `.obsidian/themes/`
2. Open Obsidian → Settings → Appearance → Themes
3. Select **V4D3R Cinder**

---

## Top 10 Customization Variables

Override these in a CSS snippet to tune the theme:

| Variable | Default | Purpose |
|---|---|---|
| `--vc-red-primary` | `#8F1622` | Main accent: links, H1 border, active states |
| `--vc-red-mid` | `#B52D38` | Secondary: H2, hover, strong text |
| `--vc-grey-base` | `#8AA0B2` | Body text color |
| `--vc-grey-bright` | `#C8DCEA` | Max emphasis text |
| `--vc-black-primary` | `#0C0C10` | Main note background |
| `--vc-black-card` | `#1A1A20` | Card surface color |
| `--vc-font-base-size` | `17px` | Base font size |
| `--vc-shadow-md` | `0 2px 8px rgba(2,2,5,0.65)` | Card elevation shadow |
| `--vc-radius-md` | `3px` | Standard card corner radius |
| `--vc-max-width` | `110ch` | Reading / editor content width |

---

## Design Philosophy

Cinder uses the **card as the primary visual organizing unit**. Every interactive region — file explorer items, search results, callouts, settings sections, command palette entries — presents itself as a discrete card with a visible border and subtle elevation shadow.

Typography is weight-dominant rather than decoration-dominant: headings are differentiated by size, weight, and colored left accent bars, not by small-caps, ornamental markers, or editorial conventions.

The grey palette runs definitively cool — blue-grey slate with no ochre or warm undertones. Combined with the more vivid crimson reds, this creates a crisper, higher-clarity feel than the warm manuscript tones of Sanguine.

---

## Plugin Compatibility

| Plugin | Notes |
|---|---|
| Dataview | Tables and lists inherit theme styling |
| Calendar | Today highlight uses red-alpha-15 |
| Kanban | Board and card surfaces match theme |
| Tasks | Checkboxes use theme colors |
| Canvas | Node cards and edges styled |
| Graph view | Nodes, links, and background mapped |

---

## Troubleshooting

**Theme doesn't appear in Appearance settings**
Check that `manifest.json` is present in the `V4D3R Cinder` folder.

**Colors look wrong / warm**
Ensure no other CSS snippets are overriding `--vc-grey-*` variables. Check `.obsidian/snippets/`.

**Headings don't show left bars**
Left accent bars use `border-left` on heading elements. If a snippet removes `padding-left` from headings, bars will be hidden.

**Code blocks missing left accent**
The `pre` selector is targeted with `!important` for background to override Obsidian defaults. If another snippet also uses `!important`, the last loaded wins.

---

## Changelog

### 1.0.0
- Initial release
- Full dark theme implementation: 37 sections
- Basic light theme parity
- Plugin compatibility: Dataview, Calendar, Kanban, Canvas, Graph
