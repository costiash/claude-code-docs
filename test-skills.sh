#!/usr/bin/env bash
set -euo pipefail

# test-skills.sh — Mechanical test harness for plugin skill quality
# Runs content-search and fuzzy-search with known queries, checks expected results.
# Output: PASS: <number> (total passed tests out of total)

DOCS_DIR="${DOCS_DIR:-$(cd "$(dirname "$0")" && pwd)/docs}"
SCRIPTS_DIR="$(cd "$(dirname "$0")" && pwd)/plugin/skills/claude-docs/scripts"

export DOCS_DIR

pass=0
fail=0
total=0

check() {
    local description="$1"
    local script="$2"
    shift 2
    local expected="$1"
    shift
    local args=("$@")

    total=$((total + 1))
    local output
    output=$("$SCRIPTS_DIR/$script" "${args[@]}" 2>/dev/null) || output=""

    if echo "$output" | grep -q "$expected"; then
        pass=$((pass + 1))
    else
        fail=$((fail + 1))
        echo "FAIL: $description — expected '$expected' in output" >&2
    fi
}

# === Content Search Tests ===
check "content: hooks"             content-search.sh claude-code__hooks.md          "hooks"
check "content: mcp"               content-search.sh claude-code__mcp.md            "mcp"
check "content: extended thinking"  content-search.sh docs__en__build-with-claude__extended-thinking.md "extended" "thinking"
check "content: streaming"         content-search.sh docs__en__build-with-claude__streaming.md         "streaming"
check "content: prompt caching"    content-search.sh docs__en__build-with-claude__prompt-caching.md    "prompt" "caching"
check "content: rate limits"       content-search.sh docs__en__api__rate-limits.md                     "rate" "limits"
check "content: agent sdk python"  content-search.sh docs__en__agent-sdk__python.md                    "agent" "sdk" "python"
check "content: vision"            content-search.sh docs__en__build-with-claude__vision.md            "vision"

# === Fuzzy Search Tests ===
check "fuzzy: hooks"       fuzzy-search.sh claude-code__hooks.md       "hooks"
check "fuzzy: mcp"         fuzzy-search.sh claude-code__mcp.md         "mcp"
check "fuzzy: plugins"     fuzzy-search.sh claude-code__plugins.md     "plugins"
check "fuzzy: agent sdk"   fuzzy-search.sh docs__en__agent-sdk         "agent sdk"
check "fuzzy: streaming"   fuzzy-search.sh streaming                   "streaming"
check "fuzzy: skills"      fuzzy-search.sh skills                      "skills"
check "fuzzy: vision"      fuzzy-search.sh vision                      "vision"

# === Edge Case Tests ===
check "content: computer use"      content-search.sh docs__en__agents-and-tools__tool-use__computer-use-tool.md  "computer"
check "content: batch processing"  content-search.sh docs__en__build-with-claude__batch-processing.md    "batch" "processing"
check "content: prompt engineering" content-search.sh docs__en__build-with-claude__prompt-engineering     "prompt" "engineering"
check "fuzzy: tool use overview"   fuzzy-search.sh   docs__en__agents-and-tools__tool-use__overview.md   "tool use overview"
check "fuzzy: batch"               fuzzy-search.sh   batch                                               "batch"

# === Robustness Tests ===
check "content: citations"         content-search.sh docs__en__build-with-claude__citations.md         "citations"
check "content: embeddings"        content-search.sh docs__en__build-with-claude__embeddings.md        "embeddings"
check "fuzzy: quickstart"          fuzzy-search.sh   claude-code__quickstart.md                        "quickstart"
check "fuzzy: settings"            fuzzy-search.sh   claude-code__settings.md                          "settings"
check "fuzzy: desktop"             fuzzy-search.sh   claude-code__desktop.md                           "desktop"

echo "PASS: $pass/$total"
echo "FAIL: $fail/$total"
