- --
title: "<% tp.file.title %>"
created_date: "<% tp.date.now("YYYY-MM-DD") %>"
type: "task-list"
status: "active"
- --
# <% tp.file.title %> Task List
## Tasks
<%
let tasks = tp.system.prompt("Enter tasks separated by commas (e.g., task1, task2)").split(", ");
for (let i = 0; i < tasks.length; i++) {
%>
- [ ] <%= tasks[i] %>
<% } %>