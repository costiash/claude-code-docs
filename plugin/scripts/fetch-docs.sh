#!/usr/bin/env bash
# fetch-docs.sh — client-side documentation fetcher (v2).
#
# The repo commits only metadata (paths_manifest.json + search_index.json). This
# script fetches the actual .md pages directly from Anthropic's servers into a
# local cache, on demand or in bulk. No Python required — bash + curl + jq.
#
# Subcommands:
#   sync [--background]   Fetch every page whose cache copy is missing or whose
#                         sha256 differs from the manifest (parallel, retry-once).
#                         --background forks and returns immediately.
#   get <filename|id>     Fetch a single page on demand (used on cache miss).
#   status                Print cached / pending / stale counts.
#   prune                 Delete cached files no longer in the manifest.
#
# Layout (resolved relative to this script's clone, overridable by env):
#   manifest : $CLAUDE_DOCS_MANIFEST      (default <clone>/paths_manifest.json)
#   cache    : $CLAUDE_DOCS_CACHE_DIR     (default <clone>/cache)
#   sidecars : <cache>/.meta/<filename>.json  {manifest_sha256, content_sha256, fetched_at, stale_manifest}
#
# Cache filenames match the manifest's flattened convention (claude-code__hooks.md),
# so the search skills' globs work unchanged.

set -uo pipefail
trap '' PIPE

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
CLONE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SELF="$SCRIPT_DIR/fetch-docs.sh"

MANIFEST="${CLAUDE_DOCS_MANIFEST:-$CLONE_ROOT/paths_manifest.json}"
CACHE_DIR="${CLAUDE_DOCS_CACHE_DIR:-$CLONE_ROOT/cache}"
META_DIR="$CACHE_DIR/.meta"
PARALLEL="${CLAUDE_DOCS_PARALLEL:-8}"

# Only these hosts may be requested. Checked per-URL before every fetch.
ALLOWED_HOSTS="code.claude.com platform.claude.com raw.githubusercontent.com"

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

die() { echo "fetch-docs: $*" >&2; exit 1; }

have_jq() { command -v jq >/dev/null 2>&1; }

# Guard used by every subcommand: jq present, manifest exists, parses to a JSON
# object AND has a `.pages` array. A truncated/empty/whitespace/wrong-shape (e.g. a
# legacy v1 {categories,metadata}) manifest must fail loudly here, not read as
# "0 pages / up to date" downstream. NB: `jq -e .` is NOT enough — jq 1.6 exits 0 on
# empty/whitespace input; the type tests reject those (and the v1 shape) while still
# accepting an empty {"pages":[]}.
require_manifest() {
    have_jq || die "jq is required"
    [ -f "$MANIFEST" ] || die "manifest not found: $MANIFEST"
    [ "$(jq -r 'type' "$MANIFEST" 2>/dev/null)" = "object" ] || die "manifest is not a valid JSON object: $MANIFEST"
    [ "$(jq -r '.pages | type' "$MANIFEST" 2>/dev/null)" = "array" ] || die "manifest has no .pages array (wrong schema?): $MANIFEST"
}

url_host() { printf '%s' "$1" | sed -E 's#^https?://([^/]+).*#\1#'; }

host_allowed() {
    case " $ALLOWED_HOSTS " in
        *" $1 "*) return 0 ;;
        *) return 1 ;;
    esac
}

sha256_of() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    else
        shasum -a 256 "$1" | awk '{print $1}'
    fi
}

ensure_dirs() { mkdir -p "$CACHE_DIR" "$META_DIR"; }

# Fetch a URL to a file with one retry. Returns 0 on success.
fetch_url() {
    local url="$1" out="$2"
    curl -fsSL --max-time 30 -o "$out" "$url" 2>/dev/null && return 0
    sleep 1
    curl -fsSL --max-time 30 -o "$out" "$url" 2>/dev/null && return 0
    return 1
}

# Sidecar records the manifest sha we synced AGAINST (the target) separately from
# the content sha we actually got. "Up to date" means synced against the current
# manifest entry — so a hash-mismatch (stale) page is fetched once, flagged, and
# NOT re-fetched every run; it re-fetches only when the manifest entry changes.
write_sidecar() {
    local filename="$1" manifest_sha="$2" content_sha="$3" stale="$4"
    printf '{"manifest_sha256":"%s","content_sha256":"%s","fetched_at":"%s","stale_manifest":%s}\n' \
        "$manifest_sha" "$content_sha" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$stale" > "$META_DIR/$filename.json"
}

