# `createScheduledMailMessage`

- Type: `mutation`
- Returns: `ResidentMailMessage!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a scheduled mail message to be sent at a specified time. The message will be stored and processed by the scheduled mail processor.  **Access:** Requires authenticated user. User must have valid mail provider credentials.  **Errors:** - User is not logged in - Access denied - If the user does not own the specified email address.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `scheduledSendTime` | `Date!` | - | - |
| `email` | `String!` | - | - |
| `body` | `String!` | - | - |
| `subject` | `String!` | - | - |
| `snippet` | `String!` | - | - |
| `threadId` | `ID` | - | - |
| `messageId` | `ID` | - | - |
| `inReplyTo` | `ID` | - | - |
| `references` | `[ID!]!` | - | - |
| `actionId` | `ID` | - | - |
| `parentThreadId` | `ID` | - | id of actions.addMailMessage.threadId where reply was created. It's used prevent action thread duplication when user replies unowned thread and recipient is a thread owner. |

## Signature

- `createScheduledMailMessage(scheduledSendTime: Date!, email: String!, body: String!, subject: String!, snippet: String!, threadId: ID, messageId: ID, inReplyTo: ID, references: [ID!]!, actionId: ID, parentThreadId: ID)` -> `ResidentMailMessage!`
