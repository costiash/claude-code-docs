#!/bin/bash
# Claude Code Docs — SessionStart sync hook (v2, manifest + client fetch).
#
# Keeps the tiny metadata clone (~/.claude-code-docs: manifest + index + plugin,
# no prose) current, then triggers a background fetch of any changed pages into
# the local cache. The clone update uses `git reset --hard origin/main` so it:
#   - absorbs the Phase-D history rewrite (non-fast-forward) without breaking,
#   - deletes stale tracked docs/*.md left over from old mirror-era clones,
#   - preserves untracked cache/ and courses/.

DOCS_DIR="$HOME/.claude-code-docs"
REPO_URL="https://github.com/costiash/claude-code-docs.git"
FETCH="$DOCS_DIR/plugin/scripts/fetch-docs.sh"
MANIFEST="$DOCS_DIR/paths_manifest.json"

run_with_timeout() {
    local secs="$1"; shift
    if command -v timeout >/dev/null 2>&1; then
        timeout "$secs" "$@"
    else
        "$@"
    fi
}

output_context() {
    local msg="$1"
    msg="${msg//\\/\\\\}"
    msg="${msg//\"/\\\"}"
    cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "$msg"
  }
}
EOF
}

doc_count() {
    if command -v jq >/dev/null 2>&1 && [ -f "$MANIFEST" ]; then
        jq '.pages | length' "$MANIFEST" 2>/dev/null || echo "?"
    else
        echo "?"
    fi
}

# Kick off a background cache sync if there is pending work (status exits 2).
maybe_background_sync() {
    [ -x "$FETCH" ] || return 0
    run_with_timeout 5 "$FETCH" status >/dev/null 2>&1
    if [ $? -eq 2 ]; then
        nohup "$FETCH" sync >/dev/null 2>&1 &
        return 0  # work started
    fi
    return 1      # nothing pending
}

# First run: shallow-clone the tiny metadata repo, then bulk-fetch in background.
if [ ! -d "$DOCS_DIR" ]; then
    if run_with_timeout 30 git clone --depth 1 "$REPO_URL" "$DOCS_DIR" >/dev/null 2>&1; then
        maybe_background_sync
        output_context "Claude documentation installed ($(doc_count) pages indexed). Pages download to the local cache in the background; /docs works immediately (missing pages fetch on demand)."
    else
        output_context "Failed to clone Claude documentation. Run: git clone $REPO_URL $DOCS_DIR"
    fi
    exit 0
fi

cd "$DOCS_DIR" || { output_context "Claude docs directory missing. Re-run /docs -t to reinstall."; exit 0; }

BEFORE=$(git rev-parse HEAD 2>/dev/null)
# Hard-sync to origin/main: fast, survives history rewrites, cleans stale tracked files.
run_with_timeout 10 git fetch --depth 1 origin main >/dev/null 2>&1 || true
run_with_timeout 10 git reset --hard origin/main >/dev/null 2>&1 || true
AFTER=$(git rev-parse HEAD 2>/dev/null)

if maybe_background_sync; then
    SYNC_NOTE=" Syncing changed pages to the cache in the background."
else
    SYNC_NOTE=""
fi

if [ "$BEFORE" != "$AFTER" ]; then
    output_context "Claude docs updated ($(doc_count) pages indexed).${SYNC_NOTE} Use /docs to search."
else
    output_context "Claude docs up-to-date ($(doc_count) pages indexed).${SYNC_NOTE} Use /docs to search."
fi

exit 0
