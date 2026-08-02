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

# Rescue cache/ and courses/ from a swap dir into the install. Existing
# NON-EMPTY data in the install always wins (never overwritten); an EMPTY
# recreated dir (a background fetch's mkdir -p racing the swap) is cleared
# first so a fully-populated parked copy isn't discarded in favor of nothing.
# Returns 1 if any rescue mv actually failed — callers must then KEEP the
# source dir (deleting it would destroy the data the rescue just failed on).
rescue_user_data() {
    local src="$1" sub failed=0
    for sub in cache courses; do
        [ -d "$src/$sub" ] || continue
        rmdir "$DOCS_DIR/$sub" 2>/dev/null || true  # only removes an EMPTY dir
        [ -e "$DOCS_DIR/$sub" ] && continue         # real data present: keep it
        mv "$src/$sub" "$DOCS_DIR/$sub" 2>/dev/null || failed=1
    done
    return $failed
}

# Reap orphaned swap dirs (.new.<pid>/.old.<pid>) left by a session that was
# killed mid-self-heal, rescuing any parked cache/ + courses/ first. Touched
# only when the suffix is ALL-NUMERIC (a user's ~/.claude-code-docs.old.bak
# must never be eaten) AND the owner looks gone: PID dead, or — since kill -0
# can lie in both directions (recycled PID reads alive forever, another user's
# live PID reads EPERM=dead) — an age backstop: dirs older than ~60 minutes
# belong to no live session regardless of what kill -0 says. A failed rescue
# keeps the orphan for the next session instead of deleting the data with it.
prune_swap_orphans() {
    [ -d "$DOCS_DIR" ] || return 0
    local d pid
    for d in "$DOCS_DIR".new.* "$DOCS_DIR".old.*; do
        [ -e "$d" ] || continue
        pid="${d##*.}"
        case "$pid" in
            ''|*[!0-9]*) continue ;;  # non-numeric suffix: not ours — never touch
        esac
        if kill -0 "$pid" 2>/dev/null; then
            [ -n "$(find "$d" -maxdepth 0 -mmin +60 2>/dev/null)" ] || continue
        fi
        if rescue_user_data "$d"; then
            run_with_timeout "$(cap 10)" rm -rf "$d" >/dev/null 2>&1 || true
        fi
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
    # Inter-session heal lock (sibling of DOCS_DIR — the dir itself gets moved
    # during the swap). Two sessions healing the same corrupt clone could
    # otherwise leapfrog each other's swaps and rm -rf a freshly-healed
    # install, courses/ included. Same mkdir+staleness pattern as .sync.lock.
    HEAL_LOCK="$DOCS_DIR.heal.lock"
    if [ -d "$HEAL_LOCK" ] && [ -n "$(find "$HEAL_LOCK" -maxdepth 0 -mmin +30 2>/dev/null)" ]; then
        rmdir "$HEAL_LOCK" 2>/dev/null || rm -rf "$HEAL_LOCK" 2>/dev/null
    fi
    if ! mkdir "$HEAL_LOCK" 2>/dev/null; then
        output_context "Claude docs installation needs repair; another session is already repairing it. It will be ready on the next session start."
        exit 0
    fi
    trap 'rmdir "$HEAL_LOCK" 2>/dev/null' EXIT

    NEW_DIR="$DOCS_DIR.new.$$"
    OLD_DIR="$DOCS_DIR.old.$$"
    # Stale leftovers under OUR pid (recycled from a dead session — kill -0
    # necessarily called them alive, so prune skipped them): rescue any parked
    # user data before clearing, never blind-delete.
    for d in "$NEW_DIR" "$OLD_DIR"; do
        if [ -e "$d" ]; then
            rescue_user_data "$d" && rm -rf "$d" 2>/dev/null
        fi
    done

    # A clone squeezed into a near-exhausted budget is doomed and just churns
    # the network — defer the repair to the next session instead.
    if [ "$(remaining)" -lt 5 ]; then
        output_context "Claude docs installation needs repair but this session's time budget is exhausted (slow network?). Repair will be retried on the next session start."
        exit 0
    fi

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
            # Do NOT try to hand-restore here — leave NEW_DIR (which now holds
            # the carried user data) as a .new.<pid> orphan; this process is
            # about to exit, its PID dies, and the next session's prune
            # rescues with the guarded logic instead of a race-prone loop.
            output_context "Claude docs installation looks corrupted and could not be replaced ($DOCS_DIR resists being moved aside). Repair will be retried on the next session start; your courses/ and cache/ are preserved."
            exit 0
        fi
        # Anti-nesting guard: DOCS_DIR must still be absent. A concurrent
        # first-run clone or a background fetch's mkdir -p can recreate it
        # between the two renames — mv would then nest the fresh clone (and
        # the carried courses/) INSIDE it, exit 0, and a later heal would
        # rm -rf the lot. Defer instead: both temp dirs outlive this process
        # as dead-PID orphans and the next session rescues the data.
        if [ -e "$DOCS_DIR" ]; then
            output_context "Claude docs repair was interrupted by a concurrent session; it will finish on the next session start (your courses/ and cache/ are preserved)."
            exit 0
        fi
        mv "$NEW_DIR" "$DOCS_DIR" 2>/dev/null || {
            output_context "Claude docs repair could not complete; it will be retried on the next session start (your courses/ and cache/ are preserved)."
            exit 0
        }
        # Best-effort cleanup of the corrupt old dir (capped: a huge mirror-era
        # dir on slow disk must not eat the remaining budget); a failure just
        # leaves a dead-PID orphan for the next session's prune.
        run_with_timeout "$(cap 10)" rm -rf "$OLD_DIR" >/dev/null 2>&1 || true
        cd "$DOCS_DIR" || { output_context "Claude docs directory missing. Re-run /docs -t to reinstall."; exit 0; }
        AFTER=$(git rev-parse HEAD 2>/dev/null)
    else
        # Clone failed BEFORE any user data was carried — NEW_DIR holds at
        # most a partial clone, safe to delete blind. DOCS_DIR still contains
        # the user's courses/ and cache/: never advise deleting it.
        rm -rf "$NEW_DIR"
        output_context "Claude docs installation looks corrupted and could not be repaired (offline?). It will be retried on the next session start. Your courses/ and cache/ remain in $DOCS_DIR — do not delete it; to force a fresh install run: mv $DOCS_DIR $DOCS_DIR.bak"
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
