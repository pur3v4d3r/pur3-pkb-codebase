---
tags: #dashboard #prompt-engineering #overview
aliases: [PE Dashboard, Prompt Library, Component Library]
status: evergreen
created: 2025-12-20
modified: 2025-12-20
link-up: "[[00-prompt-engineering-system-design]]"
---

# Prompt Engineering Dashboard

> [!abstract] Command Center
> Master overview of all prompts, components, tests, and analytics. Your daily starting point for prompt engineering work.

---

## 🎯 QUICK ACTIONS

**Create**:
- `Ctrl+P` → "Templater: Create new note from template" → Select prompt type
- `Ctrl+P` → "QuickAdd: Prompt Quick Capture" → <10 second idea capture

**Search**:
- `Ctrl+P` → "QuickAdd: Component Search & Insert" → Find library components
- `Ctrl+O` → Search by name
- Use queries below to browse by type/status

**View**:
- [[00-library-index|Component Library Index]]
- [[03-metadata-schema-reference|Metadata Schema]]
- [[02-quick-reference-guide|Quick Reference]]

---

## 📊 LIBRARY STATISTICS

```dataviewjs
// Calculate statistics
const prompts = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system/08-active-prompts" or "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"')
    .where(p => p.type === "prompt");
const components = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system/02-component-library"')
    .where(p => p.type === "component");
const tests = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system/05-testing-validation"')
    .where(p => p.type === "test-result");
const ideas = dv.pages('"00-inbox/prompt-ideas"')
    .where(p => p.type === "idea");

// Quality metrics
const ratedPrompts = prompts.where(p => p.rating > 0);
const avgRating = ratedPrompts.length > 0
    ? (ratedPrompts.array().map(p => parseFloat(p.rating || 0)).reduce((a, b) => a + b, 0) / ratedPrompts.length).toFixed(1)
    : "N/A";

const productionPrompts = prompts.where(p => p.status === "production").length;
const testingPrompts = prompts.where(p => p.status === "testing").length;

// Total component usage (convert to array first)
const totalUsage = components.array().map(c => c["usage-count"] || 0).reduce((a, b) => a + b, 0);

dv.header(3, "📈 Overview");
dv.paragraph(`
**Total Prompts**: ${prompts.length} | **Components**: ${components.length} | **Tests**: ${tests.length} | **Ideas**: ${ideas.length}

**Quality Metrics**:
- Average Rating: **${avgRating}/10** (${ratedPrompts.length} rated)
- Production: **${productionPrompts}** | Testing: **${testingPrompts}**
- Total Component Usage: **${totalUsage}**
`);
```

---

## 🆕 RECENT ACTIVITY (Last 7 Days)

### New Prompts
```dataview
TABLE type as "Type", status, rating, created
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt" AND date(created) >= date(today) - dur(7 days)
SORT created DESC
LIMIT 10
```

### New Components
```dataview
TABLE component-type as "Type", domain, rating, created
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND date(created) >= date(today) - dur(7 days)
SORT created DESC
LIMIT 10
```

### Recent Tests
```dataview
TABLE prompt-tested, test-type, success, quality-score
FROM "02-projects/_spes-sequential-prompt-engineering-system/05-testing-validation"
WHERE type = "test-result" AND date(test-date) >= date(today) - dur(7 days)
SORT test-date DESC
LIMIT 10
```

---

## ⭐ TOP PERFORMERS

### Highest Rated Prompts
```dataview
TABLE status, rating, usage-count, maturity
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt" AND rating > 0
SORT rating DESC, usage-count DESC
LIMIT 10
```

### Most Used Components
```dataview
TABLE component-type, domain, usage-count, performance-score, rating
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND usage-count > 0
SORT usage-count DESC, rating DESC
LIMIT 10
```

---

## 💡 IDEA BACKLOG

### Captured Ideas Awaiting Development
```dataview
TABLE idea-type, created, file.size as "Notes"
FROM "00-inbox/prompt-ideas"
WHERE type = "idea"
SORT created DESC
LIMIT 20
```

