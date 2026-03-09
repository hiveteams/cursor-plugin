# hive-cursor-plugin

Hive's Cursor plugin — API skills, agents, and MCP integration.

## Included

- `rules/`: always-on rule for API key gating
- `skills/hive-api/`: Hive REST & GraphQL API skill with endpoint schemas
- `agents/`: project-manager and solutions-engineer agents
- `hooks/hooks.json`: beforeMCPExecution (workspace profile gate) hooks
- `scripts/`: setup, docs freshness, MCP gate, and utility scripts

- `mcp.json`: Hive MCP server config (API key added on first use)
- `hive-profile.json`: template for persisted workspace metadata

## Getting started

### First-use setup

On your first Hive interaction the plugin handles setup automatically:

1. **API key** — the `hive-api-key` rule asks for your key if `.cursor/mcp.json` still has the placeholder. You can find it by clicking your avatar in the top right corner of the Hive app, then **My settings** → **API info** → copy **API Key**. After saving, restart Cursor.
2. **Workspace profile** — a `beforeMCPExecution` hook (`hive_mcp_gate.py`) fires before every Hive MCP call. If `.cursor/hive-profile.json` has no workspaces yet, it blocks the call and instructs the agent to run `getUsersWorkspaces` first. If you have multiple workspaces it will ask you to pick a default.

After setup, the hook automatically injects the `activeWorkspaceId` into every Hive MCP call — no manual workspace IDs needed.
