# Enhanced Tasks Styling Guide

## Overview
This guide covers the custom CSS snippet `enhanced-tasks-styling.css` that enhances the Obsidian Tasks plugin with visual improvements.

## Features Included

### 1. Strikethrough Completion
- **Completed tasks** `[x]` → Text with strikethrough + fade effect
- **Cancelled tasks** `[-]` → Double strikethrough with red tint

### 2. Colored Text by Task Status

| Checkbox | Status | Color | Style |
|----------|--------|-------|-------|
| `[ ]` | Todo | Default | Normal |
| `[x]` | Done | Muted | Strikethrough |
| `[/]` | In Progress | Blue | Bold |
| `[!]` | Important | Red | Bold + Pulse |
| `[?]` | Question | Purple | Italic |
| `[i]` | Idea | Yellow | Normal |
| `[R]` | Research | Teal | Normal |
| `[*]` | Star | Gold | Bold |
| `[P]` | Pro | Green | Normal |
| `[C]` | Con | Red | Normal |
| `[>]` | Forward | Orange | Normal |
| `[<]` | Migrated | Blue | Faded |
| `[B]` | Brainstorm | Purple | Italic |
| `[Q]` | Quote | Blue | Serif + Italic |
| `[s]` | Secret | Purple | Blurred (hover to reveal) |
| `[W]` | World | Cyan | Normal |
| `[F]` | Foreshadow | Purple | Text shadow |
| `[@]` | Person | Default | Normal |
| `[L]` | Location | Default | Normal |
| `[T]` | Time | Default | Normal |
| `[H]` | Health/Favorite | Default | Normal |

### 3. Emoji Icons (Reading Mode)

Automatic emoji prefixes in reading mode:

- `[!]` → 🔥 (Fire)
- `[i]` → 💡 (Light bulb)
- `[?]` → ❓ (Question mark)
- `[*]` → ⭐ (Star)
- `[R]` → 🔬 (Microscope)
- `[B]` → 🧠 (Brain)
- `[@]` → 👤 (Person)
- `[L]` → 📍 (Location pin)
- `[T]` → ⏰ (Clock)
- `[H]` → ❤️ (Heart)
- `[x]` → ✅ (Check mark)
- `[-]` → ❌ (Cross mark)
- `[/]` → ⏳ (Hourglass)
- `[P]` → ✅ (Pro check)
- `[C]` → ❌ (Con cross)

### 4. Background Highlighting

Special tasks get colored backgrounds with border accents:
- **Important `[!]`**: Red left border + red tinted background
- **Star `[*]`**: Gold left border + gold tinted background
- **In Progress `[/]`**: Blue left border + blue tinted background

### 5. Animations

- **Pulse effect**: Important tasks `[!]` have a subtle pulse animation
- **Fade effect**: Completed tasks fade smoothly when checked
- **Hover effects**: All tasks brighten slightly on hover
- **Smooth transitions**: All color/style changes are animated

### 6. Priority Tags (Bonus Feature)

Add tags to your tasks for additional priority highlighting:

```markdown
- [ ] Important task #high
- [ ] Medium priority #medium
- [ ] Low priority #low
```

Or use the alternate format:
```markdown
- [ ] Task #priority/high
- [ ] Task #priority/medium
- [ ] Task #priority/low
```

Priority styling includes colored left borders and tinted backgrounds.

### 7. Special Effects

**Secret Tasks** `[s]` - Text is blurred until you hover over it:
```markdown
- [s] This text is hidden until hover
```

**Recurring Tasks** - Automatically detects Tasks plugin recurring indicators and adds a 🔄 emoji.

### 8. Dark Mode Support

All colors automatically adjust for dark theme to ensure readability.

## Usage Examples

### Basic Task with Status
```markdown
- [ ] Regular task
- [x] Completed task (will show strikethrough)
- [!] Urgent task (red with pulse animation)
- [/] Working on this (blue, in progress)
- [?] Need to figure this out (purple, italic)
- [i] Great idea (yellow)
```

### Task with Priority
```markdown
- [!] Critical bug to fix #high
- [ ] Feature to implement #medium
- [ ] Nice to have #low
```

### Task with Emojis (Reading Mode)
When you switch to reading mode, tasks automatically get emoji prefixes:
```markdown
- [!] Urgent deadline
```
Displays as: 🔥 Urgent deadline

### Special Task Types
```markdown
- [B] Brainstorm ideas for project (purple, italic)
- [R] Research best practices (teal, with microscope emoji)
- [*] Priority feature (gold highlight)
- [s] Surprise party plans (blurred until hover)
- [@] Contact John about meeting
- [L] Visit the new office location
```

## Customization

### Toggle On/Off
To temporarily disable all enhanced styling, add this class to your body:
```css
body.enhanced-tasks-off
```

You can do this via Style Settings plugin or by adding it to your theme.

### Modify Colors
Edit the CSS file and search for the color codes:
- `#e06c75` - Red (Important)
- `#61afef` - Blue (In Progress)
- `#e5c07b` - Yellow (Idea)
- `#c678dd` - Purple (Question)
- `#98c379` - Green (Pro)
- `#d4af37` - Gold (Star)

### Add More Emoji Icons
To add icons for other task types, use this pattern:
```css
body .markdown-rendered .task-list-item[data-task="YOUR_SYMBOL"] .task-list-item-checkbox ~ span::before {
    content: "YOUR_EMOJI ";
    font-size: 0.9em;
}
```

## Tips & Tricks

1. **Combine with Task Plugin Features**: Use dates, priorities, and recurrence with your styled tasks
2. **Use in Task Queries**: All styling works with Tasks plugin query blocks
3. **Mix and Match**: Combine status symbols with priority tags for maximum organization
4. **Accessibility**: All colors meet WCAG contrast requirements in both light and dark modes

## Installation

1. The snippet is already saved to: `.obsidian/snippets/enhanced-tasks-styling.css`
2. Go to Settings → Appearance → CSS snippets
3. Click the refresh icon (⟳) if you don't see it
4. Toggle on "enhanced-tasks-styling"
5. Enjoy your enhanced tasks!

## Compatibility

- ✅ Works with Obsidian Tasks Plugin
- ✅ Compatible with both Reading and Live Preview modes
- ✅ Dark and Light theme support
- ✅ Works with Minimal theme and most other themes
- ✅ Compatible with Style Settings plugin

## Community Resources Referenced

This snippet was inspired by:
- Obsidian Tasks Plugin official documentation
- Things Theme checkbox styling
- Minimal Theme alternate checkboxes
- ITS Theme task enhancements
- Community snippets from Obsidian forum

## Troubleshooting

**Styles not showing?**
1. Make sure the snippet is enabled in Settings → Appearance → CSS snippets
2. Try reloading Obsidian (Ctrl/Cmd + R)
3. Check that Tasks plugin is installed and enabled

**Colors look wrong?**
- Some themes override task colors. Try adjusting the snippet specificity or use `!important` flags

**Emojis not showing?**
- Emojis only appear in Reading mode, not in Edit or Live Preview mode
- Make sure your font supports emoji characters

## Version
Version 1.0 - Created with Claude Code

---

Enjoy your beautifully styled tasks! 🎨✨
