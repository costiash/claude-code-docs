#!/bin/bash
set -euo pipefail

# Claude Code Docs Installer - Cross-platform
# This script sets up local Claude Code documentation with automatic updates

echo "Claude Code Docs Installer"
echo "========================="

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

# Check if we need to clean up old installation
if [ -f ~/.claude/commands/docs.md ]; then
    echo "✓ Found existing Claude Code Docs installation"
    echo "  Cleaning up old configuration for fresh install..."
    
    # Remove old command file
    rm -f ~/.claude/commands/docs.md
    echo "  ✓ Removed old command file"
    
    # Clean up old hooks from settings.json if it exists
    if [ -f ~/.claude/settings.json ]; then
        # Remove any hooks that contain 'claude-code-docs' in their command
        jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[]?.command // "" | contains("claude-code-docs") | not)]' ~/.claude/settings.json > ~/.claude/settings.json.tmp && \
        mv ~/.claude/settings.json.tmp ~/.claude/settings.json
        echo "  ✓ Cleaned up old hooks"
    fi
    
    echo "  ✓ Cleanup complete"
fi

# Get the docs path
if [ -f "docs/docs_manifest.json" ]; then
    # We're already in the claude-code-docs directory
    DOCS_PATH=$(pwd)
    echo "✓ Found repository at: $DOCS_PATH"
elif [ -d "claude-code-docs" ]; then
    # The directory already exists
    cd claude-code-docs || exit 1
    DOCS_PATH=$(pwd)
    echo "✓ Found repository at: $DOCS_PATH"
else
    # Clone it
    echo "Cloning documentation repository..."
    if ! git clone https://github.com/ericbuess/claude-code-docs.git; then
        echo "❌ Error: Failed to clone repository"
        exit 1
    fi
    cd claude-code-docs || exit 1
    DOCS_PATH=$(pwd)
    echo "✓ Documentation cloned to: $DOCS_PATH"
fi

# Set git merge strategy to avoid conflicts
git config pull.rebase false

# Always pull latest changes
echo "Updating to latest version..."
git pull --quiet origin main || echo "  (Could not pull latest changes, continuing with current version)"

# Escape the docs path for safe use in commands
DOCS_PATH_ESCAPED=$(printf '%q' "$DOCS_PATH")

# Create command directory
echo "Setting up /docs command..."
if ! mkdir -p ~/.claude/commands; then
    echo "❌ Error: Failed to create ~/.claude/commands directory"
    exit 1
fi

# Create the docs command file with quoted heredoc to prevent variable expansion
cat > ~/.claude/commands/docs.md << 'DOCS_COMMAND_EOF'
PLACEHOLDER_DOCS_PATH/docs/ contains a local updated copy of all Claude Code documentation.

When showing documentation freshness with -t flag:
Show the times first, then check if warning is needed.

Out-of-sync warning (ONLY show if BOTH conditions are true):
  1. GitHub hasn't updated in more than 3 hours (stale)
  2. Your local sync is missing or older than GitHub's update

If both conditions above are true, show this warning:
"⚠️ Your docs appear to be out of sync!

If your local docs haven't updated in over 3 hours, you likely have an older
version of the installer with a bug that prevents automatic updates.

To fix this and enable auto-sync, run:
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash

This one-time fix will ensure your docs stay automatically synchronized."

Usage:
- /docs <topic> - Read documentation instantly (no checks)
- /docs -t - Check documentation freshness and sync status
- /docs -t <topic> - Check freshness, then read documentation

Default behavior (no -t flag):
1. Skip ALL checks for maximum speed
2. Directly read the documentation file
3. Show note: "📚 Reading from local docs (run /docs -t to check freshness)"

