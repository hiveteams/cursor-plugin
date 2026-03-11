# `updateMembersPermissions`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Add or remove members to/from a project.  Common use cases:   - Add a new member to a project   - Remove a member from a project   - Update the permission of a member   - Update the sharing type of a member   - Update the automated status of a member  Parameters:   - projectId: Required. The ID of the project to update members permissions for   - memberIds: Optional. The IDs of the users to add as members   - teamIds: Optional. The IDs of the teams to add as members   - permission: Required. The permission to set for the members.   - sharingType: Required. The sharing type to set for the members.   - isAutomated: Optional. Whether the update is automated. Default is false.  Examples: 1. Add a new member to a project   - projectId: 123   - memberIds: [456]   - permission: 'FULL_ACCESS'   - sharingType: 'custom'   - isAutomated: false  2. Remove a member from a project   - projectId: 123   - memberIds: [456]   - permission: 'REMOVE'   - sharingType: 'custom'   - isAutomated: false

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `projectId` | `ID!` | - | Project ID to update members permissions for |
| `memberIds` | `[ID!]` | [] | User IDs to add as members |
| `teamIds` | `[ID!]` | [] | Team IDs to add as members |
| `permission` | `String!` | - | Permission to set for the members. Can be one of FULL_ACCESS, MAKE_OWNER, READ_ONLY, REMOVE. |
| `sharingType` | `String!` | - | Sharing type to set for the members. Can be one of custom, everyone, me. |
| `isAutomated` | `Boolean` | false | - |

## Signature

- `updateMembersPermissions(projectId: ID!, memberIds: [ID!], teamIds: [ID!], permission: String!, sharingType: String!, isAutomated: Boolean)` -> `Project`
