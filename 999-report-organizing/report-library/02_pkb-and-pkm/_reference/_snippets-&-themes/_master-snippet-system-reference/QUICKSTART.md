# Quick Start Guide

> **Get up and running with Pur3v4d3r's CSS Snippets in 5 minutes**

---

## ⚡ Installation (2 minutes)

### Step 1: Locate Your Snippets Folder

1. Open Obsidian
2. Go to `Settings` → `Appearance`
3. Scroll down to "CSS snippets"
4. Click the folder icon 📁 next to "CSS snippets"
   - This opens your `.obsidian/snippets/` folder

### Step 2: Copy Snippet Files

1. Download or copy all `.css` files from the `snippets/` folder in this package
2. Paste them into your `.obsidian/snippets/` folder

**You should have these files:**
```
.obsidian/snippets/
├── 01-variables.css
├── 02-typography.css
├── 03-links.css
├── 04-syntax-highlighting.css
├── 05-inline-elements.css
├── 06-animations.css
├── 07-ui-components.css
├── 08-layout.css
├── 09-dataview.css
└── 10-mermaid.css
```

### Step 3: Enable Snippets

1. Return to Obsidian Settings → Appearance → CSS Snippets
2. Click the **reload icon** 🔄 to refresh the list
3. Enable snippets by clicking the toggle switches

---

## 🎯 Recommended Setup

### For Beginners: Essential 3-Snippet Setup

**Enable these first:**
1. ✅ `01-variables.css` - **Required** (colors and variables)
2. ✅ `02-typography.css` - Beautiful headings
3. ✅ `03-links.css` - Animated link effects

**Result:** Professional appearance with minimal performance impact

### For Intermediate Users: Full Professional Theme

**Enable all except animations:**
1. ✅ `01-variables.css`
2. ✅ `02-typography.css`
3. ✅ `03-links.css`
4. ✅ `04-syntax-highlighting.css`
5. ✅ `05-inline-elements.css`
6. ❌ `06-animations.css` (skip for better performance)
7. ✅ `07-ui-components.css`
8. ✅ `08-layout.css`
9. ✅ `09-dataview.css` (if you use Dataview plugin)
10. ✅ `10-mermaid.css` (if you use Mermaid diagrams)

**Result:** Complete professional theme with excellent performance

### For Advanced Users: Full Experience

**Enable everything:**
1-10: ✅ All snippets enabled

**Optional:** Uncomment gradient effects in `06-animations.css`

**Result:** Maximum visual impact (may affect performance on older devices)

---

## 🎨 First Customization (1 minute)

### Change Your Primary Accent Color

1. Open `01-variables.css` in a text editor
2. Find this line (around line 52):
   ```css
   --ax1: #FFC700 !important;  /* Imperial Gold - Primary */
   ```
3. Replace `#FFC700` with your preferred color
4. Save the file
5. Reload Obsidian (Ctrl+R / Cmd+R)

**Popular alternatives:**
- Electric Blue: `#00B8FF`
- Hot Pink: `#FF1493`
- Lime Green: `#00FF00`
- Orange: `#FF7700`

---

## ✨ Enable Optional Effects

### Activate H1 Gradient Animation

The animated H1 shimmer is **already active** by default! Just enable `06-animations.css`.

### Activate Additional Gradients

1. Open `06-animations.css` in a text editor
2. Find the effect you want (e.g., "OPTION 1: SUBTLE GRADIENT HEADINGS")
3. Remove the `/*` at the start and `*/` at the end
4. Save and reload Obsidian

**Example:**

**Before (disabled):**
```css
/*
.theme-dark .markdown-preview-view h2 {
  background: linear-gradient(...);
}
*/
```

**After (enabled):**
```css
.theme-dark .markdown-preview-view h2 {
  background: linear-gradient(...);
}
```

---

## 🔧 Troubleshooting

### Snippets Not Showing Up?

1. **Refresh the list:** Click reload 🔄 in Settings → Appearance → CSS Snippets
2. **Check file extension:** Files must end in `.css` (not `.txt` or `.css.txt`)
3. **Check location:** Files must be in `.obsidian/snippets/` folder
4. **Reload Obsidian:** Press `Ctrl+R` (Windows/Linux) or `Cmd+R` (Mac)

