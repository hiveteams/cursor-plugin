# Hive Cursor Plugin

A Cursor plugin that gives the AI assistant access to Hive project management data and API documentation. It adds skills, agent personas, commands, rules, and an MCP server so Cursor can read and write Hive actions, generate standup summaries, find related work across Hive and git, scaffold API integration code, and optionally help operate broader Hive workflows.

## Who this is for

Developers who want the AI assistant to write their Hive API calls or want to work directly with their Hive workspace in Cursor — querying tasks, writing API calls against correct schemas, and cross-referencing tickets with code history.

The plugin also includes additional Hive workflow helpers for users who want to use Cursor as a natural-language interface for work management, forms, workflows, reporting, and operational handoffs.

## Included components

### Developer-focused components

| Type | Name | What it does |
|------|------|-------------|
| Skill | `hive-api` | Reference docs for Hive REST v1 and GraphQL v2 APIs. Loaded automatically when Cursor needs endpoint schemas, field names, or auth patterns. |
| Skill | `hive-daily-standup-helper` | Queries your assigned Hive actions from the last 24 hours and formats a standup summary (completed, status changes, in progress). |
| Skill | `hive-find-related-work` | Takes a Hive action URL or ID, searches Hive for similar tickets, then searches git history (commit messages + pickaxe) for related code changes. Links commits back to Hive actions via branch names. |
| Skill | `hive-open-pr` | Creates a GitHub pull request and attaches the branch to a Hive action. Automatically links to the action in context, or asks which action to use. |
| Agent | `hive-solutions-engineer` | Persona tuned for building Hive API integrations. Knows REST/GraphQL patterns, webhook design, pagination, error handling. Produces typed TypeScript with curl equivalents. |
| MCP Server | `hive` | Connects Cursor to a running Hive MCP server for live reads and writes against your workspace. |

### Additional Hive workflow components

#### Skills

| Skill | What it does |
|------|--------------|
| `hive-manage-hive-work` | Creates, updates, organizes, assigns, and summarizes actions and projects in Hive. |
| `hive-bootstrap-hive-workspace` | Recommends a full Hive setup for launches, agencies, customer operations, onboarding, strategic planning, and other team workflows. |
| `hive-design-hive-form` | Designs request and intake forms that create actions, projects, and follow-up flows. |
| `hive-build-hive-workflow` | Creates recurring and event-based Hive automations from natural language. |
| `hive-track-hive-goals` | Reviews goal progress, risks, and next actions. |
| `hive-summarize-hive-dashboard` | Produces executive summaries from dashboards, reporting views, and project health signals. |
| `hive-run-meeting-followup` | Turns notes and meetings into recap output, owners, and next-step actions. |
| `hive-search-hive-knowledge` | Searches notes and workspace context before guessing. |
| `hive-run-sales-ops` | Builds customer handoff, pipeline, and CRM-aware operational workflows in Hive. |
| `hive-run-services-ops` | Designs services delivery, time, approvals, and invoice-prep workflows in Hive. |
| `hive-work-with-connected-content` | Combines Hive execution with connected content sources when the user's environment already provides them. |

#### Agents

| Agent | What it does |
|------|--------------|
| `hive-ops-agent` | General-purpose Hive operating agent for work execution, forms, workflows, and structured updates. |
| `hive-reporting-agent` | Reporting-focused agent for executive summaries, dashboards, and goal reviews. |
| `hive-meetings-agent` | Meeting-to-execution agent for notes, actions, and follow-up drafts. |
| `hive-workspace-architect` | Workspace design agent for templates, rollout plans, and operating-model setup. |
| `hive-revenue-ops-agent` | Revenue and CRM workflow agent for customer handoffs and pipeline-driven execution. |
| `hive-services-ops-agent` | Services operations agent for delivery control, approvals, time, and invoice-prep workflows. |
#### Commands

| Command | What it does |
|--------|---------------|
| `/hive-connect` | Helps connect Cursor to Hive and verify the workspace context. |
| `/hive-bootstrap-workspace` | Recommends the first complete Hive setup for a team or business workflow. |
| `/hive-plan-work` | Turns a goal, project, or vague request into a concrete Hive execution plan. |
| `/hive-create-form` | Builds a Hive intake or request form. |
| `/hive-create-workflow` | Creates a Hive app workflow or recurring automation. |
| `/hive-goal-review` | Produces a goal status review with next steps. |
| `/hive-exec-summary` | Produces a concise leadership or project-health summary. |
| `/hive-meeting-followup` | Converts meetings or notes into recap output and follow-through. |
| `/hive-sales-handoff` | Builds a sales-to-delivery or CRM-to-execution handoff process in Hive. |
| `/hive-prepare-invoice` | Summarizes delivery and time data into invoice-prep workflow output. |
| `/hive-connected-content` | Uses Hive plus connected content sources when the user's environment already provides them. |

