---
title: "Custom Callout: Convert all current Callout to Hover and with a themed gradient"
id: 20251112-205220
type: prompt
status: complete
rating: ""
version: "1.0"
last-used: 2025-11-12
source: pur3v4d3r
url: ""
tags:
  - "#prompt-engineering"
  - type/prompt/one-off
  - status/complete
  - status/used
  - source/pur3v4d3r
  - llm/gemini
  - year/2025
aliases:
  - prompt/
  - prompting
link-up: "[[📝prompting_🗺️moc]]"
link-related:
  - "[[reference-comprehensive-css-variables-20251106]]"
  - "[[reference-comprehensive-css-variable-2025110619]]"
---

```prompt
---
id: prompt-block-v1
---

[CONTEXT]
These are the two main colors for my theme.

`158 108 211 Theme-Purple`  `#9E6CD3`
`255 200 0 Theme-Gold/Amber` `#ffc800`

**Use these to complete the Task**. You need to create a mixture of the two colors. Were *some Callouts will be the Gold* color and *some will be Purple*. Try and categorize them as best you can. Meaning group the callouts into categories and color each category either Purple or Gold.

[TASK]
1. Apply Gradient Background to the list of callouts.
2. Apply Hover to the list of callouts.
3. Apply Both Hover and Gradient Background to list of callouts.

[OUTPUT]

You should have 4 (four) distict sets of Callouts when you are finished:
 1. One set with only the Gold Graident Background applied.
 2. One set with only the Purple Gradeient Background Applied.
 3. One set with Hover and No color applied.
 4. One set with Hover and Gradiant Applied with groupos of Callouts either being Gold or Purple. 

Gradient Background

.callout[data-callout="check"],
.callout[data-callout="done"] {
  border: 1px solid #99f2d1;
  background: linear-gradient(43deg, #1c3e35 0%, #99f2d1 100%);
}

Hover

.callout[data-callout="tldr"]:hover {
  box-shadow: -24px 24px 69px -3px rgba(66, 4, 126, 0.4), 24px -24px 69px -3px
      rgba(7, 244, 158, 0.1);
}

List of Active Callout to Modify

{
  "callouts": {
    "custom": [
      "key-claim",
      "casual-link",
      "evidence",
      "confusion",
      "counter-argument",
      "no-evidence",
      "connection-ideas",
      "to-do",
      "read-complete",
      "reading-in-progress",
      "read-asap",
      "insight",
      "principle-point",
      "shot-idea",
      "lighting-setup",
      "composition",
      "post-processing",
      "cosmos-concept",
      "equation",
      "thought-experiment",
      "project-link",
      "hub-moc",
      "revist",
      "definition",
      "connections-and-links",
      "pre-read-questions",
      "pre-read-thoughts",
      "the-purpose",
      "important-links",
      "choice-a",
      "choice-b",
      "document",
      "capture",
      "tasks",
      "the-philosophy",
      "analogy",
      "ask-yourself-this",
      "question",
      "summary",
      "abstract",
      "how-to-use-this",
      "the-goal",
      "the-mission",
      "outcome",
      "methodology-and-sources",
      "starting-message",
      "phase-one",
      "phase-two",
      "phase-three",
      "phase-four",
      "how-to-use",
      "gemini-pro-response",
      "message",
      "key-changes",
      "how-this-dashboard-works",
      "your-new-workflow",
      "changes-from-prompting-dashboard",
      "helpful-tip",
      "the-start",
      "related-topics-to-consider",
      "key",
      "topic-idea",
      "plan",
      "math",
      "kanban",
      "note-toolbar",
      "links-to-related-notes",
      "thoughts",
      "start-of-chat",
      "atomic-concept",
      "further-exploration",
      "what-this-does",
      "analysis-rhetorical",
      "analysis-logical",
      "analysis-contextual",
      "analysis-cognitive",
      "project-kickstarter",
      "zettelkasten-incubator",
      "problem-clarity-solution",
      "disposition",
      "description",
      "use-cases-and-examples",
      "core-principle",
      "warning",
      "constraints-and-pitfalls",
      "quick-reference",
      "purpose",
      "argument",
      "review",
      "feynman-technique",
      "fleeting-thought",
      "work-log-entry",
      "left-off-reading-at",
      "in-note-metadata",
      "input-and-instruction",
      "iteration-and-versioning",
      "topic-name",
      "comprehensive-reference",
      "related-topics-for-pkb-expansion"
    ],

```