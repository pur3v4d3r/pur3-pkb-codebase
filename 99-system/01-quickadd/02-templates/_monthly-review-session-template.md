---
tags:
  - review-session
  - type/monthly
  - year/<% tp.date.now("YYYY") %>
date: <% tp.date.now("YYYY-MM-DD") %>
review-type: monthly
completed: false
notes-reviewed: 0
session-duration: 0
type: review-session
week: "[[<% tp.date.now("YYYY-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
---

# 📅 Monthly Review Session: <% tp.date.now("MMMM YYYY") %>

> [!abstract] Session Overview
> **Type**: Monthly Review & Strategic Planning
> **Month**: <% tp.date.now("MMMM YYYY") %>
> **Focus**: Queue health, maturity progression, system optimization
> **Status**: `VIEW[{completed}][toggle]`

---

## 📊 Monthly Queue Health Report

```dataviewjs
const today = dv.date("today");
const monthStart = today.startOf("month");
const monthEnd = today.endOf("month");
const lastMonth = monthStart.minus(dv.duration("1 month"));

// All active notes with review metadata
const allActiveNotes = dv.pages()
    .where(p => p.status === "active" && p.review);

// Notes due this month
const dueThisMonth = allActiveNotes
    .where(p =>
        p.review["next-review"] &&
        dv.date(p.review["next-review"]) >= monthStart &&
        dv.date(p.review["next-review"]) <= monthEnd
    );

// Overdue notes
const overdue = allActiveNotes
    .where(p =>
        p.review["next-review"] &&
        dv.date(p.review["next-review"]) < monthStart
    );

// Priority breakdown
const urgent = allActiveNotes.where(p => p.review.priority === "urgent");
const high = allActiveNotes.where(p => p.review.priority === "high");
const medium = allActiveNotes.where(p => p.review.priority === "medium");
const low = allActiveNotes.where(p => p.review.priority === "low");

// Overall health score
const healthScore = ((allActiveNotes.length - overdue.length) / allActiveNotes.length * 100).toFixed(1);

dv.header(3, "🎯 Overall Queue Health");
dv.paragraph(`**Total Active Notes**: ${allActiveNotes.length}`);
dv.paragraph(`**Due This Month**: ${dueThisMonth.length}`);
dv.paragraph(`**Overdue**: ${overdue.length} ${overdue.length > 0 ? '⚠️' : '✅'}`);
dv.paragraph(`**Health Score**: ${healthScore}% ${healthScore >= 80 ? '✅' : healthScore >= 60 ? '⚠️' : '🔴'}`);
dv.paragraph(`**By Priority**: 🔴 ${urgent.length} | 🟠 ${high.length} | 🟡 ${medium.length} | 🟢 ${low.length}`);

// Show critically overdue notes (>30 days)
const criticallyOverdue = overdue
    .where(p => (today - dv.date(p.review["next-review"])).days > 30)
    .sort(p => p.review["next-review"], "asc");

if (criticallyOverdue.length > 0) {
    dv.header(3, "🚨 Critically Overdue (>30 Days)");
    dv.table(
        ["Note", "Maturity", "Days Overdue", "Priority"],
        criticallyOverdue.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            Math.floor((today - dv.date(p.review["next-review"])).days),
            p.review.priority || "medium"
        ])
    );
}
```

---

## 🌱 Maturity Distribution & Progress

```dataviewjs
const today = dv.date("today");
const monthStart = today.startOf("month");
const lastMonth = monthStart.minus(dv.duration("1 month"));

// All notes with maturity
const allNotes = dv.pages()
    .where(p => p.maturity && p.status === "active");

// Current maturity distribution
const maturityCounts = {
    seedling: allNotes.where(p => p.maturity === "seedling").length,
    budding: allNotes.where(p => p.maturity === "budding").length,
    developing: allNotes.where(p => p.maturity === "developing").length,
    evergreen: allNotes.where(p => p.maturity === "evergreen").length,
    "needs-review": allNotes.where(p => p.maturity === "needs-review").length
};

dv.header(3, "📈 Current Maturity Distribution");
dv.table(
    ["Maturity Level", "Count", "Percentage"],
    Object.entries(maturityCounts).map(([level, count]) => [
        level.charAt(0).toUpperCase() + level.slice(1),
        count,
        ((count / allNotes.length) * 100).toFixed(1) + "%"
    ])
);

// Notes modified this month
const modifiedThisMonth = allNotes
    .where(p => p.file.mtime >= monthStart);

// Notes reviewed this month
const reviewedThisMonth = allNotes
    .where(p =>
        p.review &&
        p.review["last-reviewed"] &&
        dv.date(p.review["last-reviewed"]) >= monthStart
    );

dv.header(3, "📊 This Month's Activity");
dv.paragraph(`**Notes Modified**: ${modifiedThisMonth.length}`);
dv.paragraph(`**Notes Reviewed**: ${reviewedThisMonth.length}`);
dv.paragraph(`**Average Reviews per Note**: ${(reviewedThisMonth.map(p => p.review["review-count"] || 0).reduce((a, b) => a + b, 0) / reviewedThisMonth.length).toFixed(1)}`);
```

