# 🏗️ Repomix Configuration Architect - Quick Start

## What is This?

This is a **meta-prompt** - a prompt you give to a coder LLM (like Claude, GPT-4, etc.) that will generate comprehensive, production-ready Repomix configurations for you.

## Quick Usage

### Step 1: Copy the Prompt

Copy the entire contents of `repomix-config-architect-v1.0.md` to your coder LLM.

### Step 2: Provide Context (Optional)

Tell the LLM about your specific needs:

```
I need Repomix configurations for:
- Repository type: [PKB/codebase/documentation]
- Primary content: [markdown/code/mixed]
- Size: [small/medium/large]
- Use case: [AI analysis/documentation/archival]
```

### Step 3: Get Your Outputs

The LLM will generate:

✅ **5 JSON Configuration Files**
- repomix-minimal.json (fast, lightweight)
- repomix-standard.json (balanced, general-purpose)
- repomix-comprehensive.json (maximum detail)
- repomix-pkb.json (optimized for knowledge bases)
- repomix-secure.json (production-grade security)

✅ **3 Instruction Files**
- AI-optimized usage instructions for each variant

✅ **2 Automation Scripts**
- repomix-manager.sh (Bash)
- repomix-manager.py (Python)

✅ **Complete Documentation**
- Usage guides
- Best practices
- Troubleshooting

## Key Features

### 🎯 Multiple Variants for Different Use Cases

Each configuration is optimized for specific scenarios:

- **Speed**: Get results fast (20-40% tokens)
- **Balance**: General purpose (50-70% tokens)
- **Completeness**: Maximum context (90-100% tokens)
- **PKB**: Knowledge bases and prompts (60-80% tokens)
- **Security**: Production deployment (40-60% tokens, sanitized)

### 🔒 Security-First

All configurations enforce security checks by default and include comprehensive ignore patterns for sensitive data.

### 🤖 AI-Optimized

Every configuration includes:
- Metadata for AI understanding
- Token count estimates
- Use case documentation
- AI instruction files

### 🛠️ Automation Ready

Both Bash and Python scripts provide:
- Interactive menus
- Batch processing
- Validation
- Comparison tools
- Logging

## Directory Structure

After running this prompt with an LLM, you'll have:

```
project-root/
├── configs/
│   ├── repomix-minimal.json
│   ├── repomix-standard.json
│   ├── repomix-comprehensive.json
│   ├── repomix-pkb.json
│   └── repomix-secure.json
├── instructions/
│   ├── repomix-standard-instructions.md
│   ├── repomix-pkb-instructions.md
│   └── repomix-security-instructions.md
├── scripts/
│   ├── repomix-manager.sh
│   └── repomix-manager.py
└── docs/
    ├── USAGE_GUIDE.md
    ├── README.md
    └── TROUBLESHOOTING.md
```

## Example Workflow

### 1. Generate Configs with LLM

```
User to LLM:
"Generate Repomix configurations for my PKB repository 
focused on prompt engineering materials."

LLM Response:
[Generates all 5 configs + scripts + docs customized for PKB use case]
```

### 2. Save Files

Save each generated file to the appropriate directory.

### 3. Run Configuration

```bash
# Using Python script
python scripts/repomix-manager.py run repomix-pkb --target /path/to/pkb

# Using Bash script
./scripts/repomix-manager.sh
# Then select option 2 and choose repomix-pkb
```

### 4. Get AI-Ready Output

```
outputs/
└── repomix-pkb.xml  # Ready to feed to any LLM
```

## Customization

The generated configurations are fully customizable. Edit any JSON file to:

- Adjust file size limits
- Modify include/exclude patterns
- Enable/disable compression
- Add custom header text
- Configure git integration

Example:
```json
{
  "ignore": {
    "customPatterns": [
      "**/my-private-folder/**",
      "**/*.backup"
    ]
  }
}
```

## Best Practices

### For PKB Repositories
Use **repomix-pkb.json** - optimized for markdown, prompts, and documentation.

### For Code Reviews
Use **repomix-standard.json** - balanced completeness and efficiency.

### For Production Deployment
Use **repomix-secure.json** - maximum security with aggressive filtering.

### For Quick Analysis
Use **repomix-minimal.json** - fastest processing, smallest output.

### For Archival
Use **repomix-comprehensive.json** - maximum detail with git history.

## Troubleshooting

### Q: Output too large for LLM context window?
**A**: Switch to a lighter variant (minimal or standard) or add more exclude patterns.

### Q: Missing important files?
**A**: Check include patterns in config and review .gitignore.

### Q: Security check flagging false positives?
**A**: Create a `.repomixignore` file with exceptions.

### Q: Scripts not executable?
**A**: Run `chmod +x scripts/*.sh` on Unix systems.

## Requirements

- **Repomix CLI**: `npm install -g repomix`
- **Python** (for Python script): 3.8+
- **Bash** (for Bash script): 4.0+
- **jq** (for Bash script): Install via package manager

## Advanced Usage

### Batch Processing Multiple Repos

```bash
for repo in repo1 repo2 repo3; do
  python scripts/repomix-manager.py run repomix-standard --target "$repo"
done
```

### CI/CD Integration

```yaml
- name: Generate Repomix output
  run: |
    repomix . --config configs/repomix-minimal.json
    
- name: Upload artifact
  uses: actions/upload-artifact@v2
  with:
    path: repomix-output.xml
```

### Custom Variant Creation

```bash
# Copy template
cp configs/repomix-standard.json configs/repomix-custom.json

# Edit as needed
vim configs/repomix-custom.json

# Validate
python scripts/repomix-manager.py validate repomix-custom

# Run
python scripts/repomix-manager.py run repomix-custom
```

## Support

- **Repomix Documentation**: https://repomix.com/
- **GitHub**: https://github.com/yamadashy/repomix
- **Schema**: https://repomix.com/schemas/latest/schema.json

## What Makes This Different?

Most Repomix configs are basic examples. This prompt generates:

✨ **Production-grade** configurations with comprehensive documentation
✨ **Multiple variants** optimized for different use cases
✨ **Automation scripts** for workflow efficiency
✨ **AI-optimized** outputs with metadata and instructions
✨ **Security-first** defaults with comprehensive filtering
✨ **Customization-ready** with clear extension points

## Version

**Repomix Configuration Architect v1.0.0**

Generated by: Prompt Engineering Agent v4.0  
Based on: Repomix latest schema  
Date: 2024-12-28

---

**Ready to generate your configs?** Feed the main prompt to your favorite coder LLM and get production-ready Repomix configurations in seconds! 🚀
