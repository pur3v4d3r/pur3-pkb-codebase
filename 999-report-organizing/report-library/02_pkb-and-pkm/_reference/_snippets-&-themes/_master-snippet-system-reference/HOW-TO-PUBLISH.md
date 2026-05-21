# How to Publish to GitHub

> **Share your snippet collection with the Obsidian community**

---

## 🚀 Quick GitHub Setup

### Step 1: Install Git (if needed)

**Windows:**
1. Download from https://git-scm.com/download/win
2. Run installer with default options
3. Restart terminal/command prompt

**Check if Git is installed:**
```bash
git --version
```

---

### Step 2: Create GitHub Repository

1. Go to https://github.com
2. Sign in (or create account)
3. Click the **+** icon (top right) → **New repository**
4. Fill in:
   - **Repository name:** `obsidian-cyberpunk-snippets`
   - **Description:** "Cyberpunk-themed CSS snippets for Obsidian with gradient effects"
   - **Visibility:** Public ✅
   - **Initialize:** ❌ Do NOT check any boxes
5. Click **Create repository**

---

### Step 3: Initialize Local Repository

Open terminal/command prompt and navigate to your package:

```bash
cd "d:\10_pur3v4d3r's-vault\snippets-package"
```

Initialize Git:

```bash
git init
git add .
git commit -m "Initial release v1.0.0 - Complete CSS snippet collection"
```

---

### Step 4: Connect to GitHub

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR-USERNAME/obsidian-cyberpunk-snippets.git
git branch -M main
git push -u origin main
```

**Authentication:**
- GitHub will prompt for credentials
- Use a Personal Access Token (not password)
- Generate token at: Settings → Developer settings → Personal access tokens

---

### Step 5: Add Repository Metadata

**Create .gitignore:**

Create file `d:\10_pur3v4d3r's-vault\snippets-package\.gitignore`:

```
# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Temp
*.tmp
*.bak
```

**Create LICENSE:**

Create file `d:\10_pur3v4d3r's-vault\snippets-package\LICENSE`:

```
MIT License

Copyright (c) 2025 Pur3v4d3r

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Commit these:**

```bash
git add .gitignore LICENSE
git commit -m "Add license and gitignore"
git push
```

---

### Step 6: Create Release

1. Go to your GitHub repo
2. Click **Releases** (right sidebar)
3. Click **Create a new release**
4. Fill in:
   - **Tag:** `v1.0.0`
   - **Title:** `v1.0.0 - Initial Release`
   - **Description:** Copy from CHANGELOG.md
5. Click **Publish release**

---

## 📢 Share with Community

### Obsidian Forum

Post in: https://forum.obsidian.md/c/share-showcase/9

**Title:** `[CSS] Cyberpunk Theme Snippets - Animated Gradients & Effects`

**Template:**
```markdown
# Pur3v4d3r's Cyberpunk CSS Snippets

A complete collection of modular CSS snippets featuring:
- 🎨 Gold, Purple, and Cyan color scheme
- ✨ Animated gradient effects
- 🔗 Hover link animations
- 📝 Syntax highlighting
- 🎭 Optional gradient text

**GitHub:** [Link to your repo]
**Screenshots:** [Add screenshots]

## Quick Install
1. Download from releases
2. Copy to `.obsidian/snippets/`
3. Enable in Settings → Appearance

See README for full documentation!
```

### Reddit

Post in: r/ObsidianMD

**Title:** `Cyberpunk CSS Snippet Collection - Modular theme components`

---

## 📸 Screenshot Guide

Take screenshots showing:

1. **Before/After** - Default theme vs with snippets
2. **Animated H1** - Screen recording of shimmer
3. **Link hover** - Gradient expansion
4. **Code blocks** - Inline code with glow
5. **Color palette** - Show the color scheme

**Tools:**
- Windows: Snipping Tool, Win+Shift+S
- Screen recording: OBS Studio, ShareX
- GIF maker: ScreenToGif

---

## 🏷️ Add Topics to Repo

On GitHub repo page:
1. Click ⚙️ (settings icon) next to "About"
2. Add topics:
   - `obsidian`
   - `obsidian-md`
   - `css`
   - `css-snippets`
   - `theme`
   - `cyberpunk`
   - `gradient`
   - `markdown`

---

## 📊 Repository Badges

Add to top of README.md:

```markdown
[![GitHub release](https://img.shields.io/github/v/release/YOUR-USERNAME/obsidian-cyberpunk-snippets)](https://github.com/YOUR-USERNAME/obsidian-cyberpunk-snippets/releases)
[![GitHub stars](https://img.shields.io/github/stars/YOUR-USERNAME/obsidian-cyberpunk-snippets)](https://github.com/YOUR-USERNAME/obsidian-cyberpunk-snippets/stargazers)
[![License](https://img.shields.io/badge/License-MIT-ffc700)](LICENSE)
```

---

## 🔄 Future Updates

**When you make changes:**

```bash
# Make your edits
git add .
git commit -m "Description of changes"
git push

# Create new release
# Bump version in CHANGELOG.md
# Create new GitHub release with new tag
```

---

## ✅ Checklist

- [ ] Git installed
- [ ] GitHub account created
- [ ] Repository created
- [ ] Files pushed to GitHub
- [ ] LICENSE added
- [ ] .gitignore added
- [ ] First release created
- [ ] Topics added
- [ ] Screenshots taken
- [ ] Posted to Obsidian forum
- [ ] Posted to Reddit

---

**Need Help?**
- GitHub Docs: https://docs.github.com
- Git Tutorial: https://www.atlassian.com/git
- Obsidian Forum: https://forum.obsidian.md
