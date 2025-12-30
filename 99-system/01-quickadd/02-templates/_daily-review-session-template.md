---
tags:
  - review-session
  - type/daily
  - year/2025
date: 2025-12-14
review-type: daily
completed: false
notes-reviewed: 0
session-duration: 0
type: review-session
week: "2025-W50"
month: "2025-12"
quarter: "2025-Q4"
year: "2025"
---

# 📅 Daily Review Session: 2025-12-14

> [!abstract] Session Overview
> **Type**: Daily Review
> **Date**: 2025-12-14 (Sunday)
> **Target**: Review notes requiring attention based on maturity and priority
> **Status**: `VIEW[{completed}][toggle]`

---

## 🎯 Today's Review Queue

```dataviewjs
const today = dv.date("today");
const lookbackDays = 1; // Daily review looks at today's queue

// Find notes needing review (due today or overdue)
const reviewQueue = dv.pages()
    .where(p =>
        p.status === "active" &&
        p.review &&
        p.review["next-review"] &&
        dv.date(p.review["next-review"]) <= today
    )
    .sort(p => {
        const priorities = {"urgent": 0, "high": 1, "medium": 2, "low": 3};
        return priorities[p.review.priority] || 2;
    }, "asc")
    .sort(p => p.review["next-review"], "asc");

// Separate by priority
const urgent = reviewQueue.where(p => p.review.priority === "urgent");
const high = reviewQueue.where(p => p.review.priority === "high");
const medium = reviewQueue.where(p => p.review.priority === "medium");
const low = reviewQueue.where(p => p.review.priority === "low");

// Display urgent notes
if (urgent.length > 0) {
    dv.header(3, "🔴 Urgent Priority");
    dv.table(
        ["Note", "Maturity", "Days Overdue", "Last Reviewed", "Count"],
        urgent.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            Math.floor((today - dv.date(p.review["next-review"])).days),
            p.review["last-reviewed"] || "never",
            p.review["review-count"] || 0
        ])
    );
}

// Display high priority notes
if (high.length > 0) {
    dv.header(3, "🟠 High Priority");
    dv.table(
        ["Note", "Maturity", "Next Review", "Interval", "Count"],
        high.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            p.review["next-review"],
            (p.review["review-interval"] || 7) + " days",
            p.review["review-count"] || 0
        ])
    );
}

// Display medium priority notes
if (medium.length > 0) {
    dv.header(3, "🟡 Medium Priority");
    dv.table(
        ["Note", "Maturity", "Next Review"],
        medium.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            p.review["next-review"]
        ])
    );
}

// Display low priority notes (collapsed by default)
if (low.length > 0) {
    dv.header(3, "🟢 Low Priority (Optional)");
    dv.list(low.file.link);
}

// Queue summary
dv.header(3, "📊 Queue Summary");
dv.paragraph(`**Total Notes in Queue**: ${reviewQueue.length}`);
dv.paragraph(`**By Priority**: 🔴 ${urgent.length} | 🟠 ${high.length} | 🟡 ${medium.length} | 🟢 ${low.length}`);

// Overdue count
const overdue = reviewQueue.where(p => dv.date(p.review["next-review"]) < today);
if (overdue.length > 0) {
    dv.paragraph(`⚠️ **Overdue Notes**: ${overdue.length}`);
}
```

---

## 🔄 Quick Actions

**Review Commands**:
- Use `/quick-review` to review a note
- Mark session complete when finished
- Update `notes-reviewed` count below

---

## 📝 Session Notes

**Key Observations**:
-

**Patterns Noticed**:
-

**Follow-up Actions**:
- [ ]

---

## 📈 Session Statistics

**Notes Reviewed**: `INPUT[number:notes-reviewed]`
**Session Duration**: `INPUT[number:session-duration]` minutes
**Completion Status**: `INPUT[toggle:completed]`

---

## 🔗 Navigation

← [[2025-12-13|Previous Day]] | [[05-tasks-&-reviews/review-dashboard|Review Dashboard]] | [[2025-12-15|Next Day]] →

---

## 📅 Related

**Weekly Review**: [[2025-W50]]
**Monthly Review**: [[2025-12]]
**Daily Note**: [[2025-12-14]]
