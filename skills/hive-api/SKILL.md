---
name: hive-api
description: Reference for Hive's public REST and GraphQL APIs. Use when building integrations, creating webhooks, querying actions/projects/messages via the Hive API, or when the user asks about Hive API endpoints, authentication, or request formats.
---

# Hive API

Hive exposes three public APIs:

| API | Base URL | Best for |
|-----|----------|----------|
| REST v1 | `https://app.hive.com/api/v1` | Full CRUD on actions/projects/messages, webhooks |
| REST v2 | `https://app.hive.com/api/v2` | Bulk updates, cursor pagination, dashboards, agile sprints |
| GraphQL | `https://prod-gql.hive.com/graphql` | Complex queries, schema introspection |

All require **SSL** and an **API key**. v1 and v2 REST endpoints coexist -- use v2 when it offers the endpoint you need (it has cursor pagination and bulk operations), fall back to v1 for endpoints not yet in v2.

## Authentication

1. Log in to Hive → top-right menu → **Edit Profile** → **API Info** tab
2. Copy your **API key** and **User ID**

**REST (v1 and v2)**: `user_id` as query param, `api_key` as header:

```bash
curl -H "api_key: API_KEY" \
  "https://app.hive.com/api/v1/{endpoint}?user_id=USER_ID"
```

Test credentials: `GET /testcredentials?user_id=USER_ID` with `api_key` header → returns `"User authenticated"`.

**GraphQL**: Pass both as HTTP headers:

```
api_key: {API_KEY}
user_id: {USER_ID}
```

## REST v1 Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workspaces/{id}/actions` | List actions (limit 100, supports filters & sort) |
| GET | `/actions/{id}` | Get single action by ID |
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

## REST v2 Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workspaces/{id}/projects` | List projects (cursor pagination) |
| PATCH | `/actions` | Bulk update multiple actions |
| GET | `/agile-sprints/{id}` | Get agile sprint by ID |
| GET | `/workspaces/{id}/agile-sprints` | List agile sprints |
| GET | `/dashboard-widgets/{id}/export` | Export widget data (CSV) |
| GET | `/dashboard-widgets/{id}/data` | Get widget data (JSON, charts only) |

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
