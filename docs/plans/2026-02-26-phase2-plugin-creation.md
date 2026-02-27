# Phase 2: Plugin Creation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a native Claude Code Plugin that provides the `/docs` command, auto-discoverable Skill, and SessionStart hook — additive only, nothing removed from existing functionality.

**Architecture:** Two-layer system. The plugin (static, distributed via marketplace) provides logic (command, skill, hook). The docs data (dynamic, CI/CD updated) lives in a git clone at `~/.claude-code-docs/`. The plugin uses Claude's native Read/Grep/Glob tools — zero Python or shell script dependencies for users.

**Tech Stack:** Claude Code Plugin System (JSON manifests, markdown commands/skills, JSON hooks with bash scripts)

---

## Pre-Flight

**Before starting, ensure Phase 1 is merged and switch to the correct branch:**

```bash
cd /home/rudycosta3/claude-code-docs
git checkout feat/plugin-modernization
git merge main --no-edit  # Get Phase 1 fixes
```

---

### Task 1: Create Marketplace Manifest

The marketplace manifest tells Claude Code that this repository contains a plugin.

**Files:**
- Create: `.claude-plugin/marketplace.json`

**Step 1: Create the directory**

```bash
mkdir -p .claude-plugin
```

**Step 2: Create marketplace manifest**

Create `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    {
      "name": "claude-docs",
      "description": "Searchable local mirror of Claude documentation — always fresh, always available",
      "source": "./plugin"
    }
  ]
}
```

**Step 3: Verify JSON is valid**

```bash
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json')); print('✅ Valid JSON')"
```

**Step 4: Commit**

```bash
git add .claude-plugin/marketplace.json
git commit -m "feat: add marketplace manifest for plugin discovery

Registers the plugin directory at ./plugin for Claude Code's
plugin marketplace system."
```

---

### Task 2: Create Plugin Manifest

The plugin manifest defines the plugin's identity and components.

**Files:**
- Create: `plugin/.claude-plugin/plugin.json`

**Step 1: Create the directory**

```bash
mkdir -p plugin/.claude-plugin
```

**Step 2: Create plugin manifest**

Create `plugin/.claude-plugin/plugin.json`:

```json
{
  "name": "claude-docs",
  "version": "0.6.0",
  "description": "Searchable local mirror of Claude documentation. Provides the /docs command for instant access to API references, guides, and tutorials. Docs auto-update via SessionStart hook.",
  "author": "costiash",
  "repository": "https://github.com/costiash/claude-code-docs",
  "license": "MIT",
  "keywords": ["documentation", "claude", "api", "search", "reference"],
  "hooks": "./hooks/hooks.json"
}
```

**Step 3: Verify JSON is valid**

```bash
python3 -c "import json; json.load(open('plugin/.claude-plugin/plugin.json')); print('✅ Valid JSON')"
```

**Step 4: Commit**

```bash
git add plugin/.claude-plugin/plugin.json
git commit -m "feat: add plugin manifest with metadata

Defines the claude-docs plugin identity: name, version, description,
and component locations for Claude Code's plugin system."
```

---

### Task 3: Create `/docs` Slash Command (Plugin Version)

The plugin version of the `/docs` command uses Claude's native tools (Read, Grep, Glob) instead of shell scripts.

**Files:**
- Create: `plugin/commands/docs.md`

**Step 1: Create the directory**

```bash
mkdir -p plugin/commands
```

**Step 2: Create the command file**

Create `plugin/commands/docs.md`:

```markdown
# Claude Code Documentation — Plugin Command

You are a documentation assistant for Claude Code. Answer the user's question using locally-stored documentation.

## Documentation Location

Docs are stored at `~/.claude-code-docs/docs/` as markdown files. If this directory doesn't exist, inform the user:

> Documentation not found. Run this to set up:
> ```
> git clone https://github.com/costiash/claude-code-docs.git ~/.claude-code-docs
> ```

## How to Handle Requests

### Step 1: Understand Intent

Analyze `$ARGUMENTS` to determine:
- **Direct lookup**: User names a specific topic (e.g., "hooks", "mcp", "memory")
- **Information search**: User asks a question (e.g., "how do I use extended thinking?")
- **Discovery**: User wants to browse (e.g., "show me all MCP docs")
- **Freshness check**: `-t` flag or "what's new"

### Step 2: Find Relevant Documentation

**For direct lookup** — find files matching the topic:
1. Use Glob to find: `~/.claude-code-docs/docs/*$TOPIC*.md`
2. Common patterns:
   - Claude Code CLI docs: `docs__en__<topic>.md`
   - Platform docs: `docs/en__docs__<section>__<topic>.md`
3. Read the matching file(s)

**For information search** — search content:
1. Use Grep to search: `grep -ri "<keywords>" ~/.claude-code-docs/docs/`
2. Read the top matching files
3. Extract relevant sections

**For discovery** — list available docs:
1. Use Glob: `~/.claude-code-docs/docs/*.md`
2. Filter by pattern if topic specified
3. Present organized list with categories

**For freshness check** (`-t`):
1. Check git status: `cd ~/.claude-code-docs && git log -1 --format="%ci" && git pull --dry-run 2>&1`
2. Report last update time and whether updates are available
3. If updates available, run `cd ~/.claude-code-docs && git pull`

### Step 3: Categorize Results

When results span multiple product areas, use these labels:
- Files matching `docs__en__*.md` → **Claude Code CLI**
- Files matching `en__docs__agent-sdk__*.md` → **Claude Agent SDK**
- Files matching `en__api__*.md` → **Claude API**
- Files matching `en__docs__build-with-claude__*.md` → **Claude Documentation**
- Files matching `en__resources__prompt-library__*.md` → **Prompt Library**

### Step 4: Present Results

**Same product context** → Read ALL matching docs silently, synthesize unified answer, cite sources.

**Different product contexts** → Ask user which product area with AskUserQuestion:
```
"This topic exists in multiple Claude products:
○ 1. Claude Code CLI - ...
○ 2. Claude API - ...
Which are you working with?"
```

After selection → synthesize within that context.

### Step 5: Always Include

- Natural language synthesis (don't dump raw file contents)
- Source links in format: `https://docs.anthropic.com/<path>`
- Suggest related topics when relevant

## Special Commands

- `$ARGUMENTS` is `-t` → Run freshness check
- `$ARGUMENTS` is `what's new` → Show recent git log: `cd ~/.claude-code-docs && git log --oneline -10`
- `$ARGUMENTS` is `uninstall` → Show: `rm -rf ~/.claude-code-docs && rm ~/.claude/commands/docs.md`

## User's Request

The user requested: `$ARGUMENTS`
```

**Step 3: Verify the file is valid markdown**

```bash
wc -l plugin/commands/docs.md
# Should be ~80 lines
```

**Step 4: Commit**

```bash
git add plugin/commands/docs.md
git commit -m "feat: add /docs slash command for plugin

AI-powered documentation lookup using Claude's native Read/Grep/Glob
tools. Zero shell or Python dependencies — Claude reads the docs
directly from ~/.claude-code-docs/docs/."
```

---

### Task 4: Create Documentation Skill

The Skill enables auto-discovery — Claude automatically reads relevant docs when the user asks about Claude Code features.

**Files:**
- Create: `plugin/skills/claude-docs/SKILL.md`
- Create: `plugin/skills/claude-docs/manifest-reference.md`

**Step 1: Create the directory**

```bash
mkdir -p plugin/skills/claude-docs
```

**Step 2: Create SKILL.md**

Create `plugin/skills/claude-docs/SKILL.md`:

```markdown
---
name: claude-docs-search
description: >
  Search and read locally-stored Claude documentation. Use when the user asks about
  Claude Code features (hooks, skills, MCP, settings, plugins), Claude API usage,
  Agent SDK, prompt engineering, or any Anthropic documentation topic. Provides
  instant access to official docs without web searches.
---

# Claude Documentation Search Skill

You have access to a local mirror of Claude's official documentation at `~/.claude-code-docs/docs/`.

## When to Use This Skill

Activate when the user asks about:
- Claude Code features: hooks, skills, MCP, plugins, settings, slash commands, sub-agents
- Claude API: messages, tool use, streaming, batch processing, embeddings
- Agent SDK: Python/TypeScript SDK, sessions, custom tools, subagents
- Prompt engineering: best practices, system prompts, chain of thought
- Any topic covered by docs.anthropic.com or code.claude.com

## How to Search

### Filename-Based Category Inference

Documentation files follow naming conventions:
- `docs__en__<page>.md` → Claude Code CLI docs (hooks, mcp, skills, etc.)
- `en__docs__agent-sdk__<page>.md` → Agent SDK docs
- `en__api__<lang>__<endpoint>.md` → API reference (Python, TypeScript, Go, Java, Kotlin, Ruby)
- `en__docs__build-with-claude__<page>.md` → Guides and tutorials
- `en__resources__prompt-library__<name>.md` → Prompt templates

### Search Strategy

1. **Start with Glob** to find candidate files:
   ```
   Glob: ~/.claude-code-docs/docs/*<keyword>*.md
   ```

2. **If Glob finds matches**, Read the most relevant files (up to 3-4)

3. **If Glob finds nothing**, use Grep for content search:
   ```
   Grep: "<keyword>" in ~/.claude-code-docs/docs/
   ```

4. **Read matching files** and extract relevant sections

### Synthesis Instructions

- Read ALL matching docs within the same product context
- Synthesize a unified answer — don't dump raw file contents
- Include code examples from the docs when relevant
- Cite sources with links: `https://docs.anthropic.com/<path>` or `https://code.claude.com/<path>`
- If results span different products, ask user which context they mean

### Determining Source URLs

- Files starting with `docs__en__` → `https://code.claude.com/docs/en/<page>`
- Files starting with `en__` → `https://platform.claude.com/<path>` (replace `__` with `/`)

## Reference Files

- `manifest-reference.md` — Documentation about the manifest structure and categories
```

**Step 3: Create manifest reference file**

Create `plugin/skills/claude-docs/manifest-reference.md`:

```markdown
# Documentation Manifest Reference

## Overview

The documentation mirror at `~/.claude-code-docs/` contains:
- `docs/` — Markdown files fetched from Anthropic's documentation sites
- `docs/docs_manifest.json` — File tracking manifest (updated by CI/CD)
- `paths_manifest.json` — Path categorization manifest (updated by CI/CD)

## Categories

Documentation is organized into these categories:

| Category | Description | File Pattern |
|----------|------------|-------------|
| `claude_code` | Claude Code CLI docs | `docs__en__*.md` |
| `api_reference` | API endpoints, SDK docs | `en__api__*.md` |
| `core_documentation` | Guides, tutorials | `en__docs__build-with-claude__*.md` |
| `prompt_library` | Prompt templates | `en__resources__prompt-library__*.md` |
| `release_notes` | Changelog | `en__release-notes__*.md` |
| `resources` | Additional resources | `en__resources__overview.md` |

## User-Friendly Labels

When presenting results to users:
- `claude_code` → "Claude Code CLI"
- `api_reference` → "Claude API"
- Agent SDK paths → "Claude Agent SDK"
- `core_documentation` → "Claude Documentation"
- `prompt_library` → "Prompt Library"

## Dynamic Discovery

To count available docs:
```
Glob: ~/.claude-code-docs/docs/*.md
```

To check categories in manifest:
```
Read: ~/.claude-code-docs/paths_manifest.json
```
```

**Step 4: Commit**

```bash
git add plugin/skills/claude-docs/SKILL.md plugin/skills/claude-docs/manifest-reference.md
git commit -m "feat: add claude-docs-search Skill for auto-discovery

Claude automatically discovers and reads relevant documentation when
users ask about Claude Code features, API usage, Agent SDK, etc.
Uses native Read/Grep/Glob tools — zero dependencies."
```

---

### Task 5: Create SessionStart Hook

The hook ensures `~/.claude-code-docs/` exists and stays fresh by running `git pull` on session start.

**Files:**
- Create: `plugin/hooks/hooks.json`
- Create: `plugin/hooks/sync-docs.sh`

**Step 1: Create the directory**

```bash
mkdir -p plugin/hooks
```

**Step 2: Create the sync script**

Create `plugin/hooks/sync-docs.sh`:

```bash
#!/bin/bash
# Claude Code Docs — SessionStart sync hook
# Ensures ~/.claude-code-docs/ exists and is up-to-date

DOCS_DIR="$HOME/.claude-code-docs"
REPO_URL="https://github.com/costiash/claude-code-docs.git"

# JSON output for SessionStart additionalContext
output_context() {
    local msg="$1"
    cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "$msg"
  }
}
EOF
}

# Clone if not exists
if [ ! -d "$DOCS_DIR" ]; then
    git clone --depth 1 "$REPO_URL" "$DOCS_DIR" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        DOC_COUNT=$(find "$DOCS_DIR/docs" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
        output_context "Claude documentation installed: $DOC_COUNT docs available at ~/.claude-code-docs/. Use /docs to search."
    else
        output_context "Failed to clone Claude documentation. Run: git clone $REPO_URL $DOCS_DIR"
    fi
    exit 0
fi

# Pull updates (non-blocking, timeout after 10s)
cd "$DOCS_DIR" || exit 0
BEFORE=$(git rev-parse HEAD 2>/dev/null)
timeout 10 git pull --ff-only origin main >/dev/null 2>&1 || true
AFTER=$(git rev-parse HEAD 2>/dev/null)

DOC_COUNT=$(find "$DOCS_DIR/docs" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

if [ "$BEFORE" != "$AFTER" ]; then
    NEW_COMMITS=$(git log --oneline "$BEFORE..$AFTER" 2>/dev/null | wc -l | tr -d ' ')
    output_context "Claude docs updated ($NEW_COMMITS new commits). $DOC_COUNT docs available. Use /docs to search."
else
    output_context "Claude docs up-to-date. $DOC_COUNT docs available. Use /docs to search."
fi

exit 0
```

**Step 3: Make script executable**

```bash
chmod +x plugin/hooks/sync-docs.sh
```

**Step 4: Create hooks.json**

Create `plugin/hooks/hooks.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/hooks/sync-docs.sh",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

**Step 5: Verify JSON is valid**

```bash
python3 -c "import json; json.load(open('plugin/hooks/hooks.json')); print('✅ Valid JSON')"
```

**Step 6: Commit**

```bash
git add plugin/hooks/hooks.json plugin/hooks/sync-docs.sh
git commit -m "feat: add SessionStart hook for docs auto-sync

On each session start, the hook:
1. Clones ~/.claude-code-docs/ if it doesn't exist (first run)
2. Runs git pull if it does exist (subsequent runs)
3. Reports doc count via SessionStart additionalContext

Uses CLAUDE_PLUGIN_ROOT for portable script paths. Timeout of 15s
ensures session start isn't blocked by network issues."
```

---

### Task 6: Update README with Dual Installation Instructions

Add plugin installation as the recommended method while keeping `curl | bash` as legacy.

**Files:**
- Modify: `README.md`

**Step 1: Add plugin installation section**

In `README.md`, update the Installation section to present both methods. The plugin method should come first as "Recommended":

```markdown
## Installation

### Method 1: Plugin Install (Recommended)

If you have Claude Code with plugin support:

```bash
/plugin marketplace add costiash/claude-code-docs
/plugin install claude-docs
```

**What it does:**
1. Installs the claude-docs plugin (provides /docs command + auto-discovery Skill)
2. On first session, automatically clones documentation to `~/.claude-code-docs/`
3. On each subsequent session, auto-updates docs via git pull

**Requirements:** Claude Code with plugin support

### Method 2: Script Install (Legacy)

For environments without plugin support:

```bash
curl -fsSL https://raw.githubusercontent.com/costiash/claude-code-docs/main/install.sh | bash
```

**What it does:**
1. Clones repository to `~/.claude-code-docs`
2. Sets up `/docs` command in `~/.claude/commands/docs.md`
3. Installs helper scripts

**Requirements:** git, jq, curl. Optional: Python 3.9+ for enhanced search.
```

**Step 2: Verify changes render correctly**

```bash
head -100 README.md
```

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add plugin installation as recommended method

Plugin install is now the primary method. Script install (curl | bash)
remains as legacy for environments without plugin support.
Both methods use ~/.claude-code-docs/ for documentation storage."
```

---

### Task 7: Verify Plugin Structure

**Step 1: Verify directory structure**

```bash
find plugin/ -type f | sort
```

Expected output:
```
plugin/.claude-plugin/plugin.json
plugin/commands/docs.md
plugin/hooks/hooks.json
plugin/hooks/sync-docs.sh
plugin/skills/claude-docs/SKILL.md
plugin/skills/claude-docs/manifest-reference.md
```

**Step 2: Verify all JSON files are valid**

```bash
for f in .claude-plugin/marketplace.json plugin/.claude-plugin/plugin.json plugin/hooks/hooks.json; do
    python3 -c "import json; json.load(open('$f')); print(f'✅ {\"$f\"}')" || echo "❌ $f"
done
```

**Step 3: Run full test suite**

```bash
pytest tests/ -q
# Expected: All tests pass (Phase 2 is additive — no existing code modified except README)
```

**Step 4: Review all changes**

```bash
git log --oneline feat/plugin-modernization ^main
git diff main..feat/plugin-modernization --stat
```

**Step 5: Summary of changes**

The branch should contain these commits:
1. `feat: add marketplace manifest for plugin discovery`
2. `feat: add plugin manifest with metadata`
3. `feat: add /docs slash command for plugin`
4. `feat: add claude-docs-search Skill for auto-discovery`
5. `feat: add SessionStart hook for docs auto-sync`
6. `docs: add plugin installation as recommended method`

**Step 6: Ready for PR**

```bash
git push origin feat/plugin-modernization
gh pr create --base main --head feat/plugin-modernization \
  --title "feat: add Claude Code Plugin (Phase 2 — plugin-modernization)" \
  --body "## Summary
- Create native Claude Code plugin with /docs command, Skill, and SessionStart hook
- Plugin uses Claude's native Read/Grep/Glob tools — zero Python/shell dependencies for users
- Docs stored separately at ~/.claude-code-docs/ via git clone (updated by SessionStart hook)
- Additive only — no existing functionality removed

## New Files
- .claude-plugin/marketplace.json — marketplace registration
- plugin/.claude-plugin/plugin.json — plugin metadata
- plugin/commands/docs.md — /docs slash command (plugin version)
- plugin/skills/claude-docs/SKILL.md — auto-discoverable documentation Skill
- plugin/skills/claude-docs/manifest-reference.md — category reference
- plugin/hooks/hooks.json — SessionStart hook config
- plugin/hooks/sync-docs.sh — git clone/pull script

## Test plan
- [ ] All existing tests pass
- [ ] Plugin JSON manifests are valid
- [ ] /docs command works via plugin
- [ ] Skill auto-discovers for Claude Code questions
- [ ] SessionStart hook clones docs on first run
- [ ] SessionStart hook updates docs on subsequent runs
- [ ] Legacy curl | bash still works alongside plugin"
```