**Quick Actions**:
- Click idea to open and develop
- Use master template to promote to full prompt
- Archive ideas that are no longer relevant

---

## 📂 BROWSE BY TYPE

### System Prompts
```dataview
TABLE status, rating, usage-count, last-used
FROM "02-projects/_spes-sequential-prompt-engineering-system/08-active-prompts"
WHERE type = "prompt" AND contains(tags, "prompt-workflow") AND file.name != "00-library-index"
SORT rating DESC
LIMIT 15
```

### Components by Category

**Personas**:
```dataview
TABLE domain, rating, usage-count
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND component-type = "persona"
SORT rating DESC
LIMIT 5
```

**Instructions**:
```dataview
TABLE domain, rating, usage-count
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND component-type = "instruction"
SORT rating DESC
LIMIT 5
```

**Constraints**:
```dataview
TABLE domain, rating, usage-count
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND component-type = "constraint"
SORT rating DESC
LIMIT 5
```

---

## 🔧 MAINTENANCE & HEALTH

### Prompts Needing Review
```dataview
TABLE review-next, maturity, last-used, usage-count
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt" AND review-next <= date(today)
SORT review-next ASC
LIMIT 10
```

### Orphaned Components (No Usage)
```dataview
TABLE component-type, domain, created, rating
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND usage-count = 0 AND (date(today) - date(created)).days > 30
SORT created ASC
LIMIT 10
```

### Low-Rated Items (Need Improvement)
```dataview
TABLE rating, usage-count, status
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE (type = "prompt" OR type = "component") AND rating > 0 AND rating < 5
SORT rating ASC
LIMIT 10
```

### Metadata Health Issues
```dataviewjs
// Check for common metadata issues
const allNotes = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system"')
    .where(p => p.type === "prompt" || p.type === "component");

const issues = [];

allNotes.forEach(note => {
    // Missing required fields
    const required = ["type", "id", "status", "version", "rating", "created"];
    const missing = required.filter(field => !note[field]);

    if (missing.length > 0) {
        issues.push({
            file: note.file.link,
            issue: "Missing fields: " + missing.join(", ")
        });
    }

    // Invalid rating
    if (note.rating && (note.rating < 0 || note.rating > 10)) {
        issues.push({
            file: note.file.link,
            issue: "Invalid rating: " + note.rating
        });
    }

    // Old without usage
    const daysSinceCreated = (Date.now() - new Date(note.created)) / (1000 * 60 * 60 * 24);
    if (daysSinceCreated > 90 && (!note["usage-count"] || note["usage-count"] === 0)) {
        issues.push({
            file: note.file.link,
            issue: "90+ days old, never used"
        });
    }
});

if (issues.length > 0) {
    dv.header(4, "⚠️ Health Issues Found");
    dv.table(
        ["File", "Issue"],
        issues.slice(0, 15).map(i => [i.file, i.issue])
    );
} else {
    dv.paragraph("✅ **All Systems Go** - No health issues detected!");
}
```

---

## 📈 USAGE ANALYTICS

### Most Active This Week
```dataviewjs
const weekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
const recentlyUsed = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system"')
    .where(p => (p.type === "prompt" || p.type === "component") && p["last-used"])
    .where(p => {
        try {
            const lastUsed = p["last-used"];
            // Extract date from wiki-link format [[YYYY-MM-DD]]
            const dateMatch = lastUsed.match(/\d{4}-\d{2}-\d{2}/);
            if (dateMatch) {
                return new Date(dateMatch[0]) >= weekAgo;
            }
        } catch (e) {
            return false;
        }
        return false;
    })
    .sort(p => p["last-used"], "desc")
    .limit(10);

if (recentlyUsed.length > 0) {
    dv.header(4, "🔥 Active This Week");
    dv.table(
        ["Item", "Type", "Usage Count", "Last Used"],
        recentlyUsed.map(p => [
            p.file.link,
            p.type,
            p["usage-count"] || 0,
            p["last-used"]
        ])
    );
} else {
    dv.paragraph("*No usage recorded this week*");
}
```

