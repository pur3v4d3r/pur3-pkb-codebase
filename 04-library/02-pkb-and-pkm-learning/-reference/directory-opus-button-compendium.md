---
tags: #directory-opus #automation #windows-productivity #reference-note #file-management
aliases: [DOpus Buttons, Directory Opus QoL Buttons, DOpus Button Collection, File Manager Automation]
status: evergreen
certainty: verified
type: reference

---


```

- --

# 🎛️ Directory Opus Button Compendium
## Quality of Life Upgrade Collection

> [!abstract] Overview
> This compendium provides **50+ production-ready buttons** for [[Directory Opus]], organized by functional category. Each button includes complete [[XML]] code, functional explanation, and customization notes. These buttons transform common multi-step operations into single-click actions, dramatically improving [[file management]] workflow efficiency.

- --

## 📁 File Operations

### Create Dated Folder

> [!what-this-does] Function
> Creates a new folder with today's date in ISO format (YYYY-MM-DD), perfect for organizing daily work or downloads.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>New Dated Folder</label>
	<tip>Create folder with today's date</tip>
	<icon1>#newfolder</icon1>
	<function type="normal">
		<instruction>CreateFolder NAME="{date|yyyy-MM-dd}"</instruction>
	</function>
</button>
```

- --

### Create Timestamped Folder

> [!what-this-does] Function
> Creates a folder with full timestamp (date and time), ideal for versioning or snapshot captures.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Timestamped Folder</label>
	<tip>Create folder with date and time</tip>
	<icon1>#newfolder</icon1>
	<function type="normal">
		<instruction>CreateFolder NAME="{date|yyyy-MM-dd_HH-mm-ss}"</instruction>
	</function>
</button>
```

- --

### Flatten Folder Structure

> [!what-this-does] Function
> Moves all files from subfolders into the current directory, then removes empty folders. **Use with caution** --- this is destructive to folder hierarchy.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Flatten Folder</label>
	<tip>Move all subfolder contents to current folder</tip>
	<icon1>#flatview</icon1>
	<function type="normal">
		<instruction>@confirm:This will flatten all subfolders. Continue?</instruction>
		<instruction>Copy MOVE HERE FLATVIEWCOPY=recreate,automanage</instruction>
		<instruction>Delete REMOVECOLLECTION QUIET</instruction>
	</function>
</button>
```

- --

### Move to Parent Folder

> [!what-this-does] Function
> Instantly moves selected items up one directory level without navigation.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Move to Parent</label>
	<tip>Move selected items to parent folder</tip>
	<icon1>#moveup</icon1>
	<function type="normal">
		<instruction>Copy MOVE TO=".."</instruction>
	</function>
</button>
```

- --

### Duplicate File with Suffix

> [!what-this-does] Function
> Creates a copy of selected files with "_copy" suffix, keeping them in the same location.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Duplicate Here</label>
	<tip>Create copy with _copy suffix</tip>
	<icon1>#copy</icon1>
	<function type="normal">
		<instruction>Copy DUPLICATE AS="{file|noext}_copy.{file|ext}"</instruction>
	</function>
</button>
```

- --

### Duplicate with Timestamp

> [!what-this-does] Function
> Creates a backup copy with timestamp suffix --- excellent for manual versioning.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Backup Copy</label>
	<tip>Create timestamped backup</tip>
	<icon1>#copy</icon1>
	<function type="normal">
		<instruction>Copy DUPLICATE AS="{file|noext}_{date|yyyy-MM-dd_HH-mm}.{file|ext}"</instruction>
	</function>
</button>
```

- --

### Copy Filename to Clipboard

> [!what-this-does] Function
> Copies the filename(s) of selected items to clipboard (without path).

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Copy Filename</label>
	<tip>Copy filename to clipboard</tip>
	<icon1>#clipboard</icon1>
	<function type="normal">
		<instruction>Clipboard COPYNAMES=nopaths</instruction>
	</function>
</button>
```

- --

### Copy Full Path to Clipboard

