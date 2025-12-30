---
type: "reference"
created: "2025-12-20"
tags:
  - "year/2025"
  - "prompt-engineering"
  - "spes-system"
  - "quick-reference"
aliases:
  - "SPES Quick Reference"
---

# SPES Template Quick Reference Card

One-page guide for choosing the right template.

---

## 🎯 Decision Tree

```
START: What are you building?
│
├─ Setting AI personality/role?
│  └─ Use: SYSTEM PROMPT TEMPLATE
│     Prefix: system-prompt-*
│
├─ Teaching pattern through examples?
│  └─ Use: FEW-SHOT TEMPLATE
│     Prefix: few-shot-*
│
├─ Need step-by-step reasoning?
│  └─ Use: CHAIN-OF-THOUGHT TEMPLATE
│     Prefix: cot-*
│
├─ Building multi-step pipeline?
│  └─ Use: WORKFLOW CHAIN TEMPLATE
│     Prefix: workflow-*
│
└─ Just capturing a quick idea?
   └─ Use: IDEA CAPTURE TEMPLATE
      Prefix: idea-*
```

---

## 📋 Template Cheat Sheet

### 1. System Prompt Template
```
PREFIX: system-prompt
TYPE: Role/Behavior Definition
WHEN: Setting AI identity, tone, expertise
SECTIONS: Role | Behavior | Knowledge | Format | Examples
EXAMPLES: "Expert Coder", "Research Assistant", "Creative Writer"
```

### 2. Few-Shot Template
```
PREFIX: few-shot
TYPE: Example-Based Learning
WHEN: Need 3-5 demonstrations
SECTIONS: Task | Examples (3-5) | Pattern | New Input
EXAMPLES: "Sentiment Analysis", "Code Formatting", "Translation"
```

### 3. Chain-of-Thought Template
```
PREFIX: cot
TYPE: Step-by-Step Reasoning
WHEN: Complex problem solving
SECTIONS: Problem | Steps | Solution | Verification
EXAMPLES: "Math Problems", "Logical Puzzles", "Debug Analysis"
```

### 4. Workflow Chain Template
```
PREFIX: workflow
TYPE: Multi-Step Pipeline
WHEN: Sequential processes
SECTIONS: Overview | Steps | Transitions | Aggregation
EXAMPLES: "Code Review", "Content Pipeline", "Research Workflow"
```

### 5. Idea Capture Template
```
PREFIX: idea
TYPE: Quick Capture
WHEN: Inspiration strikes
SECTIONS: Idea | Use | Insight | Sketch | Next Steps
EXAMPLES: Any prompt idea (promote later)
```

---

## ⚡ Quick Commands

### File Naming Patterns
```
system-prompt-[title]-1.0.0-2025-12-20-14-30-22.md
few-shot-[title]-1.0.0-2025-12-20-14-30-22.md
cot-[title]-1.0.0-2025-12-20-14-30-22.md
workflow-[title]-1.0.0-2025-12-20-14-30-22.md
idea-[title]-2025-12-20-14-30-22.md (NO VERSION)
```

### Template Triggers (Templater)
```
Ctrl+P → "Templater: Open Insert Template Modal"
→ Select: _system-prompt-template.md
→ Select: _few-shot-template.md
→ Select: _chain-of-thought-template.md
→ Select: _workflow-chain-template.md
→ Select: _idea-capture-template.md
```

---

## 🔄 Workflow Shortcuts

### Rapid Capture → Promote
```
1. Idea Template (2 min)
2. Review in 3 days
3. Promote to full template if valuable
4. Test & iterate
```

### From Scratch
```
1. Choose template type
2. Answer guided questions
3. Fill 8+ cursor positions
4. Link to components
5. Test & document
```

### Iteration Cycle
```
1. Test prompt
2. Document results
3. Update rating
4. Modify content
5. Bump version
6. Retest
```

---

## 📊 Metadata Quick Fill

### Status Levels
```
active     - Currently using
testing    - Under evaluation
production - Battle-tested
deprecated - No longer recommended
archived   - Historical reference
```

