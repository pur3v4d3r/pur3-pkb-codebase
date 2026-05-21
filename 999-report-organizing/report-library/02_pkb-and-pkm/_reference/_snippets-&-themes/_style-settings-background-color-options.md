---
aliases:
  - pkb theme
  - PKB Theme
  - Theme
  - Background Theme
---



```
### Option 1: "Soft Charcoal" (Neutral & Professional)

This shifts your background from "Black" to a "Dark Slate." This is the safest bet. It maintains high contrast for your Gold (`#FFC700`) and Purple (`#7800F4`) accents but removes the harshness of the void black.

  * **Primary Background (`bg1`):** `#1F2023` (Soft dark grey, \~10% lighter than current)
  * **Secondary Background (`bg2`):** `#25262A` (Lighter grey for sidebars)
  * **Tertiary Background (`bg3`):** `#32343A` (Active panes/modals)
  * **Code Background:** `#191A1D` (Just slightly darker than the main bg)

### Option 2: "Muted Amethyst" (Thematic & Branded)

Since your primary identity color is purple, this background introduces a very subtle violet tint to the dark grey. It feels cohesive with your `#7800F4` accent and makes the vault feel like a designed environment rather than just "dark mode."

  * **Primary Background (`bg1`):** `#1E1B24` (Dark Grey with purple undertone)
  * **Secondary Background (`bg2`):** `#25212E` (Sidebar)
  * **Tertiary Background (`bg3`):** `#2D2838` (Active panes)
  * **Code Background:** `#18151D`

### Option 3: "Deep Gunmetal" (Cool & Crisp)

This uses a cool-toned grey (slightly blueish). This pairs exceptionally well with your Teal (`#72FFF1`) icon colors and provides a "tech/IDE" feel similar to VS Code's default dark themes.

  * **Primary Background (`bg1`):** `#1E2227`
  * **Secondary Background (`bg2`):** `#23272E`
  * **Tertiary Background (`bg3`):** `#2C313A`
  * **Code Background:** `#181B1F`

-----

```
### How to Apply (Recommended JSON Update)

I recommend **Option 2 (Muted Amethyst)** as it aligns best with your "Pur3v4d3r" persona and the purple/gold aesthetic.

You can manually plug these hex codes into the Style Settings plugin under **Minimal \> Colors**, or update your JSON with the following block (this replaces just the background section of your export):

```json
{
  "minimal-style@@bg1@@dark": "#1E1B24",
  "minimal-style@@bg2@@dark": "#25212E",
  "minimal-style@@bg3@@dark": "#2D2838",
  "minimal-style@@frame-background@@dark": "#25212E",
  "minimal-style@@code-background@@dark": "#18151D",
  "minimal-style@@gutter-background@@dark": "#25212E",
  "minimal-style@@workspace-background-translucent@@dark": "#7800F420"
}
```

**Next Step:** Would you like me to generate a CSS snippet to apply a "glassmorphism" effect to your sidebars, which would add depth to these lighter colors?

### Deep Cosmos (Blue-Tinted)
````
### Option 1: "Deep Cosmos" (Blue-Tinted)

*Matches your interest in Cosmology.*
This is a spiritual successor to Muted Amethyst but shifts the tint from Purple to **Deep Navy**. Because Gold and Blue are complementary colors, your **Gold accents (`#FFC700`)** will pop incredibly hard against this background, creating a high-energy, professional look. It feels like a command center.

  * **Primary Background (`bg1`):** `#151720` (Deepest Navy)
  * **Secondary Background (`bg2`):** `#1A1D26` (Sidebar)
  * **Tertiary Background (`bg3`):** `#232732` (Active/Modals)
  * **Code Background:** `#111319`

<!-- end list -->

```json
{
  "minimal-style@@bg1@@dark": "#151720",
  "minimal-style@@bg2@@dark": "#1A1D26",
  "minimal-style@@bg3@@dark": "#232732",
  "minimal-style@@frame-background@@dark": "#1A1D26",
  "minimal-style@@code-background@@dark": "#111319",
  "minimal-style@@gutter-background@@dark": "#1A1D26"
}
```
````

### Warm Carbon (Brown-Tinted)
`````

### Option 2: "Warm Carbon" (Brown-Tinted)

*Optimized for long reading sessions.*
This moves in the opposite direction, adding a subtle **Warm/Espresso** tint. This creates a "Gruvbox" style aesthetic. It is very easy on the eyes for long writing sessions and softens the harshness of digital screens. Your **Purple accents** will stand out uniquely here, looking almost regal against the warm dark grey.

  * **Primary Background (`bg1`):** `#1E1D1B` (Warm Dark Grey)
  * **Secondary Background (`bg2`):** `#262422` (Sidebar)
  * **Tertiary Background (`bg3`):** `#2E2C29` (Active/Modals)
  * **Code Background:** `#171615`

<!-- end list -->

```json
{
  "minimal-style@@bg1@@dark": "#1E1D1B",
  "minimal-style@@bg2@@dark": "#262422",
  "minimal-style@@bg3@@dark": "#2E2C29",
  "minimal-style@@frame-background@@dark": "#262422",
  "minimal-style@@code-background@@dark": "#171615",
  "minimal-style@@gutter-background@@dark": "#262422"
}
```
`````

### Titanium Slate (Neutral & Lighter)
````
### Option 3: "Titanium Slate" (Neutral & Lighter)

*Maximum Clarity.*
You mentioned you wanted something "lighter." This is the lightest of the dark themes I would recommend without washing out your text. It is a **Neutral Slate Grey** (similar to the Linear interface or GitHub Dark Dimmed). It removes all color tinting from the background, allowing your colorful syntax highlighting and tags to take center stage.

  * **Primary Background (`bg1`):** `#212121` (Solid Graphite)
  * **Secondary Background (`bg2`):** `#262626` (Sidebar)
  * **Tertiary Background (`bg3`):** `#303030` (Active/Modals)
  * **Code Background:** `#1C1C1C`

