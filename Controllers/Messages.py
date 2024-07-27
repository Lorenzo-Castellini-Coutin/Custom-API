from Models.MessageDAO import MessageDAO
from flask import Flask, jsonify, request
from Authentication_Validation import *

class Messages:
  def sendNewMessage1(self, message):
    if check_data_messages(message):
      new_message = MessageDAO().sendNewMessage2(message)

      if new_message:
        return jsonify('Message sent successfully.'), 200
      
      else:
        return jsonify('Something went wrong with sending the message.'), 500

    else:
      return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400
    

  def updateMessage1(self, new_message):
    if type(new_message['message_id']) == int and check_data_messages(new_message):
      message_update = MessageDAO().updateMessage2(new_message)

      if message_update:
        return jsonify('Message was successfully updated.'), 200
        
      else:
        return jsonify('The message might not exist/already been deleted, or something went wrong updating the message.'), 500
        
    else:
      return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400

  
  def deleteMessage1(self, message_id):
    delete_message = MessageDAO().deleteMessage2(message_id)
    if delete_message:  
      return jsonify('Message deleted successfully.'), 200
    else:
      return jsonify('Message was either already deleted or could not be deleted.'), 400
    

  def getMessageById1(self, message_id):
    message_id1 = MessageDAO().getMessageById2(message_id)
    if message_id1 is None:
      return jsonify('Message was either not found or already deleted.'), 400
    else:
      return jsonify(message_id1), 200
