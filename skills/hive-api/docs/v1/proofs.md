# Proofs (versioned files)

Versioned files, also known as "Proofs" in Hive, represent proof data associated with Actions in Hive

Below is the data structure of Versioned Files:

| Field               | Type             | Description                                                                                                   |
| :------------------ | :--------------- | :------------------------------------------------------------------------------------------------------------ |
| \_id                | String           | Unique alphanumeric string                                                                                    |
| workspace           | String           | Workspace ID                                                                                                  |
| name                | String           | Name of the proof, typically matches most recent proofing file name                                           |
| accessType          | String           | Access type "PUBLIC" or "RESTRICTED". Default is restricted, but public proofs can be set from Hive UI        |
| fileVersions        | Array of objects | See "File Versions" data structure below. Represents all non-deleted file versions associated with the proof. |
| removedFileVersions | Array of objects | See "File Versions" data structure below. Represents deleted file versions associated with the proof.         |
| deleted             | Boolean          | True/False if proof is deleted.                                                                               |
| createdAt           | ISO Date String  | Date/time of versioned file creation.                                                                         |
| modifiedAt          | ISO Date String  | Date/time of versioned file last modified.                                                                    |

<br />

Below is the data structure of File Versions used in the "versionedFiles.fileVersions" array:

| Field        | Type            | Description                                                                                                                                                                                                               |
| :----------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| fileId       | String          | File ID of the originally uploaded proofing file                                                                                                                                                                          |
| name         | String          | Name of the file. Uses originally uploaded file name and extension by default, unless renamed by end user                                                                                                                 |
| version      | Number          | Major version number that the file represents in the proof (e.g. 0, 1, 2 and so on for standard versions). Higher numbers = more recent versions. Displays in UI as "version.minorVersion" - for example, "1.0" or "2.1". |
| minorVersion | Number          | Minor version number that the file represents in the proof. Minor versions are the same as "internal versions". If a file uses a minor version, it's not visible to external approvers, only internal approvers.          |
| locked       | Boolean         | True/False for whether the version is locked.                                                                                                                                                                             |
| lockedBy     | String          | User ID of the user who locked the version (if locked).                                                                                                                                                                   |
| createdAt    | ISO Date String | Date/time of file version creation.                                                                                                                                                                                       |

<br />

<br />