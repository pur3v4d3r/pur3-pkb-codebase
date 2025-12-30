---
tags:
  - documentation
  - review-system
  - implementation-guide
type: guide
concepts:
  - "[[self-doc-concept-template]]"
---

# 🚀 Review System Implementation Guide

## Overview

Your Intelligent PKB Review System has been implemented! This guide will walk you through setup and usage.

---

## What Was Created

### Folder Structure

```
05-tasks-&-reviews/
├── review-dashboard.md          ← Main hub (START HERE)
├── IMPLEMENTATION-GUIDE.md      ← This guide
├── daily/                       ← Daily review sessions
├── weekly/                      ← Weekly review sessions
├── monthly/                     ← Monthly review sessions
├── quarterly/                   ← Quarterly review sessions
└── domain-queues/               ← Domain-specific queues (to be created)

99-system/01-quickadd/02-templates/
├── _quick-review-template.md              ← Enhanced with auto-metadata
├── _daily-review-session-template.md      ← NEW
├── _weekly-review-session-template.md     ← NEW
└── _monthly-review-session-template.md    ← NEW

99-system/03-templater/01-templater-scripts/
├── calculate-next-review.js               ← NEW
├── calculate-priority.js                  ← NEW
├── auto-promote-maturity.js               ← NEW
└── bulk-update-review-metadata.js         ← NEW
```

---


> [! ] # Quick Start Reference Card (5 Steps)
>  #### Step 1: Run Bulk Update (CRITICAL)
> This adds review metadata to all your existing notes.
> **Method 1: Via Templater Template (Recommended)**
> 1. Create a temporary note
> 2. Type: `<%* await tp.user["bulk-update-review-metadata"](tp) %>`
> 3. Switch to Reading Mode (or use Templater: Replace templates in active file)
> 4. Confirm by typing "yes" when prompted
> 5. Wait for completion message (may take 1-2 minutes)
> 6. Delete the temporary note
> **Method 2: Via Console (Advanced)**
> 7. Open Developer Tools (Ctrl/Cmd + Shift + I)
> 8. Go to Console tab
> 9. Paste and run the script manually
> 10. Confirm by typing "yes"
> **What it does**:
> - Adds `review:` object to all permanent notes
> - Fills missing `maturity`, `confidence`, `status` fields
> - Auto-calculates `priority` based on backlinks and tags
> - Sets `next-review` dates based on maturity
> **Result**: All notes in [03-notes/01_permanent-notes](../03-notes/01_permanent-notes) will have review metadata!
> 
> #### Step 2: Open the Review Dashboard
> Navigate to: [05-tasks-&-reviews/review-dashboard](review-dashboard.md)
> You should see:
> - 📊 Queue summary (total notes, overdue count, health score)
> - 🔴 Overdue & urgent notes
> - 📅 Notes due today
> - 📆 Notes due this week
> - 🌱 Maturity distribution
> 
> #### Step 3: Review Your First Note
> 1. From the dashboard, click on any overdue/due note
> 2. Read and update the note
> 3. Run command: Use QuickAdd → `_quick-review-template`
> 4. Follow prompts:
>    - Enter note title
>    - Add observations
>    - Choose maturity change
>    - Choose confidence change
> 5. Template automatically updates metadata!
> 
> #### Step 4: Start a Review Session
> Create your first review session:
> 6. Use QuickAdd command
> 7. Select `_daily-review-session-template` (or weekly/monthly)
> 8. New session note created in appropriate folder
> 9. See prioritized queue in the session note
> 10. Review notes, update `notes-reviewed` count
> 11. Mark session complete when done
> 
> #### Step 5: Monitor Progress
> Return to the [Review Dashboard](review-dashboard.md) regularly to:
> - Check queue health
> - See overdue notes
> - Track maturity progression
> - Monitor review consistency

## Metadata Schema

### Review Properties (Flattened Structure)

All reviewable notes now have these properties at root level:

```yaml
review-last-reviewed: 2025-12-14   # Last review date
review-next-review: 2025-12-21     # Scheduled review date
review-count: 3                    # Number of reviews
review-interval: 7                 # Days between reviews
review-priority: medium            # low | medium | high | urgent
```

**Note**: Properties use a flattened structure (not nested) for full Obsidian properties panel compatibility.

### Supporting Fields

```yaml
maturity: developing               # seedling | budding | developing | evergreen | needs-review
confidence: moderate               # speculative | provisional | moderate | established | high
status: active                     # active | archived | deprecated
```

---

## Review Intervals

Maturity-based scheduling:

| Maturity       | Interval | Purpose                          |
|----------------|----------|----------------------------------|
| Seedling       | 3 days   | Frequent review for new notes    |
| Budding        | 7 days   | Weekly review for developing     |
| Developing     | 14 days  | Bi-weekly for maturing notes     |
| Evergreen      | 30 days  | Monthly for stable knowledge     |
| Needs-review   | 1 day    | Daily for flagged notes          |

---

## Priority Calculation

Priority auto-calculated based on:

