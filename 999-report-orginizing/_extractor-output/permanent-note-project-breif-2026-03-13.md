# Project: Permanent Notes for Personal Knowledge Management


# What I have so Far
1. **Reports**: Plenty of Reports generated through Claude Projects, which contain a wealth of information that can be transformed into Permanent Notes for a Personal Knowledge Base (PKB).
2. **Script**: Script that extracts key PKB information from reports generated through the Claude Project Generators and prints them in both Markdown and JSON formats.
3. **Report Selection**: A selection of Reports produced from the script in both Markdown and JSON formats.
4. **YAML Structure**: Complete YAML structure and How to Use it for LLMs to generate Permanent Notes from the extracted information in the reports.
5. **Obsidian Plugins**: Templater, Dataview, QuickAdd, and any other useful plugins for Obsidian to create and manage Permanent Notes effectively.

---

# Key Locations of Materials

- `D:\10_pur3v4d3r's-vault\99-scripts\pkb_extractor.py` - Script for extracting key PKB information from reports.
- `D:\10_pur3v4d3r's-vault\99-scripts\README-pkb-extractor.md` - README file for the PKB extractor script.
- `D:\10_pur3v4d3r's-vault\999-report-orginizing` - Folder containing the generated reports in both Markdown and JSON formats.
  - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output` - Subfolder containing the output from the PKB extractor script.
- `D:\10_pur3v4d3r's-vault\04-library` - Folder containing reports and reference material that needs extracting.
- `D:\10_pur3v4d3r's-vault\00-inbox\01-reports` - Folder containing the original reports that may need to be transformed into Permanent Notes.
- `D:\10_pur3v4d3r's-vault\00-inbox\02-topic-sets` - Folder containing topic sets that may be relevant for creating Permanent Notes.
- `D:\10_pur3v4d3r's-vault\metadata-template.md` - Template for the metadata of Permanent Notes in Obsidian.
- `D:\10_pur3v4d3r's-vault\03-notes\01_permanent-notes` - Folder where the Permanent Notes will be stored in Obsidian. And home to the original permanent notes that may need to be removed or heavily edited.

---

# Things Needed

- Prompt for Claude Project to generate Permanent Notes from the extracted information in the reports while using the YAML structure.
- Stucture of the various folders.
- Template for the metadata of Permanent Notes in Obsidian.
- Template of the structure of the Permanent Notes to be generated, including guidelines for formatting, linking, and organizing the notes within Obsidian.
- Taxonomy of appropriate tags and links to use in Obsidian for organizing and connecting the Permanent Notes effectively within the PKM system.
- System for ensuring that the Claude Project can keep track of previously reviewed reports and their associated Permanent Notes to facilitate connections between new and existing information.
- Guidelines for creating and maintaining Permanent Notes to ensure consistency and quality.

---

# For Prompt Engineering

I need you to review this information for a project to turn the **vast amount of resources** I have for my Personal Knowledge Management (PKM) system into *Permanent Notes [evergreen]* that can be easily accessed and utilized in **Obsidian**. I want to ensure that the process of extracting key information from the reports and transforming it into Permanent Notes is efficient and effective.

Im thinking of taking the reports *that the script prints*, uploading them to a Claude Project one at a time and have the Claude Project review the printed report [from-the-script] in full to gain understanding and context. Then, using the YAML structure I have created, I want to prompt the Claude Project to generate **MULTIPLE Permanent Notes as downloadable ARTIFACTS** based on the extracted information in the printed reports [from-the-script]. The generated Permanent Notes should be in a format that can be easily imported into Obsidian, and should follow the guidelines for creating and maintaining Permanent Notes to ensure consistency and quality.

Overall, I want to ensure that the process of turning the vast amount of resources I have for my Personal Knowledge Management system into Permanent Notes is streamlined and effective, allowing me to easily access and utilize the information in Obsidian for my personal and professional growth.

- NOTE: I want to make sure that the process of creating Permanent Notes is not just about extracting information, but also about synthesizing and connecting ideas in a way that adds value to my PKM system. The goal is to create Permanent Notes that are not just summaries of the reports, but also include insights, connections, and reflections that can help me better understand and utilize the information in my PKM system.
- NOTE: The prompt should instruct the Claude Project  how to go about both reviewing the appropriate information and how to structure the new permanent notes in a way that is consistent with the guidelines for creating and maintaining Permanent Notes [evergreen]. This may include instructions on how to format the notes, how to link them to other relevant notes in Obsidian, and how to ensure that they are easily searchable and accessible within the PKM system.
- NOTE: The prompt needs to have the Claude Project in question become a *PKB/PKM/Obsidian expert* in order to ensure that the generated Permanent Notes are of high quality and relevance to my PKM system. This may involve providing the Claude Project with background information on PKM principles, best practices for creating Permanent Notes, and examples of well-crafted Permanent Notes to serve as a reference for the generation process.
- NOTE: The prompt should also include instructions on how to review and edit the generated Permanent Notes to ensure that they meet the desired standards for quality and relevance. This may involve providing guidelines for reviewing the notes, such as checking for clarity, coherence, and accuracy, as well as ensuring that the notes are properly linked to other relevant notes in Obsidian.
- NOTE: The prompt should also include instructions on how to organize and manage the generated Permanent Notes within Obsidian, such as creating appropriate folders, tags, and links to ensure that the notes are easily accessible and can be effectively integrated into my PKM system.
- NOTE: The prompt should be designed to be flexible and adaptable, allowing for adjustments based on the specific content of the reports and the evolving needs of my PKM system. This may involve providing options for different types of Permanent Notes (e.g., summary notes, insight notes, connection notes) and allowing for customization in how the notes are structured and linked within Obsidian.
- NOTE: The should be a system in the prompt for ensuring the Claude Project know about other printed reports that it has already reviewed, so that it can make connections between the information in the current report and the information in previously reviewed reports. This may involve providing a way for the Claude Project to access a database or index of previously reviewed reports and their associated Permanent Notes, allowing it to identify relevant connections and insights based on the information in the current report. [wich-the-claude-project-could-store]

