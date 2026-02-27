# Update user tag

Update a specific tag on a user

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
    "/workspaces/{workspaceId}/users/{userId}/user-tags/{userTagId}": {
      "put": {
        "summary": "Update user tag",
        "description": "Update a specific tag on a user",
        "operationId": "workspacesworkspaceiduser-tagsuserid-1",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "ID of user to update",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "userTagId",
            "in": "path",
            "description": "ID of tag to set on the user",
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
                  "selectedOptions"
                ],
                "properties": {
                  "selectedOptions": {
                    "type": "array",
                    "description": "Selected options for this user tag",
                    "items": {
                      "type": "string"
                    }
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
                    "value": "{\n  \"_id\": \"qFR6a524nFARukmvF\",\n  \"name\": \"Custom Tag 1\",\n  \"options\": [\"Option 1\", \"Option 2\"],\n  \"selectedOptions\": [\"Option 1\"],\n  \"isMulti\": false\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string",
                      "example": "qFR6a524nFARukmvF"
                    },
                    "name": {
                      "type": "string",
                      "example": "Custom Tag 1"
                    },
                    "options": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "Option 1"
                      }
                    },
                    "selectedOptions": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "Option 1"
                      }
                    },
                    "isMulti": {
                      "type": "boolean",
                      "example": false,
                      "default": true
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar userTagId = \"USER_TAG_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint =\n  \"workspaces/\" + workspaceId + \"/users/\" + userId + \"/user-tags/\" + userTagId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  selectedOptions: [\"Option 1\"]\n};\n\n$.ajax({\n  method: \"PUT\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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