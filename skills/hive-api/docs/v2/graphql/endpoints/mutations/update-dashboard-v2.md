# `updateDashboardV2`

- Type: `mutation`
- Returns: `Dashboard`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Updates an existing dashboard with typed V2 filter input for Buzz/MCP endpoints. This mutation provides full schema introspection for AI assistants.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | Dashboard ID to update |
| `title` | `String` | - | New dashboard title |
| `privacy` | `DashboardPrivacy` | - | New privacy setting |
| `projectIds` | `[ID]` | - | Updated project IDs for access |
| `sharingWith` | `[ID!]` | - | Updated user IDs to share with |
| `teams` | `[ID!]` | - | Updated team IDs to share with |
| `layout` | `[InputDashboardLayout!]` | - | Updated widget layout configuration |
| `filter` | `WidgetContainerFilterInputV2` | - | Updated global widget filter |
| `shareOnBehalfOfCreator` | `Boolean` | - | Whether to share on behalf of creator |
| `shareOnBehalfOfCreatorSettings` | `ShareOnBehalfOfCreatorSettingsInput` | - | - |
| `pinToUser` | `Boolean` | - | Whether to pin dashboard to user |
| `color` | `String` | - | Updated dashboard color |
| `allowedEmailDomains` | `[String!]` | - | Updated allowed email domains |
| `allowAccessToWhitelistedDomains` | `Boolean` | - | Whether to allow whitelisted domain access |
| `backgroundColor` | `DashboardBackgroundColor` | - | Updated background color |
| `backgroundImageUrl` | `String` | - | Updated background image URL |
| `backgroundImageCropType` | `DashboardBackgroundImageCropType` | - | Updated background image crop type |
| `displayTipsAndTricksFooter` | `Boolean` | - | Whether to display tips footer |
| `headerTextColor` | `DashboardHeaderTextColor` | - | Updated header text color |
| `type` | `DashboardType` | - | - |

## Signature

- `updateDashboardV2(_id: ID!, title: String, privacy: DashboardPrivacy, projectIds: [ID], sharingWith: [ID!], teams: [ID!], layout: [InputDashboardLayout!], filter: WidgetContainerFilterInputV2, shareOnBehalfOfCreator: Boolean, shareOnBehalfOfCreatorSettings: ShareOnBehalfOfCreatorSettingsInput, pinToUser: Boolean, color: String, allowedEmailDomains: [String!], allowAccessToWhitelistedDomains: Boolean, backgroundColor: DashboardBackgroundColor, backgroundImageUrl: String, backgroundImageCropType: DashboardBackgroundImageCropType, displayTipsAndTricksFooter: Boolean, headerTextColor: DashboardHeaderTextColor, type: DashboardType)` -> `Dashboard`
