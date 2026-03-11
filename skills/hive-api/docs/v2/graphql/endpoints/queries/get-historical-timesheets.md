# `getHistoricalTimesheets`

- Type: `query`
- Returns: `[Timesheet!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for edit log in "Manage" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns [] if not logged in or doesn't have access to workspace.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `userId` | `ID!` | - | associated userId |
| `startDate` | `Date!` | - | start of period for which data should be retrieved.  NOTE: Should be equal to start of the week date in requested workspace, works as an exact date match, not as a date range |
| `endDate` | `Date!` | - | end of period for which data should be retrieved.  NOTE: Should be equal to end of the week date in requested workspace, works as an exact date match, not as a date range |

## Signature

- `getHistoricalTimesheets(workspaceId: ID!, userId: ID!, startDate: Date!, endDate: Date!)` -> `[Timesheet!]!`
