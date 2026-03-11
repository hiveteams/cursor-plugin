# `getTimesheetTrackedTime`

- Type: `query`
- Returns: `[TimesheetTrackedTimeEntry!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used to retrieve tracked time for multiple containers within a date range. Returns tracked time entries that can be built into a nested structure on the client.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |
| `containerIds` | `[ID]!` | - | array of container IDs to get tracked time for |
| `containerType` | `TimesheetContainer!` | - | type of container (PROJECT, LEAVE) |
| `userIds` | `[ID!]!` | - | array of user IDs to get tracked time for |
| `startDate` | `Date!` | - | start date of the range to get tracked time for |
| `endDate` | `Date!` | - | end date of the range to get tracked time for |

## Signature

- `getTimesheetTrackedTime(workspaceId: ID!, containerIds: [ID]!, containerType: TimesheetContainer!, userIds: [ID!]!, startDate: Date!, endDate: Date!)` -> `[TimesheetTrackedTimeEntry!]!`
