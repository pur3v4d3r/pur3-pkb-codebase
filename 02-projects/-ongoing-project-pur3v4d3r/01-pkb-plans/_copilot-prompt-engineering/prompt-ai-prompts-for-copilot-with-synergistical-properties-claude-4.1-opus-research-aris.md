---
title: Prompt_AI-Prompts-for-Copilot-with-Synergistical-Properties_Claude-4.1-Opus_Research_Aris
aliases:
  - Claude AI Prompts for Obsidian - Aris Persona
  - Claude Aris Copilot Prompt Library
  - Synergistic Copilot Prompts - Claude Aris
tags:
  - prompt-engineering/llm/library
  - tools/ai/claude
  - tools/obsidian/copilot
  - workflows/pkm/automation
status: seedling
created: 2024-09-29
updated: 2024-09-29
source: "[[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]"
related:
  - "[[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]"
date created: Monday, September 29th 2025, 12:03:43 am
date modified: Monday, September 29th 2025, 12:17:05 am
---

#### Sources:

[^1]: [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]]
[^2]: [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]
[^3]: [[Types of Notes]]
[^4]: [[Note-Taking for Different Subjects and Contexts]]
[^5]: [[Outline Note Method]]
[^6]: [[Visual and Associative Methods for Note Taking]]
[^7]: [[How to Properly Cite a Source]]
[^8]: [[Advanced Search Engine Use]]
[^9]: [[ChatGPT Universal Smart Note Template SOP]]
[^10]: [[ref_chatgpt_research_guide-to-moc's_2025-09-23]]
[^11]: [[Workflow for Evaluating Sources and Information]]
[^12]: [[Source Evaluation - A Three Tiered Approach]]
[^13]: [[ref_notes_guide-to-active-reading-by-ai's_2025-09-24]]
[^14]: [[Common Logical Fallacies]]
[^15]: [[Function of Notes is Important]]
[^16]: [[S I F T - Lateral Reading for Source Verification]]
[^17]: [[The Toulmin Model]]
[^18]: [[Document Your Searches during Research]]
[^19]: [[REF_Gemini-Chat_Response-to-Note_Researching Material for use in Vault_2025-09-12]]
[^20]: [[ref_gemini-prompt_guide-to-obsidian-plug-in-quickadd_2025-09-24]]

> [!the-purpose]
> This is a prompt created using the Elias Prompt Architect Gem, its purpose is to generate Synergistical Prompts using my current Obsidian Plugins.
> - These are some important reference links:
> 
>   - [[Draft_Prompts-for-Generating-Copilot-Prompts_Pur3v4d3r]] - This is a link to the original Prompt used.
> 
>   - [[AI Persona Instruction Set - The Prompt Architect - Dr. Aris Thorne]]- This is a link to Persona that was use to create this. 

# 🤖 Obsidian Copilot Prompts Reference Guide

## 📑 Table of Contents

- [📥 Information Capture & Processing](https://claude.ai/chat/d10214ea-20f4-459b-972b-e6476e56954a#-information-capture--processing)
- [🧠 Synthesis & Connection](https://claude.ai/chat/d10214ea-20f4-459b-972b-e6476e56954a#-synthesis--connection)
- [✍️ Creation & Elaboration](https://claude.ai/chat/d10214ea-20f4-459b-972b-e6476e56954a#-creation--elaboration)
- [🔍 Review & Resurfacing](https://claude.ai/chat/d10214ea-20f4-459b-972b-e6476e56954a#-review--resurfacing)

---

## 📥 Information Capture & Processing

#### **Smart Note Scaffolding**

> **Synergy:** Copilot + Quick Add + Periodic Notes

**🎯 Goal:** Transform raw information into a structured note with metadata, tags, and initial connections to existing knowledge.

**⚡ Trigger:** When capturing new information from articles, videos, or conversations that need to be properly integrated into your PKB.

**💡 Prompt:**

```
Act as a knowledge architect. I have the following raw information to process:

{{selection}}

Please structure this into a proper note by:
1. Creating a concise title that captures the core concept
2. Generating 3-5 relevant tags in the format #topic/subtopic
3. Writing a one-paragraph summary (50-75 words)
4. Extracting the 3 most important key points as bullet points
5. Suggesting 2-3 existing notes this might connect to (use [[note name]] format)
6. Creating a "Questions to Explore" section with 2 thought-provoking questions
7. Adding a metadata section with source, date captured, and relevance score (1-5)

Format the output as a complete Obsidian note ready to save.
```

**Example Usage:** Copy a dense paragraph from a research paper, run this prompt, and receive a fully structured note with metadata, tags like `#photography/technique/composition`, a summary, key points, and questions like "How does this concept relate to Glenn Randall's philosophical approach to landscape photography?"

---

#### **Meeting Minutes Processor**

> **Synergy:** Copilot + Tasks + Dataview

**🎯 Goal:** Convert messy meeting notes into actionable items with properly formatted tasks and queryable metadata.

**⚡ Trigger:** Immediately after a meeting, workshop, or brainstorming session when you have rough notes to process.

**💡 Prompt:**

```
Transform these meeting notes into a structured format:

{{selection}}

Please:
1. Create a brief meeting summary (2-3 sentences)
2. Extract all action items and format them as Tasks plugin checkboxes with due dates:
   - [ ] Task description 📅 YYYY-MM-DD
3. Identify key decisions made and list them under "## Decisions"
4. Create a "## Participants" section with attendee names
5. Add Dataview-compatible frontmatter:
   - meeting_type: [type]
   - date: YYYY-MM-DD
   - project: [project name]
   - status: active
6. Highlight any follow-up questions or unresolved issues
7. Tag appropriately with #meeting/[type]

Output the complete formatted note.
```

**Example Usage:** Paste rough notes like "discussed new photo project timeline, John will review by Friday, need budget approval" and receive a structured note with tasks like `- [ ] John to review project timeline 📅 2025-10-03` and proper Dataview metadata.

---

#### **Visual Concept Mapper**

> **Synergy:** Copilot + Excalidraw + Highlighter

**🎯 Goal:** Generate instructions for creating visual concept maps in Excalidraw based on highlighted text passages.

**⚡ Trigger:** When processing complex theoretical content that would benefit from visual representation.

**💡 Prompt:**

```
Analyze this highlighted content and design a visual concept map:

{{selection}}

Provide:
1. A central node title for the main concept
2. 4-6 primary branches with key themes
3. 2-3 sub-branches for each primary branch
4. Suggested colors for different concept categories (use Highlighter plugin colors: ==yellow==, ==[!red]==, ==[*green*]==, ==[~blue~]==)
5. 3-4 connection lines between related concepts with relationship labels
6. Recommended icons or symbols for each major node (using Iconize plugin suggestions)
7. A brief note on the visual hierarchy and flow direction

Format as step-by-step Excalidraw drawing instructions.
```

**Example Usage:** Input a complex paragraph about exposure triangle in photography, receive structured instructions like "Central node: 'Exposure Triangle', Branch 1: 'Aperture' (==[_green_]== for creative control), connect to 'Depth of Field' with 'controls' label..."

---

#### **Source Citation Generator**

> **Synergy:** Copilot + Linter + Periodic Notes

**🎯 Goal:** Automatically format and standardize citations while creating a daily log entry for research activities.

**⚡ Trigger:** When adding new sources to your research notes or bibliography.

**💡 Prompt:**

```
Process this source information into proper citations:

[SOURCE INFO: {{selection}}]

Generate:
1. A formatted citation in Chicago style
2. An APA style alternative
3. A simplified Obsidian-friendly reference: [[Author Last Name YYYY]]
4. Extract 3 key quotes with page numbers if available
5. Create a source evaluation:
   - Credibility: [High/Medium/Low]
   - Relevance: [Core/Supporting/Tangential]
   - Date Assessment: [Current/Recent/Dated]
6. Generate tags: #source/[type] #topic/[subject]
7. Create a daily note entry snippet:
   "📚 Researched: [Title] - [One-line takeaway]"
8. Suggest 2 follow-up sources to explore

Format with proper Markdown and ready to paste.
```

**Example Usage:** Paste a book title and author, receive formatted citations, key quotes, and a daily note entry like "📚 Researched: The Art of Photography by Bruce Barnbaum - Emphasizes pre-visualization as key to meaningful landscape photography"

---

## 🧠 Synthesis & Connection

#### **Cross-Note Pattern Detector**

> **Synergy:** Copilot + Dataview + Tag Wrangler

**🎯 Goal:** Identify hidden patterns and connections across notes with similar themes but different tags.

**⚡ Trigger:** During weekly reviews or when exploring a topic from multiple angles.

**💡 Prompt:**

```
Analyze my notes about [TOPIC] and find hidden connections:

First, search for notes containing these related terms: {{selection}}

Then:
1. Identify 3-5 recurring themes across these notes
2. Find conceptual bridges between seemingly unrelated ideas
3. Detect any contradictions or tensions between sources
4. Suggest tag consolidation using Tag Wrangler format:
   - Merge: #tag1 → #tag2
   - Create hierarchy: #parent/child
5. Generate 3 synthesis statements that combine insights from multiple notes
6. Create a "Connection Map" in list format:
   - [[Note A]] ←→ [[Note B]]: [relationship]
7. Propose 2 new note titles that would bridge gaps in your knowledge
8. Highlight the most surprising or counterintuitive connection found

Format as a research synthesis report.
```

**Example Usage:** Input "composition, philosophy, landscape photography", receive insights like "Connection found: [[Randall-Philosophy]] ←→ [[Rule-of-Thirds]]: Both emphasize intentionality over technical rules"

---

#### **Perspective Synthesizer**

> **Synergy:** Copilot + Callout Manager + Dataview

**🎯 Goal:** Create multi-perspective analysis using different callout types to visually distinguish viewpoints.

**⚡ Trigger:** When comparing different approaches, philosophies, or methodologies on the same topic.

**💡 Prompt:**

```
Create a multi-perspective analysis on: [TOPIC]

Using this context: {{selection}}

Structure the analysis with:
1. > [!info] Overview
   Brief topic introduction (2-3 sentences)

2. > [!example] Perspective A: [Name]
   - Core belief:
   - Key practices:
   - Strengths:
   - Limitations:

3. > [!example] Perspective B: [Name]
   (Same structure as A)

4. > [!abstract] Synthesis
   - Common ground between perspectives:
   - Irreconcilable differences:
   - Potential integration points:

5. > [!question] Open Questions
   - 3 unresolved questions this comparison raises

6. > [!tip] Personal Application
   - How to apply the best of both approaches
   - Specific action steps

7. Create a Dataview query to find related notes:
   ```dataview
   LIST
   FROM #topic/[relevant tag]
   WHERE contains(file.name, "[keyword]")
/```

Include relevant [[wikilinks]] throughout.

```

**Example Usage:** Topic: "Digital vs Film Photography Philosophy", receive structured callouts comparing technical purity advocates vs. hybrid approach advocates, with synthesis pointing to intentionality as the common thread.

---

#### **Insight Evolution Tracker**

> **Synergy:** Copilot + Periodic Notes + Tasks

**🎯 Goal:** Track how your understanding of a concept has evolved over time and identify next learning steps.

**⚡ Trigger:** Monthly or quarterly when reviewing progress on a major learning theme.

**💡 Prompt:**

```

Track the evolution of my understanding about: [CONCEPT]

Review notes from the past [TIME PERIOD] and:

1. **Timeline of Understanding:**
    
    - Initial understanding (date):
    - Key breakthrough moments:
    - Current understanding:
2. **Perspective Shifts:**
    
    - What I used to believe:
    - What changed my mind:
    - What I believe now:
3. **Knowledge Milestones:**
    
    - [ ] Completed: [learning achievement]
    - [ ] In Progress: [current focus]
    - [ ] Next: [future exploration]
4. **Integration with Existing Knowledge:**
    
    - Connects to: [[related concept 1]], [[related concept 2]]
    - Contradicts:
    - Enhances:
5. **Unlearning Log:**
    
    - Misconceptions corrected:
    - Outdated information replaced:
6. **Next Phase Learning Plan:** Create 3 specific tasks:
    
    - [ ] Research: [specific topic] 📅 [date]
    - [ ] Practice: [application] 📅 [date]
    - [ ] Reflect: [question to explore] 📅 [date]
7. **Growth Metric:** Rate understanding depth 1-10
    
    - Starting point: /10
    - Current level: /10

Tag with #learning/evolution/[topic]

```

**Example Usage:** Concept: "Exposure Triangle", receive a timeline showing progression from "knew the three elements" to "understanding reciprocal relationships" to "intuitive adjustment in field conditions"

---

#### **Metaphor Bridge Builder**

> **Synergy:** Copilot + Excalidraw + Custom Frames

**🎯 Goal:** Generate creative metaphors that connect technical concepts to familiar experiences, with visual representation suggestions.

**⚡ Trigger:** When struggling to understand or explain complex technical concepts.

**💡 Prompt:**

```

Create metaphorical bridges for this concept: {{selection}}

Develop:

1. **Primary Metaphor:**
    
    - Technical concept = Familiar experience
    - Why this metaphor works (3 parallel points)
    - Where the metaphor breaks down
2. **Supporting Analogies:** (3 variations)
    
    - Visual/Spatial: "It's like..."
    - Process/Action: "Similar to when you..."
    - Emotional/Experiential: "Feels like..."
3. **Visual Representation:** (for Excalidraw)
    
    - Left side: Technical concept components
    - Center: Bridge/connection visual
    - Right side: Metaphor components
    - Connection lines with labels
4. **Custom Frame Suggestion:**
    
    - Frame type: [YouTube/Website/Image]
    - URL for explanatory content
    - Caption connecting to metaphor
5. **Reverse Engineering:**
    
    - If [metaphor] then [technical implication]
    - Practical example using metaphor logic
6. **Memory Anchor:**
    
    - One memorable phrase combining both
    - Emoji representation: [emoji] = [concept]
7. **Common Misconceptions:**
    
    - What the metaphor might wrongly suggest
    - Clarifying disclaimer

Tag with #metaphor/[field] and #explanation/[concept]

```

**Example Usage:** Input "Aperture in photography", receive "Primary Metaphor: Aperture = Window blinds; wider opening = more light but less of the view in focus, just as opening blinds floods room with light but reduces privacy (selective visibility)"

---

## ✍️ Creation & Elaboration

#### **Writer's Block Breaker**

> **Synergy:** Copilot + Text Generator + Quick Add

**🎯 Goal:** Generate multiple creative approaches to continue or expand stuck writing projects.

**⚡ Trigger:** When facing writer's block or needing fresh perspectives on partially written content.

**💡 Prompt:**

```

Help me break through writer's block on this piece:

Current text: {{selection}}

Generate:

1. **Three Different Continuations:** (50 words each)
    
    - Analytical approach:
    - Narrative approach:
    - Contrarian approach:
2. **Missing Puzzle Pieces:**
    
    - What context is assumed but not explained?
    - What questions would a curious reader ask?
    - What counterarguments need addressing?
3. **Structural Alternatives:**
    
    - Start with the ending instead
    - Begin with a question
    - Open with a vivid scene or example
4. **Quick Add Templates:** (3 options)
    
    - Template A: [Structure outline]
    - Template B: [Different angle]
    - Template C: [Hybrid approach]
5. **Energy Injection Points:**
    
    - Add personal anecdote here: [location]
    - Insert surprising fact: [location]
    - Include contrasting perspective: [location]
6. **Completion Momentum:**
    
    - Next sentence starter: "What most people don't realize is..."
    - Transition phrase: "This connects to..."
    - Closing thought seed: "The real insight here..."
7. **15-Minute Sprint Prompt:** "For the next 15 minutes, explore what would happen if [provocative statement related to topic]"
    

Tag: #writing/draft/[stage]

```

**Example Usage:** Stuck on a photography philosophy essay, receive three continuations including "Analytical: The technical mastery Randall advocates serves not as an end but as a language through which artistic vision speaks..."

---

#### **Concept Deep Dive Generator**

> **Synergy:** Copilot + Homepage + Highlighter

**🎯 Goal:** Create comprehensive exploration pages for complex concepts with multiple entry points and learning paths.

**⚡ Trigger:** When establishing a new major learning focus or creating cornerstone content for your PKB.

**💡 Prompt:**

```

Create a comprehensive concept page for: [CONCEPT NAME]

Build this deep dive structure:

1. **Homepage Hub Section:**

    ```markdown
    ## 🎯 [Concept] Command Center
    > One-line definition
    Current Understanding: ⬜⬜⬜⬜⬜ (0/5)
    Last Updated: [[Date]]
    ```

2. **Learning Landscape:**
    
    - ==Core Principle 1== (yellow - fundamental)
    - ==[!Core Principle 2]== (red - challenging)
    - ==[_Core Principle 3_]== (green - mastered)
3. **Multi-Level Explanations:**
    
    - **5-year-old:** (1 sentence with simple analogy)
    - **Beginner:** (1 paragraph, no jargon)
    - **Intermediate:** (Technical but accessible)
    - **Advanced:** (Full complexity, proper terminology)
4. **Interactive Learning Path:**
    
    - [ ] Stage 1: Understand [basic aspect]
    - [ ] Stage 2: Apply [practical exercise]
    - [ ] Stage 3: Analyze [case study]
    - [ ] Stage 4: Create [original work]
    - [ ] Stage 5: Teach [to someone else]
5. **Resource Architecture:**
    
    - 📚 Essential Reading: [[source1]], [[source2]]
    - 🎥 Visual Learning: [Custom Frame suggestion]
    - 🔧 Practice Tools:
    - 💡 Related Concepts: [[link1]], [[link2]]
6. **Question Framework:**
    
    - What?: [definition questions]
    - Why?: [significance questions]
    - How?: [application questions]
    - What if?: [exploration questions]
7. **Personal Connection:**
    
    - Relevance to my interests:
    - Integration with current projects:
    - Next exploration direction:

Include navigation: [[← Previous Concept]] | [[Concept Index]] | [[Next Concept →]]

```

**Example Usage:** Concept: "Dynamic Range in Photography", receive a complete page structure with sections like "5-year-old: Like trying to see in bright sun and shadow at the same time - your eyes can do it better than a camera"

---

#### **Project Blueprint Architect**

> **Synergy:** Copilot + Tasks + Dataview + Periodic Notes

**🎯 Goal:** Generate comprehensive project blueprints with integrated task management and progress tracking.

**⚡ Trigger:** When initiating a new creative project or learning endeavor.

**💡 Prompt:**

```

Design a complete project blueprint for: [PROJECT NAME]

Context/Goals: {{selection}}

Create:

1. **Project Metadata:** (Dataview-compatible)

    ```yaml
    project_name: 
    start_date: 
    target_date: 
    status: planning
    priority: high/medium/low
    tags: #project/[type]
    ```

2. **Vision & Success Metrics:**
    
    - Core Purpose:
    - Success looks like:
    - Measurable outcomes (3):
    - Non-negotiable quality standards:
3. **Phased Execution Plan:** **Phase 1: Foundation** (Week 1-2)
    
    - [ ] Major milestone 📅 YYYY-MM-DD
    - [ ] Supporting task
    - [ ] Review checkpoint
    
    **Phase 2: Development** (Week 3-4) [Similar structure]
    
    **Phase 3: Refinement** (Week 5-6) [Similar structure]
    
4. **Daily Rituals:** (for Periodic Notes)
    
    - Morning: Check [[Project Dashboard]]
    - Working block: Focus on [current phase]
    - Evening: Log progress in [[Project Journal]]
5. **Resource Station:**
    
    - Tools needed:
    - Skills to develop:
    - People to consult:
    - References: [[resource notes]]
6. **Risk Mitigation:**
    
    - Potential blocker → Mitigation strategy
    - [List 3 major risks]
7. **Dataview Queries:**
    
    - Active tasks: `tasks from #project/[name] where !completed`
    - Progress notes: `list from #project/[name] sort file.mtime desc`
8. **Weekly Review Template:**
    
    - Completed this week:
    - Challenges faced:
    - Next week's focus:
    - Overall progress: ⬜⬜⬜⬜⬜

Link structure: [[Project Home]] → [[Current Phase]] → [[Task List]]

```

**Example Usage:** Project: "Cosmological Photography Series", receive blueprint with phases like "Phase 1: Research astronomical events and optimal shooting locations" with specific tasks and dates.

---

#### **Essay Architecture Builder**

> **Synergy:** Copilot + Linter + Callout Manager

**🎯 Goal:** Transform loose ideas into structured, compelling essay outlines with writing momentum builders.

**⚡ Trigger:** When you have gathered research and ideas but need structure for long-form writing.

**💡 Prompt:**

```

Transform these ideas into an essay architecture:

Raw material: {{selection}}

Build:

1. **Thesis Crystallization:**
    
    - Working thesis: [one clear sentence]
    - Supporting angle 1:
    - Supporting angle 2:
    - Supporting angle 3:
    - Counter-thesis to address:
2. **Opening Hook Options:** (choose one)

    > [!example] Anecdotal Opening [Personal story that illustrates the theme]

    > [!question] Question Opening [Provocative question that the essay answers]

    > [!quote] Quotation Opening [Relevant quote with unexpected interpretation]

3. **Section Architecture:**
    

## Section 1: [Establishing Context]

    
    - Key point:
    - Evidence/Example:
    - Transition thought:
    

## Section 2: [Building Argument]

    
    - Key point:
    - Evidence/Example:
    - Transition thought:
    

## Section 3: [Addressing Complexity]

    
    - Counterargument:
    - Response:
    - Nuance to acknowledge:
    

## Section 4: [Synthesis & Expansion]

    
    - Bringing threads together:
    - Broader implications:
4. **Voice & Style Notes:**
    
    - Tone: [analytical/conversational/provocative]
    - POV: [first/third person]
    - Recurring metaphor to weave through:
    - Power words to emphasize:
5. **Evidence Bank:**
    
    - Statistical support:
    - Anecdotal evidence:
    - Expert testimony:
    - Logical reasoning:
6. **Linter Checklist:**
    
    - [ ] Check thesis appears in intro and conclusion
    - [ ] Verify each paragraph has topic sentence
    - [ ] Confirm transitions between sections
    - [ ] Remove redundant phrases
    - [ ] Strengthen weak verbs
7. **Momentum Maintainers:**
    
    - If stuck on intro, start with: "Most people believe..."
    - If stuck on conclusion, begin: "What this really means is..."
    - Emergency pivot: "But here's what's actually interesting..."

Target length: [word count] Reading time: [minutes]

```

**Example Usage:** Ideas about "philosophy in photography", receive structure with thesis "Technical mastery without philosophical grounding produces hollow images that may impress but rarely move the viewer"

---

## 🔍 Review & Resurfacing

#### **Weekly Knowledge Harvest**

> **Synergy:** Copilot + Dataview + Periodic Notes + Tasks

**🎯 Goal:** Generate comprehensive weekly reviews that surface forgotten gems and identify knowledge gaps.

**⚡ Trigger:** Every week during your designated review time.

**💡 Prompt:**

```

Perform my weekly knowledge harvest for: [[Week of DATE]]

Execute this analysis:

1. **Note Activity Summary:** Run Dataview: `LIST FROM "" WHERE file.mtime >= date({{last-week}}) SORT file.mtime desc LIMIT 10`
    
    - Most edited note:
    - Most linked note:
    - Orphan notes created:
2. **Knowledge Gains:**
    
    - 3 key concepts learned:
    - Most surprising insight:
    - Practical application discovered:
3. **Task Progress Audit:**

    ```dataview
    TASK
    WHERE completed >= date({{last-week}})
    GROUP BY file.name
    ```

    - Completion rate: X/Y tasks
    - Overdue items to address:
    - Tasks to migrate forward:
4. **Connection Discovery:**
    
    - Unexpected link between: [[Note A]] ←→ [[Note B]]
    - Pattern noticed across notes:
    - Theme emerging from this week:
5. **Forgotten Treasures:** (notes not accessed in 30+ days) Search for notes with: #review/pending OR #idea/unexplored
    
    - Resurrect and apply: [[old note]]
    - Archive as irrelevant: [[outdated note]]
    - Schedule for deep dive: [[promising note]]
6. **Gap Analysis:**
    
    - Questions raised but not answered:
    - Topics mentioned but not explored:
    - Tools referenced but not learned:
7. **Next Week's Learning Focus:**
    
    - [ ] Primary focus: [topic]
    - [ ] Secondary exploration: [topic]
    - [ ] Skill to practice: [skill]
8. **Weekly Wisdom Nugget:** One sentence that captures this week's growth: "[Your synthesized insight here]"
    

Save to: [[Weekly Reviews/Week-{{date}}]] Tag: #review/weekly #knowledge/harvest

```

**Example Usage:** Run on Sunday evening, receive summary showing "Most surprising insight: The zone system in photography parallels stoic philosophy's approach to controlling only what's within our power"

---

#### **Spaced Repetition Architect**

> **Synergy:** Copilot + Tasks + Tag Wrangler + Periodic Notes

**🎯 Goal:** Create intelligent review cycles for important concepts using spaced repetition principles.

**⚡ Trigger:** When processing important information that needs long-term retention.

**💡 Prompt:**

```

Create a spaced repetition schedule for: [TOPIC]

Content to remember: {{selection}}

Generate:

1. **Core Memory Items:** (5-7 key points)
    
    - Fact 1: [statement] | Recall cue: [question]
    - Fact 2: [statement] | Recall cue: [question] [Continue for all items]
2. **Review Schedule:** (Tasks with dates)
    
    - [ ] Initial review #review/1day 📅 {{tomorrow}}
    - [ ] Second review #review/3day 📅 {{in-3-days}}
    - [ ] Third review #review/1week 📅 {{in-1-week}}
    - [ ] Fourth review #review/2week 📅 {{in-2-weeks}}
    - [ ] Fifth review #review/1month 📅 {{in-1-month}}
    - [ ] Final review #review/3month 📅 {{in-3-months}}
3. **Understanding Levels:** (for each review)
    
    - Day 1: Recognize and recall basics
    - Day 3: Explain in own words
    - Week 1: Apply to example
    - Week 2: Connect to other knowledge
    - Month 1: Teach to someone else
    - Month 3: Create something new with it
4. **Active Recall Prompts:**
    
    - Surface level: "What is [concept]?"
    - Deeper: "How does [concept] relate to [other concept]?"
    - Application: "How would you use [concept] to solve [problem]?"
    - Synthesis: "What would happen if [concept] didn't exist?"
5. **Memory Palace Anchors:**
    
    - Visual association:
    - Location in mental map:
    - Sensory trigger:
    - Emotional connection:
6. **Progressive Difficulty Questions:**
    
    - Beginner: [easy question]
    - Intermediate: [moderate question]
    - Advanced: [challenging question]
    - Master: [synthesis question]
7. **Review Note Template:**

    ```markdown
    ## 📝 Review: [Topic] - [Date]
    Understanding level: ⬜⬜⬜⬜⬜
    Recall success: X/Y items
    New connections found:
    Next review: [[date]]
    ```

8. **Forgetting Curve Intervention:** If recall fails, create:
    
    - [ ] Relearn with new metaphor
    - [ ] Create visual diagram
    - [ ] Write practice problems

Auto-tag: #memory/active #review/[stage]

```

**Example Usage:** Topic: "Exposure Triangle", receive memory items like "Fact: ISO affects sensor sensitivity | Recall cue: What happens to noise when ISO increases?"

---

#### **Monthly Mind Map Generator**

> **Synergy:** Copilot + Excalidraw + Dataview + Homepage

**🎯 Goal:** Generate a visual and textual map of your knowledge landscape evolution over the past month.

**⚡ Trigger:** Monthly review session to see the big picture of your learning journey.

**💡 Prompt:**

```

Generate my monthly mind map for: [MONTH YEAR]

Analyze all notes from this month and create:

1. **Central Theme Detection:** Based on note frequency and connections:
    
    - Primary focus area: [most explored topic]
    - Secondary interests: [2-3 supporting topics]
    - Surprise exploration: [unexpected topic]
2. **Knowledge Web Structure:** (for Excalidraw)

    ```
    CENTER: [Month] Learning Journey
    ├── Branch 1: [Main Topic]
    │   ├── Sub-topic 1.1: [[related note]]
    │   ├── Sub-topic 1.2: [[related note]]
    │   └── Key Insight: "..."
    ├── Branch 2: [Secondary Topic]
    │   ├── Sub-topic 2.1
    │   └── Application: ...
    └── Branch 3: [Emerging Interest]
        └── Future exploration: ...
    ```

3. **Quantitative Summary:**
    
    - Notes created: X
    - Notes modified: Y
    - Total connections made: Z
    - Most connected note: [[title]]
    - Orphan notes needing integration: #
4. **Learning Velocity Metrics:**
    
    - Week 1 focus: [topic] - Depth: ⬜⬜⬜⬜⬜
    - Week 2 focus: [topic] - Depth: ⬜⬜⬜⬜⬜
    - Week 3 focus: [topic] - Depth: ⬜⬜⬜⬜⬜
    - Week 4 focus: [topic] - Depth: ⬜⬜⬜⬜⬜
5. **Growth Edges:** (areas of expansion)
    
    - From [old understanding] → To [new understanding]
    - Skill developed: [skill] - Progress: X%
    - Habit formed: [practice]
6. **Insight Constellation:** (breakthrough moments) ⭐ Major insight: [[note]] - "One-line summary" ⭐ Connection made: [[note1]] + [[note2]] = [synthesis] ⭐ Problem solved: [challenge] → [solution]
    
7. **Homepage Dashboard Update:**

    ```markdown
    ## 📊 [Month] Highlights
    🎯 Main Achievement: 
    📚 Books/Resources Completed: 
    💡 Big Realization: 
    🔄 Habit Streak: X days of [practice]
    ```

8. **Dataview Query Collection:** Notes to revisit:

    ```dataview
    LIST FROM #review/pending OR #idea/seed
    WHERE file.ctime >= date({{month-start}})
    AND file.ctime <= date({{month-end}})
    ```

9. **Next Month's Trajectory:** Based on this month's patterns:
    
    - Natural next topic: [what logically follows]
    - Gap to fill: [missing knowledge]
    - Challenge to tackle: [stretch goal]

Save as: [[Monthly Reviews/[Month]-[Year]-Mind-Map]]

```

**Example Usage:** "October 2025" returns a mind map showing photography as central theme with branches for "Technical Skills", "Philosophical Framework", and "Cosmology Applications", with quantified progress on each branch.

---

#### **Knowledge Archaeology Dig**

> **Synergy:** Copilot + Dataview + Custom Frames + Highlighter

**🎯 Goal:** Excavate old notes to find buried insights and forgotten connections that are newly relevant.

**⚡ Trigger:** Quarterly or when feeling stuck, to rediscover past insights with fresh eyes.

**💡 Prompt:**

```

Conduct an archaeological dig through notes older than [TIME PERIOD]:

Search parameters: {{selection}} (topics/tags/keywords)

Excavate and analyze:

1. **Time Capsule Discovery:** Find 5 notes not opened in 60+ days:

    ```dataview
    LIST
    FROM #[relevant-tags]
    WHERE file.mtime <= date({{60-days-ago}})
    SORT file.mtime asc
    LIMIT 5
    ```

    For each, identify:

    
    - Original context:
    - New relevance:
    - Modern application:
2. **Evolution Analysis:**
    
    - Past belief: "I used to think..."
    - Present understanding: "Now I know..."
    - Connection revealed by time:
3. **Forgotten Gem Restoration:** Found insight: [[old note]]
    
    - ==Original value== (yellow highlight)
    - ==[!New application]== (red - urgent to implement)
    - ==[_Integration potential_]== (green - fits current work)
4. **Historical Pattern Recognition:** Recurring themes across time periods:
    
    - Pattern 1: Appeared in [dates] → Still relevant because:
    - Pattern 2: Evolved from [old form] → To [current form]
    - Pattern 3: Cycle detected: [description]
5. **Wisdom Archaeology Layers:**
    
    - Surface (recent): [last month's focus]
    - Shallow (months): [quarterly theme]
    - Deep (year+): [long-term interest]
    - Bedrock (oldest): [fundamental principle]
6. **Revival Candidates:** Projects/ideas worth resurrecting:
    
    - [ ] Revive: [old project] because [new relevance]
    - [ ] Merge: [old idea] + [current project]
    - [ ] Archive: [truly outdated]
7. **Custom Frame Time Machine:** Historical context needed:
    
    - Frame: [YouTube/Article from that time]
    - Why it mattered then:
    - Why it matters now:
8. **Synthesis Bridge:** Connect [old insight] + [current learning] = **New Understanding:** [emerged synthesis]
    
9. **Archaeological Report:**
    
    - Total notes explored: X
    - Valuable rediscoveries: Y
    - Connections made across time: Z
    - Priority revival: [[note to focus on]]
    - Key takeaway: "What seemed [old perspective] is actually [new perspective]"

Create revival plan:

- [ ] Week 1: Deep dive into [[rediscovered topic]]
- [ ] Week 2: Integrate with [[current project]]
- [ ] Week 3: Create synthesis note: [[old-meets-new]]

Tag: #archaeology/knowledge #review/historical

```

**Example Usage:** Search "composition philosophy" from 6+ months ago, discover early notes about rule of thirds that now connect meaningfully with Glenn Randall's philosophy of intentional seeing beyond rules.

---

## 🎭 Meta-Prompts Section

#### **Prompt Optimization Engine**

> **Synergy:** Copilot + Periodic Notes + Homepage

**🎯 Goal:** Refine and improve your existing Copilot prompts based on usage patterns and results.

**⚡ Trigger:** After using a prompt multiple times, to refine and optimize it for better results.

**💡 Prompt:**

```

Optimize this frequently-used prompt:

Original prompt: {{selection}}

Analyze and improve:

1. **Current Performance Audit:**
    
    - Success rate (subjective): /10
    - Common failure points:
    - Manual adjustments needed:
2. **Precision Enhancement:**
    
    - Vague terms to specify:
    - Missing context to add:
    - Redundant elements to remove:
3. **Variable Optimization:**
    
    - Current variables: {{list them}}
    - Better variable names:
    - Additional variables needed:
4. **Output Format Refinement:**
    
    - Current format issues:
    - Improved structure:
    - Consistent formatting rules:
5. **Version History:**
    
    - v1.0: [original]
    - v1.1: [what changed]
    - v2.0: [major revision]
6. **A/B Test Variants:**
    
    - Variant A: [focus on clarity]
    - Variant B: [focus on depth]
    - Test metric: [what to measure]
7. **Context Preloading:** Add these lines for better results:
    
    - Role definition: "Act as..."
    - Context setting: "Given that..."
    - Success criteria: "The ideal output..."
8. **Create Homepage Quick Access:**

    ```markdown
    ## ⚡ Quick Prompts
    - [[Optimized Prompt Name]] - v2.0
    Last updated: {{date}}
    Success rate: X/10
    ```

Save to: [[Prompt Library/Optimized/[Name]]]

```

**Example Usage:** Optimize a book notes prompt, receive enhanced version with clearer variables, better output structure, and specific role definition like "Act as a research librarian specializing in knowledge synthesis..."

---

## 📚 Prompt Library Maintenance

Remember to:
- **Test each prompt** with real content from your vault
- **Track success rates** in your Periodic Notes
- **Share variations** that work particularly well
- **Adapt prompts** to your evolving workflow
- **Combine prompts** for complex workflows
- **Version control** your most-used prompts
- **Create shortcuts** in Homepage for frequent prompts

---

*Last Updated: {{date}}*
*Total Prompts: 20*
*Plugin Integrations: Copilot + 10 plugins*

[[← Return to PKM Resources]] | [[Copilot Documentation]] | [[Plugin Synergy Guide →]]
```
