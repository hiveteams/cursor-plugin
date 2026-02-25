# Hive REST API Reference

Base URL: `https://app.hive.com/api/v1`

All requests require `?user_id={USER_ID}&api_key={API_KEY}` as query parameters.

---

## Actions

Actions are tasks/to-dos that belong to a Workspace and optionally a Project. They can be infinitely nested (sub-actions use the `parent` field).

### Get Actions

```
GET /workspaces/{workspaceId}/actions
```

**Query params:**

| Param | Type | Description |
|-------|------|-------------|
| `projectId` | string | Filter to a specific project |
| `sortBy` | string | Sort by field, e.g. `title asc` |
| `limit` | string | Results per page (default 100, max 100) |
| `filters` | string | Filter syntax: `filters[fieldName]=value` |

**Supported filter fields:** `status`, `parent`, `archived`, `milestone`, `deleted`, `root`, `recurringId`, `teamAssignee`, `placeholderAssignees`, `priorityLevelId`, `followingUserIds`

**Response** (array of Action objects):

```json
[
  {
    "id": "jArt6JZpezAMZimzy",
    "title": "Prepare for weekly product meeting",
    "workspace": "12345aZjDQZndHqs",
    "assignees": [],
    "projectId": null,
    "status": "Unstarted",
    "deadline": null,
    "scheduledDate": null,
    "checkedDate": null,
    "parent": null,
    "root": null,
    "archived": false,
    "deleted": false,
    "hasSubactions": false,
    "estimate": null,
    "estimates": [{ "userId": "user12345", "time": 7200 }],
    "milestone": false,
    "loggedTime": [
      { "userId": "user12345", "time": 7200, "date": "2019-01-01T00:00:00.000Z" }
    ],
    "phaseId": "abcdefg9876",
    "phaseName": "Planning",
    "priority": {
      "name": "Urgent",
      "level": 1,
      "color": "#f6781a",
      "_id": "abc321"
    },
    "createdAt": "2015-07-09T20:33:56.465Z",
    "modifiedAt": "2016-08-23T07:49:09.621Z",
    "createdBy": "1234abcuJzo4k7F9",
    "modifiedBy": "1234abcuJzo4k7F9"
  }
]
```

### Create Action

```
POST /actions/create
```

**Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `workspace` | string | yes | Workspace ID |
| `title` | string | yes | Action title |
| `description` | string | no | Action description |
| `projectId` | string | no | Assign to project |
| `assignees` | string[] | no | User IDs (defaults to request user) |
| `labels` | string[] | no | Label IDs |
| `deadline` | string | no | End date (`yyyy/mm/dd`) |
| `scheduledDate` | string | no | Start date (`yyyy/mm/dd`) |
| `processId` | string | no | Action template ID to apply |
| `customFields` | object[] | no | `[{ "label": "...", "value": "..." }]` |
| `parentId` | string | no | Parent action ID (creates sub-action) |
| `phaseId` | string | no | Project phase ID |
| `phaseName` | string | no | Project phase name (phaseId takes precedence) |
| `milestone` | boolean | no | Whether action is a milestone |

**Response:**

```json
{
  "id": "qFR6a524nFARukmvF",
  "title": "This is my action",
  "workspace": "12345aZjDQZndHqs",
  "assignees": [],
  "projectId": null,
  "customFields": [],
  "status": "Unstarted",
  "deadline": null,
  "scheduledDate": null,
  "checkedDate": null,
  "parent": null,
  "root": null,
  "hasSubactions": false,
  "estimate": null,
  "loggedTime": [],
  "createdAt": "2018-01-23T21:41:40.295Z",
  "modifiedAt": "2018-01-23T21:41:40.289Z",
  "createdBy": "12345gfuJzo4k7F9",
  "modifiedBy": "12345gfuJzo4k7F9"
}
```

### Update Action

```
PUT /actions/{actionId}
```

**Body (all fields optional):**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | New status (`"Unstarted"`, `"In Progress"`, `"Completed"`) |
| `update_children` | boolean | Also update children statuses |
| `title` | string | New title |
| `projectId` | string | Move to project |
| `assignees` | string[] | Replace assignees |
| `labels` | string[] | Replace labels |
| `description` | string | Overwrite description (supports `h1`, `h2`, `a`, `b`, `u` HTML) |
| `urgent` | boolean | Urgency flag |
| `privacy` | string | `"private"` or `"public"` |
| `checked` | boolean | Checked state |
| `scheduledDate` | date | Start date |
| `deadline` | date | End date |
| `parent` | string | New parent action ID |
| `customFields` | object[] | Add/update text custom fields |
| `shiftSubactionsDeadline` | boolean | Shift sub-action dates by same delta |
| `archived` | boolean | Archive the action |
| `phaseId` | string | Project phase ID |
| `phaseName` | string | Project phase name |
| `followingUserIds` | string[] | Action card followers |
| `agileStoryPoints` | integer | Story points (max 233) |
| `agileSprintId` | string | Sprint ID |
| `milestone` | boolean | Milestone flag |

