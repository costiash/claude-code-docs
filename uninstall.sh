#!/bin/bash

# Claude Code Documentation Mirror - Uninstaller
# This script uninstalls claude-code-docs from the system

set -euo pipefail

# Check if this is the old v0.2 installation (not in ~/.claude-code-docs)
if [[ ! -d "$HOME/.claude-code-docs" ]] || [[ ! -f "$HOME/.claude-code-docs/claude-docs-helper.sh" ]]; then
    # Old v0.2 uninstaller logic for backward compatibility
    echo "Running v0.2 uninstaller..."
    
    # Get the directory where this script is located
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    
    # Color codes for output
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    NC='\033[0m' # No Color
    
    # Function to print colored output
    print_color() {
        local color=$1
        shift
        echo -e "${color}$*${NC}"
    }
    
    print_color "$GREEN" "Claude Code Documentation Mirror - Uninstaller"
    print_color "$GREEN" "=============================================="
    echo
    
    # Check if running from the installation directory
    if [[ ! -f "$SCRIPT_DIR/CLAUDE.md" ]] || [[ ! -d "$SCRIPT_DIR/docs" ]]; then
        print_color "$RED" "Error: This script must be run from the claude-code-docs installation directory."
        exit 1
    fi
    
    print_color "$YELLOW" "This will remove:"
    echo "  1. The claude-code-docs directory: $SCRIPT_DIR"
    echo "  2. The /docs command file: ~/.claude/commands/docs.md"
    echo "  3. The auto-update hook from: ~/.claude/settings.json"
    echo
    
    # Ask for confirmation
    read -p "Are you sure you want to uninstall? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_color "$YELLOW" "Uninstall cancelled."
        exit 0
    fi
    
    # Remove the command file
    if [[ -f ~/.claude/commands/docs.md ]]; then
        print_color "$YELLOW" "Removing /docs command..."
        rm -f ~/.claude/commands/docs.md
        print_color "$GREEN" "✓ Removed command file"
    else
        print_color "$YELLOW" "Command file not found (already removed?)"
    fi
    
    # Remove the hook from settings.json
    if [[ -f ~/.claude/settings.json ]]; then
        print_color "$YELLOW" "Removing auto-update hook from settings..."
        
        # Create backup first
        cp ~/.claude/settings.json ~/.claude/settings.json.backup
        
        # Remove any PreToolUse hooks that contain this installation path
        if jq --arg path "$SCRIPT_DIR" '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[0].command | contains($path) | not)]' ~/.claude/settings.json > ~/.claude/settings.json.tmp; then
            
            # Clean up empty arrays/objects
            jq 'if .hooks.PreToolUse == [] then .hooks |= if . == {PreToolUse: []} then {} else del(.PreToolUse) end else . end | if .hooks == {} then del(.hooks) else . end' ~/.claude/settings.json.tmp > ~/.claude/settings.json.tmp2
            
            mv ~/.claude/settings.json.tmp2 ~/.claude/settings.json
            rm -f ~/.claude/settings.json.tmp
            print_color "$GREEN" "✓ Removed hook from settings"
            print_color "$YELLOW" "  (Backup saved to ~/.claude/settings.json.backup)"
        else
            print_color "$RED" "Failed to update settings.json"
            print_color "$YELLOW" "Please manually remove the hook from ~/.claude/settings.json"
            rm -f ~/.claude/settings.json.tmp
        fi
    else
        print_color "$YELLOW" "Settings file not found (no hooks to remove)"
    fi
    
    # Remove tracking files
    rm -f "$SCRIPT_DIR/.last_pull" "$SCRIPT_DIR/.last_check" 2>/dev/null || true
    
    # Check if we're currently in the directory we're about to delete
    CURRENT_DIR=$(pwd)
    if [[ "$CURRENT_DIR" == "$SCRIPT_DIR"* ]]; then
        # We're inside the directory to be deleted, need to move out
        PARENT_DIR=$(dirname "$SCRIPT_DIR")
        print_color "$YELLOW" "Changing to parent directory before removal..."
        cd "$PARENT_DIR"
    fi
    
    # Remove the directory
    print_color "$YELLOW" "Removing installation directory..."
    rm -rf "$SCRIPT_DIR"
    print_color "$GREEN" "✓ Removed installation directory"
    
    echo
    print_color "$GREEN" "✅ Claude Code documentation mirror has been completely uninstalled!"
    echo
    
    # Check for other installations
    print_color "$YELLOW" "Checking for other installations..."
    OTHER_INSTALLS=()
    [[ -d "$HOME/claude-code-docs" && "$HOME/claude-code-docs" != "$SCRIPT_DIR" ]] && OTHER_INSTALLS+=("$HOME/claude-code-docs")
    [[ -d "$HOME/Projects/claude-code-docs" && "$HOME/Projects/claude-code-docs" != "$SCRIPT_DIR" ]] && OTHER_INSTALLS+=("$HOME/Projects/claude-code-docs")
    [[ -d "$HOME/.claude-code-docs" ]] && OTHER_INSTALLS+=("$HOME/.claude-code-docs (v0.3)")
    
    if [[ ${#OTHER_INSTALLS[@]} -gt 0 ]]; then
        print_color "$YELLOW" "Note: Other installations were found at:"
        for install in "${OTHER_INSTALLS[@]}"; do
            echo "  - $install"
        done
        echo "To remove them, run the uninstaller from each directory."
    fi
    
    echo
    print_color "$GREEN" "Uninstall complete!"
else
    # v0.3+ installation - delegate to helper script
    exec "$HOME/.claude-code-docs/claude-docs-helper.sh" uninstall
fi