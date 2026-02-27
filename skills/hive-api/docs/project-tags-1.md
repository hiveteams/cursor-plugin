# Get project tags

Get all project tags for a workspace and projectId

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
    "/workspaces/{workspaceId}/projects/{projectId}/project-tags": {
      "get": {
        "summary": "Get project tags",
        "description": "Get all project tags for a workspace and projectId",
        "operationId": "project-tags-1",
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
            "name": "projectId",
            "in": "path",
            "description": "Project ID to get tags for",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"_id\": \"qFR6a524nFARukmvF\",\n    \"projectId\": \"123123123\",\n    \"name\": \"Custom Tag 1\",\n    \"options\": [\"Option 1\", \"Option 2\"],\n    \"selectedOptions\": [\"Option 1\"],\n    \"isMulti\": false\n  },\n  {\n    \"_id\": \"lkdjfwjdoi2342w3\",\n    \"projectId\": \"123123123\",\n    \"name\": \"Custom Tag 2\",\n    \"options\": [\"Option 1\", \"Option 2\"],\n    \"selectedOptions\": [\"Option 2\"],\n    \"isMulti\": false\n  }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "_id": {
                        "type": "string",
                        "example": "qFR6a524nFARukmvF"
                      },
                      "projectId": {
                        "type": "string",
                        "example": "123123123"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar projectId = \"PROJECT_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint =\n  \"workspaces/\" + workspaceId + \"/projects/\" + projectId + \"/project-tags\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});\n"
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