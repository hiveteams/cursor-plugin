# Messages

Messages are sent from given Users (denoted by Message.sender) to a given chat Group (denoted by Message.containerId). All new Messages created from the API are done on behalf of the user whose API key + User ID is used in your POST.

If you'd like the Message to appear with a custom sender display name/custom sender image, use the "Message.senderFirstname" and "Message.senderPicture" to override the User's default for a given message.