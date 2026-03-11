# `recoverTimesheet`

- Type: `mutation`
- Returns: `Timesheet`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for recovering timesheets in "timesheet" tab in "Timesheets" app. Right after removing should appear toast with "recover" button  Access: It requires user access.  Errors: Returns specific expected errors if:  deleted timesheet item doesn't exist, user is not timesheet submitter and returns null if user doesn't have access to workspace

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | timesheetId to recover |
| `workspaceId` | `ID!` | - | workspace associated with timesheet |

## Signature

- `recoverTimesheet(_id: ID!, workspaceId: ID!)` -> `Timesheet`
