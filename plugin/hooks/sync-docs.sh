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
# Overridable for offline tests (file:// fixture origin); real installs never set it.
REPO_URL="${CLAUDE_DOCS_REPO_URL:-https://github.com/costiash/claude-code-docs.git}"
FETCH="$DOCS_DIR/plugin/scripts/fetch-docs.sh"
MANIFEST="$DOCS_DIR/paths_manifest.json"

# Total time budget for this hook (seconds). hooks.json kills us at 45s; keep a
# margin so we always exit cleanly on our own terms instead of mid-operation.
# Bash's SECONDS counts wall-clock since shell start, so `remaining` shrinks as
# operations run — later steps get whatever the earlier ones left over, and the
# worst-case chain (fetch + reset + self-heal clone) can no longer exceed the
# harness timeout. Overridable only for tests.
HOOK_BUDGET="${CLAUDE_DOCS_HOOK_BUDGET:-40}"

# Seconds left in the budget, never below 1 (a 0 would mean "no timeout" to
# timeout(1) and "sleep forever" to the watchdog fallback).
remaining() {
    local left=$((HOOK_BUDGET - SECONDS))
    [ "$left" -lt 1 ] && left=1
    echo "$left"
}

# Cap: min(preferred, remaining budget).
cap() {
    local want="$1" left
    left=$(remaining)
    [ "$want" -lt "$left" ] && echo "$want" || echo "$left"
}

run_with_timeout() {
    local secs="$1"; shift
    if command -v timeout >/dev/null 2>&1; then
        timeout "$secs" "$@"
        return $?
    fi
    # Stock macOS has no timeout(1) — previously this branch ran UNBOUNDED and
    # the harness SIGKILL could land mid-clone/mid-swap. Portable watchdog:
    # run the command in the background, kill it when the clock runs out.
    # (The watchdog's sleep may linger up to $secs after an early kill; it is
    # detached and harmless — the hook has exited long before.)
    "$@" &
    local cmd_pid=$!
    ( sleep "$secs"; kill "$cmd_pid" 2>/dev/null ) &
    local wd_pid=$!
    wait "$cmd_pid" 2>/dev/null
    local rc=$?
    kill "$wd_pid" 2>/dev/null
    return $rc
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

# Reap orphaned swap dirs (.new.<pid>/.old.<pid>) left by a previous session
# that was killed mid-self-heal. Only dirs whose owning PID is dead are touched
# (a concurrent session's live swap is left alone). Before deleting, rescue any
# user data the orphan carried — a kill between the carry and the swap parks
# cache/ and courses/ inside the temp dir, and courses/ is irreplaceable.
prune_swap_orphans() {
    [ -d "$DOCS_DIR" ] || return 0
    local d pid sub
    for d in "$DOCS_DIR".new.* "$DOCS_DIR".old.*; do
        [ -e "$d" ] || continue
        pid="${d##*.}"
        case "$pid" in
            ''|*[!0-9]*) : ;;                          # no numeric suffix: treat as dead
            *) kill -0 "$pid" 2>/dev/null && continue  # owner alive: skip
        esac
        for sub in cache courses; do
            if [ -d "$d/$sub" ] && [ ! -e "$DOCS_DIR/$sub" ]; then
                mv "$d/$sub" "$DOCS_DIR/$sub" 2>/dev/null || true
            fi
        done
        rm -rf "$d"
    done
}

# First run: shallow-clone the tiny metadata repo, then bulk-fetch in background.
if [ ! -d "$DOCS_DIR" ]; then
    if run_with_timeout "$(cap 30)" git clone --depth 1 "$REPO_URL" "$DOCS_DIR" >/dev/null 2>&1; then
        prune_swap_orphans
        maybe_background_sync
        output_context "Claude documentation installed ($(doc_count) pages indexed). Pages download to the local cache in the background; /docs works immediately (missing pages fetch on demand)."
    else
        output_context "Failed to clone Claude documentation. Run: git clone $REPO_URL $DOCS_DIR"
    fi
    exit 0
fi

prune_swap_orphans

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
    run_with_timeout "$(cap 10)" git fetch origin main >/dev/null 2>&1 || true
    run_with_timeout "$(cap 10)" git reset --hard origin/main >/dev/null 2>&1 || true
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
    OLD_DIR="$DOCS_DIR.old.$$"
    rm -rf "$NEW_DIR" "$OLD_DIR"
    if run_with_timeout "$(cap 30)" git clone --depth 1 "$REPO_URL" "$NEW_DIR" >/dev/null 2>&1 \
        && [ -f "$NEW_DIR/paths_manifest.json" ]; then
        # Carry the untracked user data into the replacement before the swap:
        # cache/ (all fetched pages — re-downloadable but expensive) and
        # courses/ (user-generated HTML — irreplaceable). If a kill lands
        # after this point, prune_swap_orphans rescues them from the temp dir
        # on the next session.
        for d in cache courses; do
            if [ -d "$DOCS_DIR/$d" ]; then
                mv "$DOCS_DIR/$d" "$NEW_DIR/$d" 2>/dev/null || true
            fi
        done
        cd / || true  # leave the directory we are about to move aside
        # Rename-swap instead of rm-then-mv: both renames are atomic sibling
        # moves, so there is no window where a kill deletes the install — the
        # worst interruption leaves DOCS_DIR absent with the data parked in
        # .old.<pid>/.new.<pid>, which the next session re-clones + rescues.
        # It also sidesteps the old failure mode where a partially-failed
        # rm -rf left survivors and mv nested the fresh clone inside them.
        if ! mv "$DOCS_DIR" "$OLD_DIR" 2>/dev/null; then
            # Could not move the corrupt dir aside (exotic: FS error, busy).
            # Give the carried user data back and keep NEW_DIR only if the
            # restore itself failed.
            RESTORE_OK=1
            for d in cache courses; do
                if [ -d "$NEW_DIR/$d" ]; then
                    mv "$NEW_DIR/$d" "$DOCS_DIR/$d" 2>/dev/null || RESTORE_OK=0
                fi
            done
            if [ "$RESTORE_OK" = "1" ]; then
                rm -rf "$NEW_DIR"
            fi
            output_context "Claude docs installation looks corrupted and could not be replaced ($DOCS_DIR resists being moved aside). Run: rm -rf $DOCS_DIR and restart Claude Code to reinstall."
            exit 0
        fi
        mv "$NEW_DIR" "$DOCS_DIR"
        # Best-effort cleanup of the corrupt old dir; a failure (root-owned
        # file, immutable flag) just leaves a dead-PID orphan for the next
        # session's prune_swap_orphans.
        rm -rf "$OLD_DIR" 2>/dev/null || true
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