### Confidence Levels
```
speculative - Untested idea
provisional - Initial testing
moderate    - Some validation
established - Proven effective
high        - Gold standard
```

### Priority Levels
```
low    - Nice to have
medium - Important
high   - Critical
urgent - Drop everything
```

---

## 🧩 Component Library Usage

### Search Components
```
Ctrl+P → "Component Search" (if macro configured)
OR
Grep for: type: "component"
```

### Link Components
```
In content:
[[component-expert-persona]]
[[component-json-formatter]]

In frontmatter:
components-used:
  - "[[component-expert-persona]]"
  - "[[component-json-formatter]]"
```

---

## 🧪 Testing Checklist

```
□ Define test objective
□ Prepare test input
□ Document expected output
□ Run test
□ Record actual output
□ Assign pass/fail
□ Rate quality (/10)
□ Log issues
□ Link to test results
□ Update rating if needed
```

---

## 🔗 Link Protocol (2+/2+)

### Minimum Required Links

**Outlinks (2+)**:
- [[prompt-engineering-moc]]
- [[YYYY-MM-DD]] (daily note)

**Inlinks (2+)**:
- From MOC
- From daily note
- From related prompts

### Find Orphans
```
Dataview query:
WHERE type = "prompt" OR type = "component"
WHERE length(file.inlinks) < 2
```

---

## 🎨 Common Patterns

### Pattern: Hybrid System + Few-Shot
```
1. Create system prompt (role/behavior)
2. Create few-shot prompt (examples)
3. Link them together
4. Use system prompt first, then few-shot
```

### Pattern: CoT in Workflow
```
1. Create workflow with multiple steps
2. One step = "Apply reasoning"
3. Link to chain-of-thought prompt
4. Use CoT output in next workflow step
```

### Pattern: Idea Evolution
```
1. Capture raw idea
2. Test rough version
3. Promote to full template
4. Iterate through versions
5. Reach production maturity
```

---

## 🚨 Common Mistakes

### ❌ Don't Do This
```
- Skip testing before production use
- Forget to update usage-count
- Leave orphan prompts (0 inlinks)
- Skip version history
- Ignore review intervals
- Rate everything 10/10
- Never archive old prompts
```

### ✅ Do This Instead
```
- Test immediately after creation
- Track usage metrics
- Link richly (2+/2+)
- Document version changes
- Review on schedule
- Rate honestly based on performance
- Archive deprecated prompts
```

---

## 📞 Emergency Troubleshooting

### Template Won't Execute
```
1. Check Templater syntax (<%* ... _%>)
2. Verify file path
3. Check for syntax errors in YAML
4. Restart Obsidian
```

### File Naming Fails
```
1. Verify title prompt answered
2. Check for special characters
3. Ensure timestamp format correct
4. Test rename manually
```

### Cursor Positions Missing
```
1. Count cursor calls: <% tp.file.cursor(N) %>
2. Ensure 8+ positions
3. Number sequentially (1-8+)
4. No duplicates
```

### Metadata Health Check Failing
```
1. Validate YAML syntax
2. Check required fields exist
3. Verify field names match
4. Test Meta-Bind VIEW syntax
```

---

## 🎓 Pro Tips

1. **Idea First**: When in doubt, start with idea template
2. **Test Fast**: First test within 24 hours of creation
3. **Link Early**: Add connections during creation, not later
4. **Rate Honestly**: Ratings guide future decisions
5. **Archive Boldly**: Keep vault clean, archive fearlessly
6. **Version Semantically**: Major.Minor.Patch (1.0.0)
7. **Review Regularly**: Set calendar reminders for reviews
8. **Component-ize**: Extract reusable blocks to component library
9. **Track Everything**: Usage count and last-used = goldmine
10. **Iterate Often**: Version 5.2.1 > Version 1.0.0

---

## 📚 Full Documentation

For detailed information, see:
- [[README-SPES-TEMPLATES]] - Complete template guide
- [[prompt-engineering-moc]] - Main MOC
- [[spes-system-overview]] - System architecture
- [[component-library]] - Reusable components

---

*Quick Reference Version: 1.0.0 | Created: 2025-12-20*
*Keep this handy for rapid template selection*
