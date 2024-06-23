from Models.MessageDAO import MessageDAO

class Messages:
  def sendNewMessage1(self, new_message):
    MessageDAO().sendNewMessage2(new_message)

  def deleteMessage1(self, del_message):
    MessageDAO().deleteMessage2(del_message)

  def getMessageById1(self, message_id):
    message_id1 = MessageDAO().getMessageById2(message_id)
    return message_id1