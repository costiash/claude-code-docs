# Architecture

This repository is a **manifest + client-side fetch** system, not a documentation
mirror. It commits only metadata; end users fetch the actual documentation pages
from Anthropic's servers at runtime.

## The invariant (read this first)

**No Anthropic documentation prose is ever committed to this repository — not at
the tip, not in history.** CI fetches pages only to hash them and build a lossy
index, into a gitignored scratch dir that is never committed. Contributors must
never `git add` fetched `.md` content. The two committed data files
(`paths_manifest.json`, `search_index.json`) are designed to be non-reconstructable:
the index stores titles, headings, and a capped bag of stemmed word *counts* — never
sentences, previews, positions, or n-grams.

## Data flow

```
                 CI (every 3h)                          Client (per session)
  ┌─────────────────────────────────────┐   ┌────────────────────────────────────┐
  llms.txt ∪ sitemaps                        git reset --hard origin/main
        │ discover (union by canonical URL)         │ (tiny metadata clone)
        ▼                                            ▼
  fetch .md verbatim → .doc_fetch/ (gitignored)   fetch-docs.sh sync
        │ sha256                                     │ jq-diff manifest sha256 vs sidecars
        ▼                                            ▼
  paths_manifest.json  ──────────committed────────▶ fetch changed pages → cache/
  search_index.json    ──────────committed────────▶ read from cache/ (get on miss)
```

## Committed data

### `paths_manifest.json` (schema v2 — single source of truth)

```json
{ "schema_version": 2, "generated_at": "...", "sources": ["<llms.txt + sitemap urls>"],
  "pages": [ { "id": "claude-code/hooks", "filename": "claude-code__hooks.md",
    "url": "https://code.claude.com/docs/en/hooks",
    "md_url": "https://code.claude.com/docs/en/hooks.md",
    "title": "Hooks", "category": "claude_code",
    "sha256": "<hash of the fetched .md>", "lastmod": "...", "fetch_status": "ok" } ] }
```

- **URLs are stored verbatim from discovery** — never reconstructed from a base URL.
  This structurally prevents the class of bug where a page's host is guessed wrong
  (e.g. agent-sdk pages live on `code.claude.com`, not `platform.claude.com`).
- `sha256` is the hash of the fetched page. It is the client's change-detector and
  integrity check: the client re-fetches and must get the same hash.
- `fetch_status`: `ok` | `stale` (fetch failed, previous entry carried forward) |
  `failed` (never successfully fetched). Entries leave the manifest only when
  *discovery* drops them, never on a transient fetch error.
- `lastmod` is present only for `code.claude.com` pages (platform's sitemap omits it);
  it is decorative. **Change detection keys off `sha256`, never `lastmod`.**
- `changelog.md` is a special entry: `md_url` is the raw GitHub CHANGELOG, `lastmod`
  is null, and it is fetched/stored verbatim (no header injection) so client and CI
  hashes match.

### `search_index.json` (schema v2 — lossy, prose-free)

Per page: `{ filename, id, title, category, url, headings:[{text, level}],
terms:{stem: freq, cap ~50}, word_count }`.

**Forbidden fields** (would allow prose reconstruction): `content_preview`, sentence
fragments, token positions, n-grams, absolute file paths. Heading anchors are *not*
stored — a consumer recomputes `slugify(text)` on demand.

## Filenames & categories

- `code.claude.com/docs/en/<sub/path>` → `claude-code__<sub__path>.md` (full sub-path,
  so nested pages like `agent-sdk/overview` don't collide with top-level `overview`).
- `platform.claude.com/docs/en/<path>` → `docs__en__<path>.md`.
- `id` = filename without `.md`, `__` → `/`.
- `category` is derived from host + path into the vocabulary in
  `plugin/skills/claude-docs/manifest-reference.md` (the skills' source of truth).

## Safeguards (`scripts/fetcher/safeguards.py`, `config.py`)

| Constant | Value | Guard |
|---|---|---|
| `MIN_DISCOVERY_THRESHOLD` | 200 | abort if discovery finds fewer pages |
| `MAX_DELETION_PERCENT` | 10 | abort if a manifest transition drops >10% of entries |
| `MIN_EXPECTED_FILES` | 250 | abort if the new manifest has fewer pages |

`validate_manifest_transition(old, new)` is first-run-safe: no v2 predecessor counts
as a clean start, not a mass removal. `update-docs.yml` repeats the floor check in jq.

## CI pipeline (`scripts/`, Python, not shipped to users)

- `fetcher/` — `llms_txt.py` (parse) + `sitemap.py` (`discover_sitemap_entries`) →
  `discovery.py` (union) → `cli.py` (fetch to scratch, hash, carry-forward) →
  `manifest.py` (write v2). `config.py` holds URLs, domains, thresholds.
- `build_search_index.py` — reads the scratch dir + manifest, writes the v2 index.
  A floor guard refuses to build over an empty/tiny scratch.
- Scratch dir: `.doc_fetch/` (gitignored), or `$DOCS_SCRATCH_DIR`.

## Client fetch layer (`plugin/scripts/`, bash + curl + jq, zero Python)

- **`fetch-docs.sh`** — `sync` / `get` / `status` / `prune`. Cache at
  `${CLAUDE_DOCS_CACHE_DIR:-<clone>/cache}`. Per-page sidecar
  `cache/.meta/<filename>.json` records `{manifest_sha256, content_sha256,
  fetched_at, stale_manifest}` — "up to date" means *synced against the current
  manifest sha*, so a hash-mismatch (stale) page is fetched once and not re-fetched
  every run. Per-URL **domain allowlist** (`code.claude.com`, `platform.claude.com`,
  `raw.githubusercontent.com`); atomic tmp+mv writes; retry-once; `xargs -P 8`.
  Offline + cache miss → the canonical URL is printed to stderr for a WebFetch fallback.
  `sync` is single-flight per cache via a PID-owned lock at `cache/.sync.lock/`
  (owner PID in `pid`, mtime heartbeated per batch) — every caller is covered,
  hook or direct CLI. A held lock is reaped only on evidence: dead owner PID,
  a pidless lock older than a minute, or a 30-minute-idle mtime despite a
  "live" PID (recycled-PID backstop). Release is owner-checked, so a reaped
  and re-acquired lock is never removed by the previous owner.
- **`manifest-diff.sh`** — `--since 7d|24h|<date>` diffs committed manifest revisions →
  Added / Changed / Removed (Changed keyed off `sha256`). Powers the three
  git-history-dependent features: what's-new, freshness, and the changelog report.
- **`sync-docs.sh`** (SessionStart hook) — `git fetch + reset --hard origin/main`
  (absorbs the history rewrite, cleans old clones, preserves `cache/` + `courses/`),
  then a background `sync` if `status` reports pending work.

## Client layout

```
~/.claude-code-docs/            # tiny git clone (metadata + plugin, no prose)
├── paths_manifest.json
├── search_index.json
├── plugin/…
├── cache/                      # fetched .md pages (gitignored, not in the repo)
│   ├── .meta/<filename>.json   # per-page sync sidecars
│   └── .sync.lock/pid          # transient single-flight sync lock (owner PID)
└── courses/                    # generated HTML (untracked, survives resets)
```

## Contributor rules

- Never commit documentation prose. `docs/` is gitignored; the fetch scratch is
  `.doc_fetch/`. If you see prose staged, stop.
- Keep the stemming rule identical in `build_search_index.py` (Python) and
  `content-search.sh` (jq) — `tests/unit/test_stem_parity.py` enforces it.
- URLs come from the manifest, never from filename reconstruction.