> [!what-this-does] Function
> Copies complete file path(s) to clipboard, essential for referencing files in other applications.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Copy Full Path</label>
	<tip>Copy complete file path to clipboard</tip>
	<icon1>#clipboard</icon1>
	<function type="normal">
		<instruction>Clipboard COPYNAMES=unc</instruction>
	</function>
</button>
```

- --

### Copy as URI Path

> [!what-this-does] Function
> Copies file path in `file:///` URI format, useful for [[Markdown]] links and web applications.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Copy as URI</label>
	<tip>Copy as file:/// URI path</tip>
	<icon1>#clipboard</icon1>
	<function type="normal">
		<instruction>Clipboard COPYNAMES=uri</instruction>
	</function>
</button>
```

- --

### Copy Folder Path

> [!what-this-does] Function
> Copies the current folder's path to clipboard (not the selected files, but the directory you're in).

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Copy Folder Path</label>
	<tip>Copy current folder path</tip>
	<icon1>#clipboard</icon1>
	<function type="normal">
		<instruction>Clipboard SET {sourcepath}</instruction>
	</function>
</button>
```

- --

## 🔄 Rename Operations

### Rename to Lowercase

> [!what-this-does] Function
> Converts all selected filenames to lowercase.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Lowercase Names</label>
	<tip>Convert filenames to lowercase</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename CASE=lower</instruction>
	</function>
</button>
```

- --

### Rename to UPPERCASE

> [!what-this-does] Function
> Converts all selected filenames to uppercase.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>UPPERCASE Names</label>
	<tip>Convert filenames to uppercase</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename CASE=upper</instruction>
	</function>
</button>
```

- --

### Rename to Title Case

> [!what-this-does] Function
> Capitalizes the first letter of each word in filenames.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Title Case Names</label>
	<tip>Capitalize first letter of each word</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename CASE=firstword</instruction>
	</function>
</button>
```

- --

### Replace Spaces with Underscores

> [!what-this-does] Function
> Converts spaces to underscores in filenames --- essential for [[command line]] compatibility and [[URL]]-safe naming.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Spaces → Underscores</label>
	<tip>Replace spaces with underscores</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename PATTERN=" " TO="_" FINDREP</instruction>
	</function>
</button>
```

- --

### Replace Underscores with Spaces

> [!what-this-does] Function
> The reverse operation --- humanizes filenames by converting underscores back to spaces.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Underscores → Spaces</label>
	<tip>Replace underscores with spaces</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename PATTERN="_" TO=" " FINDREP</instruction>
	</function>
</button>
```

- --

### Add Date Prefix

> [!what-this-does] Function
> Prepends today's date to selected filenames in ISO format.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Add Date Prefix</label>
	<tip>Prepend today's date to filename</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename PATTERN="*" TO="{date|yyyy-MM-dd}_*"</instruction>
	</function>
</button>
```

- --

### Sequential Numbering

> [!what-this-does] Function
> Renames selected files with sequential numbers (001, 002, 003...) while preserving extensions.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Number Sequentially</label>
	<tip>Rename with sequential numbers</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename PATTERN="*" TO="[#001].*" AUTORENAME</instruction>
	</function>
</button>
```

- --

### Custom Prefix + Number

> [!what-this-does] Function
> Prompts for a prefix, then numbers files sequentially with that prefix.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Prefix + Number</label>
	<tip>Add custom prefix with sequential number</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename PATTERN="*" TO="{dlgstring|Enter prefix:}_[#001].*"</instruction>
	</function>
</button>
```

- --

## 📂 Selection Operations

### Select All Images

> [!what-this-does] Function
> Selects all common image file types in the current view.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Images</label>
	<tip>Select all image files</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select PATTERN grp:Images</instruction>
	</function>
</button>
```

- --

### Select All Documents

> [!what-this-does] Function
> Selects document files (PDF, DOCX, TXT, etc.).

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Documents</label>
	<tip>Select document files</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select PATTERN grp:Documents</instruction>
	</function>
</button>
```

- --

### Select All Videos

> [!what-this-does] Function
> Selects all video file types.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Videos</label>
	<tip>Select all video files</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select PATTERN grp:Movies</instruction>
	</function>
