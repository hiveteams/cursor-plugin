# Get versioned files for action

Get all versioned files (Proofs via Proofing and Approvals) for an action.

Retrieves versioned files associated with a specific action for proofing purposes. This endpoint returns the versioned file data including all file versions and automatically refreshes expired file URLs.

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
    "/actions/{actionId}/versioned-files": {
      "get": {
        "summary": "Get versioned files",
        "description": "Get all versioned files for Proofing and Approvals.",
        "operationId": "get-versioned-files",
        "parameters": [
          {
            "in": "path",
            "name": "actionId",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "The unique identifier of the action"
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  },
                  "Success": {
                    "summary": "Success",
                    "value": {
                      "versionedFiles": [
                        {
                          "_id": "6jM3unPjawrE3JTgP",
                          "workspace": "36jd3S2RGjbum3kfZ",
                          "name": "Design Mockup",
                          "accessType": "Public",
                          "fileVersions": [
                            {
                              "fileId": "4zogFqWqB2PvmjQZ7",
                              "name": "mockup_v1.png",
                              "version": 1,
                              "minorVersion": 0,
                              "locked": false,
                              "lockedBy": null,
                              "createdAt": "2023-07-20T10:30:00Z"
                            }
                          ],
                          "removedFileVersions": [],
                          "deleted": false,
                          "createdAt": "2023-07-20T10:30:00Z",
                          "modifiedAt": "2023-07-20T10:30:00Z"
                        }
                      ]
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "samples-languages": [
            "shell"
          ]
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