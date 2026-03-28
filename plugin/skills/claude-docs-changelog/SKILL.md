---
name: claude-docs-changelog
description: >
  Generate a self-contained HTML changelog report showing recent documentation
  changes with interactive course generation buttons. Use this skill when the
  user asks for a docs changelog, documentation report, what changed recently,
  recent doc updates as a report, or runs `/docs --report`. Discovers changes
  via git history, categorizes them, summarizes what's new, and produces a
  stunning Obsidian & Amber themed HTML report where each entry has a
  "Create Course" button that copies the course command to clipboard.
---

# Documentation Changelog Report

Generate a self-contained HTML report showing recent documentation changes. The report groups changes by category, summarizes what's new or updated, and includes a "Create Course" button on each card so the user can instantly generate an interactive course for any topic that caught their eye.

## When to Trigger

- User says "docs changelog", "docs report", "what changed in the docs", "recent doc updates report"
- User runs `/docs --report`, `/docs changelog`, or `/docs --report <timeframe>`
- User asks for a visual summary of documentation changes

## The Process (3 Phases)

### Phase 1: Discover Changes

**Find what changed in the documentation directory:**

```bash
cd ~/.claude-code-docs && git log --since="<timeframe>" --name-status --pretty=format:"%H %ai %s" -- docs/
```

**Default timeframe:** Last 7 days. The user can specify a different window:
- `/docs --report` → last 7 days
- `/docs --report 24h` → last 24 hours
- `/docs --report 30d` → last 30 days
- `/docs --report 2026-03-20` → since that date

**Parse the output:**
- `A` = Added (new doc)
- `M` = Modified (updated doc)
- `D` = Deleted (removed doc)

If there are no changes in the timeframe, tell the user and suggest a wider window.

**Categorize each file** using the same patterns from `manifest-reference.md`:

| File pattern | Category | Label |
|---|---|---|
| `claude-code__*.md` | cli | Claude Code CLI |
| `docs__en__agent-sdk__*.md` | sdk | Agent SDK |
| `docs__en__api__*.md` | api | Claude API |
| `docs__en__agents-and-tools__*.md` | tools | Agents & Tools |
| `docs__en__build-with-claude__*.md` | platform | Claude Platform |
| `docs__en__about-claude__*.md` | about | About Claude |
| `docs__en__resources__prompt-library__*.md` | prompts | Prompt Library |
| `docs__en__test-and-evaluate__*.md` | testing | Testing & Evaluation |
| `docs__en__release-notes__*.md` | releases | Release Notes |

**Limit scope:** If there are more than 30 changed files, focus on the most recent 30 and note how many were omitted.

### Phase 2: Analyze Changes

For each changed file (or the most significant ones if there are many):

1. **Read the file** to understand the current content
2. If the file was modified (not new), run `git diff` on it to see what specifically changed
3. **Extract key points:** What's new? What was updated? What are the highlights?
4. **Write a 1-2 sentence summary** of the change
5. **Extract 3-6 bullet points** describing specific additions or updates

**For new files (A):** Read the full file and summarize what it covers.
**For modified files (M):** Focus on what changed in the diff, not the entire file.
**For deleted files (D):** Just note what was removed with a one-line description.

Group related changes (e.g., if 6 SDK language docs were all updated the same way, combine them into one card).

### Phase 3: Generate the HTML Report

Generate a single self-contained HTML file using the **Obsidian & Amber** design system. Save to:

```bash
mkdir -p ~/.claude-code-docs/courses
```

Name the file: `~/.claude-code-docs/courses/changelog-<date>.html` (e.g., `changelog-2026-03-28.html`)

**HTML structure:**

```
├── Header (title, date range, sync status badge)
├── Stats bar (count per category with colored numbers)
├── Key Highlights box (3-6 most notable changes)
├── Section per category
│   ├── Section heading (icon, label, count)
│   └── Cards per changed doc
│       ├── Title + tag (New/Updated/Removed)
│       ├── Summary paragraph
│       ├── Bullet list of key changes
│       ├── Source link → official docs URL
│       └── "Create Course" button
└── Footer (generated from, doc count, date)
```

**Design rules (Obsidian & Amber):**

Use these exact CSS variables from the course design system:

```css
:root {
  --bg: #0D0D16;
  --surface: #161624;
  --surface-hover: #1C1A28;
  --border: #2A2840;
  --text: #E8E0D4;
  --text-muted: #5C5852;
  --accent: #F0A050;
  --accent-dim: rgba(240, 160, 80, 0.08);
  --blue: #60B0E0;
  --blue-dim: rgba(96, 176, 224, 0.08);
  --green: #50C8A0;
  --green-dim: rgba(80, 200, 160, 0.08);
  --purple: #C080E0;
  --purple-dim: rgba(192, 128, 224, 0.08);
  --red: #F06060;
  --red-dim: rgba(240, 96, 96, 0.06);
  --radius: 10px;
}
```

