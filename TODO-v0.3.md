# TODO: v0.3 Script-Based Refactor

## Overview
Refactor claude-code-docs to use a single script for all operations instead of relying on Claude to interpret instructions. This will make the tool faster, more reliable, and easier to maintain.

## Auto-Update Mechanism
**Yes, users with v0.2 will auto-update!** The hook already checks installer_version and runs the installer when it increases. Just need to set `installer_version: 0.3` in the manifest.

## Implementation Steps

### 1. Create the Helper Script Template
Create `scripts/claude-docs-helper.sh.template`:

```bash
#!/bin/bash
set -euo pipefail

# Paths configured during installation
DOCS_PATH="PLACEHOLDER_DOCS_PATH"
MANIFEST="$DOCS_PATH/docs/docs_manifest.json"
LAST_PULL="$DOCS_PATH/.last_pull"
LAST_CHECK="$DOCS_PATH/.last_check"

# Function to calculate time differences
calculate_time_diff() {
    local timestamp="$1"
    local now=$(date -u +%s)
    local then=$(date -u -d "$timestamp" +%s 2>/dev/null || date -u -j -f "%Y-%m-%dT%H:%M:%S" "$timestamp" +%s 2>/dev/null)
    echo $(( (now - then) / 60 ))  # minutes
}

# Function to show freshness
show_freshness() {
    # Read manifest
    if [[ ! -f "$MANIFEST" ]]; then
        echo "❌ Error: Documentation not found. Please reinstall."
        exit 1
    fi
    
    # Get GitHub update time and installer version
    local github_time=$(jq -r '.last_updated' "$MANIFEST" | cut -d. -f1)
    local installer_version=$(jq -r '.installer_version' "$MANIFEST")
    
    # Calculate time since GitHub update
    local github_minutes=$(calculate_time_diff "$github_time")
    local github_hours=$((github_minutes / 60))
    
    # Get local sync time
    local local_sync="No sync timestamp"
    if [[ -f "$LAST_PULL" ]]; then
        local pull_time=$(cat "$LAST_PULL")
        local local_minutes=$(( ($(date +%s) - pull_time) / 60 ))
        local_sync="${local_minutes} minutes ago"
    fi
    
    # Display info
    echo "📅 Documentation last updated on GitHub: ${github_minutes} minutes ago"
    echo "📅 Your local docs last synced: ${local_sync}"
    echo "📅 Installer version: ${installer_version}"
    
    # Check if warning needed (only if GitHub > 3 hours old)
    if [[ $github_hours -gt 3 ]]; then
        if [[ ! -f "$LAST_PULL" ]] || [[ $(cat "$LAST_PULL") -lt $(date -u -d "$github_time" +%s 2>/dev/null || echo 0) ]]; then
            echo ""
            echo "⚠️ Your docs appear to be out of sync!"
            echo ""
            echo "Your docs haven't been updated in over 3 hours. To fix this and enable auto-sync:"
            echo ""
            echo "curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash"
            echo ""
            echo "Would you like me to run this command for you?"
        fi
    fi
}

# Function to read documentation
read_doc() {
    local topic="$1"
    local doc_path="$DOCS_PATH/docs/${topic}.md"
    
    if [[ -f "$doc_path" ]]; then
        cat "$doc_path"
    else
        echo "❌ Documentation not found: $topic"
        echo ""
        echo "Available topics:"
        ls "$DOCS_PATH/docs" | grep '\.md$' | sed 's/\.md$//' | sort
    fi
}

# Function for hook check
hook_check() {
    local NOW=$(date +%s)
    local CHECK_INTERVAL=10800  # 3 hours
    
    # Check if we should check for updates
    if [[ -f "$LAST_CHECK" ]]; then
        local LAST_CHECK_TIME=$(cat "$LAST_CHECK")
        if [[ $((NOW - LAST_CHECK_TIME)) -lt $CHECK_INTERVAL ]]; then
            exit 0  # Too soon to check
        fi
    fi
    
    echo $NOW > "$LAST_CHECK"
    
    # Check for updates
    cd "$DOCS_PATH"
    git fetch --quiet origin main 2>/dev/null || exit 0
    
    local LOCAL=$(git rev-parse HEAD 2>/dev/null)
    local REMOTE=$(git rev-parse origin/main 2>/dev/null)
    
    if [[ "$LOCAL" != "$REMOTE" ]]; then
        echo "🔄 Updating docs to latest version..." >&2
        git pull --quiet origin main
        echo $NOW > "$LAST_PULL"
        
        # Check if installer needs updating
        local INSTALLER_VERSION=$(jq -r '.installer_version' "$MANIFEST" 2>/dev/null || echo 0.2)
        if (( $(echo "$INSTALLER_VERSION > 0.3" | bc -l) )); then
            echo "🔧 Updating Claude Code Docs installer..." >&2
            cd "$DOCS_PATH" && ./install.sh >/dev/null 2>&1
        fi
    fi
}

# Function for uninstall
uninstall() {
    echo "Claude Code Documentation Mirror - Uninstaller"
    echo "=============================================="
    echo ""
    echo "This will remove:"
    echo "  1. The docs command: ~/.claude/commands/docs.md"
    echo "  2. The auto-update hook from: ~/.claude/settings.json"
    echo "  3. The installation directory: $DOCS_PATH"
    echo ""
    
    read -p "Are you sure? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 0
    fi
    
    # Remove command
    rm -f ~/.claude/commands/docs.md
    echo "✓ Removed command file"
    
    # Remove hook
    if [[ -f ~/.claude/settings.json ]]; then
        cp ~/.claude/settings.json ~/.claude/settings.json.backup
        jq --arg path "$DOCS_PATH" '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[0].command | contains($path) | not)]' ~/.claude/settings.json > ~/.claude/settings.json.tmp
        mv ~/.claude/settings.json.tmp ~/.claude/settings.json
        echo "✓ Removed hook from settings"
    fi
    
    # Remove directory (change to parent first)
    cd "$(dirname "$DOCS_PATH")"
    rm -rf "$DOCS_PATH"
    echo "✓ Removed installation directory"
    echo ""
    echo "✅ Uninstall complete!"
}

# Main command handling
case "${1:-}" in
    -t|--check)
        show_freshness
        if [[ -n "${2:-}" ]]; then
            echo ""
            read_doc "$2"
        fi
        ;;
    hook-check)
        hook_check
        ;;
    uninstall)
        uninstall
        ;;
    "")
        echo "Available documentation topics:"
        ls "$DOCS_PATH/docs" | grep '\.md$' | sed 's/\.md$//' | sort
        ;;
    *)
        # Default: read documentation
        echo "📚 Reading from local docs (run /docs -t to check freshness)"
        echo ""
        read_doc "$1"
        ;;
esac
```

