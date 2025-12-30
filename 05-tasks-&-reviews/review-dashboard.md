---
tags:
  - dashboard
  - review-system
  - type/moc
  - year/2025
type: dashboard
cssclass: review-dashboard
---

# 🔄 PKB Review System Dashboard

> [!abstract] Overview
> Central hub for the Intelligent PKB Review System. This dashboard provides real-time visibility into your review queue, maturity progression, and knowledge maintenance patterns.

---

## 🎯 Quick Actions

**Start Review Session**:
- Daily: Use QuickAdd command → `_daily-review-session-template`
- Weekly: Use QuickAdd command → `_weekly-review-session-template`
- Monthly: Use QuickAdd command → `_monthly-review-session-template`

**Review Individual Note**:
- Use QuickAdd command → `_quick-review-template`

**System Maintenance**:
- [[#Metadata Health Check]]
- [[#Bulk Operations]]

---

## 📊 Current Queue Status

```dataviewjs
const today = dv.date("today");
const tomorrow = today.plus(dv.duration("1d"));
const nextWeek = today.plus(dv.duration("7d"));
const nextMonth = today.plus(dv.duration("30d"));

// Get all active notes with review metadata (flattened structure)
const allReviewNotes = dv.pages()
    .where(p => p.status === "active" && p["review-next-review"]);

// Calculate categories
const overdue = allReviewNotes
    .where(p => dv.date(p["review-next-review"]) < today);

const dueToday = allReviewNotes
    .where(p => {
        const nextReview = dv.date(p["review-next-review"]);
        return nextReview >= today && nextReview < tomorrow;
    });

const dueThisWeek = allReviewNotes
    .where(p => {
        const nextReview = dv.date(p["review-next-review"]);
        return nextReview >= tomorrow && nextReview <= nextWeek;
    });

const dueThisMonth = allReviewNotes
    .where(p => {
        const nextReview = dv.date(p["review-next-review"]);
        return nextReview > nextWeek && nextReview <= nextMonth;
    });

const upcoming = allReviewNotes
    .where(p => dv.date(p["review-next-review"]) > nextMonth);

// Priority breakdown (flattened structure)
const urgent = allReviewNotes.where(p => p["review-priority"] === "urgent");
const high = allReviewNotes.where(p => p["review-priority"] === "high");
const medium = allReviewNotes.where(p => p["review-priority"] === "medium");
const low = allReviewNotes.where(p => p["review-priority"] === "low");

// Health score
const totalNotes = allReviewNotes.length;
const healthScore = totalNotes > 0 ? ((totalNotes - overdue.length) / totalNotes * 100).toFixed(1) : 100;

// Display summary
dv.header(3, "📈 Queue Summary");
dv.paragraph(`**Total Active Notes**: ${totalNotes}`);
dv.paragraph(`**Health Score**: ${healthScore}% ${healthScore >= 80 ? '✅' : healthScore >= 60 ? '⚠️' : '🔴'}`);
dv.paragraph("");

dv.paragraph(`🔴 **Overdue**: ${overdue.length} notes`);
dv.paragraph(`📅 **Due Today**: ${dueToday.length} notes`);
dv.paragraph(`📆 **Due This Week**: ${dueThisWeek.length} notes`);
dv.paragraph(`📊 **Due This Month**: ${dueThisMonth.length} notes`);
dv.paragraph(`🟢 **Upcoming**: ${upcoming.length} notes`);
dv.paragraph("");

dv.paragraph(`**By Priority**: 🔴 ${urgent.length} | 🟠 ${high.length} | 🟡 ${medium.length} | 🟢 ${low.length}`);
```

---

## 🔴 Overdue & Urgent (Immediate Action)

```dataviewjs
const today = dv.date("today");

// Overdue notes (flattened structure)
const overdue = dv.pages()
    .where(p =>
        p.status === "active" &&
        p["review-next-review"] &&
        dv.date(p["review-next-review"]) < today
    )
    .sort(p => {
        const priorities = {"urgent": 0, "high": 1, "medium": 2, "low": 3};
        return priorities[p["review-priority"]] || 2;
    }, "asc")
    .sort(p => p["review-next-review"], "asc")
    .limit(20);

if (overdue.length > 0) {
    dv.table(
        ["Note", "Maturity", "Priority", "Days Overdue", "Last Reviewed"],
        overdue.map(p => [
            p.file.link,
            p.maturity || "unknown",
            p["review-priority"] || "medium",
            Math.floor((today - dv.date(p["review-next-review"])).days),
            p["review-last-reviewed"] || "never"
        ])
    );
} else {
    dv.paragraph("✅ No overdue notes! Great job!");
}
```

---

## 📅 Due Today

```dataviewjs
const today = dv.date("today");
const tomorrow = today.plus(dv.duration("1d"));

const dueToday = dv.pages()
    .where(p =>
        p.status === "active" &&
        p["review-next-review"] &&
        dv.date(p["review-next-review"]) >= today &&
        dv.date(p["review-next-review"]) < tomorrow
    )
    .sort(p => {
        const priorities = {"urgent": 0, "high": 1, "medium": 2, "low": 3};
        return priorities[p["review-priority"]] || 2;
    }, "asc");

if (dueToday.length > 0) {
    dv.table(
        ["Note", "Maturity", "Priority", "Interval"],
        dueToday.map(p => [
            p.file.link,
            p.maturity || "unknown",
            p["review-priority"] || "medium",
            (p["review-interval"] || 7) + " days"
        ])
    );
} else {
    dv.paragraph("📭 No notes due today");
}
```

---

## 📆 Possible Reviews, for This Week

```dataviewjs
const today = dv.date("today");
const nextWeek = today.plus(dv.duration("7d"));

const dueThisWeek = dv.pages()
    .where(p =>
        p.status === "active" &&
        p["review-next-review"] &&
        dv.date(p["review-next-review"]) > today &&
        dv.date(p["review-next-review"]) <= nextWeek
    )
    .sort(p => p["review-next-review"], "asc")
    .limit(30);

if (dueThisWeek.length > 0) {
    dv.table(
        ["Note", "Maturity", "Next Review", "Priority"],
        dueThisWeek.map(p => [
            p.file.link,
            p.maturity || "unknown",
            p["review-next-review"],
            p["review-priority"] || "medium"
        ])
    );
} else {
    dv.paragraph("📭 No notes due this week");
}
```

---

## 🌱 Maturity Distribution

```dataviewjs
const allNotes = dv.pages()
    .where(p => p.maturity && p.status === "active");

const maturityCounts = {
    seedling: allNotes.where(p => p.maturity === "seedling").length,
    budding: allNotes.where(p => p.maturity === "budding").length,
    developing: allNotes.where(p => p.maturity === "developing").length,
    evergreen: allNotes.where(p => p.maturity === "evergreen").length,
    "needs-review": allNotes.where(p => p.maturity === "needs-review").length
};

dv.table(
    ["Maturity Level", "Count", "Percentage"],
    Object.entries(maturityCounts).map(([level, count]) => [
        level.charAt(0).toUpperCase() + level.slice(1),
        count,
        allNotes.length > 0 ? ((count / allNotes.length) * 100).toFixed(1) + "%" : "0%"
    ])
);

// Show seedlings ready for promotion (flattened structure)
const matureSeedlings = allNotes
    .where(p =>
        p.maturity === "seedling" &&
        p["review-count"] >= 3
    );

if (matureSeedlings.length > 0) {
    dv.header(4, "🌱→🌿 Seedlings Ready for Promotion");
    dv.list(matureSeedlings.file.link);
}
```

---

## 📊 Domain-Specific Queues

**Specialized Review Queues**:
- [[05-tasks-&-reviews/domain-queues/cognitive-science-review-queue|Cognitive Science Queue]]
- [[05-tasks-&-reviews/domain-queues/pkm-review-queue|PKM/PKB Queue]]
- [[05-tasks-&-reviews/domain-queues/philosophy-review-queue|Philosophy Queue]]

---

## 🔧 System Tools

### Metadata Health Check

```dataviewjs
// Find notes missing review metadata (flattened structure)
const allActiveNotes = dv.pages()
    .where(p => p.status === "active" || (p.type && !p.status));

const withReview = allActiveNotes.where(p => p["review-next-review"]);
const withoutReview = allActiveNotes.where(p => !p["review-next-review"]);

const missingMaturity = allActiveNotes.where(p => !p.maturity);
const missingConfidence = allActiveNotes.where(p => !p.confidence);
const missingStatus = allActiveNotes.where(p => !p.status);

dv.paragraph(`**Notes with Review Metadata**: ${withReview.length} / ${allActiveNotes.length}`);
dv.paragraph(`**Coverage**: ${allActiveNotes.length > 0 ? ((withReview.length / allActiveNotes.length) * 100).toFixed(1) : 0}%`);
dv.paragraph("");
dv.paragraph(`⚠️ **Missing review metadata**: ${withoutReview.length} notes`);
dv.paragraph(`⚠️ **Missing maturity**: ${missingMaturity.length} notes`);
dv.paragraph(`⚠️ **Missing confidence**: ${missingConfidence.length} notes`);
dv.paragraph(`⚠️ **Missing status**: ${missingStatus.length} notes`);

if (withoutReview.length > 0) {
    dv.header(4, "Notes Without Review Metadata (sample)");
    dv.list(withoutReview.limit(10).file.link);
    if (withoutReview.length > 10) {
        dv.paragraph(`... and ${withoutReview.length - 10} more`);
    }
}
```

### Bulk Operations

**Available Scripts**:
- Run bulk metadata update: `bulk-update-review-metadata.js`
- Calculate priorities: `calculate-priority.js`
- Review amnesty (reschedule overdue): Coming soon

---

## 📈 Review Analytics

**Full Analytics Dashboard**: [[06-dashboards/review-analytics-dashboard|Review Analytics Dashboard]]

**Quick Stats (Last 30 Days)**:

```dataviewjs
const today = dv.date("today");
const thirtyDaysAgo = today.minus(dv.duration("30d"));

// Find review session notes
const reviewSessions = dv.pages('#review-session')
  .where(p => p.date && dv.date(p.date) >= thirtyDaysAgo);

const totalSessions = reviewSessions.length;
const completedSessions = reviewSessions.where(p => p.completed === true).length;

// Fix: Convert to regular array before using reduce
const totalNotesReviewed = reviewSessions
  .where(p => p["notes-reviewed"])
  .map(p => p["notes-reviewed"])
  .array()
  .reduce((a, b) => a + b, 0);

dv.paragraph(`**Review Sessions**: ${totalSessions}`);
dv.paragraph(`**Completed Sessions**: ${completedSessions}`);
dv.paragraph(`**Total Notes Reviewed**: ${totalNotesReviewed}`);
dv.paragraph(`**Average Notes per Session**: ${totalSessions > 0 ? (totalNotesReviewed / totalSessions).toFixed(1) : 0}`);
```
---

## 📅 Recent Review Sessions

```dataviewjs
const recentSessions = dv.pages('#review-session')
    .sort(p => p.date, "desc")
    .limit(10);

if (recentSessions.length > 0) {
    dv.table(
        ["Date", "Type", "Notes Reviewed", "Duration (min)", "Completed"],
        recentSessions.map(p => [
            p.file.link,
            p["review-type"] || "unknown",
            p["notes-reviewed"] || 0,
            p["session-duration"] || 0,
            p.completed ? "✅" : "⏳"
        ])
    );
} else {
    dv.paragraph("No review sessions yet. Start your first review session!");
}
```

---

## 🔗 Navigation

**Review Templates**:
- [[99-system/01-quickadd/02-templates/_quick-review-template|Quick Review Template]]
- [[99-system/01-quickadd/02-templates/_daily-review-session-template|Daily Review Session]]
- [[99-system/01-quickadd/02-templates/_weekly-review-session-template|Weekly Review Session]]
- [[99-system/01-quickadd/02-templates/_monthly-review-session-template|Monthly Review Session]]

**System Documentation**:
- [[04-library/02-pkb-and-pkm-learning/-reference/reference-instructional-review-system-2025112923|Review System Guide]]
- [[06-dashboards/review-analytics-dashboard|Analytics Dashboard]]

**Related Hubs**:
- [[pkb-&-pkm-moc|PKB & PKM MOC]]
- [[cognitive-science-moc|Cognitive Science MOC]]
