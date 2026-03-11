# `updateResourcePlaceholder`

- Type: `mutation`
- Returns: `ResourcePlaceholder!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update an existing resource placeholder's properties.  This allows modification of placeholder details while preserving the placeholder's identity and existing assignments.  IMPORTANT: Only workspace administrators can modify billRate and costRate values. Regular users can only update the name and roleTagId.  Common use cases: • Refining placeholder role names for clarity • Updating role assignments as requirements change • Adjusting billing/cost rates (admin only) • Associating placeholders with different role tags  Parameters: • id: Required. The ID of the resource placeholder to update • name: Optional. New display name for the placeholder • roleTagId: Optional. New role/skill tag association (can be null to remove) • billRate: Optional. New hourly billing rate (admin only) • costRate: Optional. New hourly cost rate (admin only)  Returns: The updated ResourcePlaceholder object

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` | - | - |
| `name` | `String` | - | - |
| `billRate` | `Float` | - | - |
| `costRate` | `Float` | - | - |
| `roleTagId` | `ID` | - | - |

## Signature

- `updateResourcePlaceholder(id: ID!, name: String, billRate: Float, costRate: Float, roleTagId: ID)` -> `ResourcePlaceholder!`
