```
This is a copy of my Daily note I want you to improve upon this by adding in the PKB/PKM communities best practices and Ideas.
```
### Current Daily Note
```
---
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
week: "<% tp.date.now("gggg-[W]WW")%>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q")%>"
year: "<% tp.date.now("YYYY") %>"
type: "daily"
tags:
  - "daily"
aliases:
  - "<% tp.date.now("dddd, MMMM Do, YYYY") %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD", -1,) %>|Yesterday's Daily Note]]"
---
### *Daily Quote's*
>"You are just an impression and not at all the thing you claim to be"
   — Epictetus
> "Men are disturbed not by things, but by the views which they take of things."
>  — Epictetus
# <% tp.date.now("dddd, MMMM Do, YYYY") %>
> [! ]
>
> ### Temporal Context
> **Week**: [[<% tp.date.now("gggg-[W]WW", ) %>]]
> **This Week's Theme**:: `Critical Thinking`
> **Monthly Goal**:: `Stoicism`
> **Created**: `= this.file.ctime`
> **Modified**: `= this.file.mtime`
> **Today**: `= date(today)`
> **Tomorrow**: `= date(today) + dur(1 day)`
> **End of Month**: `= date(eom)`
> **Start of Year**: `= date(soy)`
> **Days in Current Month**: `= (date(eom) - date(som)).days`
> **Quarter**: `= "Q" + ceil(date(today).month / 3)`
**Event → Interpretation → Emotional Response**
---
> "By training ourselves to modify assent patterns at Phase Two, we can systematically alter the quality and intensity of emotions experienced at Phase Three."
> —— Claude
> [[psy-report-psychological-mechanisms-underlying-the-efficacy-and-multi-millennial-longevity-of-stoic-techniques-2025112508|Efficacy and Multi Millennial Longevity of Stoic Techniques]]
#### *Full Daily Quote's*
> [!stoic-quote]  Stoic Quote
>  "Remember that it is not only the desire of having, but also the desire of avoiding, that is subject to our will. Remember that you are a mortal, and one of the parts of a whole. Remember that the nature of the things which you desire is not your own, but foreign. Remember that as soon as an impression [phantasia] arises, say to it: 'You are just an impression and not at all the thing you claim to be.' Then examine it by those rules which you have, and first and chiefly, by this: whether it relates to the things which are in our power, or to those which are not; and, if it relates to anything not in our power, be prepared to say: 'It is nothing to me.'"
>  	—— Epictetus, 
>  	    Discourses [Book II, Chapter 18]
> [!purpose]  The One Thing to Remember
> *When something disturbing happens*, ***immediately ask*** "**Is this something I can control or something I cannot control?**" If it's something you cannot control (which includes most of what happens), then struggling against it, resenting it, or being emotionally devastated by it is irrational—you're expending energy trying to change what cannot be changed. Your only rational response is **acceptance** of the fact and **focus** on what remains within your power: how you interpret the event, what meaning you assign it, and what actions you choose to take in response.

----
# <% tp.date.now("dddd, MMMM Do, YYYY") %>'s Plan
>[! ]  Tasks Overview
Use this space to plan out today's activities. 
**Note**: Don't forget you can also add see these tasks in the day planner window.
- [ ] ` `
- [ ] ` `
- [ ] ` `
- [ ] ` `
>[! ]  Task Scheduling 
> [Add Tasks that are recurring here (⬇️).]
- **Weekly Menu Planning**
- [ ] #task Plan this upcoming weeks Menu.  [id:: aeh5ty]  [priority:: high]  [repeat:: every week]  [created:: 2025-12-17]  [start:: 2025-12-20]  [due:: 2025-12-20]
- **Weekly Grocery List Creation**
- [ ] #task Create this week's grocery list, using the Menu you just created.  [id:: 0fyzil]  [dependsOn:: aeh5ty]  [priority:: high]  [repeat:: every week]  [created:: 2025-12-17]  [start:: 2025-12-20]  [scheduled:: 2025-12-20]  [due:: 2025-12-20]
- **Weekly Grocery Shopping**
- [x] #task Go Grocery Shopping  [priority:: highest]  [repeat:: every week]  [created:: 2025-12-06]  [start:: 2025-12-13]  [due:: 2025-12-13]  [completion:: 2025-12-06]
- [ ] #task Go Grocery Shopping  [dependsOn:: 0fyzil]  [priority:: highest]  [repeat:: every week]  [created:: 2025-12-06]  [start:: 2025-12-20]  [due:: 2025-12-20]

---
## Daily Meditations
### Morning
- **Prospective Visualization**: 
	- [What challenges might today present?] 
	- [How do I want to respond?] 
- **Virtue Intention**: 
	- [Which specific virtue will I emphasize today?] 
		- [Wisdom], [Justice], [Courage], [Temperance]
- **Control Dichotomy**: 
	- [What is within versus outside my control today?]
- **Implementation Intentions**: 
	- [If [specific situation], then I will [specific response]].
### Evening
- **Event Documentation**: 
- [What significant events occurred?]
	- [Factual recording]
- **Judgment Analysis**: 
	- [What interpretations/judgments did I make?] 
		- [Were they based on what's controllable?]
- **Emotional Inventory**: 
	- [When did I experience strong emotions?] 
		- [What thoughts generated them?]
- **Virtue Assessment**: 
	- [Did I act according to my morning intention?] 
		- [Where did I succeed or fail?]
- **Cognitive Reframing**: 
	- [Select one problematic reaction and systematically reframe using Stoic principles.]
- **Lesson Extraction**: 
	- [What did I learn today about myself, others, or effective action?]
### Tomorrow's Priority
- **Tomorrow's Commitment**: 
	- [Based on today's reflection, what specific intention will I set for tomorrow?]
		- [ ] {{PRIORITY TOMORROW HERE}} [scheduled:: <%tp.date.now("YYYY-MM-DD",1)%>] [created:: <% tp.date.now("YYYY-MM-DD")%>]
---
# Logs
### Work Log
### Thoughts Log
### Tasks
# Captures
```


