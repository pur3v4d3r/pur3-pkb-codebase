---
title: "PKM/PKB Framework 1.0.0: Expansion Topic Registry"
doc_id: "pkm-pkb-framework-expansion-topics-v1-0"
doc_type: "expansion-registry"
doc_created: 2026-03-16
doc_modified: 2026-03-16
author: "claude-sonnet-4-6 (via PKB Review Agent)"
primary_domain: "knowledge-management"
status: evergreen
confidence: high
source_synthesis: "[[pkm-pkb-framework-synthesis]]"
---

# PKM/PKB Framework 1.0.0: Expansion Topic Registry

*Compiled from Pass 4 (Critical Analysis) of the six-pass analytical review.*
*Topics are drawn from two sources: (1) gaps identified by the review agent; (2) the 198 `[!topic-idea]` callouts embedded within the 30 reports themselves, curated and prioritized.*

---

## Critical Priority
*These topics represent structural gaps whose absence meaningfully limits the framework's practical utility*

> [!further-exploration] **Critical Priority Expansions**

> [!topic-idea] **[[PKM/PKB Implementation Guide for Obsidian]]**
> **Gap Identified by:** Review Agent (Pass 4) — most significant gap in the entire codebase
> **Gap Description:** The series provides excellent principle-level guidance but almost no concrete Obsidian implementation. Phase V sections in every report reference "Obsidian patterns" but rarely provide them. The following are missing: YAML frontmatter templates for each note type (Atomic, Concept, MOC); Templater templates for active recall workflows; CSS snippet definitions for all 25+ custom callout types (`[!ask-yourself-this]`, `[!best-practice]`, `[!analytical-insight]`, etc.); Dataview queries for review workflows, calibration tracking, and integration metabolism.
> **Where It Would Connect:** All 30 reports; especially Reports 09, 12, 17, 20, 25, 27
> **Estimated Effort:** Substantial — systematic translation of all Phase V recommendations
> **Value Proposition:** Without this, the framework remains intellectually ambitious but practically inaccessible. This is the bridge from knowing to doing.
> **Suggested Approach:** Work through each report's Phase V section systematically, extracting every design recommendation that implies an Obsidian pattern. Group by note type, workflow, and automation. Produce companion templates and snippets.

> [!topic-idea] **[[Neuroscience of Learning for PKB Design]]**
> **Gap Identified by:** Review Agent (Pass 4) — entirely absent from series
> **Gap Description:** Sleep-dependent memory consolidation (Walker, Stickgold), hippocampal schema formation (McClelland et al.), neuroimaging studies of expert knowledge activation (expertise neuroscience), and the neuroscience of habit formation (Graybiel) are completely absent despite being directly relevant to PKB design.
> **Where It Would Connect:** Report 06 (primary), Reports 01, 02, 19
> **Estimated Effort:** Moderate
> **Value Proposition:** Would provide new design principles not derivable from behavioral research alone — e.g., review scheduling calibrated to sleep-dependent consolidation cycles; note complexity calibrated to hippocampal encoding constraints.
> **Key Sources:** Walker (2017) *Why We Sleep*; Stickgold & Walker (2013) on sleep and memory; McClelland et al. (1995) complementary learning systems; Squire (1992) memory systems; Graybiel (2008) habits and procedural memory.

> [!topic-idea] **[[PKB Network Topology Audit — Design and Implementation]]**
> **Gap Identified by:** Review Agent (Pass 4) — Report 25's most actionable insight has no tool
> **Gap Description:** Report 25 makes a compelling case that PKB quality should be measured by network topology (small-world properties, betweenness centrality, clustering coefficient) rather than content coverage. But it provides no tool for actually performing this analysis on an Obsidian vault.
> **Where It Would Connect:** Reports 25, 15, 01, 09
> **Estimated Effort:** Moderate — requires Python/JavaScript graph analysis of vault
> **Value Proposition:** Transforms Report 25's most important insight from theoretical to operational. A practitioner could run this quarterly as part of their Integration Metabolism protocol (Report 27, RP3).
> **Suggested Approach:** Use Obsidian's graph API or parse vault markdown to build an adjacency matrix; compute centrality metrics using NetworkX; identify top 10 betweenness-centrality notes, current clustering coefficient, and average path length; surface lowest-centrality domain clusters as integration targets.

