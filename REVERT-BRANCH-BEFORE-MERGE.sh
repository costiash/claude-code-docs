#!/bin/bash
# Script to revert branch-specific changes before merging to main

echo "Reverting dev-v0.3-refactor branch references to main..."

# Replace all dev-v0.3-refactor references with main
sed -i.bak 's/dev-v0.3-refactor/main/g' install.sh

# Remove -b flag from clone commands
sed -i.bak 's/git clone -b main/git clone/g' install.sh

# Show the changes
echo "Changes made:"
diff install.sh.bak install.sh || true

echo ""
echo "✅ Branch references reverted!"
echo ""
echo "Next steps:"
echo "1. Review the changes: git diff install.sh"
echo "2. Commit: git add install.sh && git commit -m 'revert: change branch references back to main for merge'"
echo "3. Push: git push origin dev-v0.3-refactor"
echo "4. Then merge to main as documented"