</button>
```

- --

### Select All Audio

> [!what-this-does] Function
> Selects all audio/music file types.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Audio</label>
	<tip>Select all audio files</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select PATTERN grp:Music</instruction>
	</function>
</button>
```

- --

### Select by Extension (Prompt)

> [!what-this-does] Function
> Prompts for a file extension, then selects all matching files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select by Extension</label>
	<tip>Select files by extension</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select PATTERN="*.{dlgstring|Enter extension (without dot):}"</instruction>
	</function>
</button>
```

- --

### Select Same Extension

> [!what-this-does] Function
> Selects all files with the same extension as the currently focused file.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Same Type</label>
	<tip>Select all files with same extension</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select PATTERN="*.{file|ext}"</instruction>
	</function>
</button>
```

- --

### Select Files Only (No Folders)

> [!what-this-does] Function
> Selects all files while excluding folders from selection.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Files Only</label>
	<tip>Select files, exclude folders</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select ALL NOFOLDERS</instruction>
	</function>
</button>
```

- --

### Select Folders Only

> [!what-this-does] Function
> Selects only folders, excluding all files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Folders Only</label>
	<tip>Select folders, exclude files</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select ALL NODIRS=!*</instruction>
	</function>
</button>
```

- --

### Select Today's Files

> [!what-this-does] Function
> Selects all files modified today.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Select Today's Files</label>
	<tip>Select files modified today</tip>
	<icon1>#selectall</icon1>
	<function type="normal">
		<instruction>Select FILTERDEF=modified match today</instruction>
	</function>
</button>
```

- --

### Invert Selection

> [!what-this-does] Function
> Toggles selection state --- selected becomes unselected and vice versa.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Invert Selection</label>
	<tip>Swap selected and unselected</tip>
	<icon1>#selectinvert</icon1>
	<function type="normal">
		<instruction>Select INVERT</instruction>
	</function>
</button>
```

- --

## 📦 Archive Operations

### Create ZIP (Same Location)

> [!what-this-does] Function
> Creates a [[ZIP]] archive from selected files in the current folder.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Create ZIP</label>
	<tip>Compress selected to ZIP</tip>
	<icon1>#zip</icon1>
	<function type="normal">
		<instruction>Copy ARCHIVE=.zip HERE</instruction>
	</function>
</button>
```

- --

### Create Dated ZIP

> [!what-this-does] Function
> Creates a ZIP with today's date in the filename.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Create Dated ZIP</label>
	<tip>Create ZIP with date in name</tip>
	<icon1>#zip</icon1>
	<function type="normal">
		<instruction>Copy ARCHIVE=.zip HERE CREATEFOLDER="{date|yyyy-MM-dd}_archive"</instruction>
	</function>
</button>
```

- --

### Create Named ZIP (Prompt)

> [!what-this-does] Function
> Prompts for archive name before creating ZIP.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Create Named ZIP</label>
	<tip>Create ZIP with custom name</tip>
	<icon1>#zip</icon1>
	<function type="normal">
		<instruction>Copy ARCHIVE=.zip HERE CREATEFOLDER="{dlgstring|Enter archive name:}"</instruction>
	</function>
</button>
```

- --

### Extract to Subfolder

> [!what-this-does] Function
> Extracts archives to a subfolder named after the archive file.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Extract to Subfolder</label>
	<tip>Extract to named subfolder</tip>
	<icon1>#zipextract</icon1>
	<function type="normal">
		<instruction>Copy EXTRACT HERE CREATEFOLDER="{file|noext}"</instruction>
	</function>
</button>
```

- --

### Extract Here

> [!what-this-does] Function
> Extracts archive contents directly to current folder.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Extract Here</label>
	<tip>Extract to current folder</tip>
	<icon1>#zipextract</icon1>
	<function type="normal">
		<instruction>Copy EXTRACT HERE</instruction>
	</function>
</button>
```

- --

### Create 7z Archive

> [!what-this-does] Function
> Creates a [[7-Zip]] archive with better compression than ZIP.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Create 7z</label>
	<tip>Compress to 7z format</tip>
	<icon1>#zip</icon1>
	<function type="normal">
		<instruction>Copy ARCHIVE=.7z HERE</instruction>
	</function>
</button>
```