<!-- end list -->

```json
{
  "minimal-style@@bg1@@dark": "#212121",
  "minimal-style@@bg2@@dark": "#262626",
  "minimal-style@@bg3@@dark": "#303030",
  "minimal-style@@frame-background@@dark": "#262626",
  "minimal-style@@code-background@@dark": "#1C1C1C",
  "minimal-style@@gutter-background@@dark": "#262626"
}
`````

-----

### Comparison of the Vibe

| Option | Tint | Effect on Gold Accents | Effect on Purple Accents | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Cosmos** | Blue/Navy | **High Contrast (Pop)** | Harmonious (Cool) | Focus, Engineering, Science |
| **Warm Carbon** | Brown/Red | Soft/Integrated | **High Contrast (Unique)** | Long Reading, Journaling, Philosophy |
| **Titanium Slate** | Neutral | Balanced | Balanced | Photography, Image Editing (Color accuracy) |

**Next Step:** If you settle on one of these lighter backgrounds, the "translucency" effect in Obsidian can sometimes look muddy. Would you like a CSS snippet to increase the blur/vibrancy of your sidebars so the new background color shines through nicely?

### Muted Amethyst Background
```
{
  "minimal-style@@bg2@@dark": "#25212E",
  "minimal-style@@bg3@@dark": "#2D2838",
  "minimal-style@@ui2@@dark": "#7800F4",
  "minimal-style@@ax1@@dark": "#FFC700",
  "minimal-style@@ax2@@dark": "#FFE066",
  "minimal-theme@@color-accent-light": "#BE93FD",
  "minimal-theme@@color-accent-dark": "#BE93FD",
  "minimal-theme@@color-bg-primary-light": "#fcfcfc",
  "minimal-theme@@color-bg-secondary-light": "#f2f2f7",
  "minimal-theme@@color-bg-primary-dark": "#1c1c1e",
  "minimal-theme@@color-bg-secondary-dark": "#2c2c2e",
  "minimal-theme@@color-text-primary-light": "#1c1c1e",
  "minimal-theme@@color-text-primary-dark": "#f2f2f7",
  "minimal-theme@@color-text-normal-light": "#1c1c1e",
  "minimal-theme@@color-text-normal-dark": "#f2f2f7",
  "minimal-theme@@color-text-secondary-light": "#6e6e73",
  "minimal-theme@@color-text-secondary-dark": "#8d8d93",
  "minimal-theme@@color-text-faint-light": "#999999",
  "minimal-theme@@color-text-faint-dark": "#777777",
  "minimal-theme@@color-interactive-accent-light": "#BE93FD",
  "minimal-theme@@color-interactive-accent-dark": "#BE93FD",
  "minimal-theme@@link-unresolved-color-light": "#a8a8a8",
  "minimal-theme@@link-unresolved-color-dark": "#7a7a7a",
  "minimal-theme@@code-background-light": "#f2f2f7",
  "minimal-theme@@code-background-dark": "#2c2c2e",
  "minimal-style@@file-header-justify": "center",
  "minimal-style@@tag-color@@dark": "#FFC700",
  "minimal-style@@tag-background@@dark": "#212324",
  "minimal-style@@tag-background-hover@@dark": "#282838",
  "minimal-style@@tag-radius": "14px",
  "minimal-style@@minimal-tab-text-color@@dark": "#FFC700",
  "minimal-style@@minimal-tab-text-color-active@@dark": "#EAEAEA",
  "minimal-style@@row-lines": true,
  "minimal-style@@col-lines": true,
  "minimal-style@@table-lines": false,
  "minimal-style@@row-alt": true,
  "minimal-style@@col-alt": true,
  "minimal-style@@table-tabular": false,
  "minimal-style@@table-numbers": false,
  "minimal-style@@table-center": true,
  "minimal-style@@table-nowrap": false,
  "minimal-style@@row-hover": true,
  "minimal-style@@table-row-background-hover@@dark": "#4F00FF47",
  "minimal-style@@maximize-tables-off": "maximize-tables",
  "minimal-style@@ribbon-style": "ribbon-bottom-left-hover",
  "minimal-style@@sidebar-tabs-style": "sidebar-tabs-wide",
  "minimal-style@@hide-help": false,
  "minimal-style@@hide-settings": false,
  "minimal-style@@sidebar-tabs-names": "tab-names-single",
  "minimal-style@@metadata-heading-off": true,
  "minimal-style@@metadata-add-property-off": true,
  "minimal-style@@metadata-icons-off": false,
  "minimal-style@@metadata-dividers": true,
  "minimal-style@@progress-complete@@dark": "#BE93FD",
  "minimal-style@@pdf-page-style": "pdf-shadows-on",
  "minimal-style@@pdf-invert-dark": false,
  "minimal-style@@checkbox-shape": "checkbox-square",
  "minimal-style@@minimal-strike-lists": true,
  "minimal-style@@active-line-on": true,
  "minimal-style@@workspace-background-translucent@@dark": "#7800F420",
  "minimal-style@@indentation-guide-color-active@@dark": "#FFC700",
  "minimal-style@@indentation-guide-color@@dark": "#FFC700",
  "minimal-style@@icon-color@@dark": "#72FFF1",
  "minimal-style@@icon-color-hover@@dark": "#FFD84D",
  "minimal-style@@icon-color-focused@@dark": "#FFD84D",
  "minimal-style@@embed-strict": false,
  "minimal-style@@embed-underline": false,
  "minimal-style@@dataview-inline-lists": true,
  "minimal-style@@callouts-style": "callouts-outlined",
  "minimal-style@@h1-l": true,
  "minimal-style@@h2-l": false,
  "minimal-style@@h3-l": true,
  "minimal-style@@h4-l": false,
  "minimal-style@@h5-l": false,
  "minimal-style@@h6-l": false,
  "minimal-style@@bold-color@@dark": "#9E3EFF",
  "minimal-style@@tx2@@dark": "#EAEAEA",
  "minimal-style@@tx3@@dark": "#EAEAEA",
  "minimal-style@@tx1@@dark": "#EAEAEA",
  "minimal-style@@h1-font": "Jetbrains Mono",
  "minimal-style@@h2-font": "Jetbrains Mono",
  "minimal-style@@h3-color@@dark": "#FFECA6",
  "minimal-style@@h4-color@@dark": "#CDCDCD",
  "minimal-style@@h5-color@@dark": "#B5B5B5",
  "minimal-style@@h6-color@@dark": "#595959",
  "minimal-style@@h6-font": "Jetbrains Mono",
  "minimal-style@@h5-font": "Jetbrains Mono",
  "minimal-style@@h4-font": "Jetbrains Mono",
  "minimal-style@@h3-font": "Jetbrains Mono",
  "minimal-style@@h4-weight": 100,
  "minimal-style@@minimal-code-scroll": false,
  "minimal-advanced@@hide-markdown": false,
  "minimal-advanced@@hide-settings-desc": false,
  "minimal-advanced@@animations": "default",
  "minimal-style@@trim-cols": false,
  "minimal-style@@inline-title-font": "Jetbrains Mono",
  "minimal-style@@file-header-visibility": "minimal-tab-title-hover",
  "minimal-style@@blockquote-font-style": "normal",
  "minimal-style@@image-grid-fit": "cover",
  "minimal-style@@list-indent": 1.3,
  "minimal-style@@code-function@@dark": "#9E6AD3",
  "minimal-style@@code-string@@dark": "#B58900",
  "minimal-style@@code-operator@@dark": "#D33682",
  "minimal-style@@code-punctuation@@dark": "#839496",
  "minimal-style@@code-important@@dark": "#CB4B16",
  "minimal-style@@code-property@@dark": "#9E6AD3",
  "minimal-style@@code-comment@@dark": "#7A00FF",
  "minimal-style@@ax3@@dark": "#FFC700",
  "minimal-style@@color-yellow@@dark": "#A5FF00",
  "minimal-style@@color-green@@dark": "#27FF00",
  "minimal-style@@color-cyan@@dark": "#00FFEA",
  "minimal-style@@color-blue@@dark": "#006CFF",
  "minimal-style@@color-purple@@dark": "#9E6AD3",
  "minimal-style@@color-pink@@dark": "#FF00DC",
  "minimal-style@@h1-color@@dark": "#FFC700",
  "minimal-style@@h2-color@@dark": "#AA00FF",
  "minimal-style@@h6-variant": "normal",
  "minimal-style@@h5-variant": "normal",
  "minimal-style@@h4-variant": "normal",
  "minimal-style@@text-formatting@@dark": "#FFC700",
  "minimal-style@@bold-modifier": 100,
  "minimal-style@@file-header-font-weight": 100,
  "minimal-style@@inline-title-color@@dark": "#72FFF1",
  "minimal-style@@inline-title-weight": 100,
  "minimal-style@@frame-background@@dark": "#25212E",
  "minimal-style@@blockquote-color@@dark": "#EAEAEA",
  "minimal-style@@code-background@@dark": "#18151D",
  "minimal-style@@code-normal@@dark": "#EAEAEA",
  "minimal-style@@blockquote-background-color@@dark": "#464653",
  "minimal-style@@sp1@@dark": "#EAEAEA",
  "minimal-style@@color-red@@dark": "#FF0000",
  "minimal-style@@color-orange@@dark": "#FF5700",
  "minimal-style@@h1-variant": "small-caps",
  "minimal-style@@h2-variant": "small-caps",
  "minimal-style@@h3-variant": "small-caps",
  "minimal-style@@gutter-background@@dark": "#25212E",
  "minimal-style@@line-number-color@@dark": "#8d8d93",
  "minimal-style@@checkbox-color@@dark": "#FFC700",
  "minimal-style@@h2-weight": 100,
  "minimal-style@@h1-weight": 100,
  "minimal-style@@h3-weight": 100,
  "minimal-style@@h5-weight": 100,
  "minimal-style@@h6-weight": 100,
  "id@@callout-on": true,
  "id@@h1-underline": true,
  "id@@h2-underline": true,
  "id@@headers-one-color": true,
  "minimal-style@@blockquote-border-color@@dark": "#FFC700",
  "minimal-style@@embed-max-height": "1000",
  "minimal-style@@embed-background@@dark": "#101010",
  "minimal-style@@embed-hide-title": false,
  "minimal-style@@embed-decoration-style": "dashed",
  "minimal-style@@embed-decoration-color@@dark": "#9E6AD3",
  "minimal-style@@code-size": "0.93em",
  "minimal-style@@link-external-color-hover@@dark": "#FFC700",
  "minimal-style@@link-external-color@@dark": "#828282",
  "minimal-style@@link-color@@dark": "#72FFF1",
  "minimal-style@@link-color-hover@@dark": "#7800F4",
  "minimal-style@@link-unresolved-color@@dark": "#72FFF1",
  "minimal-style@@link-unresolved-decoration-color@@dark": "#FFC700",
  "minimal-style@@blockquote-size": "22",
  "minimal-style@@blockquote-border-thickness": 2,
  "minimal-style@@max-col-width": "18em",
  "minimal-style@@h1-size": "2.5em",
  "minimal-style@@h1-style": "normal",
  "minimal-style@@h2-style": "normal",
  "minimal-style@@h2-size": "2.3em",
  "minimal-style@@h3-size": "1.6em",
  "minimal-style@@h4-size": "1.4em",
  "minimal-style@@h5-size": "1.4em",
  "minimal-style@@h6-size": "1.4em",
  "minimal-style@@list-spacing": 0.015,
  "minimal-style@@metadata-label-width-multiplier": 11,
  "minimal-style@@vault-profile-display": "vault-profile-default",
  "minimal-style@@minimal-unstyled-tags": false,
  "minimal-style@@tag-border-width": "1px",
  "minimal-style@@link-unresolved-opacity": 0.4,
  "minimal-style@@file-header-font-size": "1.25em",
  "minimal-style@@inline-title-size": "1.6em",
  "minimal-style@@bg1@@dark": "#1E1B24",
  "minimal-cards-style@@cards-min-width": "200x",
  "minimal-advanced@@cursor": "default",
  "checkbox@@check-color": true,
  "checkbox@@check-bg": false,
  "checkbox@@check-text": false,
  "checkbox@@check-strike": false,
  "minimal-style@@tabs-style": "tabs-modern",
  "minimal-style@@hl2@@dark": "#CCB20047",
  "minimal-style@@hl1@@dark": "#5E00FF47",
  "minimal-style@@p-spacing": "1.3.7rem",
  "minimal-style@@title-color@@dark": "#5400FF",
  "minimal-style@@title-color-inactive@@dark": "#7E00FF",
  "minimal-style@@window-title-off": true,
  "minimal-style@@frame-icon-color@@dark": "#7E00FF",
  "minimal-style@@titlebar-text-color-focused@@dark": "#FFD400",
  "minimal-style@@titlebar-text-color@@dark": "#6900FF",
  "minimal-style@@titlebar-text-weight": 200,
  "minimal-style@@italic-color@@dark": "#D1A1FF",
  "minimal-advanced@@font-ui-small": 16,
  "minimal-advanced@@font-ui-smaller": 16,
  "minimal-style@@bases-table-row-height": 40
}
```