**Response:** Full updated Action object (same shape as Get Actions response, plus `archived` field).

### Apply Action Template

```
POST /actions/{actionId}/apply-template
```

**Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `processId` | string | yes | Action template (workflow) ID |

**Response:** `{ "message": "Action template successfully applied" }`

---

## Projects

Projects are optional containers for organizing Actions within a Workspace.

### Get Projects

```
GET /workspaces/{workspaceId}/projects
```

**Query params:**

| Param | Type | Description |
|-------|------|-------------|
| `sortBy` | string | e.g. `createdAt+asc` |
| `filters` | string | Supported: `archived`, `deleted` |

**Response:** Array of Project objects.

### Get Project

```
GET /projects/{projectId}
```

**Response:**

```json
{
  "project": {
    "id": "123ABC567XYZ",
    "name": "New project name",
    "description": "",
    "startDate": null,
    "endDate": null,
    "accessOption": "private",
    "sharingType": "me",
    "members": [],
    "template": false,
    "projectCustomFields": [
      {
        "label": "Budget",
        "value": "$5000000",
        "dropdownValues": [],
        "selectedValues": [],
        "type": "text",
        "_id": "1234abcuJzo4k7E1",
        "hidden": false
      }
    ],
    "color": "#3fcaca",
    "parentProject": null,
    "phases": [],
    "budget": 0,
    "resourcePlaceholderIds": [],
    "createdAt": "2017-05-18T15:26:17.407Z",
    "modifiedAt": "2017-05-19T02:25:06.190Z",
    "createdBy": "1234abcuJzo4k7F9",
    "modifiedBy": "1234abcuJzo4k7F9"
  }
}
```

### Create Project

```
POST /projects
```

**Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `workspace` | string | yes | Workspace ID |
| `name` | string | yes | Project name |
| `description` | string | no | Project description |
| `startDate` | date | no | Start date |
| `endDate` | date | no | End date |
| `sharingType` | string | no | `"everyone"`, `"custom"`, or `"me"` (default: `"everyone"`) |
| `members` | string[] | no | User IDs (only if sharingType is `"custom"`) |
| `teams` | string[] | no | Team IDs (only if sharingType is `"custom"`) |
| `projectCustomFields` | object[] | no | Custom field definitions (see below) |
| `color` | string | no | Hex color code |
| `template` | boolean | no | Create as template |
| `copyFrom` | string | no | Source project ID to copy from |
| `copyActionStatuses` | boolean | no | Retain statuses when copying |
| `copyAssignees` | boolean | no | Retain assignees when copying |
| `accessOption` | string | no | `"private"` or `"public"` (default: `"private"`) |
| `phases` | string[] | no | Phase names to create |
| `parentProject` | string | no | Parent project ID |
| `budget` | integer | no | Budget value |

**Project custom field object:**

| Field | Type | Description |
|-------|------|-------------|
| `label` | string | **Required.** Human-readable label |
| `_id` | string | Unique ID |
| `type` | string | `text`, `number`, `date`, `user`, `project`, `select`, `formula` |
| `value` | string | For `text` type |
| `numberValue` | integer | For `number` type |
| `dateValue` | string | For `date` type (ISO 8601) |
| `formula` | string | For `formula` type |
| `dropdownValues` | string[] | Options for `select` type |
| `selectedValues` | string[] | Selected values for `select`, `user`, `project` |
| `allowMultiSelect` | boolean | Allow multiple selections |

### Update Project

```
PUT /projects/{projectId}
```

**Body (all fields optional):**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Project name |
| `description` | string | Project description |
| `startDate` | date | Start date (pass `null` to unset) |
| `endDate` | date | End date (pass `null` to unset) |
| `color` | string | Hex color code |
| `accessOption` | string | `"public"` or `"private"` |
| `parentProject` | string | Parent project ID |
| `sharingType` | string | `"everyone"`, `"custom"`, or `"me"` |
| `members` | string[] | User IDs |
| `teams` | string[] | Team IDs |
| `archived` | boolean | Archive the project |
| `template` | array | Template application config (see docs) |
| `budget` | integer | Budget value |
| `isDraftMode` | boolean | Draft mode state |

### Delete Project

```
DELETE /projects/{projectId}
```

**Response:** `{ "message": "Project was deleted successfully" }`

---

## Messages

Messages are sent from Users to chat Groups.

### Create Message

```
POST /messages/create
```

**Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `workspace` | string | yes | Workspace ID |
| `body` | string | yes | Message body |
| `containerId` | string | yes | Target Group ID |
| `senderName` | string | no | Override sender display name |
| `senderPicture` | string | no | Override sender avatar URL |
| `color` | string | no | Background: `yellow`, `purple`, `green`, `red`, `gray` |

**Response:**

