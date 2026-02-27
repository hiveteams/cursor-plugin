# Get project statuses

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
    "/workspaces/{workspaceId}/project-statuses": {
      "get": {
        "summary": "Get project statuses",
        "description": "",
        "operationId": "get-project-statuses",
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
            "name": "first",
            "in": "query",
            "description": "Get first n items",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 200
            }
          },
          {
            "name": "last",
            "in": "query",
            "description": "Get last n items",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 200
            }
          },
          {
            "name": "before",
            "in": "query",
            "description": "document ID to query documents before it",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "after",
            "in": "query",
            "description": "document ID to query documents after it",
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
                    "value": "{\n    \"edges\": [\n        {\n            \"cursor\": \"Cursor Id\",\n            \"node\": {\n                \"_id\": \"Status Id\",\n                \"name\": \"Status name\",\n                \"color\": \"#000000\",\n                \"workspace\": \"WORKSPACE_ID\",\n                \"deleted\": false,\n                \"modifiedAt\": \"2022-02-03T07:49:26.732Z\",\n                \"modifiedBy\": \"Some user Id\",\n                \"createdAt\": \"2022-02-03T07:49:26.732Z\",\n                \"createdBy\": \"Some user Id\"\n            }\n        }\n    ],\n    \"pageInfo\": {\n        \"startCursor\": \"Start cursor Id\",\n        \"endCursor\": \"End cursor Id\",\n        \"totalCount\": 1,\n        \"hasNextPage\": false,\n        \"hasPreviousPage\": false\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "edges": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "cursor": {
                            "type": "string",
                            "example": "Cursor Id"
                          },
                          "node": {
                            "type": "object",
                            "properties": {
                              "_id": {
                                "type": "string",
                                "example": "Status Id"
                              },
                              "name": {
                                "type": "string",
                                "example": "Status name"
                              },
                              "color": {
                                "type": "string",
                                "example": "#000000"
                              },
                              "workspace": {
                                "type": "string",
                                "example": "WORKSPACE_ID"
                              },
                              "deleted": {
                                "type": "boolean",
                                "example": false,
                                "default": true
                              },
                              "modifiedAt": {
                                "type": "string",
                                "example": "2022-02-03T07:49:26.732Z"
                              },
                              "modifiedBy": {
                                "type": "string",
                                "example": "Some user Id"
                              },
                              "createdAt": {
                                "type": "string",
                                "example": "2022-02-03T07:49:26.732Z"
                              },
                              "createdBy": {
                                "type": "string",
                                "example": "Some user Id"
                              }
                            }
                          }
                        }
                      }
                    },
                    "pageInfo": {
                      "type": "object",
                      "properties": {
                        "startCursor": {
                          "type": "string",
                          "example": "Start cursor Id"
                        },
                        "endCursor": {
                          "type": "string",
                          "example": "End cursor Id"
                        },
                        "totalCount": {
                          "type": "integer",
                          "example": 1,
                          "default": 0
                        },
                        "hasNextPage": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "hasPreviousPage": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        }
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar first = 1;\nvar endpoint = \"workspaces/\" + workspaceId + \"/project-statuses\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey + \"&sortBy=title+asc\" + \"&first=\" + first;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
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