# `getActionsByWorkspace`

- Type: `query`
- Returns: `ActionConnector`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Returns a paginated list of actions by workspaceId and ID/simpleId

## Arguments

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

## Signature

- `getActionsByWorkspace(workspaceId: ID!, text: String, first: Int, last: Int, before: ID, after: ID, status: String, archived: Boolean, projectIds: [ID], excludeProjectIds: [ID], specificIds: [ID!], assignees: [ID!], labels: [ID!], includeChildProjects: Boolean, excludeCompletedActions: Boolean, excludeSnoozedActions: Boolean, createdAtStart: Date, createdAtEnd: Date, startDate: Date, endDate: Date, includePrivate: Boolean, parent: ID, sortField: String, sortOrder: Int, milestone: Boolean, customFieldId: ID, customFieldValue: String)` -> `ActionConnector`
