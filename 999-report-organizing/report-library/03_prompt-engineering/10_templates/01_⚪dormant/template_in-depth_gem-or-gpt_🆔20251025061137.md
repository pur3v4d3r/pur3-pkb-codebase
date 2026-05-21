---
title: <% tp.file.title %>
id: <% tp.date.now("YYYYMMDDHHmmss") %>
aliases:
  - prompt-engineering
type: <% tp.system.suggester(["♊ Gem", "📝 Prompt", "🦈 GPT"], ["Gem", "Prompt", "GPT"], false, "Select Note Type:") %>
status: ⚡Active
priority: ""
created: <% tp.date.now("YYYYMMDDHHmmss") %>
source: ""
url: ""
tags:
  - prompt-engineering
summary: <% tp.system.prompt("Enter a one-sentence summary of what this does:") %>
model-parameters: "0.0"
version: 1
success-rating:
output-link: ""
---

# <% tp.file.title %>

> [!important] **Core Components & Metadata**
>- *Model:* `model:: `
>- *Primary Goal:* `summary:: `
>- *Topic Area:* `topic:: `
>- *ID:* `id:: `
>- *Version:* `version:: `
>- *Status:* `status:: `

---
# <% tp.file.title %>

```prompt
---
id: prompt-block-<% tp.file.title.split('_').pop() %>
---

PASTE YOUR PROMPT OR GEM INSTRUCTION SET HERE
```

## ✍️Usage Notes & Context

- **Required Context:** What information must be provided for this prompt to work effectively? 
	
	1. 
	2. 

- **Variables:** Are there any placeholders like `{TOPIC}` or `{TONE}` that need to be replaced?
	
	1. 
	2. 

# ⌛Iteration & Test Log

## v1.0 (Initial Draft) - <% tp.date.now("YYYY-MM-DD") %>

### **Result Quality (1-5):**

- [ ] Result: 1/5
- [ ] Result: 2/5
- [ ] Result: 3/5
- [ ] Result: 4/5
- [ ] Result: 5/5

### **Observations:** What worked well? What failed?

1. 
2. 

### **Changes for next version:**

1. 
2. 


# Links to Related Content

1. 
2. 
3. 
4. 

---
