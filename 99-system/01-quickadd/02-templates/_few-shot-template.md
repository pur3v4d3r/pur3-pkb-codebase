<%*
// FILE NAMING AUTOMATION
// Convention: few-shot-[semantic-title]-[version]-[timestamp].md
// Example: few-shot-sentiment-analysis-1.0.0-20251220143022.md

// 1. Prompt for semantic title
const semanticTitle = await tp.system.prompt("Few-shot prompt title (e.g., 'sentiment-analysis', 'code-refactor'):");
if (!semanticTitle) {
    throw new Error("❌ Cancelled: No title provided");
}

// 2. Sanitize title (lowercase, replace spaces with hyphens, remove special chars)
const sanitized = semanticTitle
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^a-z0-9-]/g, '')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');

// 3. Fixed prefix for few-shot prompts
const prefix = "few-shot";

// 4. Generate version and timestamp
const version = "1.0.0";
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");

// 5. Construct filename
const filename = `${prefix}-${sanitized}-${version}-${timestamp}`;

// 6. Rename file
await tp.file.rename(filename);
_%>
---
type: "few-shot"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
status: "<% await tp.system.suggester(["Active", "Testing", "Production", "Deprecated", "Archived"], ["active", "testing", "production", "deprecated", "archived"], false, "Status?") %>"
version: "1.0.0"
rating: "0.0"
source: "<% await tp.system.suggester(["Claude Sonnet 4.5", "Claude Opus 4.5", "Gemini 3.0 Pro", "Gemini 3.0 Flash", "Original (Pur3v4d3r)", "Local LLM", "Other"], ["claude-sonnet-4.5", "claude-opus-4.5", "gemini-3.0-pro", "gemini-3.0-flash", "original", "local-llm", "other"], false, "Source of prompt?") %>"
created: "<% tp.date.now("YYYY-MM-DD") %>"
modified: "<% tp.date.now("YYYY-MM-DD") %>"
usage-count: 0
last-used: ""
review-next: "<% tp.date.now("YYYY-MM-DD", 7) %>"
review-interval: 7
review-count: 0
confidence: "<% await tp.system.suggester(["Speculative", "Provisional", "Moderate", "Established", "High"], ["speculative", "provisional", "moderate", "established", "high"], false, "Confidence level?") %>"
maturity: "seedling"
priority: "<% await tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["low", "medium", "high", "urgent"], false, "Priority?") %>"
example-count: 0
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering"
  - "few-shot-learning"
  - "llm-capability/pattern-matching"
  - "prompt-workflow/demonstration"
aliases:
  - "<% tp.file.title %>"
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
  - "[[<% tp.date.now("gggg-[W]WW") %>|Weekly Review]]"
components-used: []
test-results: []
---

> [!usage] Template Usage Instructions
> **Purpose**: Example-based learning prompts that teach models through input-output demonstrations.
>
> **How to Use**:
> 1. Define the **Task Description** (what pattern to learn)
> 2. Provide **3-5 Example Pairs** (input → output demonstrations)
> 3. Explain the **Pattern** (what the examples teach)
> 4. Include **New Input Section** (for model to apply learning)
>
> **Few-Shot Characteristics**:
> - Teaches by demonstration rather than instruction
> - Typically 3-5 examples (optimal range)
> - Examples should cover edge cases and variations
> - Pattern should be inferrable from examples
>
> **Best Practices**:
> - Use diverse examples that cover the problem space
> - Maintain consistent formatting across examples
> - Include edge cases in your example set
> - Balance between complexity and clarity

> [!metadata] Metadata Health Check
> **Type**: `VIEW[{type}]`
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Maturity**: `VIEW[{maturity}]` | **Confidence**: `VIEW[{confidence}]` | **Priority**: `VIEW[{priority}]`
> **Usage Count**: `VIEW[{usage-count}]` | **Example Count**: `VIEW[{example-count}]`
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

[Initial Creation: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]]

---

# <% tp.file.title %>

> [!abstract] Purpose
> <!-- Brief description of what pattern this few-shot prompt teaches -->
> <% tp.file.cursor(1) %>

## 🎯 Use Cases

<!-- When should this few-shot pattern be used? -->
- <% tp.file.cursor(2) %>

## 🚫 When NOT to Use

<!-- Scenarios where this few-shot approach is inappropriate -->
- <% tp.file.cursor(3) %>

---

## 📝 FEW-SHOT PROMPT CONTENT

### 1. TASK DESCRIPTION

<!-- Clear explanation of the task the model should learn -->
```markdown
<% tp.file.cursor(4) %>

**Objective**:


**Expected Behavior**:


**Key Considerations**:
-
-
-
```

---

### 2. EXAMPLE PAIRS

<!-- Provide 3-5 high-quality input-output demonstrations -->

#### Example 1

**Input**:
```
<% tp.file.cursor(5) %>
```

