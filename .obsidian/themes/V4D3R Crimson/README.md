# V4D3R Crimson Theme

A production-ready dark theme for Obsidian featuring a striking **Red, Black, and Grey** color palette.

## 🎨 Color Palette

- **Primary Accent**: Crimson Red (#DC143C)
- **Highlights**: Salmon Red (#FF6B6B)  
- **Borders**: Dark Red (#8B0000)
- **Background**: Near Black (#1A1A1A)
- **Text**: Light Silver (#C0C0C0)
- **UI Elements**: 8-shade grey system

## ✨ Features

- ✅ **WCAG 2.1 AA Compliant** - All text meets accessibility standards
- ✅ **Red/Black/Grey Palette** - Consistent color system throughout
- ✅ **JetBrains Mono Font** - Monospace typography (Light weight: 300)
- ✅ **Custom File Explorer** - Color-coded folders with emoji icons
- ✅ **Comprehensive Callout System** - 20+ callout types
- ✅ **Enhanced Code Blocks** - Syntax highlighting + language badges
- ✅ **Styled Tables** - Professional data presentation
- ✅ **Mobile Optimized** - Touch-friendly interface
- ✅ **Reduced Motion Support** - Accessibility-first design

## 📦 Installation

### Method 1: Manual Installation

1. Download `theme.css` and `manifest.json`
2. Create folder: `YourVault/.obsidian/themes/v4d3r-crimson/`
3. Place both files in that folder
4. Open Obsidian → Settings → Appearance → Themes
5. Select "V4D3R Crimson" from dropdown

### Method 2: Direct CSS

1. Copy contents of `theme.css`
2. Settings → Appearance → CSS Snippets → Open snippets folder
3. Create `v4d3r-crimson.css` and paste contents
4. Enable snippet in Obsidian

## 🎯 Recommended Settings

For optimal appearance:

1. **Font**: Install [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
2. **Font Weight**: Theme uses 300 (Light) - very readable
3. **Base Font Size**: 16px (adjustable in theme variables)

## 🛠️ Customization

### Change Global Font Weight

Edit line ~65 in `theme.css`:

```css
--v4d3r-base-font-weight: var(--font-weight-thin); /* 100 */

/* Options: */
/* var(--font-weight-thin) = 100 (ultra-light, recommended) */
/* var(--font-weight-light) = 300 (light) */
/* var(--font-weight-normal) = 400 (normal) */
```

### Adjust Colors

All colors defined as CSS variables at top of `theme.css`. Example:

```css
--v4d3r-red-primary: #DC143C; /* Change to your preferred red */
```

### File Explorer Icons

Customize folder icons by editing Part 6 in `theme.css`:

```css
.nav-folder-title[data-path="YOUR-FOLDER"]::before {
  content: "🎯 "; /* Change emoji */
}
```

## 📋 Components Included

- ✅ Workspace & Canvas
- ✅ Ribbon & Sidebars  
- ✅ File Explorer (with custom folder styling)
- ✅ Tabs & Tab Bar
- ✅ Status Bar & Titlebar
- ✅ Modals & Popovers
- ✅ Buttons & Forms
- ✅ Scrollbars
- ✅ Search Interface
- ✅ Callouts (20+ types)
- ✅ Code Blocks & Inline Code
- ✅ Links (internal & external)
- ✅ Lists & Checkboxes
- ✅ Headings (H1-H6)
- ✅ Tables
- ✅ Horizontal Rules
- ✅ Tags
- ✅ Blockquotes
- ✅ Metadata/Properties Panel
- ✅ Graph View

## 🎨 Callout Types Supported

**Default**: note, info, tip, hint, success, question, warning, caution, failure, danger, error, bug, example, quote, abstract

**Custom**: important, key-claim, definition, evidence, research, methodology-and-sources, what-this-does

## ♿ Accessibility

- **WCAG 2.1 AA**: All color combinations validated
- **Reduced Motion**: Respects `prefers-reduced-motion`
- **High Contrast**: Supports `prefers-contrast: high`
- **Mobile**: 44px minimum touch targets
- **Keyboard Navigation**: Full keyboard support

## 🐛 Troubleshooting

**Fonts not working?**
- Install JetBrains Mono system-wide
- Restart Obsidian after font installation

**Colors look wrong?**
- Ensure no other themes/snippets are active
- Check that you're using dark mode

**File explorer icons missing?**
- Icons use folder `data-path` attribute
- Rename your folders to match or edit theme

## 📝 Version

**Current**: v1.0.0  
**Obsidian**: Requires 1.5.0+

## 👤 Author

**Pur3v4d3r**

## 📄 License

Free to use and modify for personal use.

---

**Enjoy your new Crimson theme! 🔴⚫**