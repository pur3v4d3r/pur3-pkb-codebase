---
title: "cosmo-report-<% tp.file.title %>-<% tp.date.now("YYYYMMDDHHmmss") %>"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
type: "<% await tp.system.suggester(['cog-psy/report', 'pkb/pkm/report', 'prompt/report','cosmo/report','edu/report', 'report'], ['cog-psy/report', 'pkb/pkm/report', 'prompt/report','cosmo/report','edu/report', 'report'], false, 'Choose one:') %>"
status: "not-read"
source: "<% tp.frontmatter.source %>"
year: "[[<% tp.date.now('YYYY') %>]]"
tags:
  - cosmology
  - project/pur3v4d3r
  - year/2025
  - self-improvement
  - pkb/metadata/frontmatter
  - pkb/maintenance/refactoring
  - pkb/maintenance/cleanup
aliases:
  - "<% tp.frontmatter.aliases %>"
link-up:
  - "[[project-pur3v4d3r-moc]]"
link-related:
  - "[[<% tp.date.now('YYYY-MM-DD') %>|Daily-Note]]"
---
