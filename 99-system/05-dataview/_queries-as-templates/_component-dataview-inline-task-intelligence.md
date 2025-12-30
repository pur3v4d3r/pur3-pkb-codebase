> [!todo] 🏗️ Project Status
> **Tasks Open**:: `= length(filter(this.file.tasks, (t) => !t.completed))` | **Tasks Done**:: `= length(filter(this.file.tasks, (t) => t.completed))`
> **Progress**:: `= round((length(filter(this.file.tasks, (t) => t.completed)) / max(list(1, length(this.file.tasks)))) * 100) + "%"`
