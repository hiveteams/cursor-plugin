# hive-cursor-plugin

Hive's Cursor plugin — API skills, agents, MCP integration, and automatic docs freshness checks.

## Included

- `rules/`: always-on rule that gates Hive MCP usage behind API key setup
- `skills/hive-api/`: Hive REST & GraphQL API skill with endpoint schemas
- `agents/`: project-manager and solutions-engineer agents
- `hooks/hooks.json`: sessionStart hook for docs freshness checks
- `scripts/`: setup, docs freshness, and utility scripts
- `mcp.json`: Hive MCP server config (API key added on first use)

## Getting started

### API key setup

The Hive MCP server requires an API key. On first use the agent will automatically ask for it. You can find your key by:

1. Clicking your avatar in the top right corner of the Hive app
2. Clicking **My settings** → **API info**
3. Copying the **API Key**

The agent will save the key into `.cursor/mcp.json` — restart Cursor after setup.
