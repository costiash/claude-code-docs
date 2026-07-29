#!/usr/bin/env bash
# manifest-diff.sh — what changed in the docs, from the manifest's git history.
# Usage: manifest-diff.sh [--since 7d|24h|<git-date>] [--json]
#
# Compares the committed paths_manifest.json at the start of the window against
# the current one and reports Added / Changed / Removed pages.
#
# "Changed" is keyed off sha256 deltas between manifest revisions — NOT lastmod,
# because platform.claude.com pages carry no lastmod (76% of the corpus), so a
# lastmod-based diff would silently miss most content changes.
#
# Replaces the mirror-era `git log -- docs/` for the what's-new / changelog features.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
CLONE_ROOT="${CLAUDE_DOCS_CLONE:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
MANIFEST_REL="paths_manifest.json"

since="7d"
as_json=false
while [ $# -gt 0 ]; do
    case "$1" in
        --since) since="${2:-7d}"; shift 2 ;;
        --json)  as_json=true; shift ;;
        *)       since="$1"; shift ;;  # bare positional = since value
    esac
done

command -v jq >/dev/null 2>&1 || { echo "jq is required" >&2; exit 1; }
cd "$CLONE_ROOT" || { echo "clone root not found: $CLONE_ROOT" >&2; exit 1; }
[ -f "$MANIFEST_REL" ] || { echo "manifest not found: $CLONE_ROOT/$MANIFEST_REL" >&2; exit 1; }

# Translate 7d / 24h into a git date expression.
case "$since" in
    *d) git_since="${since%d} days ago" ;;
    *h) git_since="${since%h} hours ago" ;;
    *)  git_since="$since" ;;
esac

# Baseline = the manifest as of the newest commit BEFORE the window opened.
base_rev=$(git rev-list -1 --before="$git_since" HEAD -- "$MANIFEST_REL" 2>/dev/null || true)

# Write both manifests to temp files — they can be ~700KB, too large to pass on
# jq's command line (--argjson would overflow ARG_MAX). --slurpfile reads from files.
old_f=$(mktemp); new_f=$(mktemp)
trap 'rm -f "$old_f" "$new_f"' EXIT

if [ -n "$base_rev" ]; then
    git show "$base_rev:$MANIFEST_REL" > "$old_f" 2>/dev/null || echo '{"pages":[]}' > "$old_f"
else
    echo '{"pages":[]}' > "$old_f"  # window predates repo history -> everything is "added"
fi
cp "$MANIFEST_REL" "$new_f"

# .pages // [] tolerates a legacy v1 ({categories}) baseline -> treated as empty.
diff_json=$(jq -n --slurpfile old "$old_f" --slurpfile new "$new_f" '
    ($old[0].pages // [] | map({(.id): .}) | add // {}) as $o
    | ($new[0].pages // [] | map({(.id): .}) | add // {}) as $n
    | {
        added:   [ $n | to_entries[] | select($o[.key] == null) | .value ],
        removed: [ $o | to_entries[] | select($n[.key] == null) | .value ],
        changed: [ $n | to_entries[] | select(($o[.key] != null) and ($o[.key].sha256 != .value.sha256)) | .value ]
      }
')

if [ "$as_json" = true ]; then
    printf '%s\n' "$diff_json"
    exit 0
fi

section() {
    local key="$1" label="$2"
    local n; n=$(printf '%s' "$diff_json" | jq -r --arg k "$key" '.[$k] | length')
    echo "=== $label ($n) ==="
    printf '%s' "$diff_json" | jq -r --arg k "$key" \
        '.[$k] | sort_by(.category, .id)[] | "[\(.category)] \(.title // .id)\n    \(.url)"'
    echo ""
}

echo "Documentation changes since $since (baseline: ${base_rev:-<none>})"
echo ""
section added "Added"
section changed "Changed"
section removed "Removed"
