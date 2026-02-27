# Get specific proofing file

Retrieves a specific file version, including a fileUrl for download, from a versioned file associated with an action.

Retrieves a specific file version from a versioned file associated with an action. This endpoint validates that the versioned file belongs to the action and returns the file version details with an updated file URL.

By default, the file URL will be the original proofing file uploaded.

Optionally supports getting a file URL which includes the file with annotations made from Proofing in Hive (downloadType="withAnnotations").

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "hive-rest-api",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://app.hive.com/api/v1"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "api_key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/actions/{actionId}/versioned-files/{versionedFileId}/file-versions/{fileId}": {
      "get": {
        "description": "",
        "operationId": "get_actions{actionId}versioned-files{versionedFileId}file-versions{fileId}",
        "responses": {
          "200": {
            "description": ""
          }
        },
        "parameters": [
          {
            "in": "path",
            "name": "actionId",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "The unique identifier of the action"
          },
          {
            "in": "path",
            "name": "versionedFileId",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "The unique identifier of the versioned file"
          },
          {
            "in": "path",
            "name": "fileId",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "The unique identifier of the specific file ID (the \"fileId\" from an action's versionedFiles.fileVersions array)"
          },
          {
            "in": "query",
            "name": "downloadType",
            "schema": {
              "type": "string",
              "enum": [
                "withAnnotations"
              ]
            },
            "description": "Set to \"withAnnotations\" to export the file with annotations from Hive proofing included. If not passed, will download the originally uploaded file."
          }
        ]
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```