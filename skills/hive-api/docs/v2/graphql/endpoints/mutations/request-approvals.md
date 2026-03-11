# `requestApprovals`

- Type: `mutation`
- Returns: `ApprovalRound`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Request approvals from all approvers in an approval round. Notifies approvers and marks the round as requested. Use this after setting up all stages and approvers to officially request their review.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `roundId` | `ID!` | - | ID of the approval round to request approvals for |

## Signature

- `requestApprovals(roundId: ID!)` -> `ApprovalRound`
