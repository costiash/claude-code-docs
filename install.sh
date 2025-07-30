#!/bin/bash
set -euo pipefail

# Claude Code Docs Installer v0.3 - Fixed location with migration support
# This script installs/migrates claude-code-docs to ~/.claude-code-docs

echo "Claude Code Docs Installer v0.3"
echo "==============================="

# Fixed installation location
INSTALL_DIR="$HOME/.claude-code-docs"

# Detect OS type
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
    echo "✓ Detected macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="linux"
    echo "✓ Detected Linux"
else
    echo "❌ Error: Unsupported OS type: $OSTYPE"
    echo "This installer supports macOS and Linux only"
    exit 1
fi

# Check dependencies
echo "Checking dependencies..."
for cmd in git jq curl; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "❌ Error: $cmd is required but not installed"
        echo "Please install $cmd and try again"
        exit 1
    fi
done
echo "✓ All dependencies satisfied"

# Function to detect user modifications in a directory
detect_user_modifications() {
    local dir="$1"
    local custom_files=()
    
    # Expected files that come with the repo
    local expected_patterns=(
        "install.sh"
        "uninstall.sh"
        "README.md"
        "LICENSE"
        "CLAUDE.md"
        "UNINSTALL.md"
        "TODO-v0.3.md"
        ".gitignore"
        ".git/*"
        ".github/*"
        "docs/*.md"
        "docs/docs_manifest.json"
        "scripts/fetch_claude_docs.py"
        "scripts/requirements.txt"
        "scripts/claude-docs-helper.sh.template"
    )
    
    # Build find command arguments in an array
    local find_args=("$dir" "-type" "f")
    for pattern in "${expected_patterns[@]}"; do
        find_args+=("!" "-path" "$dir/$pattern")
    done
    
    # Execute find and collect custom files
    while IFS= read -r file; do
        # Skip .git internals
        if [[ "$file" =~ \.git/ ]]; then
            continue
        fi
        # Remove directory prefix for cleaner output
        custom_files+=("${file#$dir/}")
    done < <(find "${find_args[@]}" 2>/dev/null || true)
    
    printf '%s\n' "${custom_files[@]}"
}

# Function to find existing installations
find_existing_installations() {
    local installations=()
    
    # Current directory (if it has the manifest)
    if [[ -f "./docs/docs_manifest.json" && "$(pwd)" != "$INSTALL_DIR" ]]; then
        installations+=("$(pwd)")
    fi
    
    # Common installation locations
    local common_paths=(
        "$HOME/claude-code-docs"
        "$HOME/Projects/claude-code-docs"
        "$HOME/Documents/claude-code-docs"
        "$HOME/workspace/claude-code-docs"
        "$HOME/repos/claude-code-docs"
        "$HOME/src/claude-code-docs"
        "$HOME/code/claude-code-docs"
    )
    
    for path in "${common_paths[@]}"; do
        if [[ -d "$path" && -f "$path/docs/docs_manifest.json" && "$path" != "$INSTALL_DIR" ]]; then
            installations+=("$path")
        fi
    done
    
    # Remove duplicates
    printf '%s\n' "${installations[@]}" | sort -u
}

# Function to migrate from old location
migrate_installation() {
    local old_dir="$1"
    local user_files="$2"
    
    echo "Migrating from: $old_dir"
    echo "To: $INSTALL_DIR"
    
    # Create install directory
    mkdir -p "$INSTALL_DIR"
    
    # If old installation has .git, preserve it
    if [[ -d "$old_dir/.git" ]]; then
        echo "Preserving git history..."
        cp -R "$old_dir/.git" "$INSTALL_DIR/"
        
        # Reset to clean state in new location
        cd "$INSTALL_DIR"
        git reset --hard HEAD 2>/dev/null || true
        git clean -fd 2>/dev/null || true
        
        # Pull latest
        echo "Updating to latest version..."
        git pull --quiet origin main || echo "  (Could not pull latest changes)"
    else
        # No git history, clone fresh
        echo "Cloning fresh repository..."
        git clone https://github.com/ericbuess/claude-code-docs.git "$INSTALL_DIR"
    fi
    
    
    # Create migration info
    local migration_info="{
  \"migrated_from\": \"$old_dir\",
  \"migration_date\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
  \"old_dir_safe_to_delete\": $([ -z "$user_files" ] && echo "true" || echo "false"),
  \"user_files_detected\": ["
    
    if [[ -n "$user_files" ]]; then
        # Add user files to JSON array
        local first=true
        while IFS= read -r file; do
            [[ -z "$file" ]] && continue
            [[ "$first" == "true" ]] && first=false || migration_info+=","
            migration_info+="
    \"$file\""
        done <<< "$user_files"
    fi
    
    migration_info+="
  ]
}"
    
    echo "$migration_info" > "$INSTALL_DIR/.migration_info"
    
    # Auto-remove old directory if safe
    if [[ -z "$user_files" ]]; then
        echo "No user modifications detected in old location"
        echo "Removing old installation..."
        rm -rf "$old_dir"
        echo "✓ Old installation removed"
    else
        echo ""
        echo "⚠️  User modifications detected - old directory preserved"
        echo "Custom files found:"
        echo "$user_files" | sed 's/^/  - /'
    fi
}

# Main installation logic
echo ""

