# Dataview and Template Design Guide: Cognitive Science Note

This document outlines the metadata structure of a "Permanent Cognitive Science Note" based on the `_permanent-note-cognitive-science-template-v1.0.0.md` Templater template. Use this guide to design Dataview queries, dashboards, and complementary templates.

## 1. Core Metadata (Frontmatter)

These fields are located in the YAML frontmatter of each note. The "Available Options" column lists the predefined choices presented by the template's interactive prompts.

| Field          | Type     | Description                                                                                             | Origin                  | Example                                                                     |
| :------------- | :------- | :------------------------------------------------------------------------------------------------------ | :---------------------- | :-------------------------------------------------------------------------- |
| `aliases`      | List     | Alternative names for the note concept.                                                                 | User Input              | `- "CogSci"`                                                                |
| `tags`         | List     | A collection of tags defining the note's context, type, and domain. See section 3 for a full breakdown. | User Input & Calculated | `- "type/permanent"`<br/>`- "cognitive-science"`<br/>`- "status/evergreen"` |
| `source`       | String   | The origin of the information.                                                                          | User Input              | `"article"`                                                                 |
| `id`           | String   | A unique timestamp-based identifier.                                                                    | Calculated              | `"20251217143055"`                                                          |
| `created`      | Datetime | The exact date and time the note was created.                                                           | Calculated              | `"2025-12-17T14:30:55"`                                                     |
| `modified`     | Datetime | The date and time the note was last modified.                                                           | Calculated              | `"2025-12-17T14:30:55"`                                                     |
| `week`         | Link     | A link to the corresponding weekly note.                                                                | Calculated              | `[[2025-W51]]`                                                              |
| `month`        | String   | The month the note was created, in YYYY-MM format.                                                      | Calculated              | `"2025-12"`                                                                 |
| `quarter`      | String   | The quarter the note was created, in YYYY-[Q]Q format.                                                  | Calculated              | `"2025-Q4"`                                                                 |
| `year`         | String   | The year the note was created.                                                                          | Calculated              | `"2025"`                                                                    |
| `type`         | String   | The primary classification of the note's content.                                                       | User Input              | `"concept"`                                                                 |
| `maturity`     | String   | The developmental stage of the note's content.                                                          | User Input              | `"evergreen"`                                                               |
| `confidence`   | String   | The author's confidence in the note's claims.                                                           | User Input              | `"high"`                                                                    |
| `status`       | String   | The current operational status of the note.                                                             | User Input              | `"active"`                                                                  |
| `priority`     | String   | The priority level of the note.                                                                         | User Input              | `"medium"`                                                                  |
| `link-up`      | Link     | A link to a primary, high-level "Map of Content" (MOC).                                                 | User Input              | `[[cognitive-science-moc]]`                                                 |
| `link-related` | Link     | Links to related notes, such as the daily note.                                                         | Calculated              | `[[2025-12-17]]`                                                            |

id:
aliases:
tags:
source:
maturity:
confidence:
status:
priority:
created:
modified:
week:
month:
quarter:
year:
type:

link-up:
link-related:


id: ""
type: ""
source: ""
status: ""
maturity: ""
confidence: ""
priority: ""
review-priority: ""
review-last-reviewed: ""
review-next-review: ""
review-count: ""
review-interval: ""
created: ""
modified: ""
week: ""
quarter: ""
year: ""
link-up:
  - ""
link-related:
  - ""
tags:
  - ""
aliases:
  - ""
title: ""

















## 2. Available Options for Metadata Fields

The following are the complete lists of options provided by the template for selection.

### `type`
- analysis
- case-study
- claude-project
- cog-sci-report
- comparison
- concept
- cosmo-report
- dashboard
- definition
- edu-report
- experiment
- fleeting
- framework
- gemini-gem
- guide
- insight
- literature
- mental-model
- moc
- pattern
- permanent-note
- pkb-report
- practice-log
- principle
- prompt
- prompt-report
- reference
- reflection
- report
- review
- strategy
- technique
- theory
- tutorial

### `source`
- article
- book
- claude-opus-4.1
- claude-sonnet-4.5
- community
- conversation
- course
- documentation
- experience
- gemini-flash-2.5
- gemini-flash-3.0
- gemini-pro-2.5
- gemini-pro-3.0
- literature-synthesis
- local-llm
- original-synthesis
- paper
- report
- video

### `maturity`
- needs-review
- seedling
- developing
- budding
- evergreen

