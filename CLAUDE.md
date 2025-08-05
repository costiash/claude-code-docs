# Claude Code Documentation Mirror

This repository contains local copies of Claude Code documentation from https://docs.anthropic.com/en/docs/claude-code/

The docs are automatically updated every 3 hours via GitHub Actions.

## Project Structure

```
claude-code-docs/
├── docs/                  # Mirror of Claude Code documentation
├── scripts/               # Python fetch script and helper template
│   ├── claude-docs-helper.sh.template
│   ├── fetch_claude_docs.py
│   └── requirements.txt
├── .github/workflows/     # GitHub Actions for auto-updates
├── install.sh            # Installation script
├── uninstall.sh          # Uninstallation script
├── claude-docs-helper.sh # Generated helper script (git-ignored)
└── README.md             # User documentation
```

## Development Notes

- The install.sh script supports macOS and Linux
- For Windows support, please test thoroughly before submitting PRs
- All changes should be tested locally before pushing
- The helper script is generated from template during installation
- Version numbers should be updated in: install.sh, README.md, and helper template

## Architecture Overview

1. **Installation Flow**:
   - install.sh clones repo to ~/.claude-code-docs
   - Copies claude-docs-helper.sh.template to claude-docs-helper.sh
   - Creates /docs command pointing to helper script
   - Sets up PreToolUse hook for auto-updates

2. **Update Mechanism**:
   - GitHub Actions runs fetch_claude_docs.py every 3 hours
   - Helper script checks for updates on every /docs request
   - Uses git fetch/pull to sync with GitHub
   - Handles dirty working directories gracefully

3. **Documentation Access**:
   - /docs command passes arguments to helper script
   - Helper script reads from local docs/ directory
   - Manifest file tracks all available documentation

## Testing Changes

1. Test installation on clean system
2. Test migration from older versions
3. Test auto-update functionality
4. Test with dirty working directory
5. Verify uninstall removes everything

## Known Issues

- v0.3.1: Installer modifies docs_manifest.json causing update failures
  - Fix: PR #9 updates installer and helper script
  - Users need to manually run installer for fix

## For /docs Command

When responding to /docs commands:
1. Follow the instructions in the docs.md command file
2. Report update times from docs_manifest.json
3. Read documentation files from the docs/ directory only
4. Use the manifest to know available topics