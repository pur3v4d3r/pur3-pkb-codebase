# optimize_prompt.py
import re
import os

# ==========================================
# 1. NEW MODULE CONTENT DEFINITIONS
# ==========================================

MODULE_GEM_DOCS = """
<gem_documentation>

## Gem & Prompt Documentation Module

### Purpose
Document AI "Gems," "Personas," and "System Prompts" within the SPES framework.

### Standard Gem Structure
```markdown
# 💎 [Gem Name]

**Version**: 1.0.0
**Author**: [[Your Name]]
**Tags**: #pkm/prompt-engineering #gem/[type]

## 📋 Overview
[Brief description of what this Gem/Prompt solves]

## ⚙️ Configuration
| Setting | Value | Description |
|---------|-------|-------------|
| **Model** | Claude 3.5 Sonnet | Recommended model |
| **Temp** | 0.7 | Creativity level |
| **Context** | `[[project-codebase]]` | Required files |

## 📥 Input Triggers
- **Command**: `!gem [input]`
- **Slash Command**: `/gem_name`
- **Frontmatter**: `type: [gem-type]`

## 🧠 System Instruction (The Prompt)

> [!abstract] System Prompt
> ```markdown
> [Insert actual system prompt text here]
> ```

## 📤 Output Specification
The Gem produces output in the following format:
1. **Frontmatter**: Standard Obsidian YAML
2. **Callouts**: Uses `> [!info]` for metadata
3. **Links**: Strict Wikilink usage `[[Note Name]]`

## 🧪 Test Cases
| Input | Expected Behavior | Pass/Fail |
|-------|-------------------|-----------|
| `[Case 1]` | Generates list of 5 items | ✅ |
| `[Case 2]` | Handles missing data gracefully | ❌ |

```

</gem_documentation>
"""

MODULE_AUTOMATION = """
<automation_scripting>

## Automation & Scripting Module

### Purpose

Document internal Obsidian automations using Templater, QuickAdd, and Dataview JS.

### Supported Engines

| Engine | Language | File Extension |
| --- | --- | --- |
| **Templater** | JavaScript | `.js` / `.md` |
| **QuickAdd** | JavaScript | `.js` (Macro) |
| **Dataview** | DQL / JS | Codeblock |

### Templater Script Structure

```javascript
/*
 * Script: [Name]
 * Trigger: Alt+E
 * Context: Active File
 */

async function main(tp) {
    // 1. Get User Input
    const input = await tp.system.prompt("Enter Title");
    
    // 2. Process Data
    const date = tp.date.now("YYYY-MM-DD");
    
    // 3. Output
    return `[[${date}]] - ${input}`;
}

module.exports = main;

```

### Dataview Query Documentation

```markdown
### Query: [Name]
**Purpose**: List all active projects
**Type**: DataviewJS

```dataviewjs
dv.pages("#project/active")
  .sort(p => p.file.mtime, "desc")
  .map(p => [p.file.link, p.status])

```

```

</automation_scripting>
"""

# ==========================================
# 2. REPLACEMENT LOGIC
# ==========================================

