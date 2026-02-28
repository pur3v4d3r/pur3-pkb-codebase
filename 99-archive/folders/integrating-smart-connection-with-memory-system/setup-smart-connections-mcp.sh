#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════
# Smart Connections + LLM Memory Integration Setup Script
# ═══════════════════════════════════════════════════════════════════════════
# 
# This script sets up the Smart Connections MCP server for use with:
# - Claude Desktop
# - Gemini (via proxy)
# - Local LLMs (Ollama, LM Studio)
#
# Prerequisites:
# - Node.js >= 18
# - Obsidian with Smart Connections plugin installed and indexed
# - Your vault path known
#
# Usage:
#   chmod +x setup-smart-connections-mcp.sh
#   ./setup-smart-connections-mcp.sh /path/to/your/vault
#
# ═══════════════════════════════════════════════════════════════════════════

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ─────────────────────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────────────────────

print_header() {
    echo -e "\n${CYAN}═══════════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════════${NC}\n"
}

print_step() {
    echo -e "${BLUE}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# ─────────────────────────────────────────────────────────────────────────────
# Validation
# ─────────────────────────────────────────────────────────────────────────────

validate_prerequisites() {
    print_header "Checking Prerequisites"
    
    # Check Node.js
    print_step "Checking Node.js..."
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
        if [ "$NODE_VERSION" -ge 18 ]; then
            print_success "Node.js $(node -v) installed"
        else
            print_error "Node.js 18+ required. Current version: $(node -v)"
            exit 1
        fi
    else
        print_error "Node.js not found. Please install Node.js 18+"
        exit 1
    fi
    
    # Check npm
    print_step "Checking npm..."
    if command -v npm &> /dev/null; then
        print_success "npm $(npm -v) installed"
    else
        print_error "npm not found"
        exit 1
    fi
    
    # Check vault path argument
    if [ -z "$1" ]; then
        print_error "Vault path not provided"
        echo -e "Usage: $0 /path/to/your/vault"
        exit 1
    fi
    
    VAULT_PATH="$1"
    
    # Validate vault path
    print_step "Validating vault path: $VAULT_PATH"
    if [ ! -d "$VAULT_PATH" ]; then
        print_error "Vault path does not exist: $VAULT_PATH"
        exit 1
    fi
    
    # Check for .obsidian folder
    if [ ! -d "$VAULT_PATH/.obsidian" ]; then
        print_error "Not an Obsidian vault (missing .obsidian folder)"
        exit 1
    fi
    print_success "Valid Obsidian vault found"
    
    # Check for Smart Connections
    print_step "Checking for Smart Connections..."
    if [ -d "$VAULT_PATH/.obsidian/plugins/smart-connections" ]; then
        print_success "Smart Connections plugin installed"
    else
        print_warning "Smart Connections plugin not found"
        echo -e "  Please install from Obsidian Community Plugins"
    fi
    
    # Check for embeddings
    print_step "Checking for Smart Connections embeddings..."
    if [ -f "$VAULT_PATH/.smart-env/smart_sources.json" ] || [ -d "$VAULT_PATH/.smart-env/multi" ]; then
        print_success "Embeddings found"
    else
        print_warning "No embeddings found yet"
        echo -e "  Open Obsidian and let Smart Connections index your vault"
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# Installation
# ─────────────────────────────────────────────────────────────────────────────

install_mcp_package() {
    print_header "Installing Smart Connections MCP Package"
    
    print_step "Installing @yejianye/smart-connections-mcp globally..."
    npm install -g @yejianye/smart-connections-mcp
    print_success "MCP package installed"
    
    # Verify smart-cli is available
    print_step "Verifying smart-cli installation..."
    if command -v smart-cli &> /dev/null; then
        print_success "smart-cli command available"
    else
        print_warning "smart-cli not in PATH - you may need to restart terminal"
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# Claude Desktop Configuration
# ─────────────────────────────────────────────────────────────────────────────

configure_claude_desktop() {
    print_header "Configuring Claude Desktop"
    
    # Detect OS
    case "$(uname -s)" in
        Darwin)
            CONFIG_DIR="$HOME/Library/Application Support/Claude"
            ;;
        Linux)
            CONFIG_DIR="$HOME/.config/Claude"
            ;;
        MINGW*|MSYS*|CYGWIN*)
            CONFIG_DIR="$APPDATA/Claude"
            ;;
        *)
            print_warning "Unknown OS - manual configuration required"
            return
            ;;
    esac
    
    CONFIG_FILE="$CONFIG_DIR/claude_desktop_config.json"
    
    print_step "Claude Desktop config location: $CONFIG_FILE"
    
    # Create config directory if needed
    if [ ! -d "$CONFIG_DIR" ]; then
        print_step "Creating config directory..."
        mkdir -p "$CONFIG_DIR"
    fi
    
    # Create or update config
    if [ -f "$CONFIG_FILE" ]; then
        print_warning "Existing config found - backing up..."
        cp "$CONFIG_FILE" "${CONFIG_FILE}.backup.$(date +%Y%m%d%H%M%S)"
        
        # Check if smart-connections already configured
        if grep -q "smart-connections" "$CONFIG_FILE"; then
            print_warning "smart-connections already in config - please update manually"
            echo -e "  Config location: $CONFIG_FILE"
            return
        fi
    fi
    
    # Generate config
    print_step "Writing Claude Desktop configuration..."
    
    cat > "$CONFIG_FILE" << EOF
{
  "mcpServers": {
    "smart-connections": {
      "command": "npx",
      "args": ["-y", "@yejianye/smart-connections-mcp"],
      "env": {
        "OBSIDIAN_VAULT": "$VAULT_PATH"
      }
    }
  }
}
EOF
    
    print_success "Claude Desktop configured"
    echo -e "  Config file: $CONFIG_FILE"
    echo -e ""
    echo -e "  ${YELLOW}⚠ IMPORTANT: Restart Claude Desktop completely for changes to take effect${NC}"
}

