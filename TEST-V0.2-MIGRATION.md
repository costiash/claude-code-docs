# Test v0.2 Migration Commands

## Install v0.2 from main branch
```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/main/install.sh | bash
```

## Install last commit before v0.3 refactor
```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/57fc41a/install.sh | bash
```

## Then test v0.3 migration
```bash
curl -fsSL https://raw.githubusercontent.com/ericbuess/claude-code-docs/dev-v0.3-refactor/install.sh | bash
```

## Test Plan
1. Run first command (v0.2 from main)
2. Check installation location with `pwd` in the directory
3. Run v0.3 installer - should migrate/remove old
4. Repeat with second command (specific commit)

## Expected Results
- v0.2 installs wherever you are (or ~/claude-code-docs)
- v0.3 finds it from config and migrates to ~/.claude-code-docs
- Old directory removed (unless has changes)

## Quick Reset Between Tests
```bash
rm -rf ~/.claude-code-docs ~/claude-code-docs
rm -f ~/.claude/commands/docs.md
# Remove hooks manually from ~/.claude/settings.json if needed
```