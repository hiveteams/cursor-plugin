# Create versioned file for action

Creates a new versioned file (series of proofs) on an action for proofing.

Creates a new versioned file for proofing by uploading a file from a URL and associating it with the specified action.

**Warning:** This creates an entirely new proofing versioned file, and if any proofs already exist on the action, this will replace them all. If you're looking to just add a new file version, see "Add new file version to proof"

<br />

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
      "post": {
        "description": "",
        "operationId": "post_actions{actionId}versioned-files",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "examples": {
                  "New Example": {
                    "summary": "New Example",
                    "value": {
                      "message": "Proofing versioned file successfully added"
                    }
                  }
                }
              }
            }
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "fileUrl": {
                    "type": "string",
                    "description": "The URL of the file to upload. Must be publicly accessible, can follow redirects."
                  },
                  "filename": {
                    "type": "string",
                    "description": "The name for the uploaded file. Will use file's default name from the URL if nothing provided here."
                  }
                },
                "type": "object",
                "required": [
                  "fileUrl"
                ]
              }
            }
          }
        },
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