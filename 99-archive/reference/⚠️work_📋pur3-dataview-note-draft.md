
> [!the-purpose]
> The **purpose** of this note is for me to *truly understand and learn* how to use **Dataview**.

> [!the-philosophy]
> I have tried to read various guides by Gemini and AI, but Im going to try this technique. Where *I will systematically go through the various resources* I have on dataview and *compile them in* **my own words here**. In the *hopes* that this will eventually be a reference note to place permanently in the [[PKB]].


# 🏗️Dataview Query

A Dataview Query consists of these following things:
- Exactly one Query Type: This determines the appearance or look of the final output from Dataview.
- None or One FROM statement: This is the location from which the Dataview Query, will pull its data.
- None to Multiple other Data Commands: These will help you filter, group, and sort your queries.



# Commands

**These commands are executed from Top to Bottom**

This is an Example of a dataview code block.
```
<QUERY-TYPE> [fields...]  
FROM <source>  
WHERE <condition>  
SORT <field>  
```

(⬆️)Above Query:

1. `FROM` (`Optional`) `Tells dataview where to pull notes from.`
	1. **Note:** `If you leave this out, ALL files in the vault will be used.`
2. `WHERE` (`Optional`) `This is your filter stop in the query.`
	1. `Dataview keeps the notes that match the set condition, and leaves the rest out.`
3. `SORT` (`Optional`) `Dataview receives the pages from `WHERE` and then organizes, or sorts, the notes using the preset conditions.`
4. `<QUERY TYPE>` (`Mandatory`) `After all the above (⬆️) has processed step by step, the query type receives the information and renders it out into the elected option.`

**Note:** The **above (⬆️) example shows** *why these queries need to be both written and run in a specific order* and *why it does not matter if you have more than one of the commands WHERE or GROUP.* They act as just another step in the processes.




| Category            | Link-to-Official-Documentation                                                                                                                                                                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Annotation/Metadata | - [[types-of-metadata]]<br>- [[add-metadata]]<br>- [[metadata-pages]]<br>- [[metadata-tasks]]                                                                                                                                                                                                                                                                 |
| Queries/DQL         | - [[data-commands]]<br>- [[query-types]]<br>- [[structure]]                                                                                                                                                                                                                                                                                                   |
| Reference           | - [[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_📑Dataview/01_Official-Documentation/Official/Reference/Expressions\|Expressions]]<br>- [[04_library/00_obsidian-documentation/02_Official-Documentation/02_⚫🔌Plugins/Plugin_📑Dataview/01_Official-Documentation/Official/Reference/Functions\|Functions]]<br>- [[literals]]<br>- [[sources]] |
| Other               | - [[Dataview_Cheat-Sheet]]<br>- [[Indexing]]                                                                                                                                                                                                                                                                                                                  |
















# Fields

- A **field** or **metadata field** is a `KEY` and a `VALUE`.
- There is **no limit** to the number of **fields** you can place inside a *Note*, *List Item*, or *Task*.
- A **Field** can be added to notes in **THREE** different ways. However, the way you go about adding them will change the appearance of them.

### Keys with Spaces or Capitalized Letters
Dataview will provide you with a **sanitized version** of the key.
### Keys with capitalized letters 
Can be used as-is, if you wish.


## Using **emojis** as metadata keys
When using **emojis in field names**, you **need to put them into square brackets**.
- **Note:** Also, be aware when switching the OS (I.e. Windows to Android), the same emoji could use another character code, and you might not find your metadata when querying it.

You are not limited to Latin characters when naming your metadata fields. You can use all characters available in UTF-8:
```markdown
Noel:: Christmas: A console game
[🎅:: a console game]
[xmas🎄:: a console game]
```

## YAML Frontmatter **Rules**


**Text**: Enclose values in "quotes" for clarity, though it's often not required. `title: "The Great Gatsby" ` 
**Numbers**: `rating: 5`
**Dates**: Must be in `ISO 8601 format (YYYY-MM-DD)` to be automatically recognized as a date object.
**Booleans**: `read: true`
**Lists** (**Arrays**): Can be written in two ways:
  1. **Inline:** genres:
  2. **Indented:** genres:
				 - Fiction 
				 - Classic
				 - Tragedy

## In-line Fields
**Note**: For writing in line fields inside a sentence you need to use square brackets[].
Dataview supports "inline" fields via a `Key:: Value` syntax that you can use everywhere in your file.

* **Inline Fields** excel at capturing *"in-band"* or *contextual metadata*. This is data that is an integral part of the content itself.
	* **Examples**: a due date on a task, a rating next to a movie title, or the location where a meeting took place.

```markdown
**The syntax for an inline field** is a key followed by a *double colon* (::) and *then the value*:
- Key:: Value

**Note**: For writing in line fiels inside of a sentence you need to use sqaure brackets[].
- "I just finished The Great Gatsby and thought it was fantastic. [rating:: 5]"
```

