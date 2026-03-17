---
title: Role Tag Object Schema
object: role-tag
api: rest-v1
aliases: [role tags, role tag object]
---

# Role Tag Object Schema

Below is the data structure of Role Tags

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
        * id
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
        workspace
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Workspace ID
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
        Name for this role
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        createdAt
      </td>

      <td style={{ textAlign: "left" }}>
        Date
      </td>

      <td style={{ textAlign: "left" }}>
        Date created
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        createdBy
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        User ID of the user that created this role
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        modifiedAt
      </td>

      <td style={{ textAlign: "left" }}>
        Date
      </td>

      <td style={{ textAlign: "left" }}>
        Date last modified
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        modifiedBy
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        User ID of the user that last modified this role
      </td>
    </tr>
  </tbody>
</Table>
