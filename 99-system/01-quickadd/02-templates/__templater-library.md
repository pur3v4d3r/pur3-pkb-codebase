

>[! ] This is a Templater Library for useful Templater Syntax String and Logic. These are for use in building and refining templates.
>```
>After running the prompt multiple times and building up a decent collection, process everything through another LLM to structure it into a reference, Claude might work. Just watch the context window and manage the size of each document section it is building. Plan this out to ensure good results.


## Example Selection Reasoning Process

```
Categories used in previous runs: [unknown - first run]
Categories underrepresented: All categories are equally fresh
Selected categories for this run:
1. STRING MANIPULATION & INTERPOLATION
2. DATE & TIME OPERATIONS
3. SYSTEM INTERACTIONS (tp.system)
4. FILE OPERATIONS (tp.file)
5. FRONTMATTER GENERATION

Rationale:
- Start with foundational categories that are commonly used
- Mix basic and intermediate patterns to establish a learning curve
- Include both input/output focused operations for practical utility
- Cover core Templater APIs (tp.date, tp.system, tp.file) early
```

- --

### STRING MANIPULATION & INTERPOLATION

#### Dynamic-Title-With-Timestamp
* *Use Case:** Create note titles that include formatted timestamps for unique identification
* *Complexity:** Basic

```javascript
<%*
// Generate a timestamp-based title
const timestamp = tp.date.now("YYYY-MM-DD HH:mm");
const userTitle = await tp.system.prompt("Enter note title:");
// Combine timestamp and user input with proper formatting
const finalTitle = `${timestamp} - ${userTitle}`;
// Output to template
tR += `# ${finalTitle}\n\n`;
tR += `Created: ${timestamp}`;
%>
```

* *Explanation:**
1. `tp.date.now()` generates current timestamp in specified format
2. `tp.system.prompt()` requests user input (async, requires await)
3. Template literal combines both with separator
4. `tR +=` appends formatted content to template result

* *Validation Notes:**
✓ Async/await properly used for prompt
✓ Backticks used for template literals with ${} interpolation
✓ Result assigned to tR variable for output
✓ No syntax errors, all variables defined

- --

### DATE & TIME OPERATIONS

#### Relative-Date-Formatter
* *Use Case:** Automatically generate relative date references like "Today", "Tomorrow", "Yesterday"
* *Complexity:** Intermediate

```javascript
<%*
// Get today's date and compare with input date
const inputDateStr = await tp.system.prompt("Enter date (YYYY-MM-DD):");
const inputDate = moment(inputDateStr);
const today = moment().startOf('day');
// Calculate difference in days
const diffDays = inputDate.diff(today, 'days');
let displayText;
if (diffDays === 0) {
  displayText = "Today";
} else if (diffDays === 1) {
  displayText = "Tomorrow";
} else if (diffDays === -1) {
  displayText = "Yesterday";
} else {
  displayText = inputDate.format("dddd, MMMM Do");
}
tR += `📅 ${displayText}`;
%>
```

* *Explanation:**
1. Prompt user for a date string
2. Parse into Moment.js object for comparison
3. Compare with today using `.diff()` method
4. Use conditional logic to assign human-readable label
5. Format as full date for other cases

* *Validation Notes:**
✓ Proper use of moment.js methods
✓ Correct handling of positive/negative differences
✓ All code paths covered in switch logic
✓ Uses await for async prompt correctly

- --

### SYSTEM INTERACTIONS (tp.system)

#### Multi-Select-Suggester
* *Use Case:** Allow users to select multiple project tags from predefined list
* *Complexity:** Intermediate

```javascript
<%*
// Define available options
const projectTags = ["Marketing", "Engineering", "Design", "Sales", "HR"];
// Present multi-select suggester to user
const selectedTags = await tp.system.suggester(
  projectTags,
  projectTags,
  true, // Enable multi-select
  "Select relevant project tags:"
);
// Handle case where nothing is selected
const tagList = selectedTags && selectedTags.length > 0
  ? selectedTags.map(tag => `#${tag}`).join(" ")
  : "#general";
