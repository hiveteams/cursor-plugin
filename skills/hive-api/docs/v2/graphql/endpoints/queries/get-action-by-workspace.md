# `getActionByWorkspace`

- Type: `query`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get an action by ID/simpleId and workspaceId  Access: Requires user access to the action  Parameters:   - actionId: The ID or simpleId of the action to retrieve   - workspaceId: The ID of the workspace to retrieve the action from.  Returns: The requested action

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `String!` | - | - |
| `workspaceId` | `ID!` | - | - |

## Signature

- `getActionByWorkspace(actionId: String!, workspaceId: ID!)` -> `Action`