### Soft dark grey Background
```
{
  "minimal-style@@bg2@@dark": "#25262A",
  "minimal-style@@bg3@@dark": "#32343A",
  "minimal-style@@ui2@@dark": "#7800F4",
  "minimal-style@@ax1@@dark": "#FFC700",
  "minimal-style@@ax2@@dark": "#FFE066",
  "minimal-theme@@color-accent-light": "#BE93FD",
  "minimal-theme@@color-accent-dark": "#BE93FD",
  "minimal-theme@@color-bg-primary-light": "#fcfcfc",
  "minimal-theme@@color-bg-secondary-light": "#f2f2f7",
  "minimal-theme@@color-bg-primary-dark": "#1c1c1e",
  "minimal-theme@@color-bg-secondary-dark": "#2c2c2e",
  "minimal-theme@@color-text-primary-light": "#1c1c1e",
  "minimal-theme@@color-text-primary-dark": "#f2f2f7",
  "minimal-theme@@color-text-normal-light": "#1c1c1e",
  "minimal-theme@@color-text-normal-dark": "#f2f2f7",
  "minimal-theme@@color-text-secondary-light": "#6e6e73",
  "minimal-theme@@color-text-secondary-dark": "#8d8d93",
  "minimal-theme@@color-text-faint-light": "#999999",
  "minimal-theme@@color-text-faint-dark": "#777777",
  "minimal-theme@@color-interactive-accent-light": "#BE93FD",
  "minimal-theme@@color-interactive-accent-dark": "#BE93FD",
  "minimal-theme@@link-unresolved-color-light": "#a8a8a8",
  "minimal-theme@@link-unresolved-color-dark": "#7a7a7a",
  "minimal-theme@@code-background-light": "#f2f2f7",
  "minimal-theme@@code-background-dark": "#2c2c2e",
  "minimal-style@@file-header-justify": "center",
  "minimal-style@@tag-color@@dark": "#FFC700",
  "minimal-style@@tag-background@@dark": "#212324",
  "minimal-style@@tag-background-hover@@dark": "#282838",
  "minimal-style@@tag-radius": "14px",
  "minimal-style@@minimal-tab-text-color@@dark": "#FFC700",
  "minimal-style@@minimal-tab-text-color-active@@dark": "#EAEAEA",
  "minimal-style@@row-lines": true,
  "minimal-style@@col-lines": true,
  "minimal-style@@table-lines": false,
  "minimal-style@@row-alt": true,
  "minimal-style@@col-alt": true,
  "minimal-style@@table-tabular": false,
  "minimal-style@@table-numbers": false,
  "minimal-style@@table-center": true,
  "minimal-style@@table-nowrap": false,
  "minimal-style@@row-hover": true,
  "minimal-style@@table-row-background-hover@@dark": "#4F00FF47",
  "minimal-style@@maximize-tables-off": "maximize-tables",
  "minimal-style@@ribbon-style": "ribbon-bottom-left-hover",
  "minimal-style@@sidebar-tabs-style": "sidebar-tabs-wide",
  "minimal-style@@hide-help": false,
  "minimal-style@@hide-settings": false,
  "minimal-style@@sidebar-tabs-names": "tab-names-single",
  "minimal-style@@metadata-heading-off": true,
  "minimal-style@@metadata-add-property-off": true,
  "minimal-style@@metadata-icons-off": false,
  "minimal-style@@metadata-dividers": true,
  "minimal-style@@progress-complete@@dark": "#BE93FD",
  "minimal-style@@pdf-page-style": "pdf-shadows-on",
  "minimal-style@@pdf-invert-dark": false,
  "minimal-style@@checkbox-shape": "checkbox-square",
  "minimal-style@@minimal-strike-lists": true,
  "minimal-style@@active-line-on": true,
  "minimal-style@@workspace-background-translucent@@dark": "#7800F420",
  "minimal-style@@indentation-guide-color-active@@dark": "#FFC700",
  "minimal-style@@indentation-guide-color@@dark": "#FFC700",
  "minimal-style@@icon-color@@dark": "#72FFF1",
  "minimal-style@@icon-color-hover@@dark": "#FFD84D",
  "minimal-style@@icon-color-focused@@dark": "#FFD84D",
  "minimal-style@@embed-strict": false,
  "minimal-style@@embed-underline": false,
  "minimal-style@@dataview-inline-lists": true,
  "minimal-style@@callouts-style": "callouts-outlined",
  "minimal-style@@h1-l": true,
  "minimal-style@@h2-l": false,
  "minimal-style@@h3-l": true,
  "minimal-style@@h4-l": false,
  "minimal-style@@h5-l": false,
  "minimal-style@@h6-l": false,
  "minimal-style@@bold-color@@dark": "#9E3EFF",
  "minimal-style@@tx2@@dark": "#EAEAEA",
  "minimal-style@@tx3@@dark": "#EAEAEA",
  "minimal-style@@tx1@@dark": "#EAEAEA",
  "minimal-style@@h1-font": "Jetbrains Mono",
  "minimal-style@@h2-font": "Jetbrains Mono",
  "minimal-style@@h3-color@@dark": "#FFECA6",
  "minimal-style@@h4-color@@dark": "#CDCDCD",
  "minimal-style@@h5-color@@dark": "#B5B5B5",
  "minimal-style@@h6-color@@dark": "#595959",
  "minimal-style@@h6-font": "Jetbrains Mono",
  "minimal-style@@h5-font": "Jetbrains Mono",
  "minimal-style@@h4-font": "Jetbrains Mono",
  "minimal-style@@h3-font": "Jetbrains Mono",
  "minimal-style@@h4-weight": 100,
  "minimal-style@@minimal-code-scroll": false,
  "minimal-advanced@@hide-markdown": false,
  "minimal-advanced@@hide-settings-desc": false,
  "minimal-advanced@@animations": "default",
  "minimal-style@@trim-cols": false,
  "minimal-style@@inline-title-font": "Jetbrains Mono",
  "minimal-style@@file-header-visibility": "minimal-tab-title-hover",
  "minimal-style@@blockquote-font-style": "normal",
  "minimal-style@@image-grid-fit": "cover",
  "minimal-style@@list-indent": 1.3,
  "minimal-style@@code-function@@dark": "#9E6AD3",
  "minimal-style@@code-string@@dark": "#B58900",
  "minimal-style@@code-operator@@dark": "#D33682",
  "minimal-style@@code-punctuation@@dark": "#839496",
  "minimal-style@@code-important@@dark": "#CB4B16",
  "minimal-style@@code-property@@dark": "#9E6AD3",
  "minimal-style@@code-comment@@dark": "#7A00FF",
  "minimal-style@@ax3@@dark": "#FFC700",
  "minimal-style@@color-yellow@@dark": "#A5FF00",
  "minimal-style@@color-green@@dark": "#27FF00",
  "minimal-style@@color-cyan@@dark": "#00FFEA",
  "minimal-style@@color-blue@@dark": "#006CFF",
  "minimal-style@@color-purple@@dark": "#9E6AD3",
  "minimal-style@@color-pink@@dark": "#FF00DC",
  "minimal-style@@h1-color@@dark": "#FFC700",
  "minimal-style@@h2-color@@dark": "#AA00FF",
  "minimal-style@@h6-variant": "normal",
  "minimal-style@@h5-variant": "normal",
  "minimal-style@@h4-variant": "normal",
  "minimal-style@@text-formatting@@dark": "#FFC700",
  "minimal-style@@bold-modifier": 100,
  "minimal-style@@file-header-font-weight": 100,
  "minimal-style@@inline-title-color@@dark": "#72FFF1",
  "minimal-style@@inline-title-weight": 100,
  "minimal-style@@frame-background@@dark": "#25212E",
  "minimal-style@@blockquote-color@@dark": "#EAEAEA",
  "minimal-style@@code-background@@dark": "#191A1D",
  "minimal-style@@code-normal@@dark": "#EAEAEA",
  "minimal-style@@blockquote-background-color@@dark": "#464653",
  "minimal-style@@sp1@@dark": "#EAEAEA",
  "minimal-style@@color-red@@dark": "#FF0000",
  "minimal-style@@color-orange@@dark": "#FF5700",
  "minimal-style@@h1-variant": "small-caps",
  "minimal-style@@h2-variant": "small-caps",
  "minimal-style@@h3-variant": "small-caps",
  "minimal-style@@gutter-background@@dark": "#25212E",
  "minimal-style@@line-number-color@@dark": "#8d8d93",
  "minimal-style@@checkbox-color@@dark": "#FFC700",
  "minimal-style@@h2-weight": 100,
  "minimal-style@@h1-weight": 100,
  "minimal-style@@h3-weight": 100,
  "minimal-style@@h5-weight": 100,
  "minimal-style@@h6-weight": 100,
  "id@@callout-on": true,
  "id@@h1-underline": true,
  "id@@h2-underline": true,
  "id@@headers-one-color": true,
  "minimal-style@@blockquote-border-color@@dark": "#FFC700",
  "minimal-style@@embed-max-height": "1000",
  "minimal-style@@embed-background@@dark": "#101010",
  "minimal-style@@embed-hide-title": false,
  "minimal-style@@embed-decoration-style": "dashed",
  "minimal-style@@embed-decoration-color@@dark": "#9E6AD3",
  "minimal-style@@code-size": "0.93em",
  "minimal-style@@link-external-color-hover@@dark": "#FFC700",
  "minimal-style@@link-external-color@@dark": "#828282",
  "minimal-style@@link-color@@dark": "#72FFF1",
  "minimal-style@@link-color-hover@@dark": "#7800F4",
  "minimal-style@@link-unresolved-color@@dark": "#72FFF1",
  "minimal-style@@link-unresolved-decoration-color@@dark": "#FFC700",
  "minimal-style@@blockquote-size": "22",
  "minimal-style@@blockquote-border-thickness": 2,
  "minimal-style@@max-col-width": "18em",
  "minimal-style@@h1-size": "2.5em",
  "minimal-style@@h1-style": "normal",
  "minimal-style@@h2-style": "normal",
  "minimal-style@@h2-size": "2.3em",
  "minimal-style@@h3-size": "1.6em",
  "minimal-style@@h4-size": "1.4em",
  "minimal-style@@h5-size": "1.4em",
  "minimal-style@@h6-size": "1.4em",
  "minimal-style@@list-spacing": 0.015,
  "minimal-style@@metadata-label-width-multiplier": 11,
  "minimal-style@@vault-profile-display": "vault-profile-default",
  "minimal-style@@minimal-unstyled-tags": false,
  "minimal-style@@tag-border-width": "1px",
  "minimal-style@@link-unresolved-opacity": 0.4,
  "minimal-style@@file-header-font-size": "1.25em",
  "minimal-style@@inline-title-size": "1.6em",
  "minimal-style@@bg1@@dark": "#1F2023",
  "minimal-cards-style@@cards-min-width": "200x",
  "minimal-advanced@@cursor": "default",
  "checkbox@@check-color": true,
  "checkbox@@check-bg": false,
  "checkbox@@check-text": false,
  "checkbox@@check-strike": false,
  "minimal-style@@tabs-style": "tabs-modern",
  "minimal-style@@hl2@@dark": "#CCB20047",
  "minimal-style@@hl1@@dark": "#5E00FF47",
  "minimal-style@@p-spacing": "1.3.7rem",
  "minimal-style@@title-color@@dark": "#5400FF",
  "minimal-style@@title-color-inactive@@dark": "#7E00FF",
  "minimal-style@@window-title-off": true,
  "minimal-style@@frame-icon-color@@dark": "#7E00FF",
  "minimal-style@@titlebar-text-color-focused@@dark": "#FFD400",
  "minimal-style@@titlebar-text-color@@dark": "#6900FF",
  "minimal-style@@titlebar-text-weight": 200,
  "minimal-style@@italic-color@@dark": "#D1A1FF",
  "minimal-advanced@@font-ui-small": 16,
  "minimal-advanced@@font-ui-smaller": 16,
  "minimal-style@@bases-table-row-height": 40
}
```

