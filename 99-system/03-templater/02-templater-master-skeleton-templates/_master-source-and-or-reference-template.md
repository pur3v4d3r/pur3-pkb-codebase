<%*
/* ---------------------------------------------------------------
   SOURCE / REFERENCE SKELETON
   Use this for: Books, Articles, Videos, Papers
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: MEDIA TYPES ---
const mediaTypes = [
    "Book", 
    "Article", 
    "Video", 
    "Course", 
    "Whitepaper", 
    "Podcast"
];
const statusOptions = [
    "To-Consume", 
    "Reading", 
    "Processing", 
    "Finished", 
    "Abandoned"
];
// --- INPUT PROMPTS ---
const fullTitle = await tp.system.prompt("Title of Work:");
const authorName = await tp.system.prompt("Author / Creator Name:");
const urlLink = await tp.system.prompt("URL (Paste link or leave empty):");
const mediaType = await tp.system.suggester(mediaTypes, mediaTypes, false, "Select Media Type:");
const currentStatus = await tp.system.suggester(statusOptions, statusOptions, false, "Current Status:");
// --- LOGIC: TITLE CLEANING ---
// Removes illegal characters from filenames just in case
const fileName = fullTitle.replace(/[:\/\\|?*"]/g, "");
_%>
---
type: "reference"
subtype: "<% mediaType.toLowerCase() %>"
author: "[[<% authorName %>]]"
status: "<% currentStatus %>"
url: "<% urlLink %>"
rating: 
tags:
  - "input/<% mediaType.toLowerCase() %>"
created: "<% tp.date.now("YYYY-MM-DD") %>"
---

# <% fullTitle %>

> [!info] Metadata
> * **Author**:: [[<% authorName %>]]
> * **Link**:: <% urlLink %>
> * **Type**:: <% mediaType %>

## 🧠 Summary / Abstract
[Enter a high-level summary here]

## 📝 Notes & Highlights

## 🔗 Connected Concepts
- [[Related Topic A]]
- [[Related Topic B]]