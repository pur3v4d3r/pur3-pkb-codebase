# Implementation Plan: Intelligent PKB Review System

## Executive Summary

This plan implements a comprehensive review system for your Obsidian vault that automates review queue generation, provides interactive review workflows, tracks review analytics, and integrates with your existing maturity/confidence tracking system.

**Key Finding:** Your vault already has 80% of the foundation in place:
- Maturity tracking (`seedling` → `evergreen`)
- Review scheduling fields (`next-review`, `review-count`)
- Sophisticated Dataview/Templater setup
- 30+ existing templates and 20+ scripts
- Empty `05-tasks-&-reviews` folder ready for implementation

## User Preferences (Confirmed)

1. **Review Intervals:** Use seedling=3d, budding=7d, developing=14d, evergreen=30d
2. **Existing Template:** ENHANCE `_quick-review-template.md` as starting point
3. **Bulk Migration:** Create reliable bulk update script that adds missing metadata
4. **Daily Review Sessions:** Manual trigger only (QuickAdd command)
5. **Priority Field:** Auto-calculated based on backlinks, edits, tags (manual override allowed)
6. **Review Session Location:** `05-tasks-&-reviews/` (separate from daily notes)

## Implementation Strategy - 4 Phases

### Phase 1: Foundation Layer

**Files to Create/Modify:**
1. Enhance `_quick-review-template.md` - add auto-metadata updates
2. Create `_daily-review-session-template.md`
3. Create `_weekly-review-session-template.md`
4. Create `_monthly-review-session-template.md`
5. Create `05-tasks-&-reviews/review-dashboard.md`

**Metadata Schema:**
```yaml
review:
  last-reviewed: null
  next-review: <calculated>
  review-count: 0
  review-interval: <3/7/14/30 based on maturity>
  priority: medium  # auto-calculated, manual override
status: active  # active | archived | deprecated
```

### Phase 2: Interaction Layer

**Files to Create:**
1. `quick-review-workflow.js` - QuickAdd macro
2. Meta Bind button presets (5 buttons)

**Buttons:**
- Mark as Reviewed
- Promote Maturity
- Adjust Priority
- Skip Review
- Archive Note

### Phase 3: Automation & Discovery

**Files to Create:**
1. `calculate-next-review.js`
2. `calculate-priority.js`
3. `auto-promote-maturity.js`
4. `bulk-update-review-metadata.js` (with backup and reporting)

**Bulk Update Features:**
- Scans permanent notes folders
- Adds missing `review:` object
- Fills missing metadata (`maturity`, `confidence`, `status`)
- Auto-calculates priority from backlinks/edits/tags
- Creates backup before operation
- Detailed change report

### Phase 4: Analytics & Optimization

**Files to Create:**
1. `06-dashboards/review-analytics-dashboard.md`
2. `cognitive-science-review-queue.md`
3. `pkm-review-queue.md`
4. `philosophy-review-queue.md`
5. Three Dataview query templates

**Analytics:**
- Review completion trends (30-day line chart)
- Maturity distribution (doughnut chart)
- Queue health metrics
- 90-day heatmap
- Domain-specific queues

## Critical Design Decisions

1. **Nested Metadata:** Use `review:` object for organization
2. **Existing Fields:** Keep current `maturity`, `confidence` fields
3. **Priority Calculation:** Auto-calculate from backlinks + edits + tag importance
4. **Review Session Location:** `05-tasks-&-reviews/` folder structure
5. **Hybrid Controls:** Meta Bind buttons + QuickAdd workflows

## File Structure

```
05-tasks-&-reviews/
├── review-dashboard.md
├── daily/ (generated sessions)
├── weekly/ (generated sessions)
├── monthly/ (generated sessions)
└── domain-queues/
    ├── cognitive-science-review-queue.md
    ├── pkm-review-queue.md
    └── philosophy-review-queue.md

06-dashboards/
└── review-analytics-dashboard.md

99-system/01-quickadd/
├── 01-scripts/
│   └── quick-review-workflow.js
└── 02-templates/
    ├── _quick-review-template.md (enhanced)
    ├── _daily-review-session-template.md
    ├── _weekly-review-session-template.md
    └── _monthly-review-session-template.md

99-system/03-templater/01-templater-scripts/
├── calculate-next-review.js
├── calculate-priority.js
├── auto-promote-maturity.js
└── bulk-update-review-metadata.js

99-system/05-dataview/_queries-as-templates/
├── review-queue-query.md
├── maturity-distribution-query.md
└── review-health-metrics-query.md
```

## Success Metrics (4 Weeks)

1. **Coverage:** 80%+ permanent notes with review metadata
2. **Queue Health:** <20% notes overdue
3. **Consistency:** 5+ review sessions/week
4. **Promotion:** 10+ notes promoted to higher maturity
5. **Analytics:** 30 days of review history tracked

## Key Risks & Mitigations

1. **Query Performance:** Use `where()` before `sort()`, limit display to 50 notes
2. **Metadata Consistency:** Add null-safety checks (`p.review?.next_review`)
3. **Queue Overload:** Filter by priority, implement bulk rescheduling
4. **Button Failures:** Provide QuickAdd alternatives, validate YAML

## Next Steps After Implementation

1. Fine-tune intervals based on usage patterns
2. Add domain-specific workflows (active recall for cognitive science notes)
3. Integrate Smart Connections for AI-suggested reviews
4. Build review assistant using Text Generator plugin
