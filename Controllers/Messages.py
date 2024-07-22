from Models.MessageDAO import MessageDAO
from flask import Flask, jsonify, request

class Messages:
  def sendNewMessage1(self, message):
    new_message = MessageDAO().sendNewMessage2(message)
    if new_message:  
      return jsonify('Message sent succesfully.'), 200
    else:
      return jsonify('Message could not be sent.'), 500

  def updateMessage1(self, new_message):
    update_message = MessageDAO().updateMessage2(new_message)
    if update_message:
      return jsonify('Message updated successfully.'), 200
    else:
      return jsonify('Message was either already deleted or could not be updated.'), 500
  
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
