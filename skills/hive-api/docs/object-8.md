# Object

Below is the data structure of Teams

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
        Name of the Team
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        members
      </td>

      <td style={{ textAlign: "left" }}>
        \[String]
      </td>

      <td style={{ textAlign: "left" }}>
        Array of User IDs (string) who are members of the Team
      </td>
    </tr>
  </tbody>
</Table>