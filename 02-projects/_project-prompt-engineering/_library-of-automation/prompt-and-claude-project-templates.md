<thinking>
I need to create two separate templates - one for capturing prompts and one for Claude projects. Let me analyze the requirements:
1. For prompts: Need a capture template that creates new prompts with proper metadata
2. For Claude projects: Need a separate template for agentic use cases
Based on the system instructions, I should create:
- A prompt capture template 
- A Claude project template
Both should follow the metadata standards and folder structure specified.
</thinking>
I'll create both templates for you. Here are the two separate templates:
## Template 1: Prompt Capture Template
**File Path:** `03-notes/prompt-engineering/prompt-capture.md`
```markdown
---
type: prompt
source: []
maturity: seedling
confidence: provisional
status: active
priority: medium
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt
  - #status/seedling
  - #year/2025
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
<%*
const promptPurpose = await tp.system.prompt("What is the purpose of this prompt?", "");
const promptRole = await tp.system.prompt("What role should the AI take? (e.g., expert, assistant, tutor)", "helpful AI assistant");
const promptContext = await tp.system.prompt("What context should be provided?", "");
const instructionType = await tp.system.suggester(
  ["Direct instructions", "Chain-of-thought", "Step-by-step", "Custom"],
  ["Direct instructions", "Chain-of-thought", "Step-by-step", "Custom"]
);
const constraints = await tp.system.prompt("Any specific constraints? (e.g., format, length, style)", "");
const outputFormat = await tp.system.prompt("Desired output format?", "Clear and concise response");
tR += `## Purpose\n${promptPurpose}\n\n`;
tR += `## Role\nYou are a ${promptRole}.\n\n`;
tR += `## Context\n${promptContext}\n\n`;
tR += `## Instructions\n`;
if (instructionType === "Chain-of-thought") {
  tR += `Think through this step-by-step:\n1. First, consider...\n2. Next, analyze...\n3. Then, evaluate...\n4. Finally, conclude...\n\n`;
} else if (instructionType === "Step-by-step") {
  tR += `Follow these steps:\n1. [Step 1]\n2. [Step 2]\n3. [Step 3]\n\n`;
} else if (instructionType === "Direct instructions") {
  tR += `[Insert direct instructions here]\n\n`;
} else {
  tR += `[Custom instructions]\n\n`;
}
tR += `## Constraints\n${constraints}\n\n`;
tR += `## Output Format\n${outputFormat}\n\n`;
tR += `## Examples\n[Optional: Add few-shot examples here]\n\n`;
tR += `## Testing Notes\n- [ ] Test with simple case\n- [ ] Test with complex case\n- [ ] Check for consistency\n\n`;
%>
## Next Steps
1. Test this prompt with sample inputs
2. Refine based on results
3. Update maturity to "developing" after initial testing
4. Add to dashboard for tracking
<% tp.file.cursor() %>
```
## Template 2: Claude Project Template
**File Path:** `02-projects/claude-projects/claude-project-template.md`
```markdown
---
type: claude-project
source: [claude-opus-4.1, claude-sonnet-4.5]
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/claude-project
  - #status/active
  - #year/2025
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
<%*
const projectName = tp.file.title;
const projectGoal = await tp.system.prompt("What is the main goal of this Claude project?", "");
const projectScope = await tp.system.prompt("What is the scope of this project?", "");
const expectedOutcome = await tp.system.prompt("What is the expected outcome?", "");
const requiredResources = await tp.system.prompt("What resources are needed?", "Claude access, relevant documents, testing environment");
const successMetrics = await tp.system.prompt("How will success be measured?", "");
%>
## Project Overview
**Goal:** <%= projectGoal %>
**Scope:** <%= projectScope %>
**Expected Outcome:** <%= expectedOutcome %>
## Resources Required
<%= requiredResources %>
## Success Metrics
<%= successMetrics %>
## Implementation Plan
### Phase 1: Setup
- [ ] Define detailed requirements
- [ ] Gather necessary resources
- [ ] Set up testing environment
### Phase 2: Development
- [ ] Create initial prompts
- [ ] Test with sample data
- [ ] Iterate based on results
### Phase 3: Validation
- [ ] Conduct comprehensive testing
- [ ] Validate against success metrics
- [ ] Document results
### Phase 4: Deployment
- [ ] Finalize project deliverables
- [ ] Create user documentation
- [ ] Hand off to stakeholders
## Prompt Components
### System Prompt
```
[Insert system prompt here]
```
### User Prompts
1. [Primary user prompt]
2. [Follow-up prompts if needed]
## Testing Framework
- [ ] Test Case 1: [Description]
- [ ] Test Case 2: [Description]
- [ ] Test Case 3: [Description]
## Risk Assessment
- [ ] Potential issues identified
- [ ] Mitigation strategies
- [ ] Contingency plans
## Timeline
- **Start Date:** <% tp.date.now("YYYY-MM-DD") %>
- **Target Completion:** <% tp.date.now("YYYY-MM-DD", 7, true) %>
- **Milestones:** 
  - Setup Complete: [Date]
  - Development Complete: [Date]
  - Validation Complete: [Date]
## Notes and Observations
[Add project notes here]
<% tp.file.cursor() %>
```
## Summary

| Template Name | File Path | Purpose |
|---------------|-----------|---------|
| Prompt Capture Template | `03-notes/prompt-engineering/prompt-capture.md` | Creates new prompts with structured metadata and sections |
| Claude Project Template | `02-projects/claude-projects/claude-project-template.md` | Manages agentic Claude projects with full project lifecycle |
Both templates:
- Follow the specified metadata standards
- Use proper folder structure
- Include appropriate tags and link-ups
- Have cursor placement for optimal user experience
- Are ready for immediate use in your PKB workflow

