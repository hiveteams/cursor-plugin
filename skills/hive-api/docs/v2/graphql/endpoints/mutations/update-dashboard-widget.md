# `updateDashboardWidget`

- Type: `mutation`
- Returns: `DashboardWidget`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Updates an existing dashboard widget's configuration. Common update scenarios: 1. Changing visualization type 2. Updating filters or data source 3. Modifying appearance settings 4. Adjusting metrics or calculations

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID!` | - | - |
| `title` | `String` | - | - |
| `titleColor` | `String` | - | - |
| `titleSize` | `TextSize` | - | - |
| `url` | `String` | - | - |
| `sort` | `String` | - | - |
| `type` | `DashboardWidgetType` | - | - |
| `chartType` | `ChartType` | - | - |
| `slateJson` | `JSONObject` | - | - |
| `XAxis` | `DashboardWidgetXAxis` | - | - |
| `XAxisCustomFieldId` | `String` | - | - |
| `XAxisTitle` | `String` | - | - |
| `YAxis` | `DashboardWidgetYAxis` | - | - |
| `YAxisCustomFieldId` | `String` | - | - |
| `YAxisTitle` | `String` | - | - |
| `YAxisGroupBy` | `DashboardWidgetYAxis` | - | - |
| `groupByCustomFieldId` | `String` | - | - |
| `fileIds` | `[ID!]` | - | - |
| `noteId` | `String` | - | - |
| `portfolioViewId` | `String` | - | - |
| `hideHeader` | `Boolean` | - | - |
| `goalId` | `String` | - | - |
| `showTitles` | `Boolean` | - | - |
| `showLegend` | `Boolean` | - | - |
| `ignoreContainerFilter` | `Boolean` | - | - |
| `legendPosition` | `LegendPosition` | - | - |
| `showValueLabels` | `Boolean` | - | - |
| `showRowTotals` | `Boolean` | - | - |
| `showColumnTotals` | `Boolean` | - | - |
| `showFlattenedData` | `Boolean` | - | - |
| `showLinkedToProject` | `Boolean` | - | - |
| `truncateLongNumbers` | `Boolean` | - | - |
| `displayGroupsAs` | `DisplayGroupsAs` | - | - |
| `displayGoalsBy` | `DisplayGoalsBy` | - | - |
| `timeUnitsType` | `TimeUnit` | - | - |
| `projectTreeLevelsToShow` | `[Int!]` | - | - |
| `isProjectTreeLevelActive` | `Boolean` | - | - |
| `reportOn` | `DashboardWidgetReportOn` | - | - |
| `chartValueColors` | `[ChartValueColorInput!]` | - | - |
| `groupOthers` | `DashboardWidgetGroupOthersInput` | - | - |
| `projectId` | `String` | - | - |
| `buttonLabel` | `String` | - | - |
| `sectionHeaderText` | `String` | - | - |
| `sectionHeaderTextAlignment` | `TextAlignment` | - | - |
| `sectionHeaderLinePosition` | `SectionHeaderLinePosition` | - | - |
| `isHidden` | `Boolean` | - | - |
| `projectDetailsFields` | `[String!]` | - | - |
| `contentTextAlignment` | `TextAlignment` | - | - |
| `contentTextSize` | `TextSize` | - | - |
| `contentTextColorPrimary` | `String` | - | - |
| `contentTextColorSecondary` | `String` | - | - |
| `workspaceId` | `String` | - | - |
| `containerId` | `ID` | - | - |
| `colorThemeId` | `String` | - | - |
| `segmentColorOverrides` | `[SegmentColorOverrideInput!]` | - | - |
| `projectBudgetCategoryIds` | `[String]` | - | - |
| `projectBudgetDateRange` | `[Date!]` | - | - |
| `chartValuesState` | `[ChartValueStateInput!]` | - | - |

## Signature

- `updateDashboardWidget(_id: ID!, title: String, titleColor: String, titleSize: TextSize, url: String, sort: String, type: DashboardWidgetType, chartType: ChartType, slateJson: JSONObject, XAxis: DashboardWidgetXAxis, XAxisCustomFieldId: String, XAxisTitle: String, YAxis: DashboardWidgetYAxis, YAxisCustomFieldId: String, YAxisTitle: String, YAxisGroupBy: DashboardWidgetYAxis, groupByCustomFieldId: String, fileIds: [ID!], noteId: String, portfolioViewId: String, hideHeader: Boolean, goalId: String, showTitles: Boolean, showLegend: Boolean, ignoreContainerFilter: Boolean, legendPosition: LegendPosition, showValueLabels: Boolean, showRowTotals: Boolean, showColumnTotals: Boolean, showFlattenedData: Boolean, showLinkedToProject: Boolean, truncateLongNumbers: Boolean, displayGroupsAs: DisplayGroupsAs, displayGoalsBy: DisplayGoalsBy, timeUnitsType: TimeUnit, projectTreeLevelsToShow: [Int!], isProjectTreeLevelActive: Boolean, reportOn: DashboardWidgetReportOn, chartValueColors: [ChartValueColorInput!], groupOthers: DashboardWidgetGroupOthersInput, projectId: String, buttonLabel: String, sectionHeaderText: String, sectionHeaderTextAlignment: TextAlignment, sectionHeaderLinePosition: SectionHeaderLinePosition, isHidden: Boolean, projectDetailsFields: [String!], contentTextAlignment: TextAlignment, contentTextSize: TextSize, contentTextColorPrimary: String, contentTextColorSecondary: String, workspaceId: String, containerId: ID, colorThemeId: String, segmentColorOverrides: [SegmentColorOverrideInput!], projectBudgetCategoryIds: [String], projectBudgetDateRange: [Date!], chartValuesState: [ChartValueStateInput!])` -> `DashboardWidget`
