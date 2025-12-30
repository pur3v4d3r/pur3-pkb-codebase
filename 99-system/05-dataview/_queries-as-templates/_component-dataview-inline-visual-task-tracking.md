> [!abstract] 📊 Project Velocity
> **Completion**:: `= "<progress value='" + round((length(filter(this.file.tasks, (t) => t.completed)) / max(list(1, length(this.file.tasks)))) * 100) + "' max='100'></progress>"` 
> **Status**:: `= choice(length(filter(this.file.tasks, (t) => t.completed)) = length(this.file.tasks), "✅ Complete", "🚧 In Progress")`