**Output**:
```
<% tp.file.cursor(6) %>
```

**Why This Example**:
<!-- Explain what this example teaches -->
-

---

#### Example 2

**Input**:
```
<% tp.file.cursor(7) %>
```

**Output**:
```

```

**Why This Example**:
<!-- Explain what this example teaches (edge case, variation, etc.) -->
-

---

#### Example 3

**Input**:
```

```

**Output**:
```

```

**Why This Example**:
-

---

#### Example 4 (Optional)

**Input**:
```

```

**Output**:
```

```

**Why This Example**:
-

---

#### Example 5 (Optional)

**Input**:
```

```

**Output**:
```

```

**Why This Example**:
-

---

### 3. PATTERN EXPLANATION

<!-- Explicit explanation of the pattern being taught -->
```markdown
**Core Pattern**:
<% tp.file.cursor(8) %>

**Key Features to Notice**:
1.
2.
3.

**Variations Demonstrated**:
-
-

**Edge Cases Covered**:
-
-

**Common Mistakes to Avoid**:
-
-
```

---

### 4. NEW INPUT SECTION

<!-- Where user/model applies the learned pattern -->
```markdown
Now apply the same pattern to this new input:

**Input**:
[USER INPUT HERE]

**Output**:

```

---

## 🧩 COMPONENTS USED

<!-- Link to reusable components from library -->
<!-- Use Component Search macro to find and insert -->
<!-- Update components-used in frontmatter -->

**Example Templates**:
-

**Pattern Framers**:
-

**Task Descriptions**:
-

**Format Specifications**:
-

---

## 🧪 TESTING & VALIDATION

### Test 1: [Date]
**Objective**: Test pattern recognition
**Test Input**:
**Expected Output**:
**Actual Output**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

**Issues Found**:
-

**Link**: [[test-result-link]]

---

### Test 2: [Date]
**Objective**: Test edge case handling
**Test Input**:
**Expected Output**:
**Actual Output**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

---

### Version History

| Version | Date | Changes | Example Count | Quality Δ | Link |
|---------|------|---------|---------------|-----------|------|
| 1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | Initial creation | 3 | - | - |

---

## 📊 USAGE TRACKING

### Production Usage
<!-- Where and when this few-shot prompt was used -->

**Project/Context**:
**Date**:
**Input Type**:
**Output Quality**:
**Outcome**:

---

### Performance Notes
<!-- Observations about effectiveness -->

**Pattern Recognition Quality**:
-

**Generalization Ability**:
-

**Example Quality**:
- Which examples were most effective:
- Which examples were confusing:

**Improvement Ideas**:
-

---

## 🔗 RELATED PROMPTS

```dataviewjs
// Semantic Bridge: Find related few-shot prompts
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

const siblings = dv.pages()
    .where(p => (p.type === "few-shot" || p.type === "component"))
    .where(p => p.file.path !== current.file.path)
    .map(p => {
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return {
            link: p.file.link,
            type: p.type,
            rating: p.rating || 0,
            exampleCount: p["example-count"] || 0,
            sharedCount: shared.length
        };
    })
    .where(p => p.sharedCount > 0)
    .sort(p => p.sharedCount, "desc")
    .limit(5);

if (siblings.length > 0) {
    dv.header(4, "🌉 Similar Few-Shot Prompts (Shared Context)");
    dv.table(
        ["Prompt", "Type", "Rating", "Examples", "Shared Links"],
        siblings.map(s => [s.link, s.type, s.rating + "/10", s.exampleCount, "🔗 " + s.sharedCount])
    );
} else {
    dv.paragraph("*No related few-shot prompts found yet.*");
}
```

### Manual Links
<!-- Add links to related prompts, workflows, or projects -->
-

---

## 💡 OPTIMIZATION LOG

### Optimization Attempt: [Date]
**Hypothesis**: (e.g., "Adding a 4th example covering X will improve accuracy")
**Changes Made**:
- Example added/modified:
- Pattern explanation updated:

**Result**:
**New Rating**: /10
**Keep Changes?**: Yes | No

---

## 🎓 LESSONS LEARNED

<!-- Document insights for future few-shot creation -->

**Example Selection**:
-

**Pattern Clarity**:
-

**Edge Case Coverage**:
-

**Optimal Example Count**:
-

**Key Insights**:
-

---

## 📋 QUICK ACTIONS

**Meta-Bind Buttons** (if configured):
- `BUTTON[increment-usage]` - Increment usage count
- `BUTTON[add-example]` - Add new example pair
- `BUTTON[run-test]` - Quick test documentation
- `BUTTON[bump-version]` - Version increment
- `BUTTON[archive]` - Move to archive

---

## 📚 REFERENCES & RESOURCES

<!-- Links to documentation, research, examples -->

**Few-Shot Learning Research**:
-

**Pattern Sources**:
-

**Related Techniques**:
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | Few-Shot Template*
