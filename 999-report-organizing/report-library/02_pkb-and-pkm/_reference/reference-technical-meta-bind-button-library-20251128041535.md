---
aliases:
  - Meta Bind
  - Meta-Bind
maturity: developing
---


### Button Codeblock Label
```
meta-bind-button
```

### Blank Button Layout
```
label: ""
icon: ""
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: ""
hidden: false
actions:
  - type: ""
    bindTarget: maturity
    evaluate: false
    value: seedling
```

### Available Button Actions:
```
### Available Button Actions:
- command — Execute any Obsidian command
- js — Run JavaScript code
- open — Open URLs or notes
- sleep — Add delays in multi-action sequences
- updateMetadata — Modify frontmatter properties
- templaterCreateNote — Create notes using [[Templater]] templates
- replaceInNote — Find and replace text operations
- regexpReplaceInNote — Regex-based replacements
- insertIntoNote — Insert content at specific positions
```

## Note Maturity
```markdown
## 🌱 Development Status

**Current Maturity**: `VIEW[{maturity}]`

`BUTTON[maturity-seedling]`
`BUTTON[maturity-budding]`
`BUTTON[maturity-developing]`
`BUTTON[maturity-evergreen]`

```
### Maturity Seedling
`VIEW[{maturity}]`
```
# Button Template: maturity-seedling
id: maturity-seedling
label: 🌱 Seedling
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: seedling
  
  label: Seedling
icon: sprout
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-seedling
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: seedling
```

```meta-bind-button
label: Seedling
icon: sprout
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-seedling
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: seedling
```

### Maturity Budding

```
# Button Template: maturity-budding
id: maturity-budding
label: 🌿Budding
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: budding
  
  label: Budding
icon: leaf
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-budding
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: budding

```

```meta-bind-button
label: Budding
icon: leaf
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-budding
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: budding
```

### Maturity Developing

```
# Button Template: maturity-developing
id: maturity-developing
label: 🌳 Developing
style: primary
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: developing

label: Developing
icon: tree-deciduous
style: primary
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: 
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: developing
```

```meta-bind-button
label: Developing
icon: tree-deciduous
style: primary
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-developing
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: developing
```

### Maturity Evergreen

```
# Button Template: maturity-evergreen
id: maturity-evergreen
label: 🌲 Evergreen
style: primary
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: evergreen

label: Evergreen
icon: tree-pine
style: primary
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-evergreen
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: evergreen
```

```meta-bind-button
label: Evergreen
icon: tree-pine
style: primary
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-evergreen
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: evergreen
```

------

## Confidence Level Toggle
```
## 📊 Epistemic Status

**Current Confidence**: `VIEW[{confidence}]`

`BUTTON[conf-speculative]` | `BUTTON[conf-provisional]` | `BUTTON[conf-moderate]` | `BUTTON[conf-high]` | `BUTTON[conf-established]`
```

### Confidence Speculative

```
# Button Template: conf-speculative
id: conf-speculative
label: ❓ Speculative
style: default
action:
  type: updateMetadata
  bindTarget: confidence
  evaluate: false
  value: speculative
  
  label: Speculative
icon: circle-question-mark
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: conf-speculative
hidden: false
actions:
  - type: updateMetadata
    bindTarget: confidence
    evaluate: false
    value: speculative
```

```meta-bind-button
label: Speculative
icon: shield-question-mark
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: conf-speculative
hidden: false
actions:
  - type: updateMetadata
    bindTarget: confidence
    evaluate: false
    value: speculative
```










