- --

## 🖼️ Image Operations

### Rotate Image 90° Clockwise

> [!what-this-does] Function
> Rotates selected images 90 degrees clockwise using [[EXIF]] lossless rotation where possible.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Rotate 90° CW</label>
	<tip>Rotate images clockwise</tip>
	<icon1>#rotatecw</icon1>
	<function type="normal">
		<instruction>Image ROTATE=90 HERE REPLACE</instruction>
	</function>
</button>
```

- --

### Rotate Image 90° Counter-Clockwise

> [!what-this-does] Function
> Rotates selected images 90 degrees counter-clockwise.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Rotate 90° CCW</label>
	<tip>Rotate images counter-clockwise</tip>
	<icon1>#rotateccw</icon1>
	<function type="normal">
		<instruction>Image ROTATE=270 HERE REPLACE</instruction>
	</function>
</button>
```

- --

### Rotate 180°

> [!what-this-does] Function
> Flips image upside down.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Rotate 180°</label>
	<tip>Flip image upside down</tip>
	<icon1>#rotate180</icon1>
	<function type="normal">
		<instruction>Image ROTATE=180 HERE REPLACE</instruction>
	</function>
</button>
```

- --

### Convert to PNG

> [!what-this-does] Function
> Converts selected images to [[PNG]] format.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Convert to PNG</label>
	<tip>Convert images to PNG format</tip>
	<icon1>#image</icon1>
	<function type="normal">
		<instruction>Image CONVERT=png HERE</instruction>
	</function>
</button>
```

- --

### Convert to JPG

> [!what-this-does] Function
> Converts selected images to [[JPEG]] format (quality 85).

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Convert to JPG</label>
	<tip>Convert images to JPEG format</tip>
	<icon1>#image</icon1>
	<function type="normal">
		<instruction>Image CONVERT=jpg HERE QUALITY=85</instruction>
	</function>
</button>
```

- --

### Set as Wallpaper

> [!what-this-does] Function
> Sets the selected image as desktop wallpaper.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Set as Wallpaper</label>
	<tip>Use as desktop background</tip>
	<icon1>#image</icon1>
	<function type="normal">
		<instruction>Properties SETWALLPAPER=fill</instruction>
	</function>
</button>
```

- --

## ⚙️ System Operations

### Open Command Prompt Here

> [!what-this-does] Function
> Opens [[Command Prompt]] in the current directory.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>CMD Here</label>
	<tip>Open Command Prompt in current folder</tip>
	<icon1>#cmd</icon1>
	<function type="normal">
		<instruction>CLI DOSPROMPT=cmd</instruction>
	</function>
</button>
```

- --

### Open PowerShell Here

> [!what-this-does] Function
> Opens [[PowerShell]] in the current directory.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>PowerShell Here</label>
	<tip>Open PowerShell in current folder</tip>
	<icon1>#powershell</icon1>
	<function type="normal">
		<instruction>CLI DOSPROMPT=powershell</instruction>
	</function>
</button>
```

- --

### Open Windows Terminal Here

> [!what-this-does] Function
> Opens [[Windows Terminal]] in the current directory.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Terminal Here</label>
	<tip>Open Windows Terminal here</tip>
	<icon1>#terminal</icon1>
	<function type="normal">
		<instruction>CLI DOSPROMPT="wt -d ."</instruction>
	</function>
</button>
```

- --

### Open in VS Code

> [!what-this-does] Function
> Opens selected file(s) or folder in [[Visual Studio Code]].

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Open in VS Code</label>
	<tip>Open selection in Visual Studio Code</tip>
	<icon1>#vscode</icon1>
	<function type="normal">
		<instruction>"C:\Users\{$username}\AppData\Local\Programs\Microsoft VS Code\Code.exe" {file}</instruction>
	</function>
</button>
```

> [!helpful-tip] Path Customization
> Adjust the VS Code path to match your installation. Common alternatives: `C:\Program Files\Microsoft VS Code\Code.exe`

- --

### Open Folder in VS Code

