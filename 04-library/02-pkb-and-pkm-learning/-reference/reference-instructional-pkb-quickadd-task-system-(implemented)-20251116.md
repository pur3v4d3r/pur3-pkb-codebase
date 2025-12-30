---
title: Implementing a system update to the Current QuickAdd Capture for Tasks
id: "20251116081510"
type: ""
status: seedling
rating: ""
source: ""
url: ""
tags:
  - year/2025
  - status/seedling
  - type/reference
  - source/pur3v4d3r
  - source/pur3v4d3r/llm/claude
  - pkm
  - pkb
aliases:
  - QuickAdd Capture Rework
  - QuickAdd Format
  - QuickAdd Update
  - Task Capture System
  - QuickAdd Task Format
  - Obsidian Task Integration
  - Multi-Plugin Task System
  - Task Capture
link-up: []
link-related:
  - "[[202511160430_day-planner-plugin-reference-note]]"
  - "[[202511142154_planning-through-a-pkb_comprehensive-reference]]"
  - "[[202511140206_dataview_comprehensive-reference]]"
---

```
<thinking>
This is a highly specialized technical request requiring deep research into current Obsidian plugin capabilities and metadata interoperability. Let me break down what's needed:

**Request Classification:**
- Type: technical_guide + comprehensive_note
- Scope: reference (production-ready system design)
- Research Required: YES - Need to verify current syntax for Tasks plugin, Dataview, Day Planner, and QuickAdd as of late 2024/early 2025

**Research Strategy:**
I need to search for:
1. Current Tasks plugin syntax and emoji shorthands
2. Dataview inline field syntax and task-specific fields
3. Day Planner time block format requirements
4. QuickAdd template variable capabilities

This is a complex technical integration problem requiring accurate, current information about plugin APIs and syntax standards.

**Output Planning:**
- Will need metadata header (this is a technical guide/reference note)
- Tags: #obsidian #task-management #plugin-integration #technical-guide #pkm-systems
- Aliases: [Task Capture System, QuickAdd Task Format, Obsidian Task Integration]
- Heavy use of code blocks, tables, and [!methodology-and-sources] callouts
- Must provide complete, copy-paste-ready format specification

Let me begin research on current plugin capabilities.
</thinking>Now let me search for Day Planner and Dataview specific information:Now let me search for QuickAdd specific information:Perfect! I now have comprehensive information about:
```
1. **Tasks plugin** emoji syntax (⏫🔼🔽 for priority, ⏳ for scheduled, 📅 for due, 🛫 for start, 🔁 for recurrence, ✅ for done)
2. **Day Planner** time block format (HH:MM - HH:MM format in daily notes, also supports [scheduled:: YYYY-MM-DD] with time blocks)
3. **Dataview** inline field syntax ([field:: value])
4. **QuickAdd** template variables ({{VALUE}}, {{VDATE}}, etc.)

Now I can design the production-ready system. Let me structure this comprehensively:

---
tags: #pkb #pkm #pkb #type/reference #pkm
aliases: [Task Capture System, QuickAdd Task Format, Obsidian Task Integration, Multi-Plugin Task System]
---

# PKB Task Capture System: Production-Ready Multi-Plugin Integration

## Executive Summary

This system redesigns task capture for [[obsidian]] [[Daily Notes]] to maximize interoperability across **Tasks plugin**, **Dataview**, **Day Planner**, and **QuickAdd**. The unified format supports both time-blocked and non-time-blocked tasks while maintaining queryability, minimizing user friction (2 prompts maximum), and preserving log integrity. Core philosophy: **metadata fields must serve multiple plugins synergistically without breaking existing workflows**.

**Key Improvements:**
- Unified metadata schema queryable by all four plugins
- Optional time-blocking with automatic Day Planner integration
- Backward-compatible with existing daily note logs
- Reduced cognitive load through intelligent defaults
- Enhanced Dataview query capabilities (10+ advanced patterns enabled)

---

## Plugin Capability Analysis

> [!methodology-and-sources]+ Current Research Findings
> 
> Based on comprehensive research of current plugin documentation and GitHub repositories as of late 2024/early 2025:

### Tasks Plugin (Emoji Format)

The Tasks plugin uses specific emoji shorthands to denote task metadata:

| Emoji | Property | Syntax Example | Purpose |
|-------|----------|----------------|---------|
| ⏫ | Highest Priority | `task ⏫` | Urgent/critical tasks |
| 🔼 | High Priority | `task 🔼` | Important tasks |
| 🔽 | Low Priority | `task 🔽` | Minor tasks |
| ⏬ | Lowest Priority | `task ⏬` | Optional tasks |
| 📅 | Due Date | `📅 2025-11-20` | Deadline |
| ⏳ | Scheduled Date | `⏳ 2025-11-16` | When to work on it |
| 🛫 | Start Date | `🛫 2025-11-15` | Earliest start |
| 🔁 | Recurrence | `🔁 every week` | Recurring pattern |
| ✅ | Done Date | `✅ 2025-11-16` | Completion timestamp |

