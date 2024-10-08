from Models.MessagesDAO import MessageDAO
from Models.AuthenticationDAO import AuthenticationDAO
from flask import jsonify
from Data_Validation import *

class Messages:
  def sendNewMessage(self, new_message, args):
    error_code, message = validate_new_messages(new_message)
    
    if error_code != 100:
      return jsonify(message), 400
   
    else:
      sender_user_id = new_message['sender_user_id']
      sender_user_auth = AuthenticationDAO().verifyAuthTokens(sender_user_id, args.get('token'))

      if sender_user_auth:
          new_message = MessageDAO().sendNewMessage(new_message)

          if new_message:
            return jsonify(f'The message was sent. The message id is: {new_message}'), 200
        
          else:
            return jsonify('Something went wrong.'), 500
        
      else:
        return jsonify('User is not authenticated.'), 401
      

  def updateMessage(self, new_message, message_id, args):
    error_code, message = validate_new_messages(new_message)

    if message_id.isdigit():

      if error_code != 100:
        return jsonify(message), 400
      
      else:
        sender_user_auth = AuthenticationDAO().verifyAuthTokens(new_message['sender_user_id'], args.get('token'))

        if sender_user_auth:
          update_message = MessageDAO().updateMessage(new_message, message_id)

          if update_message:
            return jsonify(f'The message with id: {update_message}, has been updated.'), 200
            
          else:
            return jsonify('Something went wrong.'), 500
            
        else:
          return jsonify('User is not authenticated.'), 401
          
    else:
      return jsonify('The message id is of invalid/incorrect type.'), 400
  

  def getInbox(self, recipient_user_id, args):
    if recipient_user_id.isdigit():
      auth_user = AuthenticationDAO().verifyAuthTokens(recipient_user_id, args.get('token'))

      if auth_user:
        inbox = MessageDAO().getInbox(recipient_user_id)

        if inbox:
          return jsonify(inbox,), 200
        
        else:
          return jsonify('No messages available for this user.'), 400
        
      else:
        return jsonify('User is not authenticated.'), 401
      
  
  def getSent(self, sender_user_id, args):
    if sender_user_id.isdigit():
      auth_user = AuthenticationDAO().verifyAuthTokens(sender_user_id, args.get('token'))

      if auth_user:
        sent = MessageDAO().getSent(sender_user_id)

        if sent:
          return jsonify(sent), 200
        
        else:
          return jsonify('No messages available for this user.'), 400
        
      else:
        return jsonify('User is not authenticated.'), 401


  def deleteMessage(self, user_id, message_id, args):
    auth_user = AuthenticationDAO().verifyAuthTokens(user_id['user_id'], args.get('token'))

    if auth_user:
      if message_id.isdigit():  
        delete_message = MessageDAO().deleteMessage(user_id, message_id)
       
        if delete_message:  
          return jsonify(f'The message with id: {message_id}, has been deleted.'), 200
      
        else:
          return jsonify('The message might have been deleted/never existed.'), 400
    
      else:
        return jsonify('The message id is of invalid/incorrect type.'), 400
      
    else:
      return jsonify('User is not authenticated.'), 401
    

  def getMessageById(self, user_id, message_id, args):
    auth_user = AuthenticationDAO().verifyAuthTokens(user_id['user_id'], args.get('token'))  
      
    if auth_user:
      if message_id.isdigit():
        get_message = MessageDAO().getMessageById(user_id, message_id)
      
        if get_message:
          return jsonify(get_message), 200
        
        else:
          return jsonify('Message is not available.'), 400
        
      else:
        return jsonify('The message id is of invalid/incorrect type.'), 400
      
    else:
      return jsonify('User is not authenticated.'), 401


