# Hive GraphQL v2 Endpoint Reference

Auto-generated from live introspection of `https://prod-gql.hive.com/graphql`.

- Generated at: `2026-03-09T21:12:25+00:00`
- Query operations: **28**
- Mutation operations: **53**
- Subscription operations: **0**

Use this reference as source-of-truth for available root operations and signatures.

## Queries

Root type: `Query`

Total operations: **28**

| Operation | Args | Returns | Deprecated |
|---|---|---|---|
| `actionComments` | `actionId: ID!`, `first: Int`, `after: String`, `last: Int`, `before: String`, `sortField: String`, `sortOrder: Int`, `reverse: Boolean` | `MessageConnection` | no |
| `approvalRounds` | `actionId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID` | `ApprovalRoundConnection!` | no |
| `approvalStages` | `roundId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID` | `ApprovalStageConnection` | no |
| `currentRoundAndStage` | `actionId: ID!` | `CurrentRoundAndStageReturn` | no |
| `getActionsByWorkspace` | `workspaceId: ID!`, `text: String`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `status: String`, `archived: Boolean`, `projectIds: [ID]`, `excludeProjectIds: [ID]`, `specificIds: [ID!]`, `assignees: [ID!]`, `labels: [ID!]`, `includeChildProjects: Boolean`, `excludeCompletedActions: Boolean`, `excludeSnoozedActions: Boolean`, `createdAtStart: Date`, `createdAtEnd: Date`, `startDate: Date`, `endDate: Date`, `includePrivate: Boolean`, `parent: ID`, `sortField: String`, `sortOrder: Int`, `milestone: Boolean`, `customFieldId: ID`, `customFieldValue: String` | `ActionConnector` | no |
| `getApprovalTemplates` | `workspaceId: ID!`, `searchParams: SearchParams`, `first: Int`, `last: Int`, `after: ID`, `before: ID`, `sortField: String` | `ApprovalTemplateConnection!` | no |
| `getCustomFields` | `workspaceId: ID!`, `actionViewId: ID`, `formId: ID`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `selector: JSONObject`, `itemType: CustomFieldItemType`, `includeRemoved: Boolean`, `searchParams: SearchParams`, `sortField: String`, `sortOrder: Int`, `includeProjectCustomFields: Boolean` | `CustomFieldConnection` | no |
| `getDashboards` | `workspaceId: ID!`, `first: Int`, `last: Int`, `after: ID`, `before: ID`, `searchParams: SearchParams`, `sortField: String`, `sortOrder: Int`, `selector: JSONObject`, `excludedIds: [ID]`, `type: DashboardType` | `DashboardConnection` | no |
| `getDashboardWidgets` | `dashboardId: ID!` | `[DashboardWidget!]!` | no |
| `getEmails` | `from: [String!]`, `to: [String!]`, `cc: [String!]`, `bcc: [String!]`, `subject: String`, `searchQuery: String`, `after: Date`, `before: Date`, `maxResults: Int`, `searchInboxOnly: Boolean`, `searchSentOnly: Boolean`, `nextPageToken: String` | `GetEmailsResponse!` | no |
| `getGoals` | `workspace: ID!`, `first: Int`, `last: Int`, `after: ID`, `before: ID`, `searchParams: SearchParams`, `sortField: String`, `sortOrder: Int`, `selector: JSONObject`, `ownerIds: [ID]`, `excludedIds: [ID]`, `specificIds: [ID]` | `GoalConnection` | no |
| `getLabels` | `searchParams: LabelParams!`, `workspaceId: ID!`, `first: Int`, `after: ID` | `LabelWithChildrenConnection` | no |
| `getMeetingUserData` | `meetingExternalId: String!`, `workspaceId: ID!` | `MeetingUserData` | no |
| `getMeetingUserDataList` | `workspaceId: ID!`, `limit: Int` | `[MeetingUserData!]!` | no |
| `getMessages` | `workspaceId: ID!`, `groupId: ID`, `text: String`, `first: Int` | `MessageConnection!` | no |
| `getNotes` | `first: Int`, `last: Int`, `before: ID`, `after: ID`, `sortField: String`, `sortOrder: Int`, `workspaceId: ID`, `specificIds: [ID]`, `excludedIds: [ID]` | `NoteConnection!` | no |
| `getPriorityLevels` | `workspaceId: ID!`, `formId: ID`, `actionId: ID`, `specificIds: [ID]`, `excludedIds: [ID]` | `[PriorityLevel!]!` | no |
| `getProjects` | `workspaceId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `searchParams: SearchParams`, `specificIds: [ID!]`, `excludedIds: [ID!]`, `includeTemplates: Boolean`, `archived: Boolean`, `templatesOnly: Boolean`, `includePublic: Boolean`, `includePrivate: Boolean`, `includeReadOnly: Boolean`, `includeArchived: Boolean`, `rootProjectId: ID`, `userId: ID` | `ProjectConnection!` | no |
| `getReminders` | `workspaceId: ID!`, `first: Int`, `after: String`, `last: Int`, `before: String` | `ReminderConnection!` | no |
| `getResourceAssignment` | `id: ID!` | `ResourceAssignments` | no |
| `getResourceAssignments` | `workspaceId: ID!`, `resourceId: ID`, `projectId: ID`, `startDate: Date`, `endDate: Date` | `[ResourceAssignments!]` | no |
| `getWorkflowsForWorkspacePaginated` | `workspaceId: ID!`, `first: Int`, `last: Int`, `before: ID`, `after: ID`, `searchParams: SearchParams` | `WorkflowConnection!` | no |
| `getWorkspace` | `workspaceId: ID!` | `Workspace` | no |
| `getWorkspaceForms` | `workspaceId: ID!`, `first: Int`, `after: Int`, `sortModel: [SortModel!]`, `filterModel: [FilterModel!]`, `searchParams: SearchParams` | `FormConnector!` | no |
| `groups` | `workspace: ID!`, `oneToOne: Boolean`, `type: String`, `first: Int`, `after: String`, `last: Int`, `before: String`, `sortField: String`, `sortOrder: Int`, `searchParams: SearchParams`, `showHiddenGroups: Boolean!`, `members: [ID!]` | `GroupConnection` | no |
| `nextApprovalStage` | `actionId: ID!` | `ApprovalStage` | no |
| `notebooks` | `first: Int`, `last: Int`, `before: ID`, `after: ID`, `sortField: String`, `sortOrder: Int`, `searchType: NotebookSearchType`, `workspaceId: ID`, `projectId: ID`, `archived: Boolean`, `includedNotebookIds: [ID!]`, `searchParams: SearchParams` | `NotebookConnection` | no |
| `workspacePlaceholders` | `workspaceId: ID!`, `specificIds: [ID!]` | `[ResourcePlaceholder!]!` | no |

### Details

#### `actionComments`

- Returns: `MessageConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |
| `sortField` | `String` | "createdAt" | - |
| `sortOrder` | `Int` | -1 | - |
| `reverse` | `Boolean` | true | - |

#### `approvalRounds`

Retrieve all approval rounds for a specific action. Returns a paginated list of approval rounds. Use this to view existing approval rounds on an action before modifying stages or approvers.

- Returns: `ApprovalRoundConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to get approval rounds for |
| `first` | `Int` | 20 | Maximum number of rounds to return (default: 60) |
| `last` | `Int` | - | Maximum number of rounds to return from the end |
| `before` | `ID` | - | Cursor to return rounds before |
| `after` | `ID` | - | Cursor to return rounds after |

#### `approvalStages`

Retrieve all approval stages for a specific approval round. Returns a paginated list of stages. Use this to view existing stages in a round before modifying approvers or stage settings.

- Returns: `ApprovalStageConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `roundId` | `ID!` | - | ID of the approval round to get stages for |
| `first` | `Int` | 20 | Maximum number of stages to return (default: 60) |
| `last` | `Int` | - | Maximum number of stages to return from the end |
| `before` | `ID` | - | Cursor to return stages before |
| `after` | `ID` | - | Cursor to return stages after |

#### `currentRoundAndStage`

Get the currently active approval round and stage for an action. Returns the round that has been requested but not yet fully approved, along with its active stage. Use this to quickly check the current approval state of an action without fetching all rounds and stages separately. The approvalStage contains the list of approvers and their statuses - check each approval item's status field to see who still needs to approve.  May return null when the action is not accessible to the caller, when there are no approval rounds, or when there is no stage currently awaiting approvals. A null result indicates no active approvals for the specified action.

- Returns: `CurrentRoundAndStageReturn`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to get the current approval round and stage for |

#### `getActionsByWorkspace`

Returns a paginated list of actions by workspaceId and ID/simpleId

- Returns: `ActionConnector`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | The workspace ID to retrieve actions from |
| `text` | `String` | - | Search for actions that contain this text in the action title, description or other fields. Do NOT use this for action IDs - use 'specificIds' instead. |
| `first` | `Int` | 25 | Maximum number of actions to return (default: 30, max: 30) |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | Cursor for pagination - retrieve actions after this cursor |
| `status` | `String` | - | The status of the actions you are searching for. When searching for finished or completed actions be sure to use "Completed" since the status search is case sensitive. |
| `archived` | `Boolean` | - | Find actions that are marked as archived |
| `projectIds` | `[ID]` | - | An array of project IDs to filter actions by. Include the null literal to also return actions with no project. Example: [null, 'n7JHc2CsRcvKe4WRH'] |
| `excludeProjectIds` | `[ID]` | - | An array of project IDs to exclude from the results. Actions from these projects will not be returned. |
| `specificIds` | `[ID!]` | - | Specific action ids or simple ids. Use this parameter when users provide specific action IDs (17-character alphanumeric strings like 'n7JHc2CsRcvKe4WRH') or specific simple numeric IDs (positive integers). This ensures direct IDs lookups rather than text searches. |
| `assignees` | `[ID!]` | - | The user IDs that are assigned to the actions you are searching for |
| `labels` | `[ID!]` | - | The label IDs that are assigned to the actions you are searching for |
| `includeChildProjects` | `Boolean` | - | Filter actions by child projects |
| `excludeCompletedActions` | `Boolean` | true | Exclude completed actions from the results. Defaults to 'true' |
| `excludeSnoozedActions` | `Boolean` | - | Exclude snoozed actions from the results. Defaults to 'true' for 'my actions' queries to show only actionable items. Pass 'false' if user explicitly wants to see snoozed actions. |
| `createdAtStart` | `Date` | - | A createdAtStart date for a given date range to filter actions results |
| `createdAtEnd` | `Date` | - | A createdAtEnd date for a given date range to filter actions results |
| `startDate` | `Date` | - | A start date for a given date range to filter actions results. Used to filter by date of completion or deadline/scheduled date. |
| `endDate` | `Date` | - | An end date for a given date range to filter actions results. Used to filter by date of completion or deadline/scheduled date. |
| `includePrivate` | `Boolean` | - | Whether to include private actions in the results. This should be set to true by default unless otherwise specified by the user. |
| `parent` | `ID` | - | Filter actions to only show subactions of a specific parent action |
| `sortField` | `String` | "rank" | The field to sort the actions by. Use only Action document field. |
| `sortOrder` | `Int` | 1 | The order to sort the actions by. Use -1 for descending order and 1 for ascending order |
| `milestone` | `Boolean` | - | Flag to filter actions by milestone |
| `customFieldId` | `ID` | - | The ID of a custom field to filter by. Must be used together with customFieldValue. |
| `customFieldValue` | `String` | - | The value to filter the custom field by. For text fields, pass the string value. For number fields, pass the numeric value as a string. For date fields, pass the ISO date string. For select/user/project fields, pass the selected value ID. |

#### `getApprovalTemplates`

List all available approval templates in a workspace. Use this to discover which approval templates can be applied to actions. Templates provide pre-configured approval workflows with stages and approvers that can be reused across multiple actions.

