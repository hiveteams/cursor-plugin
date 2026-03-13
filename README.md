# Hive Cursor Plugin

A Cursor plugin that gives the AI assistant access to Hive project management data and API documentation. It adds skills, an agent persona, and an MCP server so Cursor can read and write Hive actions, generate standup summaries, find related work across Hive and git, and scaffold API integration code.

## Who this is for

Developers who want the AI assistant to write their Hive API calls or want to work directly with their Hive workspace in Cursor — querying tasks, writing API calls against correct schemas, and cross-referencing tickets with code history.

## Included components

| Type | Name | What it does |
|------|------|-------------|
| Skill | `hive-api` | Reference docs for Hive REST v1 and GraphQL v2 APIs. Loaded automatically when Cursor needs endpoint schemas, field names, or auth patterns. |
| Skill | `daily-standup-helper` | Queries your assigned Hive actions from the last 24 hours and formats a standup summary (completed, status changes, in progress). |
| Skill | `find-related-work` | Takes a Hive action URL or ID, searches Hive for similar tickets, then searches git history (commit messages + pickaxe) for related code changes. Links commits back to Hive actions via branch names. |
| Skill | `open-pr` | Creates a GitHub pull request and attaches the branch to a Hive action. Automatically links to the action in context, or asks which action to use. |
| Agent | `solutions-engineer` | Persona tuned for building Hive API integrations. Knows REST/GraphQL patterns, webhook design, pagination, error handling. Produces typed TypeScript with curl equivalents. |
| MCP Server | `hive` | Connects Cursor to a running Hive MCP server for live reads and writes against your workspace. |

**Total: 4 skills, 1 agent, 1 MCP server.**

## Install / configure

### From Cursor Plugin Marketplace

Install the plugin from Cursor Settings. The skills, agent, and MCP config are added to your project automatically.

### hive-profile.json

The `daily-standup-helper` and `find-related-work` skills read `hive-profile.json` at the plugin root to resolve your workspace. If `activeWorkspaceId` is set, they use it directly. Otherwise they fall back to calling `getUsersWorkspaces` via MCP.

```json
{
  "workspaces": [],
  "primaryWorkspaceId": null,
  "activeWorkspaceId": "YOUR_WORKSPACE_ID"
}
```

## Auth model

### OAuth

The Hive MCP server uses OAuth for authentication. When you first interact with the MCP server, Cursor prompts you to authorize with Hive. After you authorize, the MCP server manages tokens automatically — no manual credential handling required.

### API key

It is also an option to use an API key with Hive:

| Credential | How it's sent |
|-----------|---------------|
| `user_id` | Query parameter |
| `api_key` | HTTP header |

Get both from **Hive → Main Menu → My Profile → API Info**.

Store credentials in environment variables (`HIVE_API_KEY`, `HIVE_USER_ID`). Never hardcode or log them.

Validate credentials:

```bash
curl -s -H "api_key: $HIVE_API_KEY" \
  "https://app.hive.com/api/v1/testcredentials?user_id=$HIVE_USER_ID"
```

## Network access

The plugin makes requests to:

| Host | Purpose |
|------|---------|
| `hive-mind.hive.com` | MCP server |
| `app.hive.com` | REST API v1 |
| `prod-gql.hive.com` | GraphQL API v2 |

The `find-related-work` skill also uses the GitHub MCP server to fetch PR diffs when a Hive action has attached branch names. This goes through whatever GitHub MCP server is configured in your Cursor environment.

All Hive API traffic is over HTTPS. No other external services are contacted.

## Data handling

- **Read access**: Skills query your Hive actions, projects, labels, and workspace metadata. The `find-related-work` skill also reads local git history and optionally GitHub PR diffs.
- **Write access**: The MCP server can create and update Hive actions if you ask it to. The skills themselves are read-only.
- **Credential storage**: API keys are expected in environment variables or passed through the MCP server. Nothing is persisted to disk by the plugin beyond `hive-profile.json` (which contains workspace IDs, not secrets).
- **Local data**: `hive-profile.json` stores workspace IDs. No action content, user data, or API responses are cached to disk.
- **LLM context**: Hive data fetched during a session (action titles, descriptions, statuses) is passed to the LLM as part of the conversation context. This follows Cursor's standard context handling.

## Example prompts

**Standup summary**
> "What did I do yesterday?" / "Generate my standup"

Uses `daily-standup-helper`. Queries completed and modified actions from the last 24 hours, outputs a grouped summary.

**Related work lookup**
> "Find related work for <https://app.hive.com/workspace/.../action/ABC123>"

Uses `find-related-work`. Searches Hive for similar tickets, searches git for commits touching the same code, links them together.

**API integration help**
> "How do I create an action with the Hive API?"

Loads the `hive-api` skill and returns the exact endpoint, required fields, and a working code example.

**Solutions engineer agent**
> "Build a script that fetches all of the Hive actions assigned to a user X in project Y and ensures they all have custom field value Z"

The `solutions-engineer` agent picks the right API surface (REST vs GraphQL) and produces the script.

**Open a pull request**
> "Open a PR for this branch" / "Create a PR and link it to ACTION_ID"

Uses `open-pr`. Pushes the branch, creates the GitHub PR, and attaches the branch to the Hive action in context (or asks which action to link).

**Direct workspace operations**
> "Create a project in Hive called Q2 Roadmap"
> "What actions are assigned to me in the Backend project?"

Uses the Hive MCP server for live reads and writes.

## Limitations / non-goals

- **Single workspace at a time.** Skills resolve one active workspace at a time. Multi-workspace workflows require prompting the agent to change workspaces.