def optimize_prompt(master_prompt_text, taxonomy_text):
    print("🔄 Starting Optimization Process...")
    
    # --- Step A: Inject Taxonomy Rules into Quality Assurance ---
    print("   ↳ Injecting Taxonomy Rules...")
    
    taxonomy_rule = """
**Tagging Compliance (Strict)**
- [ ] **Taxonomy**: Tags must adhere to `_reference-tag-taxonomy`.
- [ ] **Structure**: Use hierarchical format `#domain/subdomain`.
- [ ] **Wikilinks**: ALL internal links must be `[[Wikilinks]]`. NO `[Markdown](links.md)`.
"""
    # Insert before "### Automated Validation"
    processed_text = master_prompt_text.replace(
        "### Automated Validation", 
        f"{taxonomy_rule}\n\n### Automated Validation"
    )

    # --- Step B: Swap API Docs for Automation Docs ---
    print("   ↳ Swapping API Module for Automation Module...")
    # Regex to find the entire <api_documentation> block and replace it
    processed_text = re.sub(
        r'<api_documentation>.*?</api_documentation>', 
        MODULE_AUTOMATION, 
        processed_text, 
        flags=re.DOTALL
    )

    # --- Step C: Add Gem Documentation Module ---
    print("   ↳ Adding Gem Documentation Module...")
    # Add it before the Technical Documentation module
    processed_text = processed_text.replace(
        "<technical_documentation>", 
        f"{MODULE_GEM_DOCS}\n\n<technical_documentation>"
    )

    # --- Step D: Update Execution Protocol (Paths & Links) ---
    print("   ↳ Refactoring Execution Protocol (Paths & Links)...")
    
    # Handle the space in "10_obsidian-documentation 2/" carefully
    old_protocol = r"\| Technical Docs \| `docs/architecture.md`, `docs/design.md` \|"
    new_protocol = "| Technical Docs | `10_obsidian-documentation 2/architecture.md` |"
    processed_text = re.sub(old_protocol, new_protocol, processed_text)
    
    # Replace standard Git folder structures with Obsidian Vault structures
    processed_text = processed_text.replace("docs/adr/", "000_databsae/adr/")
    processed_text = processed_text.replace("docs/tutorials/", "10_obsidian-documentation 2/tutorials/")
    
    # Add specific Instruction for File Naming
    naming_instruction = """
### File Naming & Linking
1. **Location**: All docs go to `10_obsidian-documentation 2/` or `000_databsae/`.
2. **Linking**: ALWAYS use Wikilinks `[[Note Name]]`.
3. **IDs**: Core resources get timestamp IDs in frontmatter (e.g., `id: "2025..."`).
    """
    processed_text = processed_text.replace("### File Naming Conventions", naming_instruction + "\n\n### File Naming Conventions")

    # --- Step E: Update Router Trigger Words ---
    print("   ↳ Updating Router Triggers...")
    processed_text = processed_text.replace(
        '| "API docs", "endpoint", "OpenAPI"', 
        '| "Automation", "Script", "Templater", "Dataview"'
    )
    processed_text = processed_text.replace(
        "| API Documentation | `<api_documentation>` |", 
        "| Automation Docs | `<automation_scripting>` |"
    )
    
    # Add Gem Trigger
    gem_trigger = '| "Gem", "Prompt", "Persona", "System Instruction" | Gem Documentation | `<gem_documentation>` |'
    processed_text = processed_text.replace(
        '| "technical docs"', 
        f"{gem_trigger}\n| \"technical docs\""
    )

    return processed_text

# ==========================================
# 3. EXECUTION BLOCK
# ==========================================

if __name__ == "__main__":
    # Define filenames (Edit these if your filenames differ)
    INPUT_FILE = "project-codebase.md"
    TAXONOMY_FILE = "_reference-tag-taxonomy-202511190109.md"
    OUTPUT_FILE = "PKB_Master_Prompt_v2.md"

    print(f"📂 Looking for input file: {INPUT_FILE}")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ ERROR: Could not find '{INPUT_FILE}'.")
        print("   Please ensure the script is in the same folder as your project-codebase.md file.")
    else:
        try:
            # Read Master Prompt
            with open(INPUT_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
                # Find the start of the prompt in the file
                start_idx = content.find("# Document Generation Master Prompt")
                if start_idx != -1:
                    prompt_text = content[start_idx:]
                else:
                    prompt_text = content

            # Read Taxonomy (Optional - uses default if missing)
            taxonomy_text = ""
            if os.path.exists(TAXONOMY_FILE):
                with open(TAXONOMY_FILE, 'r', encoding='utf-8') as f:
                    taxonomy_text = f.read()
            else:
                print(f"⚠️ Warning: Taxonomy file '{TAXONOMY_FILE}' not found. Using strict defaults.")

            # Run Optimization
            new_prompt = optimize_prompt(prompt_text, taxonomy_text)

            # Write Output
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.write(new_prompt)
                
            print(f"✅ Success! Generated '{OUTPUT_FILE}'")
            print("   You can now copy the content of that file into your system prompt.")
            
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")