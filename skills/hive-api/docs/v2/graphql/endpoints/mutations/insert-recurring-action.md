# `insertRecurringAction`

- Type: `mutation`
- Returns: `RecurringAction`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Create a recurring action. You must call insertActions first to create the action.  Parameters:   - actionId: ID of the action to make recurring (must exist)   - type: Recurrence type (daily, weekly, monthly, annually)   - startDate: Start date in ISO 8601 format   - endDate: End date in ISO 8601 format   - interval: Interval of recurrence (min: 1, max: 12)   - endingType: How recurrence ends (never, after, date)   - endingAfter: Number of occurrences before ending (min: 1, max: 52)   - days: Days of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun)   - showOnDueDate: Show the action on its due date (default: false)  Access: Requires user access to the action.  Errors: Throws error if action not found or user lacks permission.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to make recurring |
| `type` | `String` | - | Recurrence type (daily, weekly, monthly, annually) |
| `dayType` | `String` | - | Day type (calendar day, workday) |
| `startDate` | `Date` | - | Start date of the recurring action |
| `endDate` | `Date` | - | End date of the recurring action |
| `interval` | `Int` | - | Interval of recurrence (min: 1, max: 12) |
| `endingType` | `String` | - | How recurrence ends (never, after, date) |
| `endingAfter` | `Int` | - | Number of occurrences before ending (min: 1, max: 52) |
| `days` | `[String]` | - | Days of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun) |
| `showOnDueDate` | `Boolean` | - | Show the action on its due date |
| `recurringId` | `ID` | - | Existing recurring ID to link to |

## Signature

- `insertRecurringAction(actionId: ID!, type: String, dayType: String, startDate: Date, endDate: Date, interval: Int, endingType: String, endingAfter: Int, days: [String], showOnDueDate: Boolean, recurringId: ID)` -> `RecurringAction`
