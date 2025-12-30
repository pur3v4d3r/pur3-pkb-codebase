<%*
tp.hooks.on_all_templates_executed(async () => {
    const taskContent = `
---
type: review-task
target: "[[${title}]]"
maturity: ${maturity}
confidence: ${confidence}
created: ${dateNow}
---
# Review Task: ${title}
**Target Note**: [[${title}]]  
**Maturity**: ${maturity}  
**Confidence**: ${confidence}
## Task
- [ ] Review [[${title}]] 📅 ${nextReview} ${priority} 🔁 every ${intervalText} #review
**Checklist**:
- [ ] Verify definition accuracy
- [ ] Identify new connections
- [ ] Validate practical applications
- [ ] Assess confidence level
- [ ] Update maturity if needed
---
[[${title}|← Return to Concept]]
`;
    // Create task note in dedicated folder
    await tp.file.create_new(
        taskContent,
        `REVIEW-${id}-${title}`,
        false,
        "05-tasks-&-reviews"
    );
});
%>