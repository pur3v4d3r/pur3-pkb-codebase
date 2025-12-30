<%*
// FILE NAMING AUTOMATION
// Convention: idea-[semantic-title]-[timestamp].md
// Example: idea-multimodal-reasoning-20251220143022.md

// 1. Prompt for semantic title
const semanticTitle = await tp.system.prompt("Idea title (brief, e.g., 'multimodal-reasoning', 'context-priming'):");
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

// 3. Fixed prefix for idea captures
const prefix = "idea";

// 4. Generate timestamp (no version for ideas)
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");

// 5. Construct filename
const filename = `${prefix}-${sanitized}-${timestamp}`;

// 6. Rename file
await tp.file.rename(filename);
_%>
---
type: "idea"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
status: "raw"
promoted-to: ""
created: "<% tp.date.now("YYYY-MM-DD") %>"
modified: "<% tp.date.now("YYYY-MM-DD") %>"
review-next: "<% tp.date.now("YYYY-MM-DD", 3) %>"
priority: "<% await tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["low", "medium", "high", "urgent"], false, "Priority?") %>"
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering"
  - "idea-capture"
  - "status/raw"
aliases:
  - "<% tp.file.title %>"
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
---

> [!usage] Quick Capture Instructions
> **Purpose**: Rapidly capture prompt ideas without heavy structure. Promote to full templates later.
>
> **Workflow**:
> 1. **Capture** - Jot down core idea quickly (2-5 min)
> 2. **Review** - Revisit within 3 days to assess value
> 3. **Promote** - Convert to full template if idea proves valuable
> 4. **Archive** - Move to archive if idea doesn't pan out
>
> **Promotion Paths**:
> - → `_system-prompt-template.md` (for role/behavior ideas)
> - → `_few-shot-template.md` (for pattern learning ideas)
> - → `_chain-of-thought-template.md` (for reasoning ideas)
> - → `_workflow-chain-template.md` (for multi-step process ideas)
> - → `_prompt-master-template.md` (for general prompt ideas)

> [!metadata] Idea Status
> **Status**: `VIEW[{status}]` | **Priority**: `VIEW[{priority}]`
> **Created**: `= this.file.ctime` | **Age**: `= (date(today) - this.file.ctime).days + " days"`
> **Next Review**: `= this.review-next`
> **Promoted To**: `VIEW[{promoted-to}]`

[Captured: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY - HH:mm") %>]]]

---

# <% tp.file.title %>

## 💡 CORE IDEA

<!-- What's the prompt idea? Be brief and clear -->
<% tp.file.cursor(1) %>

---

## 🎯 INTENDED USE

<!-- What problem does this solve? When would you use it? -->
<% tp.file.cursor(2) %>

---

## 🧠 KEY INSIGHT

<!-- What's the "aha!" moment or unique angle? -->
<% tp.file.cursor(3) %>

---

## 📋 ROUGH SKETCH

<!-- Quick rough draft or outline (don't overthink!) -->
```markdown
<% tp.file.cursor(4) %>
```

---

## 🔗 RELATED CONCEPTS

<!-- Quick links to related prompts, components, or ideas -->
- <% tp.file.cursor(5) %>

---

## ⚡ NEXT STEPS

<!-- What needs to happen to develop this idea? -->
- [ ] Test rough concept
- [ ] <% tp.file.cursor(6) %>
- [ ] Review and decide: Promote | Archive | Iterate

---

## 📊 PROMOTION DECISION

### Decision: [ ] Promote | [ ] Archive | [ ] Keep as Idea

**Reasoning**:


**If Promoting, Convert To**:
- [ ] System Prompt Template
- [ ] Few-Shot Template
- [ ] Chain-of-Thought Template
- [ ] Workflow Chain Template
- [ ] General Prompt Template

**Link to Promoted Version**: [[]]

---

## 📝 CAPTURE NOTES

<!-- Stream of consciousness, rough thoughts, inspirations -->
<% tp.file.cursor(7) %>

---

## 🧪 QUICK TEST RESULTS (Optional)

**Tested**: Yes | No

**Quick Result**:


**Keep Developing?**: Yes | No

---

*Idea Template Version: 1.0.0 | Created: 2025-12-20 | Quick Capture Template*