> [!what-this-does] Function
> Opens the current folder as a VS Code workspace.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Folder in VS Code</label>
	<tip>Open current folder in VS Code</tip>
	<icon1>#vscode</icon1>
	<function type="normal">
		<instruction>"C:\Users\{$username}\AppData\Local\Programs\Microsoft VS Code\Code.exe" "{sourcepath}"</instruction>
	</function>
</button>
```

- --

### Take Ownership

> [!what-this-does] Function
> Takes ownership of selected files/folders (requires Administrator). Essential for accessing protected files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Take Ownership</label>
	<tip>Take ownership of selected items</tip>
	<icon1>#security</icon1>
	<function type="normal">
		<instruction>@admin</instruction>
		<instruction>@runmode:hide</instruction>
		<instruction>takeown /f "{filepath}" /r /d y</instruction>
		<instruction>icacls "{filepath}" /grant administrators:F /t</instruction>
	</function>
</button>
```

> [!warning] Administrative Privileges
> This button requires running with elevated permissions and modifies file ownership/permissions. Use responsibly.

- --

### Calculate Folder Size

> [!what-this-does] Function
> Forces calculation and display of folder sizes in the size column.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Calculate Sizes</label>
	<tip>Calculate folder sizes</tip>
	<icon1>#calculator</icon1>
	<function type="normal">
		<instruction>GetSizes EVERYTHING</instruction>
	</function>
</button>
```

- --

### Show File Properties

> [!what-this-does] Function
> Opens the Windows properties dialog for selected items.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Properties</label>
	<tip>Show file properties dialog</tip>
	<icon1>#properties</icon1>
	<function type="normal">
		<instruction>Properties</instruction>
	</function>
</button>
```

- --

## 🗂️ Navigation Operations

### Go to Desktop

> [!what-this-does] Function
> Navigates to the Desktop folder.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Desktop</label>
	<tip>Go to Desktop</tip>
	<icon1>#desktop</icon1>
	<function type="normal">
		<instruction>Go /desktop</instruction>
	</function>
</button>
```

- --

### Go to Downloads

> [!what-this-does] Function
> Navigates to the Downloads folder.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Downloads</label>
	<tip>Go to Downloads</tip>
	<icon1>#downloads</icon1>
	<function type="normal">
		<instruction>Go /downloads</instruction>
	</function>
</button>
```

- --

### Go to Documents

> [!what-this-does] Function
> Navigates to the Documents folder.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Documents</label>
	<tip>Go to Documents</tip>
	<icon1>#documents</icon1>
	<function type="normal">
		<instruction>Go /documents</instruction>
	</function>
</button>
```

- --

### Go to Obsidian Vault

> [!what-this-does] Function
> Quick navigation to [[Obsidian]] vault location. **Customize the path** to your vault.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Obsidian Vault</label>
	<tip>Go to Obsidian vault</tip>
	<icon1>#obsidian</icon1>
	<function type="normal">
		<instruction>Go "D:\Obsidian\MyVault"</instruction>
	</function>
</button>
```

- --

### Open in New Tab

> [!what-this-does] Function
> Opens selected folder in a new tab.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Open in New Tab</label>
	<tip>Open folder in new tab</tip>
	<icon1>#newtab</icon1>
	<function type="normal">
		<instruction>Go NEWTAB=def</instruction>
	</function>
</button>
```

- --

### Open in Other Pane

> [!what-this-does] Function
> Opens selected folder in the other dual-pane panel.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Open in Other Pane</label>
	<tip>Open folder in other pane</tip>
	<icon1>#dualpane</icon1>
	<function type="normal">
		<instruction>Go OPENINDEST</instruction>
	</function>
</button>
```

- --

### Swap Source and Destination

> [!what-this-does] Function
> Swaps the folder shown in dual-pane left and right panels.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Swap Panes</label>
	<tip>Swap source and destination panes</tip>
	<icon1>#swap</icon1>
	<function type="normal">
		<instruction>Go SWAP</instruction>
	</function>
</button>
```

- --

### Sync Destination to Source

> [!what-this-does] Function
> Makes the destination pane show the same folder as the source pane.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Sync Panes</label>
	<tip>Navigate destination to source location</tip>
	<icon1>#sync</icon1>
	<function type="normal">
		<instruction>Go CURRENT OPENINDEST</instruction>
	</function>
</button>
```

