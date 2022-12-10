
# Api Messages - System 

rest API backend system that is responsible for handling
messages between users.


## Functionality

Create user-https://dolev.pythonanywhere.com/rest-auth/registration/

Login user-https://dolev.pythonanywhere.com/rest-auth/login/

Writing a message-https://dolev.pythonanywhere.com/Messages/Message/ 

Get all messages for a specific user-https://dolev.pythonanywhere.com/Messages/Message/ 

Get all unread messages for a specific user-https://dolev.pythonanywhere.com/Messages/Message/UnRead/

Read message (return one message)-https://dolev.pythonanywhere.com/Messages/Message/<name Subject Message>

Delete message (as owner or as receiver)-https://dolev.pythonanywhere.com/Messages/Message/<name Subject Message> [Delete a message with the button -Delete]

## Additions
use authentication method to set up the request for the logged in user. So if you ask for the
get messages API you will only get the messages for the current logged in user.


## Requirements

Use the package manager [Installtion](https://github.com/DolevPeretz/Api-Message/blob/master/requirements.txt) to install foobar.
