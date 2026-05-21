<%*
// Permanent Note Template with Alias Configuration
const title = await tp.system.prompt("Enter Title for YAML:");
const alias1 = await tp.system.prompt("Enter first alias (or press Enter to skip):");
const alias2 = await tp.system.prompt("Enter second alias (or press Enter to skip):");
const tag1 = await tp.system.suggester(
  ["Psychology", "Philosophy", "Education", "PKM", "PKB", "Prompt-Engineering", "Methodology", "Cosmology"],
  ["psychology", "philosophy", "education", "pkm", "pkb", "prompt-engineering", "methodology", "cosmology"],
  false,
  "Select primary domain, Tag01:"
);
const tag2 = await tp.system.suggester(
  ["Psychology", "Philosophy", "Education", "PKM", "PKB", "Prompt-Engineering", "Methodology", "Cosmology"],
  ["psychology", "philosophy", "education", "pkm", "pkb", "prompt-engineering", "methodology", "cosmology"],
  false,
  "Select primary domain, Tag02:"
);
const tag3 = await tp.system.suggester(
  ["topic/psychology/metacognition", "topic/psychology/self", "topic/pkb/infrastructure", "topic/planning", "source/llm/claude", "source/llm/gemini", "source/llm", "topic/psychology/cognitive-load-theory", "topic/education/prompt-engineering"],
  ["topic/psychology/metacognition", "topic/psychology/self", "topic/pkb/infrastructure", "topic/planning", "source/llm/claude", "source/llm/gemini", "source/llm", "topic/psychology/cognitive-load-theory", "topic/education/prompt-engineering"],
  false,
  "Select Tag03:"
);
const tag4 = await tp.system.suggester(
  ["topic/psychology/metacognition", "topic/psychology/self", "topic/pkb/infrastructure", "topic/planning", "source/llm/claude", "source/llm/gemini", "source/llm", "topic/psychology/cognitive-load-theory", "topic/education/prompt-engineering"],
  ["topic/psychology/metacognition", "topic/psychology/self", "topic/pkb/infrastructure", "topic/planning", "source/llm/claude", "source/llm/gemini", "source/llm", "topic/psychology/cognitive-load-theory", "topic/education/prompt-engineering"],
  false,
  "Select Tag04:"
);
const source = await tp.system.suggester(
  ["Foundational-Claude", "Foundational-Gemini", "First-Principles-Thinking", "First-Principles-Claude", "First-Principles-Gemini", "Conceptual Genealogy", "Systems-Thinking", "Narrative-Driven", "Case-Study-Method", "Comparative-Analysis", "Problem-Based-Learning", "Socratic-Inquiry", "URG012", "Claude", "Gemini"],
  ["foundational-claude", "foundational-Gemini", "first-principles-thinking", "first-principles-claude", "first-principles-gemini", "conceptual genealogy", "systems-thinking", "narrative-driven", "case-study-method", "comparative-analysis", "problem-based-learning", "socratic-inquiry", "urg012", "claude", "gemini"],
    false,
    "Choose the Source:" 
);
const type = await tp.system.suggester(
  ["Report", "psy-report", "prompt-report", "pkb-report", "edu-report", "cosmo-report"],
  ["report", "psy-report", "prompt-report", "pkb-report", "edu-report", "cosmo-report"],
  false,
  "Select report type:"
);
-%>
---
aliases:
  - "<% alias1 %>"
  - "<% alias2 %>"
tags:
  - "type/report"
  - "year/2025"
  - "<% tag1 %>"
  - "<% tag2 %>"
  - "<% tag3 %>"
  - "<% tag4 %>"
source: "<% source %>"
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

> [!left-off-reading-at]
> - Last-Read-POS:: 

{{**PLACE COPIED TEXT HERE**}}


