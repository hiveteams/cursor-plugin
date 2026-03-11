---
name: hive-rest-api
description: Hive REST API reference for building integrations. Covers authentication, actions, projects, messages, users, labels, custom fields, custom tags, teams, files, resource assignments, webhooks, and GraphQL. Use when working with the Hive API, building Hive integrations, or making HTTP requests to app.hive.com.
---

# Hive REST API

Base URL: `https://app.hive.com/api/v1`

All requests require SSL. API may evolve; avoid strict response key checks.

## Version Scope

- REST references in this skill are based on the public v1 REST surface (`/api/v1`).
- The public `v2.0` docs currently point to GraphQL documentation rather than a separate REST surface.
- GraphQL reference entry: `https://developers.hive.com/v2.0/reference/hive-graphql-documentation`

## Authentication

Every request requires:
- **Query param**: `user_id=USER_ID`
- **Header**: `api_key: API_KEY`

Get both from Hive: Main menu > My Profile > API Info tab.

```bash
curl -H "api_key: API_KEY" "https://app.hive.com/api/v1/testcredentials?user_id=USER_ID"
```

## Error Handling

400-level errors return `{ error: 400, message: "..." }`.

## Endpoint Quick Reference

### Workspace (list endpoints)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/workspaces/{workspaceId}/actions` | List actions (filter by projectId, status, etc.) |
| GET | `/workspaces/{workspaceId}/projects` | List projects (filter by archived, deleted) |
| GET | `/workspaces/{workspaceId}/users` | List workspace users |

### Actions

| Method | Path | Description |
|--------|------|-------------|
| GET | `/actions/{actionId}` | Get action by ID |
| POST | `/actions/create` | Create action |
| PUT | `/actions/{actionId}` | Update action (status, title, assignees, etc.) |
| DELETE | `/actions/{actionId}` | Delete action |
| GET | `/actions/{actionId}/comments` | Get action comments |
| POST | `/actions/{actionId}/comments` | Create action comment |
| GET | `/actions/{actionId}/action-history` | Get action history |
| GET | `/actions/{actionId}/attachments` | Get action attachments |
| POST | `/actions/{actionId}/attachments` | Create action attachment |
| POST | `/actions/{actionId}/apply-template` | Apply action template |

### Projects

| Method | Path | Description |
|--------|------|-------------|
| POST | `/projects` | Create project |
| PUT | `/projects/{projectId}` | Update project |
| DELETE | `/projects/{projectId}` | Delete project |

### Messages

| Method | Path | Description |
|--------|------|-------------|
| POST | `/messages/create` | Create message in a chat group |

### Users & Workspace

| Method | Path | Description |
|--------|------|-------------|
| GET | `/users/{userId}` | Get user by ID |
| GET | `/users?email=EMAIL` | Get users, filter by email |
| POST | `/workspaces/{workspaceId}/users` | Invite user to workspace |
| DELETE | `/workspaces/{workspaceId}/users` | Remove user from workspace |
| GET | `/workspaces/{workspaceId}/user-settings/{userId}` | Get user settings (rates, dates) |
| GET | `/workspaces/{workspaceId}/external-users` | Get external users |
| GET | `/workspaces/{workspaceId}/removed-users` | Get removed users |

### Labels

| Method | Path | Description |
|--------|------|-------------|
| GET | `/labels?workspaceId=ID` | Get all labels |
| GET | `/labels/{labelId}` | Get label by ID |
| POST | `/labels` | Create label |
| DELETE | `/labels/{labelId}` | Delete label |

### Custom Fields

| Method | Path | Description |
|--------|------|-------------|
| GET | `/custom-fields?workspaceId=ID` | Get custom fields |
| POST | `/custom-fields` | Create custom field |

### Custom Tags

| Method | Path | Description |
|--------|------|-------------|
| GET | `/custom-tags?workspaceId=ID` | Get custom tags |
| POST | `/custom-tags/create` | Create custom tag |
| GET | `/custom-tags/{customTagId}` | Get custom tag by ID |
| PUT | `/custom-tags/{customTagId}` | Update custom tag |
| DELETE | `/custom-tags/{customTagId}` | Delete custom tag |

### Teams

| Method | Path | Description |
|--------|------|-------------|
| GET | `/teams/{teamId}` | Get team by ID |
| POST | `/teams` | Create team |
| DELETE | `/teams/{teamId}` | Delete team |
| POST | `/teams/{teamId}/add-members` | Add members to team |

### Files & Proofing

| Method | Path | Description |
|--------|------|-------------|
| GET | `/files/{fileId}` | Get file by ID |
| GET | `/actions/{actionId}/versioned-files` | Get versioned files for action |
| POST | `/actions/{actionId}/versioned-files` | Create versioned file for action |
| POST | `/versioned-files/{versionedFileId}/versions` | Add new file version |
| GET | `/proofing-files/{proofingFileId}` | Get proofing file |

### Resource Assignments

| Method | Path | Description |
|--------|------|-------------|
| GET | `/resource-assignments/{id}` | Get resource assignment |
| GET | `/resource-assignments?workspaceId=ID` | Get resource assignments |
| POST | `/resource-assignments` | Create resource assignment |
| DELETE | `/resource-assignments/{id}` | Delete resource assignment |

### Project Statuses

| Method | Path | Description |
|--------|------|-------------|
| GET | `/project-statuses?workspaceId=ID` | Get all project statuses |
| GET | `/project-statuses/{statusId}` | Get project status |
| POST | `/project-statuses` | Create project status |

### Webhooks

| Method | Path | Description |
|--------|------|-------------|
| POST | `/webhooks` | Create webhook |
| DELETE | `/webhooks/{webhookId}` | Delete webhook |

## GraphQL API

Full GraphQL docs: [https://graphql.hive.com/getting-started](https://graphql.hive.com/getting-started)

Supports queries/mutations for projects, actions, sections, users, comments, and more. SSL required.

Generated v2 operation reference from live introspection:

- [GraphQL v2 Endpoints Index](docs/v2/graphql/index.md)
- [Legacy GraphQL v2 Endpoints Path](docs/graphql-v2-endpoints.md)

### Introspection Workflow

Use GraphQL introspection when field/type accuracy matters more than static docs.

1. Run an introspection query against the GraphQL endpoint.
2. Extract exact field names, enum values, argument types, and nullability.
3. Use schema results as source of truth when docs and responses differ.
4. Prefer validating uncertain assumptions with introspection before implementing queries/mutations.

Example minimal introspection query:

```graphql
query IntrospectionQuery {
  __schema {
    types {
      name
      kind
    }
  }
}
```

## Additional Resources

For detailed endpoint parameters, request/response schemas, and examples:

- [Endpoint Details](reference/endpoints.md)
- [Data Models](reference/data-models.md)
- [Webhooks Guide](reference/webhooks.md)
- [GraphQL v2 Endpoints Index](docs/v2/graphql/index.md)
- Raw OpenAPI docs in [docs/](docs/) directory
