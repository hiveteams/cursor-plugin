# `currentRoundAndStage`

- Type: `query`
- Returns: `CurrentRoundAndStageReturn`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get the currently active approval round and stage for an action. Returns the round that has been requested but not yet fully approved, along with its active stage. Use this to quickly check the current approval state of an action without fetching all rounds and stages separately. The approvalStage contains the list of approvers and their statuses - check each approval item's status field to see who still needs to approve.  May return null when the action is not accessible to the caller, when there are no approval rounds, or when there is no stage currently awaiting approvals. A null result indicates no active approvals for the specified action.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to get the current approval round and stage for |

## Signature

- `currentRoundAndStage(actionId: ID!)` -> `CurrentRoundAndStageReturn`
