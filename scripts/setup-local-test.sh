#!/usr/bin/env bash
#
# Install or uninstall the Hive Cursor plugin components into a target
# repository for local testing before marketplace submission.
#
# Usage:
#   ./scripts/setup-local-test.sh <repo-root>              # install
#   ./scripts/setup-local-test.sh <repo-root> uninstall     # uninstall
#
# What it does (install):
#   1. Symlinks the hive-api skill into <repo>/.cursor/skills/
#   2. Symlinks the solutions-engineer agent into <repo>/.cursor/agents/
#   3. Creates <repo>/.cursor/hooks.json with the sessionStart hook
#      (skips if hooks.json already exists to avoid clobbering)
#   4. Installs the Hive MCP server config into <repo>/.cursor/mcp.json
#      (merges with existing config if present)
#   5. Symlinks the hive-api-key rule into <repo>/.cursor/rules/
#   6. Runs the docs-freshness script once to warm the cache
#
# What it does (uninstall):
#   Removes symlinks, hooks.json, the hive-api-key rule, and the 'hive'
#   MCP entry that this script created.
#
set -euo pipefail

PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ACTION="${2:-install}"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BOLD='\033[1m'
RESET='\033[0m'

usage() {
    echo "Usage: $0 <repo-root> [install|uninstall]"
    echo ""
    echo "  <repo-root>   Path to the repository where you want to test the plugin"
    echo "  install        (default) Symlink plugin components into the repo"
    echo "  uninstall      Remove symlinks and hooks created by install"
    exit 1
}

log()   { echo -e "${GREEN}  ✓${RESET} $*"; }
warn()  { echo -e "${YELLOW}  ⚠${RESET} $*"; }
err()   { echo -e "${RED}  ✗${RESET} $*"; }

if [[ $# -lt 1 ]]; then
    usage
fi

TARGET_REPO="$(cd "$1" && pwd)" || { err "Directory '$1' does not exist"; exit 1; }
CURSOR_DIR="$TARGET_REPO/.cursor"

install() {
    echo -e "${BOLD}Installing Hive Cursor plugin into ${TARGET_REPO}${RESET}"
    echo ""

    # -- Skill --
    mkdir -p "$CURSOR_DIR/skills"
    ln -sfn "$PLUGIN_ROOT/skills/hive-api" "$CURSOR_DIR/skills/hive-api"
    log "Linked skill:  hive-api -> $CURSOR_DIR/skills/hive-api"

    # -- Agent --
    mkdir -p "$CURSOR_DIR/agents"
    ln -sfn "$PLUGIN_ROOT/agents/solutions-engineer.md" "$CURSOR_DIR/agents/solutions-engineer.md"
    log "Linked agent:  solutions-engineer -> $CURSOR_DIR/agents/solutions-engineer.md"

    # -- Hooks --
    local hooks_file="$CURSOR_DIR/hooks.json"
    local hook_cmd="python $PLUGIN_ROOT/scripts/check_hive_docs_freshness.py --quiet --ttl-hours 24"

    if [[ -f "$hooks_file" ]]; then
        if grep -q "check_hive_docs_freshness" "$hooks_file" 2>/dev/null; then
            log "Hooks already configured (sessionStart hook present)"
        else
            warn "hooks.json already exists at $hooks_file"
            warn "Add this sessionStart entry manually:"
            echo ""
            echo "    {\"command\": \"$hook_cmd\", \"timeout\": 5}"
            echo ""
        fi
    else
        cat > "$hooks_file" <<HOOKS_EOF
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "command": "$hook_cmd",
        "timeout": 5
      }
    ]
  }
}
HOOKS_EOF
        log "Created hooks: $hooks_file"
    fi

    # -- MCP config --
    local mcp_file="$CURSOR_DIR/mcp.json"

    if [[ -f "$mcp_file" ]]; then
        if grep -q '"hive"' "$mcp_file" 2>/dev/null; then
            log "MCP config already contains a 'hive' entry — skipping"
        else
            local tmp_file
            tmp_file="$(mktemp)"
            if command -v python3 &>/dev/null; then
                python3 -c "
import json, sys
with open('$mcp_file') as f:
    existing = json.load(f)
with open('$PLUGIN_ROOT/mcp.json') as f:
    plugin = json.load(f)
existing.setdefault('mcpServers', {}).update(plugin.get('mcpServers', {}))
with open('$tmp_file', 'w') as f:
    json.dump(existing, f, indent=2)
    f.write('\n')
