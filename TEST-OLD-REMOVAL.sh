#!/bin/bash
# Quick test to verify old installation removal works

echo "Testing old installation removal..."
echo ""

# Check if old installation exists
if [[ -d ~/Projects/claude-code-docs ]]; then
    echo "✓ Found old installation at ~/Projects/claude-code-docs"
    
    # Check if it's a git repo
    if [[ -d ~/Projects/claude-code-docs/.git ]]; then
        cd ~/Projects/claude-code-docs
        if [[ -z "$(git status --porcelain 2>/dev/null)" ]]; then
            echo "✓ Old installation is clean (no uncommitted changes)"
            echo "  → Should be removed by v0.3 installer"
        else
            echo "⚠️  Old installation has uncommitted changes"
            echo "  → Will be preserved by v0.3 installer"
        fi
        cd - >/dev/null
    else
        echo "⚠️  Old installation is not a git repo"
        echo "  → Will be preserved by v0.3 installer"
    fi
else
    echo "❌ No old installation found at ~/Projects/claude-code-docs"
fi

echo ""
echo "Current configs point to:"
if [[ -f ~/.claude/commands/docs.md ]]; then
    echo "Command file:"
    grep -E "(Execute:|LOCAL DOCS AT:)" ~/.claude/commands/docs.md | head -3
fi

echo ""
echo "Ready to test migration with:"
echo "curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/dev-v0.3-refactor/install.sh | bash"