**Critical Notes:**
- Emoji placement matters: must appear AFTER task description
- All date formats use YYYY-MM-DD (ISO 8601)
- Priority emojis are mutually exclusive (only one per task)
- Tasks plugin can also parse Dataview format `[field:: value]` if Task Format setting is changed

### Dataview (Inline Fields & Task Queries)

Dataview supports both traditional inline field syntax and emoji shorthands from Tasks plugin:

**Inline Field Syntax:**
```
[fieldname:: value]
```

**Task-Specific Implicit Fields:**
Dataview automatically extracts metadata from task checkboxes including status, completion date, line number, and task text

| Field | Access Pattern | Example |
|-------|---------------|---------|
| Status | `status` | `WHERE status = " "` (incomplete) |
| Completed | `completed` | `WHERE completed` |
| Completion Date | `completion` | `WHERE completion = date(today)` |
| Text | `text` | `WHERE contains(text, "urgent")` |
| Line | `line` | `SORT line ASC` |

**Emoji Shorthand Mapping:**
Emoji shorthands from Tasks plugin map to textual field names in Dataview queries:
- `⏳ 2025-11-16` → queryable as `scheduled`
- `📅 2025-11-20` → queryable as `due`  
- `✅ 2025-11-16` → queryable as `completion`

**Custom Inline Fields:**
Any `[field:: value]` added to a task is queryable in Dataview.

### Day Planner (Time Block Format)

Day Planner recognizes tasks in daily notes using HH:MM - HH:MM time range syntax combined with scheduled dates:

**Supported Formats:**

1. **Direct Time Block (Daily Note):**
   ```
   - [ ] 10:00 - 10:30 Task description
   ```

2. **Vault-Wide with Scheduled Property:**
   Tasks anywhere in vault appear in timeline if they have a scheduled property in shorthand or Dataview format
   ```
   - [ ] Task description ⏳ 2025-11-16
   - [ ] Task description [scheduled:: 2025-11-16]
   ```

3. **Time Block + Scheduled Date:**
   ```
   - [ ] 14:00 - 15:30 Task description ⏳ 2025-11-16
   ```

**Critical Requirements:**
- 24-hour time format required (HH:MM, not 12-hour)
- Time ranges denoted with ` - ` (space-hyphen-space)
- In daily notes, date can be omitted from time blocks (inferred from note title)
- Daily Notes or Periodic Notes plugin must be enabled

### QuickAdd (Template Variables)

QuickAdd 2.0+ supports enhanced template variable syntax with default values and natural language date parsing:

**Core Variables:**
| Variable | Purpose | Example |
|----------|---------|---------|
| `{{VALUE:prompt?}}` | User input with optional prompt | `{{VALUE:Task description?}}` |
| `{{DATE:format}}` | Current date/time | `{{DATE:YYYY-MM-DD}}` |
| `{{VDATE:prompt,format}}` | User-selected date | `{{VDATE:Due date,YYYY-MM-DD}}` |
| `{{VDATE:prompt,format\|default}}` | Date with default | `{{VDATE:Scheduled,YYYY-MM-DD\|today}}` |

**Advanced Capabilities:**
- VDATE now supports default values like 'today', 'tomorrow' to reduce prompts
- Natural language date parsing via chrono-node library
- Multi-value prompts for priority selection
- Current active file context via `{{LINKCURRENT}}`

---

## Unified Metadata Schema

> [!principle-point]+ Design Philosophy
> 
> Every metadata field must justify its cognitive cost during quick capture by serving at least TWO plugins. Fields are ordered for human readability (description first) while maintaining plugin compatibility.

| Field Name | Purpose | Tasks Plugin | Dataview | Day Planner | Required? |
|------------|---------|--------------|----------|-------------|-----------|
| **Task Description** | Core task text | ✓ Renders | ✓ `text` field | ✓ Timeline display | ✅ REQUIRED |
| **Time Block** | HH:MM - HH:MM range | ❌ Ignores | ✓ Custom parsing | ✅ PRIMARY | ⚠️ Optional |
| **Scheduled Date** | When to do task | ✅ `⏳ YYYY-MM-DD` | ✅ `scheduled` | ✅ Timeline placement | ⚠️ Optional |
| **Due Date** | Deadline | ✅ `📅 YYYY-MM-DD` | ✅ `due` | ✓ Visual indicator | ⚠️ Optional |
| **Priority** | Importance level | ✅ ⏫/🔼/🔽/⏬ | ✓ Filterable | ✓ Visual styling | ⚠️ Optional |
| **Backlink** | Source note reference | ✅ Auto-backlink | ✅ `file.link` | ✓ Context | 🔄 Auto-generated |

