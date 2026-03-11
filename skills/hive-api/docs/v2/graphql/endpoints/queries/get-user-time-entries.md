# `getUserTimeEntries`

- Type: `query`
- Returns: `TimeEntryConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Usage: Allows user to pull time entries for the specified userId in a given time range  Access: Requires workspace admin access  Errors: Returns an error if not a workspace administrator.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `userId` | `ID!` | - | user ID to get time entries for |
| `workspaceId` | `ID!` | - | workspace ID to get time entries for |
| `startDate` | `Date!` | - | start date - can be any date value and will perform a $gte match against this start date |
| `endDate` | `Date!` | - | end date - can be any date value and will perform a $lte match against this end date |
| `status` | `TimesheetStatus` | - | optional status of the corresponding timesheet to filter time entries by |
| `containerId` | `ID` | - | optional container ID to filter time entries by |
| `containerType` | `TimesheetContainer` | - | optional container type to filter time entries by |
| `categoryId` | `ID` | - | optional category ID to filter time entries by |
| `first` | `Int` | - | optional pagination - will return a maximum of 10,000 time entries without paginating |
| `last` | `Int` | - | optional pagination - will return a maximum of 10,000 time entries without paginating |
| `before` | `ID` | - | optional pagination - return entries before the specified ID |
| `after` | `ID` | - | optional pagination - return entries after the specified ID |
| `sortOrder` | `Int` | 1 | optional sort order - defaults to 1 (ascending) |
| `filterBy` | `TimeEntriesFilter` | date | optional filter field - defaults to date |

## Signature

- `getUserTimeEntries(userId: ID!, workspaceId: ID!, startDate: Date!, endDate: Date!, status: TimesheetStatus, containerId: ID, containerType: TimesheetContainer, categoryId: ID, first: Int, last: Int, before: ID, after: ID, sortOrder: Int, filterBy: TimeEntriesFilter)` -> `TimeEntryConnection`