**IMPORTANT**:I need both the prompt and the Claude Project to produce Artifacts, so I can download the notes straight into my PKB.

**!IMPORTANT**: I need the Claude Project to be able to generate **MULTIPLE Markdown files** from each report [the-report-printed-by-the-python-extraction-script-which-is-complete], so I can easily import them into Obsidian as Permanent Notes. Each Markdown file should represent a distinct Permanent Note that captures a specific insight, connection, or piece of information from the report, and should be formatted in a way that is consistent with the guidelines for creating and maintaining Permanent Notes in my PKM system.

**!IMPORTANT**: I need the Claude Project to be able to generate MULTIPLE Permanent Notes from each report, and to ensure that each note is properly linked to other relevant notes in Obsidian to facilitate easy navigation and integration within my PKM system. This may involve providing instructions on how to identify key themes, insights, and connections within the report, and how to structure the generated Permanent Notes in a way that reflects these themes and connections effectively.

**!IMPORTANT**: I need the Claude Project to NAME THE generated Permanent Notes this way:
These are the notes that the generated reports link to wqhile reviewing/reading an actual report, so THEY MUST be semantic in their naming convention, and they must be named in a way that reflects the content and theme of the note. This may involve using a consistent naming convention that includes relevant keywords, themes, or topics from the report, as well as ensuring that the names are clear, concise, and easily understandable within the context of my PKM system.

- Coresponding Wiki-link
`[[Cognitive-Load-Theory|Cognitive Load Theory]]`

- Name of Permanent Note
`Cognitive Load Theory` or `cognitive load theory`

**!IMPORTANT**: They have to be named this way in order for future reports/previously generated reports that use that wiki-link show up as populated. This is crucial for the process of creating Permanent Notes that are interconnected and easily navigable within Obsidian, as it allows for the automatic linking of related notes based on their names and wiki-links. By following a consistent naming convention that aligns with the wiki-links used in the reports, I can ensure that the generated Permanent Notes are properly linked and integrated within my PKM system, facilitating easy access to relevant information and insights across different notes.

---





