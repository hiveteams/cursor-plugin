# `getTimesheetComments`

- Type: `query`
- Returns: `TimesheetComments`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for querying timesheet comments in timesheet comment modal in "timesheet" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: timesheet not found, user doesn't have access to workspace

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timesheetId` | `ID!` | - | timesheet to get comments from |

## Signature

- `getTimesheetComments(timesheetId: ID!)` -> `TimesheetComments`