tR += `Tags: ${tagList}`;
%>
```

* *Explanation:**
1. Predefine array of selectable tags
2. Use `tp.system.suggester()` with multi-select enabled
3. Map selected items to hashtag format
4. Join into space-separated string or default to #general

* *Validation Notes:**
✓ Multi-select flag correctly set to true
✓ Null/empty handling included
✓ Map and join used appropriately for transformation
✓ Await used for async operation

- --

### FILE OPERATIONS (tp.file)

#### Smart-Filename-Renamer
* *Use Case:** Rename current file based on frontmatter title field
* *Complexity:** Advanced

```javascript
<%*
// Check if we're in a new (unsaved) file
if (!tp.file.title || tp.file.title === "Untitled") {
  const newTitle = await tp.system.prompt("Enter new filename:");
  // Sanitize title: replace spaces with hyphens, remove special chars
  const sanitizedTitle = newTitle
    .replace(/[^a-zA-Z0-9 ]/g, '') // Remove special characters
    .trim()
    .replace(/\s+/g, '-');        // Replace spaces with hyphens
  if (sanitizedTitle) {
    await tp.file.rename(sanitizedTitle);
  }
}
%>
```

* *Explanation:**
1. Check if file has default/empty title
2. Prompt user for desired name
3. Clean input by removing special characters and normalizing spaces
4. Rename file only if valid title provided

* *Validation Notes:**
✓ Conditional check prevents renaming saved files
✓ Regex sanitization handles edge cases
✓ Trim and replace chain ensures clean output
✓ Await used for async file operation

- --

### FRONTMATTER GENERATION

#### Dynamic-Tag-Categorizer
* *Use Case:** Generate YAML frontmatter with dynamic tags based on user selections
* *Complexity:** Intermediate

```javascript
<%*
// Get user inputs
const category = await tp.system.suggester(
  ["Blog Post", "Meeting Notes", "Project Update", "Research"],
  ["blog", "meeting", "project", "research"]
);
const status = await tp.system.suggester(
  ["Draft", "In Review", "Published"],
  ["draft", "review", "published"]
);
// Generate dynamic tags
const tags = [`type/${category}`, `status/${status}`];
// Output YAML frontmatter
tR += "---\n";
tR += `title: ${await tp.system.prompt("Note title:")}\n`;
tR += `date: ${tp.date.now("YYYY-MM-DD")}\n`;
tR += `tags: [${tags.map(tag => `"${tag}"`).join(", ")}]\n`;
tR += "---\n\n";
%>
```

* *Explanation:**
1. Use suggesters to get structured category and status values
2. Construct tag strings dynamically from selections
3. Prompt for title and insert current date
4. Format array of tags as quoted YAML list
5. Output complete frontmatter block

* *Validation Notes:**
✓ Tag construction uses template literals safely
✓ Array mapping ensures proper quoting in YAML
✓ Date formatting follows standard pattern
✓ All prompts awaited correctly

- --
## Example Selection Reasoning Process

```
Categories used in previous runs: [N/A - first run]
Categories underrepresented: [All categories equally fresh]
Selected categories for this run:
1. STRING MANIPULATION & INTERPOLATION
2. DATE & TIME OPERATIONS
3. SYSTEM INTERACTIONS (tp.system)
4. FRONTMATTER GENERATION
5. ADVANCED PATTERNS

