# `bulkUpdateTimesheetStatus`

- Type: `mutation`
- Returns: `[Timesheet!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for approve/request changes of timesheets in "My approvals" tab "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: returns [] if user not logged in or doesn't have access to workspace, related timesheet docs with status different to Unsubmitted not found, user is not timesheet approval

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | workspace associated with timesheets |
| `timesheets` | `[UpdateStatusTimesheetInput!]!` | - | timesheets to approve/request changes |

## Signature

- `bulkUpdateTimesheetStatus(workspaceId: ID!, timesheets: [UpdateStatusTimesheetInput!]!)` -> `[Timesheet!]!`
