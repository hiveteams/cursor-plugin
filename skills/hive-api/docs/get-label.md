# Get label

Get all role tags for a workspace

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
    "/workspaces/{workspaceId}/labels/{labelId}": {
      "get": {
        "summary": "Get label",
        "description": "Get all role tags for a workspace",
        "operationId": "get-label",
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
            "name": "labelId",
            "in": "path",
            "description": "The ID of the Label you want to retrieve",
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
                    "value": "{\n  \"_id\": \"qFR6a524nFARukmvF\",\n  \"workspace\": \"12345aZjDQZndHqs\",\n  \"name\": \"Label 1\",\n  \"color\":\"#00CCCC\",\n  \"parent\":null,\n  \"createdBy\": \"12345gfuJzo4k7F9\",\n  \"modifiedBy\": \"12345xgfuJzo4k7F9\",\n  \"createdAt\": \"2018-01-23T22:14:24.862Z\",\n  \"modifiedAt\": \"2018-01-23T22:14:24.862Z\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string",
                      "example": "qFR6a524nFARukmvF"
                    },
                    "workspace": {
                      "type": "string",
                      "example": "12345aZjDQZndHqs"
                    },
                    "name": {
                      "type": "string",
                      "example": "Label 1"
                    },
                    "color": {
                      "type": "string",
                      "example": "#00CCCC"
                    },
                    "parent": {},
                    "createdBy": {
                      "type": "string",
                      "example": "12345gfuJzo4k7F9"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "12345xgfuJzo4k7F9"
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "2018-01-23T22:14:24.862Z"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2018-01-23T22:14:24.862Z"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar labelId = \"LABEL_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/labels/\" + labelId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});\n"
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