# needs_fetch <filename> <manifest_sha> — 0 (yes) if file missing or the sidecar
# was synced against a different manifest sha than the current one.
needs_fetch() {
    local file="$CACHE_DIR/$1" meta="$META_DIR/$1.json"
    [ -f "$file" ] || return 0
    [ -f "$meta" ] || return 0
    local have
    have=$(jq -r '.manifest_sha256 // ""' "$meta" 2>/dev/null)
    [ "$have" = "$2" ] && return 1 || return 0
}

# Core single-page fetch. Args: filename, md_url, expected_sha ("" or "null" to skip check).
fetch_one() {
    local filename="$1" md_url="$2" expected="$3"
    # https-only: reject any non-https scheme before touching the network (defense in depth beside the host allowlist)
    case "$md_url" in
        https://*) ;;
        *) echo "fetch-docs: refusing non-https URL for $filename" >&2; return 1 ;;
    esac
    local host; host=$(url_host "$md_url")
    if ! host_allowed "$host"; then
        echo "fetch-docs: refusing disallowed host '$host' for $filename" >&2
        return 1
    fi
    ensure_dirs
    local tmp="$CACHE_DIR/.tmp.$filename.$$"
    if ! fetch_url "$md_url" "$tmp"; then
        rm -f "$tmp"
        echo "fetch-docs: could not fetch $filename (offline?). Source: ${md_url}" >&2
        return 1
    fi
    local got stale=false
    got=$(sha256_of "$tmp")
    if [ -n "$expected" ] && [ "$expected" != "null" ] && [ "$got" != "$expected" ]; then
        stale=true  # committed manifest hash differs from the live page; accept anyway
    fi
    mv -f "$tmp" "$CACHE_DIR/$filename"
    write_sidecar "$filename" "$expected" "$got" "$stale"
    return 0
}

