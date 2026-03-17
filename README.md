# Hive Cursor Plugin

The Hive Cursor Plugin connects Cursor to Hive so the AI assistant can help users operate real work: manage actions and projects, build forms and workflows, summarize dashboards and goals, run meeting follow-up, and still provide API and integration guidance when needed.

It keeps the original technical integration value of the plugin, but expands it into a broader project-management and operations assistant for Hive users.

## Who this is for

- Teams using Hive as their project management system
- PMs, chiefs of staff, ops leads, and delivery leads who want faster work coordination from Cursor
- Technical users who still want API guidance, workflow design help, and integration-ready examples

## Included components

### Skills

| Skill | What it does |
|------|--------------|
| `manage-hive-work` | Creates, updates, organizes, assigns, and summarizes actions and projects in Hive. |
| `design-hive-form` | Designs request and intake forms that create actions, projects, and follow-up flows. |
| `build-hive-workflow` | Creates recurring and event-based Hive automations from natural language. |
| `track-hive-goals` | Reviews goal progress, risks, and next actions. |
| `summarize-hive-dashboard` | Produces executive summaries from dashboards, reporting views, and project health signals. |
| `run-meeting-followup` | Turns notes and meetings into recap output, owners, and next-step actions. |
| `search-hive-knowledge` | Searches notes and workspace context before guessing. |
| `daily-standup-helper` | Generates a daily standup from recent Hive action changes. |
| `find-related-work` | Links Hive work to similar tickets, local git history, and related code changes. Can optionally use GitHub tooling if it is already present in the user's Cursor environment. |
| `hive-api` | Reference docs for Hive REST v1 and GraphQL v2 APIs. |
| `open-pr` | Creates a PR and links the branch back to a Hive action when GitHub tooling is already available in Cursor. |

### Agents

| Agent | What it does |
|------|--------------|
| `hive-ops-agent` | General-purpose Hive operating agent for work execution, forms, workflows, and structured updates. |
| `hive-reporting-agent` | Reporting-focused agent for executive summaries, dashboards, and goal reviews. |
| `hive-meetings-agent` | Meeting-to-execution agent for notes, actions, and follow-up drafts. |
| `solutions-engineer` | Integration-focused agent for API requests, scripts, webhooks, and implementation guidance. |

### Commands

| Command | What it does |
|--------|---------------|
| `/hive-connect` | Helps connect Cursor to Hive and verify the workspace context. |
| `/hive-plan-work` | Turns a goal, project, or vague request into a concrete Hive execution plan. |
| `/hive-create-form` | Builds a Hive intake or request form. |
| `/hive-create-workflow` | Creates a Hive app workflow or recurring automation. |
| `/hive-goal-review` | Produces a goal status review with next steps. |
| `/hive-exec-summary` | Produces a concise leadership or project-health summary. |
| `/hive-meeting-followup` | Converts meetings or notes into recap output and follow-through. |

### Rules

The plugin also adds persistent guidance for:

- safe use of live Hive data
- email and calendar guardrails
- work item editing vs commenting behavior
- workflow authoring best practices
- reporting and pagination behavior

### MCP

| Component | What it does |
|----------|---------------|
| `Hive` MCP server | Connects Cursor to Hive for live workspace reads and writes. |

## Install and configure

### From Cursor Plugin Marketplace

Install the plugin from Cursor Settings. Cursor will load the plugin assets and the Hive MCP configuration for the project or user scope you choose.

### `hive-profile.json`

Some skills use `hive-profile.json` to remember the active workspace. If `activeWorkspaceId` is set, they use it directly. Otherwise they fall back to resolving the current workspace through Hive.

```json
{
  "workspaces": [],
  "primaryWorkspaceId": null,
  "activeWorkspaceId": "YOUR_WORKSPACE_ID"
}
```

## Auth model

### OAuth

The Hive MCP server supports OAuth. When you first use Hive from Cursor, authorize with Hive and let the MCP server manage tokens for you.

### API key

Raw REST or GraphQL requests can also use API keys:

| Credential | How it's sent |
|-----------|---------------|
| `user_id` | Query parameter |
| `api_key` | HTTP header |

Get both from **Hive → Main Menu → My Profile → API Info**.

Store credentials in environment variables such as `HIVE_API_KEY` and `HIVE_USER_ID`. Never hardcode or log them.

Credential check:

```bash
curl -s -H "api_key: $HIVE_API_KEY" \
  "https://app.hive.com/api/v1/testcredentials?user_id=$HIVE_USER_ID"
```

## Network access

The plugin may contact:

| Host | Purpose |
|------|---------|
| `hive-mind.hive.com` | Hive MCP server |
| `app.hive.com` | Hive REST API v1 |
| `prod-gql.hive.com` | Hive GraphQL API v2 |

The `find-related-work` and `open-pr` flows may also use git or GitHub tooling already available in the user's Cursor environment. The plugin does not bundle a separate GitHub MCP server.

## Data handling

- **Read access**: The plugin may query actions, projects, labels, notes, goals, dashboards, and workspace metadata.
- **Write access**: The plugin can create or update Hive objects when the user asks it to.
- **Credential storage**: Secrets should live in OAuth flows or environment variables, not in plugin files.
- **Local storage**: `hive-profile.json` stores workspace selection only.
- **LLM context**: Hive data retrieved during a session is passed through normal Cursor conversation context.

## Example prompts

### Work management

> "Create a project in Hive called Q2 Roadmap and give me the first sections I should use."

> "Summarize what is overdue in the launch project and suggest the next three actions."

### Forms and workflows

> "Build a creative request form in Hive that creates actions and routes them to the design lead."

> "Create a workflow that sends me a Friday summary of completed launch work."

### Goals and reporting

> "Review our product launch goal and tell me what is missing."

> "Give me an exec summary of project health across the current dashboard."

### Meetings and knowledge

> "Turn these meeting notes into follow-up tasks and a recap."

> "Find the prior notes and related work for this customer kickoff."

### Technical integration help

> "How do I create an action with the Hive API?"

> "Build a script that fetches all Hive actions assigned to a user in project Y and ensures they all have custom field value Z."

## Permissions

The plugin only has the permissions of the Hive user account that authenticates with it. It does not add a separate permissions layer on top of Hive.

## Current limitations

- The plugin typically operates in one active workspace at a time.
- The quality of available operations depends on the Hive permissions and apps enabled in that workspace.
