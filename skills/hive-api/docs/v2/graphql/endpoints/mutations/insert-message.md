# `insertMessage`

- Type: `mutation`
- Returns: `Message!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates a new message in a container (group, action, note, goal, or post).  Access: Requires user access to the container (or workspace if you are inserting using participants)  Parameters:   - _id: Random ID   - workspaceId: ID of the workspace (required for inserting in group container type using participants)   - containerId: ID of the container (id of group, action, note, goal, or post)   - containerType: Type of the container (group, action, note, goal, or post). You should always specify this parameter to avoid errors and confusion.   - body: body of the message, including mentions using <@userId> where userId is the actual userId   - mentions: Array of mentioned user IDs   - attachments: Array of file attachments   - userMentionsByGroup: Array of mentioned group IDs   - userMentionsByTeam: Array of mentioned team IDs  Examples: - Creating a message in a chat if you know group id:   insertMessage(     _id     containerId - Group ID     containerType - 'group'     body     mentions     attachments     body = "Hello <@sMoHY5KwWt44Xm8Sw>, how are you?"   )  - Creating a message in a DM chat if you know only participants and don't know containerId:   insertMessage(     _id     workspaceId - required for inserting using participants     participants - Array of user ids     containerType - 'group'     mentions     attachments     body = "Hello <@sMoHY5KwWt44Xm8Sw>, how are you?"   )  - Creating a comment in an action:   insertMessage(     _id     containerId - Action ID     containerType - 'action'.     mentions = ["sMoHY5KwWt44Xm8Sw"]     attachments     body = "Hello <@sMoHY5KwWt44Xm8Sw>, how are you?"   )  Returns the created message with all computed fields.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | - |
| `workspaceId` | `ID` | - | - |
| `containerId` | `ID` | - | - |
| `containerType` | `ContainerType` | group | Message container type. Only allowed values: action, group, note, workspace, goal, post |
| `participants` | `[ID!]` | [] | - |
| `mentions` | `[String]` | [] | pass userIds/teamIds which are mentioned in the message |
| `automated` | `Boolean` | false | - |
| `body` | `String!` | - | body of the message, including mentions with actual userId like <@sMoHY5KwWt44Xm8Sw> |
| `attachments` | `[Attachment]` | [] | - |
| `color` | `String` | - | - |
| `isNoteJsonComment` | `Boolean` | false | - |
| `isPrivate` | `Boolean` | false | - |
| `userMentionsByGroup` | `[ID!]` | [] | - |

## Signature

- `insertMessage(_id: ID, workspaceId: ID, containerId: ID, containerType: ContainerType, participants: [ID!], mentions: [String], automated: Boolean, body: String!, attachments: [Attachment], color: String, isNoteJsonComment: Boolean, isPrivate: Boolean, userMentionsByGroup: [ID!])` -> `Message!`
