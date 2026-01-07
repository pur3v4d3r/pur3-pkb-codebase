---
type: "prompt"
id: "20260106211348"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-sonnet-4.5"
created: "2026-01-06"
modified: "2026-01-06"
usage-count: 0
last-used: ""
review-next: "2026-01-13"
review-interval: 7
review-count: 0
confidence: "provisional"
maturity: "seedling"
priority: "low"
tags:
  - "year/2026"
  - "prompt-engineering"
  - "llm-capability/generation"
  - "prompt-workflow/creation"
aliases:
  - "prompt-academic-report-enhancement-agent-v1.0.0-2026010621"
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[2026-01-06|Daily Note]]"
  - "[[2026-W02|Weekly Review]]"
components-used: []
test-results: []
---

>[!usage] Template Usage Instructions
> **Purpose**: Master template for all prompt types. Provides consistent structure and metadata.
>
> **How to Use**:
> 1. Answer guided questions during creation
> 2. Fill in the prompt content sections below
> 3. Search component library for reusable blocks (`Ctrl+P` → "Component Search")
> 4. Test prompt and document results
> 5. Update rating and maturity as prompt evolves
>
> **Sections**:
> - Metadata Health Check: Auto-validates required fields
> - Prompt Content: Your actual prompt text
> - Components: Links to reusable building blocks
> - Testing: Test results and iterations
> - Usage: Track where/when this prompt is used
>
> **Tips**:
> - Use `` for manual input points
> - Link related prompts in `link-related`
> - Add component links to `components-used` for tracking
> - Bump version when making significant changes

> [!metadata] Metadata Health Check
> **Type**: `VIEW[{type}]`
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Maturity**: `VIEW[{maturity}]` | **Confidence**: `VIEW[{confidence}]` | **Priority**: `VIEW[{priority}]`
> **Usage Count**: `VIEW[{usage-count}]` | **Last Used**: `VIEW[{last-used}]`
>
> > [!temporal] 🕰️ Temporal Context
> > **Created**: `= this.file.ctime` | **Age**: `= (date(today) - this.file.ctime).days + " days"`
> > **Modified**: `= this.file.mtime` | **Staleness**: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
> > **Next Review**: `= this.review-next` | **Review Interval**: `= this.review-interval + " days"`
>
> > [!quality] 📊 Quality Metrics
> > **Word Count**: `= this.file.size` bytes | **Est. Read Time**: `= round(this.file.size / 1300) + " min"`
> > **Components Used**: `= length(this.components-used)` | **Test Results**: `= length(this.test-results)`
> > **Health Status**: `$= const fields = ["type", "status", "version", "source", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`
>
> > [!network] 🔗 Network Connectivity
> > **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> > **Network Status**: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
> > **Folder**: `= this.file.folder`

[Initial Creation: [[2026-01-06|Tuesday, January 6th, 2026]]]

---

# prompt-academic-report-enhancement-agent-v1.0.0-2026010621

> [!abstract] Purpose
> <!-- Brief description of what this prompt does -->
> <% tp.file.cursor(1) %>

## 🎯 Use Cases

<!-- When should this prompt be used? -->
- <% tp.file.cursor(2) %>

## 🚫 When NOT to Use

<!-- Scenarios where this prompt is inappropriate -->
- <% tp.file.cursor(3) %>

---

## 📝 PROMPT CONTENT

### Context & Background
<!-- Set the stage: What does the model need to know? -->
<% tp.file.cursor(4) %>

### Task & Instructions
<!-- Clear, specific directives -->
<% tp.file.cursor(5) %>

### Constraints & Guidelines
<!-- Boundaries, restrictions, principles -->
<% tp.file.cursor(6) %>

### Output Format
<!-- Structure of expected response -->
<% tp.file.cursor(7) %>

### Examples (Optional)
<!-- Few-shot demonstrations if needed -->
<% tp.file.cursor(8) %>

---

## 🧩 COMPONENTS USED

<!-- Link to reusable components from library -->
<!-- Use Component Search macro to find and insert -->
<!-- Update components-used in frontmatter -->

**Personas**:
-

**Instructions**:
-

**Constraints**:
-

**Formats**:
-

**Context Framers**:
-

---

## 🧪 TESTING & VALIDATION

### Test 1: [Date]
**Objective**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

**Issues Found**:
-

**Link**: [[test-result-link]]

---

### Version History

| Version | Date | Changes | Quality Δ | Link |
|---------|------|---------|-----------|------|
| 1.0.0 | 2026-01-06 | Initial creation | - | - |

---

## 📊 USAGE TRACKING

### Production Usage
<!-- Where and when this prompt was used -->

**Project/Context**:
**Date**:
**Outcome**:
**Notes**:

---

### Performance Notes
<!-- Observations about effectiveness -->

**Strengths**:
-

**Weaknesses**:
-

**Improvement Ideas**:
-

---

## 🔗 RELATED PROMPTS

```dataviewjs
// Semantic Bridge: Find related prompts
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

const siblings = dv.pages()
    .where(p => p.type === "prompt" || p.type === "component")
    .where(p => p.file.path !== current.file.path)
    .map(p => {
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return {
            link: p.file.link,
            type: p.type,
            rating: p.rating || 0,
            sharedCount: shared.length
        };
    })
    .where(p => p.sharedCount > 0)
    .sort(p => p.sharedCount, "desc")
    .limit(5);

if (siblings.length > 0) {
    dv.header(4, "🌉 Similar Prompts (Shared Context)");
    dv.table(
        ["Prompt", "Type", "Rating", "Shared Links"],
        siblings.map(s => [s.link, s.type, s.rating + "/10", "🔗 " + s.sharedCount])
    );
} else {
    dv.paragraph("*No related prompts found yet.*");
}
```

### Manual Links
<!-- Add links to related prompts, workflows, or projects -->
-

---

## 💡 OPTIMIZATION LOG

### Optimization Attempt: [Date]
**Hypothesis**:
**Changes Made**:
**Result**:
**New Rating**: /10
**Keep Changes?**: Yes | No

---

## 🎓 LESSONS LEARNED

<!-- Document insights for future prompt creation -->
-

---

## 📋 QUICK ACTIONS

**Meta-Bind Buttons** (if configured):
- `BUTTON[increment-usage]` - Increment usage count
- `BUTTON[run-test]` - Quick test documentation
- `BUTTON[bump-version]` - Version increment
- `BUTTON[archive]` - Move to archive

---

## 📚 REFERENCES & RESOURCES

<!-- Links to documentation, research, examples -->
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | Master Template for all prompts*
