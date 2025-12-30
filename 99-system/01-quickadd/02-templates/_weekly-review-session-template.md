---
tags:
  - review-session
  - type/weekly
  - year/<% tp.date.now("YYYY") %>
date: <% tp.date.now("YYYY-MM-DD") %>
review-type: weekly
completed: false
notes-reviewed: 0
session-duration: 0
type: review-session
week: "[[<% tp.date.now("YYYY-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
---

# 📅 Weekly Review Session: Week <% tp.date.now("[W]WW YYYY") %>

> [!abstract] Session Overview
> **Type**: Weekly Review
> **Week**: <% tp.date.now("YYYY-[W]WW") %>
> **Date Range**: <% tp.date.weekday("YYYY-MM-DD", 0) %> to <% tp.date.weekday("YYYY-MM-DD", 6) %>
> **Target**: Comprehensive review of notes due this week and queue health check
> **Status**: `VIEW[{completed}][toggle]`

---

## 🎯 This Week's Review Queue

```dataviewjs
const today = dv.date("today");
const weekStart = today.startOf("week");
const weekEnd = today.endOf("week");

// Find all notes due this week or overdue
const reviewQueue = dv.pages()
    .where(p =>
        p.status === "active" &&
        p.review &&
        p.review["next-review"] &&
        dv.date(p.review["next-review"]) <= weekEnd
    )
    .sort(p => {
        const priorities = {"urgent": 0, "high": 1, "medium": 2, "low": 3};
        return priorities[p.review.priority] || 2;
    }, "asc")
    .sort(p => p.review["next-review"], "asc");

// Calculate statistics
const overdue = reviewQueue.where(p => dv.date(p.review["next-review"]) < weekStart);
const dueThisWeek = reviewQueue.where(p => {
    const nextReview = dv.date(p.review["next-review"]);
    return nextReview >= weekStart && nextReview <= weekEnd;
});

// Group by priority
const urgent = reviewQueue.where(p => p.review.priority === "urgent");
const high = reviewQueue.where(p => p.review.priority === "high");
const medium = reviewQueue.where(p => p.review.priority === "medium");
const low = reviewQueue.where(p => p.review.priority === "low");

// Weekly summary
dv.header(3, "📊 Weekly Queue Summary");
dv.paragraph(`**Total in Queue**: ${reviewQueue.length} notes`);
dv.paragraph(`**Overdue**: ${overdue.length} notes ⚠️`);
dv.paragraph(`**Due This Week**: ${dueThisWeek.length} notes`);
dv.paragraph(`**By Priority**: 🔴 ${urgent.length} | 🟠 ${high.length} | 🟡 ${medium.length} | 🟢 ${low.length}`);

// Display overdue notes
if (overdue.length > 0) {
    dv.header(3, "⚠️ Overdue Notes (Priority Review)");
    dv.table(
        ["Note", "Maturity", "Days Overdue", "Priority", "Last Reviewed"],
        overdue.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            Math.floor((today - dv.date(p.review["next-review"])).days),
            p.review.priority || "medium",
            p.review["last-reviewed"] || "never"
        ])
    );
}

// Display this week's notes by priority
if (urgent.length > 0) {
    dv.header(3, "🔴 Urgent Priority");
    dv.table(
        ["Note", "Maturity", "Next Review", "Interval"],
        urgent.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            p.review["next-review"],
            (p.review["review-interval"] || 7) + " days"
        ])
    );
}

if (high.length > 0) {
    dv.header(3, "🟠 High Priority");
    dv.table(
        ["Note", "Maturity", "Next Review", "Count"],
        high.map(p => [
            p.file.link,
            p.review.maturity || "unknown",
            p.review["next-review"],
            p.review["review-count"] || 0
        ])
    );
}

if (medium.length > 0) {
    dv.header(3, "🟡 Medium Priority");
    dv.list(medium.map(p => `${p.file.link} (${p.review["next-review"]})`));
}
```

---

## 📈 Maturity Progress This Week

```dataviewjs
const today = dv.date("today");
const weekAgo = today.minus(dv.duration("7 days"));

// Find notes modified this week
const modifiedThisWeek = dv.pages()
    .where(p =>
        p.file.mtime >= weekAgo &&
        p.maturity
    );

// Group by maturity
const byMaturity = modifiedThisWeek.groupBy(p => p.maturity);

dv.header(3, "🌱 Notes Modified This Week by Maturity");
for (let group of byMaturity) {
    dv.paragraph(`**${group.key}**: ${group.rows.length} notes`);
}

// Show recently promoted notes
const recentlyPromoted = modifiedThisWeek
    .where(p =>
        p.review &&
        p.review["review-count"] &&
        p.review["review-count"] > 0
    )
    .sort(p => p.file.mtime, "desc")
    .limit(10);

if (recentlyPromoted.length > 0) {
    dv.header(3, "⬆️ Recently Reviewed Notes");
    dv.table(
        ["Note", "Maturity", "Reviews", "Last Modified"],
        recentlyPromoted.map(p => [
            p.file.link,
            p.maturity,
            p.review["review-count"],
            p.file.mtime.toFormat("yyyy-MM-dd")
        ])
    );
}
```

---

## 🔄 Weekly Actions

**This Week's Focus**:
- [ ] Clear all overdue reviews
- [ ] Complete all urgent priority reviews
- [ ] Process high priority notes
- [ ] Update quarterly goals (if applicable)

**Review Commands**:
- Use `/quick-review` to review individual notes
- Mark notes for batch rescheduling if needed

---

## 📝 Weekly Reflections

### Knowledge Gaps Identified
-

### Connections Discovered
-

### Notes to Develop Further
-

### System Improvements
-

---

## 📈 Session Statistics

**Notes Reviewed**: `INPUT[number:notes-reviewed]`
**Session Duration**: `INPUT[number:session-duration]` minutes
**Completion Status**: `INPUT[toggle:completed]`

---

## 🔗 Navigation

← [[<% tp.date.now("YYYY-[W]WW", -7, "YYYY-[W]WW") %>|Previous Week]] | [[05-tasks-&-reviews/review-dashboard|Review Dashboard]] | [[<% tp.date.now("YYYY-[W]WW", 7, "YYYY-[W]WW") %>|Next Week]] →

---

## 📅 Related

**Monthly Review**: [[<% tp.date.now("YYYY-MM") %>]]
**Daily Notes This Week**:
- [[<% tp.date.weekday("YYYY-MM-DD", 0) %>|Monday]]
- [[<% tp.date.weekday("YYYY-MM-DD", 1) %>|Tuesday]]
- [[<% tp.date.weekday("YYYY-MM-DD", 2) %>|Wednesday]]
- [[<% tp.date.weekday("YYYY-MM-DD", 3) %>|Thursday]]
- [[<% tp.date.weekday("YYYY-MM-DD", 4) %>|Friday]]
- [[<% tp.date.weekday("YYYY-MM-DD", 5) %>|Saturday]]
- [[<% tp.date.weekday("YYYY-MM-DD", 6) %>|Sunday]]
