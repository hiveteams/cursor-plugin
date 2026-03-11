# `getTimesheets`

- Type: `query`
- Returns: `TimesheetConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used for querying timesheets by date

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `startDate` | `Date!` | - | start of period for which data should be retrieved. |
| `endDate` | `Date!` | - | end of period for which data should be retrieved. |
| `status` | `TimesheetStatus` | - | status of timesheets to retrieve |
| `first` | `Int` | 20 | amount of items per request. default: 20 |
| `after` | `ID` | - | last item from previous request |

## Signature

- `getTimesheets(workspaceId: ID!, startDate: Date!, endDate: Date!, status: TimesheetStatus, first: Int, after: ID)` -> `TimesheetConnection!`