With -t flag - EXECUTE THESE STEPS:
Step 1: Read manifest using: cat "PLACEHOLDER_DOCS_PATH/docs/docs_manifest.json"
Step 2: Check last sync using: cat "PLACEHOLDER_DOCS_PATH/.last_pull" 2>/dev/null || echo "No sync timestamp"
Step 3: Calculate and display times:
   - Extract last_updated and installer_version from manifest
   - Convert GitHub timestamp to UTC unix time
   - Calculate: (current_UTC_time - github_UTC_time) for time difference
   - Display: "📅 Documentation last updated on GitHub: X hours/minutes ago"
   - Display: "📅 Your local docs last synced: X minutes ago" (or "No sync timestamp")
   - Display: "📅 Installer version: X.X"
   - Check warning conditions: If GitHub > 3 hours old AND local is missing/old, show warning
Step 4: If topic provided, read using: cat "PLACEHOLDER_DOCS_PATH/docs/${topic}.md"

Note: The hook automatically keeps docs up-to-date by checking if GitHub has newer content before each read. You'll see "🔄 Updating docs to latest version..." when it syncs.

Error handling:
- If any files are missing or commands fail, show: "❌ Error accessing docs. Try re-running: curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash"

GitHub Actions updates the docs every 3 hours. Your local copy automatically syncs at most once every 3 hours when you use this command.

