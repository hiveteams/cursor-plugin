# `bulkUpdateActionCustomFields`

- Type: `mutation`
- Returns: `[Action!]!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Updates a custom field value for multiple actions at once.  This mutation allows you to set or clear the value of a custom field across multiple actions. You must first call getCustomFields to retrieve available custom fields and their types for the workspace.  **Important**: Use only ONE value parameter based on the custom field type:  \| Custom Field Type \| Parameter to Use \| Value Format \| \|-------------------\|------------------\|--------------\| \| text              \| value            \| Any string value \| \| number            \| numberValue      \| Any numeric value (float) \| \| date              \| dateValue        \| ISO 8601 date string (e.g., "2024-01-15T00:00:00.000Z") \| \| select            \| selectedValues   \| Array of dropdown option strings (e.g., ["Option 1", "Option 2"]) \| \| user              \| selectedValues   \| Array of user IDs (e.g., ["userId123", "userId456"]) \| \| project           \| selectedValues   \| Array of project IDs (e.g., ["projectId123"]) \|  **To clear a custom field value**: Pass null or an empty value for the corresponding parameter.  Access: Requires user access to all specified actions  Returns: Array of updated Action objects with the new custom field values  Errors:   - Throws error if user doesn't have access to any of the actions   - Throws error if custom field doesn't exist   - Throws error if value type doesn't match the custom field type

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionIds` | `[ID!]!` | - | Array of action IDs to update the custom field for |
| `workspaceId` | `ID!` | - | The workspace ID that contains the actions |
| `fieldId` | `ID!` | - | The ID of the custom field to update (get this from getCustomFields query) |
| `value` | `String` | - | Text value - use ONLY for 'text' type custom fields |
| `selectedValues` | `[String]` | - | Array of selected values - use for 'select', 'user', or 'project' type custom fields. For 'select' type: pass the dropdown option strings. For 'user' type: pass an array of user IDs. For 'project' type: pass an array of project IDs. |
| `dateValue` | `Date` | - | Date value - use ONLY for 'date' type custom fields. Pass ISO 8601 format. |
| `numberValue` | `Float` | - | Numeric value - use ONLY for 'number' type custom fields |

## Signature

- `bulkUpdateActionCustomFields(actionIds: [ID!]!, workspaceId: ID!, fieldId: ID!, value: String, selectedValues: [String], dateValue: Date, numberValue: Float)` -> `[Action!]!`
