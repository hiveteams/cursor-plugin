# `updateActionCustomField`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Updates a custom field value for a specific action.  This mutation allows you to set or update the value of a custom field that has been assigned to an action. The mutation supports all custom field types including text, number, date, select (single/multi), user, and project fields.  Access: Requires user access to the action  Returns: The updated Action object with the new custom field value  Errors:   - Throws error if user doesn't have access to the action   - Throws error if custom field doesn't exist   - Throws error if custom field is not enabled for the action's project   - Throws error if value type doesn't match the custom field type

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | The ID of the action to update the custom field for |
| `fieldId` | `ID!` | - | The ID of the custom field to update |
| `value` | `String` | - | Text value for text-type custom fields |
| `selectedValues` | `[String]` | - | Array of selected values for select-type custom fields |
| `dateValue` | `Date` | - | Date value for date-type custom fields |
| `numberValue` | `Float` | - | Numeric value for number-type custom fields |

## Signature

- `updateActionCustomField(actionId: ID!, fieldId: ID!, value: String, selectedValues: [String], dateValue: Date, numberValue: Float)` -> `Action`