### Deep Gunmetal Background
```
{
  "minimal-style@@bg2@@dark": "#23272E",
  "minimal-style@@bg3@@dark": "#2C313A",
  "minimal-style@@ui2@@dark": "#7800F4",
  "minimal-style@@ax1@@dark": "#FFC700",
  "minimal-style@@ax2@@dark": "#FFE066",
  "minimal-theme@@color-accent-light": "#BE93FD",
  "minimal-theme@@color-accent-dark": "#BE93FD",
  "minimal-theme@@color-bg-primary-light": "#fcfcfc",
  "minimal-theme@@color-bg-secondary-light": "#f2f2f7",
  "minimal-theme@@color-bg-primary-dark": "#1c1c1e",
  "minimal-theme@@color-bg-secondary-dark": "#2c2c2e",
  "minimal-theme@@color-text-primary-light": "#1c1c1e",
  "minimal-theme@@color-text-primary-dark": "#f2f2f7",
  "minimal-theme@@color-text-normal-light": "#1c1c1e",
  "minimal-theme@@color-text-normal-dark": "#f2f2f7",
  "minimal-theme@@color-text-secondary-light": "#6e6e73",
  "minimal-theme@@color-text-secondary-dark": "#8d8d93",
  "minimal-theme@@color-text-faint-light": "#999999",
  "minimal-theme@@color-text-faint-dark": "#777777",
  "minimal-theme@@color-interactive-accent-light": "#BE93FD",
  "minimal-theme@@color-interactive-accent-dark": "#BE93FD",
  "minimal-theme@@link-unresolved-color-light": "#a8a8a8",
  "minimal-theme@@link-unresolved-color-dark": "#7a7a7a",
  "minimal-theme@@code-background-light": "#f2f2f7",
  "minimal-theme@@code-background-dark": "#2c2c2e",
  "minimal-style@@file-header-justify": "center",
  "minimal-style@@tag-color@@dark": "#FFC700",
  "minimal-style@@tag-background@@dark": "#212324",
  "minimal-style@@tag-background-hover@@dark": "#282838",
  "minimal-style@@tag-radius": "14px",
  "minimal-style@@minimal-tab-text-color@@dark": "#FFC700",
  "minimal-style@@minimal-tab-text-color-active@@dark": "#EAEAEA",
  "minimal-style@@row-lines": true,
  "minimal-style@@col-lines": true,
  "minimal-style@@table-lines": false,
  "minimal-style@@row-alt": true,
  "minimal-style@@col-alt": true,
  "minimal-style@@table-tabular": false,
  "minimal-style@@table-numbers": false,
  "minimal-style@@table-center": true,
  "minimal-style@@table-nowrap": false,
  "minimal-style@@row-hover": true,
  "minimal-style@@table-row-background-hover@@dark": "#4F00FF47",
  "minimal-style@@maximize-tables-off": "maximize-tables",
  "minimal-style@@ribbon-style": "ribbon-bottom-left-hover",
  "minimal-style@@sidebar-tabs-style": "sidebar-tabs-wide",
  "minimal-style@@hide-help": false,
  "minimal-style@@hide-settings": false,
  "minimal-style@@sidebar-tabs-names": "tab-names-single",
  "minimal-style@@metadata-heading-off": true,
  "minimal-style@@metadata-add-property-off": true,
  "minimal-style@@metadata-icons-off": false,
  "minimal-style@@metadata-dividers": true,
  "minimal-style@@progress-complete@@dark": "#BE93FD",
  "minimal-style@@pdf-page-style": "pdf-shadows-on",
  "minimal-style@@pdf-invert-dark": false,
  "minimal-style@@checkbox-shape": "checkbox-square",
  "minimal-style@@minimal-strike-lists": true,
  "minimal-style@@active-line-on": true,
  "minimal-style@@workspace-background-translucent@@dark": "#7800F420",
  "minimal-style@@indentation-guide-color-active@@dark": "#FFC700",
  "minimal-style@@indentation-guide-color@@dark": "#FFC700",
  "minimal-style@@icon-color@@dark": "#72FFF1",
  "minimal-style@@icon-color-hover@@dark": "#FFD84D",
  "minimal-style@@icon-color-focused@@dark": "#FFD84D",
  "minimal-style@@embed-strict": false,
  "minimal-style@@embed-underline": false,
  "minimal-style@@dataview-inline-lists": true,
  "minimal-style@@callouts-style": "callouts-outlined",
  "minimal-style@@h1-l": true,
  "minimal-style@@h2-l": false,
  "minimal-style@@h3-l": true,
  "minimal-style@@h4-l": false,
  "minimal-style@@h5-l": false,
  "minimal-style@@h6-l": false,
  "minimal-style@@bold-color@@dark": "#9E3EFF",
  "minimal-style@@tx2@@dark": "#EAEAEA",
  "minimal-style@@tx3@@dark": "#EAEAEA",
  "minimal-style@@tx1@@dark": "#EAEAEA",
  "minimal-style@@h1-font": "Jetbrains Mono",
  "minimal-style@@h2-font": "Jetbrains Mono",
  "minimal-style@@h3-color@@dark": "#FFECA6",
  "minimal-style@@h4-color@@dark": "#CDCDCD",
  "minimal-style@@h5-color@@dark": "#B5B5B5",
  "minimal-style@@h6-color@@dark": "#595959",
  "minimal-style@@h6-font": "Jetbrains Mono",
  "minimal-style@@h5-font": "Jetbrains Mono",
  "minimal-style@@h4-font": "Jetbrains Mono",
  "minimal-style@@h3-font": "Jetbrains Mono",
  "minimal-style@@h4-weight": 100,
  "minimal-style@@minimal-code-scroll": false,
  "minimal-advanced@@hide-markdown": false,
  "minimal-advanced@@hide-settings-desc": false,
  "minimal-advanced@@animations": "default",
  "minimal-style@@trim-cols": false,
  "minimal-style@@inline-title-font": "Jetbrains Mono",
  "minimal-style@@file-header-visibility": "minimal-tab-title-hover",
  "minimal-style@@blockquote-font-style": "normal",
  "minimal-style@@image-grid-fit": "cover",
  "minimal-style@@list-indent": 1.3,
  "minimal-style@@code-function@@dark": "#9E6AD3",
  "minimal-style@@code-string@@dark": "#B58900",
  "minimal-style@@code-operator@@dark": "#D33682",
  "minimal-style@@code-punctuation@@dark": "#839496",
  "minimal-style@@code-important@@dark": "#CB4B16",
  "minimal-style@@code-property@@dark": "#9E6AD3",
  "minimal-style@@code-comment@@dark": "#7A00FF",
  "minimal-style@@ax3@@dark": "#FFC700",
  "minimal-style@@color-yellow@@dark": "#A5FF00",
  "minimal-style@@color-green@@dark": "#27FF00",
  "minimal-style@@color-cyan@@dark": "#00FFEA",
  "minimal-style@@color-blue@@dark": "#006CFF",
  "minimal-style@@color-purple@@dark": "#9E6AD3",
  "minimal-style@@color-pink@@dark": "#FF00DC",
  "minimal-style@@h1-color@@dark": "#FFC700",
  "minimal-style@@h2-color@@dark": "#AA00FF",
  "minimal-style@@h6-variant": "normal",
  "minimal-style@@h5-variant": "normal",
  "minimal-style@@h4-variant": "normal",
  "minimal-style@@text-formatting@@dark": "#FFC700",
  "minimal-style@@bold-modifier": 100,
  "minimal-style@@file-header-font-weight": 100,
  "minimal-style@@inline-title-color@@dark": "#72FFF1",
  "minimal-style@@inline-title-weight": 100,
  "minimal-style@@frame-background@@dark": "#25212E",
  "minimal-style@@blockquote-color@@dark": "#EAEAEA",
  "minimal-style@@code-background@@dark": "#181B1F",
  "minimal-style@@code-normal@@dark": "#EAEAEA",
  "minimal-style@@blockquote-background-color@@dark": "#464653",
  "minimal-style@@sp1@@dark": "#EAEAEA",
  "minimal-style@@color-red@@dark": "#FF0000",
  "minimal-style@@color-orange@@dark": "#FF5700",
  "minimal-style@@h1-variant": "small-caps",
  "minimal-style@@h2-variant": "small-caps",
  "minimal-style@@h3-variant": "small-caps",
  "minimal-style@@gutter-background@@dark": "#25212E",
  "minimal-style@@line-number-color@@dark": "#8d8d93",
  "minimal-style@@checkbox-color@@dark": "#FFC700",
  "minimal-style@@h2-weight": 100,
  "minimal-style@@h1-weight": 100,
  "minimal-style@@h3-weight": 100,
  "minimal-style@@h5-weight": 100,
  "minimal-style@@h6-weight": 100,
  "id@@callout-on": true,
  "id@@h1-underline": true,
  "id@@h2-underline": true,
  "id@@headers-one-color": true,
  "minimal-style@@blockquote-border-color@@dark": "#FFC700",
  "minimal-style@@embed-max-height": "1000",
  "minimal-style@@embed-background@@dark": "#101010",
  "minimal-style@@embed-hide-title": false,
  "minimal-style@@embed-decoration-style": "dashed",
  "minimal-style@@embed-decoration-color@@dark": "#9E6AD3",
  "minimal-style@@code-size": "0.93em",
  "minimal-style@@link-external-color-hover@@dark": "#FFC700",
  "minimal-style@@link-external-color@@dark": "#828282",
  "minimal-style@@link-color@@dark": "#72FFF1",
  "minimal-style@@link-color-hover@@dark": "#7800F4",
  "minimal-style@@link-unresolved-color@@dark": "#72FFF1",
  "minimal-style@@link-unresolved-decoration-color@@dark": "#FFC700",
  "minimal-style@@blockquote-size": "22",
  "minimal-style@@blockquote-border-thickness": 2,
  "minimal-style@@max-col-width": "18em",
  "minimal-style@@h1-size": "2.5em",
  "minimal-style@@h1-style": "normal",
  "minimal-style@@h2-style": "normal",
  "minimal-style@@h2-size": "2.3em",
  "minimal-style@@h3-size": "1.6em",
  "minimal-style@@h4-size": "1.4em",
  "minimal-style@@h5-size": "1.4em",
  "minimal-style@@h6-size": "1.4em",
  "minimal-style@@list-spacing": 0.015,
  "minimal-style@@metadata-label-width-multiplier": 11,
  "minimal-style@@vault-profile-display": "vault-profile-default",
  "minimal-style@@minimal-unstyled-tags": false,
  "minimal-style@@tag-border-width": "1px",
  "minimal-style@@link-unresolved-opacity": 0.4,
  "minimal-style@@file-header-font-size": "1.25em",
  "minimal-style@@inline-title-size": "1.6em",
  "minimal-style@@bg1@@dark": "#1E2227",
  "minimal-cards-style@@cards-min-width": "200x",
  "minimal-advanced@@cursor": "default",
  "checkbox@@check-color": true,
  "checkbox@@check-bg": false,
  "checkbox@@check-text": false,
  "checkbox@@check-strike": false,
  "minimal-style@@tabs-style": "tabs-modern",
  "minimal-style@@hl2@@dark": "#CCB20047",
  "minimal-style@@hl1@@dark": "#5E00FF47",
  "minimal-style@@p-spacing": "1.3.7rem",
  "minimal-style@@title-color@@dark": "#5400FF",
  "minimal-style@@title-color-inactive@@dark": "#7E00FF",
  "minimal-style@@window-title-off": true,
  "minimal-style@@frame-icon-color@@dark": "#7E00FF",
  "minimal-style@@titlebar-text-color-focused@@dark": "#FFD400",
  "minimal-style@@titlebar-text-color@@dark": "#6900FF",
  "minimal-style@@titlebar-text-weight": 200,
  "minimal-style@@italic-color@@dark": "#D1A1FF",
  "minimal-advanced@@font-ui-small": 16,
  "minimal-advanced@@font-ui-smaller": 16,
  "minimal-style@@bases-table-row-height": 40
}
```