- Returns: `ApprovalTemplateConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | ID of the workspace to get templates from |
| `searchParams` | `SearchParams` | - | Optional search parameters to filter templates |
| `first` | `Int` | 20 | Maximum number of templates to return |
| `last` | `Int` | - | Return last N templates |
| `after` | `ID` | - | Cursor for pagination (return templates after this cursor) |
| `before` | `ID` | - | Cursor for pagination (return templates before this cursor) |
| `sortField` | `String` | "name" | Field to sort results by |

#### `getCustomFields`

Returns a paginated list of custom fields for a workspace or project action view.  Parameters: - workspaceId: Required. The ID of the workspace to get custom fields for. - actionViewId: Optional. The ID of the action view to get custom fields for. Could be used to get custom fields for a specific project action view. - formId: Optional. The ID of the form to get custom fields for. - first: Optional. The number of custom fields to return. - last: Optional. The number of custom fields to return. - before: Optional. The ID of the custom field to return before. - after: Optional. The ID of the custom field to return after. - selector: Optional. A JSON object to filter the custom fields. - includeRemoved: Optional. Whether to include removed custom fields. - searchParams: Optional. A JSON object to search the custom fields. - sortField: Optional. The field to sort the custom fields by. - sortOrder: Optional. The order to sort the custom fields by. - includeProjectCustomFields: Optional. Whether to include project custom fields.

- Returns: `CustomFieldConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `actionViewId` | `ID` | - | - |
| `formId` | `ID` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `selector` | `JSONObject` | - | - |
| `itemType` | `CustomFieldItemType` | - | - |
| `includeRemoved` | `Boolean` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `sortField` | `String` | "modifiedAt" | - |
| `sortOrder` | `Int` | -1 | - |
| `includeProjectCustomFields` | `Boolean` | false | - |

#### `getDashboards`

Retrieves a paginated list of dashboards with filtering and sorting