📁 _extractor-output
⏱️  Generated in 9 ms
──────────────────────────────────────────────────
├── 🗒️ ...in-pkm-report-topics_extracted.json (45.2 KB)
├── 📝 ...in-pkm-report-topics_report.md (28.2 KB)
├── 🗒️ abductive-reasoning-foundational-report-2026-03-06_extracted.json (126.8 KB)
├── 📝 abductive-reasoning-foundational-report-2026-03-06_report.md (52.5 KB)
├── 🗒️ achievement-goal-theory-foundational-report-2026-03-10_extracted.json (154.8 KB)
├── 📝 achievement-goal-theory-foundational-report-2026-03-10_report.md (61.9 KB)
├── 🗒️ advance-organizers-prior-knowledge-foundational-report-2026-03-11_extracted.json (165.7 KB)
├── 📝 advance-organizers-prior-knowledge-foundational-report-2026-03-11_report.md (66.9 KB)
├── 🗒️ claudes-extended-thinking_extracted.json (126.8 KB)
├── 📝 claudes-extended-thinking_report.md (44.0 KB)
├── 🗒️ cog-psy-attentional-efficiency-and-skill-aquisition_extracted.json (161.2 KB)
├── 📝 cog-psy-attentional-efficiency-and-skill-aquisition_report.md (63.8 KB)
├── 🗒️ cog-psy-critical-thinking-metacognitive-regulation_extracted.json (284.1 KB)
├── 📝 cog-psy-critical-thinking-metacognitive-regulation_report.md (113.8 KB)
├── 🗒️ cog-psy-epistemic-vigilance-and-epistemic-humility_extracted.json (58.2 KB)
├── 📝 cog-psy-epistemic-vigilance-and-epistemic-humility_report.md (10.7 KB)
├── 🗒️ cog-psy-foundational-critical-thinking_extracted.json (276.3 KB)
├── 📝 cog-psy-foundational-critical-thinking_report.md (79.6 KB)
├── 🗒️ cog-psy-historical-and-intellectual-origins-of-stoicism-20251201002626_extracted.json (169.3 KB)
├── 📝 cog-psy-historical-and-intellectual-origins-of-stoicism-20251201002626_report.md (44.2 KB)
├── 🗒️ cog-psy-john-dewey_extracted.json (254.4 KB)
├── 📝 cog-psy-john-dewey_report.md (58.7 KB)
├── 🗒️ cog-psy-john-dewey-how-we-think-review_extracted.json (174.3 KB)
├── 📝 cog-psy-john-dewey-how-we-think-review_report.md (44.8 KB)
├── 🗒️ cog-psy-role-of-stoic-journaling-practices-in-metacognitive-monitoring-20251128214625_extracted.json (234.0 KB)
├── 📝 cog-psy-role-of-stoic-journaling-practices-in-metacognitive-monitoring-20251128214625_report.md (49.6 KB)
├── 🗒️ cog-psy-william-james_extracted.json (347.6 KB)
├── 📝 cog-psy-william-james_report.md (58.4 KB)
├── 🗒️ cog-psy-william-james-principles-of-psychology-primer_extracted.json (113.5 KB)
├── 📝 cog-psy-william-james-principles-of-psychology-primer_report.md (23.3 KB)
├── 🗒️ cog-sci-pkm-cognitive-science-principles-for-habit-formation-in-pkm_extracted.json (246.5 KB)
├── 📝 cog-sci-pkm-cognitive-science-principles-for-habit-formation-in-pkm_report.md (52.3 KB)
├── 🗒️ cog-sci-pkm-first-priciples-and-socratic-metacognition-and-its-role-in-pkm_extracted.json (464.9 KB)
├── 📝 cog-sci-pkm-first-priciples-and-socratic-metacognition-and-its-role-in-pkm_report.md (153.6 KB)
├── 🗒️ cog-sci-pkm-key-components-of-socratic-questioning-and-how-they-apply-to-pkm-practices_extracted.json (202.7 KB)
├── 📝 cog-sci-pkm-key-components-of-socratic-questioning-and-how-they-apply-to-pkm-practices_report.md (47.0 KB)
├── 🗒️ cog-sci-pkm-metacognition-and-its-role-in-pkm_extracted.json (170.8 KB)
├── 📝 cog-sci-pkm-metacognition-and-its-role-in-pkm_report.md (65.8 KB)
├── 🗒️ cog-sci-pkm-reading-fluency-and-comprehension-in-pkm_extracted.json (135.3 KB)
├── 📝 cog-sci-pkm-reading-fluency-and-comprehension-in-pkm_report.md (36.9 KB)
├── 🗒️ cog-sci-pkm-reading-techniques-and-strategies-for-pkm_extracted.json (233.3 KB)
├── 📝 cog-sci-pkm-reading-techniques-and-strategies-for-pkm_report.md (52.9 KB)
├── 🗒️ cog-sci-pkm-the-role-of-reading-in-pkm_extracted.json (196.9 KB)
├── 📝 cog-sci-pkm-the-role-of-reading-in-pkm_report.md (50.4 KB)
├── 🗒️ cog-sci-pkm-theoretical-foundations-of-socratic-questioning-and-their-relevance-to-pkm_extracted.json (161.2 KB)
├── 📝 cog-sci-pkm-theoretical-foundations-of-socratic-questioning-and-their-relevance-to-pkm_report.md (48.3 KB)
├── 🗒️ cog-sci-pkm-understanding-socratic-questioning-and-its-role-in-pkm_extracted.json (212.0 KB)
├── 📝 cog-sci-pkm-understanding-socratic-questioning-and-its-role-in-pkm_report.md (55.1 KB)
├── 🗒️ cognitive-load-theory-focused-analysis-2026-03-06_extracted.json (181.6 KB)
├── 📝 cognitive-load-theory-focused-analysis-2026-03-06_report.md (79.6 KB)
├── 🗒️ cognitive-load-theory-foundational-report-2026-03-11_extracted.json (166.3 KB)
├── 📝 cognitive-load-theory-foundational-report-2026-03-11_report.md (62.6 KB)
├── 🗒️ critical-thinking-educational-settings-foundational-report-2026-03-05_extracted.json (97.9 KB)
├── 📝 critical-thinking-educational-settings-foundational-report-2026-03-05_report.md (47.2 KB)
├── 🗒️ deductive-reasoning-learning-foundational-report-2026-03-10_extracted.json (152.3 KB)
├── 📝 deductive-reasoning-learning-foundational-report-2026-03-10_report.md (57.6 KB)
├── 🗒️ extended-mind-theory-foundational-report-2026-03-11_extracted.json (116.1 KB)
├── 📝 extended-mind-theory-foundational-report-2026-03-11_report.md (51.4 KB)
├── 🗒️ fallibilism-foundational-report-2026-03-06_extracted.json (129.1 KB)
├── 📝 fallibilism-foundational-report-2026-03-06_report.md (51.8 KB)
├── 🗒️ feedback-design-autonomy-mastery-foundational-report-2026-03-10_extracted.json (136.2 KB)
├── 📝 feedback-design-autonomy-mastery-foundational-report-2026-03-10_report.md (57.3 KB)
├── 🗒️ growth-mindset-first-principles-report-2026-03-11_extracted.json (122.4 KB)
├── 📝 growth-mindset-first-principles-report-2026-03-11_report.md (66.9 KB)
├── 🗒️ growth-mindset-learning-foundational-report-2026-03-05_extracted.json (125.3 KB)
├── 📝 growth-mindset-learning-foundational-report-2026-03-05_report.md (46.3 KB)
├── 🗒️ inductive-reasoning-foundational-report-2026-03-06_extracted.json (109.4 KB)
├── 📝 inductive-reasoning-foundational-report-2026-03-06_report.md (44.3 KB)
├── 🗒️ letters-from-a-stoic-seneca_extracted.json (21.2 KB)
├── 📝 letters-from-a-stoic-seneca_report.md (2.0 KB)
├── 🗒️ llm-eng-automating-report-generation-with-claude-code_extracted.json (98.0 KB)
├── 📝 llm-eng-automating-report-generation-with-claude-code_report.md (35.5 KB)
├── 🗒️ llm-eng-building-pkm-system-with-claude-code_extracted.json (139.4 KB)
├── 📝 llm-eng-building-pkm-system-with-claude-code_report.md (41.7 KB)
├── 🗒️ memory-systems-working-memory-long-term-memory-foundational-report-2026-03-11_extracted.json (176.5 KB)
├── 📝 memory-systems-working-memory-long-term-memory-foundational-report-2026-03-11_report.md (75.4 KB)
├── 🗒️ mental-models-johnson-laird-first-principles-report-2026-03-11_extracted.json (91.3 KB)
├── 📝 mental-models-johnson-laird-first-principles-report-2026-03-11_report.md (57.2 KB)
├── 🗒️ mental-models-johnson-laird-foundational-report-2026-03-11_extracted.json (170.7 KB)
├── 📝 mental-models-johnson-laird-foundational-report-2026-03-11_report.md (61.2 KB)
├── 🗒️ metacognition-and-critical-thinking-foundational-report-2026-03-05_extracted.json (124.5 KB)
├── 📝 metacognition-and-critical-thinking-foundational-report-2026-03-05_report.md (49.6 KB)
├── 🗒️ metacognition-lifelong-learning-foundational-report-2026-03-05_extracted.json (141.0 KB)
├── 📝 metacognition-lifelong-learning-foundational-report-2026-03-05_report.md (50.1 KB)
├── 🗒️ metacognition-motivation-foundational-report-2026-03-05_extracted.json (111.3 KB)
├── 📝 metacognition-motivation-foundational-report-2026-03-05_report.md (51.4 KB)
├── 🗒️ multi-agent-systems-with-claude-code_extracted.json (310.1 KB)
├── 📝 multi-agent-systems-with-claude-code_report.md (194.8 KB)
├── 🗒️ political-reasoning-decision-making-foundational-report-2026-03-06_extracted.json (131.0 KB)
├── 📝 political-reasoning-decision-making-foundational-report-2026-03-06_report.md (50.4 KB)
├── 🗒️ reference-comprehensive-stoicism-journal-20251130195735_extracted.json (427.9 KB)
├── 📝 reference-comprehensive-stoicism-journal-20251130195735_report.md (78.1 KB)
├── 🗒️ reference-comprehensive-stoicism-quotes-and-precepts-2025120220_extracted.json (161.5 KB)
├── 📝 reference-comprehensive-stoicism-quotes-and-precepts-2025120220_report.md (58.1 KB)
├── 🗒️ reference-taxonomy-stoic-termonology-2025120303_extracted.json (450.4 KB)
├── 📝 reference-taxonomy-stoic-termonology-2025120303_report.md (150.1 KB)
├── 🗒️ report-claudes-extended-thinking-acrchitecture_extracted.json (129.4 KB)
├── 📝 report-claudes-extended-thinking-acrchitecture_report.md (43.7 KB)
├── 🗒️ report-generation-topic-inventory-by-style-2026-03-11_extracted.json (219.3 KB)
├── 📝 report-generation-topic-inventory-by-style-2026-03-11_report.md (154.2 KB)
├── 🗒️ schema-theory-and-learning-foundational-report-2026-03-06_extracted.json (141.5 KB)
├── 📝 schema-theory-and-learning-foundational-report-2026-03-06_report.md (51.6 KB)
├── 🗒️ sdt-focused-analysis-2026-03-06_extracted.json (128.5 KB)
├── 📝 sdt-focused-analysis-2026-03-06_report.md (76.1 KB)
├── 🗒️ self-determination-theory-first-principles-report-2026-03-11_extracted.json (116.9 KB)
├── 📝 self-determination-theory-first-principles-report-2026-03-11_report.md (67.2 KB)
├── 🗒️ self-determination-theory-foundational-report-2026-03-11_extracted.json (206.6 KB)
├── 📝 self-determination-theory-foundational-report-2026-03-11_report.md (73.5 KB)
├── 🗒️ self-directed-learning-foundational-report-2026-03-11_extracted.json (137.3 KB)
├── 📝 self-directed-learning-foundational-report-2026-03-11_report.md (57.9 KB)
├── 🗒️ self-regulated-learning_extracted.json (739.8 KB)
├── 📝 self-regulated-learning_report.md (190.3 KB)
├── 🗒️ self-regulated-learning-focused-analysis-2026-03-06_extracted.json (140.2 KB)
├── 📝 self-regulated-learning-focused-analysis-2026-03-06_report.md (69.2 KB)
├── 🗒️ stoicism-report-01-introduction-to-stoicism_extracted.json (113.9 KB)
├── 📝 stoicism-report-01-introduction-to-stoicism_report.md (36.9 KB)
├── 🗒️ stoicism-report-02-core-principles_extracted.json (95.6 KB)
├── 📝 stoicism-report-02-core-principles_report.md (35.5 KB)
├── 🗒️ stoicism-report-03-practice-daily-exercises_extracted.json (134.6 KB)
├── 📝 stoicism-report-03-practice-daily-exercises_report.md (54.6 KB)
├── 🗒️ stoicism-report-04-modern-psychology-parallels-and-insights_extracted.json (98.0 KB)
├── 📝 stoicism-report-04-modern-psychology-parallels-and-insights_report.md (42.1 KB)
├── 🗒️ stoicism-report-05-leadership-decision-making_extracted.json (126.1 KB)
├── 📝 stoicism-report-05-leadership-decision-making_report.md (48.9 KB)
├── 🗒️ stoicism-report-06-emotional-resilience_extracted.json (111.5 KB)
├── 📝 stoicism-report-06-emotional-resilience_report.md (46.9 KB)
├── 🗒️ stoicism-report-07-relationships_extracted.json (121.8 KB)
├── 📝 stoicism-report-07-relationships_report.md (46.9 KB)
├── 🗒️ stoicism-report-08-minimalism_extracted.json (123.2 KB)
├── 📝 stoicism-report-08-minimalism_report.md (56.1 KB)
├── 🗒️ stoicism-report-09-mindfulness_extracted.json (106.7 KB)
├── 📝 stoicism-report-09-mindfulness_report.md (41.5 KB)
├── 🗒️ stoicism-report-10-cbt-integration_extracted.json (115.1 KB)
├── 📝 stoicism-report-10-cbt-integration_report.md (44.1 KB)
├── 🗒️ stoicism-report-series-master_extracted.json (1.9 MB)
├── 📝 stoicism-report-series-master_report.md (600.6 KB)
├── 🗒️ stoicism-scartchpad_extracted.json (168.2 KB)
├── 📝 stoicism-scartchpad_report.md (47.2 KB)
├── 🗒️ stoicism-series-claude-project-prompt-v1.0.0_extracted.json (209.7 KB)
├── 📝 stoicism-series-claude-project-prompt-v1.0.0_report.md (47.6 KB)
├── 🗒️ the-golden-sayings-of-epictetus-(annotated)-20251128012340_extracted.json (131.2 KB)
├── 📝 the-golden-sayings-of-epictetus-(annotated)-20251128012340_report.md (43.4 KB)
├── 🗒️ topics-prompt_extracted.json (774.6 KB)
├── 📝 topics-prompt_report.md (148.1 KB)
├── 🗒️ types-of-reasoning-foundational-report-2026-03-05_extracted.json (120.0 KB)
├── 📝 types-of-reasoning-foundational-report-2026-03-05_report.md (48.4 KB)
├── 🗒️ what-does-it-mean-to-truley-understand-something-2026-03-10_extracted.json (86.4 KB)
└── 📝 what-does-it-mean-to-truley-understand-something-2026-03-10_report.md (45.9 KB)








