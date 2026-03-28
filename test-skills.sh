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

# === Additional Search Coverage ===
check "content: sandboxing"        content-search.sh claude-code__sandboxing.md                        "sandboxing"
check "content: context windows"   content-search.sh docs__en__build-with-claude__context-windows.md   "context" "windows"
check "fuzzy: headless"            fuzzy-search.sh   claude-code__headless.md                          "headless"
check "fuzzy: tool use"            fuzzy-search.sh   docs__en__agents-and-tools__tool-use              "tool use"
check "fuzzy: hooks guide"        fuzzy-search.sh   claude-code__hooks-guide.md                       "hooks guide"
check "content: devcontainer"      content-search.sh claude-code__devcontainer.md                      "devcontainer"
check "content: jetbrains"         content-search.sh claude-code__jetbrains.md                         "jetbrains"

# === Synonym-Adjacent Tests ===
check "content: structured outputs" content-search.sh docs__en__build-with-claude__structured-outputs.md  "structured" "outputs"
check "content: github actions"    content-search.sh claude-code__github-actions.md                       "github" "actions"
check "fuzzy: sub-agents"          fuzzy-search.sh   claude-code__sub-agents.md                           "sub-agents"

# === SDK Disambiguation Tests ===
check "content: python sdk"        content-search.sh docs__en__api__sdks__python.md                    "python" "sdk"
check "fuzzy: typescript sdk"      fuzzy-search.sh   docs__en__api__sdks__typescript.md                "typescript sdk"
check "fuzzy: go sdk"              fuzzy-search.sh   docs__en__api__sdks__go.md                        "go sdk"

# === URL Conversion Tests (extracted from validate-paths.sh) ===
_filename_to_url() {
    local fname="$1"
    fname="${fname%.md}"
    if [[ "$fname" == claude-code__* ]]; then
        local page="${fname#claude-code__}"
        page=$(echo "$page" | sed 's/__/\//g')
        echo "https://code.claude.com/docs/en/${page}"
    elif [[ "$fname" == docs__en__* ]]; then
        local path="${fname#docs__en__}"
        path=$(echo "$path" | sed 's/__/\//g')
        echo "https://platform.claude.com/en/docs/${path}"
    else
        echo ""
    fi
}

check_url() {
    local desc="$1" input="$2" expected="$3"
    total=$((total + 1))
    local got
    got=$(_filename_to_url "$input")
    if [ "$got" = "$expected" ]; then
        pass=$((pass + 1))
    else
        fail=$((fail + 1))
        echo "FAIL: $desc — expected '$expected', got '$got'" >&2
    fi
}

check_url "url: claude-code simple"   "claude-code__hooks.md"               "https://code.claude.com/docs/en/hooks"
check_url "url: claude-code nested"   "claude-code__hooks-guide.md"         "https://code.claude.com/docs/en/hooks-guide"
check_url "url: platform simple"      "docs__en__api__overview.md"          "https://platform.claude.com/en/docs/api/overview"
check_url "url: platform deep"        "docs__en__api__messages__create.md"  "https://platform.claude.com/en/docs/api/messages/create"
check_url "url: agent sdk"            "docs__en__agent-sdk__python.md"      "https://platform.claude.com/en/docs/agent-sdk/python"

# === Additional Coverage ===
check "content: model config"      content-search.sh claude-code__model-config.md                      "model" "config"
check "fuzzy: security"            fuzzy-search.sh   claude-code__security.md                          "security"
check "fuzzy: network config"      fuzzy-search.sh   claude-code__network-config.md                    "network config"
check "content: pricing"           content-search.sh docs__en__about-claude__pricing.md                 "pricing"
check "fuzzy: troubleshooting"     fuzzy-search.sh   claude-code__troubleshooting.md                    "troubleshooting"
check "content: pdf support"       content-search.sh docs__en__build-with-claude__pdf-support.md        "pdf"
check "content: data residency"    content-search.sh docs__en__build-with-claude__data-residency.md     "residency"
check "content: glossary"          content-search.sh docs__en__about-claude__glossary.md                "glossary"
check "fuzzy: analytics"           fuzzy-search.sh   claude-code__analytics.md                          "analytics"
check "fuzzy: costs"               fuzzy-search.sh   claude-code__costs.md                              "costs"

echo "PASS: $pass/$total"
echo "FAIL: $fail/$total"
