# Hive Webhooks Guide

Webhooks send real-time HTTP POST requests to your URL when Hive records are inserted or updated.

## Trigger Types

| Trigger | Event |
|---------|-------|
| `actions::i` | Action inserted |
| `actions::u` | Action updated |
| `projects::i` | Project inserted |
| `projects::u` | Project updated |

## Configuration

- **projectIds**: Filter to specific projects (empty array = all projects, `null` in array = actions with no project)
- **fields**: Filter to specific field changes (empty array = any field change, only relevant for `::u` triggers)
- **additionalHeaders**: Static headers for verifying webhook authenticity

## Examples

### Notify on new project

```json
{
  "name": "New project notification",
  "workspaceId": "WORKSPACE_ID",
  "trigger": "projects::i",
  "url": "https://your-server.com/webhook"
}
```

### Notify on project end date change

```json
{
  "name": "Project end date updated",
  "workspaceId": "WORKSPACE_ID",
  "trigger": "projects::u",
  "fields": ["endDate"],
  "url": "https://your-server.com/webhook"
}
```

### Notify on action updates in specific project

```json
{
  "name": "Action updates in project",
  "workspaceId": "WORKSPACE_ID",
  "trigger": "actions::u",
  "projectIds": ["PROJECT_ID"],
  "fields": [],
  "url": "https://your-server.com/webhook"
}
```

### Notify only on title/description changes

```json
{
  "name": "Action title or description changed",
  "workspaceId": "WORKSPACE_ID",
  "trigger": "actions::u",
  "projectIds": ["PROJECT_ID"],
  "fields": ["title", "description"],
  "url": "https://your-server.com/webhook"
}
```

## Payload Format

Payloads include webhook metadata and the full current record:

### Action webhook payload

```json
{
  "trigger": "actions::u",
  "ownerId": "USER_ID",
  "webhookId": "WEBHOOK_ID",
  "action": {
    "id": "...",
    "title": "...",
    "status": "...",
    ...
  }
}
```

### Project webhook payload

```json
{
  "trigger": "projects::i",
  "ownerId": "USER_ID",
  "webhookId": "WEBHOOK_ID",
  "project": {
    "id": "...",
    "name": "...",
    ...
  }
}
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/webhooks` | Create webhook (required: name, workspaceId, trigger, url) |
| DELETE | `/webhooks/{webhookId}` | Delete webhook |
