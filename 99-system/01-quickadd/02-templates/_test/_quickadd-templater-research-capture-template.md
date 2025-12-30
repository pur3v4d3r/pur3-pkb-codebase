<%*
// This template is designed to be called from QuickAdd with pre-filled variables
// QuickAdd can pass in: sourceTitle, sourceAuthor, sourceType, sourceUrl
const title = tp.user.sourceTitle || await tp.system.prompt("Source Title:");
const author = tp.user.sourceAuthor || await tp.system.prompt("Author:");
const type = tp.user.sourceType || await tp.system.suggester(["Article", "Book", "Paper"], ["article", "book", "paper"]);
const url = tp.user.sourceUrl || await tp.system.prompt("URL (optional):", "");
const noteTitle = `${author} - ${title}`;
const today = tp.date.now("YYYY-MM-DD");
// Determine tags based on source type
let tags = "#type/literature";
if (type === "paper") tags += " #type/research-paper";
if (type === "book") tags += " #type/book";
if (type === "article") tags += " #type/article";
// Create the literature note
const content = `---
title: ${noteTitle}
type: literature
created: ${today}
author: ${author}
source-type: ${type}
source-url: ${url}
status: unread
tags: [${tags}]
---
# ${noteTitle}
## Source Information
- Author: ${author}
- Type: ${type}
- URL: ${url}
## Summary
## Key Quotes
## Insights
## Related Notes
## Processing Log
- Added to library: ${today}
`;
await tp.file.create_new(content, noteTitle, false, tp.file.folder(true) + "/04-library");
// Update reading dashboard
const dashboardFile = tp.file.find_tfile("Reading Dashboard");
if (dashboardFile) {
  const dashboardContent = await tp.file.content(dashboardFile);
  const updatedContent = dashboardContent.replace(
    "## Current Reading\n", 
    `## Current Reading\n- [[${noteTitle}]]\n`
  );
  await tp.file.modify(dashboardFile, updatedContent);
}
%>