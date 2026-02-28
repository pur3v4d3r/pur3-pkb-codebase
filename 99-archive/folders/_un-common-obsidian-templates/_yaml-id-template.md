---
title: "<% tp.file.title %>"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
type: "<% await tp.system.suggester(['cog-psy', 'pkb/pkm', 'prompt','cosmo','edu', 'report'], ['cog-psy', 'pkb/pkm', 'prompt','cosmo','edu', 'report'], false, 'Choose one:') %>"
status: not-read
source: "<% tp.frontmatter.source %>"
year: "[[<% tp.date.now('YYYY') %>]]"
tags:
  - year/2025
  - pkb/maintenance/refactoring
  - pkb/maintenance/cleanup
aliases:
  - "<% tp.frontmatter.aliases %>"
link-up:
  - <% tp.frontmatter.link-up %>
  - 
  -
  -
link-related:
  - "[[<% tp.date.now('YYYY-MM-DD') %>|Daily-Note]]"
---

<% tp.file.include("[[_component-dataview-inline-link-header]]") %>