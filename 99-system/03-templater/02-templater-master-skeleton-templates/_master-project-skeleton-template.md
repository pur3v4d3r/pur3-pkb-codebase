<%*
/* ---------------------------------------------------------------
   PROJECT / SPRINT SKELETON
   Use this for: Projects, Goals, Sprints, Deliverables
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: DROPDOWNS ---
const statusList = [
    "1-Backlog", 
    "2-Planning", 
    "3-Active", 
    "4-Review", 
    "5-Completed", 
    "6-Archived"
];
const priorityList = [
    "High", 
    "Medium", 
    "Low"
];
const areaList = [
    "Development", 
    "Photography", 
    "Learning", 
    "Personal", 
    "Maintenance"
];
// --- INPUT PROMPTS ---
const title = await tp.system.prompt("Project Name:");
const selectedStatus = await tp.system.suggester(statusList, statusList, false, "Current Status:");
const selectedPriority = await tp.system.suggester(priorityList, priorityList, false, "Priority Level:");
const selectedArea = await tp.system.suggester(areaList, areaList, false, "Area of Responsibility:");
// --- LOGIC: DATE CALCULATIONS ---
// Ask for duration in weeks to estimate a due date
const durationWeeks = await tp.system.prompt("Estimated duration (weeks)?", "2");
const targetDate = moment().add(parseInt(durationWeeks), 'weeks').format("YYYY-MM-DD");
_%>
---
type: "project"
status: "<% selectedStatus %>"
priority: "<% selectedPriority %>"
area: "<% selectedArea %>"
started: "<% tp.date.now("YYYY-MM-DD") %>"
target-finish: "<% targetDate %>"
tags:
  - "project/<% selectedArea.toLowerCase() %>"
link-related:
  - 
---

# <% title %>

## 🎯 Objective
> [!goal]
> What is the definition of done?

## 📋 Key Deliverables
- [ ] Deliverable 1
- [ ] Deliverable 2

## 🛠 Resources & Tech Stack
* **Tools:** * **Dependencies:** ## 🗓 Log & Updates
* **<% tp.date.now("YYYY-MM-DD") %>**: Project initialized.