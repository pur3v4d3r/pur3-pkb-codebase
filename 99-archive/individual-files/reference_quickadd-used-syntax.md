Work Log
```
- **📆date:: {{DATE:YYYY-MM-DD}}** **⌛time:: {{DATE:HH:mm}}** 🖥️entry:: {{VALUE}}
```

Person Note
```
---
tags:
  - #People
  - #Person
  - #Contact
  - #Person-Note
alias: [{{VALUE:First Name?}}]
company: "{{VALUE:Company or Affiliation?}}"
role: "{{VALUE:Role or Title?}}"
first_met: {{DATE:YYYY-MM-DD}}
---
# {{VALUE:Full Name}}

## 👤 Summary
- 

## 🤝 Log
- **{{DATE:YYYY-MM-DD}}**: Initial entry. {{VALUE:How did you meet or what's the context?}}

## ✅ Next Actions
- [ ]
```
In-Note-Logging_Bullet-Point
```
-  {{VALUE}}-(🖥️Captured-on-[[{{DATE:YYYY-MM-DD}}]]-⌛Time:{{DATE:HH:mm:ss}})
```

In-Note-Logging Header
```
#  {{VALUE}}-(🖥️Captured-on-[[{{DATE:YYYY-MM-DD}}]]-⌛Time:{{DATE:HH:mm:ss}})
```
Fleeting-Thought
```
{{VALUE}} (⚡️Captured-on:[[{{DATE:YYYY-MM-DD}}]]-Time:{{DATE:HH:mm:ss}}) type:: thought
```
Task-Log
```
{{VALUE:Task description?}} ➕ Created:: {{DATE:YYYY-MM-DD}} 🔼 Priority:: {{VALUE:Priority?|High,Medium,Low}} 🔗 Source:: {{LINKCURRENT}}
```
Work-Log
```
- **📆date:: {{DATE:YYYY-MM-DD}}** **⌛time:: {{DATE:HH:mm}}** 🖥️entry:: {{VALUE}}
```
Prompt
```
{{VALUE:<variable name>|📝Prompt_}}_{{DATE:🆔YYYYMMDDHHmmss}}

```

🦖Pur3-🐲Project
```
{{VALUE:<variable name>|🦖Pur3-🐲Project_}}_{{DATE:🆔YYYYMMDDHHmmss}}
```
Prompt/Component/Options
```
{{VALUE:🧩Component,⛔Constraint,🎨Style,🎭Persona,📐Format,🏗️Scaffolds,🧠Logic,💫Exemplars}}_{{VALUE:Name}}_{{DATE:🆔YYYYMMDDHHmmss}}
```

Universal/Citation
```
<%*
const sourceType = await tp.system.suggester(
    ["AI-Report/Article", "Book", "Article", "PDF/Report"], 
    ["AI-Report/Article", "Book", "Article", "PDF/Report"], 
    "Choose a Source Type:"
);
const author = await tp.system.suggester(
    ["Gemini-2.5-Pro", "Claude", "ChatGPT","🌩️🦈URG010_🆔20251020205832", "🌩️♊URG011_v1.1_🆔20251022221217", "🌩️🐲URG012_🆔20251023000722"], 
    ["Gemini-2.5-Pro", "Claude", "ChatGPT","🌩️🦈URG010_🆔20251020205832", "🌩️♊URG011_v1.1_🆔20251022221217", "🌩️🐲URG012_🆔20251023000722"],
    "Choose an Author:"
);
const output = `> [!cite]
> **Bibliographic Information**
> - **Source Type**:: ${sourceType}
> - **Title**:: ${tp.file.title}
> - **Author(s)**:: ${author}
> - **Year**:: ${tp.date.now("YYYY")}
> - **Publisher / Journal**:: ⁉️
> - **Volume / Issue**:: 001
> - **Page(s)**:: 001
> - **URL / DOI**:: 
> - **Date Accessed**:: ${tp.date.now("YYYY-MM-DDTHH:mm:ss")}
`;
tR = output;

%>
```