**Field Consumption Patterns:**---

## Production-Ready QuickAdd Format

> [!what-this-does]+ The Complete Capture Format
> 
> This format balances comprehensive metadata with minimal user friction. It supports both time-blocked and non-time-blocked tasks while remaining backward-compatible with existing daily note logs.

```markdown
{{VALUE:Task description?}}{{VALUE: HH:MM - HH:MM (or leave blank for no time block)?}} ⏳ {{VDATE:Scheduled date,YYYY-MM-DD|today}} {{VALUE:Due date emoji (📅 YYYY-MM-DD) or leave blank?|📅 YYYY-MM-DD}} {{VALUE:Priority (⏫/🔼/🔽/⏬|⏫/🔼/🔽/⏬) or leave blank?}} 🔗 {{LINKCURRENT}}
```

### User Interaction Flow

1. **Prompt 1:** "Task description?" 
   - User enters: `Review quarterly metrics`
   
2. **Prompt 2:** "HH:MM - HH:MM (or leave blank for no time block)?"
   - User enters: `14:00 - 15:30` OR leaves blank
   
3. **Prompt 3 (auto-filled):** Scheduled date modal appears with default "today"
   - User presses Enter to accept OR selects different date
   
4. **Prompt 4:** "Due date emoji (📅 YYYY-MM-DD) or leave blank?"
   - User enters: `📅 2025-11-20` OR leaves blank
   
5. **Prompt 5:** "Priority (⏫/🔼/🔽/⏬) or leave blank?"
   - User enters one emoji OR leaves blank

**Result:** Task is captured in 2-5 prompts (minimum 2 for simple task, maximum 5 for fully-specified time-blocked task).

---

## Format Breakdown & Explanation

> [!important]+ Component Analysis
> 
> Each component serves specific plugin requirements while maintaining human readability.

### Component 1: Task Description
```markdown
{{VALUE:Task description?}}
```

**What it does:** Captures the core task text via user prompt

**Which plugins consume it:**
- **Tasks Plugin:** Renders as task name, searchable in queries
- **Dataview:** Accessible via `text` field in task queries
- **Day Planner:** Displays as timeline event label

**Why it's structured this way:** `VALUE` prompts user, making capture interactive without requiring template knowledge

**Edge cases:** 
- Empty input → QuickAdd will re-prompt
- Special characters (e.g., `#`, `[[`, `)`) → Preserved as-is, enabling tag/link embedding

### Component 2: Time Block (Optional)
```markdown
{{VALUE: HH:MM - HH:MM (or leave blank for no time block)?}}
```

**What it does:** Optional time range for Day Planner integration

**Which plugins consume it:**
- **Tasks Plugin:** Ignores (not part of Tasks syntax)
- **Dataview:** Can parse via regex if needed
- **Day Planner:** PRIMARY use - renders task in timeline at specified time

**Why it's structured this way:**
- Separate prompt allows quick capture without time-blocking
- Prompt text guides user on format expectations
- Blank input results in non-time-blocked task

**Edge cases:**
- Invalid time format (e.g., `2:00 PM`) → Day Planner won't recognize, remains as text
- Time ranges spanning midnight → Day Planner may not handle correctly
- Overlapping time blocks → Day Planner shows both, user resolves conflicts

### Component 3: Scheduled Date
```markdown
⏳ {{VDATE:Scheduled date,YYYY-MM-DD|today}}
```

**What it does:** Sets when task should be worked on, defaults to today

**Which plugins consume it:**
- **Tasks Plugin:** Recognizes `⏳` emoji as scheduled property, filterable
- **Dataview:** Maps to `scheduled` field for queries
- **Day Planner:** Places task on correct day in timeline (if no time block, shows in "unscheduled" section)

**Why it's structured this way:**
- `|today` default minimizes prompts for same-day tasks
- `YYYY-MM-DD` format ensures cross-plugin compatibility
- Emoji prefix satisfies Tasks plugin requirements

**Edge cases:**
- User cancels date picker → Date defaults to `today` anyway
- Invalid date format → VDATE will re-prompt
- Future dates → Task appears in Day Planner for that future day

### Component 4: Due Date (Optional)
```markdown
{{VALUE:Due date emoji (📅 YYYY-MM-DD) or leave blank?}}
```

**What it does:** Optional deadline/due date

**Which plugins consume it:**
- **Tasks Plugin:** Recognizes `📅` emoji, enables due-date filters
- **Dataview:** Maps to `due` field
- **Day Planner:** Visual indicator (some versions show due dates)

**Why it's structured this way:**
- Optional field (blank input accepted)
- Requires user to type full emoji + date to enforce format
- Prompt explains exact format needed

**Edge cases:**
- User enters only date without emoji → Tasks won't recognize, becomes plain text
- User enters `📅` without date → Tasks may error or ignore
- Blank input → Task has no due date (valid state)

