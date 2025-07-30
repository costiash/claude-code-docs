#!/bin/bash
# Check if hook/command files need updating

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
HOOK_VERSION_FILE="$SCRIPT_DIR/.hook_version"
USER_HOOK_VERSION_FILE="$HOME/.claude/.hook_version"

# Get current hook version from repository
if [[ -f "$HOOK_VERSION_FILE" ]]; then
    CURRENT_VERSION=$(cat "$HOOK_VERSION_FILE")
else
    CURRENT_VERSION=1
fi

# Get installed hook version
if [[ -f "$USER_HOOK_VERSION_FILE" ]]; then
    INSTALLED_VERSION=$(cat "$USER_HOOK_VERSION_FILE")
else
    INSTALLED_VERSION=1  # Assume old version if no version file
fi

# Check if update needed
if [[ "$CURRENT_VERSION" -gt "$INSTALLED_VERSION" ]]; then
    echo "⚠️  Claude Code Docs has been updated!" >&2
    echo "Your hook version: $INSTALLED_VERSION" >&2
    echo "Current version: $CURRENT_VERSION" >&2
    echo "" >&2
    echo "Please run the installer to update:" >&2
    echo "  cd $SCRIPT_DIR && ./install.sh" >&2
    echo "" >&2
    echo "This will update the auto-update mechanism and command files." >&2
    
    # Return non-zero to indicate update needed
    exit 1
fi

# All good
exit 0