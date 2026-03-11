# `addCreatorComment`

- Type: `mutation`
- Returns: `Timesheet`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for creating creator comments in comment modal in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: not deleted and not marked as history item timesheet doesn't exist, user trying to create comment for timesheet that he didn't create, $text variable is empty string after trim spaces

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timesheetId` | `ID!` | - | timesheetsId where creatorComment should be created |
| `text` | `String!` | - | text of comment |

## Signature

- `addCreatorComment(timesheetId: ID!, text: String!)` -> `Timesheet`