✅

# Extracting Key Information [2026-03-13]


## Material Locations [Input]
- Inbox
  - `D:\10_pur3v4d3r's-vault\00-inbox\01-reports`✅
    - `D:\10_pur3v4d3r's-vault\00-inbox\01-reports\01-cognitive-science`✅
    - `D:\10_pur3v4d3r's-vault\00-inbox\01-reports\02_pkb-and-pkm`✅
    - `D:\10_pur3v4d3r's-vault\00-inbox\01-reports\03_prompt-engineering`✅
    - `D:\10_pur3v4d3r's-vault\00-inbox\01-reports\04-cosmology`✅
    - `D:\10_pur3v4d3r's-vault\00-inbox\02-topic-sets`✅
- Library
  - `D:\10_pur3v4d3r's-vault\04-library\01-cognitive-science`✅
    - `D:\10_pur3v4d3r's-vault\04-library\01-cognitive-science\-reference`✅
    - `D:\10_pur3v4d3r's-vault\04-library\01-cognitive-science\-reports`✅
  - `D:\10_pur3v4d3r's-vault\04-library\02-pkb-and-pkm-learning`
    -  `D:\10_pur3v4d3r's-vault\04-library\02-pkb-and-pkm-learning\-reference`✅
    -  `D:\10_pur3v4d3r's-vault\04-library\02-pkb-and-pkm-learning\-reports`✅
 -  `D:\10_pur3v4d3r's-vault\04-library\03-prompt-engineering`✅
    -  `D:\10_pur3v4d3r's-vault\04-library\03-prompt-engineering\-reference`✅
    -  `D:\10_pur3v4d3r's-vault\04-library\03-prompt-engineering\-reports`✅
 -  `D:\10_pur3v4d3r's-vault\04-library\04-cosmology`✅
    - ` D:\10_pur3v4d3r's-vault\04-library\04-cosmology\-reference`✅
    - `D:\10_pur3v4d3r's-vault\04-library\04-cosmology\-reports`✅