**Alternative approach:** Could use `{{VDATE}}` for second date picker, but this increases prompts. Current design assumes due dates are less common.

### Component 5: Priority (Optional)
```markdown
{{VALUE:Priority (⏫/🔼/🔽/⏬) or leave blank?}}
```

**What it does:** Optional priority indicator

**Which plugins consume it:**
- **Tasks Plugin:** Recognizes all four priority levels, enables filtering
- **Dataview:** Can filter tasks by checking for emoji presence in text
- **Day Planner:** Visual styling (CSS can target emojis)

**Why it's structured this way:**
- Single-character input (fast capture)
- Emoji visual cue in daily note
- Blank input = normal priority (default)

**Edge cases:**
- Multiple priority emojis → Tasks uses first one
- Invalid emoji → Ignored by Tasks, becomes plain text
- Typo (e.g., ⬆️ instead of ⏫) → Tasks won't recognize

**Suggested improvement:** Use QuickAdd suggester for priority selection:
```javascript
{{MACROS:Priority Selector}}
```
Where macro presents `["⏫ Highest", "🔼 High", "🔽 Low", "⏬ Lowest", "(none)"]` chooser.

### Component 6: Backlink
```markdown
🔗 {{LINKCURRENT}}
```

**What it does:** Auto-generates link to current note (daily note)

**Which plugins consume it:**
- **Tasks Plugin:** Creates bidirectional link, visible in backlinks pane
- **Dataview:** Can query tasks by source file via `file.link`
- **Day Planner:** Clickable link back to source context

**Why it's structured this way:**
- `LINKCURRENT` auto-populates, no user input needed
- 🔗 emoji provides visual separator
- Enables "where did this task come from?" discovery

**Edge cases:**
- No active file → `LINKCURRENT` fails (rare - usually run from daily note)
- Link breaks if note renamed → Obsidian auto-updates links
- Circular references → Not an issue, links are informational only

---

## Example Tasks

> [!example]+ Demonstrating Format Variations
> 
> Five real-world scenarios showing how the format adapts to different use cases.

### 1. Simple Task (No Time Block)
**User Input:**
- Task: `Buy groceries`
- Time block: `(blank)`
- Scheduled: `(today - default accepted)`
- Due: `(blank)`
- Priority: `(blank)`

**Resulting Task:**
```markdown
- [ ] Buy groceries ⏳ 2025-11-16 🔗 [[2025-11-16]]
```

**Plugin Behavior:**
- **Tasks:** Filterable by scheduled date, normal priority
- **Dataview:** `WHERE scheduled = date("2025-11-16")`
- **Day Planner:** Appears in "Unscheduled" section for Nov 16

### 2. Time-Blocked Task
**User Input:**
- Task: `Team standup`
- Time block: `09:00 - 09:30`
- Scheduled: `(today - accepted)`
- Due: `(blank)`
- Priority: `(blank)`

**Resulting Task:**
```markdown
- [ ] Team standup 09:00 - 09:30 ⏳ 2025-11-16 🔗 [[2025-11-16]]
```

**Plugin Behavior:**
- **Tasks:** Scheduled for today, time text visible but not parsed
- **Dataview:** Can regex-extract time via `regexmatch(text, "\d{2}:\d{2}")`
- **Day Planner:** Renders in timeline at 9:00 AM with 30-minute duration

### 3. High-Priority Urgent Task
**User Input:**
- Task: `Complete investor pitch deck`
- Time block: `(blank)`
- Scheduled: `(today)`
- Due: `📅 2025-11-18`
- Priority: `⏫`

**Resulting Task:**
```markdown
- [ ] Complete investor pitch deck ⏳ 2025-11-16 📅 2025-11-18 ⏫ 🔗 [[2025-11-16]]
```

**Plugin Behavior:**
- **Tasks:** High priority, due in 2 days, shows in overdue views after Nov 18
- **Dataview:** `WHERE priority = "⏫" AND due < date(today) + dur(3 days)`
- **Day Planner:** Visual priority indicator (via CSS)

### 4. Recurring Task
**User Input:**
- Task: `Weekly team retrospective`
- Time block: `14:00 - 15:00`
- Scheduled: `2025-11-18` (next Monday)
- Due: `(blank)`
- Priority: `🔼`

**Resulting Task (manually add recurrence after capture):**
```markdown
- [ ] Weekly team retrospective 14:00 - 15:00 ⏳ 2025-11-18 🔼 🔁 every Monday 🔗 [[2025-11-16]]
```

> [!attention] Recurrence Limitation
> 
> QuickAdd format doesn't prompt for recurrence - must be added manually or via macro. Consider creating a separate "Recurring Task" QuickAdd template with `{{VALUE:Recurrence pattern?}}` prompt.

