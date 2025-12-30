---
aliases:
  - Dataview Inline Queries Cheat Sheet
  - Dataview Inline Queries
  - Inline Queries Cheat Sheet
---


## 📋 Quick Reference Cheat Sheet

> [!quick-reference] Function Library

### Essential Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `length()` | Count items | `length(pages("#tag"))` |
| `sum()` | Add numbers | `sum(map(pages(), p => p.value))` |
| `average()` | Calculate mean | `average(map(pages(), p => p.rating))` |
| `min()` / `max()` | Find extremes | `max(map(pages(), p => p.score))` |
| `round()` | Round decimals | `round(3.14159, 2)` → 3.14 |
| `choice()` | Conditional | `choice(condition, true, false)` |
| `default()` | Fallback value | `default(this.field, "N/A")` |
| `join()` | Array to string | `join(this.tags, ", ")` |
| `split()` | String to array | `split(this.title, " ")` |
| `filter()` | Filter array | `filter(pages(), p => p.status = "active")` |
| `map()` | Transform array | `map(pages(), p => p.title)` |
| `flat()` | Flatten nested | `flat(map(pages(), p => p.tags))` |
| `contains()` | Check substring | `contains(this.title, "Project")` |
| `startswith()` / `endswith()` | String matching | `startswith(this.file.name, "2024")` |
| `regexmatch()` | Pattern match | `regexmatch("\\d+", this.code)` |
| `string()` | Type conversion | `string(this.number)` |
| `number()` | Parse number | `number(this.text)` |
| `date()` | Parse/create date | `date(today)`, `date("2024-11-23")` |
| `dur()` | Create duration | `dur(7 days)`, `dur(3 hours)` |
| `typeof()` | Type check | `typeof(this.field)` → "date" |

### Date Operations

| Operation | Syntax | Example |
|-----------|--------|---------|
| Today's date | `date(today)` | Current date |
| Specific date | `date("YYYY-MM-DD")` | `date("2024-11-23")` |
| Date difference | `(date2 - date1).days` | `(this.due - date(today)).days` |
| Add duration | `date + dur(X days)` | `date(today) + dur(7 days)` |
| Year component | `date.year` | `this.created.year` |
| Month component | `date.month` | `this.created.month` (1-12) |
| Day component | `date.day` | `this.created.day` |
| Weekday | `date.weekday` | `this.created.weekday` (1-7) |

### Common Metadata Fields

| Field           | Type   | Description                 |
| --------------- | ------ | --------------------------- |
| `file.name`     | Text   | Filename without extension  |
| `file.folder`   | Text   | Folder path                 |
| `file.path`     | Text   | Full file path              |
| `file.size`     | Number | Size in bytes               |
| `file.ctime`    | Date   | Creation timestamp          |
| `file.cday`     | Date   | Creation date (no time)     |
| `file.mtime`    | Date   | Last modification timestamp |
| `file.mday`     | Date   | Last modification date      |
| `file.tags`     | List   | All tags (including nested) |
| `file.inlinks`  | List   | Backlinks to this file      |
| `file.outlinks` | List   | Links from this file        |
| `file.aliases`  | List   | All aliases                 |
| `file.tasks`    | List   | All tasks in file           |
