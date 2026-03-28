#!/usr/bin/env bash
set -uo pipefail
trap '' PIPE

# content-search.sh — Full-text keyword search across Claude documentation
# Usage: content-search.sh <keyword> [keyword2] [keyword3] ...
# Searches .search_index.json if available, falls back to grep.
# Output: matching filenames with match counts, sorted by relevance (descending).

DOCS_DIR="${DOCS_DIR:-${HOME}/.claude-code-docs/docs}"
INDEX_FILE="${DOCS_DIR}/.search_index.json"

if [ $# -eq 0 ]; then
    echo "Usage: content-search.sh <keyword> [keyword2 ...]" >&2
    exit 1
fi

# Sanitize keywords: lowercase, alphanumeric + hyphens only
keywords=()
for arg in "$@"; do
    clean=$(echo "$arg" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 -]//g' | xargs)
    [ -n "$clean" ] && keywords+=("$clean")
done

if [ ${#keywords[@]} -eq 0 ]; then
    echo "No valid keywords provided" >&2
    exit 1
fi

if [ ! -d "$DOCS_DIR" ]; then
    echo "Documentation directory not found: $DOCS_DIR" >&2
    echo "Install docs: /plugin marketplace add costiash/claude-code-docs" >&2
    exit 1
fi

# Strategy 1: Use search index if available and jq is installed
if [ -f "$INDEX_FILE" ] && command -v jq >/dev/null 2>&1; then
    jq_filter='.index | to_entries[] | {file: .value.file_path, title: .value.title, kw: .value.keywords, preview: .value.content_preview} |'

    count_parts=()
    for kw in "${keywords[@]}"; do
        escaped=$(echo "$kw" | sed 's/\\/\\\\/g; s/"/\\"/g')
        count_parts+=("(if (.kw | map(select(contains(\"${escaped}\"))) | length > 0) or (.title | ascii_downcase | contains(\"${escaped}\")) or (.file | ascii_downcase | contains(\"${escaped}\")) or (.preview | ascii_downcase | contains(\"${escaped}\")) then 1 else 0 end)")
    done

    count_expr=$(IFS='+'; echo "${count_parts[*]}")

    results=$(jq -r "${jq_filter} (.file) + \"\t\" + (${count_expr} | tostring)" "$INDEX_FILE" 2>/dev/null \
        | awk -F'\t' '$2 > 0' \
        | sort -t$'\t' -k2 -rn \
        | head -20)

    if [ -n "$results" ]; then
        echo "$results"
        exit 0
    fi
fi

# Strategy 2: Fallback to grep

declare -A file_scores 2>/dev/null || {
    # Bash 3 (macOS default) doesn't support associative arrays — use temp file
    score_file=$(mktemp)
    trap 'rm -f "$score_file"' EXIT

    for kw in "${keywords[@]}"; do
        grep -rli "$kw" "$DOCS_DIR"/*.md 2>/dev/null || true
    done | sort | uniq -c | sort -rn | head -20 \
        | while read -r count filepath; do
            echo -e "$(basename "$filepath")\t$count"
        done > "$score_file"

    cat "$score_file"
    exit 0
}

# Bash 4+ path with associative arrays
for kw in "${keywords[@]}"; do
    while IFS= read -r filepath; do
        fname=$(basename "$filepath")
        file_scores["$fname"]=$(( ${file_scores["$fname"]:-0} + 1 ))
    done < <(grep -rli "$kw" "$DOCS_DIR"/*.md 2>/dev/null || true)
done

for fname in "${!file_scores[@]}"; do
    echo -e "${fname}\t${file_scores[$fname]}"
done | sort -t$'\t' -k2 -rn | head -20

exit 0
