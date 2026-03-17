---
title: Message Object Schema
object: message
api: rest-v1
aliases: [messages, message object, chat message]
---

# Message Object Schema

Below is the data structure of the Message object in Hive:

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
        containerId
      </td>

      <td style={{ textAlign: "left" }}>
        String/Group ID
      </td>

      <td style={{ textAlign: "left" }}>
        ID of the chat Group that the Message belongs to
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        body
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Body of the Message
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        sender
      </td>

      <td style={{ textAlign: "left" }}>
        String/User ID
      </td>

      <td style={{ textAlign: "left" }}>
        ID of the User who sent the Message
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        senderFirstname
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Optional name of the sender, can be used to override the display name of the sender for a given Message
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        senderPicture
      </td>

      <td style={{ textAlign: "left" }}>
        String/URL
      </td>

      <td style={{ textAlign: "left" }}>
        Optional URL, can be used to override the display image over the sender for a given Message
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
        ID of the Workspace that the Message belongs to
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
        Date + time of Message creation
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
        Date + time that the Message was last modified
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
        User ID string of the Message creator
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
        User ID string of the last user to modify fields on the Message
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
        Optional background color for the message. Options are yellow, purple, green, red, gray
      </td>
    </tr>
  </tbody>
</Table>
