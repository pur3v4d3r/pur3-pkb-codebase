---
title: <% tp.file.title %>
id: <% tp.date.now("YYYYMMDDHHmmss") %>
aliases:
  - prompt-engineering
type: <%* const type = tp.file.title.split('_')[0].split(' ')[1]; tR += type %>
created: <% tp.date.now("YYYYMMDDHHmmss") %>
url: 
tags:
  - prompt-engineering
summary: 
model-parameters: 
version: 
success-rating:
output-link:
---


# <% tp.file.title %>


```prompt
---
id: prompt-block-<% tp.file.title.split('_').pop() %>
---

PASTE YOUR PROMPT OR GEM INSTRUCTION SET HERE

```