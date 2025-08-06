# Next Steps Plan - v0.3.2 Release

## Critical Issue Discovered
The installer has a **critical bug** that would break the v0.3.2 release:
- Installer always pulls from 'main' branch instead of the correct branch
- This overwrites v0.3.2 fixes with old v0.3.1 code
- Affects lines 167, 175, and 286 in install.sh

## Immediate Actions Required

### 1. Fix Installer Branch References ⚠️ CRITICAL
The installer must be fixed to use the correct branch:
- Line 167: `git pull --quiet origin main` → needs to use correct branch
- Line 175: `git fetch origin main` → needs to use correct branch  
- Line 286: Template download from `/main/` → needs to use `/v0.3.2-release/`

### 2. Complete Testing Suite
After fixing installer:
- Run comprehensive_test.sh in safe directory
- Test fresh installation scenario
- Test upgrade from main (v0.3.1) scenario
- Verify all auto-update mechanisms work

### 3. Release Process
Once tests pass:
1. Push fixed v0.3.2-release branch
2. Create/update PR #9 with test results
3. Merge to main
4. Tag v0.3.2 release
5. Verify main branch installer works

## Technical Details

### The Problem
When users run the installer from main (production), it:
1. Clones the repo (gets main branch by default)
2. Runs `safe_git_update()` which pulls from main (line 167)
3. Downloads template from main branch (line 286)
4. This overwrites any v0.3.2 fixes with v0.3.1 code!

### The Solution
Make installer branch-aware:
- For production (main): Pull from main, download from main
- For v0.3.2-release: Pull from v0.3.2-release, download from v0.3.2-release
- Use GitHub raw URL with correct branch reference

### Test Scenarios
1. **Fresh Install**: No existing installation → should install v0.3.2
2. **Upgrade from v0.3.1**: Has dirty manifest → should fix and update
3. **Upgrade from clean**: Already on main → should update cleanly
4. **Dev branch test**: On v0.3.2-release → should stay on branch

## Success Criteria
- Installer correctly installs v0.3.2 code
- Auto-updates work without modifying tracked files
- Helper script version shows "0.3.2"
- No dirty git status after installation
- All test scenarios pass

## Timeline
1. Fix installer (5 mins)
2. Run tests (10 mins)
3. Push and create PR (5 mins)
4. Total: ~20 minutes to release-ready