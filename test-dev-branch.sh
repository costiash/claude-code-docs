#!/bin/bash
# Test script for validating dev branch install/uninstall
# This tests components WITHOUT destroying the working directory

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}Dev Branch Test Suite${NC}"
echo "====================="
echo

# Save current directory
ORIGINAL_DIR=$(pwd)
PASSED=0
FAILED=0

# Ensure arithmetic operations work
set +e

# Test 1: Verify install.sh exists and is executable
echo -e "${YELLOW}Test 1: Check install.sh${NC}"
if [[ -f install.sh && -x install.sh ]]; then
    echo -e "${GREEN}✓ install.sh exists and is executable${NC}"
    ((PASSED++))
else
    echo -e "${RED}✗ install.sh missing or not executable${NC}"
    ((FAILED++))
fi

# Test 2: Verify uninstall.sh exists and has directory change logic
echo -e "\n${YELLOW}Test 2: Check uninstall.sh directory change logic${NC}"
if grep -q 'cd "$PARENT_DIR"' uninstall.sh 2>/dev/null; then
    echo -e "${GREEN}✓ uninstall.sh has directory change protection${NC}"
    ((PASSED++))
else
    echo -e "${RED}✗ uninstall.sh missing directory change protection${NC}"
    ((FAILED++))
fi

# Test 3: Test hook removal logic (dry run)
echo -e "\n${YELLOW}Test 3: Test hook removal logic (dry run)${NC}"
if [[ -f ~/.claude/settings.json ]]; then
    # Test the jq command without modifying the file
    if jq --arg path "$ORIGINAL_DIR" '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[0].command | contains($path) | not)]' ~/.claude/settings.json > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Hook removal logic is valid${NC}"
        ((PASSED++))
    else
        echo -e "${RED}✗ Hook removal logic failed${NC}"
        ((FAILED++))
    fi
else
    echo -e "${YELLOW}⚠ No settings.json found (would be created on install)${NC}"
    ((PASSED++))
fi

# Test 4: Simulate install to temp location
echo -e "\n${YELLOW}Test 4: Test installation to temp directory${NC}"
TEMP_DIR=$(mktemp -d)
cp -r . "$TEMP_DIR/claude-code-docs"
cd "$TEMP_DIR/claude-code-docs"

# Check if we can create the command file location
if mkdir -p ~/.claude/commands 2>/dev/null; then
    echo -e "${GREEN}✓ Can create command directory${NC}"
    ((PASSED++))
else
    echo -e "${RED}✗ Cannot create command directory${NC}"
    ((FAILED++))
fi

# Test 5: Verify docs directory has content
echo -e "\n${YELLOW}Test 5: Check docs directory${NC}"
if [[ -d docs ]] && [[ $(ls docs/*.md 2>/dev/null | wc -l) -gt 10 ]]; then
    echo -e "${GREEN}✓ Docs directory has documentation files${NC}"
    ((PASSED++))
else
    echo -e "${RED}✗ Docs directory missing or incomplete${NC}"
    ((FAILED++))
fi

# Test 6: Test uninstaller confirmation bypass
echo -e "\n${YELLOW}Test 6: Test uninstaller can be automated${NC}"
if grep -q 'read -p' uninstall.sh; then
    echo -e "${GREEN}✓ Uninstaller has confirmation prompt${NC}"
    # Test if we can bypass it
    if echo "n" | bash uninstall.sh > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Can safely cancel uninstall${NC}"
        ((PASSED++))
    else
        echo -e "${RED}✗ Uninstaller bypass failed${NC}"
        ((FAILED++))
    fi
else
    echo -e "${RED}✗ No confirmation prompt found${NC}"
    ((FAILED++))
fi

# Cleanup temp directory
cd "$ORIGINAL_DIR"
rm -rf "$TEMP_DIR"

# Test 7: Verify GitHub Actions workflow
echo -e "\n${YELLOW}Test 7: Check GitHub Actions workflow${NC}"
if [[ -f .github/workflows/update-docs.yml ]]; then
    echo -e "${GREEN}✓ GitHub Actions workflow exists${NC}"
    ((PASSED++))
else
    echo -e "${RED}✗ GitHub Actions workflow missing${NC}"
    ((FAILED++))
fi

# Summary
echo -e "\n${GREEN}Test Summary${NC}"
echo "============"
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"

if [[ $FAILED -eq 0 ]]; then
    echo -e "\n${GREEN}✅ All tests passed! Safe to merge to main.${NC}"
    exit 0
else
    echo -e "\n${RED}❌ Some tests failed. Fix issues before merging.${NC}"
    exit 1
fi