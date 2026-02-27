# Add new file version to proof

Adds a new file version to an existing versioned file (proof) on an action.

Adds a new file version to an existing versioned file by uploading a file from a URL. This creates a new version in the existing versioned file rather than creating an entirely new versioned file.

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
    "/actions/{actionId}/versioned-files/{versionedFileId}/file-versions": {
      "post": {
        "description": "",
        "operationId": "post_actions{actionId}versioned-files{versionedFileId}file-versions",
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
            "description": "The unique identifier of the versioned file (proof) associated with the action"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "fileUrl": {
                    "type": "string",
                    "description": "The URL of the file to upload as a new version. Must be publicly accessible, will follow redirects"
                  }
                },
                "type": "object",
                "required": [
                  "fileUrl"
                ]
              }
            }
          }
        }
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