---

## High Priority
*Significant gaps or important extensions that would substantially strengthen the framework*

> [!further-exploration] **High Priority Expansions**

> [!topic-idea] **[[AI-PKM Integration Design Patterns — Operationalizing the Offloading Quality Distinction]]**
> **Gap Identified by:** Review Agent (Pass 4) + Report 30 (internal gap acknowledgment)
> **Gap Description:** Report 30 correctly identifies the Offloading Quality Distinction (storage/retrieval offloading is beneficial; synthesis/construction offloading is harmful) but does not develop a concrete workflow framework for implementing it. Practitioners need specific decision rules: which AI interactions are beneficial for which cognitive tasks?
> **Where It Would Connect:** Report 30 (primary), Reports 06, 16, 17, 04
> **Estimated Effort:** Moderate
> **Value Proposition:** Directly addresses the most pressing practical question for PKM practitioners in 2026. The framework's silence on "how to use AI well in a PKB" is its largest contemporaneous gap.
> **Suggested Approach:** Classify every common PKM-AI interaction by offloading type (storage vs. synthesis vs. challenge-generation); map each to its likely cognitive effect using desirable difficulties research; produce decision flowchart and workflow templates.

> [!topic-idea] **[[The Tacit Knowledge Development Practice — Complementing the PKB]]**
> **Source:** Review Agent (Pass 4) + Report 22 (internal expansion flag)
> **Gap Description:** Report 22 establishes what the PKB cannot do but does not develop the complementary practices — deliberate practice, mentorship, apprenticeship, performative experience — that develop the tacit dimensions of expertise. The Tacit Knowledge Observatory requires knowing what to observe; this requires understanding what produces tacit competence.
> **Where It Would Connect:** Reports 22, 08, 10, 24
> **Estimated Effort:** Moderate
> **Key Sources:** Ericsson's deliberate practice research; Collins on tacit knowledge transmission; Polanyi on apprenticeship; Dreyfus on phenomenology of skill acquisition.

