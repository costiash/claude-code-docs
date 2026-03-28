#!/usr/bin/env bash
set -euo pipefail

# verify-skills.sh — Combined quality score for plugin skills
# Score = (search_pass_rate * 10) - shellcheck_warnings
# Output: single number (the score)

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

# 1. Run search test harness, extract pass rate
test_output=$("$REPO_DIR/test-skills.sh" 2>/dev/null)
pass_line=$(echo "$test_output" | grep "^PASS:")
pass_count=$(echo "$pass_line" | sed 's|PASS: \([0-9]*\)/.*|\1|')
total_count=$(echo "$pass_line" | sed 's|PASS: [0-9]*/\([0-9]*\)|\1|')

if [ "$total_count" -eq 0 ]; then
    echo "0"
    exit 1
fi

pass_rate=$(( (pass_count * 100) / total_count ))

# 2. Count shellcheck warnings/errors (info excluded)
sc_output=$(uv run shellcheck -S warning "$REPO_DIR"/plugin/skills/*/scripts/*.sh 2>&1 || true)
sc_count=$(echo "$sc_output" | grep -c "^In " || true)
sc_count=${sc_count:-0}

# 3. Combined score: (pass_rate_pct / 10) * 10 - warnings = pass_rate - warnings
score=$(( pass_rate - sc_count ))

echo "$score"
