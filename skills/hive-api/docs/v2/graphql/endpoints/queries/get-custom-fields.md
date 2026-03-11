# `getCustomFields`

- Type: `query`
- Returns: `CustomFieldConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Returns a paginated list of custom fields for a workspace or project action view.  Parameters: - workspaceId: Required. The ID of the workspace to get custom fields for. - actionViewId: Optional. The ID of the action view to get custom fields for. Could be used to get custom fields for a specific project action view. - formId: Optional. The ID of the form to get custom fields for. - first: Optional. The number of custom fields to return. - last: Optional. The number of custom fields to return. - before: Optional. The ID of the custom field to return before. - after: Optional. The ID of the custom field to return after. - selector: Optional. A JSON object to filter the custom fields. - includeRemoved: Optional. Whether to include removed custom fields. - searchParams: Optional. A JSON object to search the custom fields. - sortField: Optional. The field to sort the custom fields by. - sortOrder: Optional. The order to sort the custom fields by. - includeProjectCustomFields: Optional. Whether to include project custom fields.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `actionViewId` | `ID` | - | - |
| `formId` | `ID` | - | - |
| `first` | `Int` | 20 | - |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `selector` | `JSONObject` | - | - |
| `itemType` | `CustomFieldItemType` | - | - |
| `includeRemoved` | `Boolean` | - | - |
| `searchParams` | `SearchParams` | - | - |
| `sortField` | `String` | "modifiedAt" | - |
| `sortOrder` | `Int` | -1 | - |
| `includeProjectCustomFields` | `Boolean` | false | - |

## Signature

- `getCustomFields(workspaceId: ID!, actionViewId: ID, formId: ID, first: Int, last: Int, before: ID, after: ID, selector: JSONObject, itemType: CustomFieldItemType, includeRemoved: Boolean, searchParams: SearchParams, sortField: String, sortOrder: Int, includeProjectCustomFields: Boolean)` -> `CustomFieldConnection`