# Look up a page by filename OR id in the manifest -> "md_url<TAB>sha256".
lookup_page() {
    jq -r --arg k "$1" '
        .pages[] | select(.filename == $k or .id == $k)
        | [.md_url, (.sha256 // "null")] | @tsv' "$MANIFEST" 2>/dev/null | head -1
}

# --------------------------------------------------------------------------
# subcommands
# --------------------------------------------------------------------------

cmd_get() {
    [ -n "${1:-}" ] || die "usage: get <filename|id>"
    require_manifest
    local key="$1" row md_url sha filename
    row=$(lookup_page "$key")
    [ -n "$row" ] || die "no manifest entry for '$key'"
    md_url=$(printf '%s' "$row" | cut -f1)
    sha=$(printf '%s' "$row" | cut -f2)
    # If key was an id, resolve the filename for the cache path.
    filename=$(jq -r --arg k "$key" '.pages[] | select(.filename==$k or .id==$k) | .filename' "$MANIFEST" | head -1)
    fetch_one "$filename" "$md_url" "$sha"
}

cmd_sync() {
    local background=0
    [ "${1:-}" = "--background" ] && background=1
    require_manifest

    if [ "$background" = 1 ]; then
        nohup "$SELF" sync >/dev/null 2>&1 &
        echo "fetch-docs: background sync started (pid $!)"
        return 0
    fi

    ensure_dirs
    local pending; pending=$(mktemp)
    # Only pages with a real sha256 are syncable (failed pages have null).
    jq -r '.pages[] | select(.sha256 != null) | [.filename, .md_url, .sha256] | @tsv' "$MANIFEST" \
    | while IFS=$'\t' read -r filename md_url sha; do
        if needs_fetch "$filename" "$sha"; then
            printf '%s\t%s\t%s\n' "$filename" "$md_url" "$sha"
        fi
    done > "$pending"

    local count; count=$(wc -l < "$pending" | tr -d ' ')
    if [ "$count" -eq 0 ]; then
        rm -f "$pending"
        echo "fetch-docs: cache up to date (0 fetches)"
        return 0
    fi
    echo "fetch-docs: fetching $count page(s)..."

    # Parallel fetch: re-invoke self per line (line = filename\tmd_url\tsha).
    # retry-once lives inside fetch_one; a page that still fails is skipped.
    export -f fetch_one fetch_url write_sidecar url_host host_allowed sha256_of ensure_dirs 2>/dev/null || true
    export CACHE_DIR META_DIR ALLOWED_HOSTS
    xargs -P "$PARALLEL" -I{} "$SELF" __fetch_line "{}" < "$pending"

    # Recount what still needs fetching (i.e. failed) to report a success count and
    # to exit nonzero on a total failure — a silent 'sync complete' after 0 fetches
    # (e.g. offline) is otherwise indistinguishable from success to the hook.
    local still=0
    while IFS=$'\t' read -r filename _ sha; do
        needs_fetch "$filename" "$sha" && still=$((still + 1))
    done < "$pending"
    rm -f "$pending"

    local fetched=$((count - still))
    echo "fetch-docs: sync complete ($fetched/$count fetched)"
    if [ "$fetched" -eq 0 ]; then
        echo "fetch-docs: all $count fetch(es) failed (offline?)" >&2
        return 1
    fi
    return 0
}

# Internal: fetch one tab-separated line (used by xargs in sync).
cmd_fetch_line() {
    local line="$1"
    local filename md_url sha
    filename=$(printf '%s' "$line" | cut -f1)
    md_url=$(printf '%s' "$line" | cut -f2)
    sha=$(printf '%s' "$line" | cut -f3)
    fetch_one "$filename" "$md_url" "$sha" || true  # skip failures, don't abort the batch
}

cmd_status() {
    require_manifest
    local total syncable cached=0 pending=0 stale=0
    total=$(jq '.pages | length' "$MANIFEST")
    syncable=$(jq '[.pages[] | select(.sha256 != null)] | length' "$MANIFEST")

    while IFS=$'\t' read -r filename sha; do
        if needs_fetch "$filename" "$sha"; then
            pending=$((pending + 1))
        else
            cached=$((cached + 1))
        fi
    done < <(jq -r '.pages[] | select(.sha256 != null) | [.filename, .sha256] | @tsv' "$MANIFEST")

    if [ -d "$META_DIR" ]; then
        stale=$(grep -l '"stale_manifest":true' "$META_DIR"/*.json 2>/dev/null | wc -l | tr -d ' ')
    fi

    echo "manifest pages : $total"
    echo "syncable       : $syncable"
    echo "cached         : $cached"
    echo "pending        : $pending"
    echo "stale          : $stale"
    # Exit 2 signals "work pending" for the hook (0 = nothing to do).
    [ "$pending" -eq 0 ] || return 2
}

cmd_prune() {
    require_manifest
    [ -d "$CACHE_DIR" ] || { echo "fetch-docs: no cache to prune"; return 0; }
    local keep; keep=$(mktemp)
    jq -r '.pages[].filename' "$MANIFEST" | sort > "$keep"
    if [ ! -s "$keep" ]; then
        rm -f "$keep"
        die "manifest lists 0 pages — refusing to prune (would wipe the entire cache)"
    fi
    local removed=0
    for f in "$CACHE_DIR"/*.md; do
        [ -e "$f" ] || continue
        local base; base=$(basename "$f")
        if ! grep -qxF "$base" "$keep"; then
            rm -f "$f" "$META_DIR/$base.json"
            removed=$((removed + 1))
        fi
    done
    rm -f "$keep"
    echo "fetch-docs: pruned $removed file(s) not in manifest"
}

# --------------------------------------------------------------------------
# dispatch
# --------------------------------------------------------------------------

main() {
    local cmd="${1:-}"; shift || true
    case "$cmd" in
        sync)         cmd_sync "$@" ;;
        get)          cmd_get "$@" ;;
        status)       cmd_status "$@" ;;
        prune)        cmd_prune "$@" ;;
        __fetch_line) cmd_fetch_line "$@" ;;  # internal (xargs)
        ""|-h|--help)
            echo "usage: fetch-docs.sh {sync [--background]|get <filename|id>|status|prune}" ;;
        *) die "unknown subcommand: $cmd" ;;
    esac
}

main "$@"
