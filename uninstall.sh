#!/bin/bash
set -euo pipefail

# Claude Code Docs — Uninstaller v1.0.0

echo "Claude Code Docs — Uninstaller"
echo "==============================="
echo ""

INSTALL_DIR="$HOME/.claude-code-docs"

echo "To uninstall the plugin, run inside Claude Code:"
echo ""
echo "  /plugin uninstall claude-docs@claude-code-docs"
echo ""

if [ -d "$INSTALL_DIR" ]; then
    echo "Local documentation found at: $INSTALL_DIR"
    echo ""

    if [ -t 0 ]; then
        read -p "Remove local documentation? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$INSTALL_DIR"
            echo "Removed $INSTALL_DIR"
        else
            echo "Kept $INSTALL_DIR (documentation files still available locally)"
        fi
    else
        echo "Run interactively to remove, or: rm -rf $INSTALL_DIR"
    fi
fi

# Clean up any legacy artifacts
if [ -f "$HOME/.claude/commands/docs.md" ]; then
    if grep -q "claude-docs-helper" "$HOME/.claude/commands/docs.md" 2>/dev/null; then
        rm -f "$HOME/.claude/commands/docs.md"
        echo "Removed legacy /docs command"
    fi
fi

echo ""
echo "Uninstall complete."
echo "To reinstall: /plugin marketplace add costiash/claude-code-docs"
