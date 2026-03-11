# `setTimeTrackingItemToAction`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Add or edit time tracking item for action  Access: Requires user access to the underlying action and related project  Errors: Throws error if user does not have access to action or project.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | Represents the ID of the action to which time is being added |
| `time` | `TimeInput!` | - | Represents amount of time to add to action |
| `date` | `Date!` | - | Represents the date when the time item is being added or edited |
| `description` | `String` | - | Represents an optional description for the time tracking item |
| `categoryId` | `ID` | - | Represents an optional ID of the category to which the time item relates. |
| `id` | `ID` | - | Represents an optional ID for the time item itself.  Provide for edit purpose |
| `userId` | `ID` | - | Represents the ID of the user who is adding the time item |
| `replaceForDate` | `Boolean` | - | Represents the flag to indicate if the time items for the date need to be replaced with the new time item |

## Signature

- `setTimeTrackingItemToAction(actionId: ID!, time: TimeInput!, date: Date!, description: String, categoryId: ID, id: ID, userId: ID, replaceForDate: Boolean)` -> `Action`
