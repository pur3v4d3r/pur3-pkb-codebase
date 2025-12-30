<%*
// FILE NAMING AUTOMATION
// Convention: cot-[semantic-title]-[version]-[timestamp].md
// Example: cot-math-problem-solving-1.0.0-20251220143022.md

// 1. Prompt for semantic title
const semanticTitle = await tp.system.prompt("Chain-of-thought prompt title (e.g., 'math-problem-solving', 'logical-reasoning'):");
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

// 3. Fixed prefix for chain-of-thought prompts
const prefix = "cot";

// 4. Generate version and timestamp
const version = "1.0.0";
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");

// 5. Construct filename
const filename = `${prefix}-${sanitized}-${version}-${timestamp}`;

// 6. Rename file
await tp.file.rename(filename);
_%>
---
type: "chain-of-thought"
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
reasoning-steps: 0
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering"
  - "chain-of-thought"
  - "llm-capability/reasoning"
  - "prompt-workflow/analysis"
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
> **Purpose**: Step-by-step reasoning prompts that guide models through explicit thinking processes.
>
> **How to Use**:
> 1. Define the **Problem Statement** (what needs reasoning)
> 2. Specify **Reasoning Steps** (explicit thought process)
> 3. Provide **Solution Template** (how to structure answer)
> 4. Include **Verification** (how to check correctness)
>
> **Chain-of-Thought Characteristics**:
> - Makes reasoning explicit and visible
> - Breaks complex problems into steps
> - Improves accuracy on complex tasks
> - Allows for error detection in reasoning
>
> **Best Practices**:
> - Use "Let's think step by step" phrasing
> - Make each reasoning step explicit
> - Include verification/sanity checks
> - Show intermediate conclusions

> [!metadata] Metadata Health Check
> **Type**: `VIEW[{type}]`
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Maturity**: `VIEW[{maturity}]` | **Confidence**: `VIEW[{confidence}]` | **Priority**: `VIEW[{priority}]`
> **Usage Count**: `VIEW[{usage-count}]` | **Reasoning Steps**: `VIEW[{reasoning-steps}]`
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
> <!-- Brief description of what reasoning process this CoT prompt guides -->
> <% tp.file.cursor(1) %>

## 🎯 Use Cases

<!-- When should this chain-of-thought approach be used? -->
- <% tp.file.cursor(2) %>

## 🚫 When NOT to Use

<!-- Scenarios where chain-of-thought is unnecessary or inappropriate -->
- <% tp.file.cursor(3) %>

---

## 📝 CHAIN-OF-THOUGHT PROMPT CONTENT

### 1. PROBLEM STATEMENT

<!-- Clear definition of the problem requiring reasoning -->
```markdown
<% tp.file.cursor(4) %>

**Problem Type**:


**Complexity Level**:


**Key Challenges**:
-
-
-

**Success Criteria**:
-
-
```

---

### 2. REASONING STEPS

<!-- Explicit step-by-step thinking process -->
```markdown
Let's approach this problem systematically. Think through each step carefully.

**Step 1: [First Reasoning Step]**
<% tp.file.cursor(5) %>

Action:
-

Consider:
-

Intermediate Conclusion:


---

**Step 2: [Second Reasoning Step]**
<% tp.file.cursor(6) %>

Action:
-

Consider:
-

Intermediate Conclusion:


---

**Step 3: [Third Reasoning Step]**
<% tp.file.cursor(7) %>

Action:
-

Consider:
-

Intermediate Conclusion:


---

**Step 4: [Fourth Reasoning Step]** (if needed)

Action:
-

Consider:
-

Intermediate Conclusion:


---

**Step 5: [Fifth Reasoning Step]** (if needed)

Action:
-

Consider:
-

Intermediate Conclusion:

```

---

### 3. SOLUTION TEMPLATE

<!-- Structure for presenting the final answer -->
```markdown
<% tp.file.cursor(8) %>

**Final Answer**:


**Reasoning Summary**:
1.
2.
3.

**Key Insights**:
-
-

**Confidence Level**:
[Low | Medium | High] - Because:


**Alternative Approaches Considered**:
-
-
```

---

### 4. VERIFICATION