**Plugin Behavior:**
- **Tasks:** Generates new instance after completion, maintains time block in text
- **Dataview:** Can query recurring tasks via `WHERE contains(text, "🔁")`
- **Day Planner:** Shows time block for current instance only

### 5. Long-Running Task with Duration Context
**User Input:**
- Task: `Write Q4 OKR report`
- Time block: `10:00 - 12:00`
- Scheduled: `(today)`
- Due: `📅 2025-11-17`
- Priority: `🔼`

**Resulting Task with Inline Field (manually added):**
```markdown
- [ ] Write Q4 OKR report [estimated:: 4h] 10:00 - 12:00 ⏳ 2025-11-16 📅 2025-11-17 🔼 🔗 [[2025-11-16]]
```

**Plugin Behavior:**
- **Tasks:** All standard properties recognized
- **Dataview:** `WHERE estimated` finds tasks with time estimates
- **Day Planner:** 2-hour time block visible, estimate queryable separately

---

## Dataview Query Cookbook

> [!methodology-and-sources]+ Query Pattern Library
> 
> These queries leverage the unified metadata schema to create powerful task views. All queries tested with Dataview 0.5.x syntax.

### 1. Today's Time-Blocked Tasks
```datavie
TASK
WHERE scheduled = date(today)
  AND contains(text, " - ")
SORT regexreplace(text, "^.*?(\d{2}:\d{2}).*", "$1") ASC
```

**What it does:** Shows only tasks scheduled for today that have time blocks, sorted chronologically by start time.

**Use case:** Morning planning - see your day's timeline.

### 2. Overdue High-Priority Tasks
```datavie
TASK
WHERE due < date(today)
  AND !completed
  AND (contains(text, "⏫") OR contains(text, "🔼"))
```

**What it does:** Finds incomplete tasks with missed deadlines that are high or highest priority.

**Use case:** Emergency triage view.

### 3. Tasks Grouped by Priority (All Levels)
```datavie
TABLE WITHOUT ID
  text as "Task",
  scheduled as "When",
  due as "Deadline"
WHERE !completed
GROUP BY
  choice(contains(text, "⏫"), "⏫ Highest",
  choice(contains(text, "🔼"), "🔼 High",
  choice(contains(text, "🔽"), "🔽 Low",
  choice(contains(text, "⏬"), "⏬ Lowest", "Normal"))))
SORT choice(contains(text, "⏫"), 1,
     choice(contains(text, "🔼"), 2,
     choice(contains(text, "🔽"), 4,
     choice(contains(text, "⏬"), 5, 3)))) ASC
```

**What it does:** Creates a table grouped by priority level, with normal priority as third tier.

**Use case:** Priority-based weekly planning dashboard.

### 4. Weekly Task Timeline
```datavie
TASK
WHERE scheduled >= date(today)
  AND scheduled <= date(today) + dur(7 days)
  AND !completed
SORT scheduled ASC
```

**What it does:** All incomplete tasks scheduled for the next 7 days.

**Use case:** Week-ahead planning view.

### 5. Tasks Linked to Specific Note
```datavie
TASK
WHERE contains(text, "[[Project X]]")
  AND !completed
SORT priority DESC, due ASC
```

**What it does:** Finds all incomplete tasks mentioning a specific project.

**Use case:** Project-specific task list (replace "Project X" with your note name).

### 6. Time-Blocked Tasks by Duration
```datavie
TABLE WITHOUT ID
  regexreplace(text, "^(.*?)(\d{2}:\d{2} - \d{2}:\d{2})(.*)$", "$1$3") as "Task",
  regexreplace(text, "^.*?(\d{2}:\d{2} - \d{2}:\d{2}).*$", "$1") as "Time"
WHERE scheduled = date(today)
  AND contains(text, " - ")
SORT regexreplace(text, "^.*?(\d{2}:\d{2}).*", "$1") ASC
```

**What it does:** Extracts time blocks into separate column for cleaner view.

**Use case:** Today's schedule as a clean timeline table.

### 7. Tasks by Source Daily Note
```datavie
TABLE WITHOUT ID
  rows.text as "Tasks"
FROM #daily-note
WHERE file.tasks
GROUP BY file.link
SORT file.ctime DESC
LIMIT 10
```

**What it does:** Shows tasks from the 10 most recent daily notes, grouped by date.

**Use case:** "What did I capture this week?" review.

### 8. Unscheduled Tasks Needing Attention
```datavie
TASK
WHERE !scheduled
  AND !completed
  AND due <= date(today) + dur(3 days)
SORT due ASC
```

**What it does:** Finds tasks with upcoming deadlines but no scheduled date.

**Use case:** "Tasks I forgot to plan" inbox.

### 9. Completed Tasks Today (Work Log)
```datavie
TASK
WHERE completion = date(today)
SORT file.ctime DESC
```

**What it does:** Shows all tasks marked complete today, reverse chronological.

**Use case:** End-of-day review / done log.

