from Models.MessagesDAO import MessageDAO
from Models.AuthenticationDAO import AuthenticationDAO
from flask import jsonify
from User_Data_Validation import *

class Messages:
  def sendNewMessage(self, message):
    error_code = check_data_messages(message)
      
    match error_code:
      case 1:    
        return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400

      case 2:
        return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400

      case 100: 
        sender_user_auth = AuthenticationDAO().authenticateUser(message['sender_user_id'])

        if sender_user_auth:
          new_message = MessageDAO().sendNewMessage(message)

          if new_message:
            return jsonify(f'The message was sent. The message id is: {new_message}'), 200
        
          else:
            return jsonify('Something went wrong.'), 500
        
        else:
          return jsonify('User is not authenticated.'), 401
      

  def updateMessage(self, new_message, message_id):
    error_code = check_data_messages(new_message)

    if message_id.isdigit():

      match error_code:
        case 1:
          return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
        case 2:
          return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400

  
  def deleteMessage(self, message_id):
    if message_id.isdigit():  
      delete_message = MessageDAO().deleteMessage(message_id)
      
      if delete_message:  
        return jsonify('Message deleted successfully.'), 200
      
      else:
        return jsonify('Message was either already deleted or could not be deleted.'), 400
    
    else:
      return jsonify('The message id is of invalid type or not supported.'), 400
    

  def getMessageById(self, message_id):
    if message_id.isdigit():
      message_id1 = MessageDAO().getMessageById(message_id)
      
      if message_id1:
        return jsonify(message_id1), 200
        
      else:
        return jsonify('Message was either not found or already deleted.'), 400
      
    else:
      return jsonify('The message id is of invalid type or not supported.'), 400
    






#Notes:
#The numbers 1, 2, 3 are used for error handling in order to return a particular error message given the type of error.
#The numbers 1 and 2 used in variables mean controller functions and model functions, respectively.
#Error codes 400 mean bad request from client-side, 200 means that the execution was successful, and 500 is a server-side or db-side error.