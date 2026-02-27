# Hive REST API - Endpoint Details

Base: `https://app.hive.com/api/v1` | Auth: `?user_id=USER_ID` + header `api_key: API_KEY`

---

## Workspace List Endpoints

### GET `/workspaces/{workspaceId}/actions` - Get actions

| Query Param | Type | Default | Description |
|------------|------|---------|-------------|
| projectId | String | - | Filter by project |
| sortBy | String | - | Sort by field (e.g. `title asc`) |
| limit | String | "100" | Results per page (min 1, max 100) |
| filters | String | - | Filter by fields: `filters[status]=Completed`. Supported: status, parent, archived, milestone, deleted, root, recurringId, teamAssignee, placeholderAssignees, priorityLevelId, followingUserIds |

### GET `/workspaces/{workspaceId}/projects` - Get projects

| Query Param | Type | Default | Description |
|------------|------|---------|-------------|
| sortBy | String | - | Sort by field (e.g. `title+asc`) |
| filters | String | - | Filter: `filters[archived]=true`. Supported: archived, deleted |

### GET `/workspaces/{workspaceId}/users` - Get workspace users

Returns array of user objects for the workspace.

---

## Actions

### GET `/actions/{actionId}` - Get action

Returns full action object. `estimate` is in seconds (null if not set).

### POST `/actions/create` - Create action

| Body Field | Type | Required | Description |
|-----------|------|----------|-------------|
| workspace | String | Yes | Workspace ID |
| title | String | Yes | Action title |
| description | String | No | Action description |
| projectId | String | No | Project to assign to |
| assignees | String[] | No | User IDs (defaults to request user) |
| labels | String[] | No | Label IDs |
| deadline | String | No | Due date (yyyy/mm/dd) |
| scheduledDate | String | No | Start date (yyyy/mm/dd) |
| processId | String | No | Action template ID to apply |
| customFields | `[{label, value}]` | No | Custom field values |
| parentId | String | No | Parent action ID |
| phaseId | String | No | Phase ID (takes precedence over phaseName) |
| phaseName | String | No | Phase name |
| milestone | Boolean | No | Whether action is a milestone |

### PUT `/actions/{actionId}` - Update action

| Body Field | Type | Description |
|-----------|------|-------------|
| status | String | New status |
| update_children | Boolean | Also update children status (default true) |
| title | String | New title |
| projectId | String | Assign to project |
| assignees | String[] | User IDs |
| labels | String[] | Label IDs |
| description | String | HTML description (h1, h2, a, b, u tags) |
| urgent | Boolean | Urgency state |
| privacy | String | "private" or "public" |
| checked | Boolean | Checked state |
| scheduledDate | Date | Start date |
| deadline | Date | End date |
| parent | String | New parent action ID |
| customFields | `[{label, value}]` | Text custom fields only |
| shiftSubactionsDeadline | Boolean | Shift subaction dates by same offset |
| archived | Boolean | Archive state |
| phaseId | String | Phase ID |
| phaseName | String | Phase name |
| followingUserIds | String[] | Follower user IDs |
| agileStoryPoints | Integer | Story points (max 233) |
| agileSprintId | String | Sprint ID |
| milestone | Boolean | Milestone state |

### DELETE `/actions/{actionId}` - Delete action

Returns `{ message: "Action successfully deleted" }`.

### GET `/actions/{actionId}/comments` - Get comments

| Query Param | Type | Default | Description |
|------------|------|---------|-------------|
| limit | Integer | 200 | Number of comments |
| sortBy | String | "createdAt+desc" | Sort order |

Returns array of `{ id, body, workspace, attachments, mentions, createdBy, createdAt, reactions }`.

### POST `/actions/{actionId}/comments` - Create comment

| Body Field | Type | Description |
|-----------|------|-------------|
| body | String | Comment body text |

### GET `/actions/{actionId}/action-history` - Get history

Returns array of `{ id, body, actionId, date }`.

### GET `/actions/{actionId}/attachments` - Get attachments

