#!/bin/bash
# Claude Code Configuration Setup Script
# Run this on the target machine after cloning the repo.
#
# Usage:
#   git clone <your-repo-url> ~/.claude
#   cd ~/.claude
#   chmod +x setup.sh
#   ./setup.sh

set -e

echo "=== Claude Code Configuration Setup ==="

# 1. Create settings.json from template
if [ ! -f settings.json ]; then
  echo "[1/5] Creating settings.json from template..."
  HOME_DIR=$(echo ~)
  sed "s|<HOME>|${HOME_DIR}|g; s|<YOUR_SUPERMEMORY_TOKEN>|REPLACE_ME|g" \
    settings.template.json > settings.json
  echo "  -> settings.json created. Edit it to add your API tokens."
else
  echo "[1/5] settings.json already exists, skipping."
fi

# 2. Create machine-specific directories
echo "[2/5] Creating local directories..."
mkdir -p cache backups debug file-history paste-cache \
         session-env sessions shell-snapshots telemetry \
         tasks todos

# 3. Set up MCP servers
echo "[3/5] Setting up MCP servers..."
if [ -d mcp-servers/xmcp ] && [ -f mcp-servers/xmcp/requirements.txt ]; then
  cd mcp-servers/xmcp
  python3 -m venv .venv 2>/dev/null || true
  .venv/bin/pip install -r requirements.txt -q 2>/dev/null || true
  cd ../..
  echo "  -> xmcp server configured."
else
  echo "  -> No MCP server setup needed."
fi

# 4. Fix paths in projects/ memory files
echo "[4/5] Checking project memory paths..."
CURRENT_USER=$(whoami)
if [ "$CURRENT_USER" != "qianlong" ]; then
  echo "  -> Updating paths from 'qianlong' to '${CURRENT_USER}'..."
  find projects/ -name "*.md" -exec sed -i.bak \
    "s|/Users/qianlong|/Users/${CURRENT_USER}|g" {} \; 2>/dev/null || true
  find projects/ -name "*.bak" -delete 2>/dev/null || true
else
  echo "  -> Same user, no path changes needed."
fi

# 5. Verify
echo "[5/5] Verifying installation..."
SKILL_COUNT=$(find skills/ -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
AGENT_COUNT=$(find agents/ -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
RULE_COUNT=$(find rules/ -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
CMD_COUNT=$(find commands/ -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "=== Setup Complete ==="
echo "  Skills:   ${SKILL_COUNT}"
echo "  Agents:   ${AGENT_COUNT}"
echo "  Rules:    ${RULE_COUNT}"
echo "  Commands: ${CMD_COUNT}"
echo ""
echo "Next steps:"
echo "  1. Edit ~/.claude/settings.json to add your API tokens"
echo "  2. Install MCP server dependencies if needed"
echo "  3. Run 'claude' to start using"
