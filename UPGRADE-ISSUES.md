# Critical Issues Found Before v0.3 Release

## 1. Hook Removal Logic Bug (FIXED)
**Issue**: The install.sh had backwards logic - it was keeping Read hooks instead of removing them.
**Fix**: Changed `select(.matcher != "Read")` to `select(.matcher == "Read" | not)`

## 2. Uninstaller Broken in v0.3
**Issue**: The v0.3 uninstaller delegates to `claude-docs-helper.sh uninstall`, but that function only shows information - it doesn't actually uninstall anything.
**Impact**: Users can't uninstall v0.3
**Fix Needed**: Either:
  - Make the helper script actually perform uninstall, OR
  - Keep uninstall logic in uninstall.sh for all versions

## 3. Potential Hook Duplication
**Concern**: If a user runs install.sh multiple times, hooks might get duplicated
**Current behavior**: Should be OK since we remove all Read hooks first

## 4. Edge Cases to Test
- [ ] Upgrade from v0.2 with existing hook
- [ ] Multiple installations in different directories  
- [ ] Malformed settings.json
- [ ] Permission issues on ~/.claude/settings.json
- [ ] Running installer when already on v0.3

## 5. Command File Replacement
**Status**: OK - uses `cat >` which overwrites completely

## Recommendation
Fix the uninstaller issue before merging. The hook removal fix is critical for proper upgrades.