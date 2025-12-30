---
title: "gemini-gem_tag-selector-for-permanent-notes_v1.0.0-202512011939"
id: "20251201193922"
type: "gemini-gem"
status: active
version: "1.0.0"
key_takeaway: ""
rating: ""
source: pur3v4d3r
last_used: "2025-12-01"
url: ""
tags:
  - "status/seedling"
  - "topic/component-library"
  - "type/agentic"
  - "llm/gemini"
  - "source/pur3v4d3r"
  - "year/2025"
aliases:
  - "Gemini Gem Instruction Sets"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-01]]"
  - "[[2025-W49]]"
maturity: seedling
confidence: speculative


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---
> [!overview]
> - [Gem-ID:: 202512011939]
> - [Gem-Version:: 1.0.0]
> - [Gem-Description:: This is a prompt for having Gemini analyze a Key Word or Term and select from my Tag Taxonomy which of the Tags to use in the note.]

```prompt
----

Gem Metadata

Gem-ID:: 202512011939
Gem-Version:: 1.0.0
Gem-Description:: This is a prompt for having Gemini analyze a Key Word or Term and select from my Tag Taxonomy which of the Tags to use in the note.

----

## [CONTEXT]
I'm currently in the process of creating a bunch of definition/key-term/framework/Etc into permanent notes for my PKB. Think of these as like an Atomic Note, just not only my writing but anything I've learned on it. I use the wiki links in my generated reports to link to these notes and every time one comes up during active reading I open it and add something I've learned to it. It's my own from of progressive summarization/disclosure. 

## [TASK]
What I need you to do is when I input a key term, Etc. I want you to go through this list of tags and select one tag from each grouping that applies to that Key-term.
Then generate a small card for me that uses this format:

## [FORMAT]
{{Key-Term}}
- Group-Type List -> {{Tag Recommendation}}
- Group-Link Up -> {{Tag Recommendation}}
- Group-B1: Top-Level Domains (L1/L2) -> {{Tag Recommendation}}
- Group-C2: Cognitive Science Parent Paths -> {{Tag Recommendation}}
- Group-D: Cognitive Science - Memory & Attention (Granular) -> {{Tag Recommendation}}
- Group-E: Cognitive Science - Executive Function & Reasoning (Granular) -> {{Tag Recommendation}}
- Group-F: Cognitive Science - Learning & Metacognition (Granular) -> {{Tag Recommendation}}
- Group-G: Cognitive Science - Theories & Models (Granular) -> {{Tag Recommendation}}
- Group-H: PKM/Obsidian - Technical & Plugin Details (Granular) -> {{Tag Recommendation}}

## TAGS FOR APPLICATION

Tag Groupiongs to use:

Group-Type List
    "analysis",
    "case-study",
    "claude-project",
    "cog-sci-report",
    "comparison",
    "concept",
    "cosmo-report",
    "dashboard",
    "definition",
    "edu-report",
    "experiment",
    "fleeting",
    "framework",
    "gemini-gem",
    "guide",
    "insight",
    "literature",
    "mental-model",
    "moc",
    "pattern",
    "permanent-note",
    "pkb-report",
    "practice-log",
    "principle",
    "prompt",
    "prompt-report",
    "reference",
    "reflection",
    "report",
    "review",
    "strategy",
    "technique",
    "theory",
    "tutorial"

Group-Link Up
    "[[artificial-intelligence-moc]]",
    "[[cognitive-science-moc]]",
    "[[cosmology-moc]]",
    "[[educational-psychology-moc]]",
    "[[learning-theory-moc]]",
    "[[neuroscience-moc]]",
    "[[pkb-&-pkm-moc]]",
    "[[prompt-engineering-moc]]"

Group-B1: Top-Level Domains (L1/L2)
    "artificial-intelligence",
    "behavioral-science",
    "cognitive-anthropology",
    "cognitive-development",
    "cognitive-ergonomics",
    "cognitive-linguistics",
    "cognitive-neuroscience",
    "cognitive-psychology",
    "cognitive-science",
    "computational-modeling",
    "cosmology",
    "critical-thinking",
    "decision-science",
    "digital-garden",
    "educational-psychology",
    "experimental-psychology",
    "human-factors",
    "information-architecture",
    "instructional-design",
    "knowledge-graph",
    "knowledge-work",
    "learning-science",
    "learning-theory",
    "neuroscience",
    "neuroimaging",
    "note-taking",
    "obsidian",
    "pkb",
    "pkm",
    "productivity",
    "productivity-systems",
    "prompt-engineering",
    "psychometrics",
    "psychology",
    "second-brain",
    "self-improvement",
    "self-regulation",
    "vault-architecture",
    "knowledge-workflow"

Group-C2: Cognitive Science Parent Paths
    "cognitive-science/attention",
    "cognitive-science/cognitive-load",
    "cognitive-science/executive-function",
    "cognitive-science/memory",
    "cognitive-science/metacognition",
    "cognitive-science/reasoning",
    "critical-thinking/analysis",
    "critical-thinking/evaluation",
    "critical-thinking/logic",
    "critical-thinking/problem-solving",
    "critical-thinking/synthesis",
    "learning-theory/andragogy",
    "learning-theory/cognitive-apprenticeship",
    "learning-theory/constructivism",
    "learning-theory/heutagogy",
    "learning-theory/pedagogy",
    "self-improvement/growth-mindset",
    "self-improvement/mental-models",
    "self-improvement/productivity",
    "self-improvement/reflective-practice",
    "self-improvement/skill-development",
    "self-regulation/behavioral",
    "self-regulation/emotional",
    "self-regulation/goal-setting",
    "self-regulation/motivation",
    "self-regulation/self-control",
    "self-regulation/theory"

Group-D: Cognitive Science - Memory & Attention (Granular)
    "attention",
    "auditory-perception",
    "autobiographical-memory",
    "consolidation",
    "divided-attention",
    "encoding",
    "episodic-memory",
    "interference",
    "long-term-memory",
    "multimodal-integration",
    "perception",
    "phonological-loop",
    "procedural-memory",
    "prospective-memory",
    "reconsolidation",
    "retrieval",
    "selective-attention",
    "semantic-memory",
    "sustained-attention",
    "visual-perception",
    "visuospatial-sketchpad",
    "working-memory"

Group-E: Cognitive Science - Executive Function & Reasoning (Granular)
    "abductive-reasoning",
    "analogical-reasoning",
    "central-executive",
    "cognitive-control",
    "cognitive-flexibility",
    "conflict-monitoring",
    "creative-thinking",
    "critical-thinking",
    "deductive-reasoning",
    "error-monitoring",
    "executive-function",
    "inductive-reasoning",
    "inhibitory-control",
    "performance-monitoring",
    "planning",
    "problem-solving",
    "reasoning",
    "response-inhibition",
    "self-regulation",
    "task-switching"

Group-F: Cognitive Science - Learning & Metacognition (Granular)
    "active-recall",
    "andragogy-pkm",
    "attention-management",
    "calibration",
    "calibration-practices",
    "cognitive-load-management",
    "cognitive-load-theory",
    "conceptual-learning",
    "control-processes",
    "desirable-difficulties",
    "elaborative-encoding",
    "elaborative-interrogation",
    "explicit-learning",
    "expertise-development",
    "generation-effect",
    "germane-load",
    "germane-load-optimization",
    "implicit-learning",
    "instructional-design-pkm",
    "interleaving",
    "intrinsic-load",
    "learning-processes",
    "metacognitive-monitoring",
    "metacognitive-pkm",
    "metacomprehension",
    "metamemory",
    "monitoring",
    "self-directed-learning",
    "self-explanation",
    "self-regulated-learning",
    "skill-acquisition",
    "spacing-effect",
    "testing-effect",
    "transfer-of-learning",
    "working-memory-capacity",
    "working-memory-support"

Group-G: Cognitive Science - Theories & Models (Granular)
	  "ACT-R",
    "cognitive-resources",
    "distributed-cognition",
    "dual-process-theory",
    "embodied-cognition",
    "enactive-cognition",
    "extraneous-load",
    "extraneous-load-reduction",
    "extended-cognition",
    "global-workspace-theory",
    "grounded-cognition",
    "information-processing-theory",
    "levels-of-processing",
    "memory-systems",
    "mental-effort",
    "multiple-drafts-model",
    "parallel-distributed-processing",
    "situated-cognition",
    "SOAR",
    "spreading-activation",
    "symbolic-architecture"

Group-H: PKM/Obsidian - Technical & Plugin Details (Granular)
    "aging-cognition",
    "applied-cognition",
    "attention-architecture",
    "behavioral-experiments",
    "clinical-cognition",
    "cognitive-decline",
    "cognitive-disorders",
    "cognitive-enhancement",
    "cognitive-modeling",
    "cognitive-pkm",
    "cognitive-rehabilitation",
    "cognitive-training",
    "concept/attention-mechanism",
    "concept/atomic-notes",
    "concept/automaticity",
    "concept/bidirectional-linking",
    "concept/chunking",
    "concept/cognitive-bias",
    "concept/cognitive-overhead",
    "concept/context-switching",
    "concept/discoverability",
    "concept/distributed-practice",
    "concept/dual-coding",
    "concept/elaboration",
    "concept/emergence",
    "concept/error-correction",
    "concept/evergreen-notes",
    "concept/external-cognition",
    "concept/few-shot-exemplars",
    "concept/flow-state",
    "concept/generation-effect",
    "concept/in-context-learning",
    "concept/information-overload",
    "concept/instruction-following",
    "concept/interleaving",
    "concept/knowledge-synthesis",
    "concept/knowledge-transfer",
    "concept/linking-thinking",
    "concept/mental-representation",
    "concept/networked-thought",
    "concept/output-validation",
    "concept/progressive-summarization",
    "concept/prompt-chaining",
    "concept/prompt-template",
    "concept/retrieval-practice",
    "concept/second-brain",
    "concept/semantic-similarity",
    "concept/serendipity",
    "concept/spacing-effect",
    "concept/system-message",
    "concept/task-decomposition",
    "concept/temperature-control",
    "concept/testing-effect",
    "concept/token-probability",
    "concept/top-p-sampling",
    "concept/transfer",
    "concept/transformer-architecture",
    "concept/wayfinding",
    "consolidation-workflow",
    "cross-cultural-cognition",
    "cross-sectional-research",
    "developmental-cognition",
    "educational-applications",
    "empirical-research",
    "encoding-strategies",
    "evidence-based-pkm",
    "experimental-design",
    "learning-analytics",
    "learning-optimization",
    "longitudinal-research",
    "memory-systems-design",
    "meta-analysis",
    "neurodevelopmental",
    "neuroimaging-studies",
    "reflection-systems",
    "retrieval-practice-pkm",
    "spaced-review-system",
    "technology-cognition",
    "workplace-cognition"

```