- --

## 🔍 View Operations

### Toggle Hidden Files

> [!what-this-does] Function
> Toggles visibility of hidden and system files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Toggle Hidden</label>
	<tip>Show/hide hidden files</tip>
	<icon1>#hidden</icon1>
	<function type="normal">
		<instruction>Set GLOBALHIDDENFILTER=!*</instruction>
	</function>
</button>
```

- --

### Toggle Flat View

> [!what-this-does] Function
> Enables/disables flat view showing all subfolder contents.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Toggle Flat View</label>
	<tip>Show all subfolder contents</tip>
	<icon1>#flatview</icon1>
	<function type="normal">
		<instruction>Set FLATVIEW=toggle,grouped</instruction>
	</function>
</button>
```

- --

### Toggle Dual Pane

> [!what-this-does] Function
> Shows/hides the second file pane.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Toggle Dual Pane</label>
	<tip>Show/hide dual pane</tip>
	<icon1>#dualpane</icon1>
	<function type="normal">
		<instruction>Set DUAL=toggle</instruction>
	</function>
</button>
```

- --

### Toggle Thumbnail View

> [!what-this-does] Function
> Switches between details view and thumbnail view.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Toggle Thumbnails</label>
	<tip>Switch to/from thumbnail view</tip>
	<icon1>#thumbnails</icon1>
	<function type="normal">
		<instruction>Set VIEW=thumbnails</instruction>
	</function>
</button>
```

- --

### Details View

> [!what-this-does] Function
> Switches to detailed list view with columns.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Details View</label>
	<tip>Switch to details view</tip>
	<icon1>#details</icon1>
	<function type="normal">
		<instruction>Set VIEW=details</instruction>
	</function>
</button>
```

- --

### Toggle Preview Pane

> [!what-this-does] Function
> Shows/hides the file preview pane.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Toggle Preview</label>
	<tip>Show/hide preview pane</tip>
	<icon1>#preview</icon1>
	<function type="normal">
		<instruction>Set VIEWPANE=toggle</instruction>
	</function>
</button>
```

- --

### Refresh View

> [!what-this-does] Function
> Forces refresh of the current folder view.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Refresh</label>
	<tip>Refresh current view</tip>
	<icon1>#refresh</icon1>
	<function type="normal">
		<instruction>Go REFRESH</instruction>
	</function>
</button>
```

- --

## 🛠️ Utility Operations

### Compare Files (Side by Side)

> [!what-this-does] Function
> Opens two selected files for comparison. **Requires external diff tool** (configure path).

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Compare Files</label>
	<tip>Compare two selected files</tip>
	<icon1>#compare</icon1>
	<function type="normal">
		<instruction>@filesonly</instruction>
		<instruction>@confirm:Select exactly 2 files to compare</instruction>
		<instruction>"C:\Program Files\WinMerge\WinMergeU.exe" "{allfilepath}"</instruction>
	</function>
</button>
```

> [!helpful-tip] Diff Tool Options
> Adjust path to your preferred comparison tool. Popular options: [[WinMerge]], [[Beyond Compare]], VS Code with `code --diff file1 file2`

- --

### Create File List

> [!what-this-does] Function
> Generates a text file listing all files in the current view.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Create File List</label>
	<tip>Generate text list of files</tip>
	<icon1>#list</icon1>
	<function type="normal">
		<instruction>Print FOLDER AS=txt TO="{sourcepath}\FileList_{date|yyyy-MM-dd}.txt"</instruction>
	</function>
</button>
```

- --

### Hash (MD5) Selected Files

> [!what-this-does] Function
> Calculates and displays [[MD5]] hash for selected files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>MD5 Hash</label>
	<tip>Calculate MD5 hash</tip>
	<icon1>#hash</icon1>
	<function type="normal">
		<instruction>Print HASH=md5</instruction>
	</function>
</button>
```

- --

### Hash (SHA256) Selected Files

