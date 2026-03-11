# `getTimesheetsToApprove`

- Type: `query`
- Returns: `[GroupedTimesheet!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for the "My approvals" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns [] if doesn't have access or user with requested userId doesn't exist

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `startDate` | `Date!` | - | start of period for which data should be retrieved.  NOTE: Should be equal to start of the week date in requested workspace, works as an exact date match, not as a date range |
| `endDate` | `Date!` | - | end of period for which data should be retrieved.  NOTE: Should be equal to end of the week date in requested workspace, works as an exact date match, not as a date range |
| `grouping` | `TimesheetGrouping!` | - | parameter to group by |
| `statuses` | `[TimesheetStatus!]` | - | statuses to filter by |

## Signature

- `getTimesheetsToApprove(workspaceId: ID!, startDate: Date!, endDate: Date!, grouping: TimesheetGrouping!, statuses: [TimesheetStatus!])` -> `[GroupedTimesheet!]!`
