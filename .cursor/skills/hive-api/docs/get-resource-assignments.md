# Get resource assignments

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
    "/workspaces/{workspaceId}/resource-assignments": {
      "get": {
        "summary": "Get resource assignments",
        "description": "",
        "operationId": "get-resource-assignments",
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
          },
          {
            "name": "filters[resourceId]",
            "in": "query",
            "description": "Filter by resourceId - either a User ID or a Placeholder ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[startDate]",
            "in": "query",
            "description": "Filter by startDate",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "filters[endDate]",
            "in": "query",
            "description": "Filter by endDate",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "filters[notes]",
            "in": "query",
            "description": "Filter by notes text field on a Resource Assignment. Uses text matching.",
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
                    "value": "{\n    \"edges\": [\n        {\n            \"cursor\": \"Cursor Id\",\n            \"node\": {\n                \"id\": \"Some user Id\",\n                \"workspace\": \"WORKSPACE_ID\",\n                \"resourceId\": \"Resource assignment Id\",\n                \"projectId\": \"Project Id\",\n                \"startDate\": \"2022-01-10T00:00:00.000Z\",\n                \"endDate\": \"2022-01-13T00:00:00.000Z\",\n                \"allocationType\": \"fixedHours\",\n                \"assignmentType\": \"regular\",\n                \"hoursPerDay\": 0.8,\n                \"fixedHours\": 2.4,\n                \"fixedDisplayType\": \"percentages\"\n            }\n        }\n    ],\n    \"pageInfo\": {\n        \"startCursor\": \"Start cursor Id\",\n        \"endCursor\": \"End cursor Id\",\n        \"totalCount\": 5,\n        \"hasNextPage\": true,\n        \"hasPreviousPage\": false\n    }\n}"
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
                              "id": {
                                "type": "string",
                                "example": "Some user Id"
                              },
                              "workspace": {
                                "type": "string",
                                "example": "WORKSPACE_ID"
                              },
                              "resourceId": {
                                "type": "string",
                                "example": "Resource assignment Id"
                              },
                              "projectId": {
                                "type": "string",
                                "example": "Project Id"
                              },
                              "startDate": {
                                "type": "string",
                                "example": "2022-01-10T00:00:00.000Z"
                              },
                              "endDate": {
                                "type": "string",
                                "example": "2022-01-13T00:00:00.000Z"
                              },
                              "allocationType": {
                                "type": "string",
                                "example": "fixedHours"
                              },
                              "assignmentType": {
                                "type": "string",
                                "example": "regular"
                              },
                              "hoursPerDay": {
                                "type": "number",
                                "example": 0.8,
                                "default": 0
                              },
                              "fixedHours": {
                                "type": "number",
                                "example": 2.4,
                                "default": 0
                              },
                              "fixedDisplayType": {
                                "type": "string",
                                "example": "percentages"
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
                          "example": 5,
                          "default": 0
                        },
                        "hasNextPage": {
                          "type": "boolean",
                          "example": true,
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
              "language": "text",
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar first = 1;\nvar endpoint = \"workspaces/\" + workspaceId + \"/resource-assignments\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey + \"&sortBy=title+asc\" + \"&first=\" + first;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});"
            }
          ],
          "samples-languages": [
            "text"
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