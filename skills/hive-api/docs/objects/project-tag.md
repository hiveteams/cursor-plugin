---
title: Project Tag Object Schema
object: project-tag
api: rest-v1
aliases: [project tags, project tag object]
---

# Project Tag Object Schema

Below is the data structure of Project Tags

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
        projectId
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Project Id this tag belongs to
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
        Name
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        options
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of String options
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        selectedOptions
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of String options that are currently selected
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        isMulti
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean for whether or not this tag allows multi select
      </td>
    </tr>
  </tbody>
</Table>