---

## 🎯 Strategic Review Priorities

### High-Value Notes Needing Attention

```dataviewjs
const today = dv.date("today");

// High-value notes = high backlink count + overdue/due soon
const allNotes = dv.pages()
    .where(p => p.status === "active" && p.review);

// Calculate value score (simple heuristic)
const highValueNotes = allNotes
    .where(p => {
        const backlinks = app.metadataCache.getBacklinksForFile(p.file.path);
        const backlinkCount = backlinks?.data ? Object.keys(backlinks.data).length : 0;
        const isOverdue = p.review["next-review"] && dv.date(p.review["next-review"]) < today;
        return (backlinkCount > 5 || p.review.priority === "high" || p.review.priority === "urgent") && isOverdue;
    })
    .sort(p => {
        const backlinks = app.metadataCache.getBacklinksForFile(p.file.path);
        return backlinks?.data ? Object.keys(backlinks.data).length : 0;
    }, "desc")
    .limit(20);

if (highValueNotes.length > 0) {
    dv.header(4, "💎 High-Value Overdue Notes");
    dv.table(
        ["Note", "Maturity", "Priority", "Days Overdue"],
        highValueNotes.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            p.review.priority || "medium",
            Math.floor((today - dv.date(p.review["next-review"])).days)
        ])
    );
} else {
    dv.paragraph("✅ No high-value notes are overdue!");
}
```

### Seedlings Ready for Promotion

```dataviewjs
const today = dv.date("today");

// Seedlings with multiple reviews = ready for promotion
const matureSeedlings = dv.pages()
    .where(p =>
        p.status === "active" &&
        p.maturity === "seedling" &&
        p.review &&
        p.review["review-count"] >= 3
    )
    .sort(p => p.review["review-count"], "desc");

if (matureSeedlings.length > 0) {
    dv.header(4, "🌱→🌿 Seedlings Ready for Promotion");
    dv.table(
        ["Note", "Reviews", "Last Reviewed"],
        matureSeedlings.map(p => [
            p.file.link,
            p.review["review-count"],
            p.review["last-reviewed"] || "never"
        ])
    );
}
```

---

## 🔄 Monthly Actions

### Critical Tasks
- [ ] Clear all critically overdue notes (>30 days)
- [ ] Review and promote mature seedlings
- [ ] Update high-value notes
- [ ] Archive or deprecate stale notes

### System Maintenance
- [ ] Run metadata health check
- [ ] Optimize review intervals based on patterns
- [ ] Update domain-specific queues
- [ ] Review priority calculations

### Strategic Planning
- [ ] Identify knowledge gaps
- [ ] Set next month's review goals
- [ ] Adjust maturity progression criteria
- [ ] Plan new note development areas

---

## 📝 Monthly Reflections

### Knowledge Development Highlights
**Most Active Areas**:
-

**Significant Progressions**:
-

**New Connections**:
-

### System Performance
**What's Working Well**:
-

**Areas for Improvement**:
-

**Workflow Adjustments Needed**:
-

### Next Month's Focus
**Priority Domains**:
-

**Notes to Develop**:
-

**System Enhancements**:
-

---

## 📈 Session Statistics

**Notes Reviewed**: `INPUT[number:notes-reviewed]`
**Notes Promoted**: `INPUT[number]`
**Notes Archived**: `INPUT[number]`
**Session Duration**: `INPUT[number:session-duration]` minutes
**Completion Status**: `INPUT[toggle:completed]`

---

## 🔗 Navigation

← [[<% tp.date.now("YYYY-MM", -30, "YYYY-MM") %>|Previous Month]] | [[05-tasks-&-reviews/review-dashboard|Review Dashboard]] | [[<% tp.date.now("YYYY-MM", 30, "YYYY-MM") %>|Next Month]] →

---

## 📅 Related

**Quarterly Review**: [[<% tp.date.now("YYYY-[Q]Q") %>]]
**This Month's Weekly Reviews**:
- Week 1: [[<% tp.date.now("YYYY-MM-01", 0, "YYYY-[W]WW") %>]]
- Week 2: [[<% tp.date.now("YYYY-MM-08", 0, "YYYY-[W]WW") %>]]
- Week 3: [[<% tp.date.now("YYYY-MM-15", 0, "YYYY-[W]WW") %>]]
- Week 4: [[<% tp.date.now("YYYY-MM-22", 0, "YYYY-[W]WW") %>]]
