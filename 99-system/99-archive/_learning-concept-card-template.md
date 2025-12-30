```
---
type: concept-card
tags: 
  - learning-theory
  - cognitive-science
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
status: "📚 Learning"
confidence_level: <% await tp.system.suggester(["🌱 Novice", "🌿 Developing", "🌳 Proficient", "🎓 Expert"], [1, 2, 3, 4], false, "Rate your confidence level") %>
source_type: <% await tp.system.suggester(["Book", "Article", "Video", "Course", "Podcast", "Discussion"], ["book", "article", "video", "course", "podcast", "discussion"]) %>
source_title: "<% await tp.system.prompt("Source title (book/article/course name)") %>"
source_author: "<% await tp.system.prompt("Author/Creator name") %>"
related_domains: [<% (await tp.system.prompt("Related domains (comma-separated, e.g., psychology, neuroscience)")).split(',').map(d => `"${d.trim()}"`).join(', ') %>]
---

# <% tp.file.title %>

> [!definition] Core Definition
> *Brief definition in your own words - aim for 1-2 sentences that capture the essence*
> **Description**: 

## 📖 Detailed Explanation

*Expand on the concept with comprehensive explanation:*
- What is it fundamentally?
- Why does it matter?
- What problem does it solve or what question does it answer?

## 🧩 Key Components

*Break down the concept into constituent parts:*

1. **Component 1**: Description
2. **Component 2**: Description
3. **Component 3**: Description

## 🔄 Mental Model

> [!analogy] Understanding Through Comparison
> *Explain this concept using an analogy, metaphor, or comparison to something familiar*

## 💡 Personal Insight

*What clicked for you? What was the "aha!" moment?*

**Connection to Prior Knowledge:**
- How does this relate to [[Concept X]] that you already understand?
- How does this contrast with [[Concept Y]]?

## 🎯 Practical Applications

> [!example] Real-World Examples
> 1. **Example 1**: Concrete scenario
> 2. **Example 2**: Different context application
> 3. **Example 3**: Edge case or unusual application

## ❓ Open Questions & Areas for Deeper Study

- [ ] Question 1 that emerged from learning this
- [ ] Aspect that needs clarification
- [ ] Related concept to explore: [[Topic to investigate]]

## 🧪 Self-Testing

> [!attention] Comprehension Check
> Without looking at notes above, can you:
> - [ ] Define the concept in one sentence
> - [ ] Explain it to someone unfamiliar with the topic
> - [ ] Identify when you'd apply this concept
> - [ ] Connect it to 3 other concepts in your knowledge base

**Review Schedule:**
- First Review: <% moment(tp.date.now("YYYY-MM-DD")).add(1, 'days').format("YYYY-MM-DD") %>
- Second Review: <% moment(tp.date.now("YYYY-MM-DD")).add(7, 'days').format("YYYY-MM-DD") %>
- Third Review: <% moment(tp.date.now("YYYY-MM-DD")).add(30, 'days').format("YYYY-MM-DD") %>

## 🔗 Knowledge Graph Connections

**Upstream Dependencies** (what you need to know first):
- [[Prerequisite Concept 1]]
- [[Prerequisite Concept 2]]

**Downstream Applications** (what this enables):
- [[Advanced Topic 1]]
- [[Advanced Topic 2]]

**Lateral Connections** (related concepts at same level):
- [[Related Concept 1]]
- [[Related Concept 2]]

---
*Last Updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
```