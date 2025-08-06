# PR #9 - v0.3.2 Release Merge Checklist

## Bug Fixed
- [x] v0.3.1 installer modifies tracked `docs_manifest.json` file, breaking auto-updates
- [x] Installer now detects and fixes v0.3.1 installations automatically

## Critical Changes Made
1. **Installer Branch Awareness**
   - Installer now uses `INSTALL_BRANCH` variable (set to `v0.3.2-release`)
   - Detects v0.3.1 bug and switches to correct branch for upgrade
   - Downloads template from correct branch

2. **Helper Script Version**
   - Added `SCRIPT_VERSION="0.3.2"` hardcoded in script
   - No longer reads version from manifest (which was causing issues)

3. **Git Repository Management**
   - Improved `safe_git_update()` to handle dirty repos
   - Special handling for v0.3.1 → v0.3.2 upgrades
   - Cleans dirty manifest before switching branches

## Test Results ✅
- [x] Fresh installation from v0.3.2-release
- [x] Upgrade from main branch (v0.3.1 with bug)
- [x] Upgrade with dirty manifest scenario
- [x] Uninstaller on both versions
- [x] Helper script commands (hooks, -t, what's new)
- [x] Auto-update mechanism
- [x] Documentation accuracy

## Pre-Merge Steps
1. [ ] Change `INSTALL_BRANCH` from `"v0.3.2-release"` to `"main"` in installer
2. [ ] Push all changes to v0.3.2-release branch
3. [ ] Verify GitHub Actions still work
4. [ ] Create release notes

## Post-Merge Steps
1. [ ] Tag release as v0.3.2
2. [ ] Update GitHub release page
3. [ ] Monitor for user issues
4. [ ] Close issue #5 and related issues

## Release Notes Draft
```
## v0.3.2 - Critical Bug Fix

### Fixed
- Installer no longer modifies tracked git files (fixes #5)
- Auto-updates now work correctly for all users
- Improved handling of repository state during updates

### Changed
- Helper script now uses hardcoded version number
- Installer automatically migrates v0.3.1 installations
- Better error recovery during updates

### For Users
Simply run the installer to get the fix:
```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
```
```

## Rollback Plan
If issues arise:
1. Revert merge commit on main
2. Users can manually switch: `cd ~/.claude-code-docs && git checkout main && git pull`
3. Investigate and fix in new branch