# `bulkUpdateActionsType`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `actionIds` | `[ID!]!` | - | - |
| `type` | `ActionTypeEnum` | - | - |
| `rank` | `Float` | - | - |

## Signature

- `bulkUpdateActionsType(workspaceId: ID!, actionIds: [ID!]!, type: ActionTypeEnum, rank: Float)` -> `Boolean`
