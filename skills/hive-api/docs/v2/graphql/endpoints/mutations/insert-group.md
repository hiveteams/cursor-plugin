# `insertGroup`

- Type: `mutation`
- Returns: `Group`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates a new group.  It's very useful when there are no group that has the needed members.  Access: Requires user access to the workspace.  Parameters:   - workspace: ID of the workspace   - members: Array of user IDs   - teams: Array of team IDs   - name: Name of the group   - oneToOne: @deprecated do not use this parameter, use 'type' instead   - type: 'dm' (direct message) or 'group' (group chat) or 'thread'   - projectId: ID of the project  Examples: - Creating a direct message:   insertGroup(     workspace     members: ['user-id-1' (you), 'user-id-2' (other user)]     type: 'dm'   )  - Creating a group chat:   insertGroup(     workspace     members: ['user-id-1' (you), 'user-id-2' (other user), 'user-id-3' (other user)]     type: 'group'   )

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `String!` | - | - |
| `members` | `[String!]!` | - | - |
| `teams` | `[String!]` | - | - |
| `name` | `String` | - | - |
| `oneToOne` | `Boolean` | - | - |
| `type` | `String` | - | - |
| `projectId` | `String` | - | - |

## Signature

- `insertGroup(workspace: String!, members: [String!]!, teams: [String!], name: String, oneToOne: Boolean, type: String, projectId: String)` -> `Group`
