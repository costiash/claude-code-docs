#!/bin/bash
set -euo pipefail

# Claude Code Docs — Uninstaller v2.0.1

echo "Claude Code Docs — Uninstaller v2.0.1"
echo "====================================="
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

# Remove legacy hooks from ~/.claude/settings.json (non-fatal; the // "" guard
# keeps jq from erroring on entries without .hooks[0].command).
if [ -f "$HOME/.claude/settings.json" ] && command -v jq >/dev/null 2>&1; then
    if jq -e '.hooks.PreToolUse' "$HOME/.claude/settings.json" >/dev/null 2>&1; then
        if jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select((.hooks[0].command // "") | contains("claude-code-docs") | not)]' \
            "$HOME/.claude/settings.json" > "$HOME/.claude/settings.json.tmp" && \
            mv "$HOME/.claude/settings.json.tmp" "$HOME/.claude/settings.json"; then
            echo "Removed legacy hooks from settings.json"
        else
            rm -f "$HOME/.claude/settings.json.tmp"
            echo "Warning: could not clean legacy hooks from settings.json"
        fi
    fi
fi

echo ""
echo "Uninstall complete."
echo "To reinstall: /plugin marketplace add costiash/claude-code-docs"