```markdown
If your **inline field** has an *own line, without any content beforehand*, you can write it like this:

Basic Field:: Some random Value
**Bold Field**:: Nice!

**All content after the** :: *is the value of the field until the next line break.*
```

### Embedding In-Line Fields

`If you want to embed metadata inside sentences, or multiple fields on the same line, you can use the bracket syntax and wrap your field in square brackets:`

```markdown
I would rate this a [rating:: 9]! It was [mood:: acceptable].
```

`There is also the alternative parenthesis syntax, which hides the key when rendered in Reader mode:`

```markdown
This will not show the (longKeyIDontNeedWhenReading:: key).
```

`It will render to:`

```markdown
This will not show the key.
```

> [!info]
> When you want to *annotate a list item*, e.g., a task, with metadata, you *always need to use* the **bracket syntax**. *(Because the field is not the only information in this line.)* **Bracketed inline fields** are the only way to explicitly add fields to specific list items, **YAML frontmatter** *always applies to the whole page*. (but is also available in context of list items.)

## Implicit fields
 


Some *examples* for **implicit fields** are:

- Day the file was created `file.cday`
- Links in the file `file.outlinks`
- Tags in the file `file.etags`
- All list items in the file `file.lists and file.tasks`

 Available implicit fields differ depending on if you look at a page or a list item. Find the full list of available implicit fields on [Metadata on pages](metadata-pages.md) and [Metadata on Tasks and Lists](metadata-tasks.md) and **below (⬇️)**.

### Comprehensive In-Line Field Reference Table
 
The table below (⬇️) Is a comprehensive reference for all the **Implicit Fields**, their **data types** and a **description** of the data they provide.

| Field Name         | Data Type        | Description                                                                                          |
| :----------------- | :--------------- | :--------------------------------------------------------------------------------------------------- |
| `file.name`        | `Text`           | `The file's name, without the .md extension`.                                                        |
| `file.folder`      | `Text`           | ``The path to the folder containing the file.``                                                      |
| `file.path`        | `Text`           | `The full path to the file, including its name.`                                                     |
| `file.ext`         | `Text`           | `The file extension, typically md.`                                                                  |
| `file.link`        | `Link`           | `A clickable link to the file.`                                                                      |
| `file.size`        | `Number`         | `The size of the file in bytes.`                                                                     |
| `file.ctime`       | `Date with Time` | `The date and time the file was created.`                                                            |
| `file.cday`        | `Date`           | `The date the file was created (time part is ignored).`                                              |
| `file.mtime`       | `Date with Time` | `The date and time the file was last modified.`                                                      |
| `file.mday`        | `Date`           | `The date the file was last modified (time part is ignored).`                                        |
| `file.tags`        | `List`           | `A list of all tags in the note. Subtags are broken down (e.g., \#A/B/C becomes \`\`).`              |
| `file.etags`       | `List`           | `A list of all explicit tags in the note. Subtags are not broken down (e.g., \#A/B/C remains \`\`).` |
| `file.inlinks`     | `List`           | `A list of links from other files pointing to this file.`                                            |
| `file.outlinks`    | `List`           | `A list of links from this file pointing to other files.`                                            |
| `file.aliases`     | `List`           | `A list of all aliases defined in the file's YAML frontmatter.`                                      |
| `file.tasks`       | `List`           | `A list of all tasks (- \[ \]...) within the file.`                                                  |
| `file.lists`       | `List`           | `A list of all list elements (including tasks) in the file.`                                         |
| `file.frontmatter` | `Object`         | `An object containing the raw key-value pairs from the YAML frontmatter.`                            |
| `file.day`         | `Date`           | `A date object if the file's name contains a date in YYYY-MM-DD or YYYYMMDD format.`                 |
| `file.starred`     | `Boolean`        | `Returns true if the file has been bookmarked using the core "Bookmarks" plugin.`                    |



# Tasks and Dataview
## Tasks Field Shorthands

