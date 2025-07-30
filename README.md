# Claude Code Documentation Mirror

[![Last Update](https://img.shields.io/github/last-commit/ericbuess/claude-code-docs/main.svg?label=docs%20updated)](https://github.com/ericbuess/claude-code-docs/commits/main)

Local mirror of Claude Code documentation files from https://docs.anthropic.com/en/docs/claude-code/, updated every 3 hours.

## 🆕 Version 0.3 Released!

Major improvements:
- **Fixed installation location** at `~/.claude-code-docs` 
- **Automatic migration** from old installations
- **Script-based architecture** - faster and more reliable
- **Auto-updates on every request** - always stay in sync
- **Improved `/docs what's new`** - shows actual diffs with colors
- **Simplified sync status** - no confusing timestamps
- **Better performance** - all operations < 1 second

If you have v0.2 installed, it will auto-update when we push v0.3 to main!

## Why This Exists

- **Faster than web fetching** - Read from local files
- **Always up-to-date** - Auto-updates every 3 hours via GitHub Actions
- **Track documentation evolution** - See exactly what changed in docs over time with git diffs
- **Empower Claude Code** - Gives Claude the ability to deeply explore many doc files easily by referencing the manifest

## Prerequisites

This tool requires the following to be installed:
- **git** - For cloning and updating the repository (usually pre-installed)
- **jq** - For JSON processing in the auto-update hook (pre-installed on macOS; Linux users may need `apt install jq` or `yum install jq`)
- **curl** - For downloading the installation script (usually pre-installed)
- **Claude Code** - Obviously :)

**Platform Support**: macOS and Linux are fully supported. Windows support contributions welcome!

## Installation

Run this single command:

```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
```

This will:
1. Install to `~/.claude-code-docs` (or migrate existing installation)
2. Create the `/docs` slash command
3. Set up automatic git pull when reading docs

**Note**: The command is `/docs (user)` - it will show in your command list with "(user)" after it to indicate it's a user-created command.

## Usage

The `/docs` command provides instant access to documentation with optional freshness checking.

### Default: Lightning-fast access (no checks)
```bash
/docs hooks        # Instantly read hooks documentation
/docs mcp          # Instantly read MCP documentation  
/docs memory       # Instantly read memory documentation
```

You'll see: `📚 Reading from local docs (run /docs -t to check freshness)`

### Check documentation sync status with -t flag
```bash
/docs -t           # Show sync status with GitHub
/docs -t hooks     # Check sync status, then read hooks docs
/docs -t mcp       # Check sync status, then read MCP docs
```

### See what's new
```bash
/docs what's new   # Show recent documentation changes with diffs
```

### Uninstall
```bash
/docs uninstall    # Remove claude-code-docs completely
```

### Creative usage examples
```bash
# Natural language queries work great
/docs what environment variables exist and how do I use them?
/docs explain the differences between hooks and MCP

# Check for recent changes
/docs -t what's new in the latest documentation?

# Search across all docs
/docs find all mentions of authentication
/docs how do I customize Claude Code's behavior?
```

## How Updates Work

The docs automatically stay up-to-date:
- GitHub Actions updates the repository every 3 hours
- The hook compares GitHub's timestamp with your local sync time
- If GitHub has newer content, it automatically syncs before reading
- You'll see "🔄 Updating docs to latest version..." when this happens
- No manual updates needed!

**Performance**:
- `/docs` reads instantly with a simple helper script
- `/docs -t` shows you exact timestamps of GitHub updates vs local sync

## Migration from v0.2

If you have an older installation, v0.3 will automatically:
1. Find your existing installation
2. Check for any custom files you added
3. Migrate to `~/.claude-code-docs`
4. Clean up the old location (if safe)

You'll see a brief notice on first use after migration.

## Troubleshooting

### Command not found
If `/docs` returns "command not found":
1. Check if the command file exists: `ls ~/.claude/commands/docs.md`
2. Restart Claude Code to reload commands
3. Re-run the installation script

### Documentation not updating
If documentation seems outdated:
1. Run `/docs -t` to check sync status and force an update
2. Manually update: `cd ~/.claude-code-docs && git pull`
3. Check if GitHub Actions are running: [View Actions](https://github.com/ericbuess/claude-code-docs/actions)

### Installation errors
- **"git/jq/curl not found"**: Install the missing tool first
- **"Failed to clone repository"**: Check your internet connection
- **"Failed to update settings.json"**: Check file permissions on `~/.claude/settings.json`

## Uninstalling

To completely remove the docs integration:

```bash
/docs uninstall
```

Or run:
```bash
~/.claude-code-docs/uninstall.sh
```

See [UNINSTALL.md](UNINSTALL.md) for manual uninstall instructions.

## Security Notes

- The installer modifies `~/.claude/settings.json` to add an auto-update hook
- The hook only runs `git pull` when reading documentation files
- All operations are limited to the documentation directory
- No data is sent externally - everything is local
- **Repository Trust**: The installer clones from GitHub over HTTPS. For additional security, you can:
  - Fork the repository and install from your own fork
  - Clone manually and run the installer from the local directory
  - Review all code before installation

## What's New in v0.3

- **Fixed installation location**: Always installs to `~/.claude-code-docs`
- **Automatic migration**: Seamlessly moves from old locations
- **Script-based architecture**: All logic in a single maintainable script
- **Performance improvements**: Operations complete in < 1 second
- **New `/docs what's new` command**: See actual documentation changes
- **Simplified codebase**: Easier to understand and contribute

## License

Documentation content belongs to Anthropic.