> [!what-this-does] Function
> Calculates [[SHA-256]] hash for verification purposes.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>SHA256 Hash</label>
	<tip>Calculate SHA256 hash</tip>
	<icon1>#hash</icon1>
	<function type="normal">
		<instruction>Print HASH=sha256</instruction>
	</function>
</button>
```

- --

### Empty Recycle Bin

> [!what-this-does] Function
> Empties the Windows [[Recycle Bin]].

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Empty Recycle Bin</label>
	<tip>Empty the recycle bin</tip>
	<icon1>#trash</icon1>
	<function type="normal">
		<instruction>@confirm:Permanently delete all items in Recycle Bin?</instruction>
		<instruction>Delete EMPTYRECYCLE QUIET</instruction>
	</function>
</button>
```

- --

### Secure Delete

> [!what-this-does] Function
> Securely deletes files by overwriting before deletion. **Irreversible**.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Secure Delete</label>
	<tip>Securely delete with overwrite</tip>
	<icon1>#securedelete</icon1>
	<function type="normal">
		<instruction>@confirm:SECURE DELETE: Files will be permanently destroyed. Continue?</instruction>
		<instruction>Delete SECURE</instruction>
	</function>
</button>
```

> [!danger] Data Destruction
> Secure delete **overwrites file data** before deletion. This cannot be undone. Use with extreme caution.

- --

### Delete Empty Folders

> [!what-this-does] Function
> Removes all empty subfolders within the current directory.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Delete Empty Folders</label>
	<tip>Remove empty subfolders</tip>
	<icon1>#deleteempty</icon1>
	<function type="normal">
		<instruction>@confirm:Delete all empty subfolders?</instruction>
		<instruction>Delete EMPTYONLY QUIET</instruction>
	</function>
</button>
```

- --

## 📋 Batch Operations Menu

### Batch Rename (Advanced Dialog)

> [!what-this-does] Function
> Opens the advanced rename dialog with full [[regex]] and scripting support.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Advanced Rename</label>
	<tip>Open advanced rename dialog</tip>
	<icon1>#rename</icon1>
	<function type="normal">
		<instruction>Rename ADVANCED</instruction>
	</function>
</button>
```

- --

### Touch Files (Update Timestamps)

> [!what-this-does] Function
> Updates modification timestamp to current time for selected files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Touch Files</label>
	<tip>Update modification time to now</tip>
	<icon1>#time</icon1>
	<function type="normal">
		<instruction>SetAttr MODIFIED=now</instruction>
	</function>
</button>
```

- --

### Set Date from Filename

> [!what-this-does] Function
> Sets file date from patterns in filename (e.g., `2024-01-15_document.pdf`).

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Date from Filename</label>
	<tip>Set file date from filename pattern</tip>
	<icon1>#time</icon1>
	<function type="normal">
		<instruction>SetAttr MODIFIED="{file|name|regex:(\d{4}[-_]\d{2}[-_]\d{2})}"</instruction>
	</function>
</button>
```

- --

### Remove Read-Only Attribute

> [!what-this-does] Function
> Removes read-only flag from selected files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Remove Read-Only</label>
	<tip>Clear read-only attribute</tip>
	<icon1>#unlock</icon1>
	<function type="normal">
		<instruction>SetAttr ATTR=-r</instruction>
	</function>
</button>
```

- --

### Set Hidden Attribute

> [!what-this-does] Function
> Marks selected files as hidden.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Set Hidden</label>
	<tip>Mark files as hidden</tip>
	<icon1>#hidden</icon1>
	<function type="normal">
		<instruction>SetAttr ATTR=+h</instruction>
	</function>
</button>
```

- --

### Clear Hidden Attribute

> [!what-this-does] Function
> Removes hidden flag from selected files.

```xml
<?xml version="1.0"?>
<button backcol="none" display="both" label_pos="right" textcol="none">
	<label>Clear Hidden</label>
	<tip>Remove hidden attribute</tip>
	<icon1>#show</icon1>
	<function type="normal">
		<instruction>SetAttr ATTR=-h</instruction>
	</function>
