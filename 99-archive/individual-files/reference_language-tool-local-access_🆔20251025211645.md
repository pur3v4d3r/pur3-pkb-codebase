---
title: Reference_Language-Tool-Local-Access_🆔20251025211645
id: 20251025211700
aliases:
  - ai/note
  - ai/educational
  - language-tool
  - llm/local
  - llm/language-tool
type: ⚙️reference
status: ⚡active
priority: ⁉️
created: 2025-10-25T21:17:00
source: gemini-2.5-pro
url: https://gemini.google.com/app/9de42513fdc422fe
tags:
  - prompt-engineering
  - llm/local
---

>[!the-purpose] 
> This is a note dedicated to *How to set up and run* the **LanguageTool** integrated plugin on a **local machine**.
> It covers the **How-to** and the **Key information** you need to *reliable use this plugin* this way.

**To start the Sever use this code**:

- `java -cp C:\Tools\LanguageTool\languagetool-server.jar org.languagetool.server.HTTPServer --port 8081`

## 🖥️ How to Set Up a Local LanguageTool Server on Windows

This process involves **three main stages**: installing the necessary components, running the server, and pointing your Obsidian plugin to it. Given your high-performance PC (i9, 32GB DDR5), you will have more than enough resources to run this server in the background without any noticeable impact.

### Step 1: Install/Verify Java

LanguageTool is a Java application, so it requires the Java Runtime Environment (JRE) to run.
1.  Open your **Command Prompt** or **Windows Terminal**.
2.  Type the command `java -version` and press Enter.
3.  If you see a version number (e.g., "openjdk version 17.0.5" or similar), you are all set. You need **Java 8 or newer**.
4.  If you get an error, you must install Java. You can download the official "Windows x64 Installer" for the latest JRE from [Oracle's Java Downloads page](https://www.java.com/en/download/).

### Step 2: Download and Prepare the LanguageTool Server

You need the "stand-alone" version of the tool, which is a `.zip` file containing the server `.jar` file.
1.  Go to the official LanguageTool download page: [https://languagetool.org/download/](https://www.google.com/search?q=https://languagetool.org/download/)
2.  Look for the **"Stand-alone (offline) version"**. It will be a link to a file named something like `LanguageTool-stable.zip`. This is the file you want, **not** the desktop app.
3.  Create a new folder in a permanent location on your computer. For example: `C:\Tools\LanguageTool\`.
4.  **Unzip** the contents of the `LanguageTool-stable.zip` file you downloaded directly into this new folder.
5.  Inside this folder, you will now see several files, including `languagetool-server.jar`. This is the server application.

### Step 3: Run the Local Server

You will run the server from your Command Prompt or Terminal.
1.  Open **Windows Terminal** (or Command Prompt).
2.  Navigate to the folder you created in Step 2. You can do this by using the `cd` (change directory) command. For example:
    `cd C:\Tools\LanguageTool`
3.  Once you are in the correct folder, paste and run the following command:
    `java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081`
4.  If it is successful, the terminal will show several lines of text, ending with a message like `INFO org.languagetool.server.HTTPServer... Server started at http://localhost:8081`.
5.  **Do not close this terminal window.** The server is now running. As long as this window is open and running this command, your local LanguageTool server is active.
> **Pro-Tip:** To make this permanent, you could create a `.bat` (batch) file on your desktop with that command and the `cd` command, allowing you to start the server with a simple double-click whenever you need it.

### Step 4: Configure the Obsidian Plugin

Finally, you will tell the LanguageTool plugin in Obsidian to stop using the internet and to use your new local server instead.
1.  Open **Obsidian** and go to **Settings**.
2.  On the left, scroll down to **Community plugins** and select **LanguageTool**.
3.  In the plugin's settings, look for the **"Endpoint"** or **"Server URL"** setting.
4.  By default, it will be set to the public API (`https://api.languagetoolplus.com`). Delete this URL.
5.  Replace it with the address of your local server:
    `http://localhost:8081`
6.  Close the settings menu. The plugin will now automatically connect to your local server for all checks, giving you full privacy and removing all text-length limits.

-----

Here is the single, complete command you can copy and paste directly into your terminal.
`java -cp C:\Tools\LanguageTool\languagetool-server.jar org.languagetool.server.HTTPServer --port 8081`

---
## ⌨️ How to Use This Command

1.  Press the **Start** button.
2.  Type `cmd` or `Terminal`.
3.  Open the **Command Prompt** or **Windows Terminal** application.
4.  A black or blue window will appear. **Copy the complete command** from the line above.
5.  **Paste it** directly into the terminal window (you can usually right-click to paste).
6.  Press **Enter**.
If Java is installed correctly, you should see it print a few lines and end with a message like `Server started at http://localhost:8081`. You must keep this window open for the server to stay running.
### What This Command Does

This command is more specific than the previous one and doesn't require you to change directories first.
* `java`: Tells the computer to use the Java program.
* `-cp C:\Tools\LanguageTool\languagetool-server.jar`: The `-cp` (classpath) flag tells Java the **full, exact path** to the `.jar` file it needs to run. This is the part that likely failed before.
* `org.languagetool.server.HTTPServer`: This tells Java *which specific class* inside that `.jar` file to run (the server part).
* `--port 8081`: This is an argument that tells the server to "listen" on port 8081.

---
## 🚀 A Better, Permanent Solution (Batch File)

Since you'll need to run this command every time you want to use the server, I highly recommend creating a simple "shortcut" file. This is called a batch file.
1.  Right-click on your **Desktop** and go to **New** > **Text Document**.
2.  Name the new file `Start LanguageTool.txt`.
3.  Double-click the file to open it in **Notepad**.
4.  **Copy and paste** the exact command from above into the Notepad file:
    `java -cp C:\Tools\LanguageTool\languagetool-server.jar org.languagetool.server.HTTPServer --port 8081`
5.  Click **File** > **Save As…**.
6.  In the "Save As" window, change the **"File name"** from `Start LanguageTool.txt` to `Start LanguageTool.bat` (make sure you change the `.txt` to `.bat`).
7.  Change the **"Save as type"** dropdown from "Text Documents" to **"All Files"**.
8.  Click **Save**.
Now, you will have a new file on your desktop named `Start LanguageTool.bat` with a gear icon. From now on, you can just **double-click that file**, and it will automatically open a terminal and run the server for you.

Would you like help with getting that `.bat` file to run automatically when you start your computer?