> [!stack] 🎛️ Project Control Center
> **Velocity**:: `= "<progress value='" + round((length(filter(this.file.tasks, (t) => t.completed)) / max(list(1, length(this.file.tasks)))) * 100) + "' max='100'></progress>"`
> **Health**:: `$= const fields = ["priority", "due-date"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ Valid"`
> **Context**:: `= "<span style='background-color: #2d7a46; padding: 2px 8px; border-radius: 10px; color: white;'>" + this.status + "</span>"`
