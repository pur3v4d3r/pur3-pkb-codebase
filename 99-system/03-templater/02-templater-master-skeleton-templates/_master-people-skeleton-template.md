<%*
/* ---------------------------------------------------------------
   PEOPLE / ENTITY SKELETON
   Use this for: People, Organizations, Network
   ---------------------------------------------------------------
*/
// --- CONFIGURATION: RELATIONSHIPS ---
const relations = [
    "Family", 
    "Friend", 
    "Professional", 
    "Mentor", 
    "Mentee"
];
const contextTags = [
    "Photography", 
    "Tech/AI", 
    "Personal", 
    "Local/Jax"
];
// --- INPUT PROMPTS ---
const name = await tp.system.prompt("Person's Name:");
const relation = await tp.system.suggester(relations, relations, false, "Relationship Type:");
const context = await tp.system.suggester(contextTags, contextTags, false, "Primary Context:");
// --- LOGIC: FOLLOW UP REMINDER ---
// Suggest a follow-up date
const followUpInterval = await tp.system.prompt("Follow up in X days? (Enter number)", "30");
const followUpDate = moment().add(parseInt(followUpInterval), 'days').format("YYYY-MM-DD");
_%>
---
type: "person"
relation: "<% relation %>"
context: "<% context %>"
location: 
last-contact: "<% tp.date.now("YYYY-MM-DD") %>"
next-contact: "<% followUpDate %>"
tags:
  - "people/<% relation.toLowerCase() %>"
---

# <% name %>

> [!user] Profile
> * **Relation**:: <% relation %>
> * **Location**:: 
> * **Interest**:: <% context %>

## 🤝 Interaction Log

### <% tp.date.now("YYYY-MM-DD") %>
* [Note on latest interaction…]