### `confidence`
- speculative
- provisional
- moderate
- established
- high

### `status`
- active
- archived
- deprecated

### `priority`
- low
- medium
- high
- urgent

### `link-up` (MOCs)
- `[[artificial-intelligence-moc]]`
- `[[cognitive-science-moc]]`
- `[[cosmology-moc]]`
- `[[educational-psychology-moc]]`
- `[[learning-theory-moc]]`
- `[[neuroscience-moc]]`
- `[[pkb-&-pkm-moc]]`
- `[[practical-philosophy-moc]]`
- `[[prompt-engineering-moc]]`

---

## 3. Tagging Taxonomy

The template uses a rich, hierarchical tagging system divided into groups. The user is prompted to select up to 11 tags, one from each designated group, to ensure comprehensive metadata coverage.

### Group A: Meta-Dimensions
High-level descriptors for the note itself.

- **A1 (Type):** `type/analysis`, `type/case-study`, `type/claude-project`, `type/comparison`, `type/dashboard`, `type/experiment`, `type/fleeting`, `type/framework`, `type/gemini-gem`, `type/guide`, `type/literature`, `type/moc`, `type/pattern`, `type/permanent`, `type/practice-log`, `type/prompt-library`, `type/reference`, `type/reflection`, `type/report`, `type/review`, `type/synthesis`, `type/technique`, `type/template`, `type/tutorial`
- **A2 (Status):** `status/archived`, `status/budding`, `status/complete`, `status/deprecated`, `status/evergreen`, `status/experimental`, `status/in-progress`, `status/not-read`, `status/production`, `status/proven`, `status/read`, `status/review`, `status/seedling`, `status/under-revision`
- **A3 (Context & Source):** `context/applied`, `context/experimental`, `context/meta`, `context/personal`, `context/practical`, `context/professional`, `context/reference`, `context/research`, `context/teaching`, `context/theoretical`, `context/tutorial`, `source/article`, `source/blog`, `source/book`, `source/community`, `source/conference`, `source/conversation`, `source/course`, `source/documentation`, `source/experience`, `source/original`, `source/paper`, `source/podcast`, `source/video`, `source/workshop`
- **A4 (Mode, Nature, Model, etc.):** `complexity/advanced`, `complexity/basic`, `complexity/expert`, `complexity/intermediate`, `maturity/advanced`, `maturity/beginner`, `maturity/deprecated`, `maturity/emerging`, `maturity/established`, `maturity/expert`, `maturity/intermediate`, `maturity/standard`, `mode/analytical`, `mode/practical`, `mode/reflective`, `mode/synthetic`, `model/agnostic`, `model/claude`, `model/gemini`, `model/gpt`, `model/local`, `model/open-source`, `nature/conceptual`, `nature/declarative`, `nature/procedural`, `nature/reflective`, `validation/failed`, `validation/reported`, `validation/tested`, `validation/theoretical`

### Group B: Top-Level Domains & Systems (L1/L2)
Broad subject areas and methodologies.

- **B1 (Domains):** `artificial-intelligence`, `behavioral-science`, `cognitive-anthropology`, `cognitive-development`, `cognitive-ergonomics`, `cognitive-linguistics`, `cognitive-neuroscience`, `cognitive-psychology`, `cognitive-science`, `computational-modeling`, `cosmology`, `critical-thinking`, `decision-science`, `digital-garden`, `educational-psychology`, `experimental-psychology`, `human-factors`, `information-architecture`, `instructional-design`, `knowledge-graph`, `knowledge-work`, `learning-science`, `learning-theory`, `neuroscience`, `neuroimaging`, `note-taking`, `obsidian`, `pkb`, `pkm`, `productivity`, `productivity-systems`, `prompt-engineering`, `psychometrics`, `psychology`, `second-brain`, `self-improvement`, `self-regulation`, `vault-architecture`, `knowledge-workflow`
- **B2 (Systems):** `atomic-notes`, `building-second-brain`, `capture-system`, `concept-mapping`, `cornell-method`, `dashboard-design`, `evergreen-notes`, `gtd`, `hub-notes`, `index-notes`, `index-systems`, `linking-strategy`, `metadata-systems`, `mind-mapping`, `moc-system`, `note-organization`, `note-types`, `organization-system`, `outline-method`, `para`, `processing-workflow`, `progressive-summarization`, `retrieval-system`, `review-system`, `structure-notes`, `synthesis-workflow`, `tag-taxonomy`, `zettelkasten`

