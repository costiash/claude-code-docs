#!/usr/bin/env bash
# validate-paths.sh — HTTP reachability checks for the v2 manifest.
# Usage: validate-paths.sh [--quick]
#   --quick: sample 20 random pages instead of all.
# Reads md_urls directly from paths_manifest.json (no filename->URL derivation).
# Exit: 0 if all reachable, 1 if any broken/timeout.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
CLONE_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
MANIFEST="${CLAUDE_DOCS_MANIFEST:-$CLONE_ROOT/paths_manifest.json}"
QUICK_SAMPLE=20
MAX_PARALLEL=5
TIMEOUT=10

quick_mode=false
[ "${1:-}" = "--quick" ] && quick_mode=true

[ -f "$MANIFEST" ] || { echo "Manifest not found: $MANIFEST" >&2; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "jq is required" >&2; exit 1; }

# No mapfile: must run on stock macOS bash 3.2.
all_urls=()
while IFS= read -r u; do
    [ -n "$u" ] && all_urls+=("$u")
done < <(jq -r '.pages[].md_url | select(. != null)' "$MANIFEST")
[ ${#all_urls[@]} -gt 0 ] || { echo "No URLs in manifest" >&2; exit 1; }

if [ "$quick_mode" = true ]; then
    # Portable shuffle (no GNU shuf): random sort key via awk, strip it after sorting.
    check_urls=()
    while IFS= read -r u; do
        [ -n "$u" ] && check_urls+=("$u")
    done < <(printf '%s\n' "${all_urls[@]}" \
        | awk 'BEGIN{srand()}{printf "%.6f\t%s\n", rand(), $0}' \
        | sort -n | cut -f2- | head -n "$QUICK_SAMPLE")
    echo "Validating ${#check_urls[@]} random pages (quick mode)..."
else
    check_urls=("${all_urls[@]}")
    echo "Validating all ${#check_urls[@]} pages..."
fi

check_url() {
    local url="$1" status
    # No -L: the client fetcher (fetch-docs.sh) uses --max-redirs 0, so a URL that
    # answers with a redirect is unfetchable for it — report the redirect itself.
    status=$(curl -sI --proto '=https' --max-time "${TIMEOUT:-10}" -o /dev/null -w "%{http_code}" "$url" 2>/dev/null || echo "000")
    case "$status" in
        200) echo "OK $url" ;;
        301|308) echo "REDIRECT_PERM $status $url" ;;
        302|307) echo "REDIRECT $status $url" ;;
        000) echo "UNREACHABLE $url" ;;
        *) echo "BROKEN $status $url" ;;
    esac
}
export -f check_url
export TIMEOUT

results=$(printf '%s\n' "${check_urls[@]}" | xargs -P "$MAX_PARALLEL" -I{} bash -c 'check_url "$@"' _ {})

total=0; reachable=0; broken=0; timeout_count=0; redirected=0
broken_list=""; redirect_list=""
while IFS= read -r line; do
    case "$line" in
        OK*)            total=$((total+1)); reachable=$((reachable+1)) ;;
        # Permanent redirects are just as unfetchable under --max-redirs 0 as
        # temporary ones — count them broken; the separate list below only adds
        # the "URL likely moved, manifest should catch up" signal.
        REDIRECT_PERM*) total=$((total+1)); broken=$((broken+1)); redirected=$((redirected+1)); redirect_list="${redirect_list}${line#REDIRECT_PERM }\n" ;;
        REDIRECT*)      total=$((total+1)); broken=$((broken+1)); redirected=$((redirected+1)); broken_list="${broken_list}${line#REDIRECT } (redirect — client fetches with --max-redirs 0)\n" ;;
        BROKEN*)        total=$((total+1)); broken=$((broken+1)); broken_list="${broken_list}${line#BROKEN }\n" ;;
        UNREACHABLE*)   total=$((total+1)); timeout_count=$((timeout_count+1)); broken_list="${broken_list}${line#UNREACHABLE } (unreachable)\n" ;;
    esac
done <<< "$results"

echo ""
echo "=== Validation Summary ==="
echo "Total checked: $total"
echo "Reachable:     $reachable"
echo "Redirected:    $redirected (all counted broken: clients fetch with --max-redirs 0; permanent ones likely moved)"
echo "Broken:        $broken"
echo "Unreachable:   $timeout_count"

[ -n "$redirect_list" ] && { echo ""; echo "=== Permanent Redirects (broken for clients; URL likely moved) ==="; echo -e "$redirect_list"; }
[ -n "$broken_list" ] && { echo ""; echo "=== Broken Paths ==="; echo -e "$broken_list"; }

if [ "$broken" -gt 0 ] || [ "$timeout_count" -gt 0 ]; then
    exit 1
fi
exit 0
