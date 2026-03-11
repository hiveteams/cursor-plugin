# Create activity feed

Create an Activity Feed in the specified workspace for a Project or Action

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
    "/workspaces/{workspaceId}/activity-feeds": {
      "post": {
        "summary": "Create activity feed",
        "description": "Create an Activity Feed in the specified workspace for a Project or Action",
        "operationId": "workspacesworkspaceidactivity_feeds",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "type",
                  "assignedTo",
                  "attachedItemType",
                  "attachedItemId",
                  "body"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "description": "Type determines the icon used ('comment', 'addProject', 'action', 'due', 'assignees', 'subaction', 'ready')"
                  },
                  "bucket": {
                    "type": "string",
                    "description": "Bucket for the ActivityFeed",
                    "default": "activityFeed"
                  },
                  "assignedTo": {
                    "type": "string",
                    "description": "UserId to receive this ActivityFeed"
                  },
                  "attachedItemType": {
                    "type": "string",
                    "description": "'action' or 'project'"
                  },
                  "attachedItemId": {
                    "type": "string",
                    "description": "Id of the related item"
                  },
                  "title": {
                    "type": "string",
                    "description": "Title"
                  },
                  "body": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"id\": \"abcde123456\",\n    \"workspace\": \"abcde123456\",\n    \"bucket\": \"activityFeed\",\n    \"assignedTo\": \"abcde123456\",\n    \"attachedItemType\": \"action\",\n    \"attachedItemId\": \"abcde123456\",\n    \"title\": \"Comment!\",\n    \"body\": \"Comment body\",\n    \"createdAt\": \"1900-01-01T00:00:00.000Z\",\n    \"modifiedAt\": \"1900-01-01T00:00:00.000Z\",\n    \"createdBy\": \"server\",\n    \"modifiedBy\": \"server\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "abcde123456"
                    },
                    "workspace": {
                      "type": "string",
                      "example": "abcde123456"
                    },
                    "bucket": {
                      "type": "string",
                      "example": "activityFeed"
                    },
                    "assignedTo": {
                      "type": "string",
                      "example": "abcde123456"
                    },
                    "attachedItemType": {
                      "type": "string",
                      "example": "action"
                    },
                    "attachedItemId": {
                      "type": "string",
                      "example": "abcde123456"
                    },
                    "title": {
                      "type": "string",
                      "example": "Comment!"
                    },
                    "body": {
                      "type": "string",
                      "example": "Comment body"
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "1900-01-01T00:00:00.000Z"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "1900-01-01T00:00:00.000Z"
                    },
                    "createdBy": {
                      "type": "string",
                      "example": "server"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "server"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar projectId = \"PROJECT_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/activity-feeds\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  type: \"comment\",\n  bucket: \"activityFeed\",\n  assignedTo: userId,\n  attachedItemType: \"project\",\n  attachedItemId: projectId,\n  title: \"Comment title\",\n  body: \"Comment body\"\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
            }
          ],
          "samples-languages": [
            "javascript"
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