IMPORTANT: Show relative times only (no timezone conversions needed):
- GitHub last updated: Extract timestamp from manifest (it's in UTC!), convert to Unix timestamp, then calculate (current_time - github_time) / 3600 for hours or / 60 for minutes
- Local docs last synced: Read timestamp from PLACEHOLDER_DOCS_PATH/.last_pull, then calculate (current_time - last_pull) / 60 for minutes
- If GitHub hasn't updated in >3 hours, add note "(normally updates every 3 hours)"
- Be clear about wording: "local docs last synced" not "last checked"
- For calculations: Use proper parentheses like $(((NOW - GITHUB) / 3600)) for hours
- Date command compatibility: The installer uses OS-appropriate date syntax

First, check if user passed -t flag:
- If "$ARGUMENTS" starts with "-t", extract it and treat the rest as the topic
- Parse carefully: "-t hooks" → flag=true, topic=hooks; "hooks" → flag=false, topic=hooks

Examples:

Default usage (no -t):
> /docs hooks
📚 Reading from local docs (run /docs -t to check freshness)
[Executes: cat "PLACEHOLDER_DOCS_PATH/docs/hooks.md"]

With -t flag:
> /docs -t
📅 Documentation last updated on GitHub: 2 hours ago
📅 Your local docs last synced: 25 minutes ago
📅 Installer version: 0.2

> /docs -t hooks  
📅 Documentation last updated on GitHub: 5 hours ago (normally updates every 3 hours)
📅 Your local docs last synced: 3 hours 15 minutes ago
📅 Installer version: 0.2
🔄 Syncing latest documentation...
[Then shows hooks documentation]

Special handling for "what's new" or "recent changes" queries:
- If user asks about recent updates, changes, or what's new:
  1. Run: cd PLACEHOLDER_DOCS_PATH && git log --oneline -10
  2. For each commit that mentions "Update Claude Code docs":
     - Show commit date and hash
     - Run: git diff --name-only COMMIT_HASH^..COMMIT_HASH -- docs/*.md
     - List which docs changed
  3. For the most recent docs update commit:
     - Run: git diff --stat COMMIT_HASH^..COMMIT_HASH -- docs/*.md
     - Show summary of changes (files changed, insertions, deletions)
  4. If user wants specific changes, use: git diff COMMIT_HASH^..COMMIT_HASH -- docs/SPECIFIC_FILE.md

Then answer the user's question by reading docs with: cat "PLACEHOLDER_DOCS_PATH/docs/[topic].md"

Available docs: overview, quickstart, setup, memory, common-workflows, ide-integrations, mcp, github-actions, sdk, troubleshooting, security, settings, monitoring-usage, costs, hooks

IMPORTANT: This freshness check only happens when using /docs command. If continuing a conversation from a previous session, use /docs again to ensure docs are current.

User query: $ARGUMENTS
DOCS_COMMAND_EOF

# Replace the placeholder with the actual escaped path
# Use OS-appropriate sed syntax
if [[ "$OS_TYPE" == "macos" ]]; then
    sed -i '' "s|PLACEHOLDER_DOCS_PATH|$DOCS_PATH|g" ~/.claude/commands/docs.md
else
    sed -i "s|PLACEHOLDER_DOCS_PATH|$DOCS_PATH|g" ~/.claude/commands/docs.md
fi

echo "✓ Created /docs command"

# Setup hook for auto-updates (checks if GitHub has newer content)
echo "Setting up automatic updates..."

# Create the hook command with proper escaping
# Using printf to safely construct the command with escaped variables
# This hook uses git fetch to check for remote updates, with rate limiting
# It also checks for installer updates and runs the installer if needed
HOOK_COMMAND=$(printf 'if [[ $(jq -r .tool_input.file_path 2>/dev/null) == *%s/* ]]; then LAST_CHECK="%s/.last_check" && LAST_PULL="%s/.last_pull" && NOW=$(date +%%s) && CHECK_INTERVAL=10800 && SHOULD_CHECK=0 && if [[ -f "$LAST_CHECK" ]]; then LAST_CHECK_TIME=$(cat "$LAST_CHECK"); if [[ $((NOW - LAST_CHECK_TIME)) -gt $CHECK_INTERVAL ]]; then SHOULD_CHECK=1; fi; else SHOULD_CHECK=1; fi && if [[ $SHOULD_CHECK -eq 1 ]]; then echo $NOW > "$LAST_CHECK" && (cd %s && git fetch --quiet origin main 2>/dev/null && LOCAL=$(git rev-parse HEAD 2>/dev/null) && REMOTE=$(git rev-parse origin/main 2>/dev/null) && if [[ "$LOCAL" != "$REMOTE" ]]; then echo "🔄 Updating docs to latest version..." >&2 && git pull --quiet origin main && echo $NOW > "$LAST_PULL" && INSTALLER_VERSION=$(jq -r .installer_version "%s/docs/docs_manifest.json" 2>/dev/null || echo 0.1) && if (( $(echo "$INSTALLER_VERSION > 0.2" | bc -l) )); then echo "🔧 Updating Claude Code Docs installer..." >&2 && (cd %s && ./install.sh >/dev/null 2>&1 || true); fi; fi) || true; fi; fi' "$DOCS_PATH_ESCAPED" "$DOCS_PATH_ESCAPED" "$DOCS_PATH_ESCAPED" "$DOCS_PATH_ESCAPED" "$DOCS_PATH_ESCAPED" "$DOCS_PATH_ESCAPED")

if [ -f ~/.claude/settings.json ]; then
    # Update existing settings.json
    echo "Updating existing Claude settings..."
    if jq --arg cmd "$HOOK_COMMAND" '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.matcher != "Read")] + [{"matcher": "Read", "hooks": [{"type": "command", "command": $cmd}]}]' ~/.claude/settings.json > ~/.claude/settings.json.tmp; then
        mv ~/.claude/settings.json.tmp ~/.claude/settings.json
        echo "✓ Updated Claude settings"
    else
        echo "❌ Error: Failed to update settings.json"
        echo "Please check ~/.claude/settings.json manually"
        exit 1
    fi
else
    # Create new settings.json
    echo "Creating Claude settings..."
    if jq -n --arg cmd "$HOOK_COMMAND" '{
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
    }' > ~/.claude/settings.json; then
        echo "✓ Created Claude settings"
    else
        echo "❌ Error: Failed to create settings.json"
        exit 1
    fi
fi

# No version marker needed - it's in the manifest

echo ""
echo "✅ Claude Code docs installed successfully!"
echo ""
echo "📚 Command: /docs (user)"
echo "📂 Location: $DOCS_PATH"
echo ""
echo "Usage examples:"
echo "  /docs hooks         # Read hooks documentation"
echo "  /docs -t           # Check when docs were last updated"
echo "  /docs -t memory    # Check updates, then read memory docs"
echo ""
echo "🔄 Auto-updates: Enabled - syncs automatically when GitHub has newer content"
echo ""
echo "Available topics: overview, quickstart, memory, hooks, mcp, settings, etc."
echo ""
echo "⚠️  Note: Restart Claude Code for auto-updates to take effect"