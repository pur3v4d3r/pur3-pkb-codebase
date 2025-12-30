---
aliases:
  - How to Search
  - Search Help
  - Searching Help
  - Search Quick Reference
tags:
  - pkb
  - obsidian
---


# Search
Search is a [core plugin](https://help.obsidian.md/plugins) that helps you find data in your Obsidian vault by using search terms and operators to narrow down results.
By default, you can find Search in the left sidebar ( ![lucide-search.svg > icon](https://publish-01.obsidian.md/access/f786db9fac45774fa4f0d8112e232d67/Attachments/icons/lucide-search.svg) ). You can also open Search by pressing `Ctrl+Shift+F` (Windows/Linux) or `Command+Shift+F` (macOS).
- **Search selected text**: If you select text in the editor and open Search with the keyboard shortcut, Search shows you the search results for the selected text.
- **Search recent search terms**: Open Search with an empty search term to list recent search terms. Click any of them to use the search term again.
Excluded files
Files matching your [Excluded files](https://help.obsidian.md/settings#Excluded%20files) patterns will not appear in Search results.
## Search terms 
A search term is the word or phrase that you enter in the search field. Learning how to write search terms effectively can help you quickly find what you're looking for, even in large vaults. Obsidian only searches the contents of notes and canvases.
Searching paths and filenames
Each word in the search term is matched independently within each file. To search for an exact phrase, surround it with quotes, for example `"star wars"`. To search for quoted text within an exact phrase, you can _escape_ the quotes by adding a backslash (`\`) in front of the quote, for example `"they said \"hello\" to each other"`.
You can control whether to return files that contain _all_ the words in your search term, or _any_ of the words:
- `meeting work` returns files that contain both `meeting` and `work`.
- `meeting OR work` returns files that contain either `meeting` or `work`.
You can even combine the two in the same search term.
- `meeting work OR meetup personal` returns files for work meetings and personal meetups.
You can use parentheses to control the priority of each expression.
- `meeting (work OR meetup) personal` returns files that contain `meeting`, `personal`, and either `work` or `meetup`.
To exclude, or negate, a word from the search results, add a hyphen (`-`) in front of it:
- `meeting -work` returns files that contain `meeting` but not `work`.
You can exclude multiple expressions:
- `meeting -work -meetup` returns files that contain `meeting` but not `work` or `meetup`.
You can exclude a combination of expressions using parentheses:
- `meeting -(work meetup)` returns files that contain `meeting` but not _both_ `work` and `meetup`.
To filter results using the less than (`<`) and greater than (`>`) operators, surround them with square brackets (`[]`) or quotes (`""`):
- `meeting [duration:<5]` returns files where meeting is present, and duration is less than 5.
- `meeting [duration:>5]` returns files where meeting is present, and duration is greater than 5.
Explain search term
## Search operators 
Search operators enable more fine-grained search terms to filter your results even more.
Some operators even allow you to add a nested search term within parentheses, for example: `task:(call OR email)`.

|Search operator|Description|
|---|---|
|`file:`|Find text in filename. Matches any file in the vault.<br><br>Example: `file:.jpg` or `file:202209`.|
|`path:`|Find text in file path. Matches any file in the vault.<br><br>Example: `path:"Daily notes/2022-07"`.|
|`content:`|Find text in file content.<br><br>Example: `content:"happy cat"`.|
|`match-case:`|Case-sensitive match.<br><br>Example: `match-case:HappyCat`.|
|`ignore-case:`|Case-insensitive match.<br><br>Example: `ignore-case:ikea`.|
|`tag:`|Find tag in file.<br><br>Example: `tag:#work`.<br><br>Keep in mind that searching for `tag:#work` will not return results for `#myjob/work`.**Note**: Since `tag:` ignores matches in code blocks and in non-Markdown content, it's often faster and more accurate than a normal full-text search for `#work`.|
|`line:`|Find files that contain at least one line matching `x`.<br><br>Example: `line:(mix flour)`.<br><br>**Note:** Using `-line` negates the search, meaning it will find files where no line matches `x`.|
|`block:`|Find matches in the same block.<br><br>Example: `block:(dog cat)`.<br><br>**Note**: Since `block:` requires Search to parse the Markdown content in every file, it can cause your search term to take longer time to finish.|
|`section:`|Find matches in the same section (text between two headings).<br><br>Example: `section:(dog cat)`.|
|`task:`|Find matches in a [task](https://help.obsidian.md/syntax#Task%20lists) on a block-by-block basis.<br><br>Example: `task:call`.|
|`task-todo:`|Find matches in an _uncompleted_ [task](https://help.obsidian.md/syntax#Task%20lists) on a block-by-block basis.<br><br>Example: `task-todo:call`.|
|`task-done:`|Find matches in a _completed_ [task](https://help.obsidian.md/syntax#Task%20lists) on a block-by-block basis.<br><br>Example: `task-done:call`.|
## Search properties 
You can use data stored in [Properties](https://help.obsidian.md/properties) in your search terms.
Use brackets around a property name `[property]` to return files with that property:
- `[aliases]` returns files that contain the `aliases` property
Use brackets and a colon `[property:value]` to return files with that property and value:
- `[aliases:Name]` returns files where the `aliases` property value is `Name`
Use `null` as a value to find properties that have no value:
- `[aliases:null]` returns files where the `aliases` property exists but has no value
Empty values
The `null` operator works when a property is empty (e.g., `aliases:` ), but not when the property contains empty quotes (`""`) or empty brackets (`[]`).
Both property and value allow sub-queries, such as parentheses for grouping, the `OR` operator, double-quotes for exact matching, and regex.
- `[status:Draft OR Published]` returns files where the `status` property value is `Draft` or `Published`
## Change case sensitivity 
By default, search terms are not case sensitive. If you want to search for the exact case of your search term, select **Match case**  inside the search bar.
This setting can be toggled. If **Match case** icon is highlighted, that means you’re currently doing a case-sensitive search.
## Change result sort order 
1. Enter a [search term](https://help.obsidian.md/plugins/search#Search%20terms).
2. Under the search field, select the dropdown on the right.
3. Select the sort order you want. Default is "File name (A to Z)".
The following options are available:
- File name (A to Z)
- File name (Z to A)
- Modified time (new to old)
- Modified time (old to new)
- Created time (new to old)
- Created time (old to new)
## Copy search results 
1. Enter a [search term](https://help.obsidian.md/plugins/search#Search%20terms).
2. Under the search field, select the three dots icon next to the number of results.
3. Select **Copy search results**.
## Use regular expressions 
A regular expression is a set of characters that describe a text pattern. To use regular expressions in your search term, surround the expression with forward slashes (`/`).
- `/\d{4}-\d{2}-\d{2}/` matches an ISO 8601 date, such as 2022-01-01.
You can even combine regular expressions with search operators:
- `path:/\d{4}-\d{2}-\d{2}/` returns files with a date in the file path.
For more information on how to write regular expressions, refer to FreeCodeCamp's [Practical Regex guide](https://www.freecodecamp.org/news/practical-regex-guide-with-real-life-examples/) or Mozilla's [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).
JavaScript-flavored regular expressions
Regular expressions come in different flavors that may look different from each other. Obsidian uses JavaScript-flavored regular expressions.
## Configure search settings 
To configure Search, select **Search settings** ( ![lucide-sliders-horizontal.svg > icon](https://publish-01.obsidian.md/access/f786db9fac45774fa4f0d8112e232d67/Attachments/icons/lucide-sliders-horizontal.svg) ) on the right side of the search bar to see the toggles.

|Setting|Description|
|---|---|
|**Explain search term**|Breaks down the search terms and explains it in plain text.|
|**Collapse results**|Toggles whether to show the search context.|
|**Show more context**|Expands the search result to show more text around the match.|
## Embed search results in a note 
To embed search results in a note, add a `query` code block:
````
```query
embed OR search
```
````
[Obsidian Publish](https://help.obsidian.md/publish) doesn't support embedded [search results](https://help.obsidian.md/publish/limitations#Search). To see a live rendered example, use the code block above within your vault.
![search-query-rendered.png](https://publish-01.obsidian.md/access/f786db9fac45774fa4f0d8112e232d67/Attachments/search-query-rendered.png)
Links to this page
[Backlinks](https://help.obsidian.md/plugins/backlinks)
[Bookmarks](https://help.obsidian.md/plugins/bookmarks)
[Core plugins](https://help.obsidian.md/plugins)
[Drag and drop](https://help.obsidian.md/drag-and-drop)
[Embed files](https://help.obsidian.md/embeds)
[Glossary](https://help.obsidian.md/glossary)
[Graph view](https://help.obsidian.md/plugins/graph)
[Obsidian URI](https://help.obsidian.md/Extending+Obsidian/Obsidian+URI)
[Page preview](https://help.obsidian.md/plugins/page-preview)
[Properties](https://help.obsidian.md/properties)
[Properties view](https://help.obsidian.md/plugins/properties)
[Publish limitations](https://help.obsidian.md/publish/limitations)
[Settings](https://help.obsidian.md/settings)
[Tags](https://help.obsidian.md/tags)
[Tags view](https://help.obsidian.md/plugins/tags)