</button>
```

- --

## 📑 Quick Reference: Command Modifiers

> [!definition] DOpus Command Modifiers
> These prefixes modify how commands execute:

| Modifier | Function |
|----------|----------|
| `@nodeselect` | Prevents deselecting files after operation |
| `@confirm:` | Shows confirmation dialog with message |
| `@admin` | Requests administrator elevation |
| `@runmode:hide` | Hides command window |
| `@filesonly` | Only operates on files (ignores folders) |
| `@dirsonly` | Only operates on directories |
| `@ifexists:` | Conditional execution if file/path exists |
| `@async:` | Runs command asynchronously |

- --

## 📑 Quick Reference: Variables

> [!definition] DOpus Built-in Variables
> Common variables for dynamic button construction:

| Variable | Outputs |
|----------|---------|
| `{file}` | Full filename with extension |
| `{file|noext}` | Filename without extension |
| `{file|ext}` | Extension only |
| `{filepath}` | Full path including filename |
| `{sourcepath}` | Current folder path |
| `{destpath}` | Destination pane path |
| `{date|format}` | Current date (format: yyyy-MM-dd, etc.) |
| `{dlgstring|prompt}` | User input dialog |
| `{allfilepath}` | All selected files as space-separated paths |

- --

# 🔗 Related Topics for PKB Expansion

## Core Extensions

### 1. **[[Directory Opus Scripting]]**
* *Connection:** These buttons use basic commands; scripting enables complex multi-step automation
* *Depth Potential:** [[JScript]] and [[VBScript]] support allows conditional logic, loops, and external tool integration
* *Knowledge Graph Role:** Advanced automation layer building on button fundamentals
* *Priority:** High --- unlocks significantly more powerful workflows
* *Prerequisites:** [[Directory Opus Button Basics]], [[JavaScript Fundamentals]]

### 2. **[[Directory Opus Rename Scripts]]**
* *Connection:** Rename buttons are among most used; advanced rename scripts enable regex, metadata extraction, and batch operations
* *Depth Potential:** Regular expression renaming, [[EXIF]] date extraction, music tag integration
* *Knowledge Graph Role:** Specialized renaming reference extending file operation buttons
* *Priority:** High --- rename operations are daily workflow
* *Prerequisites:** [[Regular Expressions]], [[Metadata Understanding]]

## Cross-Domain Connections

### 3. **[[File Management Workflow Design]]**
* *Connection:** Individual buttons should serve cohesive workflow purposes
* *Depth Potential:** Principles of [[GTD]], [[PARA]], and [[file taxonomy]] applied to button toolbar organization
* *Knowledge Graph Role:** Bridges productivity methodology to technical implementation
* *Priority:** Medium --- systematic approach improves long-term usability
* *Prerequisites:** [[Personal Productivity Systems]]

### 4. **[[Windows Shell Integration]]**
* *Connection:** Many buttons interface with Windows shell commands and external tools
* *Depth Potential:** [[PowerShell]] integration, [[context menu]] extensions, [[registry]] customization
* *Knowledge Graph Role:** Operating system layer supporting file management tools
* *Priority:** Medium --- deeper Windows knowledge enables more powerful buttons
* *Prerequisites:** [[Windows Command Line Basics]]

## Advanced Deep Dives

### 5. **[[Directory Opus Evaluator Functions]]** *[Requires prerequisites]*
* *Connection:** Evaluator columns and buttons enable dynamic computed values
* *Depth Potential:** Custom columns, conditional formatting, dynamic labels
* *Knowledge Graph Role:** Advanced customization extending basic button functionality
* *Priority:** Low --- specialized need for power users
* *Prerequisites:** [[Directory Opus Scripting]], [[Basic Programming Logic]]

### 6. **[[Multi-Tool Automation Pipelines]]** *[Requires prerequisites]*
* *Connection:** Buttons can trigger external tools; pipelines chain multiple tools together
* *Depth Potential:** ImageMagick integration, FFmpeg processing, PDF manipulation chains
* *Knowledge Graph Role:** Cross-tool automation building on single-tool buttons
* *Priority:** Low --- specialized workflows requiring specific tool combinations
* *Prerequisites:** [[CLI Tool Proficiency]], [[Directory Opus Scripting]]

- --