### Group C: Sub-Domains & Parent Paths (L3)
Hierarchical tags indicating more specific areas.

- **C1 (PKM/PKB/Obsidian):** `digital-garden/maintenance`, `digital-garden/philosophy`, `digital-garden/publishing`, `digital-garden/structure`, `information-architecture/navigation`, `information-architecture/organization`, `information-architecture/retrieval`, `information-architecture/taxonomy`, `knowledge-graph/linking`, `knowledge-graph/structure`, `knowledge-graph/theory`, `knowledge-graph/visualization`, `knowledge-work/learning`, `knowledge-work/reading`, `knowledge-work/research`, `knowledge-work/thinking`, `knowledge-work/writing`, `knowledge-workflow/capture`, `knowledge-workflow/output`, `knowledge-workflow/processing`, `knowledge-workflow/review`, `knowledge-workflow/synthesis`, `note-taking/formats`, `note-taking/practices`, `note-taking/types`, `note-taking/zettelkasten`, `obsidian/advanced`, `obsidian/configuration`, `obsidian/core-features`, `obsidian/customization`, `obsidian/plugins`, `pkb/architecture`, `pkb/components`, `pkb/design`, `pkb/maintenance`, `pkb/metadata`, `pkb/optimization`, `pkm/methodology`, `pkm/principles`, `pkm/research`, `pkm/theory`, `pkm/workflow`, `productivity/gtd`, `productivity/para`, `productivity/task-management`, `productivity/time-management`
- **C2 (Cognitive Science):** `cognitive-science/attention`, `cognitive-science/cognitive-load`, `cognitive-science/executive-function`, `cognitive-science/memory`, `cognitive-science/metacognition`, `cognitive-science/reasoning`, `critical-thinking/analysis`, `critical-thinking/evaluation`, `critical-thinking/logic`, `critical-thinking/problem-solving`, `critical-thinking/synthesis`, `learning-theory/andragogy`, `learning-theory/cognitive-apprenticeship`, `learning-theory/constructivism`, `learning-theory/heutagogy`, `learning-theory/pedagogy`, `self-improvement/growth-mindset`, `self-improvement/mental-models`, `self-improvement/productivity`, `self-improvement/reflective-practice`, `self-improvement/skill-development`, `self-regulation/behavioral`, `self-regulation/emotional`, `self-regulation/goal-setting`, `self-regulation/motivation`, `self-regulation/self-control`, `self-regulation/theory`
- **C3 (Prompt Engineering):** `advanced-prompting/agents`, `advanced-prompting/chain-systems`, `advanced-prompting/function-calling`, `advanced-prompting/multi-modal`, `advanced-prompting/programming`, `advanced-prompting/rag`, `context-management/compression`, `context-management/injection`, `context-management/memory`, `context-management/window`, `llm-architecture/context-window`, `llm-architecture/model-family`, `llm-architecture/model-size`, `llm-architecture/training`, `llm-architecture/transformer`, `llm-capability/generation`, `llm-capability/knowledge`, `llm-capability/reasoning`, `llm-capability/understanding`, `llm-limitation`, `prompt-application/analysis`, `prompt-application/coding`, `prompt-application/creative`, `prompt-application/education`, `prompt-application/productivity`, `prompt-application/writing`, `prompt-engineering/anatomy`, `prompt-engineering/evaluation`, `prompt-engineering/optimization`, `prompt-engineering/principles`, `prompt-engineering/theory`, `prompt-pattern/context-control`, `prompt-pattern/error-handling`, `prompt-pattern/multi-turn`, `prompt-pattern/output-format`, `prompt-pattern/persona`, `prompt-pattern/template`, `prompt-safety/adversarial`, `prompt-safety/alignment`, `prompt-safety/bias`, `prompt-safety/content-policy`, `prompt-safety/information-security`, `prompt-workflow/deployment`, `prompt-workflow/evaluation`, `prompt-workflow/ideation`, `prompt-workflow/prototyping`, `prompt-workflow/version-control`, `prompting-technique/chain-of-thought`, `prompting-technique/few-shot`, `prompting-technique/meta-prompting`, `prompting-technique/react`, `prompting-technique/reasoning`, `prompting-technique/reflection`, `prompting-technique/zero-shot`

### Groups D-J: Granular Concepts & Mechanisms (L4)
These tags represent the most specific concepts, theories, and technical details.