## Material Locations [Output]

- `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output`✅
  - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports`✅
    - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\cognitive-science`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\cosmology`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\pkb-and-pkm`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\prompt-engineering`✅
    - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\topics`✅
  - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library`✅
    - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cognitive-science`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cognitive-science\reference`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cognitive-science\reports`✅
    - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cosmology`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cosmology\reference`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cosmology\reports`✅
    - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\pkb-and-pkm`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\pkb-and-pkm\reference`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\pkb-and-pkm\reports`✅
    - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\prompt-engineering`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\prompt-engineering\reference`✅
      - `D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\prompt-engineering\reports`✅





### Commands for Extraction


```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\00-inbox\01-reports\01-cognitive-science" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\cognitive-science"
```

---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\00-inbox\01-reports\02_pkb-and-pkm" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\pkb-and-pkm"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\00-inbox\01-reports\03_prompt-engineering" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\prompt-engineering"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\00-inbox\01-reports\04-cosmology" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\reports\cosmology"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\00-inbox\02-topic-sets" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-inbox-reports\topics"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\01-cognitive-science\-reference" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cognitive-science\reference"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\01-cognitive-science\-reports" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cognitive-science\reports"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\02-pkb-and-pkm-learning\-reference" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\pkb-and-pkm\reference"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\02-pkb-and-pkm-learning\-reports" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\pkb-and-pkm\reports"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\03-prompt-engineering\-reference" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\prompt-engineering\reference"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\03-prompt-engineering\-reports" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\prompt-engineering\reports"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\04-cosmology\-reference" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cosmology\reference"
```
---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\04-library\04-cosmology\-reports" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_extractor-output\2026-03-13-library\cosmology\reports"
```

