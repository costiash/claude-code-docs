#!/bin/bash

# Claude Code Documentation Mirror - Uninstall Script
# This script cleanly removes the Claude Code documentation mirror installation

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

print_color "$GREEN" "Claude Code Documentation Mirror - Uninstaller"
print_color "$GREEN" "============================================"
echo

# Check if running from the installation directory
if [[ ! -f "$SCRIPT_DIR/CLAUDE.md" ]] || [[ ! -d "$SCRIPT_DIR/docs" ]]; then
    print_color "$RED" "Error: This script must be run from the claude-code-docs installation directory."
    exit 1
fi

print_color "$YELLOW" "This will remove the Claude Code documentation mirror from:"
print_color "$YELLOW" "  $SCRIPT_DIR"
echo

# Show what will be removed
print_color "$YELLOW" "The following will be removed:"
echo "  - The entire claude-code-docs directory"
echo "  - Python virtual environment (.venv)"
echo "  - Local git repository"
echo "  - All documentation files"
echo

# Ask for confirmation
read -p "Are you sure you want to uninstall? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_color "$YELLOW" "Uninstall cancelled."
    exit 0
fi

# Remove the directory
print_color "$YELLOW" "Removing installation directory..."
cd ..
rm -rf "$SCRIPT_DIR"

print_color "$GREEN" "✓ Claude Code documentation mirror has been uninstalled successfully."
echo

# Check for other installations
print_color "$YELLOW" "Checking for other installations..."
OTHER_INSTALL=""
if [[ -d "$HOME/claude-code-docs" ]] && [[ "$HOME/claude-code-docs" != "$SCRIPT_DIR" ]]; then
    OTHER_INSTALL="$HOME/claude-code-docs"
elif [[ -d "$HOME/Projects/claude-code-docs" ]] && [[ "$HOME/Projects/claude-code-docs" != "$SCRIPT_DIR" ]]; then
    OTHER_INSTALL="$HOME/Projects/claude-code-docs"
fi

if [[ -n "$OTHER_INSTALL" ]]; then
    print_color "$YELLOW" "Note: Another installation was found at: $OTHER_INSTALL"
    echo "To remove it, run: rm -rf \"$OTHER_INSTALL\""
fi

echo
print_color "$GREEN" "Uninstall complete!"