# Check if already installed at new location
if [[ -d "$INSTALL_DIR" && -f "$INSTALL_DIR/docs/docs_manifest.json" ]]; then
    echo "✓ Found existing installation at ~/.claude-code-docs"
    
    # Just update it
    cd "$INSTALL_DIR"
    echo "Updating to latest version..."
    git pull --quiet origin main || echo "  (Could not pull latest changes)"
else
    # Look for existing installations to migrate
    echo "Checking for existing installations..."
    mapfile -t existing_installs < <(find_existing_installations)
    
    if [[ ${#existing_installs[@]} -gt 0 ]]; then
        # Found existing installation(s)
        echo "Found ${#existing_installs[@]} existing installation(s):"
        for install in "${existing_installs[@]}"; do
            echo "  - $install"
        done
        echo ""
        
        # Use the first one found (prioritize current directory)
        old_install="${existing_installs[0]}"
        echo "Checking for user modifications in: $old_install"
        
        # Check for user modifications
        user_modifications=$(detect_user_modifications "$old_install")
        
        # Migrate
        migrate_installation "$old_install" "$user_modifications"
    else
        # Fresh installation
        echo "No existing installation found"
        echo "Installing fresh to ~/.claude-code-docs..."
        
        git clone https://github.com/ericbuess/claude-code-docs.git "$INSTALL_DIR"
        cd "$INSTALL_DIR"
    fi
fi

# Now we're in $INSTALL_DIR, set up the new script-based system
echo ""
echo "Setting up Claude Code Docs v0.3..."

# Copy helper script from template
echo "Installing helper script..."
cp "$INSTALL_DIR/scripts/claude-docs-helper.sh.template" "$INSTALL_DIR/claude-docs-helper.sh"
chmod +x "$INSTALL_DIR/claude-docs-helper.sh"
echo "✓ Helper script installed"

# Create command directory
echo "Setting up /docs command..."
mkdir -p ~/.claude/commands

# Create simplified docs command
cat > ~/.claude/commands/docs.md << 'EOF'
Execute the Claude Code Docs helper script at ~/.claude-code-docs/claude-docs-helper.sh

Usage:
- /docs - List all available documentation topics
- /docs <topic> - Read specific documentation with link to official docs
- /docs -t - Check sync status without reading a doc
- /docs -t <topic> - Check freshness then read documentation
- /docs whats new - Show recent documentation changes (or "what's new")

Examples of expected output:

When reading a doc:
📚 COMMUNITY MIRROR: https://github.com/ericbuess/claude-code-docs
📖 OFFICIAL DOCS: https://docs.anthropic.com/en/docs/claude-code

[Doc content here...]

📖 Official page: https://docs.anthropic.com/en/docs/claude-code/hooks

When showing what's new:
📚 Recent documentation updates:

• 5 hours ago:
  📎 https://github.com/ericbuess/claude-code-docs/commit/eacd8e1
  📄 data-usage: https://docs.anthropic.com/en/docs/claude-code/data-usage
     ➕ Added: Privacy safeguards
  📄 security: https://docs.anthropic.com/en/docs/claude-code/security
     ✨ Data flow and dependencies section moved here

📎 Full changelog: https://github.com/ericbuess/claude-code-docs/commits/main/docs
📚 COMMUNITY MIRROR - NOT AFFILIATED WITH ANTHROPIC

Every request checks for the latest documentation from GitHub (takes ~0.4s).
The helper script handles all functionality including auto-updates.

Execute: ~/.claude-code-docs/claude-docs-helper.sh "$ARGUMENTS"
EOF

echo "✓ Created /docs command"

# Setup hook for auto-updates
echo "Setting up automatic updates..."

# Simple hook that just calls the helper script
HOOK_COMMAND="~/.claude-code-docs/claude-docs-helper.sh hook-check"

if [ -f ~/.claude/settings.json ]; then
    # Update existing settings.json
    echo "Updating existing Claude settings..."
    # Remove old hooks first
    jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.matcher != "Read")]' ~/.claude/settings.json > ~/.claude/settings.json.tmp
    # Add new hook
    jq --arg cmd "$HOOK_COMMAND" '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[]] + [{"matcher": "Read", "hooks": [{"type": "command", "command": $cmd}]}]' ~/.claude/settings.json.tmp > ~/.claude/settings.json
    rm -f ~/.claude/settings.json.tmp
    echo "✓ Updated Claude settings"
else
    # Create new settings.json
    echo "Creating Claude settings..."
    jq -n --arg cmd "$HOOK_COMMAND" '{
        "hooks": {
            "PreToolUse": [
                {
                    "matcher": "Read",
                    "hooks": [
                        {
                            "type": "command",
                            "command": $cmd
                        }
                    ]
                }
            ]
        }
    }' > ~/.claude/settings.json
    echo "✓ Created Claude settings"
fi

# Success message
echo ""
echo "✅ Claude Code Docs v0.3 installed successfully!"
echo ""
echo "📚 Command: /docs (user)"
echo "📂 Location: ~/.claude-code-docs"
echo ""
echo "Usage examples:"
echo "  /docs hooks         # Read hooks documentation"
echo "  /docs -t           # Check when docs were last updated"
echo "  /docs what's new  # See recent documentation changes"
echo ""
echo "🔄 Auto-updates: Enabled - syncs automatically when GitHub has newer content"
echo ""
echo "Available topics:"
ls "$INSTALL_DIR/docs" | grep '\.md$' | sed 's/\.md$//' | sort | column -c 60
echo ""
echo "⚠️  Note: Restart Claude Code for auto-updates to take effect"