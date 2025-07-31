# Verification Plan for v0.3 Critical Fixes

## Issue 1: Hook Removal Logic Verification

### Background
- **v0.2 hook**: Complex inline command with embedded bash logic
- **v0.3 hook**: Simple command: `~/.claude-code-docs/claude-docs-helper.sh hook-check`
- **Fix applied**: Changed `select(.matcher != "Read")` to `select(.matcher == "Read" | not)`
  - Note: These are logically equivalent, both remove Read hooks correctly

### Test Plan for Hook Removal

#### Step 1: Create Test Settings File
```bash
# Create a test settings.json with v0.2-style hook
cat > test-settings.json << 'EOF'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "command": "if [[ $(jq -r .tool_input.file_path 2>/dev/null) == */claude-code-docs/* ]]; then echo 'OLD HOOK'; fi"
          }
        ]
      },
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Write hook - should be preserved'"
          }
        ]
      }
    ]
  }
}
EOF
```

#### Step 2: Test Hook Removal Logic
```bash
# Test the jq command that removes Read hooks
jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.matcher == "Read" | not)]' test-settings.json

# Expected output: Only the Write hook should remain
```

#### Step 3: Test Full Install Process
```bash
# Backup real settings
cp ~/.claude/settings.json ~/.claude/settings.json.backup-test

# Copy test settings
cp test-settings.json ~/.claude/settings.json

# Run installer
cd ~/.claude-code-docs
./install.sh

# Check result
cat ~/.claude/settings.json | jq '.hooks.PreToolUse'

# Should show:
# - Old Read hook removed
# - Write hook preserved
# - New v0.3 Read hook added
```

## Issue 2: Uninstaller Functionality Verification

### Test Plan for Uninstaller

#### Step 1: Pre-uninstall State Check
```bash
# Document what exists before uninstall
ls -la ~/.claude/commands/docs.md
cat ~/.claude/settings.json | jq '.hooks.PreToolUse' | grep -c "claude-docs-helper.sh"
ls -la ~/.claude-code-docs/
```

#### Step 2: Run Uninstaller
```bash
# Test via command
/docs uninstall
# Type 'n' first to test cancellation
# Then run again and type 'y'

# OR test directly
~/.claude-code-docs/uninstall.sh
```

#### Step 3: Post-uninstall Verification
```bash
# All of these should fail/show nothing:
ls ~/.claude/commands/docs.md 2>/dev/null || echo "✓ Command removed"
cat ~/.claude/settings.json | jq '.hooks.PreToolUse' | grep -c "claude-code-docs" || echo "✓ Hooks removed"
ls ~/.claude-code-docs 2>/dev/null || echo "✓ Directory removed"

# Backup should exist
ls ~/.claude/settings.json.backup
```

## Automated Test Script

```bash
#!/bin/bash
# save as test-v0.3-fixes.sh

echo "=== Testing v0.3 Critical Fixes ==="

# Test 1: Hook Removal Logic
echo -e "\n[TEST 1] Hook Removal Logic"
cat > /tmp/test-settings.json << 'EOF'
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Read", "hooks": [{"type": "command", "command": "OLD_V0.2_HOOK"}]},
      {"matcher": "Write", "hooks": [{"type": "command", "command": "KEEP_THIS"}]}
    ]
  }
}
EOF

# Test removal
result=$(jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.matcher == "Read" | not)]' /tmp/test-settings.json)
if echo "$result" | grep -q "OLD_V0.2_HOOK"; then
  echo "❌ FAIL: Old hook not removed"
else
  echo "✅ PASS: Old hook removed"
fi
if echo "$result" | grep -q "KEEP_THIS"; then
  echo "✅ PASS: Other hooks preserved"
else
  echo "❌ FAIL: Other hooks not preserved"
fi

# Test 2: Uninstaller Confirmation
echo -e "\n[TEST 2] Uninstaller Confirmation Prompt"
# This would need manual testing or expect script

echo -e "\nTests complete. Manual testing required for full uninstall flow."
```

## Expected Results

### Hook Removal (Issue 1)
✅ Old v0.2 Read hook is removed
✅ Other hooks (Write, etc.) are preserved  
✅ New v0.3 Read hook is added
✅ No duplicate Read hooks

### Uninstaller (Issue 2)
✅ Confirmation prompt appears
✅ 'n' cancels the uninstall
✅ 'y' proceeds with uninstall
✅ Command file is removed
✅ Hooks are removed from settings.json
✅ Installation directory is removed
✅ Settings backup is created

## Quick Commands to Verify State

```bash
# Check hooks
cat ~/.claude/settings.json | jq '.hooks.PreToolUse[] | select(.matcher == "Read")'

# Count Read hooks (should be exactly 1 after install)
cat ~/.claude/settings.json | jq '[.hooks.PreToolUse[] | select(.matcher == "Read")] | length'

# Check for our specific hook
cat ~/.claude/settings.json | jq '.hooks.PreToolUse' | grep "claude-docs-helper.sh"
```