# ─────────────────────────────────────────────────────────────────────────────
# Environment Setup
# ─────────────────────────────────────────────────────────────────────────────

setup_environment() {
    print_header "Setting Up Environment Variables"
    
    # Detect shell config file
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    
    print_step "Adding OBSIDIAN_VAULT to $SHELL_CONFIG"
    
    # Check if already set
    if grep -q "OBSIDIAN_VAULT" "$SHELL_CONFIG" 2>/dev/null; then
        print_warning "OBSIDIAN_VAULT already in $SHELL_CONFIG"
    else
        echo "" >> "$SHELL_CONFIG"
        echo "# Smart Connections MCP Configuration" >> "$SHELL_CONFIG"
        echo "export OBSIDIAN_VAULT=\"$VAULT_PATH\"" >> "$SHELL_CONFIG"
        print_success "Environment variable added"
        echo -e "  Run: source $SHELL_CONFIG"
    fi
    
    # Set for current session
    export OBSIDIAN_VAULT="$VAULT_PATH"
    print_success "OBSIDIAN_VAULT set for current session"
}

# ─────────────────────────────────────────────────────────────────────────────
# Testing
# ─────────────────────────────────────────────────────────────────────────────

test_installation() {
    print_header "Testing Installation"
    
    export OBSIDIAN_VAULT="$VAULT_PATH"
    
    print_step "Testing smart-cli stats..."
    if smart-cli stats 2>/dev/null; then
        print_success "smart-cli working correctly"
    else
        print_warning "smart-cli test failed - check if embeddings exist"
    fi
    
    print_step "Testing semantic lookup..."
    if smart-cli lookup "test query" --limit=1 2>/dev/null; then
        print_success "Semantic search working"
    else
        print_warning "Semantic search test failed"
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# Memory Directory Setup
# ─────────────────────────────────────────────────────────────────────────────

setup_memory_directory() {
    print_header "Setting Up Memory Directory"
    
    MEMORY_DIR="$VAULT_PATH/.claude"
    
    if [ -d "$MEMORY_DIR" ]; then
        print_success "Memory directory already exists: $MEMORY_DIR"
    else
        print_step "Creating memory directory structure..."
        
        mkdir -p "$MEMORY_DIR/core"
        mkdir -p "$MEMORY_DIR/task-logs"
        mkdir -p "$MEMORY_DIR/plans"
        mkdir -p "$MEMORY_DIR/errors"
        
        # Create initial files
        cat > "$MEMORY_DIR/core/activeContext.md" << 'EOF'
---
type: working-memory
created: $(date +%Y-%m-%d)
modified: $(date +%Y-%m-%d)
status: active
---

# Active Context

## Current Focus
[Initial setup - no active work yet]

## Session Notes
Memory system initialized.
EOF

        cat > "$MEMORY_DIR/memory-index.md" << 'EOF'
---
type: index
created: $(date +%Y-%m-%d)
---

# Memory Index

## Core Memory Files
- [[activeContext]] - Current working state
- [[projectbrief]] - Project overview
- [[systemPatterns]] - Architecture patterns
- [[techContext]] - Technology stack

## Quick Navigation
- **Start work**: Read activeContext → Create plan → Execute
- **Resume work**: Load activeContext → Check progress → Continue
EOF

        print_success "Memory directory created: $MEMORY_DIR"
    fi
    
    # Verify memory dir is not excluded
    print_step "Checking Smart Connections exclusions..."
    SC_CONFIG="$VAULT_PATH/.obsidian/plugins/smart-connections/data.json"
    
    if [ -f "$SC_CONFIG" ]; then
        if grep -q ".claude" "$SC_CONFIG" && grep -q "exclude" "$SC_CONFIG"; then
            print_warning "Check if .claude is in Smart Connections exclusions"
            echo -e "  Settings → Smart Connections → Exclusions"
        else
            print_success "Memory directory should be indexed"
        fi
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────

print_summary() {
    print_header "Setup Complete!"
    
    echo -e "${GREEN}✓ Smart Connections MCP server installed${NC}"
    echo -e "${GREEN}✓ Claude Desktop configured${NC}"
    echo -e "${GREEN}✓ Environment variables set${NC}"
    echo -e "${GREEN}✓ Memory directory created${NC}"
    echo -e ""
    echo -e "${CYAN}Next Steps:${NC}"
    echo -e ""
    echo -e "1. ${YELLOW}Restart Claude Desktop completely${NC}"
    echo -e "   (Quit and reopen, don't just close window)"
    echo -e ""
    echo -e "2. ${YELLOW}Open Obsidian${NC} and let Smart Connections index"
    echo -e "   Check that .claude folder is being indexed"
    echo -e ""
    echo -e "3. ${YELLOW}Test in Claude Desktop:${NC}"
    echo -e "   Ask: \"Search my vault for notes about [topic]\""
    echo -e ""
    echo -e "4. ${YELLOW}Test CLI:${NC}"
    echo -e "   smart-cli lookup \"your search query\""
    echo -e "   smart-cli stats"
    echo -e ""
    echo -e "${CYAN}Vault Path:${NC} $VAULT_PATH"
    echo -e "${CYAN}Memory Dir:${NC} $VAULT_PATH/.claude"
    echo -e ""
    echo -e "${CYAN}Documentation:${NC}"
    echo -e "  https://github.com/yejianye/ob-smart-connections-mcp"
    echo -e ""
}

# ─────────────────────────────────────────────────────────────────────────────
# Main Execution
# ─────────────────────────────────────────────────────────────────────────────

main() {
    echo -e "${CYAN}"
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║     Smart Connections + LLM Memory Integration Setup              ║"
    echo "║     Auto-Embedding Memory System for Claude/Gemini/Local LLMs     ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    validate_prerequisites "$1"
    install_mcp_package
    configure_claude_desktop
    setup_environment
    setup_memory_directory
    test_installation
    print_summary
}

# Run main with vault path argument
main "$1"
