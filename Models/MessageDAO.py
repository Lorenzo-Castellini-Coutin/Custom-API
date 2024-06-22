from Functions import db_connect

class MessageDAO:
  def sendNewMessage(self, new_message):
    conn, cursor = db_connect()
    query1 = '''INSERT INTO Message (message_id, sender_user_id, recipient_id, reply_id, subject, body, date, is_deleted)
                VALUES(?,?,?,?,?,?,?,?)'''
    
    cursor.execute(query1, (new_message['message_id'], new_message['sender_user_id'], new_message['date']))
    
    query2 = '''INSERT INTO Recipient (message_id, sender_user_id) VALUES(?,?)'''
    cursor.execute(query2, (new_message['message_id'], new_message['sender_user_id']))
    
    conn.commit()
    conn.close()
    
  def deleteMessage(self, subject, date):  #Ask how will the message be found?
    conn, cursor = db_connect()

  def getMessageById(self, messid):
    conn, cursor = db_connect()
    self.cursor.execute("SELECT * FROM users WHERE m_id=?", (messid,))