# `setTimesheetLock`

- Type: `mutation`
- Returns: `Timesheet`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for locking/unlocking editing of timesheets in "Manage" tab "Timesheets" app.  Access: Requires workspace admin access  Errors: Returns specific expected errors if: error if user is not workspace admin, returns null if is not logged in or not deleted not history timesheet with status different to Unsubmitted not found

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timesheetId` | `ID!` | - | id of timesheet to lock/unlock |
| `locked` | `Boolean!` | - | lock/unlock state variable |

## Signature

- `setTimesheetLock(timesheetId: ID!, locked: Boolean!)` -> `Timesheet`