### Maturity Distribution
```dataviewjs
const allPrompts = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system"')
    .where(p => p.type === "prompt");

const maturityCounts = {
    seedling: allPrompts.where(p => p.maturity === "seedling").length,
    developing: allPrompts.where(p => p.maturity === "developing").length,
    budding: allPrompts.where(p => p.maturity === "budding").length,
    evergreen: allPrompts.where(p => p.maturity === "evergreen").length
};

dv.header(4, "🌱 Maturity Stages");
dv.paragraph(`
- **Seedling**: ${maturityCounts.seedling} (${((maturityCounts.seedling / allPrompts.length) * 100).toFixed(0)}%)
- **Developing**: ${maturityCounts.developing} (${((maturityCounts.developing / allPrompts.length) * 100).toFixed(0)}%)
- **Budding**: ${maturityCounts.budding} (${((maturityCounts.budding / allPrompts.length) * 100).toFixed(0)}%)
- **Evergreen**: ${maturityCounts.evergreen} (${((maturityCounts.evergreen / allPrompts.length) * 100).toFixed(0)}%)
`);
```

---

## 🔍 SEARCH & FILTERS

### By Status
```dataview
LIST
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt" AND status = "production"
SORT rating DESC
```

### By Confidence
```dataview
TABLE confidence, rating, maturity
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt" AND confidence = "high"
SORT rating DESC
```

### By Domain
```dataview
TABLE domain, component-type, rating
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND domain = "technical"
SORT rating DESC
```

---

## 🎓 LEARNING & INSIGHTS

### Lessons Learned (Recent)
*Document patterns discovered from recent prompt engineering work*

### Recommended Next Actions
```dataviewjs
// Generate recommendations based on current state
const prompts = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system"')
    .where(p => p.type === "prompt");
const components = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system/02-component-library"')
    .where(p => p.type === "component");
const ideas = dv.pages('"00-inbox/prompt-ideas"').where(p => p.type === "idea");

const recommendations = [];

// Check for ideas awaiting development
if (ideas.length > 0) {
    recommendations.push(`📝 **Develop Ideas**: ${ideas.length} captured ideas waiting for full development`);
}

// Check for prompts needing testing
const untestedPrompts = prompts.where(p => p.status === "active" && (!p["test-results"] || p["test-results"].length === 0));
if (untestedPrompts.length > 0) {
    recommendations.push(`🧪 **Test Prompts**: ${untestedPrompts.length} prompts without test results`);
}

// Check for low-rated prompts
const lowRated = prompts.where(p => p.rating > 0 && p.rating < 6);
if (lowRated.length > 0) {
    recommendations.push(`⚠️ **Improve Quality**: ${lowRated.length} prompts rated below 6/10`);
}

// Check for unused components
const unusedComponents = components.where(p => p["usage-count"] === 0);
if (unusedComponents.length > 5) {
    recommendations.push(`🧹 **Review Library**: ${unusedComponents.length} components never used - test or archive`);
}

// Check for prompts needing review
const needsReview = prompts.where(p => p["review-next"] && p["review-next"] <= dv.date("today"));
if (needsReview.length > 0) {
    recommendations.push(`📅 **Review Prompts**: ${needsReview.length} prompts due for review`);
}

if (recommendations.length > 0) {
    dv.header(4, "💡 Recommended Actions");
    dv.list(recommendations);
} else {
    dv.paragraph("✅ **All caught up!** Library is in good health.");
}
```

---

## 🔗 RELATED RESOURCES

- **System Design**: [[00-prompt-engineering-system-design]]
- **Implementation Tracker**: [[01-implementation-tracker]]
- **Metadata Schema**: [[03-metadata-schema-reference]]
- **Quick Reference**: [[02-quick-reference-guide]]
- **Component Library**: [[00-library-index]]
- **SPES Architecture**: [[architecture-overview]]

---

*Dashboard auto-updates via Dataview | Version: 1.0.0 | Created: 2025-12-20*
