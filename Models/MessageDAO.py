from Functions import db_connect

class MessageDAO:
  def sendNewMessage2(self, message):
    conn, cursor = db_connect()
    query1 = '''INSERT INTO messages (sender_user_id, recipient_user_id, reply_id, subject, body) 
                VALUES(%s, %s, %s, %s, %s)'''
    
    cursor.execute(query1, (message['sender_user_id'], message['recipient_user_id'], message['reply_id'], message['subject'], message['body']))

    query2 = '''INSERT INTO recipients (sender_user_id, recipient_user_id) 
                VALUES(%s, %s)'''
    
    cursor.execute(query2, (message['sender_user_id'], message['recipient_user_id']))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes <= 0:
      return False
    else: 
      return True
    
  def updateMessage2(self, new_message):
    conn, cursor = db_connect()
    query1 = '''UPDATE messages SET recipient_user_id=%s, subject=%s, body=%s 
                WHERE is_deleted=0 and message_id=%s'''
    
    cursor.execute(query1, (new_message['recipient_user_id'], new_message['subject'], new_message['body'], new_message['message_id']))

    query2 = '''UPDATE recipients SET recipient_user_id=%s 
                WHERE is_deleted=0 and message_id=%s'''
    
    cursor.execute(query2, (new_message['recipient_user_id'], new_message['message_id']))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes <= 0:
      return False
    else:
      return True  

  def deleteMessage2(self, del_message):  
    conn, cursor = db_connect()
    query1 = '''UPDATE messages SET is_deleted=1 
                WHERE message_id=%s'''
    
    cursor.execute(query1, (del_message,))
    
    query2 = '''UPDATE recipient SET is_deleted=1 
                WHERE message_id=%s'''
    
    cursor.execute(query2, (del_message,))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes <= 0:
      return False
    else:
      return True

  def getMessageById2(self, message_id):
    conn, cursor = db_connect()
    query1 = '''SELECT sender_user_id, recipient_user_id, subject, body, date FROM messages 
                WHERE is_deleted=0 and message_id=%s'''

    cursor.execute(query1, (message_id,))
    message_id2 = cursor.fetchone()
    
    query2 = '''UPDATE recipient SET is_read=1 
                WHERE is_deleted=0 and message_id=%s'''

    cursor.execute(query2, (message_id,))
    conn.commit()
    conn.close()
    return message_id2
    
  