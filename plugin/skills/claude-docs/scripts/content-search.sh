#!/usr/bin/env bash
# content-search.sh — full-text keyword search over the v2 search index.
# Usage: content-search.sh <keyword> [keyword2 ...]
#
# Scores each page (BM25-lite in jq): title x10 + filename-slug x10 + matched
# headings (capped 3) x3 + sqrt(stemmed-term freq) x2. Falls back to grep over
# the cache when the index or jq is unavailable. Uniform output on BOTH paths:
# filename<TAB>title<TAB>score, sorted by score descending (top 20).
#
# STEMMING must match scripts/build_search_index.py exactly (strip first of
# ing/ed/es/s if >=3 chars remain). See tests/unit/test_stem_parity.py.

set -uo pipefail
trap '' PIPE

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
CLONE_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
INDEX="${CLAUDE_DOCS_INDEX:-$CLONE_ROOT/search_index.json}"
CACHE_DIR="${CLAUDE_DOCS_CACHE_DIR:-${DOCS_DIR:-$CLONE_ROOT/cache}}"

if [ $# -eq 0 ]; then
    echo "Usage: content-search.sh <keyword> [keyword2 ...]" >&2
    exit 1
fi

# Sanitize keywords: lowercase, alphanumeric + hyphens only.
keywords=()
for arg in "$@"; do
    clean=$(printf '%s' "$arg" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 -]//g' | xargs)
    [ -n "$clean" ] && keywords+=("$clean")
done
if [ ${#keywords[@]} -eq 0 ]; then
    echo "No valid keywords provided" >&2
    exit 1
fi

# Strategy 1: v2 index + jq (BM25-lite scoring, stemming mirrored from Python).
if [ -f "$INDEX" ] && command -v jq >/dev/null 2>&1; then
    results=$(jq -r --args '
        def stem:
          ascii_downcase as $w
          | if   ($w|endswith("ing")) and (($w|length) >= 6) then $w[0:-3]
            elif ($w|endswith("ed"))  and (($w|length) >= 5) then $w[0:-2]
            elif ($w|endswith("es"))  and (($w|length) >= 5) then $w[0:-2]
            elif ($w|endswith("s"))   and (($w|length) >= 4) then $w[0:-1]
            else $w end;
        ($ARGS.positional | map(stem)) as $q
        | .pages[] | . as $p
        | ($p.filename | ascii_downcase | gsub("[_-]+"; " ")) as $fn
        | ( [ $q[] as $t
              | (if (($p.title // "")|ascii_downcase|contains($t)) then 10 else 0 end)
              + (if ($fn|contains($t)) then 10 else 0 end)
              + (([ $p.headings[]? | select(.text|ascii_downcase|contains($t)) ] | length | if . > 3 then 3 else . end) * 3)
              + ((($p.terms[$t] // 0) | sqrt) * 2)
            ] | add ) as $score
        | select($score > 0)
        | [$p.filename, ($p.title // ""), ($score|tostring)] | @tsv
    ' "${keywords[@]}" < "$INDEX" 2>/dev/null \
        | sort -t$'\t' -k3 -rn \
        | head -20)

    if [ -n "$results" ]; then
        printf '%s\n' "$results"
        exit 0
    fi
fi

# Strategy 2: grep fallback over the cache (uniform 3-column output, empty title).
if [ -d "$CACHE_DIR" ]; then
    tmp=$(mktemp); trap 'rm -f "$tmp"' EXIT
    for kw in "${keywords[@]}"; do
        grep -rli -- "$kw" "$CACHE_DIR"/*.md 2>/dev/null || true
    done | sort | uniq -c | sort -rn | head -20 \
        | while read -r count filepath; do
            printf '%s\t\t%s\n' "$(basename "$filepath")" "$count"
        done > "$tmp"
    cat "$tmp"
    exit 0
fi

echo "No search index or cache found (expected $INDEX or $CACHE_DIR)" >&2
echo "Run: fetch-docs.sh sync" >&2
exit 1
