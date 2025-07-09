# Uninstalling Claude Code Documentation Mirror

## Quick Uninstall

Run the uninstall script from the installation directory:

```bash
./uninstall.sh
```

## Manual Uninstall

If you prefer to uninstall manually:

1. Remove the installation directory:
   ```bash
   rm -rf /path/to/claude-code-docs
   ```

2. That's it! The installation is completely self-contained.

## Multiple Installations

If you have multiple installations (e.g., one in your home directory and one in Projects), you'll need to remove each one separately.

To find all installations:
```bash
find ~ -name "claude-code-docs" -type d 2>/dev/null
```

## What Gets Removed

- The entire claude-code-docs directory
- Python virtual environment (.venv)
- Local git repository  
- All documentation files
- Installation scripts

The uninstaller does NOT remove:
- Your global git configuration
- Any other Claude Code installations
- Your .claude configuration directories