**Urgent**:
- Has `needs-review` or `urgent` tag
- 20+ backlinks

**High**:
- Has `type/moc` tag
- 10-19 backlinks
- Domain tags (cognitive-science, pkm, philosophy)

**Medium**:
- 3-9 backlinks
- Recently modified (last 30 days)

**Low**:
- < 3 backlinks
- Not modified recently (60+ days)

---

## Workflows

### Daily Review Workflow

1. Open [Review Dashboard](review-dashboard.md)
2. Check "Overdue & Urgent" section
3. Click note → review → run `_quick-review-template`
4. Repeat for 5-10 notes (15-30 min)
5. Optional: Create daily review session note

### Weekly Review Workflow

1. Create weekly session: `_weekly-review-session-template`
2. Focus on clearing overdue notes
3. Review all urgent + high priority notes
4. Promote mature seedlings
5. Update session stats

### Monthly Review Workflow

1. Create monthly session: `_monthly-review-session-template`
2. Review queue health report
3. Process critically overdue notes (>30 days)
4. Analyze maturity distribution
5. Identify high-value notes needing attention
6. Strategic planning for next month

---

## Templater Scripts Reference

### calculate-next-review.js

**Usage**:
```javascript
<% tp.user["calculate-next-review"](tp, "seedling") %>
```

**Returns**: Next review date (YYYY-MM-DD)

---

### calculate-priority.js

**Usage**:
```javascript
<% await tp.user["calculate-priority"](tp) %>
```

**Returns**: Priority level (urgent | high | medium | low)

---

### auto-promote-maturity.js

**Usage**:
```javascript
<% await tp.user["auto-promote-maturity"](tp) %>
```

**Returns**: Suggested maturity level (prompts user if eligible)

---

### bulk-update-review-metadata.js

**Usage**: Run via Templater command

**Features**:
- Scans all permanent notes
- Adds missing metadata
- Auto-calculates priorities
- Provides detailed report

---

## Tips & Best Practices

### Start Small
- Don't try to review everything at once
- Focus on overdue + urgent first
- Build review habit gradually (5-10 notes/day)

### Trust the System
- Priority calculations are heuristic-based
- Manually override priority when needed
- System learns from your patterns

### Regular Maintenance
- Weekly: Check queue health
- Monthly: Review maturity distribution
- Quarterly: Optimize intervals

### Batch Operations
- Review similar notes together
- Use domain-specific queues
- Process by maturity level

---

## Troubleshooting

### Issue: Notes not showing in queue

**Solutions**:
- Check `status: active` (not archived)
- Verify `review.next-review` exists
- Run bulk update script again

### Issue: Too many overdue notes

**Solutions**:
- Filter by priority (focus on urgent/high)
- Use "review amnesty" (bulk reschedule - coming soon)
- Adjust intervals (make them longer)

### Issue: Dataview queries not working

**Solutions**:
- Ensure Dataview plugin enabled
- Check DataviewJS is enabled in settings
- Verify frontmatter YAML is valid

### Issue: Templater scripts not found

**Solutions**:
- Check scripts exist in `99-system/03-templater/01-templater-scripts/`
- Enable "Trigger Templater on file creation"
- Restart Obsidian

---

```
## Next Steps

### Immediate (This Week)
- [x] Run bulk update script
- [ ] Review 10 overdue notes
- [ ] Create first daily session
- [ ] Explore review dashboard

### Phase 2 (Next 2 Weeks)
- [ ] Establish daily review habit (5-10 notes)
- [ ] Create first weekly review session
- [ ] Promote 5+ seedlings to budding
- [ ] Fine-tune priority overrides

### Phase 3 (Month 1)
- [ ] Create monthly review session
- [ ] Achieve 80%+ queue health
- [ ] Create domain-specific queues
- [ ] Build review analytics dashboard

### Phase 4 (Future Enhancements)
- [ ] Add Meta Bind buttons to templates
- [ ] Create review analytics with Charts
- [ ] Domain-specific review queues
- [ ] AI-assisted review summaries
```

---

## Support & Documentation

**Main Resources**:
- [Review Dashboard](review-dashboard.md) ← Your command center
- [Review System Guide](../04-library/02-pkb-and-pkm-learning/-reference/reference-instructional-review-system-2025112923.md) ← Full documentation
- [Implementation Plan](file:///C:/Users/pur3v4d3rpk/.claude/plans/delegated-marinating-duckling.md) ← Technical details

**Quick Reference**:
- Review intervals: seedling(3d), budding(7d), developing(14d), evergreen(30d)
- Priority levels: urgent → high → medium → low
- Maturity stages: seedling → budding → developing → evergreen

---

## Success Metrics

After 4 weeks, target:
- ✅ 80%+ notes with review metadata
- ✅ <20% notes overdue
- ✅ 5+ review sessions per week
- ✅ 10+ notes promoted to higher maturity
- ✅ 30 days of review history

---

🎉 **You're all set!** Start by opening the [Review Dashboard](review-dashboard.md) and reviewing your first note.