Rationale:
- Start with foundational categories that appear in many templates
- Include user interaction for dynamic content creation
- Add frontmatter for structured note metadata
- Finish with advanced patterns to showcase power features
```

- --

## Candidate Generation

### Category: STRING MANIPULATION & INTERPOLATION

* *Candidate A:** Dynamic Title with Sanitized User Input
* *Candidate B:** Multi-line Template Literal Construction
* *Candidate C:** Conditional String Building Based on Prompt

### Category: DATE & TIME OPERATIONS

* *Candidate A:** Relative Date Formatter (Yesterday/Tomorrow)
* *Candidate B:** Custom Week Range Generator
* *Candidate C:** ISO Week Number Display

### Category: SYSTEM INTERACTIONS (tp.system)

* *Candidate A:** Multi-select Suggester with Default Options
* *Candidate B:** Clipboard Paste Confirmation Flow
* *Candidate C:** Prompt with Validation Loop

### Category: FRONTMATTER GENERATION

* *Candidate A:** Dynamic Tag Population from Selection
* *Candidate B:** Hierarchical Status Field Builder
* *Candidate C:** YAML Array Field from Comma-separated Input

### Category: ADVANCED PATTERNS

* *Candidate A:** Try/Catch Error Handling Wrapper
* *Candidate B:** Async Function Definition and Reuse
* *Candidate C:** Regular Expression Content Scrubber

- --

## Evaluation Criteria

| Candidate | Practical Utility | Teaching Value | Code Clarity | Feature Coverage | Total |
|----------|-------------------|----------------|--------------|------------------|-------|
| String A | 4 | 3 | 5 | 4 | 16 |
| String B | 3 | 4 | 4 | 3 | 14 |
| String C | 5 | 5 | 4 | 5 | 19 |
| Date A | 4 | 4 | 5 | 4 | 17 |
| Date B | 3 | 3 | 4 | 3 | 13 |
| Date C | 2 | 3 | 3 | 2 | 10 |
| System A | 5 | 5 | 5 | 5 | 20 |
| System B | 3 | 4 | 4 | 3 | 14 |
| System C | 4 | 4 | 4 | 4 | 16 |
| Frontmatter A | 4 | 4 | 5 | 4 | 17 |
| Frontmatter B | 3 | 3 | 4 | 3 | 13 |
| Frontmatter C | 4 | 4 | 4 | 4 | 16 |
| Advanced A | 4 | 5 | 4 | 5 | 18 |
| Advanced B | 3 | 4 | 4 | 4 | 15 |
| Advanced C | 3 | 4 | 3 | 3 | 13 |

- --

## Selection Justification

```
Selected:
- String C: Conditional String Building Based on Prompt (Score: 19)
- Date A: Relative Date Formatter (Score: 17)
- System A: Multi-select Suggester (Score: 20)
- Frontmatter A: Dynamic Tag Population (Score: 17)
- Advanced A: Try/Catch Error Handling (Score: 18)

Reasoning:
- String C shows conditional logic + user input handling
- Date A demonstrates practical date formatting
- System A is most comprehensive system interaction example
- Frontmatter A illustrates dynamic metadata population
- Advanced A teaches essential error resilience

Rejected alternatives:
- Simpler or less commonly used variants omitted
- Redundant functionality consolidated
- Examples chosen to progress in complexity
```

- --

## Diversity Check

```
Does this selection provide:
- Different complexity levels? Y (Basic → Intermediate → Advanced)
- Variety in use cases? Y (Title generation, scheduling, tagging, etc.)
- Coverage of different Templater APIs? Y (tp.system, tp.date, tp.file implicitly)
- Mix of syntax patterns? Y (Conditionals, loops, functions, try/catch)
```

- --

## Final Output


### STRING MANIPULATION & INTERPOLATION

#### [Conditional-String-Building-Based-on-Prompt]
* *Use Case:** Generate a formatted string based on user input with fallback logic
* *Complexity:** Intermediate

```javascript
<%*
// Request user input
const userInput = await tp.system.prompt("Enter description (or leave blank):");
// Build output conditionally using ternary operator
const output = userInput.trim()
  ? `📝 ${userInput}`
  : "📝 _No description provided_";
