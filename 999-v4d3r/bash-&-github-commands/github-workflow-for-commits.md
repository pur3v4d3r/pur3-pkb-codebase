## 🧠 The "Vault-Code" Protocol (v1.0)

This is your Standard Operating Procedure (SOP) for managing `10_pur3v4d3r's-vault`. Keep this document accessible until the muscle memory sets in.

### 🖼️ The Big Picture

You have a **Local Fortress** (`10_pur3v4d3r's-vault`) and a **Remote Backup** (GitHub). VS Code is the bridge between them.

* **Obsidian** = Where you create.
* **VS Code** = Where you save and sync.
* **GitHub** = Where you back up.

---

### ⚡ Quick Reference Cheat Sheet

| Action | Command / Button | When to use? |
| --- | --- | --- |
| **Check Status** | `git status` (Terminal) | Before every commit. |
| **Stage Files** | `git add .` | When you are ready to save changes. |
| **Save Snapshot** | `git commit -m "Message"` | To permanently save a version. |
| **Sync to Cloud** | `git push` | To upload your saved snapshots. |
| **Check Size** | `git count-objects -vH` | If you suspect you added heavy files. |

---

### 🔄 The Daily Workflow Loop

#### 1. The Creation Phase (Obsidian)

* Write your notes, create prompts, and build agents in **Obsidian** as usual.
* *Don't worry about Git yet.* Just do your work.

#### 2. The Staging Phase (VS Code)

*When you are ready to "Save" your session:*

1. Open **VS Code**.
2. Click the **Source Control Icon** (The branching Y shape on the left sidebar).
* *Visual Check:* Look at the list of files.
* **Is the list huge (1000+ files)?** 🛑 STOP. You might have added a folder that needs ignoring. Check `.gitignore`.
* **Is the list just your `.md` files?** ✅ PROCEED.


3. Open the **Terminal** (`Ctrl + ~`) and type:
```bash
git add .

```



#### 3. The Weigh-In (Optional but Recommended)

*If you added images, PDFs, or new plugins today:*

1. In the Terminal, type:
```bash
git count-objects -vH

```


2. Check the `size-pack`.
* **< 500MB?** ✅ Green Light.
* **> 1GB?** 🛑 Red Light. Run `git reset` (undoes the add) and find the large file.



#### 4. The Commit (The "Save")

1. In the Terminal, type:
```bash
git commit -m "Brief description of what you did"

```


* *Example:* `git commit -m "Updated Agent Prompts and added Daily Note"`



#### 5. The Push (The Sync)

1. Send it to the cloud:
```bash
git push

```


2. *Success Indicator:* You will see `To https://github.com/... [new branch] main -> main`.

---

### 🛠️ Maintenance & Safety

#### 🛑 The "Emergency Stop"

If you accidentally `git add .` and realize you staged a 2GB video file:

1. **Do NOT commit.**
2. Run this command to "un-stage" everything:
```bash
git reset

```


3. Add the large file to your `.gitignore`.
4. Start over from Step 2.

#### 🧹 Monthly Cleaning

Over time, your `.git` folder might grow slightly. Run this command once a month to let Git optimize itself (Garbage Collection):

```bash
git gc

```

#### 📂 The "Bloat" Patrol

If you add a new folder structure (like a new `__LOCAL-REPO` download), **always** add it to your `.gitignore` *before* running `git add`.

---

### 📝 VS Code UI Shortcut (Mouse Method)

If you prefer clicking over typing:

1. **Source Control Tab:** Hover over the "Changes" header and click the **+ (Plus)** icon. *(This does `git add .`)*.
2. **Message Box:** Type your message in the box above the files.
3. **Commit:** Click the blue **Commit** button (or checkmark).
4. **Sync:** Click the big blue **Sync Changes** button that appears.

*Note: The Terminal method is safer because it lets you check file size before pushing.*