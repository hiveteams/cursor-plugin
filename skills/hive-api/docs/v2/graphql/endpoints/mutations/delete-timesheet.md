# `deleteTimesheet`

- Type: `mutation`
- Returns: `Timesheet`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for deleting timesheets in "timesheet" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: not deleted timesheet item doesn't exist, user is not timesheet submitter

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | timesheetId to delete |
| `workspaceId` | `ID!` | - | workspace associated with timesheet |

## Signature

- `deleteTimesheet(_id: ID!, workspaceId: ID!)` -> `Timesheet`
