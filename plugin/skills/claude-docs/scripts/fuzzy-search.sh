#!/usr/bin/env bash
# fuzzy-search.sh — fuzzy filename/title matching over the v2 manifest.
# Usage: fuzzy-search.sh <query>
#
# Reads filenames + titles from paths_manifest.json (not the cache), so it works
# before any page is fetched. Output: ranked filenames (top 10), one per line.

set -uo pipefail
trap '' PIPE

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
CLONE_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
MANIFEST="${CLAUDE_DOCS_MANIFEST:-$CLONE_ROOT/paths_manifest.json}"

if [ $# -eq 0 ]; then
    echo "Usage: fuzzy-search.sh <query>" >&2
    exit 1
fi

query=$(printf '%s' "$*" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 -]//g' | xargs)
[ -n "$query" ] || { echo "No valid query provided" >&2; exit 1; }
[ -f "$MANIFEST" ] || { echo "Manifest not found: $MANIFEST" >&2; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "jq is required" >&2; exit 1; }

read -ra tokens <<< "$query"
query_hyphen=$(printf '%s' "$query" | tr ' ' '-')
query_spaced=$(printf '%s' "$query" | tr '-' ' ')

score_file=$(mktemp)
trap 'rm -f "$score_file"' EXIT

while IFS=$'\t' read -r fname title; do
    [ -n "$fname" ] || continue
    base="${fname%.md}"
    fname_lower=$(printf '%s' "$base" | tr '[:upper:]' '[:lower:]' | tr '_-' '  ')
    title_lower=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]')

    score=0
    echo "$fname_lower" | grep -q -- "$query" && score=$((score + 100))
    [ "$query_hyphen" != "$query" ] && echo "$fname_lower" | grep -q -- "$query_hyphen" && score=$((score + 90))
    [ "$query_spaced" != "$query" ] && echo "$fname_lower" | grep -q -- "$query_spaced" && score=$((score + 90))
    [ -n "$title_lower" ] && printf '%s' "$title_lower" | grep -qF -- "$query" && score=$((score + 80))

    matched=0
    for token in "${tokens[@]}"; do
        token_spaced=$(printf '%s' "$token" | tr '-' ' ')
        if echo "$fname_lower" | grep -q -- "$token" \
           || echo "$fname_lower" | grep -q -- "$token_spaced" \
           || { [ -n "$title_lower" ] && printf '%s' "$title_lower" | grep -qF -- "$token"; }; then
            if [ "${#token}" -ge 6 ]; then score=$((score + 15)); else score=$((score + 10)); fi
            matched=$((matched + 1))
        fi
    done
    if [ "$matched" -eq "${#tokens[@]}" ] && [ "${#tokens[@]}" -gt 1 ]; then
        score=$((score + 50))
    fi

    [ "$score" -gt 0 ] && printf '%s\t%s\n' "$score" "$fname" >> "$score_file"
done < <(jq -r '.pages[] | [.filename, (.title // "")] | @tsv' "$MANIFEST")

sort -t$'\t' -k1 -rn "$score_file" | head -10 | cut -f2
exit 0
