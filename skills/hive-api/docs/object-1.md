# Object

Below is the data structure of the Action object in Hive:

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
        title
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Title of the action
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        workspace
      </td>

      <td style={{ textAlign: "left" }}>
        String/Workspace ID
      </td>

      <td style={{ textAlign: "left" }}>
        ID of the Workspace that the Action belongs to
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        assignees
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of User ID strings. Array with value 'none' represents unassigned
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        projectId
      </td>

      <td style={{ textAlign: "left" }}>
        String/Project ID
      </td>

      <td style={{ textAlign: "left" }}>
        ID of the Project (if any) that the Action belongs to
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
        User input description of the action
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        customFields
      </td>

      <td style={{ textAlign: "left" }}>
        Array of objects\
        \[\{ label: '', value: '' }]\[\{ label: '', value: '' }]
      </td>

      <td style={{ textAlign: "left" }}>
        Action custom fields
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
        Date + time of Action creation
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
        Date + time that the Action was last modified
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
        User ID string of the Action creator
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
        User ID string of the last user to modify fields on the Action
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        status
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Status of the action
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        scheduledDate
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Start Date as Date ISO String
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        deadline
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Due date as Date ISO String
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        parent
      </td>

      <td style={{ textAlign: "left" }}>
        String/Action ID
      </td>

      <td style={{ textAlign: "left" }}>
        Parent action the Action belongs to (if any)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        root
      </td>

      <td style={{ textAlign: "left" }}>
        String/Action ID
      </td>

      <td style={{ textAlign: "left" }}>
        Highest-level action of a tree of actions
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        hasSubactions
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the Action has subactions
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        estimate
      </td>

      <td style={{ textAlign: "left" }}>
        Int32
      </td>

      <td style={{ textAlign: "left" }}>
        Estimated time
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        loggedTime
      </td>

      <td style={{ textAlign: "left" }}>
        Array of objects\
        \[\{userId:'',time:'',date:''}]\[\{userId:'',time:'',date:''}]
      </td>

      <td style={{ textAlign: "left" }}>
        Time logged to an action card
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        estimates
      </td>

      <td style={{ textAlign: "left" }}>
        Array of objects\
        \[\{userId:'',time:''}]\[\{userId:'',time:''}]
      </td>

      <td style={{ textAlign: "left" }}>
        Estimated time per assignee
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        milestone
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the Action is a milestone or not
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        phaseId
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Id of phase
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        phaseName
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Name of phase
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        archived
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the action is archived or not
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
        Whether the action is deleted or not
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        checkedDate
      </td>

      <td style={{ textAlign: "left" }}>
        ISO Date String
      </td>

      <td style={{ textAlign: "left" }}>
        Date that the action was marked "Completed" or checked
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        completedBy
      </td>

      <td style={{ textAlign: "left" }}>
        String/User ID
      </td>

      <td style={{ textAlign: "left" }}>
        User ID of the user who marked the action "Completed" or checked last. Note that this may be different than the assignee.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        placeholderAssignees
      </td>

      <td style={{ textAlign: "left" }}>
        Array
      </td>

      <td style={{ textAlign: "left" }}>
        Array of Placeholder ID strings. Empty array if no placeholder assignees set on an action. If placeholders assignees are set on an action, will be populated with Placeholder IDs as strings in the array.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        agileStoryPoints
      </td>

      <td style={{ textAlign: "left" }}>
        Number
      </td>

      <td style={{ textAlign: "left" }}>
        Number of story points assigned to action
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        agileSprintId
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Identifier of the agile sprint
      </td>
    </tr>
  </tbody>
</Table>