# `getTimesheetEstimatedTime`

- Type: `query`
- Returns: `[TimesheetEstimatedTimeEntry!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used to retrieve estimated time from action estimates for multiple containers within a date range. Returns estimated time entries that can be built into a nested structure on the client. Follows the same pattern as getTimesheetTrackedTime but uses action estimates instead of tracked time.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `containerIds` | `[ID]!` | - | array of container IDs to get estimated time for |
| `containerType` | `TimesheetContainer!` | - | type of container (PROJECT, LEAVE) |
| `userIds` | `[ID!]!` | - | array of user IDs to get estimated time for |
| `startDate` | `Date!` | - | start date of the range to get estimated time for |
| `endDate` | `Date!` | - | end date of the range to get estimated time for |

## Signature

- `getTimesheetEstimatedTime(workspaceId: ID!, containerIds: [ID]!, containerType: TimesheetContainer!, userIds: [ID!]!, startDate: Date!, endDate: Date!)` -> `[TimesheetEstimatedTimeEntry!]!`
