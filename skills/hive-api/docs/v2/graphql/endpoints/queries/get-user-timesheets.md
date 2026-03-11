# `getUserTimesheets`

- Type: `query`
- Returns: `[Timesheet!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for the "Manage" tab in "Timesheets" app.  Access: Requires workspace admin access  Errors: Returns [] if not a workspace admin.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `userId` | `ID!` | - | user whose data we want to retrieve |
| `startDate` | `Date!` | - | start of period for which data should be retrieved.  NOTE: Should be equal to start of the week date in requested workspace, works as an exact date match, not as a date range |
| `endDate` | `Date!` | - | end of period for which data should be retrieved.  NOTE: Should be equal to end of the week date in requested workspace, works as an exact date match, not as a date range |

## Signature

- `getUserTimesheets(workspaceId: ID!, userId: ID!, startDate: Date!, endDate: Date!)` -> `[Timesheet!]!`