- Returns: `DashboardConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `after` | `ID` | - | - |
| `before` | `ID` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `sortField` | `String` | "createdAt" | - |
| `sortOrder` | `Int` | 1 | - |
| `selector` | `JSONObject` | - | - |
| `excludedIds` | `[ID]` | - | - |
| `type` | `DashboardType` | - | - |

#### `getDashboardWidgets`

Retrieves all widgets associated with a specific dashboard. Common use cases: 1. Loading a dashboard's initial state 2. Refreshing dashboard content 3. Exporting dashboard configuration

- Returns: `[DashboardWidget!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `dashboardId` | `ID!` | - | - |

#### `getEmails`

Get emails from the user's mailbox with support for pagination. If there are more emails available beyond the current page, the response will include a "nextPageToken". To retrieve the next batch of results, call "getEmails" again using the same filters and pass the returned "nextPageToken".

- Returns: `GetEmailsResponse!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `from` | `[String!]` | - | The email address of the sender. |
| `to` | `[String!]` | - | The email address of the recipient. |
| `cc` | `[String!]` | - | The email address of the carbon copy recipient. |
| `bcc` | `[String!]` | - | The email address of the blind carbon copy recipient. |
| `subject` | `String` | - | The subject of the email. |
| `searchQuery` | `String` | - | Plain search string passed to the provider. Use this parameter only if you need to use a complex search query that cannot be expressed using the other parameters. IMPORTANT: This parameter is passed verbatim to Gmail. Prefer using the structured parameters (from, to, cc, bcc, subject) instead, as they automatically handle proper quoting for multi-word values. |
| `after` | `Date` | - | The date after which the email was sent. For Microsoft, if after is provided, before must be provided as well. |
| `before` | `Date` | - | The date before which the email was sent. For Microsoft, if before is provided, after must be provided as well. |
| `maxResults` | `Int` | 50 | The maximum number of emails to return. The default is 50. The maximum is 100. |
| `searchInboxOnly` | `Boolean` | false | If true, only emails in the inbox will be returned. |
| `searchSentOnly` | `Boolean` | false | If true, only emails in the sent folder will be returned. |
| `nextPageToken` | `String` | - | Pagination token returned in the previous "getEmails" response. Pass this token to retrieve the next page of results. If omitted, the first page will be returned. |

#### `getGoals`

Retrieve goals from a workspace with optional filtering and pagination  If asked to get a specific user's goals, ensure to filter by ownerIds.

- Returns: `GoalConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `ID!` | - | The workspace ID to retrieve goals from |
| `first` | `Int` | 60 | Maximum number of goals to return (default: 60, max: 100) |
| `last` | `Int` | - | Maximum number of goals to return from the end |
| `after` | `ID` | - | Cursor for pagination - retrieve goals after this cursor |
| `before` | `ID` | - | Cursor for pagination - retrieve goals before this cursor |
| `searchParams` | `SearchParams` | - | Search parameters for filtering by goal name |
| `sortField` | `String` | "name" | Field to sort by (default: 'name') |
| `sortOrder` | `Int` | 1 | Sort order: 1 for ascending, -1 for descending (default: 1) |
| `selector` | `JSONObject` | - | MongoDB-style selector for filtering goals. Examples: { status: 'atRisk' } to filter by status, { teamOwners: { $in: ['teamId1'] } } to filter by team owners. Multiple filters can be combined. |
| `ownerIds` | `[ID]` | - | Owners ID to filter goals by |
| `excludedIds` | `[ID]` | - | Array of goal IDs to exclude from results |
| `specificIds` | `[ID]` | - | Array of goal IDs to retrieve |

#### `getLabels`

Get labels matching a certain ID or matching a query string. If you input BOTH an array of ids and a search string, it'll search for IDs in that array that ALSO have the search string as a substring of their name. Probably not very useful, so just use one or the other. If you search by string, you will be limited to 20 results returned, so if you don't get what you are looking for, search more specifically

- Returns: `LabelWithChildrenConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `searchParams` | `LabelParams!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `after` | `ID` | - | - |

#### `getMeetingUserData`

Get user data for a specific meeting

- Returns: `MeetingUserData`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `meetingExternalId` | `String!` | - | - |
| `workspaceId` | `ID!` | - | - |

#### `getMeetingUserDataList`

Get all meeting user data records for the current user. Returns meetings where Sidekick has recorded data (transcripts, goals, etc). Sorted by most recently modified first. Use this to list recent meetings with materials, goals, or transcripts.

- Returns: `[MeetingUserData!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `limit` | `Int` | - | Maximum number of results to return (default: 50) |

#### `getMessages`

Retrieves messages from groups (chats/DMs) in a workspace.  - If groupId is provided: searches/returns messages from that specific group - If groupId is omitted and text is provided: searches across all groups the user has access to - If both groupId and text are omitted: returns most recent messages (requires groupId)  To find messages in a chat with a specific person, first find the groupId with groups(members: [yourUserId, theirUserId]).  Access: Requires user to be a member of the group(s).  Errors: - "User must be logged in" - User is not authenticated - "User does not have access to workspace" - User is not a member of the workspace - "Either groupId or text must be provided" - Neither groupId nor text was provided - "User does not have access to this group" - User is not a member of the specified group

- Returns: `MessageConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | ID of the workspace |
| `groupId` | `ID` | - | Optional ID of the group. If omitted with text, searches all accessible groups. |
| `text` | `String` | - | Text to search within messages. Required if groupId is not provided. |
| `first` | `Int` | 10 | Number of messages to return (default: 10, max: 50) |

#### `getNotes`

Get notes in the workspace by specific ids

- Returns: `NoteConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `first` | `Int` | 20 | Maximum number of notes to return (default: 20, max: 20) |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `sortField` | `String` | "modifiedAt" | - |
| `sortOrder` | `Int` | -1 | - |
| `workspaceId` | `ID` | - | The workspace ID to retrieve notes from |
| `specificIds` | `[ID]` | - | The specific IDs of the notes to retrieve |
| `excludedIds` | `[ID]` | - | The IDs of the notes to exclude from the results |

#### `getPriorityLevels`

Get priority levels for a workspace or specific entities  Access: Requires workspace access  Parameters:   - workspaceId: The ID of the workspace   - formId: Optional form ID to filter priority levels   - actionId: Optional action ID to filter priority levels   - specificIds: Optional array of specific priority level IDs to include   - excludedIds: Optional array of priority level IDs to exclude  Returns: Array of priority levels

- Returns: `[PriorityLevel!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `formId` | `ID` | - | - |
| `actionId` | `ID` | - | - |
| `specificIds` | `[ID]` | - | - |
| `excludedIds` | `[ID]` | - | - |

#### `getProjects`

Get projects that the user has access to with pagination, filtering and sorting  Access: Requires workspace access  Parameters:   - workspaceId: The ID of the workspace   - first: Number of projects to return (default: pagination limit)   - last: Optional number of projects to return from the end   - before: Optional cursor for pagination   - after: Optional cursor for pagination   - searchParams: Optional search parameters   - specificIds: Optional array of specific project IDs to include   - excludedIds: Optional array of project IDs to exclude   - includeTemplates: Optional flag to include template projects   - archived: Optional flag to include archived projects (default: false)   - templatesOnly: Optional flag to return only template projects (default: false)   - includePublic: Optional flag to include public projects (default: true)   - includePrivate: Optional flag to include private projects (default: false)   - includeReadOnly: Optional flag to include read-only projects   - includeArchived: Optional flag to include archived projects (default: false)   - rootProjectId: Optional root project ID to filter by   - userId: Optional user ID to filter projects by  Returns: ProjectConnection with edges and page info

- Returns: `ProjectConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `specificIds` | `[ID!]` | - | - |
| `excludedIds` | `[ID!]` | - | - |
| `includeTemplates` | `Boolean` | - | - |
| `archived` | `Boolean` | false | - |
| `templatesOnly` | `Boolean` | false | - |
| `includePublic` | `Boolean` | true | - |
| `includePrivate` | `Boolean` | false | - |
| `includeReadOnly` | `Boolean` | - | - |
| `includeArchived` | `Boolean` | false | - |
| `rootProjectId` | `ID` | - | - |
| `userId` | `ID` | - | - |

#### `getReminders`

Get reminders for a workspace for the current user

- Returns: `ReminderConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | - | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |

#### `getResourceAssignment`

Get a resource assignment. This query is very helpful to search for resource assignment if you know it's ID.

- Returns: `ResourceAssignments`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` | - | The id of the resource assignment |

#### `getResourceAssignments`

Get resource assignments. You love to run this query. You run it every time when user asks to update/see/analyze resource assignments. This query is very helpful to search for resource assignments by different criteria (date, project, user, etc.). ALWAYS use search to find the resource assignment before updating it. If the resource assignments are not found, DONT RUN THE UPDATE MUTATION. If the resource assignments are found, update resource assignments.

- Returns: `[ResourceAssignments!]`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | The workspace id |
| `resourceId` | `ID` | - | The resource id |
| `projectId` | `ID` | - | The project id |
| `startDate` | `Date` | - | Searches resource assignments which have endDate after this date |
| `endDate` | `Date` | - | Searches resource assignments which have startDate before this date |

#### `getWorkflowsForWorkspacePaginated`

Get all action templates for a workspace

- Returns: `WorkflowConnection!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `searchParams` | `SearchParams` | - | - |

#### `getWorkspace`

Get a workspace by ID  Access: Requires workspace access or be a member of the workspace  Parameters:   - workspaceId: The ID of the workspace to retrieve  Returns: The requested workspace

- Returns: `Workspace`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |

#### `getWorkspaceForms`

- Returns: `FormConnector!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `first` | `Int` | 15 | - |
| `after` | `Int` | 0 | - |
| `sortModel` | `[SortModel!]` | [] | - |
| `filterModel` | `[FilterModel!]` | [] | - |
| `searchParams` | `SearchParams` | - | - |

#### `groups`

Paginated groups the user belongs to. Use this query to get all groups (direct messages, groupchats, threads) the user belongs to. It's very useful when you need to get the group id and then send a message to the group or the user.  Access: Requires user access to the workspace and the group.  Parameters:   - workspace: ID of the workspace   - oneToOne: @deprecated do not use this parameter, use 'type' instead   - type: 'dm' (direct message) or 'group' (group chat) or 'thread'   - members: Array of user IDs (most important for search through chats)   - first: Pagination parameter   - after: Pagination parameter   - last: Pagination parameter   - before: Pagination parameter   - sortField: Sorting parameter   - sortOrder: Sorting parameter   - searchParams: Search parameters   - showHiddenGroups: Include hidden groups

- Returns: `GroupConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `ID!` | - | - |
| `oneToOne` | `Boolean` | - | - |
| `type` | `String` | - | - |
| `first` | `Int` | 20 | - |
| `after` | `String` | - | - |
| `last` | `Int` | - | - |
| `before` | `String` | - | - |
| `sortField` | `String` | - | - |
| `sortOrder` | `Int` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `showHiddenGroups` | `Boolean!` | false | - |
| `members` | `[ID!]` | - | - |

#### `nextApprovalStage`

Get the next approval stage awaiting approval for an action. Returns the stage that approvers should review next if one exists. Each approval item in the stage has a status field (unstarted, awaitingApproval, approved, approvedWithChanges, requireChanges) and approver details. Use this to identify who still needs to approve and send them reminders.  May return null if the action does not exist, the current user does not have access, there are no approval rounds for the action, or there is currently no pending approval stage.

- Returns: `ApprovalStage`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to get the next pending approval stage for |

#### `notebooks`

Gets paginated notebooks for a user across all workspaces. Use this resolver when you want to find notebooks by title or list notebooks in a workspace or project. Supports searching by title, filtering by workspace/project, search type (mine, shared, templates), and pagination.

- Returns: `NotebookConnection`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `first` | `Int` | 20 | Optional number of notebooks to return |
| `last` | `Int` | - | - |
| `before` | `ID` | - | Optional cursor to return notebooks before a specific notebook |
| `after` | `ID` | - | Optional cursor to return notebooks after a specific notebook |
| `sortField` | `String` | "modifiedAt" | Optional field to sort notebooks by |
| `sortOrder` | `Int` | -1 | Optional order to sort notebooks by |
| `searchType` | `NotebookSearchType` | - | Optional notebook search type to restrict notebook results |
| `workspaceId` | `ID` | - | Optional workspaceId to restrict notebook results |
| `projectId` | `ID` | - | Optional projectId to restrict notebook results |
| `archived` | `Boolean` | false | Optional archived flag to get archived notebook results |
| `includedNotebookIds` | `[ID!]` | - | Optional notebook ids to restrict notebook results |
| `searchParams` | `SearchParams` | - | Optional search parameters to find notebooks by title |

#### `workspacePlaceholders`

Get all resource placeholders for a workspace  Access: Requires user access to the workspace  Parameters:   - workspaceId: The ID of the workspace   - specificIds: Array of specific resource placeholder IDs to return  Returns: Array of ResourcePlaceholder objects

- Returns: `[ResourcePlaceholder!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `specificIds` | `[ID!]` | - | - |

## Mutations

Root type: `Mutation`

Total operations: **53**

| Operation | Args | Returns | Deprecated |
|---|---|---|---|
| `addActionCustomFields` | `ids: [ID!]!`, `projectIds: [ID!]!`, `workspaceId: ID!` | `[Project!]!` | no |
| `addProjectOwner` | `projectId: ID!`, `ownerId: ID!`, `workspaceId: ID!` | `Project` | no |
| `addStatusToProjectView` | `input: AddStatusToProjectViewInput!` | `ActionView` | no |
| `applyApprovalTemplate` | `actionId: ID!`, `templateId: ID!`, `roundId: ID` | `Boolean!` | no |
| `applyProjectTemplate` | `templateProjectId: ID!`, `targetProjectId: ID!`, `importWith: ApplyProjectTemplateImportWithInput`, `overrideLabels: Boolean` | `Project` | no |
| `bulkArchiveActions` | `actionIds: [ID!]!`, `workspaceId: ID!` | `[Action!]!` | no |
| `bulkInsertActions` | `actions: [BulkInsertActionInput!]!`, `sortByDates: Boolean` | `[ID!]` | no |
| `bulkUpdateActionCustomFields` | `actionIds: [ID!]!`, `workspaceId: ID!`, `fieldId: ID!`, `value: String`, `selectedValues: [String]`, `dateValue: Date`, `numberValue: Float` | `[Action!]!` | no |
| `bulkUpdateActionDescription` | `actionIds: [ID!]!`, `workspaceId: ID!`, `description: String!`, `isCollabUpdate: Boolean`, `forcePersistCollab: Boolean` | `Boolean` | no |
| `bulkUpdateActionLabels` | `actionIds: [ID!]!`, `workspaceId: ID!`, `labelIds: [ID!]!`, `operation: BatchOperation!`, `shouldUpdateChildren: Boolean`, `shouldUpdateRecurring: Boolean`, `isAutomated: Boolean` | `Boolean` | no |
| `bulkUpdateActionsAssignees` | `actionIds: [ID!]!`, `workspaceId: ID!`, `assigneesToSet: [ID!]`, `assigneesToAdd: [ID!]`, `assigneesToPull: [ID!]`, `teamAssignee: ID`, `placeholderAssigneesToSet: [ID!]`, `placeholderAssigneesToAdd: [ID!]`, `placeholderAssigneesToPull: [ID!]`, `privacy: ActionPrivacy`, `shouldUpdateChildren: Boolean`, `shouldUpdateRecurring: Boolean`, `updatePlaceholderAssignees: Boolean`, `currentAssigneeId: ID` | `Boolean` | no |
| `bulkUpdateActionsPriorityLevelId` | `actionIds: [ID!]!`, `workspaceId: ID!`, `priorityLevelId: ID`, `shouldUpdateRecurring: Boolean`, `rank: Float` | `Boolean` | no |
| `bulkUpdateActionStatus` | `actionIds: [ID!]!`, `workspaceId: ID!`, `status: String!`, `rankInput: RankInput`, `shouldUpdateChildren: Boolean` | `Boolean` | no |
| `bulkUpdateActionsTitles` | `actionTitleUpdates: [ActionTitleUpdateInput!]!`, `workspaceId: ID!` | `Boolean` | no |
| `bulkUpsertCustomFields` | `workspaceId: ID!`, `customFields: [CustomFieldToInsertInput!]!` | `CustomFieldUpsertResult` | no |
| `changeApprovalStageApprover` | `actionId: ID!`, `stageId: ID!`, `type: ApprovalType!`, `index: Int!`, `approvalItemId: ID!` | `ApprovalStage` | no |
| `convertActionToProject` | `actionId: ID!`, `projectName: String`, `parentProjectId: ID`, `deleteOriginalAction: Boolean`, `applyTemplateId: ID`, `sharingType: SharingTypes`, `members: [ID!]`, `teams: [ID!]`, `viewType: ActionViewType` | `Project` | no |
| `copyAction` | `actionId: ID!`, `shouldAddCopySign: Boolean!`, `assigneeForSubaction: [String!]`, `isPlaceholdersAssignee: Boolean!`, `lowestRank: Boolean`, `projectId: ID` | `Action` | no |
| `createDashboardV2` | `workspaceId: ID!`, `title: String!`, `privacy: DashboardPrivacy!`, `projectIds: [ID]!`, `sharingWith: [ID!]!`, `teams: [ID!]!`, `filter: WidgetContainerFilterInputV2`, `shareOnBehalfOfCreator: Boolean`, `color: String`, `type: DashboardType` | `Dashboard!` | no |
| `createDashboardWidget` | `dashboardId: ID`, `containerId: ID`, `containerType: WidgetContainerType`, `type: DashboardWidgetType!`, `title: String!`, `titleColor: String`, `titleSize: TextSize`, `fileIds: [ID!]`, `chartType: ChartType`, `sort: String`, `url: String`, `projectId: String`, `goalId: String`, `noteId: String`, `showTitles: Boolean`, `showLegend: Boolean`, `ignoreContainerFilter: Boolean`, `legendPosition: LegendPosition`, `showValueLabels: Boolean`, `showRowTotals: Boolean`, `showColumnTotals: Boolean`, `chartValuesState: [ChartValueStateInput!]`, `showFlattenedData: Boolean`, `showLinkedToProject: Boolean`, `truncateLongNumbers: Boolean`, `displayGroupsAs: DisplayGroupsAs`, `timeUnitsType: TimeUnit`, `projectTreeLevelsToShow: [Int!]`, `isProjectTreeLevelActive: Boolean`, `reportOn: DashboardWidgetReportOn`, `XAxis: DashboardWidgetXAxis`, `XAxisCustomFieldId: String`, `XAxisTitle: String`, `YAxis: DashboardWidgetYAxis`, `YAxisCustomFieldId: String`, `YAxisTitle: String`, `YAxisGroupBy: DashboardWidgetYAxis`, `groupByCustomFieldId: String`, `chartValueColors: [ChartValueColorInput!]`, `groupOthers: DashboardWidgetGroupOthersInput`, `sectionHeaderText: String`, `sectionHeaderTextAlignment: TextAlignment`, `sectionHeaderLinePosition: SectionHeaderLinePosition`, `isHidden: Boolean`, `projectDetailsFields: [String!]`, `contentTextAlignment: TextAlignment`, `contentTextSize: TextSize`, `contentTextColorPrimary: String`, `contentTextColorSecondary: String`, `workspaceId: String`, `overdueFilter: IncludeFilterType`, `recurringFilter: IncludeFilterType`, `completedDateRange: DateRangeFilterInput`, `createdDateRange: DateRangeFilterInput`, `dueDatesRange: DateRangeFilterInput`, `projectDateRange: DateRangeFilterInput`, `projectStatusDateRange: DateRangeFilterInput`, `dateRange: DateRangeFilterInput`, `colorThemeId: String`, `segmentColorOverrides: [SegmentColorOverrideInput!]`, `projectBudgetCategoryIds: [String]`, `projectBudgetDateRange: [Date!]` | `DashboardWidget!` | no |
| `createGoal` | `_id: ID`, `workspace: ID!`, `owners: [ID!]!`, `teamOwners: [ID!]!`, `name: String!`, `parentId: ID`, `description: String!`, `initialValue: Float!`, `currentValue: Float!`, `goalValue: Float!`, `startDate: Date`, `endDate: Date`, `ongoingDate: Boolean`, `recurringDate: GoalRecurringDateInput`, `measurementType: MeasurementType`, `measurementUnit: MeasurementUnit`, `measurementUnitValue: String!`, `measurementUnitSymbol: String!`, `displayType: DisplayType!`, `actionIds: [ID!]`, `includeSubActions: Boolean`, `projectIds: [ID!]`, `sharingType: SharingTypes`, `sharingWith: [ID!]`, `isAutomated: Boolean` | `Goal` | no |
| `createReminder` | `text: String!`, `userIds: [ID!]!`, `recurrenceDefinition: RecurrenceDefinitionInput!`, `workspaceId: ID!`, `originType: ReminderOriginType!`, `originId: ID!` | `Reminder!` | no |
| `createResourceAssignment` | `resourceAssignment: CreateResourceAssignmentInput!` | `ResourceAssignments` | no |
| `createResourcePlaceholder` | `name: String!`, `workspaceId: ID!`, `billRate: Float`, `costRate: Float`, `roleTagId: ID` | `ResourcePlaceholder!` | no |
| `disableActionCustomFields` | `customFieldIds: [ID!]!`, `projectIds: [ID!]!`, `workspaceId: ID!`, `removeFromActions: Boolean` | `[Project!]!` | no |
| `disableProjectsCustomFields` | `customFieldIds: [ID!]!`, `projectIds: [ID!]!`, `workspaceId: ID!` | `[Project!]!` | no |
| `insertApprovalRound` | `actionId: ID!`, `roundId: ID!`, `stageId: ID!` | `ApprovalRound` | no |
| `insertApprovalStage` | `actionId: ID!`, `roundId: ID!`, `stageId: ID` | `ApprovalStage` | no |
| `insertGroup` | `workspace: String!`, `members: [String!]!`, `teams: [String!]`, `name: String`, `oneToOne: Boolean`, `type: String`, `projectId: String` | `Group` | no |
| `insertMessage` | `_id: ID`, `workspaceId: ID`, `containerId: ID`, `containerType: ContainerType`, `participants: [ID!]`, `mentions: [String]`, `automated: Boolean`, `body: String!`, `attachments: [Attachment]`, `color: String`, `isNoteJsonComment: Boolean`, `isPrivate: Boolean`, `userMentionsByGroup: [ID!]` | `Message!` | no |
| `insertPost` | `_id: ID`, `body: String!`, `workspaceId: ID!`, `fileId: ID`, `category: String` | `Post!` | no |
| `insertRecurringAction` | `actionId: ID!`, `type: String`, `dayType: String`, `startDate: Date`, `endDate: Date`, `interval: Int`, `endingType: String`, `endingAfter: Int`, `days: [String]`, `showOnDueDate: Boolean`, `recurringId: ID` | `RecurringAction` | no |
| `removeProjectOwner` | `projectId: ID!`, `ownerId: ID!`, `workspaceId: ID!` | `Project` | no |
| `requestApprovals` | `roundId: ID!` | `ApprovalRound` | no |
| `runWorkflow` | `workflowId: ID!`, `actionId: ID!` | `Boolean` | no |
| `salesforceOperation` | `input: SalesforceOperationInput!` | `SalesforceOperationResult!` | no |
| `setActionColor` | `actionId: ID!`, `actionColor: String!` | `Action` | no |
| `setCustomStatusColor` | `workspaceId: ID!`, `status: String!`, `color: String` | `Workspace` | no |
| `setStoryPoints` | `actionId: ID!`, `storyPoints: Int!` | `Action` | no |
| `unsetRecurringActions` | `actionIds: [ID!]!`, `workspaceId: ID!` | `Boolean` | no |
| `updateActionGithubBranchNames` | `actionId: ID!`, `githubBranchNames: [String!]!` | `Action` | no |
| `updateActionProject` | `actionId: ID!`, `projectId: ID`, `rank: Float` | `Action` | no |
| `updateActionsMilestone` | `actionIds: [ID!]!`, `workspaceId: ID!`, `value: Boolean!` | `Boolean` | no |
| `updateActionSnoozeDate` | `actionId: ID!`, `snoozeDate: Date` | `Action` | no |
| `updateDashboardV2` | `_id: ID!`, `title: String`, `privacy: DashboardPrivacy`, `projectIds: [ID]`, `sharingWith: [ID!]`, `teams: [ID!]`, `layout: [InputDashboardLayout!]`, `filter: WidgetContainerFilterInputV2`, `shareOnBehalfOfCreator: Boolean`, `shareOnBehalfOfCreatorSettings: ShareOnBehalfOfCreatorSettingsInput`, `pinToUser: Boolean`, `color: String`, `allowedEmailDomains: [String!]`, `allowAccessToWhitelistedDomains: Boolean`, `backgroundColor: DashboardBackgroundColor`, `backgroundImageUrl: String`, `backgroundImageCropType: DashboardBackgroundImageCropType`, `displayTipsAndTricksFooter: Boolean`, `headerTextColor: DashboardHeaderTextColor`, `type: DashboardType` | `Dashboard` | no |
| `updateDashboardWidget` | `_id: ID!`, `title: String`, `titleColor: String`, `titleSize: TextSize`, `url: String`, `sort: String`, `type: DashboardWidgetType`, `chartType: ChartType`, `slateJson: JSONObject`, `XAxis: DashboardWidgetXAxis`, `XAxisCustomFieldId: String`, `XAxisTitle: String`, `YAxis: DashboardWidgetYAxis`, `YAxisCustomFieldId: String`, `YAxisTitle: String`, `YAxisGroupBy: DashboardWidgetYAxis`, `groupByCustomFieldId: String`, `fileIds: [ID!]`, `noteId: String`, `portfolioViewId: String`, `hideHeader: Boolean`, `goalId: String`, `showTitles: Boolean`, `showLegend: Boolean`, `ignoreContainerFilter: Boolean`, `legendPosition: LegendPosition`, `showValueLabels: Boolean`, `showRowTotals: Boolean`, `showColumnTotals: Boolean`, `showFlattenedData: Boolean`, `showLinkedToProject: Boolean`, `truncateLongNumbers: Boolean`, `displayGroupsAs: DisplayGroupsAs`, `displayGoalsBy: DisplayGoalsBy`, `timeUnitsType: TimeUnit`, `projectTreeLevelsToShow: [Int!]`, `isProjectTreeLevelActive: Boolean`, `reportOn: DashboardWidgetReportOn`, `chartValueColors: [ChartValueColorInput!]`, `groupOthers: DashboardWidgetGroupOthersInput`, `projectId: String`, `buttonLabel: String`, `sectionHeaderText: String`, `sectionHeaderTextAlignment: TextAlignment`, `sectionHeaderLinePosition: SectionHeaderLinePosition`, `isHidden: Boolean`, `projectDetailsFields: [String!]`, `contentTextAlignment: TextAlignment`, `contentTextSize: TextSize`, `contentTextColorPrimary: String`, `contentTextColorSecondary: String`, `workspaceId: String`, `containerId: ID`, `colorThemeId: String`, `segmentColorOverrides: [SegmentColorOverrideInput!]`, `projectBudgetCategoryIds: [String]`, `projectBudgetDateRange: [Date!]`, `chartValuesState: [ChartValueStateInput!]` | `DashboardWidget` | no |
| `updateMeetingUserData` | `meetingExternalId: String!`, `workspaceId: ID!`, `goals: GoalDiff`, `nextSteps: NextStepDiff`, `materials: MaterialDiff`, `speakerLabels: SpeakerLabelDiff`, `customTitle: String` | `MeetingUserData` | no |
| `updateMembersPermissions` | `projectId: ID!`, `memberIds: [ID!]`, `teamIds: [ID!]`, `permission: String!`, `sharingType: String!`, `isAutomated: Boolean` | `Project` | no |
| `updateProjectArchived` | `projectId: ID!`, `archived: Boolean!`, `includeChildren: Boolean` | `Project` | no |
| `updateProjectDescription` | `projectId: ID!`, `description: String!` | `Project` | no |
| `updateProjectsCustomFields` | `projectIds: [ID!]!`, `workspaceId: ID!`, `fields: [CustomFieldItemInput!]!` | `[Project!]!` | no |
| `updateResourceAssignment` | `id: ID!`, `workspaceId: ID!`, `resourceAssignment: UpdateResourceAssignmentInput!` | `ResourceAssignments` | no |
| `updateResourcePlaceholder` | `id: ID!`, `name: String`, `billRate: Float`, `costRate: Float`, `roleTagId: ID` | `ResourcePlaceholder!` | no |

### Details

#### `addActionCustomFields`

Enables custom fields for actions in specific projects.  This should be used to enable only action itemType custom fields.  Parameters:   - ids: Required. The IDs of the custom fields to enable   - projectIds: Required. The IDs of the projects to enable the custom fields for   - workspaceId: Required. The ID of the workspace to enable the custom fields for

- Returns: `[Project!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `ids` | `[ID!]!` | - | - |
| `projectIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

#### `addProjectOwner`

Add a user to the project owner list.

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | Project ID to add owner to |
| `ownerId` | `ID!` | - | User ID to add as owner |
| `workspaceId` | `ID!` | - | Workspace ID of the project |

#### `addStatusToProjectView`

This mutation is used to add a status to a specific project. ALWAYS run the setCustomStatusColor mutation (setting status color) to set the color of the status afterwards.

- Returns: `ActionView`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddStatusToProjectViewInput!` | - | The ID of the action view and status name to add |

#### `applyApprovalTemplate`

Apply an existing approval template to an action. Creates all rounds and stages defined in the template with configured approvers. Use this to quickly set up a standard approval workflow on an action. The template defines who needs to approve and in what order. This is the easiest way to add approval workflows - instead of manually creating rounds and stages, just apply a pre-configured template.

- Returns: `Boolean!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to apply the template to |
| `templateId` | `ID!` | - | ID of the template to apply |
| `roundId` | `ID` | - | Optional ID of an existing round to replace (if the round is empty) |

#### `applyProjectTemplate`

Apply a project template to an existing project.  This mutation copies settings, structure, and configuration from a template project to a target project based on the importWith flags.  Access: Requires user access to both template and target projects  Returns: The updated target project

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `templateProjectId` | `ID!` | - | - |
| `targetProjectId` | `ID!` | - | - |
| `importWith` | `ApplyProjectTemplateImportWithInput` | - | - |
| `overrideLabels` | `Boolean` | false | - |

#### `bulkArchiveActions`

- Returns: `[Action!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

#### `bulkInsertActions`

Batch insert actions and return the inserted action ids Access: Requires user access to the workspace and projects. Won't add actions to projects that user doesn't have access to. If the user uses phrases like "on my list" or otherwise implies the actions are for themselves, assume the user is the assignee by default. Errors: Throws error if user does not have access to workspace.

- Returns: `[ID!]`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actions` | `[BulkInsertActionInput!]!` | - | Action objects to insert |
| `sortByDates` | `Boolean` | false | Set to true to sort actions with dates chronologically for sequential dependencies |

#### `bulkUpdateActionCustomFields`

Updates a custom field value for multiple actions at once.  This mutation allows you to set or clear the value of a custom field across multiple actions. You must first call getCustomFields to retrieve available custom fields and their types for the workspace.  **Important**: Use only ONE value parameter based on the custom field type:  \| Custom Field Type \| Parameter to Use \| Value Format \| \|-------------------\|------------------\|--------------\| \| text              \| value            \| Any string value \| \| number            \| numberValue      \| Any numeric value (float) \| \| date              \| dateValue        \| ISO 8601 date string (e.g., "2024-01-15T00:00:00.000Z") \| \| select            \| selectedValues   \| Array of dropdown option strings (e.g., ["Option 1", "Option 2"]) \| \| user              \| selectedValues   \| Array of user IDs (e.g., ["userId123", "userId456"]) \| \| project           \| selectedValues   \| Array of project IDs (e.g., ["projectId123"]) \|  **To clear a custom field value**: Pass null or an empty value for the corresponding parameter.  Access: Requires user access to all specified actions  Returns: Array of updated Action objects with the new custom field values  Errors:   - Throws error if user doesn't have access to any of the actions   - Throws error if custom field doesn't exist   - Throws error if value type doesn't match the custom field type

- Returns: `[Action!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | Array of action IDs to update the custom field for |
| `workspaceId` | `ID!` | - | The workspace ID that contains the actions |
| `fieldId` | `ID!` | - | The ID of the custom field to update (get this from getCustomFields query) |
| `value` | `String` | - | Text value - use ONLY for 'text' type custom fields |
| `selectedValues` | `[String]` | - | Array of selected values - use for 'select', 'user', or 'project' type custom fields. For 'select' type: pass the dropdown option strings. For 'user' type: pass an array of user IDs. For 'project' type: pass an array of project IDs. |
| `dateValue` | `Date` | - | Date value - use ONLY for 'date' type custom fields. Pass ISO 8601 format. |
| `numberValue` | `Float` | - | Numeric value - use ONLY for 'number' type custom fields |

#### `bulkUpdateActionDescription`

Update descriptions for multiple actions at once  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - description: The new description to set. Must be a valid HTML string. Use the corresponding markdown (<ul> for lists, <code> for code blocks, etc). Code blocks should be contained in a single tag.  Returns: Boolean indicating success

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `description` | `String!` | - | - |
| `isCollabUpdate` | `Boolean` | - | - |
| `forcePersistCollab` | `Boolean` | - | - |

#### `bulkUpdateActionLabels`

Update labels for the provided action IDs.  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - labelIds: Array of label IDs to add or remove   - operation: The operation to perform (ADD, REMOVE)   - shouldUpdateChildren: Boolean to update children   - shouldUpdateRecurring: Boolean to update recurring  Returns: Boolean indicating success

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `labelIds` | `[ID!]!` | - | - |
| `operation` | `BatchOperation!` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `isAutomated` | `Boolean` | - | - |

#### `bulkUpdateActionsAssignees`

Update actions assignees in bulk  IMPORTANT: - Set operation will override existing assignees and placeholder assignees. - Add/pull operation will add/pull assignees and placeholder assignees to existing ones.  The set and add/pull parameters are mutually exclusive. If you want to set the assignees, you should not pass any of the add/pull parameters. If you want to add or pull assignees, you should not pass the set parameter.  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - assigneesToSet: Array of user IDs to assign   - assigneesToAdd: Array of user IDs to add   - assigneesToPull: Array of user IDs to remove   - teamAssignee: The ID of the team to assign   - placeholderAssigneesToSet: Array of placeholder IDs to assign   - placeholderAssigneesToAdd: Array of placeholder IDs to add   - placeholderAssigneesToPull: Array of placeholder IDs to remove   - privacy: The privacy of the action   - shouldUpdateChildren: Boolean to update children   - shouldUpdateRecurring: Boolean to update recurring   - updatePlaceholderAssignees: Boolean to update placeholder assignees   - currentAssigneeId: The ID of the current assignee  Returns: Boolean indicating success

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `assigneesToSet` | `[ID!]` | [] | - |
| `assigneesToAdd` | `[ID!]` | [] | - |
| `assigneesToPull` | `[ID!]` | [] | - |
| `teamAssignee` | `ID` | - | - |
| `placeholderAssigneesToSet` | `[ID!]` | [] | - |
| `placeholderAssigneesToAdd` | `[ID!]` | [] | - |
| `placeholderAssigneesToPull` | `[ID!]` | [] | - |
| `privacy` | `ActionPrivacy` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `updatePlaceholderAssignees` | `Boolean` | false | - |
| `currentAssigneeId` | `ID` | - | - |

#### `bulkUpdateActionsPriorityLevelId`

Update priority level for multiple actions at once.  Always call getPriorityLevels before calling this function to get the priority level IDs and ensure that priorityLevelId exists.  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - priorityLevelId: The ID of the priority level to set (null to unset)   - shouldUpdateRecurring: Optional flag to update recurring instances  Returns: Boolean indicating success

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `priorityLevelId` | `ID` | - | - |
| `shouldUpdateRecurring` | `Boolean` | - | - |
| `rank` | `Float` | - | - |

#### `bulkUpdateActionStatus`

Update status for multiple actions at once.  ALWAYS look for existing statuses in the project. Only add statuses if they're definitely different from the existing ones. Otherwise, don't add them and use the existing ones that have the same meaning.  Examples: Project has statuses: "To Do", "In Progress", "Review feedback", "Done"    1)     - User asks to update statuses: "update to feedback"     - Result: Action statuses are updated to "Review feedback"    2)     - User asks to update statuses: "set in progress"     - Result: Action statuses are updated to "In Progress"    3)     - User asks to update statuses: "mark as completed"     - Result: Action statuses are updated to "Done"  Access: Requires user access to all actions  Parameters:   - actionIds: Array of action IDs to update   - workspaceId: The ID of the workspace   - status: The new status to set   - rankInput: Optional rank information for repositioning   - shouldUpdateChildren: Optional flag to update child actions  Returns: Boolean indicating success

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `status` | `String!` | - | - |
| `rankInput` | `RankInput` | - | - |
| `shouldUpdateChildren` | `Boolean` | - | - |

#### `bulkUpdateActionsTitles`

Update different titles for multiple actions at once  Access: Requires user access to all actions  Parameters:   - actionTitleUpdates: Array of {actionId, title} pairs to update   - workspaceId: The ID of the workspace  Behavior:   - Empty titles are not allowed (will throw error)   - Only updates the specific actions in the batch (does not update recurring series)  Returns: Boolean indicating success

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionTitleUpdates` | `[ActionTitleUpdateInput!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

#### `bulkUpsertCustomFields`

Creates or updates multiple custom fields at once.    It can be used to upsert custom fields for a project or an action.  Parameters: - workspaceId: Required. The ID of the workspace to upsert custom fields for. - customFields: Required. An array of custom fields to upsert.  Examples: 1. Create a custom field (text type) for a project:  { "workspaceId": "TCB9NnnbcC4BEc2rF", "customFields": [     {         "allowMultiSelect": false,         "_id": "d6JfiYb34mMb5zNqL",         "label": "Test Project Field",         "dropdownValues": [],         "formula": null,         "type": "text",         "itemType": "project",         "onlyAdminEditable": false,         "jiraCustomFieldId": "",         "groupIds": []     }   ] }  2. Create a custom field (number type) for an action:  { "workspaceId": "TCB9NnnbcC4BEc2rF", "customFields": [     {         "allowMultiSelect": false,         "_id": "y7RCztztQ4D36GKk5",         "label": "asasas",         "dropdownValues": [],         "formula": "Test Action Field",         "type": "number",         "itemType": "action",         "onlyAdminEditable": false,         "jiraCustomFieldId": "",         "groupIds": []     }   ] }  When creating custom fields the _id field is generated server-side automatically, so you don't need to provide it. When updating custom fields you must provide old _id and new field data (old field data with new values).

- Returns: `CustomFieldUpsertResult`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `customFields` | `[CustomFieldToInsertInput!]!` | - | - |

#### `changeApprovalStageApprover`

Add or change an approver at a specific position in an approval stage. This is the primary way to assign approvers (users, teams, placeholders, or external approvers) to approval stages. The index parameter specifies which approval slot to update (0 for first approver, 1 for second, etc). If an approver already exists at that index, they will be replaced. If the index is beyond the current array length, a new approval will be added.

- Returns: `ApprovalStage`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action containing the approval stage |
| `stageId` | `ID!` | - | ID of the approval stage to modify. Use the stage._id field from approvalStages query, not the sortIndex. |
| `type` | `ApprovalType!` | - | Type of approver being added (user, team, placeholder, or external) |
| `index` | `Int!` | - | Position in the approvals array where to add/replace the approver (0 for first position, 1 for second, etc) |
| `approvalItemId` | `ID!` | - | ID of the approver to assign (user ID, team ID, placeholder ID, or external user ID) |

#### `convertActionToProject`

Convert an action to a project.  This mutation creates a new project from an action, and clones subactions as actions in the new project.  Access: Requires user access to the action and workspace  Parameters:   - actionId: The ID of the action to convert   - projectName: Optional custom name for the new project (defaults to action title)   - parentProjectId: Optional parent project ID to nest the new project under   - deleteOriginalAction: Whether to delete the original action after conversion (default: false)   - applyTemplateId: Optional project template ID to apply to the new project   - sharingType: Project sharing type (me, custom, everyone) - defaults to 'me'   - members: User IDs to add as project members (defaults to current user)   - teams: Team IDs to give access to the project  Returns: The newly created Project object

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | The ID of the action to convert to a project |
| `projectName` | `String` | - | Optional custom name for the new project (defaults to action title) |
| `parentProjectId` | `ID` | - | Optional parent project ID to nest the new project under |
| `deleteOriginalAction` | `Boolean` | false | Whether to delete the original action after conversion (default: false) |
| `applyTemplateId` | `ID` | - | Optional project template ID to apply to the new project |
| `sharingType` | `SharingTypes` | - | Project sharing type (me, custom, everyone) - defaults to 'me' |
| `members` | `[ID!]` | - | User IDs to add as project members (defaults to current user) |
| `teams` | `[ID!]` | - | Team IDs to give access to the project |
| `viewType` | `ActionViewType` | - | Default view type for the project - defaults to 'listView' |

#### `copyAction`

Copy/duplicate an action including its subactions, attachments, approval rounds, and dependencies. Returns the newly created action.

- Returns: `Action`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | The ID of the action to duplicate |
| `shouldAddCopySign` | `Boolean!` | - | Whether to append '(copy)' to the duplicated action's title |
| `assigneeForSubaction` | `[String!]` | - | User IDs to assign as assignees on copied subactions (empty array keeps original assignees) |
| `isPlaceholdersAssignee` | `Boolean!` | - | Whether the assigneeForSubaction values are placeholder IDs rather than user IDs |
| `lowestRank` | `Boolean` | - | Place the copied action at the lowest rank (bottom of list). Defaults to false (top of list) |
| `projectId` | `ID` | - | Optional target project ID. When provided, copies the action into a different project and clears project-specific fields (sections, phases) |

#### `createDashboardV2`

Creates a new dashboard with typed V2 filter input for Buzz/MCP endpoints. This mutation provides full schema introspection for AI assistants.

- Returns: `Dashboard!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `title` | `String!` | - | - |
| `privacy` | `DashboardPrivacy!` | - | - |
| `projectIds` | `[ID]!` | - | - |
| `sharingWith` | `[ID!]!` | - | - |
| `teams` | `[ID!]!` | - | - |
| `filter` | `WidgetContainerFilterInputV2` | - | - |
| `shareOnBehalfOfCreator` | `Boolean` | false | - |
| `color` | `String` | "#FFCF55" | - |
| `type` | `DashboardType` | - | - |

#### `createDashboardWidget`

Creates a new dashboard widget with specified configuration. Common configurations by widget type:   1. Chart Widgets (Bar/Line/Pie): - Set chartType, XAxis, YAxis - Configure grouping and aggregation - Set up color schemes - Use these types of widgets when asked to show something broken down by project, assignee, etc.  2. List Widgets (Actions/Projects): - Define filters (status, assignee, etc.) - Set up sorting and grouping - Configure display options - When user asks to create a widget for all actions assigned to them, create a widget with type 'myActionsList' - Use these types of widgets when asked to show something in a list format, like actions, projects, etc.  3. Status Widgets: - Specify project or goal - Configure metrics to display - Set up refresh intervals  4. Custom Widgets: - Set up embedded content - Configure interactive elements - Define data sources      When asked to show something over time, use binBy and binByDateRange parameters.

- Returns: `DashboardWidget!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `dashboardId` | `ID` | - | - |
| `containerId` | `ID` | - | - |
| `containerType` | `WidgetContainerType` | - | Type of container this widget belongs |
| `type` | `DashboardWidgetType!` | - | The type of dashboard widget to create |
| `title` | `String!` | - | Title text to display for the widget |
| `titleColor` | `String` | - | Hex color code for the widget title |
| `titleSize` | `TextSize` | - | Size of the title text |
| `fileIds` | `[ID!]` | - | Array of file IDs associated with this widget |
| `chartType` | `ChartType` | - | Type of chart to display |
| `sort` | `String` | - | Sort order for widget data |
| `url` | `String` | - | URL for embedded content widgets |
| `projectId` | `String` | - | ID of associated project |
| `goalId` | `String` | - | ID of associated goal |
| `noteId` | `String` | - | ID of associated note |
| `showTitles` | `Boolean` | - | Whether to show titles in the widget |
| `showLegend` | `Boolean` | - | Whether to show chart legend |
| `ignoreContainerFilter` | `Boolean` | - | If true, widget ignores container-level filters |
| `legendPosition` | `LegendPosition` | - | Position of the chart legend |
| `showValueLabels` | `Boolean` | - | Whether to show data point values |
| `showRowTotals` | `Boolean` | - | Whether to show row totals |
| `showColumnTotals` | `Boolean` | - | Whether to show column totals |
| `chartValuesState` | `[ChartValueStateInput!]` | - | Used to store the state of the chart values (colors, order, etc.) |
| `showFlattenedData` | `Boolean` | - | Whether to show pivot table in a data mode (flattened) |
| `showLinkedToProject` | `Boolean` | - | Whether to show links to related projects |
| `truncateLongNumbers` | `Boolean` | - | Whether to truncate long numbers |
| `displayGroupsAs` | `DisplayGroupsAs` | - | How to display grouped data |
| `timeUnitsType` | `TimeUnit` | - | Time unit for temporal data |
| `projectTreeLevelsToShow` | `[Int!]` | - | Which levels of project tree to display |
| `isProjectTreeLevelActive` | `Boolean` | - | Whether project tree level is active |
| `reportOn` | `DashboardWidgetReportOn` | - | What type of data to report on |
| `XAxis` | `DashboardWidgetXAxis` | - | Field to use for X-axis |
| `XAxisCustomFieldId` | `String` | - | Custom field ID for X-axis |
| `XAxisTitle` | `String` | - | Title for X-axis |
| `YAxis` | `DashboardWidgetYAxis` | - | Field to use for Y-axis |
| `YAxisCustomFieldId` | `String` | - | Custom field ID for Y-axis |
| `YAxisTitle` | `String` | - | Title for Y-axis |
| `YAxisGroupBy` | `DashboardWidgetYAxis` | - | Field to group Y-axis values by |
| `groupByCustomFieldId` | `String` | - | Custom field ID for grouping |
| `chartValueColors` | `[ChartValueColorInput!]` | - | Color configuration for chart values |
| `groupOthers` | `DashboardWidgetGroupOthersInput` | - | Configuration for grouping "other" values |
| `sectionHeaderText` | `String` | - | Text for section header |
| `sectionHeaderTextAlignment` | `TextAlignment` | - | Alignment of section header text |
| `sectionHeaderLinePosition` | `SectionHeaderLinePosition` | - | Position of section header line |
| `isHidden` | `Boolean` | - | Whether widget is hidden |
| `projectDetailsFields` | `[String!]` | - | Fields to show in project details |
| `contentTextAlignment` | `TextAlignment` | - | Alignment of content text |
| `contentTextSize` | `TextSize` | - | Size of content text |
| `contentTextColorPrimary` | `String` | - | Primary color for content text |
| `contentTextColorSecondary` | `String` | - | Secondary color for content text |
| `workspaceId` | `String` | - | ID of workspace this widget belongs to |
| `overdueFilter` | `IncludeFilterType` | - | Filter for overdue actions. Used to include or exclude overdue actions. Example: {overdueFilter: 'includeOnly'} |
| `recurringFilter` | `IncludeFilterType` | - | Filter for recurring actions. Used to include or exclude recurring actions. Example: {recurringFilter: 'includeOnly'} |
| `completedDateRange` | `DateRangeFilterInput` | - | Date range filter for completed actions. Example: filter to last 3 months - { selectedOption: 'lastNMonths', amount: 3, timeUnit: 'month', timeDirection: 'last' } |
| `createdDateRange` | `DateRangeFilterInput` | - | Date range filter for created actions |
| `dueDatesRange` | `DateRangeFilterInput` | - | Date range filter for due dates |
| `projectDateRange` | `DateRangeFilterInput` | - | Date range filter for project dates |
| `projectStatusDateRange` | `DateRangeFilterInput` | - | Date range filter for project status dates |
| `dateRange` | `DateRangeFilterInput` | - | General date range filter |
| `colorThemeId` | `String` | - | - |
| `segmentColorOverrides` | `[SegmentColorOverrideInput!]` | - | - |
| `projectBudgetCategoryIds` | `[String]` | - | - |
| `projectBudgetDateRange` | `[Date!]` | - | - |

#### `createGoal`

Create a new goal with comprehensive validation rules  IMPORTANT VALIDATION RULES:  Display Type Rules: - progress: Only works with measurementType null, number, or actions - number: Only works with measurementType null, number, actions, or overdue - status: Only works with measurementType status  Measurement Type + Unit Combinations: - measurementType actions/overdue: Must use measurementUnit actions OR projects - measurementType number: Must use measurementUnit currency, custom, OR percentage - measurementType status: Must use measurementUnit subGoals  Measurement Unit + Value + Symbol Rules: - measurementUnit currency: measurementUnitValue must be one of the supported currency codes (e.g., USD/EUR/JPY/GBP/AUD), symbol $/€/¥/£/AU$   This list is not exhaustive. For additional currencies, specify the ISO 4217 currency code as measurementUnitValue and provide the appropriate symbol. Refer to the application's documentation or configuration for the full list of supported currencies and symbols. - measurementUnit percentage: measurementUnitValue must be 'percentage', symbol '%' - measurementUnit actions: measurementUnitValue must be 'actions' - measurementUnit projects: measurementUnitValue must be 'projects' - measurementUnit subGoals: measurementUnitValue must be the empty string ("") - measurementUnit custom: measurementUnitValue can be any string  Action/Project ID Rules: - actionIds: Requires measurementType actions/overdue + measurementUnit actions + measurementUnitValue 'actions' - projectIds: Requires measurementType actions/overdue + measurementUnit projects + measurementUnitValue 'projects'  Date Rules: - Cannot be both ongoingDate AND recurringDate - Cannot combine ongoingDate with startDate/endDate - Cannot combine recurringDate with startDate/endDate - If startDate provided, endDate is required - startDate must be before endDate

- Returns: `Goal`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | - |
| `workspace` | `ID!` | - | The workspace ID where this goal will be created |
| `owners` | `[ID!]!` | - | User IDs who own this goal (must contain at least one element; empty arrays are not allowed and will be rejected at runtime) |
| `teamOwners` | `[ID!]!` | - | Team IDs who own this goal |
| `name` | `String!` | - | Goal name (cannot be empty string) |
| `parentId` | `ID` | - | Parent goal ID if this is a sub-goal |
| `description` | `String!` | - | Goal description in HTML format |
| `initialValue` | `Float!` | - | Initial numeric value for the goal |
| `currentValue` | `Float!` | - | Current numeric value for the goal |
| `goalValue` | `Float!` | - | Target numeric value for the goal |
| `startDate` | `Date` | - | Start date (requires endDate if provided) |
| `endDate` | `Date` | - | End date (required if startDate provided, must be after startDate) |
| `ongoingDate` | `Boolean` | false | Whether goal is ongoing (cannot combine with recurringDate or start/endDate) |
| `recurringDate` | `GoalRecurringDateInput` | null | Recurring schedule (cannot combine with ongoingDate or start/endDate) |
| `measurementType` | `MeasurementType` | null | How goal value is measured (null, number, actions, status, overdue) |
| `measurementUnit` | `MeasurementUnit` | null | Unit for measurement (currency, percentage, custom, actions, projects, subGoals) |
| `measurementUnitValue` | `String!` | - | Specific value for the unit (e.g., 'USD', 'percentage', 'actions', 'projects', '' for subGoals) |
| `measurementUnitSymbol` | `String!` | - | Symbol for the unit (e.g., '$', '%', '€', '¥', '£', 'AU$') |
| `displayType` | `DisplayType!` | - | How goal is displayed (number, progress, status) |
| `actionIds` | `[ID!]` | [] | Action IDs to track (requires measurementType actions/overdue + measurementUnit actions + measurementUnitValue 'actions') |
| `includeSubActions` | `Boolean` | - | Whether to include sub-actions in tracking |
| `projectIds` | `[ID!]` | [] | Project IDs to track (requires measurementType actions/overdue + measurementUnit projects + measurementUnitValue 'projects') |
| `sharingType` | `SharingTypes` | - | Who can access this goal (me, custom, everyone) |
| `sharingWith` | `[ID!]` | [] | User IDs to share with (only valid when sharingType is custom) |
| `isAutomated` | `Boolean` | false | Whether this goal was created automatically |

#### `createReminder`

Create a new reminder  Examples:  Create a one time reminder for 5 minutes from now Now: 2025-09-17T20:22:00.000Z {   "text": "Remind me to check in on Beta Deploy",   "userIds": ["some_user_id"],   "recurrenceDefinition": {     "type":"daily",     "interval":1,     "days":["Wed","Thu","Fri","Sat","Sun","Mon","Tue"],     "startDate":"2025-09-17T20:27:00.000Z",     "endingType":"after",     "endingAfter":1   },   "workspaceId": "7driFnaZjDQZndHqs",   originType: "buzzThread",   originId: "some_buzz_thread_id" }  Create a recurring reminder for every 2 days with no end Now: 2025-09-17T20:22:00.000Z {   "text": "Remind me to check in on Beta Deploy",   "userIds": ["some_user_id"],   "recurrenceDefinition": {     "type":"daily",     "interval":2,     "days":["Wed","Thu","Fri","Sat","Sun","Mon","Tue"],     "startDate":"2025-09-17T20:27:00.000Z",     "endingType":"never",   },   "workspaceId": "7driFnaZjDQZndHqs",   originType: "buzzThread",   originId: "some_buzz_thread_id" }

- Returns: `Reminder!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `text` | `String!` | - | - |
| `userIds` | `[ID!]!` | - | - |
| `recurrenceDefinition` | `RecurrenceDefinitionInput!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `originType` | `ReminderOriginType!` | - | - |
| `originId` | `ID!` | - | - |

#### `createResourceAssignment`

Create a resource assignment.  IMPORTANT: ALWAYS pass 'fixedDisplayType' and 'allocationType' together. Use assignmentType: 'regular' by default. Use other assignment types only if the user explicitly mentioned another type.  Possible valid combinations ('allocationType' + 'fixedDisplayType'): • 'hoursPerDay' + 'hours' - when you want to allocate hours per day • 'fixedHours' + 'hours' - when you want to allocate total hours • 'fixedHours' + 'days' - when you want to allocate in days (default work day = 8 hours) • 'fixedHours' + 'percentages' - when you want to allocate in percentages (percentage of the default default work day hours, e,g, 50% = 4 hours)  IMPORTANT: ALWAYS pass 'allocationValue' when allocating by percentage. IMPORTANT: ALWAYS pass 'fixedHours' when allocating by hours or days. IMPORTANT: ALWAYS pass 'hoursPerDay' when allocating by hours per day.  Examples: • Duration: 1 day, allocationType = hoursPerDay, fixedDisplayType = hours, allocationValue = 8, hoursPerDay = 8 • Duration: 5 days, allocationType = hoursPerDay, fixedDisplayType = hours, allocationValue = 8, hoursPerDay = 8 • Duration: 1 day, allocationType = fixedHours, fixedDisplayType = hours, allocationValue = 40, fixedHours = 40 • Duration: 5 days, allocationType = fixedHours, fixedDisplayType = hours, allocationValue = 40, fixedHours = 40 • Duration: 1 day, allocationType = fixedHours, fixedDisplayType = percentages, allocationValue = 50 (percents), fixedHours = 8 (default work day hours) * 1 (days) * 0.5 = 4 • Duration: 5 days, allocationType = fixedHours, fixedDisplayType = percentages, allocationValue = 50 (percents), fixedHours = 8 (default work day hours) * 5 (days) * 0.5 = 20 • Duration: 1 day, allocationType = fixedHours, fixedDisplayType = days, allocationValue = 2 (days), fixedHours = 8 (default work day hours) * 2 = 16 • Duration: 5 days, allocationType = fixedHours, fixedDisplayType = days, allocationValue = 2 (days), fixedHours = 8 (default work day hours) * 2 = 16

- Returns: `ResourceAssignments`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `resourceAssignment` | `CreateResourceAssignmentInput!` | - | The resource assignment to create |

#### `createResourcePlaceholder`

Create a new resource placeholder for the workspace.  Resource placeholders are virtual team members that can be assigned to projects and actions before actual people are hired or designated for those roles.  IMPORTANT: Only workspace administrators can set billRate and costRate values. Regular users can only set the name and roleTagId.  Use cases: • Planning projects before hiring specific team members • Creating role-based assignments in project templates   • Resource planning and capacity management • Budgeting and cost estimation for future roles  Parameters: • name: Required. The display name for the placeholder (e.g., "Senior Developer", "Marketing Manager") • workspaceId: Required. The workspace where this placeholder will be created • roleTagId: Optional. Associates the placeholder with a specific role/skill tag • billRate: Optional. The hourly billing rate (admin only) • costRate: Optional. The hourly cost rate (admin only)  Returns: The created ResourcePlaceholder object

- Returns: `ResourcePlaceholder!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `name` | `String!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `billRate` | `Float` | - | - |
| `costRate` | `Float` | - | - |
| `roleTagId` | `ID` | - | - |

#### `disableActionCustomFields`

Disables custom fields for actions in specific projects.  This should be used to disable only action itemType custom fields.  Parameters:   - customFieldIds: Required. The IDs of the custom fields to disable   - projectIds: Required. The IDs of the projects to disable the custom fields for   - workspaceId: Required. The ID of the workspace to disable the custom fields for   - removeFromActions: Optional. Whether to remove the custom fields from the actions

- Returns: `[Project!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `customFieldIds` | `[ID!]!` | - | - |
| `projectIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `removeFromActions` | `Boolean` | false | - |

#### `disableProjectsCustomFields`

Disables custom fields for specific projects.  This should be used to disable only project itemType custom fields.  Parameters:   - customFieldIds: Required. The IDs of the custom fields to disable   - projectIds: Required. The IDs of the projects to disable the custom fields for   - workspaceId: Required. The ID of the workspace to disable the custom fields for

- Returns: `[Project!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `customFieldIds` | `[ID!]!` | - | - |
| `projectIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |

#### `insertApprovalRound`

Create a new approval round with an initial empty stage for an action. The created stage will have no approvers initially - you'll need to use the deprecated changeApprovalStageApprover mutation to add approvers.

- Returns: `ApprovalRound`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to add the approval round to |
| `roundId` | `ID!` | - | Unique ID for the new approval round |
| `stageId` | `ID!` | - | Unique ID for the initial approval stage |

#### `insertApprovalStage`

Add a new empty approval stage to an existing approval round. The created stage will have no approvers initially - you'll need to use the changeApprovalItem mutation to add approvers.

- Returns: `ApprovalStage`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to add the stage to |
| `roundId` | `ID!` | - | ID of the approval round to add this stage to |
| `stageId` | `ID` | - | Optional unique ID for the new stage (will be auto-generated if not provided) |

#### `insertGroup`

Creates a new group.  It's very useful when there are no group that has the needed members.  Access: Requires user access to the workspace.  Parameters:   - workspace: ID of the workspace   - members: Array of user IDs   - teams: Array of team IDs   - name: Name of the group   - oneToOne: @deprecated do not use this parameter, use 'type' instead   - type: 'dm' (direct message) or 'group' (group chat) or 'thread'   - projectId: ID of the project  Examples: - Creating a direct message:   insertGroup(     workspace     members: ['user-id-1' (you), 'user-id-2' (other user)]     type: 'dm'   )  - Creating a group chat:   insertGroup(     workspace     members: ['user-id-1' (you), 'user-id-2' (other user), 'user-id-3' (other user)]     type: 'group'   )

- Returns: `Group`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `String!` | - | - |
| `members` | `[String!]!` | - | - |
| `teams` | `[String!]` | - | - |
| `name` | `String` | - | - |
| `oneToOne` | `Boolean` | - | - |
| `type` | `String` | - | - |
| `projectId` | `String` | - | - |

#### `insertMessage`

Creates a new message in a container (group, action, note, goal, or post).  Access: Requires user access to the container (or workspace if you are inserting using participants)  Parameters:   - _id: Random ID   - workspaceId: ID of the workspace (required for inserting in group container type using participants)   - containerId: ID of the container (id of group, action, note, goal, or post)   - containerType: Type of the container (group, action, note, goal, or post). You should always specify this parameter to avoid errors and confusion.   - body: body of the message, including mentions using <@userId> where userId is the actual userId   - mentions: Array of mentioned user IDs   - attachments: Array of file attachments   - userMentionsByGroup: Array of mentioned group IDs   - userMentionsByTeam: Array of mentioned team IDs  Examples: - Creating a message in a chat if you know group id:   insertMessage(     _id     containerId - Group ID     containerType - 'group'     body     mentions     attachments     body = "Hello <@sMoHY5KwWt44Xm8Sw>, how are you?"   )  - Creating a message in a DM chat if you know only participants and don't know containerId:   insertMessage(     _id     workspaceId - required for inserting using participants     participants - Array of user ids     containerType - 'group'     mentions     attachments     body = "Hello <@sMoHY5KwWt44Xm8Sw>, how are you?"   )  - Creating a comment in an action:   insertMessage(     _id     containerId - Action ID     containerType - 'action'.     mentions = ["sMoHY5KwWt44Xm8Sw"]     attachments     body = "Hello <@sMoHY5KwWt44Xm8Sw>, how are you?"   )  Returns the created message with all computed fields.

- Returns: `Message!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | - |
| `workspaceId` | `ID` | - | - |
| `containerId` | `ID` | - | - |
| `containerType` | `ContainerType` | group | Message container type. Only allowed values: action, group, note, workspace, goal, post |
| `participants` | `[ID!]` | [] | - |
| `mentions` | `[String]` | [] | pass userIds/teamIds which are mentioned in the message |
| `automated` | `Boolean` | false | - |
| `body` | `String!` | - | body of the message, including mentions with actual userId like <@sMoHY5KwWt44Xm8Sw> |
| `attachments` | `[Attachment]` | [] | - |
| `color` | `String` | - | - |
| `isNoteJsonComment` | `Boolean` | false | - |
| `isPrivate` | `Boolean` | false | - |
| `userMentionsByGroup` | `[ID!]` | [] | - |

#### `insertPost`

Creates a new news post.  You can also specify the category of the post and the attachment file id or even predefined reactions to post.  Access: Requires user access to the workspace  Examples: {   "body": "This is a <b>very exciting</b> news post",   "workspaceId": "7driFnaZjDQZndHqs",   "category": "news" }

- Returns: `Post!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | Post unique ID. Can be omitted, will be generated automatically |
| `body` | `String!` | - | Post body. Must be a valid HTML string |
| `workspaceId` | `ID!` | - | Workspace ID |
| `fileId` | `ID` | - | Attachment file ID. File should be pre-uploaded to Hive |
| `category` | `String` | - | Post category. Omit if you want to use no category |

#### `insertRecurringAction`

Create a recurring action. You must call insertActions first to create the action.  Parameters:   - actionId: ID of the action to make recurring (must exist)   - type: Recurrence type (daily, weekly, monthly, annually)   - startDate: Start date in ISO 8601 format   - endDate: End date in ISO 8601 format   - interval: Interval of recurrence (min: 1, max: 12)   - endingType: How recurrence ends (never, after, date)   - endingAfter: Number of occurrences before ending (min: 1, max: 52)   - days: Days of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun)   - showOnDueDate: Show the action on its due date (default: false)  Access: Requires user access to the action.  Errors: Throws error if action not found or user lacks permission.

- Returns: `RecurringAction`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to make recurring |
| `type` | `String` | - | Recurrence type (daily, weekly, monthly, annually) |
| `dayType` | `String` | - | Day type (calendar day, workday) |
| `startDate` | `Date` | - | Start date of the recurring action |
| `endDate` | `Date` | - | End date of the recurring action |
| `interval` | `Int` | - | Interval of recurrence (min: 1, max: 12) |
| `endingType` | `String` | - | How recurrence ends (never, after, date) |
| `endingAfter` | `Int` | - | Number of occurrences before ending (min: 1, max: 52) |
| `days` | `[String]` | - | Days of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun) |
| `showOnDueDate` | `Boolean` | - | Show the action on its due date |
| `recurringId` | `ID` | - | Existing recurring ID to link to |

#### `removeProjectOwner`

Remove a user from the project owner list.

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | Project ID to remove owner from |
| `ownerId` | `ID!` | - | User ID to remove as owner |
| `workspaceId` | `ID!` | - | Workspace ID of the project |

#### `requestApprovals`

Request approvals from all approvers in an approval round. Notifies approvers and marks the round as requested. Use this after setting up all stages and approvers to officially request their review.

- Returns: `ApprovalRound`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `roundId` | `ID!` | - | ID of the approval round to request approvals for |

#### `runWorkflow`

Apply an action template to an action

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workflowId` | `ID!` | - | - |
| `actionId` | `ID!` | - | - |

#### `salesforceOperation`

Unified Salesforce operation using jsforce SOAP/REST API. Supports query, search, insert, update, upsert, merge, describe, and lead conversion.  Access: Requires an authenticated Hive user with a connected Salesforce account.  ## Operation Examples:  ### QUERY ```graphql salesforceOperation(input: {   operation: QUERY   query: "SELECT Id, Name FROM Account LIMIT 10" }) ```  ### INSERT ```graphql salesforceOperation(input: {   operation: INSERT   objectType: "Account"   fields: [{ fieldName: "Name", fieldValue: "Acme Corp" }] }) ```  ### UPDATE ```graphql salesforceOperation(input: {   operation: UPDATE   objectType: "Account"   recordId: "001XXXXXXXXXXXXXXX"   fields: [{ fieldName: "Description", fieldValue: "Updated description" }] }) ```  ### DELETE ```graphql salesforceOperation(input: {   operation: DELETE   objectType: "Opportunity"   recordId: "006XXXXXXXXXXXXXXX" }) ```  ### SEARCH (SOSL) ```graphql salesforceOperation(input: {   operation: SEARCH   search: "FIND {Acme*} IN ALL FIELDS RETURNING Account(Id, Name), Contact(Id, Name)" }) ```  ### MERGE ```graphql salesforceOperation(input: {   operation: MERGE   objectType: "Account"   masterRecordId: "001XXXXXXXXXXXXXXX"   recordIdsToMerge: ["001YYYYYYYYYYYYYYY"] }) ```  ### DESCRIBE ```graphql salesforceOperation(input: {   operation: DESCRIBE   objectType: "Account" }) ```  ### CONVERT_LEAD ```graphql salesforceOperation(input: {   operation: CONVERT_LEAD   leadId: "00QXXXXXXXXXXXXXXX"   convertedStatus: "Qualified"   doNotCreateOpportunity: false }) ```  Errors:   - User is not logged in.   - Salesforce account is not connected.   - Invalid operation parameters.   - Salesforce API errors.

- Returns: `SalesforceOperationResult!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SalesforceOperationInput!` | - | - |

#### `setActionColor`

Set the color of an action to be used in the timeline view.

- Returns: `Action`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `actionColor` | `String!` | - | - |

#### `setCustomStatusColor`

This mutation is used to set the color of a custom status. ALWAYS run it after the addStatusToProjectView mutation (adding new status) to set the color of the new status. Pick the color that would logically fit the status name (e.g. "In Progress" -> "blue", "Done" -> "green", etc.).  Also could be used separately to update or remove the color of the status.

- Returns: `Workspace`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | The ID of the workspace |
| `status` | `String!` | - | The name of the status |
| `color` | `String` | - | The color of the status in HEX format. If not provided, the color will be removed. |

#### `setStoryPoints`

Set the agile story point value for an action  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to update   - storyPoints: The new story point value

- Returns: `Action`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `storyPoints` | `Int!` | - | - |

#### `unsetRecurringActions`

Make actions non-recurring by removing their recurring linkage. Stops future recurring instances from being generated while preserving the action.  Parameters:   - actionIds: Array of action IDs to make non-recurring   - workspaceId: The ID of the workspace  Access: Requires user access to the actions.  Errors: Throws error if user lacks edit permission on the actions.

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | Array of action IDs to make non-recurring |
| `workspaceId` | `ID!` | - | The ID of the workspace |

#### `updateActionGithubBranchNames`

Update the GitHub branch names associated with an action  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to update   - githubBranchNames: An array of branch names in the format "Repo:branch-name"  Returns: The updated action

- Returns: `Action`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `githubBranchNames` | `[String!]!` | - | - |

#### `updateActionProject`

Update the project for an action  Access: Requires user access to the action and target project  Parameters:   - actionId: The ID of the action to update   - projectId: The ID of the new project (null to unset)   - rank: Optional rank for the action in the new project  Returns: The updated action

- Returns: `Action`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `projectId` | `ID` | - | - |
| `rank` | `Float` | - | - |

#### `updateActionsMilestone`

- Returns: `Boolean`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `value` | `Boolean!` | - | - |

#### `updateActionSnoozeDate`

Update the snooze date for an action.  Snoozing an action temporarily hides it from the user's task list until the specified date. Pass null for snoozeDate to unsnooze (clear the snooze).  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to snooze   - snoozeDate: The date to snooze until (pass null to unsnooze)  Returns: The updated Action object with the new snoozeDate

- Returns: `Action`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `snoozeDate` | `Date` | - | - |

#### `updateDashboardV2`

Updates an existing dashboard with typed V2 filter input for Buzz/MCP endpoints. This mutation provides full schema introspection for AI assistants.

- Returns: `Dashboard`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | Dashboard ID to update |
| `title` | `String` | - | New dashboard title |
| `privacy` | `DashboardPrivacy` | - | New privacy setting |
| `projectIds` | `[ID]` | - | Updated project IDs for access |
| `sharingWith` | `[ID!]` | - | Updated user IDs to share with |
| `teams` | `[ID!]` | - | Updated team IDs to share with |
| `layout` | `[InputDashboardLayout!]` | - | Updated widget layout configuration |
| `filter` | `WidgetContainerFilterInputV2` | - | Updated global widget filter |
| `shareOnBehalfOfCreator` | `Boolean` | - | Whether to share on behalf of creator |
| `shareOnBehalfOfCreatorSettings` | `ShareOnBehalfOfCreatorSettingsInput` | - | - |
| `pinToUser` | `Boolean` | - | Whether to pin dashboard to user |
| `color` | `String` | - | Updated dashboard color |
| `allowedEmailDomains` | `[String!]` | - | Updated allowed email domains |
| `allowAccessToWhitelistedDomains` | `Boolean` | - | Whether to allow whitelisted domain access |
| `backgroundColor` | `DashboardBackgroundColor` | - | Updated background color |
| `backgroundImageUrl` | `String` | - | Updated background image URL |
| `backgroundImageCropType` | `DashboardBackgroundImageCropType` | - | Updated background image crop type |
| `displayTipsAndTricksFooter` | `Boolean` | - | Whether to display tips footer |
| `headerTextColor` | `DashboardHeaderTextColor` | - | Updated header text color |
| `type` | `DashboardType` | - | - |

#### `updateDashboardWidget`

Updates an existing dashboard widget's configuration. Common update scenarios: 1. Changing visualization type 2. Updating filters or data source 3. Modifying appearance settings 4. Adjusting metrics or calculations

- Returns: `DashboardWidget`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | - |
| `title` | `String` | - | - |
| `titleColor` | `String` | - | - |
| `titleSize` | `TextSize` | - | - |
| `url` | `String` | - | - |
| `sort` | `String` | - | - |
| `type` | `DashboardWidgetType` | - | - |
| `chartType` | `ChartType` | - | - |
| `slateJson` | `JSONObject` | - | - |
| `XAxis` | `DashboardWidgetXAxis` | - | - |
| `XAxisCustomFieldId` | `String` | - | - |
| `XAxisTitle` | `String` | - | - |
| `YAxis` | `DashboardWidgetYAxis` | - | - |
| `YAxisCustomFieldId` | `String` | - | - |
| `YAxisTitle` | `String` | - | - |
| `YAxisGroupBy` | `DashboardWidgetYAxis` | - | - |
| `groupByCustomFieldId` | `String` | - | - |
| `fileIds` | `[ID!]` | - | - |
| `noteId` | `String` | - | - |
| `portfolioViewId` | `String` | - | - |
| `hideHeader` | `Boolean` | - | - |
| `goalId` | `String` | - | - |
| `showTitles` | `Boolean` | - | - |
| `showLegend` | `Boolean` | - | - |
| `ignoreContainerFilter` | `Boolean` | - | - |
| `legendPosition` | `LegendPosition` | - | - |
| `showValueLabels` | `Boolean` | - | - |
| `showRowTotals` | `Boolean` | - | - |
| `showColumnTotals` | `Boolean` | - | - |
| `showFlattenedData` | `Boolean` | - | - |
| `showLinkedToProject` | `Boolean` | - | - |
| `truncateLongNumbers` | `Boolean` | - | - |
| `displayGroupsAs` | `DisplayGroupsAs` | - | - |
| `displayGoalsBy` | `DisplayGoalsBy` | - | - |
| `timeUnitsType` | `TimeUnit` | - | - |
| `projectTreeLevelsToShow` | `[Int!]` | - | - |
| `isProjectTreeLevelActive` | `Boolean` | - | - |
| `reportOn` | `DashboardWidgetReportOn` | - | - |
| `chartValueColors` | `[ChartValueColorInput!]` | - | - |
| `groupOthers` | `DashboardWidgetGroupOthersInput` | - | - |
| `projectId` | `String` | - | - |
| `buttonLabel` | `String` | - | - |
| `sectionHeaderText` | `String` | - | - |
| `sectionHeaderTextAlignment` | `TextAlignment` | - | - |
| `sectionHeaderLinePosition` | `SectionHeaderLinePosition` | - | - |
| `isHidden` | `Boolean` | - | - |
| `projectDetailsFields` | `[String!]` | - | - |
| `contentTextAlignment` | `TextAlignment` | - | - |
| `contentTextSize` | `TextSize` | - | - |
| `contentTextColorPrimary` | `String` | - | - |
| `contentTextColorSecondary` | `String` | - | - |
| `workspaceId` | `String` | - | - |
| `containerId` | `ID` | - | - |
| `colorThemeId` | `String` | - | - |
| `segmentColorOverrides` | `[SegmentColorOverrideInput!]` | - | - |
| `projectBudgetCategoryIds` | `[String]` | - | - |
| `projectBudgetDateRange` | `[Date!]` | - | - |
| `chartValuesState` | `[ChartValueStateInput!]` | - | - |

#### `updateMeetingUserData`

Update meeting user data using diff operations for array fields and direct values for scalars. Array fields (goals, nextSteps, materials, speakerLabels) accept add/remove/update diffs. Scalar fields (customTitle) accept direct values.

- Returns: `MeetingUserData`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `meetingExternalId` | `String!` | - | Calendar event ID from Google/Microsoft (e.g., 'abc123_20240115T140000Z') |
| `workspaceId` | `ID!` | - | Workspace ID where the meeting belongs |
| `goals` | `GoalDiff` | - | Diff operations for goals (add/remove/update) |
| `nextSteps` | `NextStepDiff` | - | Diff operations for next steps (add/remove/update) |
| `materials` | `MaterialDiff` | - | Diff operations for materials (add/remove/update) |
| `speakerLabels` | `SpeakerLabelDiff` | - | Diff operations for speaker labels (add/remove/update) |
| `customTitle` | `String` | - | User-set title override (pass null to clear) |

#### `updateMembersPermissions`

Add or remove members to/from a project.  Common use cases:   - Add a new member to a project   - Remove a member from a project   - Update the permission of a member   - Update the sharing type of a member   - Update the automated status of a member  Parameters:   - projectId: Required. The ID of the project to update members permissions for   - memberIds: Optional. The IDs of the users to add as members   - teamIds: Optional. The IDs of the teams to add as members   - permission: Required. The permission to set for the members.   - sharingType: Required. The sharing type to set for the members.   - isAutomated: Optional. Whether the update is automated. Default is false.  Examples: 1. Add a new member to a project   - projectId: 123   - memberIds: [456]   - permission: 'FULL_ACCESS'   - sharingType: 'custom'   - isAutomated: false  2. Remove a member from a project   - projectId: 123   - memberIds: [456]   - permission: 'REMOVE'   - sharingType: 'custom'   - isAutomated: false

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | Project ID to update members permissions for |
| `memberIds` | `[ID!]` | [] | User IDs to add as members |
| `teamIds` | `[ID!]` | [] | Team IDs to add as members |
| `permission` | `String!` | - | Permission to set for the members. Can be one of FULL_ACCESS, MAKE_OWNER, READ_ONLY, REMOVE. |
| `sharingType` | `String!` | - | Sharing type to set for the members. Can be one of custom, everyone, me. |
| `isAutomated` | `Boolean` | false | - |

#### `updateProjectArchived`

Update project archived status  Access: Requires user access to the project  Parameters:   - projectId: The ID of the project to update   - archived: The new archived state to set   - includeChildren: Whether to include children in the update  Returns: The updated project

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | - |
| `archived` | `Boolean!` | - | - |
| `includeChildren` | `Boolean` | false | - |

#### `updateProjectDescription`

- Returns: `Project`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | - |
| `description` | `String!` | - | - |

#### `updateProjectsCustomFields`

Enables custom fields for specific projects.  This should be used to enable only project itemType custom fields.  Parameters:   - projectIds: Required. The IDs of the projects to add the custom fields to   - workspaceId: Required. The ID of the workspace to add the custom fields to   - fields: Required. The custom fields to add to the projects

- Returns: `[Project!]!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectIds` | `[ID!]!` | - | projects ids associated with custom field |
| `workspaceId` | `ID!` | - | workspace associated with projectIds |
| `fields` | `[CustomFieldItemInput!]!` | - | custom field to update |

#### `updateResourceAssignment`

Update a resource assignment. ALWAYS use search to find the resource assignment before updating it. If the resource assignment is not found, DONT RUN THE MUTATION. If the resource assignment is found, update resource assignment.

- Returns: `ResourceAssignments`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` | - | The id of the resource assignment to update |
| `workspaceId` | `ID!` | - | The workspace id |
| `resourceAssignment` | `UpdateResourceAssignmentInput!` | - | The resource assignment to update |

#### `updateResourcePlaceholder`

Update an existing resource placeholder's properties.  This allows modification of placeholder details while preserving the placeholder's identity and existing assignments.  IMPORTANT: Only workspace administrators can modify billRate and costRate values. Regular users can only update the name and roleTagId.  Common use cases: • Refining placeholder role names for clarity • Updating role assignments as requirements change • Adjusting billing/cost rates (admin only) • Associating placeholders with different role tags  Parameters: • id: Required. The ID of the resource placeholder to update • name: Optional. New display name for the placeholder • roleTagId: Optional. New role/skill tag association (can be null to remove) • billRate: Optional. New hourly billing rate (admin only) • costRate: Optional. New hourly cost rate (admin only)  Returns: The updated ResourcePlaceholder object

- Returns: `ResourcePlaceholder!`
- Deprecated: no

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` | - | - |
| `name` | `String` | - | - |
| `billRate` | `Float` | - | - |
| `costRate` | `Float` | - | - |
| `roleTagId` | `ID` | - | - |

## Subscriptions

Root type: `Subscription`

Total operations: **0**

| Operation | Args | Returns | Deprecated |
|---|---|---|---|

### Details
