# `isAdminOrManagerOrProjectCreator`

- Type: `query`
- Returns: `Boolean!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Check does a current user can view unsubmitted timesheet data  Access: Requires to be organization/workspace admin, user manager or project owner  Errors: Returns false if requester isn't identified.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | associated workspaceId |

## Signature

- `isAdminOrManagerOrProjectCreator(workspaceId: ID!)` -> `Boolean!`
