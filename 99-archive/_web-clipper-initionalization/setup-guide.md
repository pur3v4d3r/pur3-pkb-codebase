# 🛠️ Obsidian Web Clipper Setup Guide

> [!abstract] Overview
> Complete installation and configuration guide for the Pur3v4d3r Web Clipper System. Follow these steps to get fully operational.

---

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [x] **Obsidian** v1.7.2 or later installed
- [x] **Web browser**: Chrome, Firefox, Safari, Edge, Brave, or Arc
- [x] **API Key** for one of these LLM providers:
  - Anthropic Claude (recommended: Claude Haiku for speed)
  - OpenAI (GPT-4o-mini recommended)
  - Google Gemini (Gemini Flash recommended)
  - Ollama (for local/private processing)

---

## Step 1: Install the Web Clipper Extension

### Chrome/Brave/Edge/Arc
1. Visit [Chrome Web Store - Obsidian Web Clipper](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf)
2. Click "Add to Chrome"
3. Confirm the installation

### Firefox
1. Visit [Firefox Add-ons - Obsidian Web Clipper](https://addons.mozilla.org/en-US/firefox/addon/web-clipper-obsidian/)
2. Click "Add to Firefox"
3. Confirm the installation

### Safari (macOS/iOS)
1. Visit [Safari Extensions](https://apps.apple.com/app/obsidian-web-clipper/id6720708363)
2. Install from the App Store
3. Enable in Safari Preferences → Extensions

### Verify Installation
- You should see the Obsidian icon in your browser toolbar
- If hidden, click the puzzle piece icon to find it

---

## Step 2: Connect to Your Vault

1. **Click the Obsidian icon** in your browser toolbar
2. **Click the Settings gear** (⚙️) in the top-right of the popup
3. Navigate to **General** settings
4. Under **Vaults**, click **"Add vault"**
5. Enter your vault name exactly as it appears in Obsidian
6. Click **Save**

> [!tip] Multiple Vaults
> You can add multiple vaults and switch between them when clipping.

---

## Step 3: Configure the Interpreter (AI Processing)

This is where the magic happens. The Interpreter enables AI-powered content processing.

### 3.1 Enable Interpreter
1. In Web Clipper Settings, go to **Interpreter**
2. Toggle **Enable Interpreter** to ON
3. Choose **Auto-run** or **Manual** mode:
   - **Auto-run**: AI processes immediately when you clip (uses API credits)
   - **Manual**: Click "Interpret" button to trigger AI (more control)

### 3.2 Add Your LLM Provider

#### Option A: Anthropic Claude (Recommended)
1. Click **"Add Provider"**
2. Select **Anthropic** from presets
3. Enter your API key from [console.anthropic.com](https://console.anthropic.com)
4. Click **"Add Model"**
5. Select **claude-3-haiku-20240307** (fast, cheap, accurate)
6. Or **claude-3-5-sonnet-20241022** (better quality, slower)

#### Option B: OpenAI
1. Click **"Add Provider"**
2. Select **OpenAI** from presets
3. Enter your API key from [platform.openai.com](https://platform.openai.com)
4. Add model: **gpt-4o-mini** (recommended for speed/cost)

#### Option C: Google Gemini
1. Click **"Add Provider"**
2. Select **Google AI** from presets
3. Enter your API key from [aistudio.google.com](https://aistudio.google.com)
4. Add model: **gemini-1.5-flash** (fast, generous free tier)

#### Option D: Ollama (Local/Private)
1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull a model: `ollama pull llama3.2:3b` or `ollama pull qwen2.5:7b`
3. In Web Clipper, add provider:
   - Name: Ollama
   - Base URL: `http://localhost:11434/v1`
   - No API key needed
4. Add your model name

### 3.3 Set Default Model
1. After adding providers/models, select your preferred default
2. This model will be used for all Interpreter operations

---

## Step 4: Import the Templates

### Method 1: Drag and Drop (Easiest)
1. Download the template JSON files from this system
2. In Web Clipper Settings, go to **Templates**
3. Drag the `.json` files directly into the templates area
4. They'll be imported automatically

### Method 2: Copy/Paste
1. Open a template JSON file in a text editor
2. In Web Clipper Settings → Templates, click **"New template"**
3. Click **"More" (⋮)** → **"Edit JSON"**
4. Paste the JSON content
5. Click **Save**

### Method 3: Import Button
1. In Web Clipper Settings → Templates
2. Click **Import** in the top-right
3. Select your JSON template files
4. Confirm import

### Verify Templates
After import, you should see:
- Pur3v4d3r Universal
- Pur3v4d3r Research Article
- Pur3v4d3r Video Transcript
- Pur3v4d3r Documentation
- Pur3v4d3r Quick Capture
- Pur3v4d3r Definition Extractor

---

## Step 5: Configure Template Paths

Adjust the `path` in each template to match your vault structure:

| Template | Default Path | Change To |
|----------|--------------|-----------|
| Universal | `00-inbox/webclips` | Your inbox folder |
| Research Article | `03-notes/literature` | Your literature notes folder |
| Video Transcript | `03-notes/media` | Your media notes folder |
| Documentation | `03-notes/reference` | Your reference folder |
| Quick Capture | `00-inbox/webclips` | Your quick capture folder |
| Definition Extractor | `03-notes/reference` | Your glossary folder |

### To Edit Paths:
1. Click on a template in Settings
2. Find the **"Path"** field
3. Enter your desired folder path
4. Changes save automatically

---

## Step 6: Import Your Properties (Optional)

If you have existing YAML properties in your vault:

1. In Web Clipper Settings, go to **Properties**
2. Click **"Import from vault"**
3. Select your vault
4. The clipper will detect your existing property types
5. This helps with autocomplete when editing templates

---

## Step 7: Test Your Setup

### Test 1: Quick Capture
1. Visit any article (e.g., a Wikipedia page)
2. Click the Obsidian icon
3. Select **"Pur3v4d3r Quick Capture"**
4. Click **"Add to Obsidian"**
5. Check your vault - the note should appear

### Test 2: AI Processing
1. Visit an article with substantive content
2. Click the Obsidian icon
3. Select **"Pur3v4d3r Universal"**
4. If Auto-run is off, click **"Interpret"**
5. Wait for AI processing (10-30 seconds)
6. Review the generated metadata and content
7. Click **"Add to Obsidian"**

### Test 3: YouTube
1. Visit a YouTube video
2. **Important**: Open the transcript panel (click "...More" → "Show transcript")
3. Click the Obsidian icon
4. Select **"Pur3v4d3r Video Transcript"**
5. Click **"Interpret"** then **"Add to Obsidian"**

---

## 🎛️ Recommended Settings

### General Settings
- **Default behavior**: Create (not append)
- **Show notifications**: On
- **Open note after saving**: Your preference

### Hotkeys (Customize to your preference)
- **Open clipper**: `Ctrl/Cmd + Shift + O`
- **Quick clip**: `Ctrl/Cmd + Shift + S`
- **Toggle highlighter**: `Ctrl/Cmd + Shift + H`

### Interpreter Settings
- **Auto-run**: Off (recommended to control API costs)
- **Default model**: Claude Haiku or Gemini Flash (fast, cheap)

---

## 🔧 Troubleshooting

### "Vault not found"
- Ensure Obsidian is running
- Verify vault name matches exactly (case-sensitive)
- Try removing and re-adding the vault

### "Interpreter not working"
- Verify API key is correct
- Check you have credits/quota with your provider
- Try a different model
- Check browser console for errors (F12 → Console)

### "Template not triggering"
- Check the template's triggers match the URL
- Try manually selecting the template
- Verify template JSON is valid

### "Content not captured correctly"
- Some sites have unusual DOM structures
- Try editing the `context` selector in the template
- Use the highlighter to manually select content

### "AI output has errors"
- Reduce context size (edit `slice:0,8000` to smaller number)
- Try a more capable model
- Simplify the prompt variables

---

## 📚 Next Steps

After setup is complete:

1. **Customize templates** to match your exact metadata schema
2. **Test with different content types** to verify triggers work
3. **Adjust prompts** based on output quality
4. **Create additional templates** for specific sites you frequent
5. **Review the Interpreter Prompts** folder for customization ideas

---

## 📖 Resources

- [Official Web Clipper Documentation](https://help.obsidian.md/web-clipper)
- [Web Clipper Variables Reference](https://help.obsidian.md/web-clipper/variables)
- [Web Clipper Filters Reference](https://help.obsidian.md/web-clipper/filters)
- [Community Templates Repository](https://github.com/obsidian-community/web-clipper-templates)
- [Obsidian Discord - #obsidian-clipper channel](https://discord.gg/obsidianmd)

---

*Setup complete! Start capturing knowledge.* 🚀
