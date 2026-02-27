# Get projects

Get all projects for a given workspace that the user has access to

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
    "/workspaces/{workspaceId}/projects": {
      "get": {
        "summary": "Get projects",
        "description": "Get all projects for a given workspace that the user has access to",
        "operationId": "workspacesworkspaceidprojects",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "sortBy",
            "in": "query",
            "description": "Sort results by an Action Object field (for example, `sortBy=title+asc`)",
            "schema": {
              "type": "string",
              "default": "fieldName+asc"
            }
          },
          {
            "name": "filters",
            "in": "query",
            "description": "Optional fields to filter by. Filters expect a structure like \"filters[fieldName]=value\". For example, if you want to filter to just get deleted projects, you would pass: \"filters[deleted]=true\". Currently, only two fields are supported:  \"archived\", \"deleted\".",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"id\": \"9MRZ6oYzRMJ4eJYnR\",\n    \"name\": \"Spring Bee Hive Rebuild\",\n    \"description\": \"\",\n    \"startDate\": null,\n    \"endDate\": null,\n    \"accessOption\": \"private\",\n    \"sharingType\": \"me\",\n    \"members\": [],\n    \"template\": true,\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"\",\n    \"modifiedBy\": \"\",\n    \"projectCustomFields\": [],\n    \"color\": \"#3390dc\",\n    \"parentProject\": null,\n    \"phases\": [],\n    \"budget\": 100000,\n    \"resourcePlaceholderIds\": []\n  },\n  {\n    \"id\": \"9S8pMXXJwCeExYWzq\",\n    \"name\": \"Sell More Honey Campaign\",\n    \"description\": \"\",\n    \"startDate\": null,\n    \"endDate\": null,\n    \"accessOption\": \"private\",\n    \"sharingType\": \"me\",\n    \"members\": [],\n    \"template\": true,\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"\",\n    \"modifiedBy\": \"\",\n    \"projectCustomFields\": [],\n    \"color\": \"#3390dc\",\n    \"parentProject\": null,\n    \"phases\": [],\n    \"budget\": 0,\n    \"resourcePlaceholderIds\": []\n  }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "example": "9MRZ6oYzRMJ4eJYnR"
                      },
                      "name": {
                        "type": "string",
                        "example": "Spring Bee Hive Rebuild"
                      },
                      "description": {
                        "type": "string",
                        "example": ""
                      },
                      "startDate": {},
                      "endDate": {},
                      "accessOption": {
                        "type": "string",
                        "example": "private"
                      },
                      "sharingType": {
                        "type": "string",
                        "example": "me"
                      },
                      "members": {
                        "type": "array"
                      },
                      "template": {
                        "type": "boolean",
                        "example": true,
                        "default": true
                      },
                      "createdAt": {
                        "type": "string",
                        "example": "2017-05-18T15:26:17.407Z"
                      },
                      "modifiedAt": {
                        "type": "string",
                        "example": "2017-05-19T02:25:06.190Z"
                      },
                      "createdBy": {
                        "type": "string",
                        "example": ""
                      },
                      "modifiedBy": {
                        "type": "string",
                        "example": ""
                      },
                      "projectCustomFields": {
                        "type": "array"
                      },
                      "color": {
                        "type": "string",
                        "example": "#3390dc"
                      },
                      "parentProject": {},
                      "phases": {
                        "type": "array"
                      },
                      "budget": {
                        "type": "integer",
                        "example": 100000,
                        "default": 0
                      },
                      "resourcePlaceholderIds": {
                        "type": "array"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/projects\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
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