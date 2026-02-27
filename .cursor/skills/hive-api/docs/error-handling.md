# Error handling

Errors are returned using standard HTTP error code syntax. Any additional info is included in the body of the return call, JSON-formatted. Error codes not listed here are in the API methods listed below.

Any 400 level errors will return an object with a message key describing the error. An example error response might look like:

```
{ error: 400, message: "User not found" }
```