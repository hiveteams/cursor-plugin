# `approvalRounds`

- Type: `query`
- Returns: `ApprovalRoundConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Retrieve all approval rounds for a specific action. Returns a paginated list of approval rounds. Use this to view existing approval rounds on an action before modifying stages or approvers.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to get approval rounds for |
| `first` | `Int` | 20 | Maximum number of rounds to return (default: 60) |
| `last` | `Int` | - | Maximum number of rounds to return from the end |
| `before` | `ID` | - | Cursor to return rounds before |
| `after` | `ID` | - | Cursor to return rounds after |

## Signature

- `approvalRounds(actionId: ID!, first: Int, last: Int, before: ID, after: ID)` -> `ApprovalRoundConnection!`
