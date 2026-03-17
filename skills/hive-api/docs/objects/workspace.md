---
title: Workspace Object Schema
object: workspace
api: rest-v1
aliases: [workspaces, workspace object, workspace schema]
---

## Workspace Object Schema

Below is the data structure of the Workspace object in Hive:

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
        Name of the workspace
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
        Members of the workspace as an array of User ID Strings
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
        Date + time of Workspace creation
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
        Date + time that the Workspace was last modified
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
        User ID string of the Workspace creator
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
        User ID string of the last user to modify fields on the Workspace
      </td>
    </tr>
  </tbody>
</Table>