<!-- How to check if the reasoning and solution are correct -->
```markdown
**Verification Checklist**:

□ Does each step logically follow from the previous?
□ Are all assumptions explicitly stated?
□ Are there any logical leaps or gaps?
□ Does the conclusion address the original problem?
□ Are edge cases considered?
□ Is the reasoning consistent throughout?

**Sanity Checks**:
1.
2.
3.

**Common Error Patterns to Watch For**:
-
-
-

**If Answer Seems Wrong**:
- Re-examine Step:
- Consider Alternative:
- Check Assumption:
```

---

## 🧩 COMPONENTS USED

<!-- Link to reusable components from library -->
<!-- Use Component Search macro to find and insert -->
<!-- Update components-used in frontmatter -->

**Reasoning Frameworks**:
-

**Problem Decomposition**:
-

**Verification Protocols**:
-

**Solution Templates**:
-

---

## 🧪 TESTING & VALIDATION

### Test 1: [Date]
**Objective**: Test reasoning quality
**Problem**:
**Expected Steps**:
**Actual Steps**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Reasoning Errors Found**:
-

**Link**: [[test-result-link]]

---

### Test 2: [Date]
**Objective**: Test edge case handling
**Problem**:
**Expected Steps**:
**Actual Steps**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

---

### Version History

| Version | Date | Changes | Steps Count | Quality Δ | Link |
|---------|------|---------|-------------|-----------|------|
| 1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | Initial creation | 3 | - | - |

---

## 📊 USAGE TRACKING

### Production Usage
<!-- Where and when this CoT prompt was used -->

**Project/Context**:
**Date**:
**Problem Complexity**:
**Reasoning Quality**:
**Outcome**:

---

### Performance Notes
<!-- Observations about effectiveness -->

**Reasoning Quality**:
-

**Step Clarity**:
-

**Common Reasoning Errors**:
-

**Verification Effectiveness**:
-

**Improvement Ideas**:
-

---

## 🔗 RELATED PROMPTS

```dataviewjs
// Semantic Bridge: Find related chain-of-thought prompts
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

const siblings = dv.pages()
    .where(p => (p.type === "chain-of-thought" || p.type === "component"))
    .where(p => p.file.path !== current.file.path)
    .map(p => {
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return {
            link: p.file.link,
            type: p.type,
            rating: p.rating || 0,
            steps: p["reasoning-steps"] || 0,
            sharedCount: shared.length
        };
    })
    .where(p => p.sharedCount > 0)
    .sort(p => p.sharedCount, "desc")
    .limit(5);

if (siblings.length > 0) {
    dv.header(4, "🌉 Similar CoT Prompts (Shared Context)");
    dv.table(
        ["Prompt", "Type", "Rating", "Steps", "Shared Links"],
        siblings.map(s => [s.link, s.type, s.rating + "/10", s.steps, "🔗 " + s.sharedCount])
    );
} else {
    dv.paragraph("*No related chain-of-thought prompts found yet.*");
}
```

### Manual Links
<!-- Add links to related prompts, workflows, or projects -->
-

---

## 💡 OPTIMIZATION LOG

### Optimization Attempt: [Date]
**Hypothesis**: (e.g., "Adding intermediate verification improves accuracy")
**Changes Made**:
- Steps added/modified:
- Verification updated:

**Result**:
**New Rating**: /10
**Keep Changes?**: Yes | No

---

## 🎓 LESSONS LEARNED

<!-- Document insights for future CoT creation -->

**Step Design**:
-

**Reasoning Clarity**:
-

**Verification Strategy**:
-

**Optimal Step Count**:
-

**Key Insights**:
-

---

## 📋 QUICK ACTIONS

**Meta-Bind Buttons** (if configured):
- `BUTTON[increment-usage]` - Increment usage count
- `BUTTON[add-step]` - Add reasoning step
- `BUTTON[run-test]` - Quick test documentation
- `BUTTON[bump-version]` - Version increment
- `BUTTON[archive]` - Move to archive

---

## 📚 REFERENCES & RESOURCES

<!-- Links to documentation, research, examples -->

**Chain-of-Thought Research**:
-

**Reasoning Techniques**:
-

**Related Methods**:
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | Chain-of-Thought Template*