"
                mv "$tmp_file" "$mcp_file"
                log "Merged Hive MCP config into existing $mcp_file"
            else
                warn "python3 not found — cannot merge MCP config automatically"
                warn "Add the contents of $PLUGIN_ROOT/mcp.json to $mcp_file manually"
            fi
        fi
    else
        cp "$PLUGIN_ROOT/mcp.json" "$mcp_file"
        log "Created MCP config: $mcp_file"
    fi

    # -- Rule --
    mkdir -p "$CURSOR_DIR/rules"
    ln -sfn "$PLUGIN_ROOT/rules/hive-api-key.mdc" "$CURSOR_DIR/rules/hive-api-key.mdc"
    log "Linked rule:   hive-api-key -> $CURSOR_DIR/rules/hive-api-key.mdc"

    # -- Warm cache --
    echo ""
    echo -e "${BOLD}Warming docs cache...${RESET}"
    if python "$PLUGIN_ROOT/scripts/check_hive_docs_freshness.py" --ttl-hours 24; then
        log "Docs cache warmed"
    else
        warn "Docs cache warmup failed (non-fatal — will retry on next session)"
    fi

    echo ""
    echo -e "${BOLD}Done!${RESET} Restart Cursor, then verify:"
    echo ""
    echo "  1. Open Cursor Settings (Cmd+Shift+J) → Rules"
    echo "     → 'hive-rest-api' skill should appear under Agent Decides"
    echo "     → 'hive-api-key' rule should appear under Always"
    echo ""
    echo "  2. Agent selector → 'solutions-engineer' should be available"
    echo ""
    echo "  3. Cursor Settings → MCP tab"
    echo "     → 'hive' MCP server should appear (will need API key on first use)"
    echo ""
    echo "  4. Cursor Settings → Hooks tab"
    echo "     → sessionStart hook should show as registered"
    echo ""
    echo "  5. Start a new Agent conversation — the sessionStart hook"
    echo "     should fire (check Hooks output channel for errors)"
    echo ""
    echo "  6. Ask: \"Create a project in Hive\""
    echo "     → Agent should ask for your Hive API key if not yet configured"
    echo ""
    echo "  7. Ask: \"How do I create an action with the Hive API?\""
    echo "     → Agent should load the hive-rest-api skill automatically"
}

uninstall() {
    echo -e "${BOLD}Removing Hive Cursor plugin from ${TARGET_REPO}${RESET}"
    echo ""

    if [[ -L "$CURSOR_DIR/skills/hive-api" ]]; then
        rm "$CURSOR_DIR/skills/hive-api"
        log "Removed skill symlink: hive-api"
    else
        warn "Skill symlink not found (already removed?)"
    fi

    if [[ -L "$CURSOR_DIR/agents/solutions-engineer.md" ]]; then
        rm "$CURSOR_DIR/agents/solutions-engineer.md"
        log "Removed agent symlink: solutions-engineer"
    else
        warn "Agent symlink not found (already removed?)"
    fi

    if [[ -f "$CURSOR_DIR/hooks.json" ]] && grep -q "check_hive_docs_freshness" "$CURSOR_DIR/hooks.json" 2>/dev/null; then
        rm "$CURSOR_DIR/hooks.json"
        log "Removed hooks.json"
    else
        warn "hooks.json not found or not created by this script"
    fi

    if [[ -L "$CURSOR_DIR/rules/hive-api-key.mdc" ]]; then
        rm "$CURSOR_DIR/rules/hive-api-key.mdc"
        log "Removed rule symlink: hive-api-key"
    else
        warn "Rule symlink not found (already removed?)"
    fi

    if [[ -f "$CURSOR_DIR/mcp.json" ]] && grep -q '"hive"' "$CURSOR_DIR/mcp.json" 2>/dev/null; then
        local other_servers
        other_servers="$(python3 -c "
import json
with open('$CURSOR_DIR/mcp.json') as f:
    cfg = json.load(f)
servers = cfg.get('mcpServers', {})
servers.pop('hive', None)
print(len(servers))
" 2>/dev/null || echo "error")"
        if [[ "$other_servers" == "0" ]]; then
            rm "$CURSOR_DIR/mcp.json"
            log "Removed mcp.json (no other servers)"
        elif [[ "$other_servers" == "error" ]]; then
            warn "Could not parse mcp.json — remove the 'hive' entry manually"
        else
            python3 -c "
import json
with open('$CURSOR_DIR/mcp.json') as f:
    cfg = json.load(f)
cfg.get('mcpServers', {}).pop('hive', None)
with open('$CURSOR_DIR/mcp.json', 'w') as f:
    json.dump(cfg, f, indent=2)
    f.write('\n')
"
            log "Removed 'hive' entry from mcp.json (kept other servers)"
        fi
    else
        warn "mcp.json not found or does not contain a 'hive' entry"
    fi

    # Clean up empty directories
    rmdir "$CURSOR_DIR/rules" 2>/dev/null && log "Removed empty rules/" || true
    rmdir "$CURSOR_DIR/skills" 2>/dev/null && log "Removed empty skills/" || true
    rmdir "$CURSOR_DIR/agents" 2>/dev/null && log "Removed empty agents/" || true

    echo ""
    echo -e "${BOLD}Done!${RESET} Restart Cursor to deactivate."
}

case "$ACTION" in
    install)   install ;;
    uninstall) uninstall ;;
    *)         usage ;;
esac
