<%*
const files = this.app.vault.getMarkdownFiles();
const scratchpadRegex = /^Scratchpad-(\d+)/;
let maxNumber = 0;
for (const file of files) {
  const match = file.basename.match(scratchpadRegex);
  if (match) {
    const currentNumber = parseInt(match[1], 10);
    if (currentNumber > maxNumber) {
      maxNumber = currentNumber;
    }
  }
}
const nextNumber = (maxNumber + 1).toString().padStart(2, '0');
const newTitle = `Scratchpad-${nextNumber}`;
await tp.file.rename(newTitle);
const noteContent = `---
title: ${newTitle}
id: ${tp.date.now("YYYYMMDDHHmmss")}
type: scratchpad
status: draft
source: pur3v4d3r
url: ""
tags:
  - daily/scratchpad
aliases:
  - daily-scratchpad
  - scratchpad
link-up: ""
link-related:
  - 
---

# ${newTitle}
`;

tR += noteContent;

%>
### Today's Active TO-DO** LIST
```dataview
TASK 
WHERE created = date(today)
LIMIT 10
SORT created DESC
```
### Yesterday's Completed Tasks

```dataview
TASK
WHERE completed
WHERE file.cday = (date(yesterday) - dur(1 day))
LIMIT 10
GROUP BY file.link
```
# 📥Intake

> STOICISM: DICHOTOMY OF CONTROL
> > - Does this impression correctly identify what is good, evil, or indifferent? 
> > > - More specifically, does it attribute value to something within my control or beyond it?










---
# 💡Initial Processing

>[!question]
> - *What* is the **core idea** here?
> - *What* does this **connect to**?
> - *What* **assumptions** am **I making**?
> - *What* is the **immediate next action**?








---

>[!disposition]
> 🗃️ Disposition
> *Once processed, check one and delete the note or move to archive.*
>
> - [ ] **Processed:** Ideas moved to permanent notes.
> - [ ] **Archived:** Moved to reference folder.
> - [ ] **Actioned:** Tasks moved to task manager.
> - [ ] **Deleted:** No longer needed.








---

>[!problem-clarity-solution]
> ⚡ **Problem-Clarity-Solution**
>
> - **Problem**: Define the actual problem in one clear sentence.
>
> - **Clarity (Knowns/Unknowns)**: What do I know about this? What do I not know and need to find out?
>
> - **Solution (Hypothesis)**: What is a potential path forward? What is the first step?

---

>[!zettelkasten-incubator]
📚 **Zettelkasten Incubator**
>
> - **Source (Bibliographic)**: [Paste citation or link]
>
> - **Verbatim Quote**: "…"
>
> - **My Thought (Paraphrased)**: [Re-write the idea entirely in your own words. How do you understand it?]
>
> - **Connections**: [[Related Idea 1]], [[Future Question]]

---

>[!project-kickstarter]
> 🚀 **Project Kickstarter**
>
> - **Objective**: What is the desired final outcome?
>
> - **Why**: What is the core motivation or purpose?
>
> - **Key Components**: What are the 3-5 major "chunks" of this project?
>
> - **First Actions**: What are the very first physical steps to get moving?

---

## Recommeded Topics to Process

