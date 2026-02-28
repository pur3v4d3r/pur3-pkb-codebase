# Implementation Plan: Intelligent PKB Review System

## Executive Summary

This plan implements a comprehensive review system for your Obsidian vault that automates review queue generation, provides interactive review workflows, tracks review analytics, and integrates with your existing maturity/confidence tracking system.

**Key Finding:** Your vault already has 80% of the foundation in place:
- Maturity tracking (`seedling` → `evergreen`)
- Review scheduling fields (`next-review`, `review-count`)
- Sophisticated Dataview/Templater setup
- 30+ existing templates and 20+ scripts
- Empty `05-tasks-&-reviews` folder ready for implementation

## Current State Analysis

### What You Already Have
1. **Metadata Infrastructure**: `maturity`, `confidence`, `next-review`, `review-count` fields in use
2. **Plugin Ecosystem**: All required plugins installed and configured
   - Dataview (with DataviewJS enabled)
   - Templater (folder templates enabled)
   - Meta Bind (JavaScript enabled)
   - Tasks (40+ custom statuses)
   - QuickAdd (30+ templates, 20+ scripts)
   - Charts (configured)
   - Periodic Notes (daily notes active)
3. **Template System**: 30 QuickAdd templates in `99-system/01-quickadd/02-templates/`
4. **Script Library**: 20 QuickAdd scripts in `99-system/01-quickadd/01-scripts/`
5. **Dataview Queries**: Component library in `99-system/05-dataview/_queries-as-templates/`
6. **MOC Pattern**: Sophisticated dashboard pattern with DataviewJS (cognitive-science-moc.md)
7. **Tag Taxonomy**: 577-tag hierarchical system

### What's Missing
1. **Periodic review notes** (weekly, monthly, quarterly templates)
2. **Automated review queue discovery** (Dataview queries)
3. **Interactive review controls** (Meta Bind buttons)
4. **Review workflow automation** (QuickAdd macros)
5. **Review analytics dashboard** (Charts integration)
6. **Spaced repetition scheduling** (Tasks integration)

## Implementation Strategy

### Phase 1: Foundation Layer (Week 1)

**Goal:** Establish review metadata schema and create basic periodic review templates

#### 1.1 Enhance Review Metadata Schema
**Files to modify:** Existing templates in `99-system/03-templater/02-templater-master-skeleton-templates/`

Add to existing frontmatter templates:
```yaml
review:
  last-reviewed: null
  next-review: <calculated>
  review-count: 0
  review-interval: <based on maturity>
  priority: medium  # low | medium | high | urgent
status: active  # active | archived | deprecated
```

**Maturity-to-Interval Mapping:**
- `seedling`: 3 days
- `budding`: 7 days
- `developing`: 14 days
- `evergreen`: 30 days
- `needs-review`: 1 day (urgent)

#### 1.2 Enhance Quick Review Template
**File to modify:** `99-system/01-quickadd/02-templates/_quick-review-template.md`

**Enhancements to add:**
- Auto-update target note's `review.*` metadata fields
- Auto-calculate next review date based on maturity
- Auto-increment review count
- Auto-calculate and update priority
- Optional maturity promotion with interval adjustment
- Append review log to target note (not separate file)
- Track review duration
- Link to today's review session note

#### 1.3 Create Periodic Review Session Templates
**New files to create in:** `99-system/01-quickadd/02-templates/`

1. `_daily-review-session-template.md`
2. `_weekly-review-session-template.md`
3. `_monthly-review-session-template.md`

Each template will include:
- Frontmatter with session metadata
- DataviewJS review queue query (priority-sorted)
- Meta Bind buttons for workflow actions
- Session notes section
- Statistics tracking

#### 1.3 Create Review Queue Dashboard
**New file:** `05-tasks-&-reviews/review-dashboard.md`

Central hub with:
- Overdue notes list
- Due this week
- Due this month
- Review completion trends
- Maturity distribution chart

### Phase 2: Interaction Layer (Week 2)

**Goal:** Add interactive controls and streamlined workflows

#### 2.1 Configure Meta Bind Buttons
**Update:** Meta Bind plugin settings → Button Presets

Create button presets:
1. **Mark as Reviewed** - Updates `last-reviewed`, increments `review-count`, calculates `next-review`
2. **Promote Maturity** - Advances maturity stage and adjusts review interval
3. **Adjust Priority** - Cycles through priority levels
4. **Skip Review** - Postpones review by 3 days
5. **Archive Note** - Sets status to archived (removes from queue)

#### 2.2 Create QuickAdd Review Macro
**New file:** `99-system/01-quickadd/01-scripts/quick-review-workflow.js`

Macro will:
1. Prompt for review notes/observations
2. Update review metadata automatically
3. Optionally promote maturity
4. Append review log entry to note
5. Increment session counter in today's review note