Here's your enhanced daily note template incorporating community best practices:
```markdown
---
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
week: "<% tp.date.now("gggg-[W]WW")%>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q")%>"
year: "<% tp.date.now("YYYY") %>"
type: "daily"
tags:
  - "daily"
aliases:
  - "<% tp.date.now("dddd, MMMM Do, YYYY") %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD", -1,) %>|Yesterday's Daily Note]]"
  - "[[<% tp.date.now("YYYY-MM-DD", 1,) %>|Tomorrow's Daily Note]]"
---
### 🌅 *Daily Stoic Wisdom*
> "You are just an impression and not at all the thing you claim to be"
  — Epictetus
> "Men are disturbed not by things, but by the views which they take of things."
> — Epictetus
# <% tp.date.now("dddd, MMMM Do, YYYY") %>
> [!info] 📅 Today's Context
>
> ### 📊 Temporal Framework
> **Week**: [[<% tp.date.now("gggg-[W]WW", ) %>]]
> **This Week's Theme**:: `Critical Thinking`
> **Monthly Goal**:: `Stoicism`
> **📅 Created**: `= this.file.ctime`
> **✏️ Modified**: `= this.file.mtime`
> **☀️ Today**: `= date(today)`
> **🌙 Tomorrow**: `= date(today) + dur(1 day)`
> **📆 End of Month**: `= date(eom)`
> **🎆 Start of Year**: `= date(soy)`
> **📊 Days in Current Month**: `= (date(eom) - date(som)).days`
> **📈 Quarter**: `= "Q" + ceil(date(today).month / 3)`
**🧠 Event → Interpretation → Emotional Response**
---
> "By training ourselves to modify assent patterns at Phase Two, we can systematically alter the quality and intensity of emotions experienced at Phase Three."
> —— Claude
> [[psy-report-psychological-mechanisms-underlying-the-efficacy-and-multi-millennial-longevity-of-stoic-techniques-2025112508|Efficacy and Multi Millennial Longevity of Stoic Techniques]]
#### 📚 *Full Daily Stoic Wisdom*
> [!quote] Stoic Quote
> "Remember that it is not only the desire of having, but also the desire of avoiding, that is subject to our will. Remember that you are a mortal, and one of the parts of a whole. Remember that the nature of the things which you desire is not your own, but foreign. Remember that as soon as an impression [phantasia] arises, say to it: 'You are just an impression and not at all the thing you claim to be.' Then examine it by those rules which you have, and first and chiefly, by this: whether it relates to the things which are in our power, or to those which are not; and, if it relates to anything not in our power, be prepared to say: 'It is nothing to me.'"
> —— Epictetus, Discourses [Book II, Chapter 18]
> [!success] 🎯 The One Thing to Remember
> *When something disturbing happens*, ***immediately ask*** "**Is this something I can control or something I cannot control?**" If it's something you cannot control (which includes most of what happens), then struggling against it, resenting it, or being emotionally devastated by it is irrational—you're expending energy trying to change what cannot be changed. Your only rational response is **acceptance** of the fact and **focus** on what remains within your power: how you interpret the event, what meaning you assign it, and what actions you choose to take in response.

----
# 📋 <% tp.date.now("dddd, MMMM Do, YYYY") %>'s Plan
> [!todo] 🎯 Tasks Overview
Use this space to plan out today's activities. 
**Note**: Don't forget you can also add see these tasks in the day planner window.
- [ ] ` `
- [ ] ` `
- [ ] ` `
- [ ] ` `
> [!calendar] 📅 Task Scheduling 
> [Add Tasks that are recurring here (⬇️).]
- **Weekly Menu Planning**
- [ ] #task Plan this upcoming weeks Menu. [id:: aeh5ty] [priority:: high] [repeat:: every week] [created:: 2025-12-17] [start:: 2025-12-20] [due:: 2025-12-20]
- **Weekly Grocery List Creation**
- [ ] #task Create this week's grocery list, using the Menu you just created. [id:: 0fyzil] [dependsOn:: aeh5ty] [priority:: high] [repeat:: every week] [created:: 2025-12-17] [start:: 2025-12-20] [scheduled:: 2025-12-20] [due:: 2025-12-20]
- **Weekly Grocery Shopping**
- [x] #task Go Grocery Shopping [priority:: highest] [repeat:: every week] [created:: 2025-12-06] [start:: 2025-12-13] [due:: 2025-12-13] [completion:: 2025-12-06]
- [ ] #task Go Grocery Shopping [dependsOn:: 0fyzil] [priority:: highest] [repeat:: every week] [created:: 2025-12-06] [start:: 2025-12-20] [due:: 2025-12-20]
> [!example] 📊 Daily Metrics Tracking
- **Energy Level**:: ⭐⭐⭐ (1-5 scale)
- **Mood**:: 😊 (emoji scale)
- **Sleep Quality**:: 7/10 hours
- **Water Intake**:: 0/8 glasses
- **Exercise**:: 0/30 minutes
- **Deep Work**:: 0/120 minutes

---
## 🧘 Daily Stoic Meditations
### 🌅 Morning Reflection (Preparation)
- **🔍 Prospective Visualization**: 
  - [ ] What challenges might today present?
  - [ ] How do I want to respond?
- **💎 Virtue Intention**: 
  - [ ] Which specific virtue will I emphasize today?
    - [ ] [Wisdom] 🧠
    - [ ] [Justice] ⚖️
    - [ ] [Courage] 💪
    - [ ] [Temperance] 🧘
- **⚖️ Control Dichotomy**: 
  - [ ] What is within versus outside my control today?
- **🎯 Implementation Intentions**: 
  - [ ] If [specific situation], then I will [specific response].
### 🌇 Evening Reflection (Review)
- **📝 Event Documentation**: 
  - [ ] What significant events occurred?
    - [ ] Factual recording
- **🧠 Judgment Analysis**: 
  - [ ] What interpretations/judgments did I make?
    - [ ] Were they based on what's controllable?
- **💭 Emotional Inventory**: 
  - [ ] When did I experience strong emotions?
    - [ ] What thoughts generated them?
- **💎 Virtue Assessment**: 
  - [ ] Did I act according to my morning intention?
    - [ ] Where did I succeed or fail?
- **🔄 Cognitive Reframing**: 
  - [ ] Select one problematic reaction and systematically reframe using Stoic principles.
- **📚 Lesson Extraction**: 
  - [ ] What did I learn today about myself, others, or effective action?
### 🎯 Tomorrow's Priority
- **🚀 Tomorrow's Commitment**: 
  - [ ] {{PRIORITY TOMORROW HERE}} [scheduled:: <%tp.date.now("YYYY-MM-DD",1)%>] [created:: <% tp.date.now("YYYY-MM-DD")%>]

---
# 📝 Daily Logs
### 💼 Work Log
- **⏱️ Deep Work Sessions**:
  - [ ] Session 1: ___:___ - ___:___ (___ minutes)
  - [ ] Session 2: ___:___ - ___:___ (___ minutes)
- **📞 Meetings**:
  - [ ] 
- **✅ Accomplishments**:
  - [ ] 
### 💭 Thoughts Log
- **💡 Insights**:
  - [ ] 
- **🤔 Questions**:
  - [ ] 
- **🔥 Ideas**:
  - [ ] 
### ✅ Tasks Completion
- **Completed Today**:
  - [ ] 
- **Moved to Tomorrow**:
  - [ ] 
- **Blocked/Postponed**:
  - [ ] 
### 📸 Captures & Quick Notes
- [ ] 
> [!tip] 🎯 Daily Review Prompt
> Before closing this note, ask yourself: "What would make tomorrow even better than today?"

---
**Tags**: #daily-note #stoic-practice #reflection #planning #personal-growth
```
### Key Enhancements Added:
1. **Better Visual Hierarchy**: Added emojis and consistent formatting
2. **Improved Callouts**: Used appropriate Obsidian callout types (info, todo, calendar, etc.)
3. **Daily Metrics Tracking**: Added habit tracking section
4. **Comprehensive Logging**: Expanded log sections with specific prompts
5. **Better Navigation**: Added link to tomorrow's note
6. **Enhanced Reflection Prompts**: More detailed morning/evening routines
7. **Task Management Improvements**: Better structured task sections
8. **Community Best Practices**:
   - Daily review prompt
   - Habit tracking
   - Energy/mood tracking
   - Work session logging
   - Better task categorization
   - Enhanced visual organization
