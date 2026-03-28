#!/usr/bin/env bash
set -euo pipefail

# validate-paths.sh — HTTP reachability checks for Claude documentation
# Usage: validate-paths.sh [--quick]
#   --quick: sample 20 random docs instead of all
# Output: summary + list of broken paths
# Exit: 0 if all reachable, 1 if any broken

DOCS_DIR="${HOME}/.claude-code-docs/docs"
QUICK_SAMPLE=20
MAX_PARALLEL=5
TIMEOUT=10

quick_mode=false
if [ "${1:-}" = "--quick" ]; then
    quick_mode=true
fi

if [ ! -d "$DOCS_DIR" ]; then
    echo "Documentation directory not found: $DOCS_DIR" >&2
    exit 1
fi

filename_to_url() {
    local fname="$1"
    fname="${fname%.md}"

    if [[ "$fname" == claude-code__* ]]; then
        local page="${fname#claude-code__}"
        page=$(echo "$page" | tr '__' '/')
        echo "https://code.claude.com/docs/en/${page}"
    elif [[ "$fname" == docs__en__* ]]; then
        local path="${fname#docs__en__}"
        path=$(echo "$path" | sed 's/__/\//g')
        echo "https://platform.claude.com/en/docs/${path}"
    else
        echo ""
    fi
}

mapfile -t all_files < <(find "$DOCS_DIR" -maxdepth 1 -name "*.md" -exec basename {} \; | sort)

if [ ${#all_files[@]} -eq 0 ]; then
    echo "No documentation files found" >&2
    exit 1
fi

if [ "$quick_mode" = true ]; then
    mapfile -t check_files < <(printf '%s\n' "${all_files[@]}" | shuf | head -n "$QUICK_SAMPLE")
    echo "Validating ${#check_files[@]} random docs (quick mode)..."
else
    check_files=("${all_files[@]}")
    echo "Validating all ${#check_files[@]} docs..."
fi

total=0
reachable=0
broken=0
timeout_count=0
skipped=0
broken_list=""

check_url() {
    local fname="$1"
    local url
    url=$(filename_to_url "$fname")

    if [ -z "$url" ]; then
        echo "SKIP $fname"
        return
    fi

    local status
    status=$(curl -sI --max-time "$TIMEOUT" -o /dev/null -w "%{http_code}" "$url" 2>/dev/null || echo "000")

    if [ "$status" = "200" ] || [ "$status" = "301" ] || [ "$status" = "302" ] || [ "$status" = "307" ] || [ "$status" = "308" ]; then
        echo "OK $fname"
    elif [ "$status" = "000" ]; then
        echo "TIMEOUT $fname $url"
    else
        echo "BROKEN $fname $status $url"
    fi
}

export -f filename_to_url check_url
export DOCS_DIR TIMEOUT

results=$(printf '%s\n' "${check_files[@]}" | xargs -P "$MAX_PARALLEL" -I{} bash -c 'check_url "$@"' _ {})

while IFS= read -r line; do
    case "$line" in
        OK*)
            total=$((total + 1))
            reachable=$((reachable + 1))
            ;;
        BROKEN*)
            total=$((total + 1))
            broken=$((broken + 1))
            broken_list="${broken_list}${line#BROKEN }\n"
            ;;
        TIMEOUT*)
            total=$((total + 1))
            timeout_count=$((timeout_count + 1))
            broken_list="${broken_list}${line#TIMEOUT } (timeout)\n"
            ;;
        SKIP*)
            skipped=$((skipped + 1))
            ;;
    esac
done <<< "$results"

echo ""
echo "=== Validation Summary ==="
echo "Total checked: $total"
echo "Reachable:     $reachable"
echo "Broken:        $broken"
echo "Timeout:       $timeout_count"
echo "Skipped:       $skipped"

if [ -n "$broken_list" ]; then
    echo ""
    echo "=== Broken Paths ==="
    echo -e "$broken_list"
fi

if [ "$broken" -gt 0 ] || [ "$timeout_count" -gt 0 ]; then
    exit 1
fi

exit 0
