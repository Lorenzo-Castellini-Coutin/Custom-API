from Functions import db_connect

class MessageDAO:
  def sendNewMessage2(self, new_message):
    conn, cursor = db_connect()
    query1 = '''INSERT INTO messages (message_id, sender_user_id, recipient_user_id, reply_id, subject, body, date)
                VALUES(?,?,?,?,?,?,?)'''
    
    cursor.execute(query1, (new_message['message_id'], new_message['sender_user_id'], new_message['recipient_user_id'], new_message['reply_id'], new_message['subject'], new_message['body'], new_message['date']))
    
    query2 = '''INSERT INTO recipient (message_id, sender_user_id, recipient_user_id) VALUES(?,?,?)'''
    cursor.execute(query2, (new_message['message_id'], new_message['sender_user_id'], new_message['recipient_user_id']))
    conn.commit()
    conn.close()
    
  def deleteMessage2(self, del_message):  
    conn, cursor = db_connect()
    query1 = 'UPDATE messages SET is_deleted=1 WHERE subject=? and date=?'
    cursor.execute(query1, (del_message['subject'], del_message['date']))
    
    query2 = 'UPDATE recipient SET is_deleted=1 WHERE message_id=?'
    cursor.execute(query2, (del_message['message_id'],))
    conn.commit()
    conn.close()


  def getMessageById2(self, message_id):
    conn, cursor = db_connect()
    query = 'SELECT sender_user_id, recipient_user_id, reply_id, subject, body, date FROM messages WHERE is_deleted=0 and message_id=?'
    cursor.execute(query, (message_id,))
    message_id2 = cursor.fetchone()
    conn.commit()
    conn.close()
    return message_id2
  