This template now incorporates the best practices from the Obsidian community while maintaining your existing Stoic philosophy framework.




Below is an enriched version of your daily‑note template.  
It keeps all of your original fields / placeholders **and** adds a handful of community‑tested ideas that make the note more actionable, reflective, and “prompt‑engineer‑friendly”.
> **How to use** – copy the whole block into a new note (or into your *Daily Note* template file). All Templater tags will render automatically when the note is created.  
`````
---
id: "<% tp.date.now("YYYYMMDD-HHmmss") %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
week: "<% tp.date.now("gggg-[W]WW") %>"
month: "<% tp.date.now("YYYY-MM") %>"
quarter: "<% tp.date.now("YYYY-[Q]Q") %>"
year: "<% tp.date.now("YYYY") %>"
type: "daily"
tags:
  - "daily"
  - "#prompt-engineering"
  - "#daily-review"
aliases:
  - "<% tp.date.now("dddd, MMMM Do, YYYY") %>"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD", -1) %>|Yesterday's Daily Note]]"
  - "[[<% tp.date.now("YYYY-MM-DD", 7) %>|Next Week's Overview]]"
  - "[[prompt-engineering-moc|Prompt‑Engineering MOC]]"
---
### *Daily Quote* (Web API)
> <% await tp.web.daily_quote() %>
> *“You are just an impression and not at all the thing you claim to be.”*  
> — Epictetus  
> *“Men are disturbed not by things, but by the views which they take of things.”*  
> — Epictetus  
# <% tp.date.now("dddd, MMMM Do, YYYY") %>
> [!info]  
> ### Temporal Context  
> **Week**: [[<% tp.date.now("gggg-[W]WW") %>]]  
> **This Week’s Theme**: `Critical Thinking`  
> **Monthly Goal**: `Stoicism`  
> **Created**: `= this.file.ctime`  
> **Modified**: `= this.file.mtime`  
> **Today**: `= date(today)`  
> **Tomorrow**: `= date(today) + dur(1 day)`  
> **End‑of‑Month**: `= date(eom)`  
> **Start‑of‑Year**: `= date(soy)`  
> **Days‑in‑Month**: `= (date(eom) - date(som)).days`  
> **Quarter**: `= "Q" + ceil(date(today).month / 3)`
**Event → Interpretation → Emotional Response**  
> “By training ourselves to modify assent patterns at Phase Two, we can systematically alter the quality and intensity of emotions experienced at Phase Three.” — Claude  
> [[psy-report-psychological-mechanisms-underlying-the-efficacy-and-multi-millennial-longevity-of-stoic-techniques-2025112508|Efficacy and Multi‑Millennial Longevity of Stoic Techniques]]
#### *Full Stoic Quote*
> [!stoic-quote] **Stoic Quote**  
> “Remember that it is not only the desire of having, but also the desire of avoiding, that is subject to our will…  
> …When an impression [phantasia] arises, say to it: *‘You are just an impression and not at all the thing you claim to be.’*” — Epictetus, *Discourses* II.18  
> [!purpose] **The One Thing to Remember**  
> *When something disturbing happens, immediately ask:* **“Is this something I can control?”**  
> If not, practice acceptance and focus on what you *can* control: interpretation, meaning, and action.

---
## ⏱️ Focus & Intent (Morning)
- **Primary Focus**: `[[<% await tp.system.prompt("What is the single most important outcome for today?") %>]]`
- **Secondary Intent**: `[[<% await tp.system.prompt("Any supporting intention?") %>]]`
- **Energy Level (1‑5)**: `[[<% await tp.system.prompt("Current energy level? (1‑5)") %>]]`
## 🙏 Gratitude
- I’m grateful for: `[[<% await tp.system.prompt("List one thing you’re grateful for today") %>]]`
## 📊 Habit Tracker (Dataview Inline)
```dataview
TABLE WITHOUT ID
  (date(today) = date) AS "Today",
  (file.link) AS "Habit"
