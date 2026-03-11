# `getTimesheetApprovals`

- Type: `query`
- Returns: `TimesheetConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

paginated resolver for the timesheet approval log.  Used for approvals log in "Timesheets" app.  Access: It has admin access.  Errors: Returns empty paginated response if is not workspace admin.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `first` | `Int` | 20 | amount of items per request |
| `after` | `ID` | - | last item from previous request |

## Signature

- `getTimesheetApprovals(workspaceId: ID!, first: Int, after: ID)` -> `TimesheetConnection!`
