# `getProjectIds`

- Type: `query`
- Returns: `[String]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `specificIds` | `[ID]` | - | - |
| `excludedIds` | `[ID]` | - | - |
| `includeTemplates` | `Boolean` | - | - |
| `includeReadOnly` | `Boolean` | - | - |
| `publicOnly` | `Boolean` | - | - |

## Signature

- `getProjectIds(workspaceId: ID!, specificIds: [ID], excludedIds: [ID], includeTemplates: Boolean, includeReadOnly: Boolean, publicOnly: Boolean)` -> `[String]!`