### 2. Update install.sh
Modify install.sh to:

1. Copy the script template to installation directory
2. Replace PLACEHOLDER_DOCS_PATH with actual path
3. Make it executable
4. Create simpler docs.md command file:
```
Execute: PLACEHOLDER_DOCS_PATH/claude-docs-helper.sh $ARGUMENTS
```

5. Update hook to use script:
```bash
HOOK_COMMAND="$DOCS_PATH/claude-docs-helper.sh hook-check"
```

### 3. Update uninstall.sh
Replace with simple wrapper:
```bash
#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
exec "$SCRIPT_DIR/claude-docs-helper.sh" uninstall
```

### 4. Fix "What's New" Feature
Add to the script:
```bash
whats_new)
    # Compare actual file hashes, not timestamps
    # Show real content changes
    ;;
```

### 5. Testing Plan
1. Test fresh install
2. Test upgrade from v0.2
3. Test all commands:
   - `/docs` (list topics)
   - `/docs hooks` (read specific doc)
   - `/docs -t` (check freshness)
   - `/docs -t hooks` (check + read)
   - `/docs whats new` (show changes)
4. Test hook auto-update
5. Test uninstaller
6. Test from different directories

### 6. Update docs_manifest.json
When ready to release, update:
```json
"installer_version": 0.3
```

This will trigger auto-update for all v0.2 users!

### 7. Update Documentation
- Update README.md with v0.3 changes
- Update CLAUDE.md if needed
- Add changelog entry

## Key Benefits
1. **Reliable** - No more Claude interpretation issues
2. **Fast** - Single script execution
3. **Testable** - Can test without Claude
4. **Maintainable** - All logic in one place
5. **Portable** - Same script works everywhere

## Migration Path
1. Users with v0.2 will auto-update when we set installer_version to 0.3
2. Fresh installs will get v0.3 directly
3. Old command/hook will be replaced automatically

## Success Criteria
- [ ] All commands work consistently from any directory
- [ ] No more relative path issues
- [ ] Faster execution (< 1 second for most operations)
- [ ] What's new shows actual changes, not timestamp updates
- [ ] Auto-update from v0.2 works smoothly
- [ ] All tests pass