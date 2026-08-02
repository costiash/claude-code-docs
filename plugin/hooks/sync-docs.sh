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
    # Prefer jq (correct escaping for any content); fall back to manual escaping.
    if command -v jq >/dev/null 2>&1; then
        jq -n --arg msg "$msg" \
            '{hookSpecificOutput: {hookEventName: "SessionStart", additionalContext: $msg}}'
        return 0
    fi
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

# Kick off a background cache sync. We launch unconditionally rather than gating on a
# foreground `status` scan: status is O(pages) and a large cache blew the 5s timeout
# (exit 124, not 2), silently stranding pending updates. `sync` has its own cheap
# 0-fetch fast path, so an already-current cache just no-ops in the background.
# A lock dir prevents concurrent sessions from stacking parallel syncs; the worst
# case of losing the mkdir race is a skipped sync (the next session retries).
maybe_background_sync() {
    [ -x "$FETCH" ] || return 1
    local lock="$DOCS_DIR/.sync.lock"
    # Stale lock (a crashed sync never removed it): clear if older than ~30 minutes.
    if [ -d "$lock" ] && [ -n "$(find "$lock" -maxdepth 0 -mmin +30 2>/dev/null)" ]; then
        rmdir "$lock" 2>/dev/null || rm -rf "$lock" 2>/dev/null
    fi
    mkdir "$lock" 2>/dev/null || return 1  # another sync is running (or just won the race)
    # The child owns the lock and removes it when the fetch finishes, however it exits.
    nohup bash -c 'trap '\''rmdir "$2" 2>/dev/null'\'' EXIT; "$1" sync >/dev/null 2>&1' \
        sync-docs-lock "$FETCH" "$lock" >/dev/null 2>&1 &
    return 0
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

# The clone is healthy only if git resolves to THIS directory as its toplevel.
# A bare `rev-parse --git-dir` is satisfied by git's upward repo discovery: with
# ~/.claude-code-docs/.git lost but $HOME itself under version control (dotfiles
# repos), git would resolve to the ancestor repo — and the unscoped fetch/reset
# below would then hard-reset the USER'S repo. Compare physical paths (pwd -P)
# so a symlinked $HOME doesn't produce a false mismatch.
if [ "$(git rev-parse --show-toplevel 2>/dev/null)" = "$(pwd -P)" ]; then
    BEFORE=$(git rev-parse HEAD 2>/dev/null)
    # Hard-sync to origin/main: fast, survives history rewrites, cleans stale tracked files.
    # No --depth here: it would re-shallow a clone that manifest-diff.sh deepened for the
    # what's-new / changelog features (the first-run clone above stays shallow for speed).
    run_with_timeout 10 git fetch origin main >/dev/null 2>&1 || true
    run_with_timeout 10 git reset --hard origin/main >/dev/null 2>&1 || true
    AFTER=$(git rev-parse HEAD 2>/dev/null)
else
    BEFORE=""; AFTER=""
fi

# Self-heal: if the clone is corrupt (git absent, or resolving to an ancestor
# repo) or the manifest is still missing after the update attempt, every
# downstream feature is broken. Re-clone into a sibling temp dir and swap it
# in — the corrupt dir is removed ONLY after the fresh clone succeeded, so an
# offline session keeps whatever it had.
if [ "$(git -C "$DOCS_DIR" rev-parse --show-toplevel 2>/dev/null)" != "$(pwd -P)" ] || [ ! -f "$MANIFEST" ]; then
    NEW_DIR="$DOCS_DIR.new.$$"
    rm -rf "$NEW_DIR"
    if run_with_timeout 30 git clone --depth 1 "$REPO_URL" "$NEW_DIR" >/dev/null 2>&1 \
        && [ -f "$NEW_DIR/paths_manifest.json" ]; then
        # Carry the untracked user data into the replacement before the swap:
        # cache/ (all fetched pages — re-downloadable but expensive) and
        # courses/ (user-generated HTML — irreplaceable).
        for d in cache courses; do
            if [ -d "$DOCS_DIR/$d" ]; then
                mv "$DOCS_DIR/$d" "$NEW_DIR/$d" 2>/dev/null || true
            fi
        done
        cd / || true  # leave the directory we are about to delete
        rm -rf "$DOCS_DIR"
        mv "$NEW_DIR" "$DOCS_DIR"
        cd "$DOCS_DIR" || { output_context "Claude docs directory missing. Re-run /docs -t to reinstall."; exit 0; }
        AFTER=$(git rev-parse HEAD 2>/dev/null)
    else
        rm -rf "$NEW_DIR"
        output_context "Claude docs installation looks corrupted and could not be repaired (offline?). Run: rm -rf $DOCS_DIR and restart Claude Code to reinstall."
        exit 0
    fi
fi

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