Returns array of file attachment objects. Only direct uploads, not 3rd-party or comment attachments.

### POST `/actions/{actionId}/attachments` - Create attachment

| Body Field | Type | Description |
|-----------|------|-------------|
| url | String | File URL |
| filename | String | Optional filename with extension |

### POST `/actions/{actionId}/apply-template` - Apply template

| Body Field | Type | Required | Description |
|-----------|------|----------|-------------|
| processId | String | Yes | Action template (workflow) ID |

---

## Projects

### POST `/projects` - Create project

| Body Field | Type | Required | Description |
|-----------|------|----------|-------------|
| workspace | String | Yes | Workspace ID |
| name | String | Yes | Project name |
| description | String | No | Project description |
| startDate | Date | No | Start date |
| endDate | Date | No | End date |
| sharingType | String | No | "everyone" (default), "custom", or "me" |
| members | String[] | No | User IDs (for sharingType "custom") |
| teams | String[] | No | Team IDs (for sharingType "custom") |
| projectCustomFields | `[{label, type, value, ...}]` | No | Custom fields (types: text, number, date, user, project, select, formula) |
| color | String | No | Hex color code |
| template | Boolean | No | Create as template (default false) |
| copyFrom | String | No | Project ID to copy from |
| copyActionStatuses | Boolean | No | Retain action statuses when copying |
| copyAssignees | Boolean | No | Retain assignees when copying |
| accessOption | String | No | "private" (default) or "public" |
| phases | String[] | No | Phase names to create |
| parentProject | String | No | Parent project ID |
| budget | Integer | No | Budget value |

### PUT `/projects/{projectId}` - Update project

| Body Field | Type | Description |
|-----------|------|-------------|
| name | String | Project name |
| description | String | Project description |
| startDate | Date | Start date (null to unset) |
| endDate | Date | End date (null to unset) |
| color | String | Hex color code |
| accessOption | String | "public" or "private" |
| parentProject | String | Parent project ID |
| sharingType | String | "everyone", "custom", or "me" |
| members | String[] | Member user IDs |
| teams | String[] | Team IDs |
| archived | Boolean | Archive state |
| template | Array/String | Template ID(s) to apply, with optional importWith settings |
| budget | Integer | Budget value |
| isDraftMode | Boolean | Draft mode state |

### DELETE `/projects/{projectId}` - Delete project

Returns `{ message: "Project was deleted successfully" }`.

---

## Messages

### POST `/messages/create` - Create message

| Body Field | Type | Description |
|-----------|------|-------------|
| workspace | String | Workspace ID |
| body | String | Message body |
| senderName | String | Override sender display name |
| senderPicture | String | Override sender image URL |
| containerId | String | Chat Group ID to post in |
| color | String | Background: yellow, purple, green, red, gray |

---

## Users & Workspace

### GET `/users/{userId}` - Get user by ID

### GET `/users?email=EMAIL` - Get users by email

Returns array of user objects.

### POST `/workspaces/{workspaceId}/users` - Invite user

| Body Field | Type | Required | Description |
|-----------|------|----------|-------------|
| email | String | Yes | Email address |
| fullName | String | No | Full name |
| shouldSendInvite | Boolean | No | Send invite email (default true) |
| isExternal | Boolean | No | Invite as external (default false) |
| projectIds | String[] | No | Projects to invite into (required for external) |

### DELETE `/workspaces/{workspaceId}/users` - Remove user

| Body Field | Type | Description |
|-----------|------|-------------|
| userId | String | User ID to remove |

Returns 204 on success.

### GET `/workspaces/{workspaceId}/user-settings/{userId}` - Get user settings

Returns `{ workspaceId, _id, userId, firstDayOfWork, lastDayOfWork, billRate, costRate }`.

### GET `/workspaces/{workspaceId}/external-users` - Get external users

### GET `/workspaces/{workspaceId}/removed-users` - Get removed users

---

## Labels

### GET `/labels?workspaceId=ID` - Get all labels

