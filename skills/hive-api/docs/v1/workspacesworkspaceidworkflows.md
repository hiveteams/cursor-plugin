# Get action templates

Get all action templates for a given workspace that the user has access to

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
    "/workspaces/{workspaceId}/actiontemplates": {
      "get": {
        "summary": "Get action templates",
        "description": "Get all action templates for a given workspace that the user has access to",
        "operationId": "workspacesworkspaceidworkflows",
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
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"id\": \"BrhDWFRzJDPMcitEk\",\n    \"name\": \"Blog Post\",\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\" \n  },\n  {\n    \"id\": \"J7ixnuHFP4kmncLun\",\n    \"name\": \"Product Research\",\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\"   \n  }\n]\n"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "example": "BrhDWFRzJDPMcitEk"
                      },
                      "name": {
                        "type": "string",
                        "example": "Blog Post"
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
                        "example": "1234abcuJzo4k7F9"
                      },
                      "modifiedBy": {
                        "type": "string",
                        "example": "1234abcuJzo4k7F9"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/actiontemplates\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
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