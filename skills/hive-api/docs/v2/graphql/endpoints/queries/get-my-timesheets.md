# `getMyTimesheets`

- Type: `query`
- Returns: `[Timesheet!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for the "Timesheet" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns [] if doesn't have access or user with requested userId doesn't exist.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `startDate` | `Date!` | - | start of period for which data should be retrieved.  NOTE: Should be equal to start of the week date in requested workspace, works as an exact date match, not as a date range |
| `endDate` | `Date!` | - | end of period for which data should be retrieved.  NOTE: Should be equal to end of the week date in requested workspace, works as an exact date match, not as a date range |
| `userId` | `ID` | - | user whose data we want to retrieve, if not sent using current user data |
| `rootTimesheetCreatedAt` | `Date` | - | Client's local date used to determine sorting order for the root timesheet's creation date |
| `includeEstimatedActions` | `Boolean` | true | whether to include estimated actions without tracked time |

## Signature

- `getMyTimesheets(workspaceId: ID!, startDate: Date!, endDate: Date!, userId: ID, rootTimesheetCreatedAt: Date, includeEstimatedActions: Boolean)` -> `[Timesheet!]!`
