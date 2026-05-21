

<%*
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)
const groupA_Tags = [
    "", "", "", "", "", 
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
];  
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)
const groupB_Tags = [
    // PKM & PKB
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
    // Psychology & Cognitive
	  "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
    // Prompt Engineering
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
	  "", "", "", "", "",
    "", "", "", "", "",
    // Cross-Cutting Concepts
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
];
// Tag Suggester (Hierarchical Selection)
// GROUP A: High-Level Domains (For Tags 01 & 02)
const tag1 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 01 (Domain):");
const tag2 = await tp.system.suggester(groupA_Tags, groupA_Tags, false, "Select Tag 02 (Domain):");
// Tag Suggester (Hierarchical Selection)
// GROUP B: Granular Concepts (For Tags 03, 04, & 05)
const tag3 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 03 (Concept):");
const tag4 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 04 (Concept):");
const tag5 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 05 (Concept):");
const tag6 = await tp.system.suggester(groupB_Tags, groupB_Tags, false, "Select Tag 06 (Concept):");
// Alias system-prompt (User-Input)
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
// Type Suggester (User Selection for Type of Note)
const type = await tp.system.suggester(
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
false,
    "Choose the Type:"
)
// Status Suggester (User Selection for Status of Note)
const status = await tp.system.suggester(
	  "", "", "", "", "",
	  "", "", "", "", "",
	  "", "", "", "", "",
false,
    "Choose the Status:"
)
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
// Tag Placement in Note Body
// GROUP A: High-Level Domains
  - "<% tag1 %>"
  - "<% tag2 %>"
// Tag Placement in Note Body
// GROUP B: Granular Concepts
  - "<% tag3 %>"
  - "<% tag4 %>"
  - "<% tag5 %>"
  - "<% tag6 %>"
-%>
title: "<% tp.file.title %>"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
type: "<% type %>"
link-up:
  - 
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily-Note]]"
---

# <% tp.file.title %>