### Option 1: "Bio-Digital" (Tech Green)

*The Matrix / Fallout Terminal Vibe.*
This is a very dark, desaturated grey-green. It feels utilitarian and "hacker-ish." It pairs excellently with your **Gold** accents (giving a military circuit-board feel).

  * **Primary Background (`bg1`):** `#161916` (Almost black, distinct green undertone)
  * **Secondary Background (`bg2`):** `#1E241E` (Dark Camo Green)
  * **Tertiary Background (`bg3`):** `#283028`
  * **Code Background:** `#111411`

<!-- end list -->

```json
{
  "minimal-style@@bg1@@dark": "#161916",
  "minimal-style@@bg2@@dark": "#1E241E",
  "minimal-style@@bg3@@dark": "#283028",
  "minimal-style@@frame-background@@dark": "#1E241E",
  "minimal-style@@code-background@@dark": "#111411",
  "minimal-style@@gutter-background@@dark": "#1E241E"
}
```

### Option 2: "Deep Sage" (Natural Green)

*Organic and Calm.*
This is a softer, earthier green. It is less "tech" and more "library." It is lighter than the option above and feels very comfortable for reading. Your **Purple** accents will stand out sharply here because they are roughly opposite on the color wheel.

  * **Primary Background (`bg1`):** `#1A1D1A` (Soft Dark Moss)
  * **Secondary Background (`bg2`):** `#212621` (Lighter Sage)
  * **Tertiary Background (`bg3`):** `#2D332D`
  * **Code Background:** `#141714`

