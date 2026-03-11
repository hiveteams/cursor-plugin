# `createTimeEntries`

- Type: `mutation`
- Returns: `CreateTimeEntriesResult!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `entries` | `[CreateTimeEntryInput!]!` | - | - |
| `status` | `TimesheetStatus` | - | - |

## Signature

- `createTimeEntries(workspaceId: ID!, entries: [CreateTimeEntryInput!]!, status: TimesheetStatus)` -> `CreateTimeEntriesResult!`
