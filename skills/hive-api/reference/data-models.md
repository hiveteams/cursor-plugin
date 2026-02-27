# Hive REST API - Data Models

## Workspace

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| name | String | Workspace name |
| members | String[] | Member user IDs |
| createdAt | ISO Date | Creation timestamp |
| modifiedAt | ISO Date | Last modified timestamp |
| createdBy | String | Creator user ID |
| modifiedBy | String | Last modifier user ID |

## Action

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| title | String | Title of the action |
| workspace | String | Workspace ID the action belongs to |
| assignees | String[] | Array of User IDs (value `['none']` = unassigned) |
| projectId | String | Project ID (null if no project) |
| description | String | User input description |
| customFields | `[{label, value}]` | Action custom fields |
| createdAt | ISO Date | Creation timestamp |
| modifiedAt | ISO Date | Last modified timestamp |
| createdBy | String | User ID of creator |
| modifiedBy | String | User ID of last modifier |
| status | String | Status (e.g. "Unstarted", "In Progress", "Completed") |
| scheduledDate | ISO Date | Start date |
| deadline | ISO Date | Due date |
| parent | String | Parent action ID (null if top-level) |
| root | String | Highest-level action ID in tree |
| hasSubactions | Boolean | Whether action has sub-actions |
| estimate | Int32 | Estimated time in seconds (null if not set) |
| estimates | `[{userId, time}]` | Estimated time per assignee |
| loggedTime | `[{userId, time, date}]` | Time logged to action |
| milestone | Boolean | Whether action is a milestone |
| phaseId | String | Phase ID |
| phaseName | String | Phase name |
| archived | Boolean | Whether archived |
| deleted | Boolean | Whether deleted |
| checkedDate | ISO Date | Date marked "Completed" |
| completedBy | String | User ID who completed |
| placeholderAssignees | String[] | Placeholder IDs |
| agileStoryPoints | Number | Story points (max 233) |
| agileSprintId | String | Agile sprint ID |
| priority | `{name, level, color, _id}` | Priority object (appears in endpoint responses; not listed in the Action object table) |

## User

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| fullName | String | Full name |
| profile.firstName | String | First name |
| profile.lastName | String | Last name |
| email | String | Email address |

## Project

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| name | String | Project name |
| description | String | Optional description |
| endDate | ISO Date | End date |
| sharingType | String | "everyone", "custom", or "me" |
| members | String[] | User IDs (when sharingType = "custom") |
| projectCustomFields | `[{_id, type, label, value}]` | Project-level custom fields |
| createdAt | ISO Date | Creation timestamp |
| modifiedAt | ISO Date | Last modified timestamp |
| createdBy | String | Creator user ID |
| modifiedBy | String | Last modifier user ID |
| color | String | Hex color code |
| statusUpdates | Array | Project status updates |
| resourcePlaceholderIds | String[] | Placeholder IDs on project |
| budget | Number | Project budget |
| isDraftMode | Boolean | Whether in draft mode |

## Message

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| containerId | String | Chat Group ID |
| body | String | Message body |
| sender | String | Sender user ID |
| senderFirstname | String | Optional override display name |
| senderPicture | String | Optional override display image URL |
| workspace | String | Workspace ID |
| color | String | Background color (yellow, purple, green, red, gray) |
| createdAt | ISO Date | Creation timestamp |
| modifiedAt | ISO Date | Last modified timestamp |
| createdBy | String | Creator user ID |
| modifiedBy | String | Last modifier user ID |

## Label

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| workspace | String | Workspace ID |
| name | String | Label name |
| color | String | Label color |
| parent | String | Parent label ID |
| createdAt | Date | Creation date |
| createdBy | String | Creator user ID |
| modifiedAt | Date | Last modified date |
| modifiedBy | String | Last modifier user ID |

## Custom Field