### GET `/labels/{labelId}` - Get label

### POST `/labels` - Create label

| Body Field | Type | Description |
|-----------|------|-------------|
| workspace | String | Workspace ID |
| name | String | Label name |
| color | String | Label color |
| parent | String | Parent label ID |

### DELETE `/labels/{labelId}` - Delete label

---

## Custom Fields

### GET `/custom-fields?workspaceId=ID` - Get custom fields

### POST `/custom-fields` - Create custom field

| Body Field | Type | Description |
|-----------|------|-------------|
| workspace | String | Workspace ID |
| label | String | Field label |
| type | String | "text", "date", "project", "formula", "user", "select" |
| attachedToObject | String | Object type |
| dropdownValues | String[] | Options for select type |
| allowMultiSelect | Boolean | Enable multi-select |

---

## Custom Tags

### GET `/custom-tags?workspaceId=ID` - Get custom tags

### POST `/custom-tags/create` - Create custom tag

| Body Field | Type | Description |
|-----------|------|-------------|
| workspace | String | Workspace ID |
| name | String | Tag name |
| type | String | "user" or "project" |
| options | String[] | Available options |
| isMulti | Boolean | Allow multi-select |

### GET `/custom-tags/{customTagId}` - Get custom tag

### PUT `/custom-tags/{customTagId}` - Update custom tag

### DELETE `/custom-tags/{customTagId}` - Delete custom tag

---

## Teams

### GET `/teams/{teamId}` - Get team

### POST `/teams` - Create team

| Body Field | Type | Description |
|-----------|------|-------------|
| workspace | String | Workspace ID |
| name | String | Team name |
| members | String[] | User IDs |

### DELETE `/teams/{teamId}` - Delete team

### POST `/teams/{teamId}/add-members` - Add members

| Body Field | Type | Description |
|-----------|------|-------------|
| members | String[] | User IDs to add |

---

## Files & Proofing

### GET `/files/{fileId}` - Get file

### GET `/actions/{actionId}/versioned-files` - Get versioned files

### POST `/actions/{actionId}/versioned-files` - Create versioned file

### POST `/versioned-files/{versionedFileId}/versions` - Add file version

### GET `/proofing-files/{proofingFileId}` - Get proofing file

---

## Resource Assignments

### GET `/resource-assignments/{resourceAssignmentId}` - Get assignment

### GET `/resource-assignments?workspaceId=ID` - Get assignments

### POST `/resource-assignments` - Create assignment

| Body Field | Type | Required | Description |
|-----------|------|----------|-------------|
| workspace | String | Yes | Workspace ID |
| resourceId | String | Yes | User ID |
| startDate | Date | Yes | Start date |
| endDate | Date | Yes | End date |
| assignmentType | String | Yes | "regular", "timeOff", or "allocation" |
| projectId | String | No | Project ID |
| notes | String | No | Notes |
| allocationType | String | No | "hoursPerDay" or "fixedHours" |
| hoursPerDay | Integer | No | Hours per day |
| fixedHours | Integer | No | Total hours |
| fixedDisplayType | String | No | "hours" or "days" |

### DELETE `/resource-assignments/{resourceAssignmentId}` - Delete assignment

---

## Project Statuses

### GET `/project-statuses?workspaceId=ID` - Get statuses

### GET `/project-statuses/{statusId}` - Get status

### POST `/project-statuses` - Create status

---

## Webhooks

### POST `/webhooks` - Create webhook

| Body Field | Type | Required | Description |
|-----------|------|----------|-------------|
| name | String | Yes | Webhook name |
| workspaceId | String | Yes | Workspace ID |
| trigger | String | Yes | Event type (see Webhooks guide) |
| url | String | Yes | Destination URL |
| projectIds | String[] | No | Project IDs to watch (empty = all) |
| fields | String[] | No | Fields to watch (empty = all) |
| additionalHeaders | Object[] | No | Extra HTTP headers |

### DELETE `/webhooks/{webhookId}` - Delete webhook
