---
title: "Plugin Reference: Day Planner"
id: 20251116-043038
type: reference
source: claude-4.5-sonnet
tags:
  - year/2025
  - status/seedling
  - productivity/time-management
  - productivity/time-management/blocking
  - productivity/task-management/todos
  - productivity/task-management/workflows
aliases:
  - Day Planner Plugin
  - Obsidian Timeboxing
  - Day Planner Guide
  - Time Block Planning
link-up: []
link-related: []
---


---

aliases: [Day Planner Plugin, Obsidian Timeboxing, Day Planner Guide, Time Block Planning]
---

> [!the-purpose]
> **This reference note provides comprehensive documentation for the Day Planner plugin in Obsidian—a powerful tool for timeboxing, task scheduling, and time tracking.** It covers installation, configuration, advanced features, and optimization strategies to help you use this plugin to its fullest potential for daily planning and productivity management.

---

## 📘 What is Day Planner?

**Day Planner** is a [[Community Plugin]] for [[obsidian]] that transforms your vault into a sophisticated time-management system through **timeboxing**—the practice of assigning specific time blocks to tasks rather than maintaining open-ended to-do lists. The plugin integrates editable calendar views, timeline visualizations, and basic time-tracking capabilities directly into your notes.

> [!core-principle]
> **The Philosophy of Timeboxing**
> 
> Timeboxing shifts you from task-oriented thinking ("*what* needs to be done") to time-oriented thinking ("*when* will I do this"). This approach:
> - Creates artificial scarcity that combats [[parkinson's law]]
> - Reduces decision fatigue by pre-committing to activities
> - Provides realistic constraints for estimating workload
> - Transforms abstract tasks into concrete time commitments

The plugin was originally created by James Lynch and has evolved through community contributions, with the modern version maintained by Ivan Lednev focusing on clean UI, simple task formats, and extensive calendar integration.

> [!warning]
> **Plugin Version Clarification**
> 
> There are **two distinct versions** in the Obsidian ecosystem:
> - **Day Planner** (modern, by Ivan Lednev) - Calendar integration, timeline views, time tracking
> - **Day Planner OG** (original fork, by Erin Schnabel) - Pomodoro-style time blocks, simpler interface
> 
> This note focuses on the **modern Day Planner** (Ivan Lednev's version), which offers more advanced features and active development.

---

## ⚙️ Prerequisites & Installation

### Required Dependencies

Before installing Day Planner, you **must** have these plugins enabled:

> [!definition]
> **Critical Dependencies**
> 
> 1. **[[Dataview Plugin]]** (community plugin) - REQUIRED
>    - Day Planner uses Dataview's query engine to discover tasks across your vault
>    - Without Dataview, the plugin will not function
> 
> 2. **[[Daily Notes]]** (core plugin) OR **[[Periodic Notes]]** (community plugin) - REQUIRED
>    - Provides the infrastructure for Day Planner to "see" and interact with daily notes
>    - At least one must be enabled for timeline functionality

### Installation Process

> [!methodology-and-sources]
> **Installation Steps**
> 
> 1. **Enable Prerequisites**
>    - Navigate to Settings → Core Plugins → Enable **Daily Notes**
>    - Navigate to Settings → Community Plugins → Browse → Search "Dataview" → Install & Enable
> 
> 2. **Install Day Planner**
>    - Settings → Community Plugins → Browse
>    - Search "Day Planner" (by Ivan Lednev)
>    - Click **Install** → Click **Enable**
> 
> 3. **Initial Configuration** (Optional but Recommended)
>    - Settings → Day Planner
>    - Review default settings (covered in detail in [[#Advanced Configuration]])

### First-Time Setup Checklist

After installation, verify your setup:

- [x] Dataview plugin is enabled  [completion:: 2025-11-16]
- [x] Daily Notes or Periodic Notes is enabled and configured  [completion:: 2025-11-16]
- [x] Day Planner plugin is installed and enabled  [completion:: 2025-11-16]
- [x] You can create a daily note successfully  [completion:: 2025-11-16]
- [x] Command Palette shows Day Planner commands (Cmd/Ctrl + P → search "Day Planner")  [completion:: 2025-11-16]

---

## 🎯 Core Functionality & Views

Day Planner provides three primary interfaces for interacting with your schedule, each serving distinct purposes in your workflow.

### 📊 Timeline View

The **Timeline View** is the heart of Day Planner—a vertical timeline that displays your scheduled tasks with a live indicator showing your current position in the day.

> [!how-to-use-this]
> **Opening the Timeline View**
> 
> - **Command Palette Method**: `Cmd/Ctrl + P` → Type "Show Timeline" → Enter
> - **Result**: Opens in your sidebar (typically right sidebar)
> - **Visual Features**:
>   - Red vertical line indicating current time
>   - Color-coded task blocks (can be customized)
>   - Drag-to-resize capability for time blocks
>   - Visual differentiation between task sources (daily notes, vault tasks, calendar events)

**Key Timeline Capabilities:**

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Live Time Indicator** | Red line tracks current time | Instantly see what you should be doing now |
| **Drag-and-Drop Editing** | Resize blocks by dragging borders | Quick adjustments without editing markdown |
| **Multi-Source Display** | Shows tasks from daily notes, Tasks plugin, and ICS calendars | Unified view of all commitments |
| **Zoom Control** | Adjust density of timeline | Customize detail level for your workflow |

> [!helpful-tip]
> **Timeline Density Optimization**
> 
> The Timeline Zoom Level setting (found in Day Planner settings) controls vertical space allocation:
> - **Low values (0.5-1.0)**: Condensed view, see more tasks at once, better for busy days
> - **High values (2.0-3.0)**: Spacious view, easier to read, better for fewer tasks
> 
> Experiment to find your preference—most users find 1.0-1.5 optimal.

### 📅 Week Planner View

The **Week Planner** provides a horizontal calendar view spanning seven days, enabling weekly planning and cross-day visualization.

> [!use-cases-and-examples]
> **Week Planner Strengths**
> 
> **Use it when you need to:**
> - Plan your entire week in advance
> - Identify scheduling conflicts across days
> - Batch similar tasks together
> - Balance workload distribution
> - Create time blocks without writing markdown syntax
> 
> **Example Workflow:**
> Sunday evening, open Week Planner → drag meetings from calendar → allocate focus blocks → identify gaps for deep work

**Week Planner Features:**

- **Visual Drag-and-Drop**: Create tasks by clicking and dragging on empty time slots
- **Cross-Day Overview**: See patterns in your weekly rhythm
- **Resize Interface**: Adjust time block duration by dragging edges
- **Direct Editing**: Double-click tasks to edit details inline

> [!insight]
> **Why Week Planner Excels for Planning**
> 
> While Timeline View is optimal for *executing* your day, Week Planner is superior for *designing* your week. The horizontal layout reveals weekly patterns that vertical timelines obscure—recurring meetings, unbalanced workloads, and strategic opportunities for deep work blocks.

### 📍 Status Bar Integration

The **Status Bar** (bottom of Obsidian window) displays a compact summary of your current task and progress.

> [!what-this-does]
> **Status Bar Display Options**
> 
> Configurable elements (Settings → Day Planner):
> 
> 1. **Current Task Name**: Shows what you should be doing right now
> 2. **Progress Indicator**: Visual gauge of time remaining in current block
> 3. **Next Task Preview**: Displays upcoming task
> 4. **Mini-Timeline** (optional): 3-hour preview of upcoming blocks
> 
> **Clicking the status bar** instantly navigates to your daily note.

> [!principle-point]
> **The Power of Ambient Awareness**
> 
> Status bar integration creates *peripheral accountability*—you don't need to actively check your schedule because it's always visible. This reduces task-switching overhead and keeps you anchored to your plan without conscious effort.

**Mini-Timeline Feature:**

The mini-timeline (enable in settings) condenses your next 3 hours into the status bar:

```
[Current Task: Write report] ⏱️ 25m → 🔍Review → 📞Meeting
```

This provides just-in-time awareness of what's ahead without requiring you to open views.

---

## ✍️ Task Syntax & Formatting

Day Planner supports multiple task formats, allowing integration with various workflows and plugins. Understanding these formats is crucial for optimal usage.

### Format 1: Daily Note Inline Time Blocks

The **primary format** for Day Planner—simple, human-readable time blocks within daily notes.

> [!definition]
> **Inline Time Block Syntax**
> 
> ```markdown
> # Day planner
> - [ ] 08:00 - 09:00 Morning routine
> - [ ] 09:00 - 10:30 Deep work: Project X
> - [ ] 10:30 - 11:00 Coffee break
> - [ ] 11:00 - 12:30 Team meeting
> ```
> 
> **Syntax Rules:**
> - **Checkbox required**: `- [ ]` (unchecked) or `- [x]` (checked)
> - **Time format**: `HH:mm` (24-hour format required)
> - **Time range**: `HH:mm - HH:mm` (start - end)
> - **Description**: Any text after the time range
> - **Header required**: Tasks must appear under a heading (default: `# Day planner`, configurable)

**Advanced Inline Features:**

```markdown
# Day planner

## Morning Block
- [ ] 07:00 - 07:30 Wake up and stretch
  - Sub-task: Set intentions for the day
  - Sub-task: Review calendar

## Work Block  
- [ ] 09:00 - 11:00 [[Project Apollo]] - Phase 2 implementation
  - Link to project note for context
  - Integration with other notes via [[Wiki-Links]]

## Afternoon
- [ ] 13:00 - 14:30 Client meeting: Q4 strategy #meetings
  - Tags work for filtering and organization
```

> [!helpful-tip]
> **Sub-Tasks and Nested Content**
> 
> You can add nested content under timed tasks for context:
> - Sub-tasks (also checkboxes but indented)
> - Notes and details (regular bullets)
> - Links to relevant notes
> - Tags for organization
> 
> **Day Planner ignores nested items** for timeline display but preserves them in your note for reference.

### Format 2: Tasks Plugin Integration (Vault-Wide Discovery)

Day Planner integrates with the [[Tasks Plugin]], allowing tasks anywhere in your vault to appear in timelines if they have scheduled dates.

> [!connection-ideas]
> **Tasks Plugin Synergy**
> 
> The Tasks plugin provides sophisticated task management (due dates, recurrence, filtering). When combined with Day Planner, you get:
> - Tasks scattered across project notes appear in your timeline
> - No need to manually copy tasks to daily notes
> - Tasks plugin's modal for quick date entry
> - Automatic scheduling of recurring tasks

**Tasks Plugin Syntax Options:**

Day Planner recognizes three Tasks plugin formats:

```markdown
1. Emoji Shorthand (Tasks plugin default)
- [ ] 08:00 - 10:00 Code review ⏳ 2025-11-16

2. Dataview Property (Inline)
- [ ] 11:00 - 13:00 Workshop preparation [scheduled:: 2025-11-16]

3. Dataview Property (Parentheses)
- [ ] 14:00 - 15:30 Client call (scheduled:: 2025-11-16)
```

> [!important]
> **Emoji Format Limitation**
> 
> While the Tasks plugin supports emoji-based date notation (⏳ for scheduled, 📅 for due, ✅ for done), Day Planner currently has **inconsistent support** for the shorthand emoji syntax (⌛ and ⏳).
> 
> **Recommendation**: Use Dataview property format `[scheduled:: YYYY-MM-DD]` for most reliable recognition.

**Vault-Wide Task Discovery:**

By default (as of recent versions), Day Planner automatically searches your entire vault for tasks with scheduled properties—**no Dataview query configuration required**.

> [!what-this-does]
> **How Automatic Discovery Works**
> 
> 1. Day Planner scans all markdown files in your vault
> 2. Identifies tasks with scheduled date properties
> 3. Filters tasks matching today's date (or the date of the daily note you're viewing)
> 4. Displays them in the timeline alongside daily note tasks
> 5. Color-codes them differently (remote tasks vs. local tasks)

### Format 3: Calendar Event Syntax (ICS Integration)

External calendar events from [[Google Calendar]], [[iCloud Calendar]], or [[Outlook]] appear in the timeline through ICS feed integration.

**Calendar events display characteristics:**

- **Read-only**: Cannot be edited from within Obsidian
- **Distinct color coding**: Visually differentiated from tasks
- **Full event details**: Title, time, location (if provided)
- **Automatic refresh**: Updates based on plugin settings

> [!example]
> **Mixed-Source Timeline**
> 
> Your 2 PM-4 PM timeline might show:
> - **Green block** (daily note task): "Focus: Write quarterly report" 
> - **Blue block** (Google Calendar): "Client Meeting - Conference Room B"
> - **Yellow block** (vault task from project note): "[[Project Phoenix]] - Code review"
> 
> All three sources unified in one view.

### Visual Differentiation & Color Codi

Day Planner uses color to distinguish between task sources:

| Source Type | Default Color | Meaning | Editable in Obsidian? |
|-------------|---------------|---------|----------------------|
| Daily Note Tasks | Primary theme color | Tasks in today's daily note | Yes (edit markdown) |
| Remote Vault Tasks | Secondary color | Tasks from other notes with scheduled dates | Yes (edit source note) |
| ICS Calendar Events | Accent color | External calendar events | No (edit in calendar app) |
| Time Tracking Clocks | Distinct color | Recorded time blocks | View only |

> [!helpful-tip]
> **Enabling Colorful Timeline**
> 
> By default, the timeline might look monochrome. Enable "Colorful Timeline" in Day Planner settings to activate visual differentiation. This significantly improves scanability and source recognition.

---

## 🔗 Calendar Integration (ICS Feeds)

One of Day Planner's most powerful features is seamless integration with external calendars through **ICS (iCalendar) feeds**—bringing meetings, appointments, and events directly into your Obsidian timeline.

### Why Calendar Integration Matters

> [!core-principle]
> **The Unified Schedule Principle**
> 
> Productivity systems fail when you must maintain multiple sources of truth. Calendar integration means:
> - **No manual duplication**: Meetings automatically appear in Obsidian
> - **Single planning interface**: See appointments and tasks together
> - **Context-aware scheduling**: Plan tasks around fixed commitments
> - **Reduced cognitive load**: One place to check your day

### Setting Up ICS Integration

All calendar integration happens through ICS (Internet Calendar Subscription) links—shareable URLs that provide read-only access to calendar data.

> [!methodology-and-sources]
> **Universal ICS Setup Process**
> 
> 1. **Obtain ICS link** from your calendar service (instructions below)
> 2. **Add to Day Planner**:
>    - Settings → Day Planner → Calendars section
>    - Click "+" to add new calendar
>    - Paste ICS URL
>    - Assign a name (for identification)
> 3. **Verify**: Check Timeline View to confirm events appear
> 4. **Repeat**: Add multiple calendars if needed (work, personal, family, etc.)

### 📆 Google Calendar Integration

**Obtaining the ICS Link:**

1. Open [Google Calendar](https://calendar.google.com) (web version)
2. **Left sidebar** → Find the calendar you want to integrate
3. **Click the three dots** (⋮) next to the calendar name
4. **Select "Settings and sharing"**
5. **Scroll down** to "Integrate calendar" section
6. **Copy** the "Secret address in iCal format" (ends with `.ics`)

> [!warning]
> **Security Consideration**
> 
> The "Secret address" URL provides **read access** to your calendar. Google warns against sharing this URL because anyone with it can view your calendar events. Treat it like a password:
> - Store securely in Obsidian settings (not in public notes)
> - Don't share your vault folder publicly without removing ICS URLs
> - Regenerate the URL if accidentally exposed (Google Calendar settings)

**Google Calendar-Specific Notes:**

- **Multiple calendars**: Repeat the process for each Google Calendar you want to integrate (work, personal, etc.)
- **Shared calendars**: You can add ICS links for calendars others have shared with you
- **Refresh rate**: Day Planner typically checks for updates every 15-30 minutes (configurable)

### 🍎 iCloud Calendar Integration

**Obtaining the ICS Link:**

1. Open [iCloud.com](https://www.icloud.com) → Calendar
2. **Click the share icon** (radio waves symbol) next to the calendar name
3. **Enable "Public Calendar"**
4. **Copy the public calendar link**
5. **Modify the URL**: Change `webcal://` to `https://` if present

**Alternative Method (iOS/macOS Calendar App):**

1. Open Calendar app
2. Right-click calendar name → **Share Calendar**
3. Enable **Public Calendar**
4. Copy the link provided

> [!attention]
> **iCloud Public Calendar Limitation**
> 
> iCloud requires making calendars **public** to generate ICS links. This means:
> - Events become viewable by anyone with the link
> - Consider creating a separate "Public Events" calendar for Obsidian integration
> - Keep sensitive appointments in a non-integrated private calendar

### 🏢 Microsoft Outlook / Office 365 Integration

Outlook integration is more complex due to organizational security policies. There are two primary methods:

**Method 1: Outlook.com (Personal Accounts)**

1. Open [Outlook on the web](https://outlook.live.com)
2. Settings (gear icon) → **View all Outlook settings**
3. **Calendar** → **Shared calendars**
4. Under "Publish a calendar":
   - Select the calendar
   - Choose permission level
   - **Copy the ICS link**

**Method 2: Office 365 / Outlook Web App (Work Accounts)**

1. Open Outlook on the web (your organization's URL)
2. Click **Settings** (gear icon)
3. **Calendar** → **Shared calendars**  
4. Select calendar and permissions
5. **Publish calendar** → Copy ICS link

> [!warning]
> **Office 365 Restrictions**
> 
> Many organizations **disable calendar publishing** for security reasons. If you don't see the "Publish calendar" option:
> - Your IT department has restricted this feature
> - You'll need to request permission or use alternative methods
> - Consider using the workaround described below

**Office 365 Alternative Workaround** (from community):

For work accounts where standard publishing is disabled:

```
https://outlook.office365.com/owa/calendar/<CALENDAR_TOKEN>/reachcalendar.ics
```

1. Navigate to Calendar → Right-click your calendar → **Properties**
2. The URL bar will contain a token (long alphanumeric string)
3. Extract this token and use it in the format above
4. **Note**: This method may violate IT policies—check with your administrator

> [!helpful-tip]
> **Testing Your ICS Link**
> 
> Before adding to Day Planner, verify your ICS link works:
> 1. Paste the URL into a web browser
> 2. You should see a download prompt or plain text calendar data
> 3. If you get an error or login page, the link isn't properly configured

### Managing Multiple Calendars

Day Planner supports **multiple ICS feeds** simultaneously—essential for work/life separation or family coordination.

**Multi-Calendar Strategy:**

| Calendar Type | Example Use | Color Coding Strategy |
|---------------|-------------|----------------------|
| **Work Calendar** | Meetings, deadlines, work events | Primary/red blocks |
| **Personal Calendar** | Appointments, personal commitments | Secondary/blue blocks |
| **Family Calendar** | Kids' activities, household events | Accent/green blocks |
| **Project-Specific** | Event-driven projects | Custom colors |

> [!use-cases-and-examples]
> **Multi-Calendar Workflow Example**
> 
> **User Profile**: Freelance developer with consulting clients
> 
> **Calendar Setup**:
> 1. **Client A Calendar** (Google) → Red blocks
> 2. **Client B Calendar** (Google) → Orange blocks  
> 3. **Personal Calendar** (iCloud) → Blue blocks
> 4. **Daily note tasks** → Green blocks
> 
> **Result**: Timeline instantly reveals schedule conflicts between clients and personal boundaries become visible, preventing overcommitment.

### Troubleshooting Calendar Integration

**Common Issues & Solutions:**

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Events not appearing | Invalid ICS URL | Verify URL works in browser; check for `.ics` ending |
| Events delayed/outdated | Refresh interval too long | Settings → Increase refresh frequency |
| Permission errors | Calendar not public/published | Verify sharing settings in calendar service |
| Outlook events missing | IT policy restrictions | Use alternative method or request admin assistance |
| Too many events | Pulled wrong calendar | Verify you copied the correct calendar's ICS link |

> [!constraints-and-pitfalls]
> **ICS Integration Limitations**
> 
> **What ICS CAN do:**
> ✅ Display event title, time, location
> ✅ Show multiple calendars simultaneously  
> ✅ Update automatically (based on refresh interval)
> 
> **What ICS CANNOT do:**
> ❌ Edit calendar events from Obsidian (read-only)
> ❌ Create new calendar events
> ❌ Sync completed task status back to calendar
> ❌ Access private/authentication-required calendars
> 
> **Workaround**: For two-way sync, consider complementary plugins like [[iCal Plugin]] or [[Morgen Tasks]].

---

## ⏱️ Time Tracking System

Beyond scheduling, Day Planner includes **time tracking** functionality—recording actual time spent on tasks through a manual "clock" system.

### Understanding Time Tracking vs. Time Planning

> [!analogy]
> **Planned Time vs. Actual Time**
> 
> Think of Day Planner as having two layers:
> 
> **Planning Layer** (green timeline blocks):
> - *Intent*: "I plan to work on this from 2-4 PM"
> - Shows your schedule
> - Created by writing time blocks in notes
> 
> **Tracking Layer** (distinct color timeline blocks):
> - *Reality*: "I actually worked on this from 2:15-3:45 PM"
> - Shows what happened
> - Created by starting/stopping clocks
> 
> Over time, comparing these layers reveals planning accuracy and helps you estimate better.

### How Clock Recording Works

Day Planner's time tracking uses **Dataview properties** to store start/stop timestamps, which are then visualized as timeline blocks.

> [!methodology-and-sources]
> **Time Tracking Workflow**
> 
> **Starting a Clock:**
> 1. Right-click on any task in the editor
> 2. Select **"Start clock"** from context menu
>    - *Alternative*: Use command palette (`Cmd/Ctrl + P` → "Start clock")
>    - *Alternative*: Assign a hotkey in Settings → Hotkeys
> 3. Task is now "clocked in"
> 4. Active clock appears in timeline sidebar
> 
> **Stopping a Clock:**
> 1. Right-click on the same task (or any task if only one clock active)
> 2. Select **"Stop clock"**
>    - *Alternative*: Right-click the active clock in timeline sidebar → "Stop clock"
> 3. Dataview properties are written to the task
> 
> **Canceling a Clock:**
> - Right-click active clock → "Cancel clock"
> - Discards the timing data without saving

### Clock Data Storage

When you stop a clock, Day Planner adds **Dataview inline properties** to your task:

```markdown
- [x] 09:00 - 11:00 Deep work: Write documentation [clock-in:: 2025-11-16T09:12:00] [clock-out:: 2025-11-16T10:48:00]
```

**Property Breakdown:**

| Property | Format | Meaning |
|----------|--------|---------|
| `[clock-in:: ...]` | ISO 8601 timestamp | When you started the clock |
| `[clock-out:: ...]` | ISO 8601 timestamp | When you stopped the clock |
| Checkbox `[x]` | Often auto-marked | Task completion (optional) |

> [!what-this-does]
> **Why Dataview Properties?**
> 
> Storing timing data as Dataview properties means:
> - **Queryable**: Use Dataview to analyze time spent (total hours per project, weekly summaries)
> - **Portable**: Data lives in plain text, not a database
> - **Flexible**: Can be manually edited if you forgot to start/stop timer
> - **Compatible**: Works with other plugins that read Dataview properties

### Visualizing Tracked Time

Day Planner provides two ways to see recorded time:

**1. Timeline Column View**

Enable "Show clocks in timeline" (Settings → Day Planner → Time Tracking):

```
┌─────────────────┬─────────────────┐
│  Planned Tasks  │  Tracked Time   │
├─────────────────┼─────────────────┤
│ 09:00-11:00    │ ██████████      │ ← Visual comparison
│ Deep Work       │ 09:12-10:48     │
│                 │ (1h 36m)        │
├─────────────────┼─────────────────┤
│ 11:00-12:30    │ ███████         │
│ Meeting         │ 11:05-12:15     │
│                 │ (1h 10m)        │
└─────────────────┴─────────────────┘
```

This dual-column view reveals:
- Tasks that took longer than planned (overruns)
- Tasks completed faster than planned (efficiency)
- Gaps between planned and actual (context switching)

**2. Active Clock Sidebar**

While a clock is running, the **Timeline sidebar** shows:

- **Current task name**
- **Elapsed time** (updates in real-time)
- **Start time**
- **Stop/Cancel controls**

> [!helpful-tip]
> **Using Active Clock Display**
> 
> The active clock indicator serves as:
> - **Accountability mechanism**: Visible reminder you're "on the clock"
> - **Time awareness**: See exactly how long you've been on current task
> - **Focus aid**: Similar to Pomodoro timer, creates time-bounded focus sessions

### Analyzing Tracked Time (Dataview Integration)

The real power of clock data emerges when you query it with [[dataview]]:

**Example Dataview Queries:**

```dataview
TABLE
  file.name as "2025-11-16",
  round((clock-out - clock-in).hours, 2) as "Hours"
FROM ""
WHERE clock-in
AND dateformat(clock-in, "yyyy-MM-dd") = dateformat(date(today), "yyyy-MM-dd")
SORT clock-in ASC
```

This query shows all tasks you tracked today with time spent.

**Advanced Time Tracking Query** (Weekly Summary):

```dataview
TABLE WITHOUT ID
  project as "Project",
  sum(rows.hours) as "Total Hours"
FROM ""
WHERE clock-in
AND dateformat(clock-in, "yyyy-MM-dd") >= dateformat(date(today) - dur(7 days), "yyyy-MM-dd")
FLATTEN round((clock-out - clock-in).hours, 2) as hours
GROUP BY project
SORT sum(rows.hours) DESC
```

Shows total hours per project over the last 7 days.

> [!use-cases-and-examples]
> **Time Tracking Use Cases**
> 
> **Freelancers & Consultants:**
> - Track billable hours per client
> - Generate timesheets from Dataview queries
> - Identify most time-consuming projects
> 
> **Researchers & Students:**
> - Measure time spent on different research tasks
> - Optimize study schedule based on actual focus time
> - Track pomodoro-style work sessions
> 
> **Personal Productivity:**
> - Compare planned vs. actual time for better estimation
> - Identify time-wasting patterns
> - Build awareness of focus capacity

### Time Tracking Limitations

> [!constraints-and-pitfalls]
> **Current Time Tracking Limitations**
> 
> **What you CAN do:**
> ✅ Start/stop clocks manually on tasks
> ✅ View active clock in timeline
> ✅ See tracked time as timeline blocks
> ✅ Query clock data with Dataview
> 
> **What you CANNOT do (yet):**
> ❌ **Edit clock blocks directly** in timeline (read-only visualization)
> ❌ **Auto-start clocks** based on time (no automation)
> ❌ **Pause/resume** clocks (must stop and start new clock)
> ❌ **Track multiple simultaneous tasks** (one active clock at a time)
> ❌ **Set clock reminders** ("you've been working for 2 hours")
> 
> **Workarounds:**
> - For simultaneous tracking, use complementary plugins like [[Obsidian Simple Time Tracker]]
> - For pomodoro reminders, use [[PomoBar Plugin]]
> - For clock editing, manually adjust Dataview properties in markdown

> [!important]
> **Experimental Feature Notice**
> 
> Time tracking is marked as **experimental** by the plugin developer. This means:
> - Features may change in future updates
> - Some edge cases may not be handled perfectly
> - Community feedback is actively shaping development
> 
> If you rely heavily on time tracking, consider keeping notes backed up and be prepared for potential changes to the tracking interface.

---

## 🎨 Advanced Features & Customization

Beyond core functionality, Day Planner offers extensive customization to match your workflow preferences and visual aesthetics.

### Drag-and-Drop Task Editing

Both Timeline and Week Planner views support **direct manipulation** of time blocks without touching markdown.

**Drag-and-Drop Capabilities:**

| Action | How To | Result |
|--------|--------|--------|
| **Resize duration** | Drag top or bottom edge of task block | Changes end time in markdown |
| **Move time slot** | Drag entire task block up/down | Changes start time in markdown |
| **Create new task** | Click and drag on empty timeline space | Creates new task block (Week Planner) |
| **Rearrange order** | Drag task to new position | Updates task sequence in note |

> [!helpful-tip]
> **When to Use Drag vs. Markdown**
> 
> **Use drag-and-drop for:**
> - Quick time adjustments during the day
> - Visual experimentation with schedule
> - Rapid rescheduling when plans change
> 
> **Use markdown editing for:**
> - Adding detailed task descriptions
> - Adding wiki-links or tags
> - Bulk creation of many tasks
> - Template-based planning

### Desktop Notifications

Day Planner can send **native OS notifications** when tasks are about to start or switch.

> [!how-to-use-this]
> **Notification Settings**
> 
> **Enable notifications:**
> 1. Settings → Day Planner → Notifications section
> 2. Toggle "Show notifications" ON
> 3. Configure timing:
>    - "Minutes before task" (e.g., 5 minutes warning)
>    - "Show notification at task start time"
> 
> **Notification Types:**
> - **Upcoming task**: "In 5 minutes: Team Meeting"
> - **Task starting**: "Now: Deep Work Session"
> - **Task ending**: "Task complete: Move to next activity"

**Notification Behavior:**

- **Desktop only**: Notifications work on desktop Obsidian only (Windows, macOS, Linux)
- **Mobile limitation**: Obsidian mobile doesn't support native notifications
- **Requires Obsidian focus**: Some OSes only show notifications when Obsidian is running (check your system notification settings)

> [!use-cases-and-examples]
> **Notification Use Case: Context Switching**
> 
> **Problem**: You get hyperfocused and lose track of time, missing meetings.
> 
> **Solution**: Enable 5-minute warning notifications. When you're in deep work, a gentle reminder gives you time to wrap up current thought before the next commitment.
> 
> **Pro tip**: Combine with [[Do Not Disturb]] mode during focus blocks to prevent other interruptions while still receiving Day Planner transition alerts.

### Timeline Zoom & Density Control

The **Timeline Zoom Level** setting adjusts how much vertical space each hour occupies.

**Zoom Level Effects:**

```
┌──────────────────────────────────────┐
│ Zoom Level: 0.5 (Condensed)          │
├──────────────────────────────────────┤
│ 08:00 ▂▂▂ Morning Routine           │
│ 09:00 ▄▄▄ Deep Work                 │
│ 11:00 ▂▂▂ Break                     │
│ 11:30 ▄▄▄▄▄ Meeting                 │  ← More tasks visible
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ Zoom Level: 2.0 (Spacious)           │
├──────────────────────────────────────┤
│                                       │
│ 08:00 ████████                        │
│       Morning Routine                 │
│                                       │
│ 09:00 ████████████████                │
│       Deep Work                       │  ← Easier to read
│                                       │
│ 11:00 ████                            │
│       Break                           │
└──────────────────────────────────────┘
```

> [!principle-point]
> **Density vs. Context Trade-off**
> 
> **Low zoom** (condensed) = More context, see full day at once
> **High zoom** (spacious) = Less scrolling needed for current task, easier reading
> 
> Most users find **1.0-1.5** balances both needs. Experiment based on:
> - Screen size (larger screens → can go more spacious)
> - Number of daily tasks (busy days → more condensed)
> - Visual preference (some people prefer information density, others find it overwhelming)

### Colorful Timeline Option

By default, Day Planner timelines can appear monochrome. The **Colorful Timeline** setting adds visual differentiation.

**Enabling Color:**

1. Settings → Day Planner → Display section
2. Toggle "Colorful Timeline" ON
3. Task blocks now use color to indicate source

**Color Scheme** (typical, may vary by theme):

- **Daily Note Tasks**: Theme primary color (often blue/green)
- **Vault Tasks** (from Tasks plugin): Secondary color (often purple/orange)
- **Calendar Events**: Accent color (often red/yellow)
- **Tracked Time**: Distinct color (often gray/teal)

> [!helpful-tip]
> **Custom Color Schemes**
> 
> While Day Planner doesn't provide built-in color customization, you can modify colors through:
> - **CSS Snippets**: Override plugin CSS classes
> - **Theme Selection**: Different Obsidian themes render Day Planner colors differently
> - **Accessibility**: If you have color vision deficiency, consider themes with pattern differentiation (stripes, dots) rather than color alone

### Status Bar Customization

Fine-tune what information appears in the status bar:

**Available Status Bar Elements:**

| Element | Description | When to Enable |
|---------|-------------|----------------|
| **Current Task Name** | Shows active task | Always (core feature) |
| **Progress Bar** | Visual time remaining | If you like visual feedback |
| **Time Remaining** | Text countdown (e.g., "25m") | If you prefer specific numbers |
| **Next Task Preview** | Upcoming task name | For planning context switches |
| **Mini-Timeline** | 3-hour preview | If you have status bar space |

> [!ask-yourself-this]
> **What Status Bar Configuration Works for You?**
> 
> Consider your working style:
> - **Minimalist**: Task name only, avoid clutter
> - **Visual Learner**: Progress bar helps perceive time
> - **Planner**: Next task preview reduces surprises
> - **Information Dense**: All elements (if screen space allows)

### Command Palette Shortcuts

Day Planner integrates deeply with Obsidian's [[Command Palette]]—access all features quickly without mouse:

**Essential Commands:**

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `Show Timeline` | Opens timeline in sidebar | Start of day, need current view |
| `Show Week Planner` | Opens week planner view | Weekly planning sessions |
| `Start clock` | Begins time tracking | Starting a task |
| `Stop clock` | Ends time tracking | Finishing a task |
| `Add Day Planner for today` | Inserts template in note | Setting up new daily note |

> [!helpful-tip]
> **Custom Hotkeys for Speed**
> 
> Assign keyboard shortcuts to frequently-used commands:
> 
> 1. Settings → Hotkeys
> 2. Search "Day Planner"
> 3. Click on command → Press key combination
> 
> **Suggested Hotkeys:**
> - `Cmd/Ctrl + Shift + T`: Show Timeline
> - `Cmd/Ctrl + Shift + K`: Start/Stop Clock (toggle)
> - `Cmd/Ctrl + Shift + W`: Show Week Planner

---

## 🔧 Workflows & Best Practices

Effective use of Day Planner goes beyond understanding features—it requires developing intentional workflows that support your goals.

### Morning Planning Routine

A consistent **morning planning ritual** sets up Day Planner for success.

> [!methodology-and-sources]
> **Recommended Morning Workflow**
> 
> **Time Required**: 10-15 minutes
> 
> **Steps:**
> 
> 1. **Open Today's Daily Note** (`Cmd/Ctrl + T` if you have Daily Notes hotkey)
> 
> 2. **Review External Commitments**
>    - Open Week Planner or Timeline
>    - Check calendar events (meetings, appointments) that auto-populated
>    - Note any scheduling conflicts
> 
> 3. **Time-Box Priority Tasks**
>    - Identify your [[Most Important Task]] (MIT) for the day
>    - Assign it a time block (preferably morning, during peak energy)
>    - Add 2-3 secondary priority tasks
> 
> 4. **Fill Around Fixed Points**
>    - Meetings are immovable—treat them as anchors
>    - Schedule tasks in gaps between meetings
>    - Buffer time: add 10-15 minute breaks between blocks
> 
> 5. **Reality Check**
>    - Total your committed time
>    - Is it less than your available work hours?
>    - If overcommitted, ruthlessly cut or defer tasks
> 
> 6. **Add Context & Links**
>    - Link tasks to project notes: `[[Project X]] - Implementation`
>    - Add tags for later filtering: `#deep-work` `#meetings` `#admin`
>    - Include sub-tasks or notes for context

**Example Morning Plan:**

```markdown
# Day planner

## Morning Focus Block
- [ ] 07:00 - 07:30 Morning routine (exercise, breakfast)
- [ ] 07:30 - 08:00 Review email, plan day
- [ ] 08:00 - 10:30 🎯 MIT: [[Project Apollo]] - Complete phase 2 architecture #deep-work
  - Focus: No interruptions, phone on DND
  - Goal: Finish data model design
  - Links: [[System Architecture Doc]], [[Technical Requirements]]

## Meeting Block  
- [ ] 10:30 - 11:00 Coffee & email triage
- [ ] 11:00 - 12:00 Team standup (from Google Calendar)

## Afternoon Execution
- [ ] 13:00 - 14:00 Lunch & walk
- [ ] 14:00 - 15:30 [[Project Beta]] - Code review #collaboration
- [ ] 15:30 - 16:00 Admin: Expense reports, timesheets #admin
- [ ] 16:00 - 17:00 Client email responses #communication

## Evening Wind-Down
- [ ] 17:00 - 17:30 Plan tomorrow, review today's progress
```

> [!principle-point]
> **Front-Load Cognitive Work**
> 
> Day Planner makes **chronological energy management** visible. Notice the example places:
> - **Deep work** (architecture design) early morning (peak cognitive hours)
> - **Collaborative work** (code review) post-lunch (moderate energy)
> - **Administrative tasks** late afternoon (low energy tolerance)
> 
> This aligns [[Circadian Rhythms]] with task demands.

### Integration with External Task Managers

Many users combine Day Planner with dedicated task managers ([[Things 3]], [[Todoist]], [[Wrike]], etc.) rather than replacing them.

> [!use-cases-and-examples]
> **Two-System Workflow Pattern**
> 
> **Task Manager Role** (Things 3, Todoist, etc.):
> - **Master task repository**: All tasks, projects, someday/maybe items
> - **Capture inbox**: Quick capture from phone/anywhere
> - **Project management**: Hierarchical task breakdown
> - **Recurring tasks**: Sophisticated repeat patterns
> 
> **Day Planner Role** (Obsidian):
> - **Daily commitment**: Which tasks happen *today*
> - **Time allocation**: *When* tasks happen
> - **Context layer**: Links to notes, research, documentation
> - **Reflection space**: Capture thoughts during task execution
> 
> **Daily Bridge Workflow**:
> 1. Morning: Review task manager for due/priority items
> 2. Decide: "Which 3-5 tasks will I do TODAY?"
> 3. Time-box: Assign those tasks to specific time blocks in Day Planner
> 4. Execute: Work from Day Planner timeline throughout day
> 5. Evening: Mark tasks complete in task manager, update progress

This workflow leverages the strengths of both tools—sophisticated task management AND time-bound daily planning.

**User Example** (Curtis McHale's workflow):

From research: Curtis uses Day Planner alongside [[Wrike]] (team project management) and Things3 (personal tasks):

- **Morning**: Surveys Wrike for team deadlines, Things3 for personal tasks, and Google Calendar for meetings
- **Planning**: Transfers selected tasks into Day Planner time blocks
- **Execution**: Works solely from Day Planner timeline
- **Context**: Meetings in daily notes include agenda items and action items
- **Decision Delays**: Uses daily notes to capture thoughts for future discussions (e.g., issues to discuss with CEO) rather than immediately addressing—builds in reflection time

> [!insight]
> **Why Not Replace Task Managers Entirely?**
> 
> Day Planner is intentionally **planning-focused**, not **task-management-complete**:
> - No sophisticated filters or queries for tasks (Day Planner is for today)
> - No mobile quick-capture (Obsidian mobile less frictionless than task apps)
> - No sharing/collaboration (Obsidian is personal workspace)
> - No recurring task automation (must manually create each day)
> 
> Think of Day Planner as the "execution layer" on top of your task management "strategy layer."

### Meeting Note Preparation

Day Planner excels at preparing for and documenting meetings through its integration with [[Daily Notes]].

**Pre-Meeting Workflow:**

1. **Calendar Event Appears**: Meeting auto-populates from ICS feed
2. **Create Context**: Below the meeting time block in daily note, add:

```markdown
- [ ] 14:00 - 15:00 Q4 Strategy Meeting (from calendar)
  
  **Meeting Context:**
  - [[Q4 Strategy Document]] - Review before meeting
  - [[Previous Q3 Retrospective]] - Reference last quarter's learnings
  
  **My Agenda Items:**
  - [ ] Discuss budget allocation for new initiative
  - [ ] Clarify timeline for product launch
  - [ ] Get decision on hiring for design role
  
  **Questions to Ask:**
  - What are success metrics for Q4?
  - Who owns the go-to-market strategy?
```

3. **During Meeting**: Take notes directly under the context (daily note stays open)
4. **Post-Meeting**: Extract action items as new tasks

**Post-Meeting Task Extraction:**

```markdown
- [x] 14:00 - 15:00 Q4 Strategy Meeting ✅ Complete
  
  **Key Decisions:**
  - Budget approved for new initiative: $50K
  - Product launch target: March 15
  - Design role approved for Q1 hire
  
  **Action Items:**
  - [ ] [[Follow-Up Task]]: Draft job description for designer ⏳ 2025-11-20
  - [ ] [[Follow-Up Task]]: Create project brief for new initiative ⏳ 2025-11-18
```

> [!helpful-tip]
> **The "Meeting Stack" Pattern**
> 
> For users with meeting-heavy days:
> 
> Create a **consistent meeting note structure** in your daily note template:
> - **Before**: Context, agenda, questions
> - **During**: Real-time notes  
> - **After**: Decisions, action items (with scheduled dates for vault-wide discovery)
> 
> This pattern ensures:
> - You're prepared (reviewed context)
> - You capture value (notes during)
> - You follow through (action items as schedulable tasks)

### Focus Session Scheduling


> [!definition]
> **Focus Session (Deep Work Block)**
> 
> A focus session is:
> - **Time-bounded**: Fixed start and end (creates urgency)
> - **Single-task**: One project/activity only (prevents context switching)
> - **Protected**: Minimal interruptions (notifications off, colleagues aware)
> - **Intentional**: Clear outcome defined (not just "work on X")

**Focus Session Best Practices:**

| Principle | Implementation | Rationale |
|-----------|----------------|-----------|
| **90-minute max** | Break deep work into 60-90 min blocks | Cognitive capacity limit |
| **Clear outcome** | "Draft section 3" not "work on paper" | Concrete target aids focus |
| **Pre-session prep** | Materials ready, know next step | Reduces activation energy |
| **Break between sessions** | 10-15 min walk/stretch | Mental reset, prevents burnout |
| **Post-session capture** | 5-min reflection note | Captures insights, plans next session |

**Example Focus Session Time Block:**

```markdown
- [ ] 09:00 - 10:30 🎯 FOCUS: [[Quarterly Report]] - Complete data analysis section #deep-work
  
  **Session Outcome**: Finish all charts and statistical summaries for Q3 data
  
  **Materials Needed**:
  - [[Q3 Dataset]] (already cleaned)
  - [[Analysis Framework Template]]
  - Previous quarter's charts for consistency
  
  **Post-Session Note**:
  [After session, capture: What worked? What's next? Any insights?]
```

> [!attention]
> **Protecting Focus Sessions**
> 
> The biggest threat to focus sessions is **interruption**. Day Planner makes the commitment visible, but you must:
> 
> - **Communicate boundaries**: Team knows "blocked time" means no interruptions
> - **Disable notifications**: Slack, email, phone on Do Not Disturb
> - **Physical cues**: Headphones, door closed, "Focus" status
> - **Honor the block**: Treat it as seriously as a meeting
> 
> **Key insight**: Time-boxing is a commitment to YOURSELF—just as valid as a commitment to others.

### Weekly Planning Strategy

While Day Planner emphasizes daily execution, the **Week Planner view** enables higher-level scheduling.

**Weekly Planning Session** (Sunday evening or Monday morning):

> [!phase-one]
> **Phase 1: Input Gathering (5 minutes)**
> 
> Collect information from multiple sources:
> - [ ] Review calendar for fixed commitments (meetings, appointments)
> - [ ] Check task manager for due dates and priorities
> - [ ] Review project notes for ongoing work
> - [ ] Consider personal goals/aspirations for the week

> [!phase-two]
> **Phase 2: Theme & Big Rocks (10 minutes)**
> 
> Identify the week's focus:
> - [ ] What's the **theme** of this week? (e.g., "Client deliverables," "Research sprint")
> - [ ] What are the **3-5 "big rocks"**—outcomes that matter most?
> - [ ] Which days are best for deep work? Which are meeting-heavy?

> [!phase-three]
> **Phase 3: Time Allocation (15 minutes)**
> 
> Open Week Planner view and distribute work:
> - [ ] Place big rocks in optimal time slots (morning focus blocks)
> - [ ] Balance workload across days (don't overload Monday)
> - [ ] Protect recovery time (lunch, breaks, exercise)
> - [ ] Plan energy-matched tasks (admin on low-energy days)

> [!phase-four]
> **Phase 4: Reality Check & Buffer (5 minutes)**
> 
> Ensure the plan is sustainable:
> - [ ] Total committed hours per day < actual available hours
> - [ ] 20-30% buffer time for unexpected tasks
> - [ ] Personal time protected (dinner, exercise, hobbies)
> - [ ] One "flex day" with lighter schedule for overflow

**Week Planner Advantage:**

The horizontal, multi-day view reveals patterns invisible in daily planning:

- **Unbalanced weeks**: Monday overloaded, Friday underutilized → redistribute
- **Meeting clusters**: Back-to-back meetings with no prep time → reschedule
- **No focus blocks**: Week is all meetings → block focus time or defer meetings
- **Missing recovery**: No breaks between intense days → add rest

> [!principle-point]
> **Weekly Planning Prevents Daily Fire-Fighting**
> 
> Without weekly planning, each morning becomes reactive—"What's urgent today?"
> 
> With weekly planning, each morning becomes confirmatory—"Is today's plan still optimal?" You've already made strategic decisions, so daily planning is minor adjustment, not wholesale creation.

---

## 🛠️ Technical Considerations

For power users and those troubleshooting issues, understanding Day Planner's technical architecture helps optimize usage.

### Plugin Settings Deep Dive

Day Planner's settings panel offers extensive configuration options. Here's what each section controls:

**Timeline Display Settings:**

| Setting | Options | Recommendation |
|---------|---------|----------------|
| **Timeline Zoom Level** | 0.5 - 3.0 | Start with 1.0, adjust based on daily task count |
| **Show Current Time** | ON/OFF | ON—provides temporal anchoring |
| **Colorful Timeline** | ON/OFF | ON—improves source differentiation |
| **Show Progress on Tasks** | ON/OFF | Personal preference (adds visual clutter vs. helpful feedback) |

**Status Bar Settings:**

| Setting | Effect | Use Case |
|---------|--------|----------|
| **Show in Status Bar** | Toggle entire status bar feature | Disable if you want minimal UI |
| **Show Progress Bar** | Visual time remaining indicator | Enable if you prefer visual feedback |
| **Show Next Task** | Preview upcoming task | Enable for context switching awareness |
| **Mini-Timeline** | 3-hour upcoming tasks preview | Enable if you have horizontal space |

**Calendar/ICS Settings:**

| Setting | Description | Notes |
|---------|-------------|-------|
| **Calendars** | Manage ICS feed URLs | Add/edit/remove calendar integrations |
| **Refresh Interval** | How often to check for calendar updates | Default 15 min (balance freshness vs. API limits) |
| **Show Calendar Events** | Toggle event display in timeline | Disable if calendars clutter your view |

**Time Tracking Settings:**

| Setting | Purpose | Recommendation |
|---------|---------|----------------|
| **Show Clocks in Timeline** | Enable tracked time column | ON if you use time tracking |
| **Active Clock Display** | Show running clock in sidebar | ON—provides accountability |
| **Auto-Complete on Clock Stop** | Mark task done when clock stops | Personal preference |

**Task Discovery Settings:**

| Setting | Description | Impact |
|---------|-------------|--------|
| **Dataview Filter** | (Legacy) Custom query for task discovery | No longer needed in recent versions—auto-discovery |
| **Show Vault Tasks** | Display tasks from non-daily notes | ON for full task visibility |

> [!helpful-tip]
> **Settings Experimentation Protocol**
> 
> Day Planner has many settings, which can be overwhelming. Try this approach:
> 
> **Week 1**: Use all defaults, don't change anything
> **Week 2**: Identify ONE friction point and adjust setting to address it
> **Week 3**: Identify ANOTHER friction point and adjust
> 
> This incremental approach prevents over-optimization before you understand your actual needs.

### Performance Optimization

For large vaults or users experiencing slowdowns:

**Performance Factors:**

1. **Vault Size**: Scanning many files for scheduled tasks is computationally expensive
2. **ICS Calendars**: Multiple calendars with many events increase load time
3. **Dataview Queries**: Complex custom queries slow timeline rendering
4. **Plugin Conflicts**: Other plugins (especially heavy ones like Dataview, Templater) compete for resources

**Optimization Strategies:**

> [!methodology-and-sources]
> **Performance Tuning Steps**
> 
> **If Day Planner is slow:**
> 
> 1. **Reduce Task Discovery Scope**
>    - Day Planner scans entire vault by default
>    - Consider using tags to filter: only tasks with `#daily-plan` appear
>    - (Check documentation—recent versions may have folder filtering)
> 
> 2. **Limit Calendar Integrations**
>    - Each ICS feed adds loading time
>    - Only add calendars you actively reference
>    - Increase refresh interval (e.g., 30 minutes instead of 15)
> 
> 3. **Simplify Timeline Display**
>    - Disable "Show Clocks" if you don't use time tracking
>    - Reduce zoom level to show fewer tasks on screen
>    - Turn off mini-timeline in status bar
> 
> 4. **Vault Maintenance**
>    - Archive old daily notes (move completed years to archive folder)
>    - Use Obsidian's "Excluded Files" setting to ignore large media folders
> 
> 5. **Check Plugin Conflicts**
>    - Temporarily disable other plugins to isolate issue
>    - Common culprits: Heavy Dataview queries auto-running, Templater scripts

> [!constraints-and-pitfalls]
> **Known Performance Bottlenecks**
> 
> - **Large daily notes**: If your daily notes are massive (1000+ lines), timeline parsing slows
> - **Complex regex in Dataview**: Custom task filters with regex matching are expensive
> - **Real-time updates**: Timeline refreshes on every note edit, which can lag on slow systems
> - **Mobile limitations**: Obsidian mobile has less processing power—Day Planner may be sluggish

### Troubleshooting Common Issues

**Issue 1: Tasks Not Appearing in Timeline**

Diagnostic checklist:

- [ ] Dataview plugin is installed and enabled
- [ ] Task syntax is correct (`- [ ] HH:mm - HH:mm Description`)
- [ ] Task is under a heading (any level: #, ##, ###, ####)
- [ ] Daily Notes plugin is enabled
- [ ] You're viewing the correct day's note
- [ ] Timeline view is open (Command Palette → "Show Timeline")

**Issue 2: Calendar Events Not Importing**

Diagnostic checklist:

- [ ] ICS URL ends with `.ics` (not just a web link)
- [ ] ICS URL works in browser (paste URL, should download/show calendar data)
- [ ] Calendar is published/shared with appropriate permissions
- [ ] Sufficient time has passed for first refresh (check refresh interval setting)
- [ ] No authentication required (ICS format is read-only, public access only)

**Issue 3: Time Tracking Clocks Not Saving**

Diagnostic checklist:

- [ ] You stopped the clock (not just closed Obsidian with clock running)
- [ ] Task has proper checkbox syntax (`- [ ]`)
- [ ] Note is saved (Obsidian auto-saves, but check for unsaved indicator)
- [ ] Dataview properties are writable (not in a code block or comment)

**Issue 4: Week Planner Shows Wrong Days**

Likely cause: **Week Start Day mismatch**

- Day Planner respects Obsidian's "Week Start" setting
- Settings → General → "Week starts on" → Verify it matches your preference (Sunday vs. Monday)

**Issue 5: Drag-and-Drop Not Working**

Possible causes:

- **Read-only mode**: You're in preview mode, not edit mode
- **Source conflict**: Trying to edit ICS calendar events (which are read-only)
- **Mobile**: Drag-and-drop is desktop-only feature
- **Theme conflict**: Some themes interfere with drag functionality (try default theme)

> [!warning]
> **When to Report Bugs**
> 
> If you encounter issues not listed above:
> 
> 1. **Check GitHub Issues**: [Day Planner GitHub](https://github.com/ivan-lednev/obsidian-day-planner/issues)
> 2. **Search Forum**: [Obsidian Forum - Day Planner tag](https://forum.obsidian.md)
> 3. **Create Issue Report**:
>    - Include Obsidian version
>    - Include Day Planner version
>    - Describe expected vs. actual behavior
>    - Provide minimal reproducible example
>    - Share relevant console logs (Developer Tools → Console)

### Mobile vs. Desktop Differences

Day Planner is primarily **desktop-optimized**. Mobile functionality is limited:

**Mobile Limitations:**

| Feature | Desktop | Mobile |
|---------|---------|--------|
| **Timeline View** | ✅ Full support | ⚠️ Limited (may be sluggish) |
| **Week Planner** | ✅ Full support | ❌ Not available or very limited |
| **Drag-and-Drop** | ✅ Full support | ❌ Not supported |
| **Notifications** | ✅ Native OS notifications | ❌ No notifications |
| **Time Tracking** | ✅ Full clock controls | ⚠️ Manual property editing only |
| **Calendar Sync** | ✅ ICS integration | ⚠️ Events visible but not editable |

**Mobile Workaround Strategy:**

Use mobile Obsidian for:
- **Viewing** your day's plan (read timeline)
- **Checking off** completed tasks (edit checkboxes)
- **Quick notes** during tasks (add context to existing blocks)

Reserve for desktop:
- **Planning** (Week Planner, drag-and-drop)
- **Time tracking** (clock controls)
- **Calendar integration setup**

> [!use-cases-and-examples]
> **Mobile + Desktop Workflow**
> 
> **Morning (Desktop)**: Plan day in Week Planner, time-box tasks, set up timeline
> **Throughout Day (Mobile)**: Check current task on timeline, mark tasks complete, add notes
> **Evening (Desktop)**: Review day, start time tracking for reflection, plan tomorrow

### Compatibility with Other Plugins

Day Planner interacts with several popular plugins—some synergistically, others with conflicts.

**Synergistic Plugins:**

| Plugin | Integration Point | Benefit |
|--------|-------------------|---------|
| **[[Tasks Plugin]]** | Scheduled task discovery | Vault-wide task scheduling |
| **[[dataview]]** | Task queries, clock analysis | Advanced task filtering, time analytics |
| **[[Templater]]** | Daily note automation | Auto-insert Day Planner sections |
| **[[Calendar Plugin]]** | Date navigation | Quick jump to specific daily notes |
| **[[Periodic Notes]]** | Weekly/monthly notes | Extended planning beyond daily |

**Potential Conflicts:**

| Plugin | Issue | Workaround |
|--------|-------|------------|
| **[[Full Calendar]]** | Both provide calendar views | Choose one as primary, disable unused views |
| **[[Toggl Track]]** | Duplicate time tracking | Use one system (either Day Planner clocks or Toggl) |
| **[[Kanban]]** | Different task visualization paradigm | Use Kanban for project status, Day Planner for time allocation |

> [!helpful-tip]
> **Plugin Stack Recommendation**
> 
> For optimal Day Planner experience, consider this plugin combination:
> 
> **Essential**:
> - Daily Notes (core)
> - Dataview
> - Day Planner
> 
> **Highly Recommended**:
> - Tasks (for vault-wide task management)
> - Calendar (for date navigation)
> - Templater (for daily note automation)
> 
> **Optional Enhancers**:
> - Periodic Notes (if you want weekly planning)
> - Heatmap Calendar (for activity visualization)
> - Natural Language Dates (for quick date entry)

---

## ⚠️ Limitations & Workarounds

No plugin is perfect. Understanding Day Planner's limitations helps you work within constraints or find alternative solutions.

### Known Limitations

> [!constraints-and-pitfalls]
> **Feature Gaps in Day Planner**
> 
> **What Day Planner Does NOT Do:**
> 
> 1. **No Recurring Tasks**: Must manually create tasks each day
>    - No "Daily standup at 9 AM every weekday" automation
>    - Workaround: Use Tasks plugin's recurrence + vault-wide discovery
> 
> 2. **No Task Templates**: Can't define reusable task blocks
>    - No "Morning Routine" template with preset time blocks
>    - Workaround: Use Templater to insert template text in daily notes
> 
> 3. **No Two-Way Calendar Sync**: Calendar integration is read-only
>    - Can't create calendar events from Obsidian tasks
>    - Workaround: Use complementary plugins like [[iCal Plugin]] for export
> 
> 4. **No Task Dependencies**: Can't say "Task B starts after Task A completes"
>    - Manual rescheduling required when tasks take longer than planned
>    - Workaround: Time-box conservatively, build buffer time
> 
> 5. **Limited Mobile Support**: Many features desktop-only
>    - No Week Planner on mobile
>    - No drag-and-drop on mobile
>    - Workaround: Use mobile for execution only, plan on desktop
> 
> 6. **No Pomodoro Timer**: Time tracking requires manual start/stop
>    - No automatic 25-minute work / 5-minute break cycles
>    - Workaround: Use [[PomoBar]] or external Pomodoro timer
> 
> 7. **No Task Prioritization**: All tasks visually equal
>    - No P1/P2/P3 labels or visual priority indicators
>    - Workaround: Use emojis or tags in task text (🎯 for high priority)
> 
> 8. **No Effort Estimates**: Can't track planned vs. actual effort
>    - Time blocks show duration, but no "2 hours planned, 3 hours actual" comparison
>    - Workaround: Use time tracking clocks + Dataview analysis

### Common Pain Points & Solutions

**Pain Point 1: Forgetting to Plan**

**Problem**: You open Obsidian intending to plan your day, but get distracted and start working without a plan.

**Solutions:**

- **Templater Automation**: Auto-insert Day Planner section when creating daily note
- **Morning Ritual**: Link planning to existing habit (e.g., "I plan day while drinking coffee")
- **Status Bar Reminder**: If status bar shows no tasks, it's a visual cue you haven't planned

**Pain Point 2: Plans Become Obsolete**

**Problem**: Life happens, your 2 PM meeting gets moved to 4 PM, and your whole afternoon plan is now wrong.

**Solutions:**

- **Buffer Time**: Schedule only 60-70% of available time, leaving flexibility
- **Rapid Rescheduling**: Use drag-and-drop in timeline to quickly adjust
- **Accept Imperfection**: Timeboxing is aspirational, not prescriptive—adapt as needed

**Pain Point 3: Task Overcommitment**

**Problem**: You time-box 12 hours of work into an 8-hour day because "I'll just work faster."

**Solutions:**

- **Reality-Based Planning**: Track actual time with clocks, compare to estimates, adjust future plans
- **Fixed Horizon**: Hard stop time (e.g., "Work ends at 6 PM") forces realistic planning
- **Defer, Don't Delete**: When overcommitted, move tasks to tomorrow instead of cramming

> [!principle-point]
> **The Planning Fallacy**
> 
> Humans are notoriously bad at estimating how long tasks will take ([[Planning Fallacy]]). Time tracking with Day Planner provides **objective feedback**—revealing that your "2-hour task" actually took 4 hours. Over time, this calibrates your estimates.

**Pain Point 4: Interruptions Derail Plan**

**Problem**: You planned focus time, but got interrupted by 5 urgent requests.

**Solutions:**

- **Communication**: Make focus blocks visible to team (calendar blocking, Slack status)
- **Interruption Log**: Use daily note to capture interruptions—data to advocate for protected time
- **Response Time Expectations**: "I check Slack every 2 hours"—sets boundaries

**Pain Point 5: No Motivation to Follow Plan**

**Problem**: You created a beautiful time-boxed schedule, then completely ignored it.

**Solutions:**

- **Start Small**: Time-box just 2-3 critical tasks per day, leave rest flexible
- **External Accountability**: Share your plan with a colleague or accountability partner
- **Review Habit**: End-of-day review ("What worked? What didn't?") increases commitment
- **Intrinsic Motivation**: Ensure tasks align with your values—easier to follow plan you believe in

### Complementary Plugins for Gaps

When Day Planner doesn't meet a need, these plugins fill gaps:

| Need | Plugin | How It Helps |
|------|--------|--------------|
| **Recurring Tasks** | [[Tasks Plugin]] | Define recurrence patterns (daily, weekly, etc.) |
| **Pomodoro Timing** | [[PomoBar]] | 25/5 work/break timers |
| **Calendar Export** | [[iCal Plugin]] | Export Obsidian tasks to external calendars |
| **Weekly/Monthly Planning** | [[Periodic Notes]] | Extend time-boxing beyond daily notes |
| **Habit Tracking** | [[Heatmap Calendar]] | Visualize consistency over time |
| **Project Management** | [[Kanban]] | Track project phases, not just daily tasks |
| **Advanced Time Tracking** | [[Obsidian Simple Time Tracker]] | More sophisticated tracking features |

> [!helpful-tip]
> **The Plugin Minimalist Principle**
> 
> While these complementary plugins solve gaps, **resist the urge to install everything**. Each additional plugin:
> - Increases complexity
> - Potentially slows Obsidian
> - Creates maintenance burden (updates, conflicts)
> 
> Start with Day Planner alone. Only add plugins when you've repeatedly encountered a specific friction point.

---

## 🚀 Optimization Strategies

For users who've mastered Day Planner basics and want to maximize efficiency:

### Template Design

Well-designed daily note templates make planning frictionless.

**Effective Daily Note Template Pattern:**

```markdown
---
date: {{date:YYYY-MM-DD}}
type: daily-note
---

# {{date:dddd, MMMM D, YYYY}}

## 🎯 Today's Focus

**Most Important Task (MIT):**
- [ ] [Your most critical outcome for today]

**Secondary Priorities:**
- [ ] [Priority 2]
- [ ] [Priority 3]

---

## ⏰ Day Planner

### Morning Block (07:00 - 12:00)
- [ ] 07:00 - 07:30 Morning routine
- [ ] 07:30 - 08:00 Plan day, review calendar
- [ ] 08:00 - 10:30 🎯 MIT: [Focus work]
- [ ] 10:30 - 11:00 Break / Coffee
- [ ] 11:00 - 12:00 [Secondary task or meeting]

### Afternoon Block (13:00 - 17:00)
- [ ] 13:00 - 14:00 Lunch & walk
- [ ] 14:00 - 15:30 [Task block]
- [ ] 15:30 - 16:00 [Task block]
- [ ] 16:00 - 17:00 [Task block or admin time]

### Evening Wind-Down (17:00 - 18:00)
- [ ] 17:00 - 17:30 Email cleanup, tomorrow prep
- [ ] 17:30 - 18:00 Day review & reflection

---

## 📝 Notes & Capture

[Space for meeting notes, ideas, journal entries]

---

## ✅ Daily Review

**What went well:**
- 

**What could improve:**
- 

**Tomorrow's prep:**
- 
```

**Template Optimization Principles:**

> [!principle-point]
> **Pre-Structured vs. Blank Canvas**
> 
> **Pre-structured templates** (like above) work best for:
> - Consistent daily rhythms
> - People who value predictability
> - Those who struggle with decision fatigue
> 
> **Minimal templates** (just heading, blank timebox area) work best for:
> - Highly variable schedules
> - Creative/flexible workers
> - Those who find structure constraining
> 
> Start with structure, remove what feels excessive.

### Hotkey Configuration

Strategic hotkey assignment reduces friction in Day Planner workflows.

**Recommended Hotkey Assignments:**

| Command | Suggested Hotkey | Rationale |
|---------|------------------|-----------|
| **Open Today's Note** | `Cmd/Ctrl + T` | Most frequent action, deserves single key |
| **Show Timeline** | `Cmd/Ctrl + Shift + T` | Related to "Today" key, easy muscle memory |
| **Show Week Planner** | `Cmd/Ctrl + Shift + W` | "W" for Week, shift modifier for planning mode |
| **Start Clock** | `Cmd/Ctrl + Shift + K` | "K" for Clock (C often taken), quick access |
| **Stop Clock** | `Cmd/Ctrl + Shift + K` | Same key as start (toggle behavior) |
| **Open Tomorrow's Note** | `Cmd/Ctrl + Shift + T` (if available) | Forward-planning convenience |

> [!helpful-tip]
> **Hotkey Design Philosophy**
> 
> Good hotkeys are:
> - **Mnemonic**: `W` for Week, `T` for Today/Timeline
> - **Consistent**: Related actions use similar key combinations
> - **Non-Conflicting**: Don't override critical Obsidian defaults (Cmd+N for new note, etc.)
> - **Comfortable**: Keys reachable without hand contortion
> 
> Avoid: Function keys (F1-F12), complex 3-modifier combos (Cmd+Shift+Ctrl+X)

### Command Palette Workflow

For actions used frequently but not "hotkey-worthy," optimize command palette usage.

**Fast Command Palette Navigation:**

- Day Planner commands start with "Day Planner:", so typing "day" filters them immediately
- Obsidian remembers recently-used commands—most-used commands rise to the top
- Alias commands: Some commands have short aliases (e.g., "timeline" instead of "Show the Day Planner Timeline")

**Power User Trick:**

Create **custom commands** using [[Templater]] or [[component-exemplar-quickadd-plugin-documentation-v1.0.0-20251119225738]] that combine multiple Day Planner actions:

Example: "Start Day" command that:
1. Opens today's daily note
2. Inserts Day Planner template
3. Opens timeline view
4. Opens Week Planner in second pane

This turns 4 manual actions into 1 keystroke.

### Automated Workflows

Leverage [[Templater]] for advanced automation.

**Example: Auto-Populate Calendar Events in Daily Note**

If you use the [[obsidian-ics]] plugin alongside Day Planner:

```javascript
<%* 
// Templater script to auto-insert calendar events as time blocks
const events = await app.plugins.getPlugin('ics').getEvents(moment(tp.file.title,'YYYY-MM-DD'));
events.sort((a,b) => a.utime - b.utime).forEach((e) => { 
  tR += `- [ ] ${e.time} ${e.summary}${e.location ? ' - ' + e.location : ''}\n`;
});
%>
```

This script runs when you create a daily note, automatically pulling calendar events and formatting them as Day Planner time blocks.

**Example: Weekly Planning Automation**

Create a Templater template for weekly planning that:

1. Generates a weekly overview note
2. Lists all daily notes for the week
3. Aggregates all scheduled tasks from the week
4. Provides space for weekly theme and goals

**Example: End-of-Day Automation**

Templater script that runs when you close a daily note:

- Counts completed vs. planned tasks
- Calculates total tracked time
- Appends summary statistics to daily note

> [!insight]
> **Automation Trade-off**
> 
> Automation has diminishing returns:
> - **High-value automation**: Eliminates repeated manual work (e.g., inserting calendar events)
> - **Low-value automation**: Adds complexity without meaningful time savings
> 
> Only automate tasks you perform daily AND take meaningful time (>30 seconds per occurrence).

### Integration with Review Systems

Day Planner shines when integrated with periodic review practices ([[GTD Weekly Review]], [[Quarterly Planning]], etc.).

**Daily Review Integration:**

At day's end, use Day Planner data for reflection:

```markdown
## ✅ Daily Review

**Planned Tasks:** 8
**Completed:** 6
**Time Tracked:** 5.5 hours

**Key Wins:**
- Completed Q4 analysis ahead of schedule
- Had productive client meeting—secured next phase

**Challenges:**
- Underestimated report writing (planned 2h, took 3.5h)
- Interrupted 3x during focus block—need better boundaries

**Tomorrow's Adjustment:**
- Time-box report tasks at 1.5x estimate
- Enable Do Not Disturb during morning focus
```

**Weekly Review Integration:**

Review week's worth of Day Planner data:

- **What You Did**: Look back at all completed tasks
- **Time Analysis**: Use Dataview to query total hours tracked per project
- **Planning Accuracy**: Compare planned vs. actual time (improve estimates)
- **Pattern Recognition**: Which days had best focus? What enabled it?

**Sample Weekly Review Dataview Query:**

```dataview
TABLE
  file.day as "Date",
  length(file.tasks.completed) as "Completed Tasks",
  choice(trackedTime, trackedTime + " hours", "—") as "Time Tracked"
FROM "Daily Notes"
WHERE file.day >= date(today) - dur(7 days)
SORT file.day DESC
```

> [!use-cases-and-examples]
> **Review-Driven Optimization**
> 
> **Month 1**: Use Day Planner, no reviews → chaotic, inconsistent
> **Month 2**: Add daily 5-min review → notice patterns (always overcommit Mondays)
> **Month 3**: Adjust based on reviews → realistic Monday plans, better outcomes
> **Month 6**: Reviews reveal 80% planning accuracy → trust your estimates, feel in control

---

## 🔗 Related Topics for PKB Expansion

1. **[[Timeboxing Methodology]]**
   - *Connection*: Day Planner is the implementation tool; timeboxing is the underlying philosophy
   - *Depth Potential*: Historical origins (time management evolution), psychological research on time-bounded work, comparison with other productivity frameworks
   - *Knowledge Graph Role*: Core concept node connecting productivity, scheduling, and cognitive psychology domains

2. **[[Tasks Plugin for Obsidian]]**
   - *Connection*: Day Planner's most important integration partner for vault-wide task discovery
   - *Depth Potential*: Full Tasks plugin capabilities (recurrence, queries, filtering, custom statuses), optimal configuration for Day Planner synergy
   - *Knowledge Graph Role*: Technical integration node linking task management with temporal scheduling

3. **[[Calendar Integration Strategies (ICS Feeds)]]**
   - *Connection*: External calendar synchronization is Day Planner's gateway to unified scheduling
   - *Depth Potential*: ICS protocol details, multi-calendar management, privacy considerations, alternative sync methods (CalDAV, native apps)
   - *Knowledge Graph Role*: Cross-tool interoperability node connecting Obsidian ecosystem with external productivity tools

4. **[[Personal Knowledge Management (PKM) Daily Note Systems]]**
   - *Connection*: Day Planner sits within the broader context of daily note workflows in PKM practice
   - *Depth Potential*: Daily note philosophies (Bullet Journal, Interstitial Journaling, Day Planner), template design, integration with other PKM practices (capture, reflection, linking)
   - *Knowledge Graph Role*: Methodological hub connecting multiple PKM techniques and tools

---

This comprehensive reference note equips you to use Day Planner at an expert level—from basic installation through advanced optimization strategies. The plugin transforms Obsidian from a static knowledge base into a dynamic daily operations center, unifying planning, execution, and reflection in a single workspace.

```
<thinking>
**REQUEST CLASSIFICATION:**
- Type: Comprehensive Reference Note
- Scope: Reference note with practical guide elements
- Topic: Obsidian Day Planner Plugin
- Research Required: YES - Need current information about plugin features, best practices, and recent updates
- User Intent: Dual purpose - reference documentation + optimization guide for daily use

**RESEARCH STRATEGY:**
I need to gather comprehensive information about:
1. Core functionality and features of Day Planner plugin
2. Installation and setup procedures
3. Syntax and formatting options
4. Integration with other Obsidian features
5. Best practices and optimization techniques
6. Common pitfalls and troubleshooting
7. Comparison with alternative approaches
8. Recent updates and community insights

Let me search for authoritative information on this plugin.
</thinking><thinking>
**SYNTHESIS & BLUEPRINT CONSTRUCTION:**

Based on my research, I've gathered comprehensive information about the Day Planner plugin for Obsidian. Let me now construct a detailed blueprint for the reference note.

**KEY FINDINGS:**
1. There are TWO distinct versions: Day Planner (modern, by Ivan Lednev) and Day Planner OG (original fork by Erin Schnabel)
2. The modern version focuses on calendar integration, timeline views, and time tracking
3. Core dependencies: Dataview plugin (REQUIRED), Daily Notes or Periodic Notes plugin
4. Multiple task sources: Daily notes with time formats, Tasks plugin with scheduled dates, external ICS calendars
5. Key features: Week Planner view, Timeline view, status bar integration, time tracking with clocks, drag-and-drop editing
6. Task syntax variations: inline time format (HH:mm - HH:mm), Tasks plugin emoji format (⏳), Dataview properties ([scheduled::])
7. Calendar integration: Google Calendar, iCloud, Outlook via ICS links
8. Time tracking: Right-click menu to start/stop clocks, stores as Dataview properties
9. Customization: notifications, status bar indicators, timeline zoom, colorful timeline option
10. Use cases: timeboxing, focus sessions, daily planning, task management

**HIERARCHICAL OUTLINE FOR REFERENCE NOTE:**

I. Introduction & Core Concept
   A. What is Day Planner
   B. Philosophy of timeboxing in Obsidian
   C. Plugin versions and which to choose

II. Prerequisites & Installation
   A. Required plugins (Dataview, Daily Notes/Periodic Notes)
   B. Installation process
   C. Initial configuration

III. Core Functionality & Views
   A. Timeline View
   B. Week Planner View
   C. Status Bar Integration
   D. Mini-Timeline Feature

IV. Task Syntax & Formats
   A. Daily note inline format (HH:mm - HH:mm)
   B. Tasks plugin integration (emoji shortcuts)
   C. Dataview property formats
   D. Vault-wide task discovery
   E. Color coding and visual differentiation

V. Calendar Integration
   A. ICS link setup
   B. Google Calendar integration
   C. iCloud Calendar integration
   D. Outlook/Office 365 integration
   E. Multi-calendar management

VI. Time Tracking System
   A. Clock recording mechanism
   B. Starting/stopping clocks
   C. Active clock display
   D. Time tracking timeline column
   E. Dataview property storage

VII. Advanced Features & Customization
   A. Drag-and-drop editing
   B. Notifications and alerts
   C. Timeline zoom and density
   D. Colorful timeline option
   E. Progress indicators

VIII. Workflows & Best Practices
   A. Morning planning routine
   B. Integration with external task managers
   C. Meeting note preparation
   D. Focus session scheduling
   E. Weekly planning strategy

IX. Technical Considerations
   A. Plugin settings deep dive
   B. Performance optimization
   C. Troubleshooting common issues
   D. Mobile vs desktop differences
   E. Compatibility with other plugins

X. Limitations & Workarounds
   A. Known issues
   B. Feature gaps
   C. Alternative approaches
   D. Complementary plugins

XI. Optimization Strategies
   A. Template design
   B. Hotkey configuration
   C. Command palette shortcuts
   D. Automated workflows

This comprehensive blueprint will ensure the note covers all aspects of Day Planner usage, from basic setup to advanced optimization techniques.
</thinking>

```