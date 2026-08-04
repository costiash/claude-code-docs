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

# Single awk pass over the whole manifest. The old per-page shell loop forked
# grep up to ~10 times per page (~7,000 processes, ~17s per query); awk's
# index() gives the same fixed-substring semantics (the query is sanitized to
# [a-z0-9 -] above, so the old grep patterns had no live regex metacharacters)
# in one process. Scoring is unchanged: query in filename +100, space-normalized
# hyphen variant +90, query in title +80, per-token +15/+10 (>=6 chars scores
# 15), all-tokens bonus +50. (The old loop also scored a hyphenated variant of
# the query against the filename, but the filename haystack has every hyphen
# converted to a space, so that branch could never match — dropped, not ported.)
jq -r '.pages[] | [.filename, (.title // "")] | @tsv' "$MANIFEST" \
| awk -F'\t' -v query="$query" '
    BEGIN {
        ntok = split(query, tok, " ")
        qs = query; gsub(/-/, " ", qs)
    }
    $1 != "" {
        fname = $1
        title = tolower($2)
        base = fname; sub(/\.md$/, "", base)
        fl = tolower(base); gsub(/[_-]/, " ", fl)

        score = 0
        if (index(fl, query)) score += 100
        if (qs != query && index(fl, qs)) score += 90
        if (title != "" && index(title, query)) score += 80

        matched = 0
        for (i = 1; i <= ntok; i++) {
            t = tok[i]
            ts = t; gsub(/-/, " ", ts)
            if (index(fl, t) || index(fl, ts) || (title != "" && index(title, t))) {
                score += (length(t) >= 6 ? 15 : 10)
                matched++
            }
        }
        if (matched == ntok && ntok > 1) score += 50

        if (score > 0) printf "%d\t%s\n", score, fname
    }' \
| sort -t$'\t' -k1 -rn | head -10 | cut -f2
exit 0
