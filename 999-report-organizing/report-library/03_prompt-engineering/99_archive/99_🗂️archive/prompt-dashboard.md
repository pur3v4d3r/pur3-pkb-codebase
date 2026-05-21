# Prompt Engineering Knowledge Base

## Recent Prompts
```dataview
TABLE prompt_objective, llm_model, success_rating
FROM #prompt-log
SORT date_created DESC
LIMIT 10
```

## Top Performing Coding Prompts
```dataview
TABLE prompt_objective, key_takeaway
FROM #prompt-log
WHERE contains(tags, "coding") AND success_rating >= 4
SORT success_rating DESC
```

## Analyze Failures
```dataview
LIST FROM #prompt-log
WHERE success_rating <= 2
SORT date_created DESC
```

## Model Comparison (Creative Tasks)
```dataview
TABLE llm_model, success_rating
FROM #prompt-log
WHERE contains(tags, "creative-writing")
SORT llm_model, success_rating DESC
```