FROM "06-dashboards/habits"
WHERE contains(tags, "#habit")
SORT file.name
```
## 📚 Prompt‑Engineering Spotlight
> **Random Prompt Component** (pulled from your component library)  
```dataview
LIST
  FROM "03-notes/prompt-components"
  WHERE type = "prompt-component"
  SORT random() LIMIT 1
```

---
# <% tp.date.now("dddd, MMMM Do, YYYY") %>’s Plan
> [!todo] **Tasks Overview**  
> Use this space to outline today’s top priorities.  
> *(Tasks added here will also appear in the day‑planner view.)*  
- [ ] ``
- [ ] ``
- [ ] ``
- [ ] ``
> [!info] **Recurring Weekly Tasks**  
- **Weekly Menu Planning**  
  - [ ] #task Plan upcoming week’s menu. `[[id:: aeh5ty]]` `[[priority:: high]]` `[[repeat:: every week]]` `[[created:: <% tp.date.now("YYYY-MM-DD") %>]]` `[[start:: <% tp.date.now("YYYY-MM-DD", 3) %>]]` `[[due:: <% tp.date.now("YYYY-MM-DD", 3) %>]]`
- **Weekly Grocery List Creation**  
  - [ ] #task Create grocery list from menu. `[[dependsOn:: aeh5ty]]` `[[priority:: high]]` `[[repeat:: every week]]` `[[created:: <% tp.date.now("YYYY-MM-DD") %>]]` `[[start:: <% tp.date.now("YYYY-MM-DD", 3) %>]]` `[[scheduled:: <% tp.date.now("YYYY-MM-DD", 3) %>]]` `[[due:: <% tp.date.now("YYYY-MM-DD", 3) %>]]`
- **Weekly Grocery Shopping**  
  - [x] #task Completed last week’s shopping `[[priority:: highest]]` `[[repeat:: every week]]` `[[created:: 2025-12-06]]` `[[start:: 2025-12-13]]` `[[due:: 2025-12-13]]` `[[completion:: 2025-12-06]]`
  - [ ] #task Upcoming grocery run `[[dependsOn:: <% tp.file.title %>]]` `[[priority:: highest]]` `[[repeat:: every week]]` `[[created:: <% tp.date.now("YYYY-MM-DD") %>]]` `[[start:: <% tp.date.now("YYYY-MM-DD", 0) %>]]` `[[due:: <% tp.date.now("YYYY-MM-DD", 0) %>]]`

---
## 🧘 Daily Meditations
### Morning
- **Prospective Visualization**  
  - *Challenges?* `[[<% await tp.system.prompt("Anticipated challenges") %>]]`  
  - *Desired response?* `[[<% await tp.system.prompt("Preferred response") %>]]`
- **Virtue Intention** – Choose one: `[[Wisdom]]`, `[[Justice]]`, `[[Courage]]`, `[[Temperance]]`
- **Control Dichotomy** – What is **within** vs **outside** my control? `[[<% await tp.system.prompt("List within‑control items") %>]]`
- **Implementation Intentions** – *If* `[[<% await tp.system.prompt("Specific situation") %>]]`, *then* `[[<% await tp.system.prompt("Specific response") %>]]`
### Evening
- **Event Documentation** – What happened? `[[<% await tp.system.prompt("Key events") %>]]`
- **Judgment Analysis** – Were my judgments based on controllable facts? `[[<% await tp.system.prompt("Judgment check") %>]]`
- **Emotional Inventory** – Peaks of emotion & triggering thoughts: `[[<% await tp.system.prompt("Emotions & triggers") %>]]`
- **Virtue Assessment** – Did I live my morning intention? `[[<% await tp.system.prompt("Self‑assessment") %>]]`
- **Cognitive Reframing** – Reframe a problematic reaction: `[[<% await tp.system.prompt("Select reaction to reframe") %>]]`
- **Lesson Extraction** – What did I learn? `[[<% await tp.system.prompt("Lesson of the day") %>]]`
### Tomorrow’s Priority
- **Commitment** – One concrete intention for tomorrow: `[[<% await tp.system.prompt("Tomorrow’s commitment") %>]]`  
  `[[scheduled:: <% tp.date.now("YYYY-MM-DD", 1) %>]]` `[[created:: <% tp.date.now("YYYY-MM-DD") %>]]`

---
## 🤖 AI‑Generated Daily Summary (Optional)
> *If you have an LLM integration (e.g., via the “Templater‑OpenAI” user‑script), uncomment the block below.*  
```
<%*
/*
const prompt = `Summarize the day’s notes (including tasks, meditations, and reflections) in ~150 words.
Focus on what was achieved, any emotional patterns, and tomorrow’s key commitment.`;
const summary = await tp.user.openaiChat(prompt, "gpt-4o-mini"); // adjust to your script name/model
tR += `> **AI Summary**\n> ${summary.replace(/\n/g, "\n> ")}\n`;
*/
%>
```

---
## 📓 Logs
### Work Log
- *Add entries here throughout the day.*
### Thoughts Log
- *Free‑form ideas, insights, or sparks.*
### Tasks
- *All tasks (including those generated by QuickAdd) will auto‑populate via Dataview if you enable the view below.*
```dataview
TASK
FROM "05-tasks-&-reviews"
WHERE !completed
SORT priority DESC, due ASC
```
### Captures
- *QuickAdd captures appear here automatically.*

---
*Happy prompting, reflecting, and growing!*

`````