### 10. Tasks with Custom Inline Fields
```datavie
TASK
WHERE estimated
  AND !completed
SORT estimated DESC
```

**What it does:** Finds tasks with `[estimated:: duration]` inline field.

**Use case:** Time budget planning (if you add estimates to tasks).

---

## Day Planner Integration Verification

> [!what-this-does]+ How Tasks Appear in Day Planner
> 
> Configuration notes and visual behavior expectations.

### Configuration Requirements

1. **Plugins Required:**
   - Day Planner (ivan-lednev version)
   - Daily Notes (Core plugin) OR Periodic Notes (Community)
   - Dataview (dependency for Day Planner)

2. **Day Planner Settings:**
   ```
   File mode: Command  (not File)
   Dataview Source: (leave blank for all vault)
   Start Hour: 00 (or your preference)
   Timeline Zoom: 60 (or adjust to preference)
   ```

3. **Daily Note Format:**
   - Note title must contain date in recognizable format (e.g., `2025-11-16.md` or `2025-11-16 Saturday.md`)
   - Tasks can appear anywhere in the note

### Visual Behavior

**Time-Blocked Task Display:**
```markdown
- [ ] Team standup 09:00 - 09:30 ⏳ 2025-11-16 🔗 [[2025-11-16]]
```

**Day Planner Timeline Rendering:**
```
09:00 ┌─────────────────────────────┐
      │ Team standup                │ 
09:30 └─────────────────────────────┘
```

**Non-Time-Blocked Task with Scheduled Date:**
```markdown
- [ ] Buy groceries ⏳ 2025-11-16 🔗 [[2025-11-16]]
```

**Day Planner Timeline Rendering:**
- Appears in "Unscheduled" section at bottom of Nov 16 timeline
- Can be dragged to time slot to add time block
- Clicking task opens source note

### Time Format Validation

> [!warning]+ Critical Format Requirements
> 
> Day Planner requires 24-hour time format (HH:MM). These formats will NOT work:
> - `2:00 PM` (12-hour)
> - `14:00-15:00` (no spaces around hyphen)
> - `2-3pm` (mixed format)

**Valid formats:**
- `14:00 - 15:00` ✅
- `09:00 - 09:30` ✅
- `00:00 - 01:00` ✅ (midnight)

### Edge Case: Tasks from Other Notes

Tasks anywhere in vault with `⏳ 2025-11-16` will appear in Day Planner's Nov 16 timeline, even if not in the daily note. This is intentional - enables project notes to contribute to daily planning.

---

```
## Implementation Checklist

> [!important]+ Step-by-Step Setup Guide
> 
> Complete configuration process for the task capture system.

### Phase 1: Plugin Installation & Verification

- [ ] Install **Tasks** plugin (Community Plugins → Browse → "Tasks")
- [ ] Install **Dataview** plugin (required dependency)
- [ ] Install **Day Planner** (ivan-lednev version, not OG)
- [ ] Install **QuickAdd** plugin
- [ ] Enable **Daily Notes** core plugin
- [ ] Restart Obsidian to ensure all plugins loaded

### Phase 2: QuickAdd Configuration

1. **Create Capture Format:**
   - [ ] Open Settings → QuickAdd
   - [ ] Click "Manage Choices" → "Add Choice"
   - [ ] Name: `Quick Task Capture`
   - [ ] Type: **Capture**
   - [ ] Click gear icon ⚙️ to configure

2. **Configure Capture Settings:**
   - [ ] **Capture To:** `{{DATE:YYYY-MM-DD}}.md` (your daily note format)
   - [ ] **Capture Format:**
     ```markdown
     {{VALUE:Task description?}}{{VALUE: HH:MM - HH:MM (or leave blank)?}} ⏳ {{VDATE:Scheduled,YYYY-MM-DD|today}} {{VALUE:Due date (📅 YYYY-MM-DD) or blank?}} {{VALUE:Priority (⏫/🔼/🔽/⏬) or blank?}} 🔗 {{LINKCURRENT}}
     ```
   - [ ] **Insert After:** `## Tasks` (or your preferred heading)
   - [ ] **Insert At End:** OFF
   - [ ] **Create if not found:** ON

3. **Set Hotkey:**
   - [ ] Go to Settings → Hotkeys
   - [ ] Search "QuickAdd: Quick Task Capture"
   - [ ] Assign hotkey (suggestion: `Ctrl/Cmd + Shift + T`)

### Phase 3: Day Planner Configuration

- [ ] Open Settings → Day Planner
- [ ] **File Mode:** Command (not File or Dataview)
- [ ] **Dataview Source:** (leave blank for all vault)
- [ ] **Start Hour:** 00 (or your day start time)
- [ ] **End Hour:** 24 (or your day end time)
- [ ] **Timeline Zoom Level:** 60 (adjust to preference)
- [ ] **Show Completed:** ON (to see done tasks)
- [ ] **Colorful Timeline:** ON (optional visual enhancement)

