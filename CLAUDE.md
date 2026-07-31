# Claude Code Documentation Index

This repository indexes Claude documentation from two Anthropic sources but **commits no
documentation prose** — only metadata. End users fetch the actual `.md` pages from
Anthropic's servers at runtime into a local cache.

- **Platform docs**: https://platform.claude.com (API, guides, Agent SDK, etc.)
- **Claude Code docs**: https://code.claude.com/docs (CLI-specific documentation)

The metadata (`paths_manifest.json` + `search_index.json`) is regenerated via GitHub
Actions every 3 hours with safeguards against catastrophic manifest changes.

> **Read `ARCHITECTURE.md` first** for the full v2 design: manifest schema, index schema,
> fetch pipeline, safeguard thresholds, filename conventions, cache layout, and the
> no-committed-content invariant.

## Delivery: the `/docs` skill and its sibling skills

Documentation ships as a Claude Code plugin rooted at `plugin/` (the `source` in
`.claude-plugin/marketplace.json`). `plugin/skills/docs/SKILL.md` is a lean router
(manual-only via `disable-model-invocation`, so it fires only on an explicit `/docs`;
auto-discovery is the `claude-docs` skill's job) that delegates to:

- **`claude-docs`** — all lookups, questions, and searches. Search strategy, synthesis
  rules, and URL generation live in its `SKILL.md`; the category-to-label mapping lives in
  its `manifest-reference.md` (single source of truth). Search intelligence belongs there,
  not in this file.
- **`claude-docs-validate`** — freshness checks (`-t`) and health validation
- **`claude-docs-course`** — interactive course generation (`--course <topic>`)
- **`claude-docs-changelog`** — HTML changelog reports (`--report`)
- **inline git log** — "what's new" queries

A SessionStart hook keeps the metadata current via `git reset --hard origin/main`.

## Repo-only vs shipped

Only `plugin/` ships. `scripts/` (Python, executed in GitHub Actions) is **not**
user-facing and is **not** installed with the plugin. `.doc_fetch/` is ephemeral CI fetch
scratch and `docs/` is legacy scratch — both are gitignored and must never be committed.
Keeping fetched prose out of the repo is the entire point of the v2 design.

## Documentation deletion safeguards

These exist because of a real incident: broken sitemap URLs once deleted 80%+ of the
documentation in a single sync. Thresholds live in `scripts/fetcher/config.py`, the checks
in `scripts/fetcher/safeguards.py`, and `ARCHITECTURE.md` documents both. The design
intent behind them:

- Discovery aborts before anything is written if too few pages are found — a failing
  discovery source must never read as "these pages are gone".
- A manifest transition that removes too large a share of entries, or that leaves too few
  behind, aborts rather than committing the loss. The guard is first-run-safe: no v2
  predecessor means a clean start, not a violation.
- **Carry-forward**: a page that fails to fetch stays in the manifest marked
  `fetch_status: stale`. A transient error never drops a page.
- `update-docs.yml` repeats the minimum-file-count floor as a jq check before committing,
  so the workflow fails closed even if the Python guard is bypassed.

Discovery is the **union** of two `llms.txt` files and two sitemaps, keyed by canonical
URL — llms.txt supplies titles and coverage, sitemaps supply `lastmod`. The four URLs are
listed with rationale in `scripts/fetcher/config.py`.

## Working on this repository

```bash
# CI script dependencies (uses uv)
uv sync --group dev

# Regenerate metadata locally — fetches into gitignored .doc_fetch/, then builds the index
DOCS_FETCH_LIMIT=8 python3 scripts/fetch_claude_docs.py   # fast preview (.preview manifest in scratch)
python3 scripts/fetch_claude_docs.py                      # full run, ~10 min, writes paths_manifest.json
python3 scripts/build_search_index.py                     # build search_index.json from scratch

# Client search scripts resolve the manifest/index from the repo root — run them in place
./plugin/skills/claude-docs/scripts/content-search.sh hooks matcher
./plugin/skills/claude-docs/scripts/fuzzy-search.sh agent sdk python
./plugin/skills/claude-docs-validate/scripts/validate-paths.sh --quick

pytest tests/ -q -m "not network"
```
