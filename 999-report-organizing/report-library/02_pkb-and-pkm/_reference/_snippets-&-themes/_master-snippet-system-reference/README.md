# Pur3v4d3r's Obsidian CSS Snippet Collection

> **A comprehensive, professional CSS theming system for Obsidian**
> Cyberpunk-inspired aesthetics with gold, purple, and cyan accents

[![Obsidian](https://img.shields.io/badge/Obsidian-1.5+-7c3aed?style=flat&logo=obsidian)](https://obsidian.md)
[![License](https://img.shields.io/badge/License-MIT-ffc700?style=flat)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Pur3v4d3r-00ffd2?style=flat)](https://github.com/pur3v4d3r)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Snippet Categories](#snippet-categories)
- [Color Palette](#color-palette)
- [Customization](#customization)
- [Compatibility](#compatibility)
- [Credits](#credits)

---

## 🎨 Overview

This collection provides a complete theming system for Obsidian, featuring:

- **Cyberpunk aesthetics** with gradient effects and animations
- **Consistent color scheme** across all UI elements
- **Modular design** - use snippets individually or together
- **Extensive customization** through CSS variables
- **Performance optimized** with hardware-accelerated effects

### Design Philosophy

- **Visual hierarchy** through strategic use of color and animation
- **Readability first** - all effects enhance, never distract
- **Dark mode optimized** with light mode support
- **Professional appearance** suitable for work and personal use

---

## ✨ Features

### Typography & Text
- 🎭 Animated gradient headings (H1-H6)
- 📝 Customizable markdown syntax highlighting
- ✍️ Enhanced inline code blocks with glow effects
- 🔗 Animated link hover effects

### UI Components
- 🎨 Custom scrollbars with gradient effects
- 📦 Styled modals and command palette
- 🏷️ Enhanced tags and metadata
- 📊 Gradient table headers and dataview integration

### Interactive Elements
- ⚡ Active line highlighting with gradient underline
- 🖱️ Hover animations on links and buttons
- 🎯 Command palette with translucent backdrop
- 🔄 Smooth transitions throughout

### Layout & Structure
- 📐 Optimized reading width (90ch)
- 🎪 Canvas view styling
- 📄 Mermaid diagram resizing
- 🖼️ Embed and blockquote enhancements

---

## 📦 Installation

### Method 1: Quick Install (Recommended)

1. Download this repository
2. Copy all `.css` files from the `snippets/` folder to your vault's `.obsidian/snippets/` directory
3. Open Obsidian Settings → Appearance → CSS Snippets
4. Enable the snippets you want to use

### Method 2: Manual Installation

1. Navigate to your vault's `.obsidian/snippets/` folder (create if it doesn't exist)
2. Copy individual snippet files from this collection
3. Reload Obsidian or enable snippets in Settings

### Directory Structure

```
your-vault/
└── .obsidian/
    └── snippets/
        ├── 01-variables.css           # Core color variables
        ├── 02-typography.css          # Headings and text
        ├── 03-links.css               # Link styling
        ├── 04-syntax-highlighting.css # Markdown syntax
        ├── 05-inline-elements.css     # Code blocks, tags
        ├── 06-animations.css          # Gradient effects
        ├── 07-ui-components.css       # Modals, command palette
        ├── 08-layout.css              # Core layout
        ├── 09-dataview.css            # Dataview plugin
        └── 10-mermaid.css             # Mermaid diagrams
```

---

## 🗂️ Snippet Categories

### 1. Variables & Foundation (`01-variables.css`)
**Core CSS variables for the entire theme**

- Background colors (dark/light mode)
- Accent colors (gold, purple, cyan)
- Text colors with hierarchy
- Code syntax colors
- UI element colors

**Dependencies:** None
**Required:** Yes (for other snippets to work)

---

### 2. Typography (`02-typography.css`)
**Complete heading and text styling system**

- H1-H6 heading styles with JetBrains Mono font
- All-small-caps variant styling
- Inline title customization
- Paragraph spacing optimization
- Bold and italic gradient effects

**Dependencies:** 01-variables.css
**Standalone:** Partial

---

### 3. Links (`03-links.css`)
**Advanced link styling with animations**

Features:
- Internal links: Cyan-to-purple gradient underline
- External links: Gold-to-orange gradient underline
- Unresolved links: Dotted purple underline
- Animated gradient expansion on hover
- Pseudo-link hover effects

**Dependencies:** 01-variables.css
**Standalone:** Yes

---

### 4. Syntax Highlighting (`04-syntax-highlighting.css`)
**Markdown syntax character customization**

Highlights:
- Gold brackets `[[ ]]` and link formatting
- Silver link text
- Purple bold markers `**`
- Teal italic markers `*`
- Animated glow effects on hover

**Dependencies:** 01-variables.css
**Standalone:** Yes

---

### 5. Inline Elements (`05-inline-elements.css`)
**Inline code blocks and special formatting**

Features:
- Custom inline code styling with glow
- Click-to-select behavior
- JetBrains Mono font integration
- Transparent purple background
- Cyan border with gold shadow

**Dependencies:** 01-variables.css
**Standalone:** Yes

---

### 6. Animations (`06-animations.css`)
**Gradient effects and keyframe animations**

Includes:
- H1 gradient shimmer animation
- Scrolling underline effects
- Pulse glow animations
- Active line gradient underline
- HR gradient dividers

**Dependencies:** 01-variables.css, 02-typography.css
**Standalone:** Partial

**⚠️ Performance Note:** May impact performance on older devices

---

### 7. UI Components (`07-ui-components.css`)
**Modal dialogs, command palette, and menus**

Styling for:
- Translucent modal backgrounds
- Command palette with backdrop blur
- Suggestion highlighting
- Hotkey indicators
- Menu gradients

**Dependencies:** 01-variables.css
**Standalone:** Yes

---

### 8. Layout (`08-layout.css`)
**Core layout and workspace styling**

Components:
- Sidebar styling
- Tab system (modern rounded tabs)
- Ribbon positioning
- Scrollbar customization
- Titlebar and window controls
- Canvas view

**Dependencies:** 01-variables.css
**Standalone:** Partial

---

### 9. Dataview (`09-dataview.css`)
**Dataview plugin integration**

Features:
- Gradient table headers
- Enhanced row hover effects
- Inline field styling
- List formatting

**Dependencies:** 01-variables.css, Dataview plugin
**Standalone:** Yes (requires plugin)

---

### 10. Mermaid Diagrams (`10-mermaid.css`)
**Resizable and scrollable Mermaid diagrams**

Capabilities:
- Drag-to-resize functionality
- Automatic scrolling for large diagrams
- Centered layout
- Hover effects

**Dependencies:** None
**Standalone:** Yes

---

## 🎨 Color Palette

### Primary Colors

| Color Name        | Hex Code  | Usage                          | Variable Name           |
|-------------------|-----------|--------------------------------|-------------------------|
| Imperial Gold     | `#FFC700` | Primary accent, icons, links   | `--ax1`                 |
| Deep Amethyst     | `#7200FF` | Secondary accent, gradients    | `--ui2`, `--ui3`        |
| Cyber Cyan        | `#00FFD2` | Tertiary accent, highlights    | N/A                     |
| Neon Magenta      | `#FF0075` | Warning states, emphasis       | N/A                     |
| Terminal Green    | `#CBFF00` | Success states                 | N/A                     |
| Reactor Orange    | `#FF6E00` | External links, alerts         | N/A                     |

### Background Colors (Dark Mode)

| Element           | Hex Code  | Variable Name            |
|-------------------|-----------|--------------------------|
| Primary BG        | `#1C1C1F` | `--background-primary`   |
| Secondary BG      | `#2C2C2E` | `--background-secondary` |
| Code BG           | `#18151D` | `--code-background`      |
| Embed BG          | `#101010` | `--embed-background`     |

### Text Colors

| Type              | Hex Code  | Variable Name   |
|-------------------|-----------|-----------------|
| Normal Text       | `#F2F2F7` | `--text-normal` |
| Muted Text        | `#8D8D93` | `--text-muted`  |
| Faint Text        | `#777777` | `--text-faint`  |

### Gradient Combinations

**Professional Gradients:**
- H1: Gold → Amethyst (`#D8BE34` → `#7200FF`)
- H2: Cyan → Amethyst (`#00FFD2` → `#7200FF`)
- Links: Cyan → Amethyst (internal), Gold → Orange (external)

**Effect Gradients:**
- Scrollbar: Gold → Purple vertical
- Active Line: Gold fade (transparent → gold → transparent)
- HR: Transparent → Purple → Cyan → Purple → Transparent

---

## ⚙️ Customization

### Quick Color Changes

Edit `01-variables.css` to change the entire theme:

```css
.theme-dark {
  /* Change primary accent color */
  --ax1: #YOUR_COLOR !important;

  /* Change secondary accent */
  --ui2: #YOUR_COLOR !important;

  /* Change link colors */
  --link-color: #YOUR_COLOR !important;
}
```

### Enable/Disable Gradient Effects

Many gradient effects are commented out by default. To enable:

1. Open `06-animations.css`
2. Find the desired effect (marked with `OPTION X`)
3. Remove `/*` and `*/` comment markers
4. Save and reload

### Font Customization

To change the monospace font from JetBrains Mono:

1. Open `02-typography.css`
2. Find all instances of `"Jetbrains Mono"`
3. Replace with your preferred font
4. Ensure the font is installed on your system

### Adjust Animation Speed

Modify animation duration in `06-animations.css`:

```css
animation: gradient-shift 6s ease infinite !important;
                         /* ↑ Change this value */
```

---

## 🔧 Compatibility

### Obsidian Version
- **Minimum:** Obsidian 1.5.0
- **Recommended:** Latest version
- **Tested on:** 1.5.x, 1.6.x

### Plugins
**Fully Compatible:**
- Dataview
- Calendar
- Kanban
- Minimal Theme Settings (use snippets instead for more control)

**Partial Compatibility:**
- Custom themes may override these snippets
- Disable conflicting theme settings for best results

### Operating Systems
- ✅ Windows 10/11
- ✅ macOS (Monterey+)
- ✅ Linux (Ubuntu, Arch)
- ⚠️ Mobile (limited animation support)

---

## 📝 Usage Tips

### Best Practices

1. **Start with variables** - Enable `01-variables.css` first
2. **Add incrementally** - Enable one snippet at a time to test
3. **Check performance** - Disable animations on slower devices
4. **Backup your vault** - Before making extensive changes
5. **Use DevTools** - Press `Ctrl+Shift+I` to inspect elements

### Performance Optimization

If experiencing lag:

1. Disable `06-animations.css`
2. Remove gradient effects from headings
3. Simplify scrollbar styling
4. Reduce backdrop-filter blur values

### Troubleshooting

**Snippets not applying?**
- Ensure they're enabled in Settings → Appearance → CSS Snippets
- Check for syntax errors (missing `}` or `;`)
- Reload Obsidian (`Ctrl+R`)

**Colors look wrong?**
- Verify you're in Dark Mode
- Check if another theme is active
- Ensure `01-variables.css` is enabled

**Gradients not showing?**
- Some are commented out by default
- Uncomment desired effects in `06-animations.css`
- Clear cache and reload

---

## 🎯 Recommended Combinations

### Minimal Setup (Best Performance)
```
01-variables.css
02-typography.css
03-links.css
```

### Complete Professional Theme
```
01-variables.css
02-typography.css
03-links.css
04-syntax-highlighting.css
05-inline-elements.css
07-ui-components.css
08-layout.css
```

### Full Experience (All Features)
```
All snippets enabled
```

---

## 📚 Additional Resources

### Color Theory Reference
- [Adobe Color Wheel](https://color.adobe.com/)
- [Coolors.co](https://coolors.co/) - Palette generator
- [CSS Gradient Generator](https://cssgradient.io/)

### CSS Learning Resources
- [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [CSS-Tricks](https://css-tricks.com/)
- [Obsidian CSS Documentation](https://docs.obsidian.md/Reference/CSS+variables)

### Font Resources
- [JetBrains Mono](https://www.jetbrains.com/lp/mono/) - Featured monospace font
- [Google Fonts](https://fonts.google.com/)

---

## 🤝 Contributing

Found a bug? Have a suggestion?

1. Check existing issues
2. Create a detailed bug report or feature request
3. Include your Obsidian version and OS
4. Provide screenshots if applicable

---

## 📜 License

MIT License - Feel free to modify and distribute

---

## 👤 Credits

**Author:** Pur3v4d3r
**Created:** 2025-12-13
**Version:** 1.0.0

**Inspired by:**
- Cyberpunk aesthetics
- Minimal Theme by @kepano
- Obsidian community CSS snippets

---

## 🌟 Changelog

### Version 1.0.0 (2025-12-13)
- Initial release
- 10 modular CSS snippets
- Complete documentation
- Color palette reference
- Installation guide

---

**Enjoy your enhanced Obsidian experience! 🎨✨**

> If you find this useful, consider sharing it with the Obsidian community!
