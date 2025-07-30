# Pre-Merge Checklist for Dev → Main

## Quick Validation

Run this before merging dev to main:
```bash
./test-dev-branch.sh
```

All tests must pass before merging.

## Manual Verification Steps

### 1. Test Full Install/Uninstall Flow (Optional - Destructive)
```bash
# Save your work first!
git stash

# Copy project to test location
cp -r . /tmp/test-claude-docs
cd /tmp/test-claude-docs

# Test uninstaller
echo "y" | ./uninstall.sh

# Verify:
# - Command file removed: ~/.claude/commands/docs.md
# - Hook removed from: ~/.claude/settings.json
# - Directory deleted properly

# Test installer from dev branch
cd /tmp
git clone -b dev https://github.com/ericbuess/claude-code-docs.git
cd claude-code-docs
./install.sh

# Verify:
# - Command created
# - Hook added
# - Docs accessible
```

### 2. Verify Key Changes
- [ ] `uninstall.sh` has directory change logic (line ~88-93)
- [ ] `install.sh` properly handles existing installations
- [ ] Both scripts are executable
- [ ] GitHub Actions workflow is present

### 3. Clean Up Test Script
After successful merge to main:
```bash
rm test-dev-branch.sh PRE-MERGE-CHECKLIST.md
```

## The Tests Check:
1. ✓ Install script exists and is executable
2. ✓ Uninstall script has directory protection
3. ✓ Hook removal logic works
4. ✓ Can create necessary directories
5. ✓ Documentation files present
6. ✓ Uninstaller has safe cancellation
7. ✓ GitHub Actions configured

## Git Commands
```bash
# When ready to merge
git checkout main
git merge dev
git push origin main
```