---

```python
# Process an entire folder of reports:
python pkb_extractor.py --input "D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0" --output "D:\10_pur3v4d3r's-vault\999-report-orginizing\_pkm-and-pkb-framework-1.0.0\extraction-material"
```


---

---









# PKB Metadata Template
This final section is a YAML Metadata template that should be included at the beginning of each report.
- Ensuring consistent documentation and classification across my PKB.

```yaml
---
# DOCUMENT IDENTIFICATION

doc_id: {{Unique identifier for this document, e.g., "Foundational_Report_001"}}
doc_type: Foundational Report
doc_created: {{Creation date, e.g., "2024-06-01"}}
doc_modified: {{Last modified date, e.g., "2024-06-01"}}
author: {{Author's name, e.g., "ChatGPT"}}

# CLASSIFICATION & DISCOVERY
primary_domain: {{Primary domain of knowledge, e.g., "Cognitive Science"}}
secondary_domains: {{List of secondary domains, e.g., ["Philosophy", "Neuroscience"]}}
related_concepts: {{List of related concepts, e.g., ["[[Concept A]]", "[[Theory B]]"]}}
knowledge_level: {{Level of depth, e.g., "Encyclopedic overview", "In-depth technical analysis", "Historical context"}}
tags: {{List of relevant tags, e.g., ["#cognition", "#philosophy", "#neuroscience"]}}

# QUALITY & STATUS
status: {{Current status of the document, e.g., "evergreen", "draft", "needs review"}}
maturity: {{Maturity level, e.g., "highly developed", "in progress", "conceptual"}}
confidence: {{Confidence level in the content, e.g., "high", "medium", "low"}}

# REASONING ARCHITECTURE
reasoning_tier: {{Tier of reasoning, e.g., "Tier 1: Foundational Understanding", "Tier 2: Analytical Depth", "Tier 3: Synthesis & Innovation"}}
reasoning_methods: {{List of reasoning methods used, e.g., ["Deductive reasoning", "Inductive reasoning", "Analogical reasoning"]}}
reasoning_technique: {{Specific techniques employed, e.g., "Socratic questioning", "Thought experiments", "Comparative analysis"}}

# EPISTEMIC & VALIDATION
epistemic_status: {{Epistemic status, e.g., "well-established", "emerging theory", "speculative"}}
validation_methods: {{Methods used for validation, e.g., "Peer review", "Empirical evidence", "Logical consistency"}}
test_coverage: {{Scope of testing, e.g., "Comprehensive", "Limited", "Theoretical"}}
validation_results: {{Summary of validation results, e.g., "Consistent with existing literature", "Requires further empirical testing", "Contradicted by recent studies"}}
validation_date: {{Date of last validation, e.g., "2024-06-01"}}
factual_verification: {{Status of factual verification, e.g., "Verified", "Partially verified", "Not verified"}}
hallucination_check: {{Status of hallucination check, e.g., "True", "False"}}

# SOURCE & ATTRIBUTION
source: {{Primary source of information, e.g., "Academic journals", "Books", "Expert interviews", "claude-sonnet-4.5"}}
based_on_prompts: {{List of prompts used to generate the content, e.g., ["Prompt 1: Define the core principles of cognitive science", "Prompt 2: Explain the historical development of cognitive science"]}}

# KNOWLEDGE GRAPH INTEGRATION
related_concepts:
  - "[[Concept A]]"
  - "[[Theory B]]"

prerequisites:
  - "[[Prerequisite Concept 1]]"
  - "[[Prerequisite Concept 2]]"

builds_on:
  - "[[Theory X]]"
  - "[[Concept Y]]"

extends:
  - "[[Concept Z]]"
  - "[[Theory W]]"

# ALIASES & LINKING
aliases:
  - "[[Alias 1]]"
  - "[[Alias 2]]"

link_up: "[[Higher-Level Concept]]"
link_down: "[[Lower-Level Concept]]"
link_related:
  - "[[Related Concept 1]]"
  - "[[Related Concept 2]]"

# ADDITIONAL METADATA
summary: {{A brief summary of the document, e.g., "This report provides an in-depth analysis of the core principles of cognitive science, exploring its historical development, key theories, and implications for understanding human cognition."}}
keywords: {{List of keywords, e.g., ["cognition", "neuroscience", "philosophy", "cognitive science"]}}

---
```

# Complete Metadata Template Explanation

This is How the Yaml at the front Must look in order to be consistent with the rest of the PKB and to ensure that it is properly integrated into the knowledge graph. Each field should be filled out with accurate and relevant information to facilitate discovery, classification, and connection within the PKB.

---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Critical Thinking Skills and Metacognitive Self-Regulation"
aliases:
  - Critical Thinking Deployment
  - Metacognitive Self-Regulation in Reasoning
  - Applied Critical Thinking Framework
  - PENCRISAL-MAI Integration
  - CT-MSR Framework
  - Situational Critical Thinking
  - Metacognitive Control of Reasoning
  - Critical Thinking Architecture
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  # Content Type
  - permanent-note
  - academic-synthesis
  - reference-note
  - practical-framework
  
  # Domain (hierarchical)
  - cognitive-psychology/metacognition
  - cognitive-psychology/critical-thinking
  - educational-psychology/learning-strategies
  - cognitive-psychology/self-regulation
  
  # Methodology
  - empirical-research
  - assessment-frameworks
  - systematic-protocols
  - practical-application
  - evidence-based
  
  # Specific Frameworks
  - pencrisal-framework
  - mai-framework
  - epistemic-vigilance
  
  # Core Competencies
  - reasoning-skills
  - error-detection
  - transfer-learning
  - calibration-training
  - deployment-strategies
  
  # Status
  - evergreen
  - comprehensive
  - research-grounded

