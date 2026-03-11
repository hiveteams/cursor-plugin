# `getTimeCategories`

- Type: `query`
- Returns: `[TimeCategory!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `projectId` | `ID` | - | - |
| `specificIds` | `[ID!]` | [] | - |
| `includeSubmitted` | `Boolean` | false | - |
| `onlyBillable` | `Boolean` | false | - |

## Signature

- `getTimeCategories(workspaceId: ID!, projectId: ID, specificIds: [ID!], includeSubmitted: Boolean, onlyBillable: Boolean)` -> `[TimeCategory!]!`
