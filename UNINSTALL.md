# Uninstalling Claude Code Documentation Mirror

## Plugin Uninstall (Recommended)

If you installed via the Claude Code plugin:

```bash
/plugin uninstall claude-docs@claude-code-docs
```

To also remove the local documentation files:
```bash
rm -rf ~/.claude-code-docs
```

## Legacy Script Uninstall

If you have an older script-based installation (v0.6.0 or earlier):

```bash
~/.claude-code-docs/uninstall.sh
```

This removes:
1. Legacy `/docs` command from `~/.claude/commands/docs.md` (if present)
2. Legacy hooks from `~/.claude/settings.json` (if present)
3. Optionally, the `~/.claude-code-docs/` directory

## Manual Cleanup

```bash
# Remove legacy command (if present)
rm -f ~/.claude/commands/docs.md

# Remove local documentation
rm -rf ~/.claude-code-docs
```

## Reinstalling

```bash
/plugin marketplace add costiash/claude-code-docs
/plugin install claude-docs@claude-code-docs
```