#### 2.3 Add Review Buttons to Note Templates
**Files to modify:** Existing templates with review metadata

Add button section at bottom:
```markdown
## 🔄 Review Actions

`BUTTON[mark-reviewed]` Mark as Reviewed
`BUTTON[promote-maturity]` Promote Maturity
`BUTTON[adjust-priority]` Adjust Priority
```

### Phase 3: Automation & Discovery (Week 3)

**Goal:** Automate review scheduling and queue generation

#### 3.1 Create Templater Helper Functions
**New files in:** `99-system/03-templater/01-templater-scripts/`

1. `calculate-next-review.js` - Calculates next review date based on maturity/interval
2. `auto-promote-maturity.js` - Suggests maturity promotions based on review history
3. `calculate-priority.js` - Auto-calculates priority based on backlinks, edits, tags
4. `bulk-update-review-metadata.js` - Batch updates for existing notes with missing metadata

**Bulk Update Script Features:**
- Scans all notes in permanent notes folders
- Adds missing `review:` object with calculated values
- Fills in missing standard metadata (`maturity`, `confidence`, `status`)
- Calculates initial `next-review` based on `modified` date and maturity
- Auto-calculates `priority` based on:
  - Backlink count (high backlinks = higher priority)
  - Days since last modified (recently edited = higher priority)
  - Tag importance (notes with `#type/moc` or domain tags = higher priority)
- Creates backup before bulk operations
- Provides detailed report of changes made

#### 3.2 Tasks Integration
**Modify:** Existing templates to add recurring review tasks

Add to reviewable notes:
```markdown
## 📅 Review Schedule

- [ ] Review: {{title}} 📅 {{next-review}} 🔁 every {{review-interval}} days ⏫
```

#### 3.3 Enable Periodic Notes (Weekly/Monthly/Quarterly)
**Update:** Periodic Notes plugin settings

Configure:
- Weekly notes → `05-tasks-&-reviews/weekly/`
- Monthly notes → `05-tasks-&-reviews/monthly/`
- Quarterly notes → `05-tasks-&-reviews/quarterly/`

Link templates to review session templates.

### Phase 4: Analytics & Optimization (Week 4)

**Goal:** Visual analytics and system refinement

#### 4.1 Create Review Analytics Dashboard
**New file:** `06-dashboards/review-analytics-dashboard.md`

Include:
- Review completion trends (line chart - last 30 days)
- Maturity distribution (doughnut chart)
- Review queue health metrics
- Review consistency tracking
- Domain-specific review queues

#### 4.2 Domain-Specific Review Queues
**New files in:** `05-tasks-&-reviews/domain-queues/`

Create specialized queues:
1. `cognitive-science-review-queue.md`
2. `pkm-review-queue.md`
3. `philosophy-review-queue.md`

Each filters by relevant tags from your 577-tag taxonomy.

#### 4.3 Review Heatmap Visualization
**Add to:** Review Analytics Dashboard

GitHub-style contribution heatmap showing 90-day review activity patterns.

## File Structure

```
05-tasks-&-reviews/
├── review-dashboard.md (main hub)
├── daily/
│   └── (generated daily review sessions)
├── weekly/
│   └── (generated weekly review sessions)
├── monthly/
│   └── (generated monthly review sessions)
├── quarterly/
│   └── (generated quarterly review sessions)
└── domain-queues/
    ├── cognitive-science-review-queue.md
    ├── pkm-review-queue.md
    └── philosophy-review-queue.md

06-dashboards/
└── review-analytics-dashboard.md (new)

99-system/01-quickadd/
├── 01-scripts/
│   └── quick-review-workflow.js (new)
└── 02-templates/
    ├── _daily-review-session-template.md (new)
    ├── _weekly-review-session-template.md (new)
    └── _monthly-review-session-template.md (new)

99-system/03-templater/01-templater-scripts/
├── calculate-next-review.js (new)
├── auto-promote-maturity.js (new)
└── bulk-update-review-metadata.js (new)

99-system/05-dataview/_queries-as-templates/
├── review-queue-query.md (new)
├── maturity-distribution-query.md (new)
└── review-health-metrics-query.md (new)
```

## Critical Design Decisions

### 1. Metadata Structure
**Decision:** Nest review fields under `review:` object rather than top-level fields

**Rationale:**
- Keeps frontmatter organized
- Matches your existing patterns (e.g., `link-up`, `link-related`)
- Easier to bulk update/query

### 2. Integration with Existing Maturity System
**Decision:** Use your existing `maturity` field, don't create duplicate

**Rationale:**
- You already have: `seedling`, `budding`, `developing`, `needs-review`, `evergreen`
- These align perfectly with spaced repetition intervals
- Avoids metadata proliferation

