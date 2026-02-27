#!/bin/bash
# Claude Code Docs — SessionStart sync hook
# Ensures ~/.claude-code-docs/ exists and is up-to-date

DOCS_DIR="$HOME/.claude-code-docs"
REPO_URL="https://github.com/costiash/claude-code-docs.git"

# Portable timeout wrapper (GNU timeout not available on macOS by default)
run_with_timeout() {
    local secs="$1"; shift
    if command -v timeout >/dev/null 2>&1; then
        timeout "$secs" "$@"
    else
        "$@"
    fi
}

# JSON output for SessionStart additionalContext
output_context() {
    local msg="$1"
    # Escape backslashes and double-quotes for valid JSON
    msg="${msg//\\/\\\\}"
    msg="${msg//\"/\\\"}"
    cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "$msg"
  }
}
EOF
}

# Clone if not exists
if [ ! -d "$DOCS_DIR" ]; then
    if run_with_timeout 30 git clone --depth 1 "$REPO_URL" "$DOCS_DIR" >/dev/null 2>&1; then
        DOC_COUNT=$(find "$DOCS_DIR/docs" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
        output_context "Claude documentation installed: $DOC_COUNT docs available at ~/.claude-code-docs/. Use /docs to search."
    else
        output_context "Failed to clone Claude documentation. Run: git clone $REPO_URL $DOCS_DIR"
    fi
    exit 0
fi

# Pull updates (non-blocking, timeout after 10s)
cd "$DOCS_DIR" || exit 0
BEFORE=$(git rev-parse HEAD 2>/dev/null)
run_with_timeout 10 git pull --ff-only origin main >/dev/null 2>&1 || true
AFTER=$(git rev-parse HEAD 2>/dev/null)

DOC_COUNT=$(find "$DOCS_DIR/docs" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

if [ "$BEFORE" != "$AFTER" ]; then
    NEW_COMMITS=$(git log --oneline "$BEFORE..$AFTER" 2>/dev/null | wc -l | tr -d ' ')
    output_context "Claude docs updated ($NEW_COMMITS new commits). $DOC_COUNT docs available. Use /docs to search."
else
    output_context "Claude docs up-to-date. $DOC_COUNT docs available. Use /docs to search."
fi

exit 0
