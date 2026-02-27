# Custom Fields

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
        label
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Custom Field Label
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        attachedToObject
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Type of object this custom field is in relation to
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        type
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Type of custom field ('text', 'date', 'project', 'formula', 'user', 'select')
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        dropdownValues
      </td>

      <td style={{ textAlign: "left" }}>
        String\[]
      </td>

      <td style={{ textAlign: "left" }}>
        Array of possible values for a select custom field
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        allowMultiSelect
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether or not multi select is enabled for this custom field
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        formula
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Formula definition for formula custom fields
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
        Workspace ID for this custom field
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        deleted
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether this custom field is deleted
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
        Date this custom field was created
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
        Date this custom field was modified
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
        User ID that created this custom field
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
        User ID that last modified this custom field
      </td>
    </tr>
  </tbody>
</Table>