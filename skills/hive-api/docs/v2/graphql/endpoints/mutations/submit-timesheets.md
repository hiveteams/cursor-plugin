# `submitTimesheets`

- Type: `mutation`
- Returns: `[Timesheet!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for submit timesheets button timesheets in "timesheet" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: timesheets array is empty, user is not logged in, user doesn't have access to workspace, user trying to submit timesheets beyond 4 weeks period from start of current week, userId is different from current userId and user is not admin for current workspace, if one of timesheets is locked, approved or waiting for approval

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | workspace associated with timesheets |
| `userId` | `ID!` | - | user associated with timesheets |
| `startDate` | `Date!` | - | start of period for which data should be retrieved.  NOTE: Should be equal to start of the week date in requested workspace, works as an exact date match, not as a date range |
| `endDate` | `Date!` | - | end of period for which data should be retrieved.  NOTE: Should be equal to end of the week date in requested workspace, works as an exact date match, not as a date range |
| `timesheets` | `[TimesheetInput!]!` | - | timesheets to submit |
| `isEditMode` | `Boolean` | - | Edit mode for admins |
| `includeEstimatedActions` | `Boolean` | true | whether to include estimated actions without tracked time |

## Signature

- `submitTimesheets(workspaceId: ID!, userId: ID!, startDate: Date!, endDate: Date!, timesheets: [TimesheetInput!]!, isEditMode: Boolean, includeEstimatedActions: Boolean)` -> `[Timesheet!]!`