| Field | Type | Description |
|-------|------|-------------|
| label | String | Field label |
| attachedToObject | String | Object type this field relates to |
| type | String | "text", "date", "project", "formula", "user", "select" |
| dropdownValues | String[] | Options for select fields |
| allowMultiSelect | Boolean | Whether multi-select is enabled |
| formula | String | Formula definition (for formula type) |
| workspace | String | Workspace ID |
| deleted | Boolean | Whether deleted |
| createdAt | Date | Creation date |
| modifiedAt | Date | Last modified date |
| createdBy | String | Creator user ID |
| modifiedBy | String | Last modifier user ID |

## Custom Tag

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| name | String | Tag name |
| options | String[] | Available tag options |
| type | String | "user" or "project" |
| isMulti | Boolean | Whether multi-select allowed |
| createdAt | Date | Creation date |
| createdBy | String | Creator user ID |
| modifiedAt | Date | Last modified date |
| modifiedBy | String | Last modifier user ID |

## File Attachment

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| name | String | File name |
| workspace | String | Workspace ID |
| url | String | File URL |
| createdAt | ISO Date | Creation timestamp |
| modifiedAt | ISO Date | Last modified timestamp |
| createdBy | String | Uploader user ID |
| modifiedBy | String | Last modifier user ID |

## Team

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| name | String | Team name |
| members | String[] | Member user IDs |
| workspace | String | Workspace ID |

## Project Tag

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| projectId | String | Project ID this tag belongs to |
| name | String | Tag name |
| options | String[] | Available options |
| selectedOptions | String[] | Currently selected options |
| isMulti | Boolean | Whether multi-select allowed |

## User Tag

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| userId | String | User ID this tag belongs to |
| name | String | Tag name |
| options | String[] | Available options |
| selectedOptions | String[] | Currently selected options |
| isMulti | Boolean | Whether multi-select allowed |

## Role Tag

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| workspace | String | Workspace ID |
| name | String | Role name |
| createdAt | Date | Creation date |
| createdBy | String | Creator user ID |
| modifiedAt | Date | Last modified date |
| modifiedBy | String | Last modifier user ID |

## Resource Assignment

| Field | Type | Description |
|-------|------|-------------|
| id | String | Unique ID |
| workspace | String | Workspace ID |
| resourceId | String | User or placeholder ID |
| projectId | String | Project ID |
| startDate | ISO Date | Start date |
| endDate | ISO Date | End date |
| allocationType | String | "hoursPerDay" or "fixedHours" |
| assignmentType | String | "regular", "timeOff", or "allocation" |
| hoursPerDay | Integer | Hours per day |
| fixedHours | Integer | Total fixed hours |
| fixedDisplayType | String | "hours" or "days" |
| notes | String | Notes |

## User Setting

| Field | Type | Description |
|-------|------|-------------|
| _id | String | Unique ID |
| workspaceId | String | Workspace ID |
| userId | String | User ID |
| firstDayOfWork | Date | First work day |
| lastDayOfWork | Date | Last work day |
| billRate | Number | Billing rate |
| costRate | Number | Cost rate |
| managers | String[] | User IDs of managers |

## Webhook

| Field | Type | Description |
|-------|------|-------------|
| _id | String | Unique ID |
| name | String | Webhook name |
| ownerId | String | Owner user ID |
| workspaceId | String | Workspace ID |
| projectIds | String[] | Project IDs to watch (empty = all) |
| trigger | String | Event type (see Webhooks guide) |
| fields | String[] | Fields to watch (empty = all) |
| filters | Object[] | Conditional filters (not yet publicly supported) |
| operator | String | Filter operator (not yet publicly supported) |
| url | String | Payload destination URL |
| additionalHeaders | Object[] | Extra HTTP headers |
| deleted | Boolean | Whether deleted |
| createdAt | ISO Date | Creation timestamp |
| modifiedAt | ISO Date | Last modified timestamp |
| createdBy | String | Creator user ID |
| modifiedBy | String | Last modifier user ID |