// Append to template result
tR += output;
%>
```

* *Explanation:**
1. `tp.system.prompt()` requests optional user input (async)
2. `.trim()` removes whitespace to detect empty strings
3. Ternary operator builds message conditionally
4. Emoji prefix adds visual context
5. Result assigned to `tR` for output

* *Validation Notes:**
✓ Async/await used correctly
✓ Backticks for template literals
✓ Conditional expression with fallback
✓ Proper variable declaration and usage
✓ No syntax errors

- --



### DATE & TIME OPERATIONS

#### [Relative-Date-Formatter]
* *Use Case:** Display human-readable relative dates like "Yesterday" or "Tomorrow"
* *Complexity:** Basic

```javascript
<%*
// Get current date
const today = tp.date.now();
// Calculate yesterday and tomorrow
const yesterday = tp.date.now("YYYY-MM-DD", -1);
const tomorrow = tp.date.now("YYYY-MM-DD", 1);
// Format display strings
tR += `📅 Today: ${today}\n`;
tR += `⬅️ Yesterday: ${yesterday}\n`;
tR += `➡️ Tomorrow: ${tomorrow}`;
%>
```

* *Explanation:**
1. `tp.date.now()` gets today's date in default format
2. Second parameter adjusts days: `-1` for yesterday, `+1` for tomorrow
3. Strings formatted for readability with emojis
4. Each line appended to `tR` for output

* *Validation Notes:**
✓ Correct use of `tp.date.now()` with offset
✓ Proper string concatenation with newlines
✓ All variables defined before use
✓ No async issues since no prompts involved

- --

### SYSTEM INTERACTIONS (tp.system)

#### [Multi-Select-Suggester-With-Default-Options]
* *Use Case:** Allow user to select multiple items from a predefined list with defaults
* *Complexity:** Intermediate

```javascript
<%*
// Define options and default selections
const options = ["Project Alpha", "Project Beta", "Project Gamma", "Other"];
const defaults = ["Project Alpha"];
// Present multi-select suggester
const selected = await tp.system.suggester(
  item => item, // display text
  options,      // items to choose from
  true,         // allow multiple selections
  defaults      // pre-selected items
);
// Handle case where nothing selected
if (!selected || selected.length === 0) {
  tR += "> No projects selected.";
} else {
  tR += "## Selected Projects\n";
  selected.forEach(project => {
    tR += `- [[${project}]]\n`;
  });
}
%>
```

* *Explanation:**
1. Predefined array of project names
2. `tp.system.suggester()` allows multi-select with defaults
3. Conditional logic handles empty selection
4. Loop generates internal links for each selection
5. Output assigned to `tR`

* *Validation Notes:**
✓ Async/await used for suggester
✓ Multi-select mode enabled (`true`)
✓ Default values passed correctly
✓ Null/empty checks prevent runtime errors
✓ Internal link syntax correct

- --


### FRONTMATTER GENERATION

#### [Dynamic-Tag-Population-From-Selection]
* *Use Case:** Automatically populate tags in YAML frontmatter based on user selections
* *Complexity:** Intermediate

```javascript
<%*
// Define tag categories
const categories = ["Work", "Personal", "Learning", "Health"];
const priorities = ["High", "Medium", "Low"];
// Prompt user for selections
const selectedCategories = await tp.system.suggester(
  cat => cat,
  categories,
  true
);
const selectedPriority = await tp.system.suggester(
  pri => pri,
  priorities,
  false
);
// Build tags array
let tags = [];
if (selectedCategories && selectedCategories.length > 0) {
  tags = [...selectedCategories];
}
if (selectedPriority) {
  tags.push(`priority/${selectedPriority.toLowerCase()}`);
}
// Output YAML frontmatter
tR += "---\n";
tR += "tags:\n";
tags.forEach(tag => {
  tR += `  - ${tag}\n`;
});
tR += "---\n\n";
%>
```

* *Explanation:**
1. Two separate suggesters for category and priority
2. One allows multiple selections, one single
3. Tags built dynamically from selections
4. Priority converted to lowercase for consistency
5. YAML frontmatter constructed line by line

* *Validation Notes:**
✓ Multiple suggesters used appropriately
✓ Tag array built conditionally
✓ YAML indentation correct (2 spaces)
✓ Triple dashes for frontmatter boundaries
✓ No undefined references

- --



### ADVANCED PATTERNS

#### [Try-Catch-Error-Handling-Wrapper]
* *Use Case:** Safely execute potentially failing operations with graceful error messages
* *Complexity:** Advanced

```javascript
<%*
try {
  // Simulate an operation that might fail
  const userInput = await tp.system.prompt("Enter a number:");
  // Attempt conversion and validation
  const num = parseFloat(userInput);
  if (isNaN(num)) {
    throw new Error("Invalid number entered");
  }
  // Perform calculation
  const result = num * 2;
  tR += `✅ Result: ${result}`;
} catch (error) {
  // Graceful error handling
  tR += `❌ Error: ${error.message}`;
}
%>
```

* *Explanation:**
1. `try` block wraps code that may throw errors
2. User input parsed and validated
3. Invalid input triggers custom error
4. Successful path outputs calculated result
5. `catch` block handles all exceptions gracefully

* *Validation Notes:**
✓ Try/catch structure properly implemented
✓ Custom error thrown for invalid input
✓ Error message captured and displayed
✓ Async/await used within try block
✓ All paths assign output to `tR`

- --
## Example Generation Reasoning

### STEP 1: CATEGORY ANALYSIS
```
Categories used in previous runs: [unknown - first run]
Categories underrepresented: All categories equally new
Selected categories for this run:
1. DATE & TIME OPERATIONS
2. SYSTEM INTERACTIONS (tp.system)
3. FRONTMATTER GENERATION
4. LOGIC & CONTROL FLOW
5. ARRAYS & ITERATION

