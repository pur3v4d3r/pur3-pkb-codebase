```yaml
# DOCUMENT IDENTIFICATION
doc_id: "dewey-ct-project-pipeline-overview-v1-0"
doc_created: 2026-02-21
doc_modified: 2026-02-21
doc_type: "workflow"
primary_domain: "project-management"
tags: ["dewey-ct", "pipeline", "coordination", "overview"]
prompt_title: "DeweyCT Project Pipeline Overview v1.0"
```

# DeweyCT — Project Pipeline Overview

This document coordinates the two parallel workstreams (Research and Build) and defines what gets handed off between them.

---

## The Two Workstreams

```
┌─────────────────────────────────┐     ┌──────────────────────────────────┐
│  RESEARCH WORKSTREAM            │     │  BUILD WORKSTREAM                │
│  Claude Project (separate)      │     │  Claude Code                     │
│                                 │     │                                  │
│  System prompt:                 │     │  Starter prompt:                 │
│  dewey-ct-research-project-     │     │  dewey-ct-claude-code-starter-   │
│  system-prompt.md               │     │  prompt.md                       │
│                                 │     │                                  │
│  Produces: JSON + MD files      │────▶│  Consumes: JSON + MD files       │
│  in data/ directory             │     │  to build the app                │
└─────────────────────────────────┘     └──────────────────────────────────┘
```

---

## Documents in This Package

| File | Purpose | Send To |
|---|---|---|
| `dewey-ct-research-project-system-prompt.md` | System prompt for the Research Claude Project | Paste as Claude Project system prompt |
| `dewey-ct-claude-code-starter-prompt.md` | Initial message to Claude Code to begin the build | First message in Claude Code session |
| `dewey-ct-agent-prompts.md` | Sub-agent prompts for parallel work in Claude Code | Keep in repo as `AGENT_PROMPTS.md` |
| `dewey-ct-project-pipeline-overview.md` | This document — coordination reference | Keep for your own reference |

---

## What to Do First

### Step 1 — Set Up the Research Project
1. Create a new Claude Project named "DeweyCT Content Research"
2. Upload `dewey-ct-research-project-system-prompt.md` as the Project Instructions
3. Add your chapter markdown files to the Project Knowledge
4. First session: ask for Phase 1 — Master Index + Chapter 1 JSON

### Step 2 — Start the Build in Parallel
1. Open Claude Code
2. Navigate to your target repository directory
3. Paste `dewey-ct-claude-code-starter-prompt.md` as your first message
4. Wait for Claude Code to produce `BUILD_PLAN.md` and confirm architecture
5. After confirmation, tell it to proceed with Phase 0 (Foundation)

### Step 3 — Converge at Phase 1
- When Research delivers Chapter 1 JSON → hand to Build for Phase 1
- Build can work on skeleton + Chapter 1 while Research completes remaining chapters
- The two workstreams converge fully when Research completes Phase 2 (Frameworks)

---

## Content Delivery Handoff Protocol

When Research produces a file, deliver it to Build like this:

```
[In Claude Code session]

"The research workstream has delivered a new file. Add it to the repository:

File path: data/chapters/chapter-02.json
Content:
[paste JSON content]

After adding: verify the TypeScript types still validate against this file,
then update the master-index if needed."
```

---

## Priority Decision Matrix

If you can only work on one thing at a time, prioritize in this order:

1. **Chapter 1 JSON** (blocks everything in Build)
2. **master-index.json** (blocks chapter library page)
3. **Dewey Five Phases framework JSON** (blocks first template)
4. **Dewey Reflective template definition** (blocks template feature)
5. **Q&A LLM prompts** (blocks Q&A feature)
6. Remaining chapters (can be added incrementally after V1)
7. Remaining frameworks (add as features are built)

---

## Questions Requiring Your Input

Before the Research workstream starts, confirm:

1. **Edition**: Which edition of "How We Think" are your markdown files from — 1910 (25 chapters) or 1933 revised (different chapter structure)?

2. **Chapter file format**: Are your existing markdown files one-file-per-chapter, or the full book in one file?

3. **API key**: Do you have an Anthropic API key? (needed by Build workstream — the start.sh script will prompt for it)

4. **Hosting**: Do you want the public Vercel URL (simplest) or local-only? (Affects what Claude Code configures in Phase 5)
