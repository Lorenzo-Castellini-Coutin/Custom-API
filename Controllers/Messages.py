from Models.MessagesDAO import MessageDAO
from flask import Flask, jsonify, request
from User_Data_Validation import *

class Messages:
  def sendNewMessage(self, message):
    if check_data_messages(message):
      new_message1 = MessageDAO().sendNewMessage2(message)

      if new_message1:
        return jsonify(f'Message sent successfully. The message id is: {new_message1}'), 200
      
      else:
        return jsonify('Something went wrong with sending the message.'), 500

    else:
      return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400
    

  def updateMessage(self, new_message, message_id):
    if message_id.isdigit() and check_data_messages(new_message):
      message_update = MessageDAO().updateMessage2(new_message, message_id)

      if message_update:
        return jsonify('Message was successfully updated.'), 200
        
      else:
        return jsonify('The message might not exist/already been deleted, or something went wrong with updating the message.'), 500
        
    else:
      return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400

  
  def deleteMessage(self, message_id):
    if message_id.isdigit():  
      delete_message = MessageDAO().deleteMessage2(message_id)
      
      if delete_message:  
        return jsonify('Message deleted successfully.'), 200
      
      else:
        return jsonify('Message was either already deleted or could not be deleted.'), 400
    
    else:
      return jsonify('The message id is of invalid type or not supported.'), 400
    

  def getMessageById(self, message_id):
    if message_id.isdigit():
      message_id1 = MessageDAO().getMessageById2(message_id)
      
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