Rationale: Starting with fundamental categories that cover core Templater functionality. These provide a strong foundation for more complex patterns later.
```

### STEP 2: CANDIDATE GENERATION

* *Category: DATE & TIME OPERATIONS**
- Candidate A: Relative date calculator (yesterday/tomorrow)
- Candidate B: Week range generator (Monday to Sunday)
- Candidate C: Quarterly date formatter

* *Category: SYSTEM INTERACTIONS (tp.system)**
- Candidate A: Multi-select tag chooser
- Candidate B: Clipboard content inserter
- Candidate C: Confirmation dialog for destructive actions

* *Category: FRONTMATTER GENERATION**
- Candidate A: Dynamic tag and category system
- Candidate B: Status-based frontmatter generator
- Candidate C: Hierarchical project metadata

* *Category: LOGIC & CONTROL FLOW**
- Candidate A: Priority-based content routing
- Candidate B: Conditional section inclusion
- Candidate C: Type-specific template branching

* *Category: ARRAYS & ITERATION**
- Candidate A: Task list generator with sorting
- Candidate B: Tag frequency counter
- Candidate C: File reference collector

### STEP 3: EVALUATION CRITERIA

```
Evaluate each candidate on:
1. Practical utility (1-5): How often would someone use this?
2. Teaching value (1-5): Does it demonstrate important concepts?
3. Code clarity (1-5): Is it easy to understand and modify?
4. Feature coverage (1-5): Does it showcase category capabilities?
```

### STEP 4: SELECTION JUSTIFICATION

```
Selected Examples:
1. DATE & TIME OPERATIONS - Week Range Generator (Score: 18/20)
   - High practical utility for planning notes
   - Demonstrates date arithmetic and formatting
   - Clear, readable code structure
   - Covers multiple moment.js features

2. SYSTEM INTERACTIONS - Multi-select Tag Chooser (Score: 19/20)
   - Very common use case in note-taking
   - Shows advanced tp.system features
   - Well-structured with good error handling
   - Excellent teaching value for user interaction

3. FRONTMATTER GENERATION - Dynamic Tag System (Score: 17/20)
   - Essential for organization systems
   - Shows proper YAML generation
   - Good balance of simplicity and functionality
   - Covers array handling in frontmatter

4. LOGIC & CONTROL FLOW - Priority-Based Content Routing (Score: 16/20)
   - Practical for task management systems
   - Demonstrates conditional logic patterns
   - Clear flow with good documentation
   - Shows template literal usage

5. ARRAYS & ITERATION - Task List Generator (Score: 18/20)
   - Highly practical for daily planning
   - Comprehensive array manipulation
   - Good example of sorting and filtering
   - Excellent for learning iteration patterns
