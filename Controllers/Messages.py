from Models.MessagesDAO import MessageDAO
from Models.AuthenticationDAO import AuthenticationDAO
from flask import jsonify
from Data_Validation import *

class Messages:
  def sendNewMessage(self, message):
    error_code = validate_new_messages(message)
      
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
    error_code = validate_new_messages(new_message)

    if message_id.isdigit():

      match error_code:
        case 1:
          return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
        case 2:
          return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400
        
        case 100:
          sender_user_auth = AuthenticationDAO().authenticateUser(new_message['sender_user_id'])

          if sender_user_auth:
            update_message = MessageDAO().updateMessage(new_message)

            if update_message:
              return jsonify(f'The message with id: {update_message}, has been updated.'), 200
            
            else:
              return jsonify('Something went wrong.'), 500
            
          else:
            return jsonify('User is not authenticated.'), 401
          
    else:
      return jsonify('The message id is of invalid/incorrect type.'), 400
  

  def getInbox(self, recipient_user_id):
    if recipient_user_id.isdigit():
      auth_user = AuthenticationDAO().verifyAuthTokens(recipient_user_id)

      if auth_user:
        inbox = MessageDAO().getInbox(recipient_user_id)

        if inbox:
          return jsonify(inbox), 200
        
        else:
          return jsonify('No messages available for this user.'), 400
        
      else:
        return jsonify('User is not authenticated.'), 401
      
  
  def getSent(self, sender_user_id):
    if sender_user_id.isdigit():
      auth_user = AuthenticationDAO().verifyAuthTokens(sender_user_id)

      if auth_user:
        sent = MessageDAO().getSent(sender_user_id)

        if sent:
          return jsonify(sent), 200
        
        else:
          return jsonify('No messages available for this user.'), 400
        
      else:
        return jsonify('User is not authenticated.'), 401


  def deleteMessage(self, message_id):
    if message_id.isdigit():  
      delete_message = MessageDAO().deleteMessage(message_id)
      
      if delete_message:  
        return jsonify(f'The message with id: {delete_message}, has been deleted.'), 200
      
      else:
        return jsonify('The message might have been deleted/never existed.'), 400
    
    else:
      return jsonify('The message id is of invalid/incorrect type.'), 400
    

  def getMessageById(self, message_id):
    if message_id.isdigit():
      get_message = MessageDAO().getMessageById(message_id)

      if get_message:
        return jsonify(get_message), 200
        
      else:
        return jsonify('Message is not available.'), 400
        
    else:
      return jsonify('The message id is of invalid/incorrect type.'), 400
      
      
      


