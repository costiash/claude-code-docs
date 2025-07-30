# Updating Claude Code Docs

## For Users with Existing Installations

If you installed claude-code-docs before and want to update to the latest version with bug fixes:

### Method 1: Re-run the installer (Recommended)
```bash
cd /path/to/claude-code-docs
git pull
./install.sh
```

This will:
- Update your repository to the latest version
- Update the `/user:docs` command
- Update the auto-update hook with bug fixes

### Method 2: Fresh reinstall
```bash
# First uninstall
cd /path/to/claude-code-docs
./uninstall.sh

# Then reinstall
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
```

## Important Notes

- **The auto-update hook does NOT update itself**. You must re-run `install.sh` after major updates
- If you had the version with the circular logic bug (before July 29, 2025), you MUST re-run the installer
- The uninstaller only removes the repository. To fully clean up, also remove:
  - `~/.claude/commands/docs.md`
  - The hook entry in `~/.claude/settings.json`

## Checking Your Version

To see if you have the old broken hook:
```bash
grep "GITHUB_TS=\$(jq -r .last_updated" ~/.claude/settings.json
```

If this returns a match, you have the old version and should update.

The new version uses `git fetch` to check for updates instead of reading local timestamps.