### Colors Look Wrong?

1. **Enable Dark Mode:** Settings → Appearance → Base color scheme → Dark
2. **Enable 01-variables.css:** This snippet is required for colors to work
3. **Disable conflicting themes:** Settings → Appearance → Themes → Select "Default"

### Gradients Not Showing?

1. **Check if commented out:** Most gradients in `06-animations.css` are disabled by default
2. **Uncomment desired effects:** Remove `/*` and `*/` around the CSS rules
3. **Clear cache:** Close and reopen Obsidian

### Performance Issues?

1. **Disable 06-animations.css:** Animations can impact older devices
2. **Keep gradients commented out:** Only enable what you need
3. **Reduce backdrop blur:** In `07-ui-components.css`, change `blur(30px)` to `blur(10px)`

---

## 📖 Next Steps

### Learn More

- **Full Documentation:** See [README.md](04-library/02-pkb-and-pkm-learning/-reference/_snippets-&-themes/_master-snippet-system-reference/README.md) for complete feature list
- **Color Reference:** See [COLOR-PALETTE.md](COLOR-PALETTE.md) for all colors
- **Customization:** Each snippet has detailed comments explaining what it does

### Join the Community

- Share your customizations
- Report bugs or request features
- Show off your vault screenshots

---

## 🎓 Pro Tips

### Tip 1: Use JetBrains Mono Font

1. Download [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
2. Install the font on your system
3. Reload Obsidian
4. Headings and code will automatically use it

### Tip 2: Combine with Minimal Theme

These snippets work great with the Minimal theme:
1. Install Minimal theme from Community Themes
2. Enable these snippets
3. Snippets will override Minimal where needed

### Tip 3: Create Your Own Snippet

1. Copy any snippet file as a template
2. Rename it (e.g., `11-custom.css`)
3. Modify the CSS rules
4. Save to `.obsidian/snippets/`
5. Enable in Settings

### Tip 4: Preview Before Committing

Use Obsidian's built-in DevTools to test changes:
1. Press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac)
2. Click "Elements" tab
3. Add CSS rules temporarily to test
4. Copy working rules to your snippet file

---

## ⌨️ Keyboard Shortcuts

- **Reload Obsidian:** `Ctrl+R` / `Cmd+R`
- **Open DevTools:** `Ctrl+Shift+I` / `Cmd+Option+I`
- **Open Settings:** `Ctrl+,` / `Cmd+,`
- **Command Palette:** `Ctrl+P` / `Cmd+P`

---

## 📋 Checklist

Use this checklist for your first install:

- [ ] Downloaded all snippet files
- [ ] Copied files to `.obsidian/snippets/` folder
- [ ] Refreshed CSS snippets list in Settings
- [ ] Enabled `01-variables.css`
- [ ] Enabled desired additional snippets
- [ ] Reloaded Obsidian (`Ctrl+R`)
- [ ] Checked Dark Mode is enabled
- [ ] Verified headings look correct
- [ ] Tested link hover effects
- [ ] (Optional) Installed JetBrains Mono font

---

## 🆘 Need Help?

### Common Issues

| Problem | Solution |
|---------|----------|
| Nothing changed | Enable Dark Mode, enable 01-variables.css |
| Weird colors | Disable other theme, reload Obsidian |
| Slow performance | Disable 06-animations.css |
| Headings too large | Adjust font sizes in 02-typography.css |

### Still Stuck?

1. Check [README.md](04-library/02-pkb-and-pkm-learning/-reference/_snippets-&-themes/_master-snippet-system-reference/README.md) for detailed documentation
2. Review snippet comments for inline help
3. Open DevTools to inspect elements
4. Try disabling all snippets and re-enabling one at a time

---

**Ready to customize?** See [README.md](04-library/02-pkb-and-pkm-learning/-reference/_snippets-&-themes/_master-snippet-system-reference/README.md) for advanced options!

**Want to understand colors?** See [COLOR-PALETTE.md](COLOR-PALETTE.md) for the complete palette!

---

**Version:** 1.0.0
**Last Updated:** 2025-12-13
**Author:** Pur3v4d3r

🎨 **Enjoy your enhanced Obsidian experience!**
