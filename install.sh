#!/bin/bash
set -euo pipefail

# Claude Code Docs Installer v1.0.0
# Migration wrapper: routes to plugin install when possible,
# falls back to git clone for environments without plugin support.

echo "Claude Code Docs v1.0.0"
echo "======================="
echo ""

INSTALL_DIR="$HOME/.claude-code-docs"
REPO_URL="https://github.com/costiash/claude-code-docs.git"

# Check if Claude Code is available
if [ -d "$HOME/.claude" ]; then
    echo "Claude Code detected."
    echo ""
    echo "The recommended installation method is the Claude Code plugin."
    echo "Run these two commands inside Claude Code:"
    echo ""
    echo "  /plugin marketplace add costiash/claude-code-docs"
    echo "  /plugin install claude-docs@claude-code-docs"
    echo ""
    echo "The plugin provides:"
    echo "  - /docs command for documentation lookups"
    echo "  - Auto-discovery Skill (Claude reads docs automatically)"
    echo "  - Session-start auto-updates"
    echo "  - Content search and fuzzy matching"
    echo ""

    # Check for legacy script-install artifacts
    legacy_found=false

    if [ -f "$HOME/.claude/commands/docs.md" ]; then
        # Check if the command references claude-docs-helper.sh (legacy indicator)
        if grep -q "claude-docs-helper" "$HOME/.claude/commands/docs.md" 2>/dev/null; then
            legacy_found=true
        fi
    fi

    if [ -f "$HOME/.claude/settings.json" ]; then
        if grep -q "claude-code-docs" "$HOME/.claude/settings.json" 2>/dev/null; then
            legacy_found=true
        fi
    fi

    if [ "$legacy_found" = true ]; then
        echo "Legacy script-install artifacts detected."
        echo ""

        if [ -t 0 ]; then
            read -p "Clean up legacy artifacts? (y/N): " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                # Remove legacy /docs command if it references the helper script
                if [ -f "$HOME/.claude/commands/docs.md" ]; then
                    if grep -q "claude-docs-helper" "$HOME/.claude/commands/docs.md" 2>/dev/null; then
                        rm -f "$HOME/.claude/commands/docs.md"
                        echo "  Removed legacy /docs command"
                    fi
                fi

                # Remove legacy hooks from settings.json
                if [ -f "$HOME/.claude/settings.json" ] && command -v jq >/dev/null 2>&1; then
                    if jq -e '.hooks.PreToolUse' "$HOME/.claude/settings.json" >/dev/null 2>&1; then
                        jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[0].command | contains("claude-code-docs") | not)]' \
                            "$HOME/.claude/settings.json" > "$HOME/.claude/settings.json.tmp" && \
                            mv "$HOME/.claude/settings.json.tmp" "$HOME/.claude/settings.json"
                        echo "  Cleaned legacy hooks from settings.json"
                    fi
                fi

                echo ""
                echo "Legacy artifacts cleaned up."
            fi
        else
            echo "Run this script interactively to clean up, or install the plugin to replace them."
        fi
    fi

    echo ""
    echo "After installing the plugin, restart Claude Code."

else
    echo "Claude Code not detected (no ~/.claude directory)."
    echo ""
    echo "Falling back to git clone..."
    echo "NOTE: Plugin install is recommended when Claude Code is available."
    echo ""

    if [ -d "$INSTALL_DIR" ]; then
        echo "Updating existing installation..."
        cd "$INSTALL_DIR" && git pull --ff-only origin main || {
            echo "Update failed. Try: rm -rf $INSTALL_DIR && re-run this script"
            exit 1
        }
    else
        git clone --depth 1 "$REPO_URL" "$INSTALL_DIR" || {
            echo "Clone failed. Check your network connection."
            exit 1
        }
    fi

    DOC_COUNT=$(find "$INSTALL_DIR/docs" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
    echo ""
    echo "Documentation installed: $DOC_COUNT files at $INSTALL_DIR"
    echo ""
    echo "To use with Claude Code later, install the plugin:"
    echo "  /plugin marketplace add costiash/claude-code-docs"
    echo "  /plugin install claude-docs@claude-code-docs"
fi

echo ""
echo "Documentation: https://github.com/costiash/claude-code-docs"
