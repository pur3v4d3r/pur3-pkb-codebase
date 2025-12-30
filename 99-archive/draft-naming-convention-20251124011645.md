---
aliases:
  - Draft Naming Convention
---



### Draft for Naming Conventio
1. Create reference note: "Naming Convention Standard"
2. Define pattern for different note types:
    - Permanent notes: `[topic]_atomic-note_[id].md`
    - Reference notes: `[topic]_reference_[id].md`
    - MOCs: `[topic]_🗺️moc.md`
    - Projects: `[year]-[month]_[project-name]_🚀.md`
    - Daily notes: `YYYY-MM-DD_daily-note.md`
 3. Document exceptions and special cases

[[reference-draft-naming-convention-pur3v4d3r-202511170115]]
```
# Naming Convention

## Reference Key

- []     - Note: These only deliniate seperation here, not throughout the PKB.
- [{id}] - All id's are generated through Templater via [<% tp.date.now("YYYYMMDDHHmmss") %>]
- pur3   - Type of note created by the user me Pur3v4d3r
- Permanent Notes - These are not the same as a traditional Atomic Note These are definition or notes Im keeping on specific termonology Im studying, definitions, theories, methodologies, frameworks, the people resopnsible for these academic acts, Etc.These get stored in temporary folder within a permanent folder. The move freeley between the temporary options based on what Im studying. I just keep adding to them everytime I come across new information, connecting it to the information I currently have stored in these notes. So some are far more advanced then others but its okay because I see it as they are a some what realistic representation of what I have learned, just explecitley more detailed. I find that this is an exceptional way to learn. What are your thoughts on this? I dont know if there is already something silmilar or not. I havent come across it yet if there is. Is this system any good, or am I messing up something, It kind of just devweloped on its own.
- I need to figuer out a way to incorperate an Id marker or something into the notes name however when I add in the Id it breaks the ability to use them as wiki links in the generated content you provide me with, as it looks like this: "…the [[Self-Regulation Theory 20251117035824]] is based on this…" so I need help with this system.

----
## List of Naming Patterns

- General
[general]-[source(llm-chat|pur3)]-[{topic}]-[{semantic-title}]-[{id}].md
	- Example: `pur3-infastructure-naming-convention-update-20251117032320.md`
	  
- Report
[{type}(academic, pkb, prompting, cosmology, general)]-[{semantic-title}]-[{id}].md
	- Example: `academic-report-comprehensive-overview-or-how-self-regulation-can-be-implemented-through-a-pkb-20251117032306.md`
	  
- Reference Notes
[reference]-[type(instructional, comprehensive, qiuick, Etc.)]-[{semantic-title}]-[{id}].md
	- Example: `reference-comprehensive-learning-about-naming-patterns-20251117032856.md`

Quick Referenc for Reference Type:	  
 - quick - Brief lookup reference (1-2 pages)
 - standard - Moderate depth (3-10 pages)  
 - comprehensive - Exhaustive coverage (10+ pages)
 - instructional - Step-by-step how-to guides
   
- Topic Set
[topic-set]-[{semantic-title}]-[{id}].md
	- Example: `topic-set-cognitive-self-regulation-through-pkb-use-202511170363044.md`
	  
- Daily Notes
[YYYY-MM-DD].md
	- Example: 2025-11-17.md
	  
- Projects
[project]-[{semantic-title}]-[{id}].md
	- Example: `project-pur3v4d3r-20251117033249.md`
	  
- Permanent Notes - (Note: Knowledge-Graph these are the notes I create during active reading from the wiki-links I have you place in the output.)
[{Term/Theory/Person}].md
	- Example: [[Constructivist Epistemology]]
	- Example: [[Curve Of Forgetting]]
	- Example: [[Metacognitive Awareness]]
	- Example: [[Strategic Planning]]
	- Example: [[Socratic Method]]
	- Example: [[The Law Of Cognitive Miserliness]]
	- Example: [[Self Regulation Theory]]
	- Example: [[Getting Things Done (GTD)]]
	- Example: [[Knowledge Management]]
	- Example: [[Stock Of Abstract Conceptualizations]]
	  
- Atmoic/Evergreen Notes
[atomic]-[{topic}]-[{semantic-title}]-[{id}].md
	- Example: `atomic-cognitive-psycology-my-theory-on-how-the-education-system-is-failing-all-of-us-20251117034030.md`
	  
- MOC
[moc]-[{topic}]-[{semantic-title}]-[{id}].md
	- Example: `moc-pkb-systems-infastructure-update-20251117034153.md`
	  
- Dashboard
[dashboard]-[{topic}]-[{semantic-title}]-[{id}].md
	- Example: dashboard-pkb-systems-infastructure-update-20251117034253.md`
	  
- Composite-Prompt
[prompt]-[{semantic-title}]-[{version}]-[{id}].md
	- Example: `prompt-academic-report-first-priciples-v2.0.0-20251117034339.md`
	  
- Composite Agent/Project/Gem
[agent]-[(claude-project|gemini-gem)]-[{semantic-title}]-[{version}]-[{id}].md
	- Example: `agent-clade-project-component-librarian-v1.0.1-20251117034513.md`
	  
- Prompt Component
[component]-[{component-type}(persona, instruction, constraints, formats, context)]-[{semantic-title}]-[{version}]-[{id}].md
	- Example: `component-persona-information-architect-pkb-speacialist-v2.0.0-20251117034712.md`
	  
- Archive 
  - Folder/Hybrid System will be put in place.
	  
- System Reference
_[{semantic-title}].md
	- Example: `_pkb-cheat-sheet.md`
	  
- Templates
_[template]-[{semantic-title}].md
	- Example: _template-daily-note
	  

```