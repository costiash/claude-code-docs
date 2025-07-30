#!/bin/bash

# Claude Code Documentation Mirror - Complete Uninstall Script
# This script completely removes the Claude Code documentation mirror installation

set -euo pipefail

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

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

print_color "$GREEN" "Claude Code Documentation Mirror - Complete Uninstaller"
print_color "$GREEN" "===================================================="
echo

# Check if running from the installation directory
if [[ ! -f "$SCRIPT_DIR/CLAUDE.md" ]] || [[ ! -d "$SCRIPT_DIR/docs" ]]; then
    print_color "$RED" "Error: This script must be run from the claude-code-docs installation directory."
    exit 1
fi

print_color "$YELLOW" "This will completely remove the Claude Code documentation mirror from your system."
echo

# Show what will be removed
print_color "$YELLOW" "The following will be removed:"
echo "  - The entire claude-code-docs directory: $SCRIPT_DIR"
echo "  - The /user:docs command file: ~/.claude/commands/docs.md"
echo "  - The auto-update hook from: ~/.claude/settings.json"
echo "  - Any tracking files (.last_check, .last_pull)"
echo

# Ask for confirmation
read -p "Are you sure you want to completely uninstall? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_color "$YELLOW" "Uninstall cancelled."
    exit 0
fi

# Remove the command file
if [[ -f ~/.claude/commands/docs.md ]]; then
    print_color "$YELLOW" "Removing /user:docs command..."
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
    
    # Remove hooks that contain the installation path
    if jq --arg path "$SCRIPT_DIR" '.hooks.PreToolUse = [.hooks.PreToolUse[]? | select(.hooks[]?.command | contains($path) | not)]' ~/.claude/settings.json > ~/.claude/settings.json.tmp; then
        # Check if we have any PreToolUse hooks left
        if [[ $(jq '.hooks.PreToolUse | length' ~/.claude/settings.json.tmp) -eq 0 ]]; then
            # Remove empty PreToolUse array
            jq 'if .hooks.PreToolUse == [] then .hooks |= del(.PreToolUse) else . end' ~/.claude/settings.json.tmp > ~/.claude/settings.json.tmp2
            mv ~/.claude/settings.json.tmp2 ~/.claude/settings.json.tmp
        fi
        
        # Check if hooks object is now empty
        if [[ $(jq '.hooks | length' ~/.claude/settings.json.tmp) -eq 0 ]]; then
            # Remove empty hooks object
            jq 'del(.hooks)' ~/.claude/settings.json.tmp > ~/.claude/settings.json.tmp2
            mv ~/.claude/settings.json.tmp2 ~/.claude/settings.json.tmp
        fi
        
        mv ~/.claude/settings.json.tmp ~/.claude/settings.json
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

# Remove the installation directory
print_color "$YELLOW" "Removing installation directory..."
cd ..
rm -rf "$SCRIPT_DIR"
print_color "$GREEN" "✓ Removed installation directory"

echo
print_color "$GREEN" "✅ Claude Code documentation mirror has been completely uninstalled!"
echo

# Check for other installations
print_color "$YELLOW" "Checking for other installations..."
OTHER_INSTALLS=()
[[ -d "$HOME/claude-code-docs" ]] && OTHER_INSTALLS+=("$HOME/claude-code-docs")
[[ -d "$HOME/Projects/claude-code-docs" ]] && OTHER_INSTALLS+=("$HOME/Projects/claude-code-docs")

if [[ ${#OTHER_INSTALLS[@]} -gt 0 ]]; then
    print_color "$YELLOW" "Note: Other installations were found at:"
    for install in "${OTHER_INSTALLS[@]}"; do
        [[ "$install" != "$SCRIPT_DIR" ]] && echo "  - $install"
    done
    echo "To remove them, run the uninstaller from each directory."
fi

echo
print_color "$GREEN" "Complete uninstall finished!"