The [Tasks](https://publish.obsidian.md/tasks/Introduction) plugin introduced a different [notation by using Emoji](https://publish.obsidian.md/tasks/Reference/Task+Formats/Tasks+Emoji+Format) to configure the different dates related to a task. In the context of Dataview, this notation is called (Field Shorthands).

`The current version of Dataview only support the dates shorthands as shown below. The priorities and recurrence shorthands are not supported.``

### Example

    - [ ] Due this Saturday 🗓️2021-08-29
    - [x] Completed last Saturday ✅2021-08-22
    - [ ] I made this on ➕1990-06-14
    - [ ] Task I can start this weekend 🛫2021-08-29
    - [x] Task I finished ahead of schedule ⏳2021-08-29 ✅2021-08-22

There are two specifics to these emoji-shorthands.

First, they omit the inline field syntax (no [🗓️:: YYYY-MM-DD] needed) and secondly, they map to a **textual** field name data-wise:

| Field name | Short hand syntax |
| ---------- | ----------------- |
| due | `🗓️YYYY-MM-DD` |
| completion |  `✅YYYY-MM-DD` |
| created | `➕YYYY-MM-DD` |
| start | `🛫YYYY-MM-DD` |
| scheduled | `⏳YYYY-MM-DD` |

This means if you want to query for all tasks that are completed 2021-08-22, you'll write:

~~~markdown
```dataview
TASK
WHERE completion = date("2021-08-22")
```
~~~

Which will list both variants - shorthands and textual annotation:

```markdown
- [x] Completed last Saturday ✅2021-08-22
- [x] Some Done Task [completion:: 2021-08-22]
```

### Tasks and Lists Fields

Just like pages, you can also add **fields** on list item and task level to bind it to a specific task as context. For this you need to use the [inline field syntax](add-metadata.md#inline-fields):

```markdown
- [ ] Hello, this is some [metadata:: value]!
- [X] I finished this on [completion:: 2021-08-15].
```

Tasks and list items are the same data wise, so all your bullet points have all the information described here available, too.






















# Queries
[[Dv-Dql-Basic-Syntax]]




## `From` — Sourcing Your Data

The `FROM` **command or statement** *determines the location of which Dataview's query will pull data.* Which is then passed on to the next command in sequence and so on.

The **sources** you can currently select from are: 
1. **The entire Vault** ([[PKB]]): To search your entire Vault *use*: `""`
2. **Folders**: To select from a folder (and all of its sub-folders) *use*: `FROM "folder"`
3. **Single Files**: To select a single file *use*: `FROM path/to/file`
4. **Tags**: to select from a tag (and all of its sub-tags) *use*: `FROM #tag`
5. **Incoming/Outgoing links**: You can either select link that go **TO** a file or all the links **FROM** a file.
	1. To obtain all the links going TO `[[NOTE]]` *use*: `FROM [[NOTE]]`
	2. To obtain all the notes that link FROM `[[NOTE]]` *use*: `FROM outgoing([[note]])`
		- **Note**: This means all the links **IN** that file.

*A way to customize your query further is to add in Boolean operators.*
**For Example**:
	- `#tag and "folder"` will give you back all the notes in `"folder"` with the tag `#tag`.
	- `[[FOOD]] or [[EXCERCISE]]` will return any pages that link TO `[[FOOD]]` or `[[EXCERCISE]]`.

You can also **negate** (*choose to omit*) *sources* that **DO NOT** match the given *source*, *use*: `-`.
For Example:
	- `-#tag` will *exclude all* the file that have the given `#tag` in them.
	- `#tag or -"folder"` will *only include* `#tag` that are **NOT** in the `"folder"`.
 
### Links
- [[data-commands#FROM Commands-FROM|Link to the Documentation on the FROM command.]]
- [[sources]]

|          | Link-to-Official-Documentation  |
| -------- | ------------------------------- |
| Beginner | - <br>- <br>- <br>- <br>-       |
| Advanced | - <br>- <br>- <br>- <br>- <br>- |

## `Where` — Filtering and Refining


|          | Link-to-Official-Documentation   |
| -------- | -------------------------------- |
| Beginner | - <br>- <br>- <br>- <br>-        |
| Advanced | - <br>- <br>- <br>- <br>- <br>-  |


## `SORT` and `LIMIT` — Ordering and Organizing
[[Dv-Dql-Sorting]]

|          | Link-to-Official-Documentation   |
| -------- | -------------------------------- |
| Beginner | - <br>- <br>- <br>- <br>-        |
| Advanced | - <br>- <br>- <br>- <br>- <br>-  |


## `GROUP`, `GROUP BY`, and `FLATTEN` — Advanced Data Shaping


|          | Link-to-Official-Documentation   |
| -------- | -------------------------------- |
| Beginner | - <br>- <br>- <br>- <br>-        |
| Advanced | - <br>- <br>- <br>- <br>- <br>-  |


## List


|          | Link-to-Official-Documentation |
| -------- | ------------------------------ |
| Beginner | -                              |
| Advanced | -                              |
| Other    | -[[Basic-List-Queries]]        |


## Table



|          | Link-to-Official-Documentation                                                                                                                  |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Beginner | - [[Dv-Dql-Basic-Syntax]]<br>- [[Dv-Dql-Sorting]]<br>- [[Dv-Dql-Table-Any-Contains]]<br>- [[Dv-Dql-Table-Filter]]<br>- [[Dv-Dql-Table-Flatten]] |
| Advanced | - [[Dv-Dql-Table-Lists-Manipulation]]<br>- [[Dv-Dql-Table-With-Tasks]]                                                                          |
| Other    | - [[Basic-Table-Queries]]                                                                                                                       |




## Task



|          | Link-to-Official-Documentation                            |
| -------- | --------------------------------------------------------- |
| Beginner | - [[Dv-Dql-Task-Any-Contains]]<br>- [[Dv-Dql-Task-Query]] |
| Advanced | - [[Dv-Dql-Table-With-Tasks]]                             |
| Other    | - [[Basic-Task-Queries]]                                  |



## Calendar
[[Basic-Calendar-Queries]]

|          | Link-to-Official-Documentation   |
| -------- | -------------------------------- |
| Beginner | - <br>- <br>- <br>- <br>-        |
| Advanced | - <br>- <br>- <br>- <br>- <br>-  |


## In-Line
[[Basic-Inline-Queries]]

|          | Link-to-Official-Documentation  |
| -------- | ------------------------------- |
| Beginner | - <br>- <br>- <br>- <br>-       |
| Advanced | - <br>- <br>- <br>- <br>- <br>- |






















---

---

---

---

---

---


# Fields, What are they?

























## In-Line Fields

An option for those who would prefer a less intrusive, or just a different "*In-Note*" way of inserting metadata directly into the note body itself. **In-Line Fields** is your go to. *These consist of* `KEY:: VALUE` *syntax* that is usable through the *entirety of the note*. This allows you to write queryable data directly into your notes, or even into a sentence.

**In-Line Fields** excel at capturing what is considered "contextual metadata". This would be data that is considered integral, or part of the content itself. Some examples would be a due date on a task, a rating for a movie or book.

When writing **In-Line Fields** without content beforehand (↩️) you can write them like this.

(⬇️)
 
`This is an example of a KEY`:: `and then this would be the example for the VALUE.`

>[!important] **(⬆️) Note** *the space after the `::`, it must be written this way. **No space** after `KEY` and **one space** before the `VALUE` portion of the* **In-Line Field**.
>
> - Also, note that **all** the content after the `::` **until** the **next line break** is considered to be the `VALUE`.
>  
> - When you need to embed an **In-Line Field** or use **multiple in one line**, use the *bracket syntax and wrap the fields in square brackets*.
>   

```
- Example of **square bracket** being used to wrap **In-Line Fields** in a sentence.

	- "I would rate this a [rating:: 9]! It was [mood:: acceptable]."

```

> [!helpful-tip] `Mind the` `::`
> **Pro-Tip:** `You need to use a double colon` `::` `between key and value when using inline fields, contrary to YAML Frontmatter fields where one colon is enough.`

`There is also an option, less obvious looking that is, way to have the In-Line Filed appear while in reading mode. Simply wrap the entire filed in parentheses ().`













[[Basic-Inline-Queries]] `- Link to Official Documentation`
# YAML Frontmatter

[Types-of-Metadata](types-of-metadata.md) `<Link to Official Documentation.`

### Example of YAML Frontmatter
```yaml
    ---
    alias: "document"
    last-reviewed: 2021-08-17
    thoughts:
      rating: 8
      reviewable: false
    ---
```

Take note that each of the **fields** in the example above (⬆️) has a *different data type*
- `alias` When information is wrapped in **(`""`)** it is *considered by Dataview* as **text**.
- `last-reviwed` This is obviously a **date** because it follows the standard *ISO format*.
- `thoughts` Is simply a filed, becuse it uses YAML Frontmatter Syntax

**This (⬇️) is an example of Query for this Frontmatter.**
~~~
```dataview
LIST
WHERE thoughts.rating = 8
```
~~~
*Notice how, already, it's become easier to understand.*

**YAML Frontmatter Data Types**
- `Text` Always try to enclose these values with **quotes** for clarity purposes.
	- *Though often not a requirement*
- `Numbers` Example: `rating: 5`
- Dates For Dataview to automatically register, these **must be** in the standard **ISO 8601 format**. (I.e., [[2025-10-15]])
- `Booleans` Example: `read: true`
- Lists or Arrays You have two options when writing these.
	1. `Inline` Example: `genres: Fiction`
	2. `Indented` Example: `genres:`
								`1. Fiction`
								`2. Classic`
								`3. Tragedy`






# Dataview Query Language (D.Q.L)

## Query Types

### Links
- [[query-types]]

## List






### Links
- [[query-types#LIST Query-Type-LIST|Link to the LIST, Official Note section.]]

## Table




### Links
- [[query-types#TABLE Query-Type-TABLE|Link to the TABLE, Official Note section.]]

## Task




### Links
- [[query-types#TASK Query-Type-TASK|Link to the TASK, Official Note section.]]

## Calendar





### Links
- [[query-types#CALENDAR Query-Type-Calendar|Link to the CALENDAR, Official Note section.]]

# Calculations and Functions








# Java and Dataview — Unleash the Full Potential of this Plugin

























# End of Document Link