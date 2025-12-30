---
type: concept-card
tags:
  - learning-science
  - learning-theory
  - cognitive-development
  - self-improvement/skill-development
  - knowledge-work/thinking
  - knowledge-work/learning/study-methods
  - knowledge-workflow/synthesis/integration
  - knowledge-workflow/processing/elaboration
  - status/review
  - status/in-progress
  - nature/reflective
  - mode/analytical
  - mode/reflective
  - mode/practical
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
created: "<% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>"
week: "[[<% tp.date.now("gggg-[W]WW") %>]]"
month: "[[<% tp.date.now("YYYY-MM") %>]]"
quarter: "[[<% tp.date.now("YYYY-[Q]Q") %>]]"
year: "[[<% tp.date.now("YYYY") %>]]"
key-term: "<% await tp.system.prompt("Key term of this Concept-Card:") %>"
confidence_level: <% await tp.system.suggester(["🌱 Novice", "🌿 Developing", "🌳 Proficient", "🎓 Expert"], [1, 2, 3, 4], false, "Rate your confidence level") %>
source_type: <% await tp.system.suggester(["Book", "Report", "Article", "Course", "Podcast", "Discussion"], ["book", "report", "article", "course", "podcast", "discussion"]) %>
source_title: "<% await tp.system.prompt("Source title (book/article/course name)") %>"
source_author: "<% await tp.system.prompt("Author/Creator name") %>"
related_domains: [<% (await tp.system.prompt("Related domains (comma-separated, e.g., psychology, neuroscience)")).split(',').map(d => `"${d.trim()}"`).join(', ') %>]
status: "in-progress"
title: "<% await tp.system.prompt("Title for YAML:") %>"
---

# <% tp.frontmatter.title %>

> [!definition] Core Definition
> [Key-Term:: <% tp.frontmatter.key-term %>]
> [Definition:: ]

## Detailed Explanation

*Expand on <% tp.frontmatter.key-term %> with comprehensive explanation:*
- What is it fundamentally?
- Why does it matter?
- What problem does it solve or what question does it answer?

## Key Components

*Break down <% tp.frontmatter.key-term %>t into constituent parts:*

1. **Component 1**: Description
2. **Component 2**: Description
3. **Component 3**: Description

## Mental Model

> [!analogy] Understanding Through Comparison
> *Explain <% tp.frontmatter.key-term %> using an analogy, metaphor, or comparison to something familiar*

## Personal Insight

*What clicked for you? What was the "aha!" moment?*

**Connection to Prior Knowledge:**
- How does this relate to [[Concept X]] that you already understand?
- How does this contrast with [[Concept Y]]?

### Practical Applications for <% tp.frontmatter.key-term %>

> [!example] Real-World Examples
> 1. **Example 1**: Concrete scenario
> 2. **Example 2**: Different context application
> 3. **Example 3**: Edge case or unusual application

## Open Questions & Areas for Deeper Study

- [ ] Question 1 that emerged from learning this.
- [ ] Aspect that needs clarification?
- [ ] Related concept to explore: 
	- [ ] [[Topic to investigate]]
	- [ ] [[Topic to investigate]]
	- [ ] [[Topic to investigate]]

## Self-Testing

> [!attention] Comprehension Check
> Without looking at notes above, can you:
> - [ ] Define <% tp.frontmatter.key-term %> in one sentence?
> - [ ] Explain <% tp.frontmatter.key-term %> to someone unfamiliar with the topic?
> - [ ] Identify when you'd apply <% tp.frontmatter.key-term %>?
> - [ ] Connect it to 3 other concepts in your knowledge base?

**Review Schedule for <% tp.frontmatter.key-term %>:**
- First Review: <% moment(tp.date.now("YYYY-MM-DD")).add(1, 'days').format("YYYY-MM-DD") %>
- Second Review: <% moment(tp.date.now("YYYY-MM-DD")).add(7, 'days').format("YYYY-MM-DD") %>
- Third Review: <% moment(tp.date.now("YYYY-MM-DD")).add(30, 'days').format("YYYY-MM-DD") %>

## Knowledge Graph Connections

#### **Upstream Dependencies** 
- (What you need to know first about <% tp.frontmatter.key-term %>):
	- [[Prerequisite Concept 1]]
	- [[Prerequisite Concept 2]]
#### **Downstream Applications** 
(What does <% tp.frontmatter.key-term %> enable?):
	- [[Advanced Topic 1]]
	- [[Advanced Topic 2]]
#### **Lateral Connections** 
(Related concepts to <% tp.frontmatter.key-term %>, at same level.):
	- [[Related Concept 1]]
	- [[Related Concept 2]]
---
*Last Updated:<% tp.file.last_modified_date("dddd, MMMM Do YYYY @ HH:mm") %>*