- **Group D (CogSci - Memory & Attention):** `attention`, `auditory-perception`, `autobiographical-memory`, `consolidation`, `divided-attention`, `encoding`, `episodic-memory`, `interference`, `long-term-memory`, `multimodal-integration`, `perception`, `phonological-loop`, `procedural-memory`, `prospective-memory`, `reconsolidation`, `retrieval`, `selective-attention`, `semantic-memory`, `sustained-attention`, `visual-perception`, `visuospatial-sketchpad`, `working-memory`
- **Group E (CogSci - Executive Function & Reasoning):** `abductive-reasoning`, `analogical-reasoning`, `central-executive`, `cognitive-control`, `cognitive-flexibility`, `conflict-monitoring`, `creative-thinking`, `critical-thinking`, `deductive-reasoning`, `error-monitoring`, `executive-function`, `inductive-reasoning`, `inhibitory-control`, `performance-monitoring`, `planning`, `problem-solving`, `reasoning`, `response-inhibition`, `self-regulation`, `task-switching`
- **Group F (CogSci - Learning & Metacognition):** `active-recall`, `andragogy-pkm`, `attention-management`, `calibration`, `calibration-practices`, `cognitive-load-management`, `cognitive-load-theory`, `conceptual-learning`, `control-processes`, `desirable-difficulties`, `elaborative-encoding`, `elaborative-interrogation`, `explicit-learning`, `expertise-development`, `generation-effect`, `germane-load`, `germane-load-optimization`, `implicit-learning`, `instructional-design-pkm`, `interleaving`, `intrinsic-load`, `learning-processes`, `metacognitive-monitoring`, `metacognitive-pkm`, `metacomprehension`, `metamemory`, `monitoring`, `self-directed-learning`, `self-explanation`, `self-regulated-learning`, `skill-acquisition`, `spacing-effect`, `testing-effect`, `transfer-of-learning`, `working-memory-capacity`, `working-memory-support`
- **Group G (CogSci - Theories & Models):** `ACT-R`, `cognitive-resources`, `distributed-cognition`, `dual-process-theory`, `embodied-cognition`, `enactive-cognition`, `extraneous-load`, `extraneous-load-reduction`, `extended-cognition`, `global-workspace-theory`, `grounded-cognition`, `information-processing-theory`, `levels-of-processing`, `memory-systems`, `mental-effort`, `multiple-drafts-model`, `parallel-distributed-processing`, `situated-cognition`, `SOAR`, `spreading-activation`, `symbolic-architecture`
- **Group H (PKM/Obsidian - Technical):** `api-integration`, `automation`, `backlinks`, `backup-systems`, `bidirectional-links`, `breadcrumbs`, `daily-notes`, `dataview`, `dataview-queries`, `dataviewjs`, `excalidraw`, `export-import`, `file-naming`, `filter-strategies`, `folder-hierarchy`, `folder-strategy`, `frontmatter-design`, `graph-analysis`, `javascript`, `language-processing`, `link-density`, `link-maintenance`, `linking-strategy`, `meeting-notes`, `meta-bind`, `metadata-schema`, `metadata-systems`, `naming-conventions`, `note-templates`, `obsidian-plugins`, `orphan-notes`, `progressive-review`, `quick-capture`, `quickadd`, `quickadd-macros`, `search-operators`, `semantic-search`, `smart-connections`, `spaced-repetition`, `status-tracking`, `sync-systems`, `tag-cleanup`, `tag-strategy`, `tag-taxonomy`, `tasks-plugin`, `template-automation`, `templater`, `templater-scripts`, `transclusion`, `unlinked-mentions`, `version-control`, `wiki-links`
- **Group I (Prompt Engineering - Techniques):** `advanced-prompting/agents/autonomous`, `advanced-prompting/agents/multi-agent`, `advanced-prompting/agents/planning`, `advanced-prompting/agents/tool-use`, `advanced-prompting/rag/context-injection`, `advanced-prompting/rag/hybrid-search`, `advanced-prompting/rag/retrieval`, `llm-limitation/bias`, `llm-limitation/hallucination`, `llm-limitation/reasoning-failures`, `prompt-pattern/context-control/constraints`, `prompt-pattern/context-control/framing`, `prompt-pattern/context-control/perspective`, `prompt-pattern/error-handling/clarification`, `prompt-pattern/error-handling/fallback`, `prompt-pattern/error-handling/validation`, `prompt-pattern/multi-turn/context-threading`, `prompt-pattern/multi-turn/conversation`, `prompt-pattern/multi-turn/state-management`, `prompt-pattern/output-format/code`, `prompt-pattern/output-format/creative`, `prompt-pattern/output-format/markdown`, `prompt-pattern/output-format/structured-data`, `prompt-pattern/persona/expertise`, `prompt-pattern/persona/role-assignment`, `prompt-pattern/persona/style`, `prompt-pattern/template/fill-in-blank`, `prompt-pattern/template/formulaic`, `prompt-pattern/template/structured`, `prompt-safety/adversarial/defense`, `prompt-safety/adversarial/jailbreaking`, `prompt-safety/adversarial/prompt-injection`, `prompting-technique/chain-of-thought/basic`, `prompting-technique/chain-of-thought/self-consistency`, `prompting-technique/chain-of-thought/zero-shot`, `prompting-technique/few-shot/diversity`, `prompting-technique/few-shot/example-ordering`, `prompting-technique/few-shot/example-selection`, `prompting-technique/meta-prompting/optimization`, `prompting-technique/meta-prompting/prompt-generation`, `prompting-technique/meta-prompting/self-improvement`, `prompting-technique/react/iteration`, `prompting-technique/react/reasoning-acting`, `prompting-technique/react/tool-use`, `prompting-technique/reasoning/decomposition`, `prompting-technique/reasoning/graph-of-thoughts`, `prompting-technique/reasoning/step-by-step`, `prompting-technique/reasoning/tree-of-thoughts`, `prompting-technique/reflection/refinement`, `prompting-technique/reflection/self-critique`, `prompting-technique/reflection/verification`, `prompting-technique/zero-shot/instruction`, `prompting-technique/zero-shot/task-specification`
- **Group J (Cross-Cutting Concepts & Research):** `aging-cognition`, `applied-cognition`, `attention-architecture`, `behavioral-experiments`, `clinical-cognition`, `cognitive-decline`, `cognitive-disorders`, `cognitive-enhancement`, `cognitive-modeling`, `cognitive-pkm`, `cognitive-rehabilitation`, `cognitive-training`, `concept/attention-mechanism`, `concept/atomic-notes`, `concept/automaticity`, `concept/bidirectional-linking`, `concept/chunking`, `concept/cognitive-bias`, `concept/cognitive-overhead`, `concept/context-switching`, `concept/discoverability`, `concept/distributed-practice`, `concept/dual-coding`, `concept/elaboration`, `concept/emergence`, `concept/error-correction`, `concept/evergreen-notes`, `concept/external-cognition`, `concept/few-shot-exemplars`, `concept/flow-state`, `concept/generation-effect`, `concept/in-context-learning`, `concept/information-overload`, `concept/instruction-following`, `concept/interleaving`, `concept/knowledge-synthesis`, `concept/knowledge-transfer`, `concept/linking-thinking`, `concept/mental-representation`, `concept/networked-thought`, `concept/output-validation`, `concept/progressive-summarization`, `concept/prompt-chaining`, `concept/prompt-template`, `concept/retrieval-practice`, `concept/second-brain`, `concept/semantic-similarity`, `concept/serendipity`, `concept/spacing-effect`, `concept/system-message`, `concept/task-decomposition`, `concept/temperature-control`, `concept/testing-effect`, `concept/token-probability`, `concept/top-p-sampling`, `concept/transfer`, `concept/transformer-architecture`, `concept/wayfinding`, `consolidation-workflow`, `cross-cultural-cognition`, `cross-sectional-research`, `developmental-cognition`, `educational-applications`, `empirical-research`, `encoding-strategies`, `evidence-based-pkm`, `experimental-design`, `learning-analytics`, `learning-optimization`, `longitudinal-research`, `memory-systems-design`, `meta-analysis`, `neurodevelopmental`, `neuroimaging-studies`, `reflection-systems`, `retrieval-practice-pkm`, `spaced-review-system`, `technology-cognition`, `workplace-cognition`

---

## 4. Other Template Features

- **Review System**: The template contains logic to calculate a `next-review` date and create a follow-up task. The interval is based on `maturity` and `confidence` levels.
- **Dynamic Content**: The body is populated with numerous `dataviewjs` blocks that provide dynamic analysis of the note's relationship to other notes in the vault. These are for display only and cannot be queried directly.
- **Extractable Definitions**: The template includes a DataviewJS script to find and aggregate definitions formatted as `[**Key**:: Value]` from a specific folder.