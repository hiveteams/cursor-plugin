# `updateTimeEntry`

- Type: `mutation`
- Returns: `TimeEntry`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `timesheetId` | `ID!` | - | - |
| `date` | `Date!` | - | - |
| `loggedTime` | `Int!` | - | - |
| `snapshot` | `[TimeEntrySnapshotItemInput!]` | - | - |

## Signature

- `updateTimeEntry(timesheetId: ID!, date: Date!, loggedTime: Int!, snapshot: [TimeEntrySnapshotItemInput!])` -> `TimeEntry`