> [!topic-idea] **[[Mental-Models-and-PKB-Design-—-Johnson-Laird's-Alternative-to-Schema-Theory]]**
> **Source:** Report 01 Expansion Topics (internal)
> **Gap Description:** Philip Johnson-Laird's mental model theory offers an important alternative to schema theory: mental models are analog, spatial, and "runnable" — they can be mentally simulated to generate predictions. What would it mean to design PKB notes that function as runnable mental models? How does the mental model perspective change Report 01's design recommendations?
> **Where It Would Connect:** Reports 01, 02, 09, 11, 22
> **Estimated Effort:** Moderate
> **Value Proposition:** Extends the cognitive architecture foundation into the domain of dynamic, causal, and spatial reasoning — where schema theory alone is insufficient.

> [!topic-idea] **[[Knowledge Graph Theory Applied to PKB Design — Network Science for Personal Knowledge]]**
> **Source:** Report 01 Expansion Topics (internal)
> **Gap Description:** The recommendation to build PKBs as semantic networks invites formal analysis using network science tools: degree centrality, betweenness centrality, clustering coefficients, scale-free network structure, and power-law distributions. What does a network analysis of a mature PKB reveal about knowledge organization quality? What network metrics should PKM practitioners track as leading indicators?
> **Where It Would Connect:** Reports 01, 15, 20, 25
> **Estimated Effort:** Moderate-substantial
> **Value Proposition:** Bridges knowledge management, cognitive science, and network science in a quantitative analysis of PKB structure — provides the theoretical foundation for the Network Topology Audit Tool.

> [!topic-idea] **[[Ontology Design for Personal Knowledge Bases — Formal Approaches to Cognitive Alignment]]**
> **Source:** Report 01 Expansion Topics (internal)
> **Gap Description:** Formal ontology design (OWL, RDF, knowledge graphs) represents the most sophisticated technical approach to the Cognitive Alignment Principle — specifying not only concepts and hierarchies but arbitrary typed relationships, inference rules, and formal axioms. What would it look like to apply ontology methodology to a personal PKB? What relationship vocabulary would serve a generalist lifelong learner?
> **Where It Would Connect:** Reports 01, 09, 15, 25
> **Estimated Effort:** Substantial
> **Value Proposition:** The highest-precision implementation of the Cognitive Alignment Principle — for practitioners ready to invest seriously in relational architecture.

> [!topic-idea] **[[Feedback Loop Architecture for PKM — Designing the System That Learns From Itself]]**
> **Source:** Report 26 (internal expansion direction) + Review Agent
> **Gap Description:** Report 26 introduces feedback loops in PKM but does not fully develop the systems-design perspective: how to build explicit feedback mechanisms into PKB architecture so that the system improves over time based on the practitioner's performance data (calibration scores, retrieval failures, integration gaps).
> **Where It Would Connect:** Reports 12, 18, 26, 27
> **Estimated Effort:** Moderate
> **Value Proposition:** Closes the loop between the series' diagnostic tools (calibration, retrieval practice, integration audits) and structural improvement of the PKB itself.

---

## Medium Priority
*Valuable extensions that would deepen specific areas of the framework*

> [!further-exploration] **Medium Priority Expansions**

> [!topic-idea] **[[The Novice-to-Expert Transition in Knowledge Organization — Implications for PKB Architecture Evolution]]**
> **Source:** Report 01 Expansion Topics (internal)
> **Gap Description:** Chi et al.'s research documents expert vs. novice organizational differences, but what is the cognitive mechanism of the transition — and what role can a PKB play in actively supporting it? How does a PKB designed according to the Cognitive Alignment Principle from the beginning accelerate the novice-to-expert transition?
> **Where It Would Connect:** Reports 01, 10, 11, 24
> **Estimated Effort:** Moderate

> [!topic-idea] **[[Embodied-and-Situated-Cognition-—-What-Text-Based-PKBs-Cannot-Capture]]**
> **Source:** Report 01 Expansion Topics (internal)
> **Gap Description:** Embodied cognition (Lakoff & Johnson, Varela et al.) and situated cognition (Brown et al.) argue that much of what we know is grounded in bodily experience and situational context in ways text-based representations cannot fully capture. What categories of knowledge resist text capture? What complementary practices address these? This report would honestly map the PKB's limits from an embodied cognition perspective — complementing Report 22's phenomenological approach.
> **Where It Would Connect:** Reports 22, 23, 24, 28
> **Estimated Effort:** Moderate

> [!topic-idea] **[[The Cognitive Economics of PKB Maintenance — When Organizational Effort Pays Off]]**
> **Source:** Report 01 Expansion Topics (internal)
> **Gap Description:** When does the organizational overhead of principle-organized concept notes, explicit relationship typing, and multi-dimensional tagging pay off in retrieval and learning dividends — and when does it become self-defeating? Drawing on attention research (Kahneman), habit formation theory, and the Stoic concept of judicious effort allocation.
> **Where It Would Connect:** Reports 01, 05, 09, 13, 19
> **Estimated Effort:** Moderate

> [!topic-idea] **[[Socratic Dialogue and Dialectical PKM — Productive Intellectual Disagreement as Practice]]**
> **Source:** Reports 07, 14, 21 internal expansion flags
> **Gap Description:** The series recommends dialectical engagement (devil's advocate notes, steel-man notes, synthesis notes) but does not fully develop the Socratic dialogue tradition as a PKM practice. What would it mean to structure a PKB around Socratic inquiry as the primary mode of knowledge development?
> **Where It Would Connect:** Reports 07, 14, 21, 29
> **Estimated Effort:** Moderate

> [!topic-idea] **[[Epistemic Justice in Personal Knowledge Curation — Whose Knowledge Counts in Your PKB?]]**
> **Source:** Report 29 internal expansion + Review Agent
> **Gap Description:** Report 29 introduces epistemic justice (Fricker) but does not develop its practical implications for PKB design. Whose sources do you cite? Whose experience do you count as evidence? Which communities of knowledge do you draw on or exclude? This report would develop the epistemic justice audit as a periodic PKB practice.
> **Where It Would Connect:** Reports 07, 18, 21, 29
> **Estimated Effort:** Moderate

> [!topic-idea] **[[Calibration as Daily Practice — Concrete Protocols for Epistemic Accuracy]]**
> **Source:** Reports 18, 12 internal expansion direction
> **Gap Description:** Report 18 establishes calibration as essential and provides the theoretical framework. A companion report developing concrete daily/weekly calibration protocols — pre-reading confidence rating, post-reading knowledge state tracking, comparison against active recall performance — would significantly increase the practical utility of this framework element.
> **Where It Would Connect:** Reports 18, 12, 04, 27
> **Estimated Effort:** Low-Moderate

> [!topic-idea] **[[The Integration Problem: Practical Protocols for Building Bridge Notes]]**
> **Source:** Report 25 + Review Agent
> **Gap Description:** Report 25 provides the theoretical diagnosis of the Integration Problem (lack of bridge notes with high betweenness centrality) but does not develop practical protocols for systematically creating them. What are the practices, prompts, and workflows that reliably produce bridge notes?
> **Where It Would Connect:** Reports 25, 15, 09, 27
> **Estimated Effort:** Low-Moderate

> [!topic-idea] **[[Stoic Practices for Learning Resilience — Marcus Aurelius, Epictetus, and the Serious Learner]]**
> **Source:** Report 13 internal expansion direction
> **Gap Description:** Report 13 introduces Stoic philosophy as a framework for learning resilience but covers it at the conceptual level. A deeper treatment — specific Stoic practices (negative visualization, memento mori, prosoche, the view from above) and their direct application to PKM challenges (frustration with learning slowness, difficulty of desirable difficulties, intellectual hubris) — would be practically useful.
> **Where It Would Connect:** Reports 05, 13, 19, 29
> **Estimated Effort:** Moderate

---

## Exploratory Priority
*Intellectually interesting extensions that could expand the framework's scope*

> [!further-exploration] **Exploratory Priority Expansions**

> [!topic-idea] **[[The Philosophy of Personal Knowledge — Gettier, Justified True Belief, and What a PKB Can "Know"]]**
> **Source:** Report 28 internal expansion flags
> **Gap Description:** Report 28 opens the philosophical question of what "knowing" means for a PKB practitioner. A deeper treatment of the post-Gettier epistemology literature, reliabilism, and virtue epistemology accounts of knowledge would strengthen the philosophical foundation of the entire series.
> **Where It Would Connect:** Reports 28, 29, 18, 07
> **Estimated Effort:** Substantial

> [!topic-idea] **[[Collective and Collaborative PKM — Transactive Memory Systems and Shared Knowledge Networks]]**
> **Source:** Review Agent (identified structural gap — series treats PKM as entirely solo)
> **Gap Description:** The series is entirely focused on individual PKM. Wegner's Transactive Memory Systems, organizational knowledge management (Nonaka), and collaborative sense-making represent a substantial adjacent domain with direct implications for how individual PKBs can participate in and contribute to collective knowledge ecosystems.
> **Where It Would Connect:** Reports 22, 26, 30
> **Estimated Effort:** Substantial — significant new domain

> [!topic-idea] **[[The Future of PKM Beyond Text — Multimodal Knowledge Representation]]**
> **Source:** Review Agent (identified future direction)
> **Gap Description:** The entire framework assumes text-based note-taking. Emerging multimodal AI capabilities (vision, voice, spatial computing) raise the question of what PKB design looks like when notes can include images, audio, video, and spatial representations. What cognitive architecture principles from the series apply, and which require revision?
> **Where It Would Connect:** Reports 01, 22, 23, 30
> **Estimated Effort:** Speculative but high interest

> [!topic-idea] **[[Complexity and Emergence in Knowledge Systems — When the PKB Becomes More Than Its Parts]]**
> **Source:** Review Agent (emergent from Pass 3 relational analysis)
> **Gap Description:** The series implicitly assumes that the PKB's value is the sum of its components. Complexity theory suggests that well-structured knowledge networks exhibit emergent properties — insights and connections that were not explicit in any individual note. This report would develop a complexity-theoretic account of how PKBs generate emergent understanding.
> **Where It Would Connect:** Reports 25, 26, 15
> **Estimated Effort:** Speculative — would require novel synthesis

---

## Expansion Topics from Within the Series (Curated Top 15)

*The 30 reports collectively contain 198 `[!topic-idea]` callouts. The following 15 are the most structurally important across the series — the topics that multiple reports point toward independently.*

| # | Topic | Source Reports | Priority |
|---|-------|---------------|----------|
| 1 | Knowledge Graph Theory for PKB Design | Reports 01, 15, 20, 25 | High |
| 2 | Ontology Design for Personal Knowledge Bases | Report 01 | High |
| 3 | Mental Models and PKB Design (Johnson-Laird) | Report 01 | High |
| 4 | Embodied Cognition Limits of Text-Based PKBs | Reports 01, 22 | Medium |
| 5 | Cognitive Economics of PKB Maintenance | Reports 01, 05, 19 | Medium |
| 6 | The Novice-to-Expert Transition in Organization | Reports 01, 10 | Medium |
| 7 | Forgetting as Feature: Planned Obsolescence in PKBs | Reports 06, 22 | Medium |
| 8 | Analogical Reasoning and Cross-Domain Transfer | Reports 11, 14 | Medium |
| 9 | Progressive Summarization and Capture Hierarchies | Reports 09, 17 | Medium |
| 10 | The PKB as a Writing Instrument (Commonplace → Zettelkasten) | Report 17 | Low-Medium |
| 11 | Epistemic Bubbles and PKB Curation Bias | Reports 07, 21, 29 | Medium |
| 12 | The Role of Wonder and Curiosity in Lifelong Learning | Reports 05, 14, 24 | Low-Medium |
| 13 | Complexity Science and Emergent Knowledge | Reports 25, 26 | Exploratory |
| 14 | Death and Knowledge: What Happens to Your PKB? | Reports 19, 28 | Exploratory |
| 15 | The PKB as Cultural Artifact — Intellectual Legacy | Reports 24, 29 | Exploratory |

---

## Quick Reference: Expansion by Framework Tier

| Tier | Report Gap | Priority |
|------|-----------|----------|
| Tier 1 Supplement | Neuroscience of Learning | High |
| Tier 1 Supplement | Mental Models (Johnson-Laird) | High |
| Tier 2 Supplement | Obsidian Implementation Guide | Critical |
| Tier 2 Supplement | Calibration as Daily Practice | Medium |
| Tier 2 Supplement | Bridge Note Building Protocols | Medium |
| Tier 3 Supplement | Tacit Knowledge Development Practice | High |
| Tier 3 Supplement | Network Topology Audit Tool | High |
| Tier 3 Supplement | Feedback Loop Architecture | Medium |
| Tier 4 Supplement | AI-PKM Integration Design Patterns | High |
| Tier 4 Supplement | Collective and Collaborative PKM | Exploratory |
| Cross-Tier | Epistemic Justice in Personal Curation | Medium |
| Cross-Tier | Cognitive Economics of PKB Maintenance | Medium |

---

*Expansion Topic Registry Version 1.0.0*
*Generated by PKB Codebase Review & Synthesis Agent v1.0.0*
*Source analysis: pkb-pkm-report-series-codebase-pack.md (23,164 lines, 31 documents)*
