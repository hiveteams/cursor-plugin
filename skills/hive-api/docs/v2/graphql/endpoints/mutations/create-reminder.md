# `createReminder`

- Type: `mutation`
- Returns: `Reminder!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a new reminder  Examples:  Create a one time reminder for 5 minutes from now Now: 2025-09-17T20:22:00.000Z {   "text": "Remind me to check in on Beta Deploy",   "userIds": ["some_user_id"],   "recurrenceDefinition": {     "type":"daily",     "interval":1,     "days":["Wed","Thu","Fri","Sat","Sun","Mon","Tue"],     "startDate":"2025-09-17T20:27:00.000Z",     "endingType":"after",     "endingAfter":1   },   "workspaceId": "REDACTED_WORKSPACE_ID",   originType: "buzzThread",   originId: "some_buzz_thread_id" }  Create a recurring reminder for every 2 days with no end Now: 2025-09-17T20:22:00.000Z {   "text": "Remind me to check in on Beta Deploy",   "userIds": ["some_user_id"],   "recurrenceDefinition": {     "type":"daily",     "interval":2,     "days":["Wed","Thu","Fri","Sat","Sun","Mon","Tue"],     "startDate":"2025-09-17T20:27:00.000Z",     "endingType":"never",   },   "workspaceId": "REDACTED_WORKSPACE_ID",   originType: "buzzThread",   originId: "some_buzz_thread_id" }

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `text` | `String!` | - | - |
| `userIds` | `[ID!]!` | - | - |
| `recurrenceDefinition` | `RecurrenceDefinitionInput!` | - | - |
| `workspaceId` | `ID!` | - | - |
| `originType` | `ReminderOriginType!` | - | - |
| `originId` | `ID!` | - | - |

## Signature

- `createReminder(text: String!, userIds: [ID!]!, recurrenceDefinition: RecurrenceDefinitionInput!, workspaceId: ID!, originType: ReminderOriginType!, originId: ID!)` -> `Reminder!`
