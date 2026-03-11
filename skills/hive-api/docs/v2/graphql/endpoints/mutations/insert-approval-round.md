# `insertApprovalRound`

- Type: `mutation`
- Returns: `ApprovalRound`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a new approval round with an initial empty stage for an action. The created stage will have no approvers initially - you'll need to use the deprecated changeApprovalStageApprover mutation to add approvers.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to add the approval round to |
| `roundId` | `ID!` | - | Unique ID for the new approval round |
| `stageId` | `ID!` | - | Unique ID for the initial approval stage |

## Signature

- `insertApprovalRound(actionId: ID!, roundId: ID!, stageId: ID!)` -> `ApprovalRound`