<!-- end list -->

```json
{
  "minimal-style@@bg1@@dark": "#1A1D1A",
  "minimal-style@@bg2@@dark": "#212621",
  "minimal-style@@bg3@@dark": "#2D332D",
  "minimal-style@@frame-background@@dark": "#212621",
  "minimal-style@@code-background@@dark": "#141714",
  "minimal-style@@gutter-background@@dark": "#212621"
}
```

### Option 3: "Solarized Command" (The Solar Theme)

*The Classic.*
This is based on the famous **Solarized Dark** palette (specifically the background values). It is not black or grey—it is a very specific, rich **Deep Petrol / Cyan-Blue**.

  * **Note:** Because your icons are currently **Teal (`#72FFF1`)**, they might blend in slightly with this background. You might need to change your icon color to White or Gold if you use this one.

  * **Primary Background (`bg1`):** `#002B36` (The classic Solarized Base03)

  * **Secondary Background (`bg2`):** `#073642` (Solarized Base02 - Sidebar)

  * **Tertiary Background (`bg3`):** `#0F404D` (Calculated lighter step)

  * **Code Background:** `#00212B`

<!-- end list -->

```json
{
  "minimal-style@@bg1@@dark": "#002B36",
  "minimal-style@@bg2@@dark": "#073642",
  "minimal-style@@bg3@@dark": "#0F404D",
  "minimal-style@@frame-background@@dark": "#073642",
  "minimal-style@@code-background@@dark": "#00212B",
  "minimal-style@@gutter-background@@dark": "#073642"
}
```

**Next Step:** If you choose **Solarized Command**, your **Teal Icons** (`#72FFF1`) will likely vanish into the background color. Would you like a JSON snippet to swap your icons to **Gold** or **White** so they pop against the Solarized background?