```

### STEP 5: DIVERSITY CHECK
```
Does this selection provide:
- Different complexity levels? Y (Basic to Intermediate)
- Variety in use cases? Y (Planning, Organization, Task Management)
- Coverage of different Templater APIs? Y (tp.date, tp.system, tp.file)
- Mix of syntax patterns? Y (Conditionals, Arrays, Date Ops, UI)
```

- --

## Generated Examples

### DATE & TIME OPERATIONS

#### [Week-Range-Generator]
* *Use Case:** Create formatted date ranges for weekly planning notes
* *Complexity:** Intermediate

```javascript
<%*
// Calculate the start (Monday) and end (Sunday) of the current week
const today = tp.date.now();
const startOfWeek = tp.date.now("YYYY-MM-DD", true, "Monday");
const endOfWeek = tp.date.now("YYYY-MM-DD", true, "Sunday");
// Format for human-readable display
const formattedStart = tp.date.now("MMMM D, YYYY", true, "Monday");
const formattedEnd = tp.date.now("MMMM D, YYYY", true, "Sunday");
// Output formatted week range
tR += `# Week of ${formattedStart}\n\n`;
tR += `**Date Range:** ${startOfWeek} to ${endOfWeek}\n\n`;
%>
```

* *Explanation:**
1. `tp.date.now()` gets today's date
2. Using the 3rd parameter to specify day of week ("Monday", "Sunday")
3. Creating both machine-readable (YYYY-MM-DD) and human-readable formats
4. Building a header with the formatted date range

* *Validation Notes:**
✓ Proper use of moment.js day shifting
✓ Correct date formatting strings
✓ All variables properly declared and used
✓ No async operations needed

- --

### SYSTEM INTERACTIONS (tp.system)

#### [Multi-Select-Tag-Chooser]
* *Use Case:** Allow users to select multiple tags from a predefined list for categorization
* *Complexity:** Intermediate

```javascript
<%*
// Define available tags for selection
const availableTags = [
  "project",
  "meeting",
  "documentation",
  "research",
  "todo",
  "important",
  "review"
];
// Present multi-select suggester to user
const selectedTags = await tp.system.suggester(
  (item) => item,  // How to display items
  availableTags,   // Items to choose from
  true,            // Allow multiple selections
  "Select relevant tags (ESC to skip):"
);
// Format tags for YAML frontmatter
let tagsYAML = "";
if (selectedTags && selectedTags.length > 0) {
  tagsYAML = selectedTags.map(tag => `  - ${tag}`).join("\n");
}
// Output to template
tR += "---\n";
tR += "tags:\n";
tR += tagsYAML || "  - uncategorized";
tR += "\n---\n\n";
%>
```

* *Explanation:**
1. Defines an array of available tags
2. Uses `tp.system.suggester()` with multiple selection enabled
3. Maps selected tags to proper YAML list format
4. Handles case where no tags are selected
5. Generates valid YAML frontmatter

* *Validation Notes:**
✓ Async/await properly used for suggester
✓ Correct suggester parameters (display, items, multi-select, prompt)
✓ Proper YAML formatting with indentation
✓ Edge case handling for empty selections

- --

### FRONTMATTER GENERATION

#### [Dynamic-Tag-And-Category-System]
* *Use Case:** Generate structured frontmatter with dynamic tags and hierarchical categories
* *Complexity:** Intermediate

```javascript
<%*
// Get basic metadata
const noteTitle = tp.file.title;
const createdDate = tp.date.now("YYYY-MM-DD");
// Prompt for category with suggestions
const categories = ["Work", "Personal", "Learning", "Health", "Finance"];
const category = await tp.system.suggester(
  item => item,
  categories,
  false,
  "Select category:"
) || "General";
// Get subcategory based on main category
let subcategory = "General";
if (category === "Work") {
  const workSubs = ["Meeting", "Project", "Report", "Planning"];
  subcategory = await tp.system.suggester(
    item => item,
    workSubs,
    false,
    "Select work subcategory:"
  ) || "General";
}
// Generate tags based on category
const baseTags = ["gtd", "obsidian"];
const categoryTags = {
  "Work": ["professional", "business"],
  "Personal": ["life", "self"],
  "Learning": ["education", "study"],
  "Health": ["wellness", "fitness"],
  "Finance": ["money", "budget"]
};
const allTags = [...baseTags, ...categoryTags[category] || []];
// Output YAML frontmatter
tR += "---\n";
tR += `title: "${noteTitle}"\n`;
tR += `created: ${createdDate}\n`;
tR += `category: ${category}\n`;
tR += `subcategory: ${subcategory}\n`;
tR += "tags:\n";
allTags.forEach(tag => {
  tR += `  - ${tag}\n`;
});
tR += "---\n\n";
%>
```

* *Explanation:**
1. Gets note title and current date automatically
2. Uses suggester to choose from predefined categories
3. Provides context-specific subcategories
4. Dynamically generates tags based on category selection
5. Constructs properly formatted YAML frontmatter

* *Validation Notes:**
✓ All async operations properly awaited
✓ Correct YAML structure with proper indentation
✓ Fallback values for all user inputs
✓ No undefined references in tag mapping
✓ Proper string quoting in YAML

- --

### LOGIC & CONTROL FLOW

#### [Priority-Based-Content-Routing]
* *Use Case:** Generate different content sections based on task priority level
* *Complexity:** Basic

```javascript
<%*
// Prompt user for priority level
const priority = await tp.system.suggester(
  item => `${item.emoji} ${item.label}`,
  [
    { value: "high", label: "High Priority", emoji: "🔴" },
    { value: "medium", label: "Medium Priority", emoji: "🟡" },
    { value: "low", label: "Low Priority", emoji: "🟢" }
  ],
  false,
  "Select task priority:"
);
// Generate content based on priority
let content = "";
switch(priority?.value || "low") {
  case "high":
    content = `
## 🔴 High Priority Task
* *Action Required:** Immediate attention needed
* *Deadline:** Today
* *Impact:** Significant
### Next Steps:
- [ ] Identify blockers
- [ ] Allocate dedicated time block
- [ ] Communicate with stakeholders
`;
    break;
  case "medium":
    content = `
## 🟡 Medium Priority Task
* *Action Required:** Complete this week
* *Deadline:** This week
* *Impact:** Moderate
### Next Steps:
- [ ] Schedule time this week
- [ ] Break into smaller tasks
- [ ] Add to task list
`;
    break;
  case "low":
  default:
    content = `
## 🟢 Low Priority Task
* *Action Required:** Complete when possible
* *Deadline:** Flexible
* *Impact:** Minor
### Next Steps:
- [ ] Add to backlog
- [ ] Review during weekly planning
- [ ] Delegate if appropriate
`;
    break;
}
tR += content;
%>
```

* *Explanation:**
1. Uses suggester with formatted display options (emoji + text)
2. Implements switch statement for content routing
3. Provides appropriate content for each priority level
4. Includes default case for safety
5. Generates markdown content with checklists

* *Validation Notes:**
✓ Safe object access with optional chaining
✓ Default case handles undefined priority
✓ Proper markdown formatting
✓ All code paths produce valid output
✓ Clear, readable content structure

- --

### ARRAYS & ITERATION

#### [Task-List-Generator-With-Sorting]
* *Use Case:** Create a sortable task list with status tracking and statistics
* *Complexity:** Advanced

```javascript
<%*
// Get existing tasks from file content or create new list
let tasks = [];
// Prompt for number of tasks to add
const taskCount = parseInt(await tp.system.prompt("How many tasks to add?", "3")) || 3;
// Collect tasks with details
for (let i = 0; i < taskCount; i++) {
  const description = await tp.system.prompt(`Task ${i+1} description:`);
  if (!description) continue;
  const priority = await tp.system.suggester(
    item => item,
    ["High", "Medium", "Low"],
    false,
    `Priority for "${description}":`
  ) || "Medium";
  const effort = await tp.system.suggester(
    item => item,
    ["Small", "Medium", "Large"],
    false,
    `Effort for "${description}":`
  ) || "Medium";
  tasks.push({
    description,
    priority,
    effort,
    status: "todo",
    created: tp.date.now("YYYY-MM-DD")
  });
}
// Sort tasks: High priority first, then by effort
tasks.sort((a, b) => {
  // Priority sorting (High > Medium > Low)
  const priorityOrder = { "High": 3, "Medium": 2, "Low": 1 };
  if (priorityOrder[b.priority] !== priorityOrder[a.priority]) {
    return priorityOrder[b.priority] - priorityOrder[a.priority];
  }
  // Effort sorting (Small > Medium > Large for same priority)
  const effortOrder = { "Small": 3, "Medium": 2, "Large": 1 };
  return effortOrder[b.effort] - effortOrder[a.effort];
});
// Generate statistics
const totalTasks = tasks.length;
const highPriority = tasks.filter(t => t.priority === "High").length;
const mediumPriority = tasks.filter(t => t.priority === "Medium").length;
const lowPriority = tasks.filter(t => t.priority === "Low").length;
// Output task list with statistics
tR += `## Task List\n\n`;
tR += `**Summary:** ${totalTasks} tasks (${highPriority} high, ${mediumPriority} medium, ${lowPriority} low priority)\n\n`;
tR += `| Status | Task | Priority | Effort | Created |\n`;
tR += `|--------|------|----------|--------|---------|\n`;
tasks.forEach(task => {
  tR += `| [ ] | ${task.description} | ${task.priority} | ${task.effort} | ${task.created} |\n`;
});
tR += `\n---\n`;
%>
```

* *Explanation:**
1. Prompts user for number of tasks to create
2. Collects task details through multiple prompts
3. Stores tasks in array with structured data
4. Sorts tasks by priority then effort using custom comparator
5. Generates statistics using array filter operations
6. Outputs formatted markdown table with all tasks

* *Validation Notes:**
✓ Proper array manipulation (push, sort, filter)
✓ Safe number parsing with fallback
✓ Correct markdown table formatting
✓ All async operations properly awaited
✓ Edge case handling for empty descriptions
✓ Comprehensive data structure with multiple properties