#### Rules

The plugin also adds persistent guidance for:

- safe use of live Hive data
- email and calendar guardrails
- work item editing vs commenting behavior
- workflow authoring best practices
- reporting and pagination behavior
- integration readiness for external systems and connectors

### MCP

| Component | What it does |
|----------|---------------|
| `hive` MCP server | Connects Cursor to Hive for live workspace reads and writes. |

## Install and configure

### From Cursor Plugin Marketplace

Install the plugin from Cursor Settings. Cursor will load the plugin assets and the Hive MCP configuration for the project or user scope you choose.

### `hive-profile.json`

Some skills use `hive-profile.json` to remember the active workspace. The file is saved in your project root at:

`<project-root>/hive-profile.json`

If `activeWorkspaceId` is set, skills use it directly. Otherwise they fall back to resolving the current workspace through Hive.

```json
{
  "workspaces": [],
  "primaryWorkspaceId": "",
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

The `hive-find-related-work` and `hive-open-pr` flows can also use GitHub tooling that is already available in the user's Cursor environment. The plugin does not bundle a separate GitHub MCP server.

All Hive API traffic is over HTTPS. No other external services are contacted by default.

## Data handling

- **Read access**: Skills query your Hive actions, projects, labels, and workspace metadata. Additional workflow helpers may also query notes, goals, dashboards, and connected content sources when those are available.
- **Write access**: The MCP server can create and update Hive objects if you ask it to. Many of the prompt assets are guidance-only until used alongside the appropriate Hive or environment tooling.
- **Credential storage**: API keys are expected in environment variables or passed through the MCP server. Nothing is persisted to disk by the plugin beyond `hive-profile.json` (which contains workspace IDs, not secrets).
- **Local data**: `hive-profile.json` stores workspace IDs. No action content, user data, or API responses are cached to disk.
- **LLM context**: Hive data fetched during a session is passed to the LLM as part of the conversation context. This follows Cursor's standard context handling.

## Example prompts

### Developer workflows

**Standup summary**
> "What did I do yesterday?" / "Generate my standup"

Uses `hive-daily-standup-helper`. Queries completed and modified actions from the last 24 hours, outputs a grouped summary.

**Related work lookup**
> "Find related work for <https://app.hive.com/workspace/.../action/ABC123>"

Uses `hive-find-related-work`. Searches Hive for similar tickets, searches git for commits touching the same code, and links them together.

**API integration help**
> "How do I create an action with the Hive API?"

Loads `hive-api` and returns the exact endpoint, required fields, and a working code example.

**Solutions engineer agent**
> "Build a script that fetches all of the Hive actions assigned to a user X in project Y and ensures they all have custom field value Z"

The `hive-solutions-engineer` agent picks the right API surface (REST vs GraphQL) and produces the script.

**Open a pull request**
> "Open a PR for this branch" / "Create a PR and link it to ACTION_ID"

Uses `hive-open-pr`. Pushes the branch, creates the GitHub PR, and attaches the branch to the Hive action in context when the needed GitHub tooling is available.

### Hive workflow examples

> "Create a project in Hive called Q2 Roadmap and give me the first sections I should use."

> "Summarize what is overdue in the launch project and suggest the next three actions."

> "Set up Hive for a customer onboarding team and tell me which projects, forms, and dashboards to create first."

### Forms and workflows

> "Build a creative request form in Hive that creates actions and routes them to the design lead."

> "Create a workflow that sends me a Friday summary of completed launch work."

### Revenue and services operations

> "Create a closed-won handoff process in Hive from sales to onboarding."

> "Prepare an invoice review summary for this client project from delivery work in Hive."

### Connector-aware workflows

> "Search our connected content for the latest implementation plan, then turn it into Hive follow-up work."

### Goals and reporting

> "Review our product launch goal and tell me what is missing."

> "Give me an exec summary of project health across the current dashboard."

### Meetings and knowledge

> "Turn these meeting notes into follow-up tasks and a recap."

> "Find the prior notes and related work for this customer kickoff."

## Permissions

The MCP server operates with the same permissions as the Hive user account you authenticate with.

There is no separate permission layer added by the plugin. The authenticated user's role and workspace membership in Hive are the sole authority for what the MCP server can read or write.

## Current limitations

- **Single workspace at a time.** Skills typically resolve one active workspace at a time. Multi-workspace workflows require prompting the agent to change workspaces.
- The quality of available operations depends on the Hive permissions and apps enabled in that workspace.
