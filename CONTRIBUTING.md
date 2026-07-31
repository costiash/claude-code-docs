# Contributing Guidelines

Thank you for contributing to **claude-code-docs** — a Claude Code plugin that gives Claude local, searchable access to Anthropic's documentation.

This repository is a **manifest + client-side fetch** system, not a documentation mirror: it commits only metadata (`paths_manifest.json` + `search_index.json`). End users fetch the actual `.md` pages from Anthropic's servers at runtime into a local cache. **Read [`ARCHITECTURE.md`](./ARCHITECTURE.md) first** — it covers the manifest/index schemas, the fetch pipeline, the safeguards, and the invariant below.

## The one rule that matters most

**Never commit Anthropic documentation prose — not at the tip, not in history.**

CI fetches pages only to hash them and build a lossy, prose-free index, into the gitignored `.doc_fetch/` scratch dir. The client caches fetched pages under the gitignored `cache/`. The two committed data files store titles, headings, and stemmed word *counts* only — never sentences, previews, positions, or n-grams. If you ever see documentation prose staged for commit, stop.

## Project philosophy

**Plugin-first, zero user dependencies.**

- All user-facing features ship via the Claude Code plugin (skills, commands, hooks).
- The client layer is **bash + curl + jq** — no Python on user machines.
- Python under `scripts/` is **CI-only** (discover pages, fetch + hash into scratch, build the manifest and index). It runs in GitHub Actions and is never installed with the plugin.
- Single install path: the plugin marketplace. The plugin slug `claude-docs` must not change.

## Getting started

**Prerequisites**

- Git, Bash
- For the CI Python scripts: Python 3.10+ and [`uv`](https://github.com/astral-sh/uv)

**Clone**

```bash
git clone https://github.com/costiash/claude-code-docs.git
cd claude-code-docs
```

## Development workflows

### Plugin skills (bash — the user-facing layer)

The search scripts read the committed `search_index.json` / `paths_manifest.json` and the local `cache/`. Populate a throwaway cache to test against real pages:

```bash
# Fetch a few pages into an isolated cache (no Python required)
CLAUDE_DOCS_CACHE_DIR=/tmp/ccd-cache ./plugin/scripts/fetch-docs.sh sync

# Search the prose-free index
./plugin/skills/claude-docs/scripts/content-search.sh hooks matcher
./plugin/skills/claude-docs/scripts/fuzzy-search.sh agent sdk python

# Validate that manifest URLs are reachable (quick sample)
./plugin/skills/claude-docs-validate/scripts/validate-paths.sh --quick

# Lint every shell script (must be clean at this severity)
uv run shellcheck --severity=warning plugin/scripts/*.sh plugin/skills/*/scripts/*.sh plugin/hooks/*.sh
```

**Files to work on:**

- `plugin/skills/docs/SKILL.md` — the `/docs` router skill (manual-only, `disable-model-invocation`)
- `plugin/skills/claude-docs/` — search skill + `content-search.sh` / `fuzzy-search.sh`
- `plugin/skills/claude-docs-validate/` — health / freshness checks
- `plugin/skills/claude-docs-course/`, `plugin/skills/claude-docs-changelog/` — self-contained HTML generators
- `plugin/scripts/fetch-docs.sh` — cache `sync` / `get` / `status` / `prune`
- `plugin/scripts/manifest-diff.sh` — git-history manifest diff (what's-new / changelog)
- `plugin/hooks/` — SessionStart auto-sync

### CI/CD scripts (Python — runs in GitHub Actions only)

```bash
# Install dev dependencies
uv sync --group dev

# Run the test suite (network tests excluded)
uv run pytest tests/ -q -m "not network"

# Regenerate metadata locally: fetch into the gitignored .doc_fetch/ scratch, then build the index
DOCS_FETCH_LIMIT=8 python3 scripts/fetch_claude_docs.py   # fast preview
python3 scripts/build_search_index.py                     # build search_index.json from scratch
```

**Files to work on:**

- `scripts/fetch_claude_docs.py` — fetcher entry point (thin wrapper)
- `scripts/fetcher/` — discovery (`llms_txt`, `sitemap`, `discovery`), fetch + hash (`content`, `paths`), `manifest`, `safeguards`, `config`, `cli`
- `scripts/build_search_index.py` — the prose-free index builder
- `tests/` — the pytest suite (CI-only)

## Code standards

### Shell scripts

- `set -euo pipefail` (or `set -uo pipefail` where a `trap` handles broken pipes, as the client scripts do)
- Sanitize all user input (alphanumeric + safe characters only)
- UPPERCASE for environment variables; comment non-obvious logic
- Must pass `shellcheck --severity=warning`
- Portable across macOS and Linux

### Python (CI scripts)

- Python 3.10+, type hints on function signatures, Google-style docstrings
- PEP 8, max line length 100

## Filename conventions

Cache filenames follow the manifest's flattened convention. URLs are stored **verbatim** in the manifest — never reconstruct a URL from a filename.

| Source URL | Filename |
|------------|----------|
| `code.claude.com/docs/en/hooks` | `claude-code__hooks.md` |
| `platform.claude.com/docs/en/agent-sdk/python` | `docs__en__agent-sdk__python.md` |

- `id` = filename without `.md`, with `__` → `/`.
- Code pages use the full sub-path so nested pages don't collide with top-level ones.

## Testing requirements

- All new Python code needs unit tests; keep the suite green with `uv run pytest tests/ -q -m "not network"`.
- Shell scripts are tested via a mocked-curl harness under `tests/unit/` (see `test_fetch_docs_sh.py`) — no live network in unit tests.
- The stemming rule in `build_search_index.py` (Python) and `content-search.sh` (jq) must stay **identical**; `tests/unit/test_stem_parity.py` enforces it.

## Pull requests

Use [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `test:`). Before opening a PR:

- [ ] `uv run pytest tests/ -q -m "not network"` is green
- [ ] `shellcheck --severity=warning` is clean (if you touched shell)
- [ ] No documentation prose is staged (the invariant above)
- [ ] Relevant docs updated (`README.md`, `CLAUDE.md`, `ARCHITECTURE.md`)

## Getting help

- Issues & discussions: <https://github.com/costiash/claude-code-docs>

## Code of Conduct

Be respectful and inclusive, welcome newcomers, accept constructive criticism gracefully, and focus on what's best for the project. Harassment, trolling, personal attacks, and publishing others' private information are not tolerated. Report concerns to the maintainers via GitHub Issues.

## License

By contributing, you agree to license your contributions under the MIT License (see [LICENSE](./LICENSE)). The MIT license covers the tool code and the generated metadata only — it grants no rights in Anthropic's documentation, which remains © Anthropic PBC and is fetched at runtime by the end user.