### Phase 4: Testing Procedure

**Test 1: Simple Task**
- [ ] Create/open today's daily note
- [ ] Trigger QuickAdd hotkey
- [ ] Enter task: `Test simple task`
- [ ] Leave time block blank
- [ ] Accept default date (today)
- [ ] Leave due and priority blank
- [ ] Verify task appears with: `- [ ] Test simple task ⏳ [TODAY'S DATE] 🔗 [[TODAY'S DATE]]`

**Test 2: Time-Blocked Task**
- [ ] Trigger QuickAdd again
- [ ] Enter task: `Test time block`
- [ ] Enter time: `10:00 - 11:00`
- [ ] Accept default date
- [ ] Leave due and priority blank
- [ ] Open Day Planner timeline (Command Palette → "Day Planner: Show Timeline")
- [ ] Verify task appears at 10:00 AM in timeline

**Test 3: Dataview Query**
- [ ] Create new note for testing queries
- [ ] Add this query:
     ```dataview
     TASK
     WHERE scheduled = date(today)
     ```
- [ ] Verify both test tasks appear in results

**Test 4: Tasks Plugin Filter**
- [ ] Create Tasks query block:
     ```tasks
     not done
     scheduled today
     ```
- [ ] Verify test tasks appear

### Phase 5: Migration of Existing Tasks (Optional)

If you have existing tasks in daily notes:

- [ ] **Backup vault first**
- [ ] Use Find & Replace (Ctrl/Cmd + Shift + F) with regex:
  - Find: `- \[ \] (.+?) ➕ (\d{4}-\d{2}-\d{2})(.*)`
  - Replace: `- [ ] $1 ⏳ $2$3 🔗 [[FILENAME]]`
  - Review each match before replacing
- [ ] Manually add time blocks to time-sensitive existing tasks

> [!attention] Migration Caution
> 
> The above regex assumes your existing format matches `{{VALUE}} ➕ {{DATE}}` exactly. Test on a copy of one daily note first.

### Phase 6: Optional Enhancements

**Priority Suggester Macro:**
- [ ] Create QuickAdd Macro for priority selection
- [ ] Use QuickAdd API suggester to replace manual emoji entry
- [ ] Reduces typos in priority field

**Recurrence Template:**
- [ ] Create separate QuickAdd template: "Recurring Task"
- [ ] Add prompt: `{{VALUE:Recurrence pattern (e.g., every Monday)?}}`
- [ ] Format: `… 🔁 {{VALUE:pattern}} …`

**Custom Inline Fields:**
- [ ] Decide on additional metadata (e.g., `[energy:: high/low]`, `[context:: home/work]`)
- [ ] Add to capture format as `{{VALUE:field?}}`
- [ ] Update Dataview queries to leverage new fields

---
```

## Future Extension Points

> [!principle-point]+ Extensibility Architecture
> 
> The format is designed to accommodate growth without breaking existing tasks.

### 1. Custom Inline Fields

**Current format allows insertion anywhere:**
```markdown
- [ ] Task description [field:: value] 10:00 - 11:00 ⏳ 2025-11-16 📅 2025-11-20 ⏫ 🔗 [[2025-11-16]]
```

**Suggested extensions:**

| Field | Syntax | Use Case |
|-------|--------|----------|
| Energy level | `[energy:: high/low/medium]` | Match tasks to energy availability |
| Context | `[context:: @home/@work/@phone]` | GTD-style context filtering |
| Estimate | `[estimated:: 2h]` | Time budgeting |
| Assignee | `[assigned:: @person]` | Team task management |
| Project | `[project:: [[Project Name]]]` | Roll-up queries |

**Implementation:** Add VALUE prompts to QuickAdd format:
```markdown
… {{VALUE:Energy level (high/low/medium)?}} …
```

### 2. Integration with Other Plugins

**Full Calendar:**
- Tasks with `[date:: YYYY-MM-DD]` and `[startTime:: HH:MM]` appear in calendar
- Requires separate QuickAdd template or macro to add these fields

**Kanban:**
- Add `[status:: todo/doing/done]` inline field
- Dataview queries can then populate Kanban columns

**Tasks Plugin Auto-Suggest:**
- Enable "Auto-suggest" in Tasks settings
- Typing `📅` triggers date picker
- Reduces QuickAdd prompt count

### 3. Advanced Automation via QuickAdd Macros

**Macro Example: Smart Time Block Assignment**
```javascript
module.exports = async (params) => {
  const { quickAddApi } = params;
  const hour = new Date().getHours();
  
  // Suggest time block based on current time
  const suggestedStart = hour < 12 ? "09:00" : "14:00";
  const suggestedEnd = hour < 12 ? "10:00" : "15:00";
  
  const timeBlock = await quickAddApi.inputPrompt(
    `Time block (default: ${suggestedStart} - ${suggestedEnd})?`,
    `${suggestedStart} - ${suggestedEnd}`
  );
  
  return { timeBlock };
};
```

**Integration:** Reference macro variable in format:
```markdown
{{VALUE:Task?}} {{MACRO:Smart Time Block}} ⏳ …
```

### 4. Template Variations for Different Task Types

Create specialized QuickAdd templates:

**Meeting Template:**
```markdown
{{VALUE:Meeting title?}} {{VDATE:Date,YYYY-MM-DD|today}} {{VALUE:HH:MM - HH:MM?}} [attendees:: {{VALUE:Attendees?}}] ⏳ {{VDATE:Date}} 🔗 {{LINKCURRENT}}
```

**Email Follow-up Template:**
```markdown
Follow up with {{VALUE:Person?}} re: {{VALUE:Subject?}} [context:: @email] ⏳ {{VDATE:Follow-up date,YYYY-MM-DD|tomorrow}} 📅 {{VDATE:Deadline,YYYY-MM-DD}} 🔗 {{LINKCURRENT}}
```

**Reading Task Template:**
```markdown
Read: {{VALUE:Material?}} [pages:: {{VALUE:Pages?}}] [estimated:: {{VALUE:Duration?}}] ⏳ {{VDATE:Date,YYYY-MM-DD|today}} 🔗 {{LINKCURRENT}}
```

### 5. CSS Customization for Visual Priority

**Snippet to color-code priorities:**
```css
/* High priority tasks - red */
.task-list-item:has(li:contains("⏫")) {
  border-left: 3px solid #ff4444;
}