domain: cognitive-psychology
subdomains:
  - metacognition
  - critical-thinking
  - educational-psychology
  - self-regulated-learning

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-02-01
updated: 2026-02-01

# ═══════════════════════════════════════════════════════════════════════════
# ACADEMIC METADATA
# ═══════════════════════════════════════════════════════════════════════════
source-type: academic-synthesis
research-base: empirical-studies
evidence-quality: high
peer-validation: multiple-frameworks

key-frameworks:
  - name: PENCRISAL
    description: "Five-dimensional critical thinking assessment (Deductive Reasoning, Inductive Reasoning, Practical Reasoning, Decision-Making, Problem-Solving)"
    developers: "Rivas & Saiz (2012)"
    validation: "psychometric-validated"
  
  - name: MAI
    description: "Metacognitive Awareness Inventory - 8 subdimensions across Knowledge and Regulation of Cognition"
    developers: "Schraw & Dennison (1994)"
    validation: "widely-validated"
  
  - name: EEVF
    description: "Extended Epistemic Vigilance Framework - 3-dimensional evaluation (Source, Claim, Receiver)"
    developers: "Sperber et al. (2010), Bielik & Krüger (2024)"
    validation: "empirically-supported"
  
  - name: Halpern Transfer Model
    description: "Four-component framework for critical thinking transfer across domains"
    developers: "Halpern (1998)"
    validation: "empirically-validated"

key-researchers:
  - Diane Halpern
  - Gregory Schraw
  - Carlos Saiz
  - Dan Sperber
  - Hugo Mercier
  - Raymond Dennison

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
word-count: 6200
complexity-level: advanced-practitioner
target-audience: "Intermediate to Advanced learners in cognitive psychology, educators, professionals seeking systematic reasoning improvement"
depth-level: comprehensive
treatment-type: practical-deployment-focused

practical-components:
  - operational-templates
  - decision-protocols
  - calibration-exercises
  - debugging-workflows
  - self-assessment-tools
  - monitoring-checklists

# ═══════════════════════════════════════════════════════════════════════════
# CORE CONCEPTS
# ═══════════════════════════════════════════════════════════════════════════
core-concepts:
  - Metacognitive Self-Regulation as Cognitive Control System
  - PENCRISAL Five-Dimensional Framework
  - Transfer Problem and Domain-Specificity
  - Recognition Patterns for Deployment Triggers
  - Knowledge of Cognition (Declarative, Procedural, Conditional)
  - Regulation of Cognition (Planning, Monitoring, Evaluation, Information Management, Debugging)
  - Epistemic Vigilance Three-Dimensional Model
  - Confidence Calibration Training
  - Structural Encoding for Transfer
  - Systematic Error Debugging Protocols

key-distinctions:
  - "Domain-General vs Domain-Specific Critical Thinking"
  - "Monitoring vs Control in Metacognition"
  - "Knowledge of Cognition vs Regulation of Cognition"
  - "Immersion vs Infusion Instructional Approaches"
  - "System 1 vs System 2 Deployment Triggers"
  - "Overconfidence vs Underconfidence Calibration Errors"

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[Introduction-to-Critical-Thinking|Introduction to Critical Thinking]]"
  - "[[Metacognition Fundamentals]]"
  - "[[Basic Argument Analysis]]"
  - "[[Logical Reasoning Foundations]]"

related:
  - "[[Metacognition]]"
  - "[[PENCRISAL Assessment Framework]]"
  - "[[Metacognitive Awareness Inventory]]"
  - "[[Epistemic-Vigilance|Epistemic Vigilance]]"
  - "[[Dual-Process-Theory|Dual Process Theory]]"
  - "[[Cognitive-Load-Theory|Cognitive Load Theory]]"
  - "[[Argument-Analysis|Argument Analysis]]"
  - "[[Decision Making Under Uncertainty]]"
  - "[[Cognitive Biases and Debiasing]]"
  - "[[Scientific-Reasoning|Scientific Reasoning]]"
  - "[[Transfer-of-Learning|Transfer of Learning]]"
  - "[[999-report-orginizing/_permanent-notes/_permanent-notes/Self-Regulated-Learning|Self-Regulated Learning]]"
  - "[[Confirmation-Bias-Myside-Bias|Confirmation Bias]]"
  - "[[Availability-Heuristic|Availability Heuristic]]"
  - "[[Anchoring Bias]]"

broader:
  - "[[cognitive-psychology|Cognitive Psychology]]"
  - "[[Educational-Psychology|Educational Psychology]]"
  - "[[Applied Epistemology]]"
  - "[[Rationality Studies]]"

narrower:
  - "[[Deductive Reasoning Techniques]]"
  - "[[Inductive Reasoning Strategies]]"
  - "[[Practical Reasoning in Real-World Contexts]]"
  - "[[Metacognitive Monitoring Protocols]]"
  - "[[Calibration Training Methods]]"
  - "[[Debugging Strategies for Reasoning Errors]]"
  - "[[Structural Encoding Techniques]]"

