# `getTimeTrackingData`

- Type: `query`
- Returns: `TimeTrackingData!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for querying time tracking data in "Time-tracking" tab in "Timesheets" app.  Access: It requires user access.  Errors: Returns specific expected errors if: user doesn't have access to workspace or not logged then returns { projects: [], actions: [] }

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | related workspace |
| `startDate` | `Date` | - | start of period for which data should be retrieved. |
| `endDate` | `Date` | - | end of period for which data should be retrieved. |

## Signature

- `getTimeTrackingData(workspaceId: ID!, startDate: Date, endDate: Date)` -> `TimeTrackingData!`
