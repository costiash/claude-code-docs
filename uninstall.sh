#!/bin/bash
set -euo pipefail

# Claude Code Docs — Uninstaller v2.1.0

echo "Claude Code Docs — Uninstaller v2.1.0"
echo "====================================="
echo ""

INSTALL_DIR="$HOME/.claude-code-docs"
# Set when stdin is not a terminal and the docs directory is left in place:
# the closing line must then say what happened, not "Uninstall complete."
KEPT_NONINTERACTIVE=0

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
        # %q shell-quotes the path so the hint is copy-paste safe whatever
        # characters the home directory contains.
        printf 'Run interactively to remove, or: rm -rf %q\n' "$INSTALL_DIR"
        KEPT_NONINTERACTIVE=1
    fi
fi

# Clean up any legacy artifacts
if [ -f "$HOME/.claude/commands/docs.md" ]; then
    if grep -q "claude-docs-helper" "$HOME/.claude/commands/docs.md" 2>/dev/null; then
        rm -f "$HOME/.claude/commands/docs.md"
        echo "Removed legacy /docs command"
    fi
fi

# Remove legacy hooks from ~/.claude/settings.json (non-fatal). Fully
# type-safe: a non-array PreToolUse passes through untouched, malformed
# entries (non-array .hooks, scalar elements, missing .command) are kept,
# EVERY hook command in an entry is checked (not just .[0]), and a
# non-string .command is tostring-coerced so contains() can never error
# the whole filter — only entries mentioning claude-code-docs are removed.
# NOTE: this jq filter is deliberately duplicated in install.sh — both
# scripts must stay runnable standalone (curl | bash), so there is no
# shared file to source. Edit both in lockstep.
if [ -f "$HOME/.claude/settings.json" ] && command -v jq >/dev/null 2>&1; then
    if jq -e '.hooks.PreToolUse' "$HOME/.claude/settings.json" >/dev/null 2>&1; then
        if jq '.hooks.PreToolUse = (if (.hooks.PreToolUse | type) == "array" then [.hooks.PreToolUse[] | select(([((.hooks? // null) | if type == "array" then .[] else empty end | (.command? // "" | tostring))] | any(contains("claude-code-docs"))) | not)] else .hooks.PreToolUse end)' \
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
if [ "$KEPT_NONINTERACTIVE" -eq 1 ]; then
    echo "Plugin uninstall instructions printed; local docs kept at $INSTALL_DIR"
else
    echo "Uninstall complete."
fi
echo "To reinstall: /plugin marketplace add costiash/claude-code-docs"
