# v0.3 Ready to Merge - Next Steps

## Test Command
```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/dev-v0.3-refactor/install.sh | bash
```

## What to Test
1. **Migration** - Should remove old installation (unless it has changes)
2. **Commands** - `/docs hooks`, `/docs -t`, `/docs what's new`
3. **Uninstall** - `~/.claude-code-docs/uninstall.sh` finds all installations

## Key Changes in v0.3
- Smart migration (finds from configs, not guessing)
- Auto-removes old installations if clean
- No version dependencies
- Safe uninstaller
- All commands work with spaces

## After Testing
1. Merge to main: `git checkout main && git merge dev-v0.3-refactor`
2. Push: `git push origin main`
3. Delete dev branch: `git branch -d dev-v0.3-refactor && git push origin --delete dev-v0.3-refactor`
4. Users auto-update via manifest version 0.3

## Summary
50 commits ready. Major simplification. Works as expected.