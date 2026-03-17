---
title: Project Object Schema
object: project
api: rest-v1
aliases: [projects, project object, project schema]
---

# Project Object Schema

Below is the data structure of the Project object in Hive:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Field
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        id
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Unique alphanumeric string id
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        name
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Name of the Project
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        description
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Text representing an optional project description
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        endDate
      </td>

      <td style={{ textAlign: "left" }}>
        ISO Date String
      </td>

      <td style={{ textAlign: "left" }}>
        End date of the Project
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        sharingType
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Can be one of three types:

        1. "everyone" - Project is accessible by everyone in the workspace
        2. "custom" - Project is limited to a subset of users in the workspace. If set to "custom", the "members" field shows which users have access
        3. "me" - Project is limited to just the user who has access
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        members
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Members of the project (if sharingType is set to "custom") as an array of User ID Strings
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        projectCustomFields
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of project-level custom fields
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        projectCustomFields.$.\_id
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Unique alphanumeric string id for a projectCustomField entry
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        projectCustomFields.$.type
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Custom field value type. Currently just limited/defaulted to "text"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        projectCustomFields.$.label
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Label for the custom field
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        projectCustomFields.$.value
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Stored value of the custom field
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        createdAt
      </td>

      <td style={{ textAlign: "left" }}>
        ISO Date String
      </td>

      <td style={{ textAlign: "left" }}>
        Date + time of Project creation
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        modifiedAt
      </td>

      <td style={{ textAlign: "left" }}>
        ISO Date String
      </td>

      <td style={{ textAlign: "left" }}>
        Date + time that the Project was last modified
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        createdBy
      </td>

      <td style={{ textAlign: "left" }}>
        String/User ID
      </td>

      <td style={{ textAlign: "left" }}>
        User ID string of the Project creator
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        modifiedBy
      </td>

      <td style={{ textAlign: "left" }}>
        String/User ID
      </td>

      <td style={{ textAlign: "left" }}>
        User ID string of the last user to modify fields on the Project
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        color
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Hex code for project color
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        statusUpdates
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of Project Status updates that exist on the project
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        resourcePlaceholderIds
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of placeholder IDs which represent placeholders added to a given project
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        budget
      </td>

      <td style={{ textAlign: "left" }}>
        Number
      </td>

      <td style={{ textAlign: "left" }}>
        Number value for Project budget
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        isDraftMode
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean value representing whether a project is in Draft Mode state or not.
      </td>
    </tr>
  </tbody>
</Table>
