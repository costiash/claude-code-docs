# v0.3 Upgrade Testing Checklist

## Critical Fixes Applied
✅ Fixed hook removal logic (was keeping Read hooks instead of removing them)
✅ Implemented actual uninstall in v0.3 helper script
✅ Both fixes pushed to dev-v0.3-refactor

## Test Scenarios

### 1. Clean Install Test
```bash
# Remove any existing installation
rm -rf ~/.claude-code-docs
rm -f ~/.claude/commands/docs.md

# Install fresh
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/dev-v0.3-refactor/install.sh | bash
```

### 2. Upgrade from v0.2 Test
```bash
# First install v0.2 from main branch
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash

# Check hooks in settings.json
cat ~/.claude/settings.json | jq '.hooks.PreToolUse'

# Then upgrade to v0.3
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/dev-v0.3-refactor/install.sh | bash

# Verify old hook was removed and new one added
cat ~/.claude/settings.json | jq '.hooks.PreToolUse'
```

### 3. Uninstall Test
```bash
# Test v0.3 uninstall
/docs uninstall

# Or
~/.claude-code-docs/uninstall.sh

# Verify removal:
ls ~/.claude/commands/docs.md  # Should not exist
cat ~/.claude/settings.json | jq '.hooks.PreToolUse'  # Should have no claude-code-docs hooks
ls ~/.claude-code-docs  # Should not exist
```

### 4. Edge Cases
- [ ] Multiple installations in different directories
- [ ] Running installer multiple times
- [ ] Malformed settings.json
- [ ] No settings.json file

## What to Look For
1. **Hook Cleanup**: Only ONE hook after upgrade (no duplicates)
2. **Command File**: Gets completely replaced
3. **Uninstall**: Actually removes everything
4. **Migration**: Preserves git history and user files

## Commands to Verify State
```bash
# Check hooks
cat ~/.claude/settings.json | jq '.hooks.PreToolUse'

# Check command
cat ~/.claude/commands/docs.md

# Check installation
ls -la ~/.claude-code-docs/
```