see-also:
  - "[[Working Memory and Executive Function]]"
  - "[[Expertise Development]]"
  - "[[Reflective Judgment Model]]"
  - "[[Intellectual-Humility|Intellectual Humility]]"
  - "[[Bayesian Reasoning]]"
  - "[[Argument-Mapping|Argument Mapping]]"
  - "[[Socratic-Questioning|Socratic Questioning]]"
  - "[[Pre-Mortem Analysis]]"
  - "[[Red Team Thinking]]"
  - "[[Cognitive Forcing Functions]]"

contrasts-with:
  - "[[Heuristic-Based Decision Making]]"
  - "[[Intuitive Judgment]]"
  - "[[Unconscious Competence]]"

applied-in:
  - "[[Professional Decision Making]]"
  - "[[Academic Research]]"
  - "[[Strategic-Planning|Strategic Planning]]"
  - "[[Problem Solving in Complex Domains]]"
  - "[[Evidence-Based Practice]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[Foundational-Logic|Foundational Logic]]"
  - "[[Cognitive-Development-Theory|Cognitive Development Theory]]"
  - "[[Information-Processing-Models|Information Processing Models]]"

enables:
  - "[[Advanced Reasoning Techniques]]"
  - "[[Domain-Specific Critical Thinking]]"
  - "[[Debiasing-Interventions|Debiasing Interventions]]"
  - "[[Metacognitive Instruction Design]]"
  - "[[Epistemic Virtue Development]]"

expansion-topics:
  - topic: "[[Domain-Specific Critical Thinking Standards]]"
    description: "Field-specific criteria and recognition patterns for professional contexts"
    priority: high
  
  - topic: "[[Metacognitive Intervention Design]]"
    description: "Systematic protocols for targeting specific metacognitive deficiencies"
    priority: high
  
  - topic: "[[Cognitive Bias Mitigation Protocols]]"
    description: "Operational detection and correction algorithms for specific biases"
    priority: medium
  
  - topic: "[[Transfer-Enabling Pedagogical Frameworks]]"
    description: "Instructional design for building transferable competencies"
    priority: medium
  
  - topic: "[[Epistemic Humility and Intellectual Virtue]]"
    description: "Dispositional foundations supporting critical thinking deployment"
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICAL APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
use-cases:
  - Personal decision-making improvement
  - Professional reasoning enhancement
  - Educational instruction design
  - Research methodology
  - Strategic planning
  - Quality assurance protocols

deployment-contexts:
  - High-stakes decisions
  - Persuasive communication evaluation
  - Complex problem-solving
  - Evidence assessment
  - Strategic planning
  - Learning and skill development

tools-provided:
  - Pre-task planning protocol
  - Monitoring checkpoint template
  - Post-task reflection framework
  - Error debugging workflow
  - Calibration training exercise
  - MAI self-assessment guide
  - Recognition pattern checklist

# ═══════════════════════════════════════════════════════════════════════════
# QUALITY INDICATORS
# ═══════════════════════════════════════════════════════════════════════════
empirical-support:
  - PENCRISAL validation studies (Rivas & Saiz, 2012, 2015)
  - MAI psychometric validation (Schraw & Dennison, 1994)
  - Transfer research (Halpern, 1998; Tiruneh et al., 2017)
  - Epistemic vigilance studies (Sperber et al., 2010)
  - Metacognition-CT relationship studies (Magno, 2010; Ku & Ho, 2010)

validation-evidence:
  - Longitudinal persistence of training effects
  - Cross-cultural replication
  - Convergent validity with multiple instruments
  - Predictive validity for academic performance
  - Structural equation modeling support

limitations-noted:
  - Optimal balance of explicit vs implicit instruction remains debated
  - Domain specificity vs generality tension
  - Limited long-term naturalistic validation
  - Individual difference moderators not fully characterized

# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENT STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════
sections:
  - Abstract and Executive Overview
  - Architectural Foundation (Metacognitive Engine)
  - Deployment Challenge (Recognition Patterns)
  - Critical Thinking Skills (PENCRISAL Framework)
  - Transfer Problem
  - Metacognitive Deployment Protocols
  - Error Detection and Correction
  - Self-Assessment Frameworks
  - Bridging Transfer Gap
  - Synthesis and Integration
  - References and Resources

document-features:
  - callouts: 17
  - wiki-links: 27+
  - empirical-citations: 15+
  - operational-templates: 7
  - framework-integrations: 4
  - practical-examples: 12+

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: budding
importance: critical
foundational-for-future-learning: true

connection-strength:
  high:
    - Metacognition
    - Critical Thinking
    - Transfer of Learning
  medium:
    - Cognitive Biases
    - Decision Making
    - Self-Regulated Learning
  exploratory:
    - Expertise Development
    - Instructional Design
    - Epistemic Virtue

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM METADATA
# ═══════════════════════════════════════════════════════════════════════════
pencrisal-dimensions:
  - Deductive Reasoning
  - Inductive Reasoning
  - Practical Reasoning
  - Decision-Making
  - Problem-Solving

mai-dimensions:
  knowledge:
    - Declarative Knowledge
    - Procedural Knowledge
    - Conditional Knowledge
  regulation:
    - Planning
    - Information Management
    - Comprehension Monitoring
    - Debugging Strategies
    - Evaluation

eevf-dimensions:
  - Source Evaluation
  - Claim Evaluation
  - Receiver Self-Evaluation

assessment-instruments:
  - PENCRISAL (35 items, 0-70 scale)
  - MAI (52 items, two-factor structure)
  - Holistic Critical Thinking Scoring Rubric
  - Watson-Glaser Critical Thinking Test (referenced)
  - Cornell Critical Thinking Tests (referenced)

---