### 3. Priority Field Addition
**Decision:** Add `review.priority` field separate from maturity

**Rationale:**
- Maturity = knowledge development stage
- Priority = urgency/importance for review
- A seedling note might be high priority if it's critical to ongoing work
- Allows manual override of review scheduling

### 4. Tasks vs. Periodic Notes for Review Sessions
**Decision:** Use Periodic Notes for session notes, Tasks for individual note reminders

**Rationale:**
- Periodic Notes creates structured review sessions (daily/weekly/monthly)
- Tasks creates reminders for individual notes
- Both systems complement each other

### 5. Meta Bind vs. QuickAdd for Review Actions
**Decision:** Use Meta Bind for in-note buttons, QuickAdd for workflows

**Rationale:**
- Meta Bind: Immediate actions visible in Reading Mode
- QuickAdd: Complex multi-step workflows with prompts
- Best of both worlds

## Migration Strategy

### Existing Notes Without Review Metadata

**Two Approaches:**

**Approach A: Gradual (Recommended)**
1. Add review metadata to new notes via updated templates
2. Add metadata manually to high-priority existing notes during normal work
3. After 2-3 weeks, use bulk update script for remaining notes

**Approach B: Bulk Update**
1. Use `bulk-update-review-metadata.js` Templater script
2. Query all notes with `maturity` but without `review.next-review`
3. Calculate initial `next-review` based on:
   - Current maturity level
   - Last modified date
   - Note type (MOCs reviewed less frequently)

**Recommendation:** Start with Approach A for first 50-100 notes, then use Approach B.

## Testing Strategy

### Phase 1 Testing (Week 1)
- Test with 5-10 notes manually
- Verify Dataview queries return expected results
- Validate date calculations
- Check frontmatter parsing

### Phase 2 Testing (Week 2)
- Test Meta Bind buttons in Reading Mode
- Verify metadata updates persist correctly
- Test QuickAdd macro workflow end-to-end
- Validate review log appending

### Phase 3 Testing (Week 3)
- Generate weekly/monthly review notes
- Test recurring Tasks reminders
- Verify bulk update script doesn't corrupt frontmatter
- Check review queue accuracy

### Phase 4 Testing (Week 4)
- Validate Charts rendering with real data
- Test analytics calculations
- Verify domain-specific queue filtering
- Load test with 100+ notes in review queue

## Potential Issues & Mitigations

### Issue 1: Dataview Query Performance
**Problem:** Queries may be slow with 100+ notes in review queue

**Mitigation:**
- Use `where()` filters before `sort()` and `map()`
- Cache query results in dashboard notes
- Limit default display to 50 notes (pagination)

### Issue 2: Metadata Consistency
**Problem:** Notes missing review metadata break queries

**Mitigation:**
- Add null-safety checks: `p.review?.next_review`
- Create "incomplete metadata" validator query
- Run weekly metadata health check

### Issue 3: Review Queue Overload
**Problem:** Accumulated backlog becomes overwhelming

**Mitigation:**
- Implement "review amnesty" script for bulk rescheduling
- Filter by priority to show only urgent/high by default
- Allow bulk "extend by 7 days" action

### Issue 4: Meta Bind Button Failures
**Problem:** Buttons may not work in Edit Mode or with YAML errors

**Mitigation:**
- Add helper text: "Switch to Reading Mode to use buttons"
- Validate YAML before button actions
- Provide QuickAdd alternative for all button actions

## Success Metrics

After 4 weeks of implementation:

1. **Coverage:** 80%+ of permanent notes have review metadata
2. **Queue Health:** <20% of notes overdue for review
3. **Consistency:** 5+ review sessions per week
4. **Promotion:** 10+ notes promoted to higher maturity
5. **Analytics:** Dashboard shows 30 days of review history

## Next Steps After Implementation

1. **Fine-tune intervals** based on actual review patterns
2. **Create domain-specific workflows** (e.g., cognitive science notes reviewed with active recall questions)
3. **Integrate with Smart Connections** plugin for AI-suggested reviews
4. **Export review analytics** to track long-term knowledge development
5. **Build "review assistant"** using Text Generator plugin for AI-guided reviews

## User Preferences (Confirmed)

1. **Review Intervals:** CONFIRMED - Use seedling=3d, budding=7d, developing=14d, evergreen=30d
2. **Existing Template:** ENHANCE `_quick-review-template.md` as starting point, add all additional metadata and functionality
3. **Bulk Migration:** YES - Create reliable bulk update script that also adds missing metadata
4. **Daily Review Sessions:** Manual trigger only (QuickAdd command)
5. **Priority Field:** Auto-calculated based on backlinks, recent edits, tag importance (with manual override capability)
6. **Review Session Location:** `05-tasks-&-reviews/` (keep reviews separate from daily notes)
