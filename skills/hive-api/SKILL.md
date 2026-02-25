---
name: hive-api
description: Reference for Hive's public REST and GraphQL APIs. Use when building integrations, creating webhooks, querying actions/projects/messages via the Hive API, or when the user asks about Hive API endpoints, authentication, or request formats.
---

# Hive API

Hive exposes two public APIs. Choose based on your use case:

| API | Base URL | Best for |
|-----|----------|----------|
| REST | `https://app.hive.com/api/v1` | Simple CRUD, webhooks, quick integrations |
| GraphQL | `https://prod-gql.hive.com/graphql` | Complex queries, pagination, schema introspection |

Both require **SSL** and an **API key**.

## Authentication

1. Log in to Hive → top-right menu → **Edit Profile** → **API Info** tab
2. Copy your **API key** and **User ID**

**REST**: Pass as query params on every request:

```
https://app.hive.com/api/v1/{endpoint}?user_id={USER_ID}&api_key={API_KEY}
```

**GraphQL**: Pass as HTTP headers:

```
api_key: {API_KEY}
user_id: {USER_ID}
```

## REST API Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workspaces/{id}/actions` | List actions (limit 100, supports filters & sort) |
| POST | `/actions/create` | Create action |
| PUT | `/actions/{id}` | Update action (status, title, assignees, etc.) |
| POST | `/actions/{id}/apply-template` | Apply action template |
| GET | `/workspaces/{id}/projects` | List projects |
| GET | `/projects/{id}` | Get project by ID |
| POST | `/projects` | Create project |
| PUT | `/projects/{id}` | Update project |
| DELETE | `/projects/{id}` | Delete project |
| GET | `/workspaces/{id}/users` | List workspace users |
| GET | `/workspaces/{id}/groups` | List chat groups |
| POST | `/messages/create` | Send a message to a group |
| POST | `/workspaces/{id}/labels` | Create label |
| GET | `/workspaces/{id}/custom-tags?type={user\|project}` | Get custom tags |
| PUT | `/resource-assignments/{id}` | Update resource assignment |
| POST | `/webhooks` | Register a webhook |
| DELETE | `/webhooks/{id}` | Delete a webhook |

For full parameter details, request/response schemas, and examples, see [rest-api-reference.md](rest-api-reference.md).

## GraphQL API Quick Reference

**Endpoint**: `https://prod-gql.hive.com/graphql`
**Playground**: [https://prod-gql.hive.com/graphql](https://prod-gql.hive.com/graphql) (interactive schema browser)

Test credentials with:

```graphql
query {
  getUser {
    userId
    email
  }
}
```

The GraphQL API supports queries and mutations for actions, projects, messages, approval rounds, and more. Use the Playground's schema explorer for the full, up-to-date list of operations and types.

For details, see [graphql-reference.md](graphql-reference.md).

## Webhooks

Register webhooks to receive real-time POST notifications when records change.

**Supported triggers:**

| Trigger | Event |
|---------|-------|
| `actions::i` | Action created |
| `actions::u` | Action updated |
| `projects::i` | Project created |
| `projects::u` | Project updated |

Use `fields` array to filter which field changes fire the webhook. Use `projectIds` to scope action webhooks to specific projects.

For webhook setup details, see the Webhooks section in [rest-api-reference.md](rest-api-reference.md).

## Error Handling

All errors return standard HTTP status codes. 400-level errors include a JSON body:

```json
{ "error": 400, "message": "User not found" }
```

## Important Notes

- The API is actively evolving; avoid relying on undocumented fields
- Action statuses: `"Unstarted"`, `"In Progress"`, `"Completed"` (not `"Complete"`)
- Date format for REST: `yyyy/mm/dd` for create, ISO 8601 for update
- Description fields support basic HTML (`h1`, `h2`, `a`, `b`, `u` tags)
