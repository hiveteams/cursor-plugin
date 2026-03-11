# `deleteTimesheetComment`

- Type: `mutation`
- Returns: `Timesheet`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for removing existing comments in comment modal in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: not deleted and not marked as history item timesheet doesn't exist, user trying to delete comment that he didn't create

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timesheetId` | `ID!` | - | timesheetsId with which comment is associated |
| `isManager` | `Boolean` | - | variable to detect should managerComment be updated or creatorComment.  By default false |

## Signature

- `deleteTimesheetComment(timesheetId: ID!, isManager: Boolean)` -> `Timesheet`