```json
{
  "id": "2bK58icvKeJSzvupB",
  "sender": "12345gfuJzo4k7F9",
  "workspace": "12345naZjDQZndHqs",
  "containerId": "12345ZTJqWY2QK2B",
  "body": "This is a new message",
  "senderPicture": "https://example.com/bot.png",
  "senderFirstName": "My Bot",
  "createdAt": "2018-01-23T22:14:24.862Z",
  "modifiedAt": "2018-01-23T22:14:24.862Z",
  "createdBy": "12345gfuJzo4k7F9",
  "modifiedBy": "12345xgfuJzo4k7F9"
}
```

---

## Users

### Get Workspace Users

```
GET /workspaces/{workspaceId}/users
```

**Response:**

```json
[
  {
    "id": "22YK3N5uGpzMdw7fm",
    "profile": { "firstName": "Vera", "lastName": "Morrisville" },
    "fullName": "Vera Morrisville",
    "email": "vera@example.com"
  }
]
```

---

## Groups

### Get Groups

```
GET /workspaces/{workspaceId}/groups
```

**Response:**

```json
[
  {
    "id": "8MRZ6oYzRMJ4eJYnR",
    "name": "Everyone",
    "members": ["1234abcuJzo4k7F9", "6789abcuJzo4k7F9"],
    "workspace": "12345aZjDQZndHqs",
    "createdAt": "2017-05-18T15:26:17.407Z",
    "createdBy": "1234abcuJzo4k7F9",
    "modifiedBy": "1234abcuJzo4k7F9"
  }
]
```

---

## Labels

### Create Label

```
POST /workspaces/{workspaceId}/labels
```

**Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | yes | Label name |
| `color` | string | yes | Hex color (e.g. `"#00CCCC"`) |
| `parent` | string | no | Parent label ID |

**Response:**

```json
{
  "_id": "qFR6a524nFARukmvF",
  "workspace": "12345aZjDQZndHqs",
  "name": "Label 1",
  "color": "#00CCCC",
  "parent": null,
  "createdAt": "2018-01-23T22:14:24.862Z",
  "modifiedAt": "2018-01-23T22:14:24.862Z",
  "createdBy": "12345gfuJzo4k7F9",
  "modifiedBy": "12345xgfuJzo4k7F9"
}
```

---

## Custom Tags

### Get Custom Tags

```
GET /workspaces/{workspaceId}/custom-tags?type={user|project}
```

**Response:**

```json
[
  {
    "_id": "qFR6a524nFARukmvF",
    "workspace": "12345aZjDQZndHqs",
    "name": "Custom Tag 1",
    "type": "user",
    "options": ["Option 1", "Option 2"],
    "isMulti": false,
    "createdAt": "2018-01-23T22:14:24.862Z",
    "modifiedAt": "2018-01-23T22:14:24.862Z"
  }
]
```

---

## Resource Assignments

### Update Resource Assignment

```
PUT /resource-assignments/{resourceAssignmentId}
```

**Body (all fields optional):**

| Field | Type | Description |
|-------|------|-------------|
| `startDate` | date | Start date |
| `endDate` | date | End date |
| `projectId` | string | Project ID |
| `notes` | string | Notes |
| `assignmentType` | string | `"regular"`, `"timeOff"`, or `"allocation"` |
| `allocationType` | string | `"hoursPerDay"` or `"fixedHours"` |
| `hoursPerDay` | integer | Hours per day |
| `fixedHours` | integer | Total fixed hours |
| `fixedDisplayType` | string | `"hours"` or `"days"` |

**Error:** Returns `400` with `"Resourcing is not enabled in current workspace"` if feature is disabled.

---

## Webhooks

### Create Webhook

```
POST /webhooks
```

**Body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | yes | Human-readable webhook name |
| `workspaceId` | string | yes | Workspace ID |
| `trigger` | string | yes | `"actions::i"`, `"actions::u"`, `"projects::i"`, `"projects::u"` |
| `url` | string | yes | URL to receive POST payloads |
| `fields` | string[] | no | Field names to filter on (empty = all fields) |
| `projectIds` | string[] | no | Scope to specific projects (actions only) |
| `additionalHeaders` | object[] | no | Custom HTTP headers for verification |

**Response (201):**

```json
{
  "message": "Webhook created",
  "webhook": {
    "_id": "v2Y3CNCDyzeHEeorr",
    "name": "Tell me when Projects are inserted",
    "workspaceId": "oQkqDmkXzoHwjatAA",
    "trigger": "projects::i",
    "url": "https://webhook.site/example",
    "projectIds": [],
    "fields": [],
    "ownerId": "9Mbh6keyT33iNN2xp",
    "deleted": false,
    "createdAt": "2023-09-27T15:21:14.839Z",
    "modifiedAt": "2023-09-27T15:21:14.839Z"
  }
}
```

### Delete Webhook

```
DELETE /webhooks/{webhookId}
```

**Response:** `{ "message": "Webhook deleted" }`

### Webhook Payload Format

When triggered, Hive sends a POST to your URL:

```json
{
  "trigger": "actions::u",
  "ownerId": "9Mbh6keyT33iNN2xp",
  "webhookId": "zhMJzqMTa8GKz3yqH",
  "action": { /* full action object */ }
}
```

For project triggers, the key is `"project"` instead of `"action"`.
