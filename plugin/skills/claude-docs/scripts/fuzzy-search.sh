#!/usr/bin/env bash
set -euo pipefail

# fuzzy-search.sh — Fuzzy filename matching for Claude documentation
# Usage: fuzzy-search.sh <query>
# Tokenizes query, matches against filenames in docs/, scores by match quality.
# Output: ranked list of filenames (top 10), one per line.

DOCS_DIR="${HOME}/.claude-code-docs/docs"

if [ $# -eq 0 ]; then
    echo "Usage: fuzzy-search.sh <query>" >&2
    exit 1
fi

query=$(echo "$*" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 -]//g' | xargs)

if [ -z "$query" ]; then
    echo "No valid query provided" >&2
    exit 1
fi

if [ ! -d "$DOCS_DIR" ]; then
    echo "Documentation directory not found: $DOCS_DIR" >&2
    exit 1
fi

read -ra tokens <<< "$query"

score_file=$(mktemp)
trap 'rm -f "$score_file"' EXIT

for filepath in "$DOCS_DIR"/*.md; do
    [ -f "$filepath" ] || continue
    fname=$(basename "$filepath" .md)
    fname_lower=$(echo "$fname" | tr '[:upper:]' '[:lower:]' | tr '_' ' ' | tr '-' ' ')

    score=0

    if echo "$fname_lower" | grep -q "$query"; then
        score=$((score + 100))
    fi

    matched_tokens=0
    for token in "${tokens[@]}"; do
        if echo "$fname_lower" | grep -q "$token"; then
            score=$((score + 10))
            matched_tokens=$((matched_tokens + 1))
        fi
    done

    if [ "$matched_tokens" -eq "${#tokens[@]}" ] && [ "${#tokens[@]}" -gt 1 ]; then
        score=$((score + 50))
    fi

    if [ "$score" -gt 0 ]; then
        echo -e "${score}\t${fname}.md" >> "$score_file"
    fi
done

sort -t$'\t' -k1 -rn "$score_file" | head -10 | cut -f2

exit 0
