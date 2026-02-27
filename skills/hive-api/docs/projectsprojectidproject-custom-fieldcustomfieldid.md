# Update project custom field

Updates an existing custom field for a project

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
    "/projects/{projectId}/project-custom-field/{customFieldId}": {
      "put": {
        "summary": "Update project custom field",
        "description": "Updates an existing custom field for a project",
        "operationId": "projectsprojectidproject-custom-fieldcustomfieldid",
        "parameters": [
          {
            "name": "projectId",
            "in": "path",
            "description": "ID of the project to add a custom field to",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "customFieldId",
            "in": "path",
            "description": "ID of the custom field to update",
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
                "properties": {
                  "label": {
                    "type": "string",
                    "description": "Label for the custom field"
                  },
                  "value": {
                    "type": "string",
                    "description": "Value of the custom field. If custom field type is date, you can pass date string as a value. Please pass date with time in ISO 8601 format. We pass date with time in order to avoid next bug When we send API request with date \"2023-06-26\" from Chicago, IL (GMT-5). In DB value will be saved as UTC date \"2023-06-26T00:00:00.000Z\" But when we display it on the client UI we convert UTC date to user local timezone (subtract 5 hours) and get \"2023-06-25T19:00:00-0500\" (previous day) Exists several ways to fix it. 1. Pass date with timezone \"2023-06-26T00:00:00-0500\" 2. Pass data in UTC but with time shifted by negative GTM offset \"2023-06-26T05:00:00Z\" You could shift time more than GTM offset. For example add 12 hours for Chicago instead of 5 \"2023-06-26T12:00:00Z\""
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
                    "value": "{\n  \"project\": {\n    \"id\": \"123ABC567XYZ\",\n    \"name\": \"Mobile app development\",\n    \"description\": \"A project for tracking our shiny new mobile app.\",\n    \"startDate\": \"2020-01-04T18:55:02.126Z\",\n    \"endDate\": \"2020-01-04T18:55:02.126Z\",\n    \"accessOption\": \"public\",\n    \"sharingType\": \"everyone\",\n    \"members\": [],\n    \"template\": false,\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\",\n    \"projectCustomFields\": [\n      {\n        \"label\": \"Budget\",\n        \"value\": \"$5000000\",\n        \"dropdownValues\": [],\n        \"selectedValues\": [],\n        \"type\": \"text\",\n        \"_id\": \"1234abcuJzo4k7E2\",\n        \"hidden\": false\n      }\n    ],\n    \"color\": \"#F2F2F2\",\n    \"parentProject\": null,\n    \"phases\": [],\n    \"resourcePlaceholderIds\": []\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "project": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "123ABC567XYZ"
                        },
                        "name": {
                          "type": "string",
                          "example": "Mobile app development"
                        },
                        "description": {
                          "type": "string",
                          "example": "A project for tracking our shiny new mobile app."
                        },
                        "startDate": {
                          "type": "string",
                          "example": "2020-01-04T18:55:02.126Z"
                        },
                        "endDate": {
                          "type": "string",
                          "example": "2020-01-04T18:55:02.126Z"
                        },
                        "accessOption": {
                          "type": "string",
                          "example": "public"
                        },
                        "sharingType": {
                          "type": "string",
                          "example": "everyone"
                        },
                        "members": {
                          "type": "array"
                        },
                        "template": {
                          "type": "boolean",
                          "example": false,
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
                          "example": "1234abcuJzo4k7F9"
                        },
                        "modifiedBy": {
                          "type": "string",
                          "example": "1234abcuJzo4k7F9"
                        },
                        "projectCustomFields": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "label": {
                                "type": "string",
                                "example": "Budget"
                              },
                              "value": {
                                "type": "string",
                                "example": "$5000000"
                              },
                              "dropdownValues": {
                                "type": "array"
                              },
                              "selectedValues": {
                                "type": "array"
                              },
                              "type": {
                                "type": "string",
                                "example": "text"
                              },
                              "_id": {
                                "type": "string",
                                "example": "1234abcuJzo4k7E2"
                              },
                              "hidden": {
                                "type": "boolean",
                                "example": false,
                                "default": true
                              }
                            }
                          }
                        },
                        "color": {
                          "type": "string",
                          "example": "#F2F2F2"
                        },
                        "parentProject": {},
                        "phases": {
                          "type": "array"
                        },
                        "resourcePlaceholderIds": {
                          "type": "array"
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
                    "value": "// If you are trying to update a custom field label\n// while a different custom field with that label\n// and type already exists - an error will be thrown\n{}"
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
              "code": "var userId = \"USER_ID\";\nvar projectId = \"PROJECT_ID\";\nvar customFieldId = \"CUSTOM_FIELD_ID\"\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"projects/\" + projectId + \"/project-custom-field/\" + customFieldId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  label: \"Budget\",\n  value: \"$5000000\"\n};\n\n$.ajax({\n  method: \"PUT\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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