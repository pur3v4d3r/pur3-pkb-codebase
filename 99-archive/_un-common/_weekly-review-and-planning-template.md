---
type: weekly-review
tags:
year: <% tp.date.now("YYYY") %>
---

# Week <% tp.frontmatter.week_number %> Review - <% moment(tp.date.now("YYYY-MM-DD")).format("MMMM YYYY") %>

> [!abstract] Week at a Glance
> **Period**: <% moment(tp.frontmatter.week_start).format("MMM DD") %> - <% moment(tp.frontmatter.week_end).format("MMM DD, YYYY") %>
> **Energy Level**: <% tp.frontmatter.energy_level %>
> **Satisfaction**: <% "⭐".repeat(tp.frontmatter.satisfaction_rating) %>

---

## 🎯 Goal Progress Review

### Professional Goals

> [!key-claim] Primary Objective
> *What was the main professional goal for this week?*
> Main Goal: <% tp.file.cursor() %>

**Progress Status:**
- [ ] Goal achieved completely
- [ ] Made significant progress
- [ ] Some progress, but behind schedule
- [ ] Minimal or no progress

**Key Accomplishments:**
1. 
2. 
3. 

**Challenges Encountered:**
- 

**Lessons Learned:**
- 

### Personal Goals

**Focus Area**: *Health / Learning / Relationships / Hobbies*

**This Week's Wins:**
- 

**Areas for Improvement:**
- 

---

## 📊 Time & Energy Analysis

### Time Allocation Breakdown

*Estimate percentage of time spent in each category*

| Category | % Time | Quality Rating (1-5) | Notes |
|----------|--------|----------------------|-------|
| Deep Work | | | |
| Meetings | | | |
| Admin/Email | | | |
| Learning | | | |
| Personal | | | |

> [!thought-experiment] Reflection Prompt
> If you could redistribute your time this week, what would you change?

### Energy Patterns

**Peak Productivity Times:**
- 

**Energy Drains Identified:**
- 

**Strategies for Next Week:**
- 

---

## 📚 Learning & Growth

### New Knowledge Acquired

> [!example] Key Concepts Learned
> - **[[Concept 1]]**: Brief description and why it matters
> - **[[Concept 2]]**: Brief description and source
> - **[[Concept 3]]**: Application or next step

### Skills Practiced

- **Skill**: [Context where practiced]
- **Skill**: [Context where practiced]

### Content Consumed

**Books/Articles Read:**
- [[Source 1]] - Key takeaway::
- [[Source 2]] - Key takeaway::

**Courses/Videos Completed:**
- 

---

## 🙏 Gratitude & Positive Moments

> [!helpful-tip] Gratitude Practice
> Research shows regular gratitude reflection improves well-being and life satisfaction.

**Three Things I'm Grateful For:**
1. 
2. 
3. 

**Meaningful Interactions:**
- 

**Small Wins to Celebrate:**
- 
- 
- 

---

## 🔄 Habit Tracking

| Habit | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Weekly Total |
|-------|-----|-----|-----|-----|-----|-----|-----|--------------|
| Morning routine | ✓ | | | | | | | /7 |
| Exercise | ✓ | | | | | | | /7 |
| Reading (30min) | ✓ | | | | | | | /7 |
| Meditation | ✓ | | | | | | | /7 |
| Deep work block | ✓ | | | | | | | /7 |

**Habit Insights:**
- 

---

## 📅 Week Ahead Planning

### Next Week's Focus

> [!important] Primary Intention
> *What is the ONE thing that would make next week successful?*

**Top 3 Priorities:**
1. 
2. 
3. 

### Scheduled Commitments

| Day | Commitment | Time | Prep Needed |
|-----|------------|------|-------------|
| Monday | | | |
| Tuesday | | | |
| Wednesday | | | |
| Thursday | | | |
| Friday | | | |

### Buffer & Recovery

**Planned Rest Time:**
- 

**Contingency Plans:**
- If energy is low: 
- If unexpected urgent work arrives: 

---

## 💭 Free Reflection Space

*Unstructured thoughts, feelings, or observations about the week*

---

## 🔗 Connected Reviews

- Previous Week: [[Week <% tp.frontmatter.week_number - 1 %> Review - <% tp.frontmatter.year %>]]
- Next Week: [[Week <% tp.frontmatter.week_number + 1 %> Review - <% tp.frontmatter.year %>]]
- Monthly Summary: [[<% moment(tp.date.now("YYYY-MM-DD")).format("YYYY-MM") %> Monthly Review]]
- Annual Review: [[<% tp.frontmatter.year %> Year in Review]]

---
*Review Completed: <% tp.date.now("YYYY-MM-DD HH:mm") %>*