**Typography:** Use the same fonts as the course skill:
```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```
- `Instrument Serif` for h1/h2 headings
- `Outfit` for body text
- `JetBrains Mono` for code and badges

**Include the grain overlay** (same as course design system):
```css
body::after {
  content: '';
  position: fixed; top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none; z-index: 9999; opacity: 0.035;
  background-image: url("data:image/svg+xml,...");  /* same noise SVG */
}
```

**Card styling:**
- Background: `--surface` with `--border` border
- Hover: border shifts to `--accent` muted, subtle glow
- Inner shadow highlight: `inset 0 1px 0 rgba(255,255,255,0.04)`

**Tags:**
- `New` → green badge (`--green-dim` bg, `--green` text)
- `Updated` → blue badge (`--blue-dim` bg, `--blue` text)
- `Removed` → red badge (`--red-dim` bg, `--red` text)
- `Beta` → purple badge (`--purple-dim` bg, `--purple` text)

**Category icons:**
- CLI: `>_` (terminal prompt)
- SDK: `{}` (code braces)
- API: `⟡` (diamond)
- Platform: `◈` (nested diamond)
- Prompt Library: `✎` (pen)
- Other: `●` (dot)

### The "Create Course" Button

Each card gets a button in its footer area that lets the user generate a course for that topic.

**Button behavior (JavaScript):**
1. On click, copy the command `/docs --course <topic>` to the clipboard
2. Show a toast notification: "Copied! Paste in Claude Code to generate a course."
3. The toast auto-dismisses after 3 seconds

**Button HTML pattern:**
```html
<button class="course-btn" data-topic="hooks" onclick="copyCourseCmd(this)">
  <span class="course-btn-icon">▶</span>
  Create Course
</button>
```

**Button CSS:**
```css
.course-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid var(--accent);
  background: var(--accent-dim);
  color: var(--accent);
  font-family: 'Outfit', sans-serif;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.course-btn:hover {
  background: var(--accent);
  color: var(--bg);
  box-shadow: 0 0 20px rgba(240, 160, 80, 0.25);
}
.course-btn-icon {
  font-size: 0.65rem;
}
```

**Toast notification:**
```css
.toast {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--surface);
  border: 1px solid var(--accent);
  color: var(--accent);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius);
  font-family: 'Outfit', sans-serif;
  font-size: 0.88rem;
  font-weight: 500;
  box-shadow: 0 8px 32px rgba(0,0,8,0.5), 0 0 20px rgba(240,160,80,0.15);
  opacity: 0;
  transition: opacity 0.3s, transform 0.3s;
  z-index: 10000;
}
.toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
```

**JavaScript:**
```javascript
function copyCourseCmd(btn) {
  const topic = btn.dataset.topic;
  const cmd = '/docs --course ' + topic;
  navigator.clipboard.writeText(cmd).then(() => {
    showToast('Copied! Paste in Claude Code: ' + cmd);
  }).catch(() => {
    // Fallback for older browsers
    const ta = document.createElement('textarea');
    ta.value = cmd; document.body.appendChild(ta);
    ta.select(); document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Copied! Paste in Claude Code: ' + cmd);
  });
}

function showToast(msg) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toast._timeout);
  toast._timeout = setTimeout(() => toast.classList.remove('show'), 3000);
}
```

### Phase 4: Open and Present

After generating the HTML:
1. Open it in the browser
2. Tell the user where it's saved: `~/.claude-code-docs/courses/changelog-<date>.html`
3. Summarize the key findings: "Found X changes across Y categories in the last Z days."
4. Mention they can click "Create Course" on any card to copy the course generation command

## URL Generation

Use the same URL rules as the `claude-docs` skill:
- `claude-code__<page>.md` → `https://code.claude.com/docs/en/<page>`
- `docs__en__<path>.md` → `https://platform.claude.com/en/docs/<path>` (replace `__` with `/`)

## Topic Extraction for Course Buttons

The `data-topic` attribute on each course button should be the human-readable topic name extracted from the filename:
- `claude-code__hooks.md` → `hooks`
- `claude-code__hooks-guide.md` → `hooks guide`
- `docs__en__agent-sdk__python.md` → `Agent SDK Python`
- `docs__en__build-with-claude__prompt-caching.md` → `prompt caching`
- `docs__en__agents-and-tools__tool-use__overview.md` → `tool use`

Strip the category prefix, replace `__` and `-` with spaces, and capitalize naturally.
