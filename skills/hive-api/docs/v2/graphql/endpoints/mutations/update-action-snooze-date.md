# `updateActionSnoozeDate`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update the snooze date for an action.  Snoozing an action temporarily hides it from the user's task list until the specified date. Pass null for snoozeDate to unsnooze (clear the snooze).  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to snooze   - snoozeDate: The date to snooze until (pass null to unsnooze)  Returns: The updated Action object with the new snoozeDate

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `snoozeDate` | `Date` | - | - |

## Signature

- `updateActionSnoozeDate(actionId: ID!, snoozeDate: Date)` -> `Action`
