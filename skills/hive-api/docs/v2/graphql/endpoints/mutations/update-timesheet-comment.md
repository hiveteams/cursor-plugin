# `updateTimesheetComment`

- Type: `mutation`
- Returns: `Timesheet`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for updating existing comments in comment modal in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: not deleted and not marked as history item timesheet doesn't exist, user trying to update comment that he didn't create, $text variable is empty string after trim spaces

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timesheetId` | `ID!` | - | timesheetsId with which comment is associated |
| `text` | `String!` | - | text of updated comment |
| `isManager` | `Boolean` | - | variable to detect should managerComment be updated or creatorComment.  By default false |

## Signature

- `updateTimesheetComment(timesheetId: ID!, text: String!, isManager: Boolean)` -> `Timesheet`