/* High priority - orange */
.task-list-item:has(li:contains("🔼")) {
  border-left: 3px solid #ff9944;
}

/* Low priority - blue */
.task-list-item:has(li:contains("🔽")) {
  border-left: 3px solid #4488ff;
}

/* Time blocks - bold */
.task-list-item li:contains("- ") {
  font-family: monospace;
  font-weight: 600;
}
```

### 6. Dataview Scripts for Advanced Queries

**Dynamic "Today's Focus" Dashboard:**
```dataviewjs
const today = dv.date("today");
const tasks = dv.pages()
  .file.tasks
  .where(t => !t.completed && t.scheduled?.equals(today));

const highPriority = tasks.where(t => t.text.includes("⏫"));
const timeBlocked = tasks.where(t => t.text.match(/\d{2}:\d{2} - \d{2}:\d{2}/));
const unscheduled = tasks.where(t => !t.text.match(/\d{2}:\d{2}/));

dv.header(2, "🔥 Today's Focus");
dv.taskList(highPriority, false);

dv.header(2, "📅 Time-Blocked");
dv.taskList(timeBlocked, false);

dv.header(2, "📋 To Schedule");
dv.taskList(unscheduled.limit(5), false);
```

---

# 🔗 Related Topics for PKB Expansion

1. **[[GTD Workflow in Obsidian]]**
   - *Connection*: Task capture is the first step of Getting Things Done methodology
   - *Depth Potential*: Complete GTD implementation using Obsidian's graph structure, including Inbox, Next Actions, Projects, and Review processes
   - *Knowledge Graph Role*: Links task management to broader productivity philosophy, connects to [[03-notes/01_permanent-notes/02_personal-knowledge-base/Personal Knowledge Management]] and [[Cognitive Offloading]]

2. **[[QuickAdd Macro Development]]**
   - *Connection*: Macros can enhance task capture with intelligent defaults and context-aware prompts
   - *Depth Potential*: Deep dive into QuickAdd JavaScript API, async operations, and vault manipulation for power users
   - *Knowledge Graph Role*: Technical skill development in [[JavaScript]], [[Obsidian API]], and [[Workflow Automation]]

3. **[[Dataview Query Language (DQL) Mastery]]**
   - *Connection*: Advanced queries unlock powerful task analytics and custom dashboards
   - *Depth Potential*: Complete DQL reference covering WHERE clauses, GROUP BY operations, functions, and DataviewJS for dynamic views
   - *Knowledge Graph Role*: Core technical skill for [[Obsidian Power Users]], connects to [[Data Analysis]] and [[Dashboard Design]]

4. **[[Time-Blocking Methodology]]**
   - *Connection*: Day Planner integration implements Cal Newport's time-blocking philosophy
   - *Depth Potential*: Explore time-blocking research, cognitive benefits, implementation strategies, and integration with [[deep work]] principles
   - *Knowledge Graph Role*: Productivity methodology connecting [[Attention Management]], [[Calendar Blocking]], and [[Task Prioritization]]

---

This comprehensive system provides a production-ready foundation for task management in Obsidian while remaining extensible for future enhancements. The format balances capture speed with metadata richness, ensuring that tasks serve as both actionable items and valuable data points in your Personal Knowledge Base.