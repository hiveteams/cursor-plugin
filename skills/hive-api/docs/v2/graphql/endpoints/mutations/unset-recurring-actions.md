# `unsetRecurringActions`

- Type: `mutation`
- Returns: `Boolean`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Make actions non-recurring by removing their recurring linkage. Stops future recurring instances from being generated while preserving the action.  Parameters:   - actionIds: Array of action IDs to make non-recurring   - workspaceId: The ID of the workspace  Access: Requires user access to the actions.  Errors: Throws error if user lacks edit permission on the actions.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | Array of action IDs to make non-recurring |
| `workspaceId` | `ID!` | - | The ID of the workspace |

## Signature

- `unsetRecurringActions(actionIds: [ID!]!, workspaceId: ID!)` -> `Boolean`
