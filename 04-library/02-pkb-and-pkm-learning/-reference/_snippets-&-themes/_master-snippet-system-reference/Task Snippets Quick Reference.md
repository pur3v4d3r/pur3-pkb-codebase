# Task Snippets Quick Reference Sheet

> **⚠️ Important**: These two snippets conflict with each other. Only enable ONE at a time.
> - **Enhanced Tasks Styling**: Functional task management with colors & emojis
> - **Alternate Checkboxes**: Visual checkbox variety with custom icons

---

## 🎨 Enhanced Tasks Styling (Recommended)

**File**: `enhanced-tasks-styling.css` (470 lines)
**Best For**: Productivity, task management, GTD workflows, project planning

### Standard Tasks

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [ ]` | Todo | Normal | Default | - | Uncompleted task |
| `- [x]` | Complete | Strikethrough + fade | Gray muted | ✅ | Completed task (opacity 0.6) |
| `- [X]` | Complete | Strikethrough + fade | Gray muted | ✅ | Completed (uppercase also works) |

### Status Tasks

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [/]` | In Progress | Blue background + border | Blue (#61afef) | ⏳ | Currently working on |
| `- [!]` | Important | Red background + pulse | Red (#e06c75) | 🔥 | High priority with animation |
| `- [?]` | Question | Italic | Purple (#c678dd) | ❓ | Needs clarification |
| `- [i]` | Idea | Normal | Yellow (#e5c07b) | 💡 | Brainstorming/idea |
| `- [*]` | Star | Gold background + border | Gold (#d4af37) | ⭐ | Starred/important |
| `- [-]` | Cancelled | Double strikethrough | Red fade | ❌ | Cancelled task |

### Research & Analysis

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [R]` | Research | Normal | Teal (#56b6c2) | 🔬 | Research task |
| `- [B]` | Brainstorm | Italic | Purple (#bb9af7) | 🧠 | Brainstorming session |
| `- [Q]` | Quote | Serif font, italic | Blue (#7aa2f7) | - | Quotation or reference |

### Pro/Con & Arguments

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [P]` | Pro | Normal | Green (#98c379) | ✅ | Pro argument |
| `- [C]` | Con | Normal | Red (#be5046) | ❌ | Con argument |

### Context Tasks

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [@]` | Person | Normal | Default | 👤 | Assign to person |
| `- [L]` | Location | Normal | Default | 📍 | Location-specific |
| `- [T]` | Time | Normal | Default | ⏰ | Time-sensitive |
| `- [H]` | Heart | Normal | Default | ❤️ | Important/loved item |

### Movement Tasks

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [>]` | Forward | Normal | Orange (#d19a66) | - | Scheduled/forwarded |
| `- [<]` | Migrated | Faded | Muted blue (#528bff) | - | Moved to another location |

### Special Tasks

| Syntax | Name | Visual | Color | Emoji | Description |
|--------|------|--------|-------|-------|-------------|
| `- [s]` | Secret | **Blurred until hover** | Purple (#9d7cd8) | - | Hidden text (blur effect) |
| `- [W]` | World | Normal | Cyan (#7dcfff) | - | World/global scope |
| `- [F]` | Foreshadow | Text shadow | Purple (#bb9af7) | - | Future reference |

### Priority Tags (Works with any task)

```markdown
- [ ] Task text #priority/high    → Red background, bold
- [ ] Task text #priority/medium  → Orange background
- [ ] Task text #priority/low     → Green background
- [ ] Task text #high             → Also works (shorter version)
```

### Special Features

- **Pulse Animation**: `[!]` tasks pulse with red glow
- **Strikethrough**: `[x]` and `[-]` tasks have strikethrough
- **Recurring Indicator**: Tasks with `.task-recurring` class show 🔄
- **Hover Effects**: All tasks brighten on hover
- **Dark Mode**: Colors auto-adjust for dark theme

---

## 🎯 Alternate Checkboxes

**File**: `alternate-checkboxes.css` (1,291 lines)
**Best For**: Visual aesthetics, themed notes, creative projects

### Available Checkbox Types

| Syntax | Name | Icon Style | Description |
|--------|------|------------|-------------|
| `- [ ]` | Unchecked | Empty box | Standard unchecked box |
| `- [x]` | Checked | Checkmark | Standard checked box |
| `- [X]` | Checked | Checkmark | Uppercase X (same as lowercase) |
| `- [>]` | Forward | Arrow right | Scheduled/forwarded task |
| `- [<]` | Backward | Arrow left | Rescheduled/moved back |
| `- [-]` | Dropped | Minus/dash | Cancelled/dropped task |
| `- [?]` | Question | Question mark | Uncertain/needs info |
| `- [/]` | Half Done | Slash | Partially complete |
| `- [!]` | Important | Exclamation | High priority/urgent |
| `- [+]` | Added | Plus sign | New/added item |
| `- [~]` | Confused | Tilde/wave | Uncertain/confused |
| `- [@]` | Character/Person | At symbol | Person/character related |
| `- [&]` | And/Link | Ampersand | Connected/linked items |

### Visual Features

- **Custom Icons**: Uses embedded icon fonts (ITS Icons)
- **Checkbox Variations**: Multiple visual styles for checkboxes
- **Strikethrough Options**: Optional strikethrough for checked items
- **Color Coding**: Different colors for different task types
- **Theme Support**: Works with light and dark themes

### Optional Classes (Advanced)

Add these CSS classes to your note's frontmatter to enable features:

```yaml
---
cssclasses:
  - check-strike         # Strikethrough ALL checked tasks
  - checkbox-strike-frwd # Strikethrough > (forward) tasks
  - checkbox-strike-bkwd # Strikethrough < (backward) tasks
  - checkbox-strike-dropped # Strikethrough - (dropped) tasks
  - checkbox-strike-q    # Strikethrough ? (question) tasks
  - checkbox-strike-imp  # Strikethrough ! (important) tasks
  - checkbox-strike-add  # Strikethrough + (added) tasks
  - checkbox-strike-half # Strikethrough / (half done) tasks
  - checkbox-strike-conf # Strikethrough ~ (confused) tasks
  - checkbox-strike-char # Strikethrough @ (character) tasks
---
```

---

## 📋 Usage Examples

### Enhanced Tasks Example

```markdown
## Daily Tasks

### High Priority 🔥
- [!] Fix production bug #priority/high
- [!] Client meeting at 2pm

### In Progress ⏳
- [/] Writing documentation
- [/] Code review for PR #123

### Standard Tasks
- [ ] Update dependencies
- [ ] Reply to emails
- [?] Check with team about deadline

### Ideas 💡
- [i] Consider migrating to new framework
- [i] Refactor authentication module

### Research 🔬
- [R] Investigate GraphQL alternatives
- [R] Security audit tools

### Completed ✅
- [x] Morning standup
- [x] Deploy to staging
- [x] Update Jira tickets

### Cancelled ❌
- [-] Old feature nobody wanted
- [-] Deprecated API integration
```

### Alternate Checkboxes Example

```markdown
## Project Tracking

### Status Updates
- [>] Moved to next sprint
- [<] Pulled back for revision
- [/] Half complete
- [-] Dropped from scope

### Priority Markers
- [!] Critical bug fix needed
- [+] New feature request
- [?] Needs clarification

### Team Tasks
- [@] Assigned to John
- [&] Dependent on other task
- [~] Waiting for decision

### Completed
- [x] Setup complete
- [X] Testing done
```

---

## 🔄 Switching Between Snippets

### To Enable a Snippet:
1. Press `Ctrl/Cmd + ,` to open Settings
2. Navigate to **Appearance** → **CSS Snippets**
3. Toggle ON the desired snippet
4. Changes apply immediately

### To Disable a Snippet:
1. Go to **Appearance** → **CSS Snippets**
2. Toggle OFF the snippet
3. Changes apply immediately

### Best Practice:
**Never enable both snippets at the same time** - they will conflict and cause visual inconsistencies.

---

## 🎯 Which One Should I Use?

### Choose Enhanced Tasks If:
- ✅ You use Obsidian for task management
- ✅ You want color-coded status indicators
- ✅ You use emoji indicators
- ✅ You need priority tagging
- ✅ You want animated important tasks
- ✅ You follow GTD, bullet journal, or project management workflows
- ✅ **Recommended for most users**

### Choose Alternate Checkboxes If:
- ✅ Visual aesthetics are your priority
- ✅ You want custom icon designs
- ✅ You create themed notes
- ✅ You don't need functional task management
- ✅ You prefer simple icon-based checkboxes

---

## 💡 Pro Tips

### Enhanced Tasks Tips:
1. **Use `[!]` sparingly** - The pulse animation draws attention
2. **Combine with tags** - Use `#priority/high` with `[!]` for critical tasks
3. **Secret tasks** - Use `[s]` for sensitive information that reveals on hover
4. **Pro/Con lists** - Use `[P]` and `[C]` for decision-making
5. **Quick visual scan** - Emojis make it easy to see task types at a glance

- [!] 

### Alternate Checkboxes Tips:
1. **Strikethrough control** - Add CSS classes to control which tasks get strikethrough
2. **Use consistently** - Pick a meaning for each symbol and stick to it
3. **Documentation** - Document your checkbox meanings in a note
4. **Theme matching** - Icons work well with themed note templates

---

## 🔧 Customization

### Enhanced Tasks:
- Colors defined in lines 36-100
- Emojis defined in lines 105-180
- Background highlighting in lines 186-211
- Animations in lines 223-251

### Alternate Checkboxes:
- Custom fonts embedded (lines 1-200)
- Checkbox styles throughout the file
- Icon mappings in pseudo-elements
- Strike-through classes at the end

**To customize**: Edit the CSS files directly in `.obsidian/snippets/`

---

## ⚙️ Troubleshooting

### Issue: Checkboxes not showing correctly
- **Solution**: Make sure only ONE snippet is enabled at a time

### Issue: Colors not showing
- **Solution**: Check if you're in Reading/Preview mode (colors show best there)

### Issue: Emojis not appearing
- **Solution**: Enhanced Tasks emojis only appear in Reading mode, not Live Preview

### Issue: Strikethrough not working
- **Solution**: For Alternate Checkboxes, add appropriate CSS class to frontmatter

### Issue: Performance slow
- **Solution**: Disable Alternate Checkboxes (it's 1,291 lines). Use Enhanced Tasks instead (470 lines)

---

## 📖 Syntax Cheat Sheet

### Enhanced Tasks (One-Line Reference)
```
[ ] [x] [/] [!] [?] [i] [*] [-] [R] [B] [Q] [P] [C] [@] [L] [T] [H] [>] [<] [s] [W] [F]
```

### Alternate Checkboxes (One-Line Reference)
```
[ ] [x] [X] [>] [<] [-] [?] [/] [!] [+] [~] [@] [&]
```

---

**Last Updated**: 2025-12-13
**Files**:
- [enhanced-tasks-styling.css](.obsidian/snippets/enhanced-tasks-styling.css)
- [alternate-checkboxes.css](.obsidian/snippets/alternate-checkboxes.css)
