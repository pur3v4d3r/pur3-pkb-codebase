- --
title: "<% tp.file.title %>"
created_date: "<% tp.date.now("YYYY-MM-DD") %>"
type: "capture"
- --
# <% tp.file.title %> Capture
## Content
<%
let clipboardContent = await tp.system.clipboard();
if (clipboardContent.includes("http")) {
    folderPath = "04-library/";
} else {
    folderPath = "03-notes/";
}
%>
This note was captured from the clipboard on <% tp.date.now("YYYY-MM-DD") %>.
## Clipboard Content
<%= clipboardContent %>