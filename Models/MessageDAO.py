from Functions import db_connect

class MessageDAO:
  def sendNewMessage2(self, message):
    try:
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated FROM authentication_data
                      WHERE user_id=%s, user_id=%s'''
      
      cursor.execute(auth_query, (message['sender_user_id'], message['recipient_user_id']))
      
      auth_users = cursor.fetchone()
      
      if auth_users:
        messages_query = '''INSERT INTO messages (sender_user_id, recipient_user_id, reply_id, subject, body) 
                            VALUES(%s, %s, %s, %s, %s)'''
    
        cursor.execute(messages_query, (message['sender_user_id'], message['recipient_user_id'], message['reply_id'], message['subject'], message['body']))

        recipients_query = '''INSERT INTO recipients (sender_user_id, recipient_user_id) 
                              VALUES(%s, %s)'''
    
        cursor.execute(recipients_query, (message['sender_user_id'], message['recipient_user_id']))
        conn.commit()
        conn.close()
        return True

      else:
        return False

    except:
      return False

    
  def updateMessage2(self, new_message):
    try:
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, (new_message['sender_user_id']))

      auth_user = cursor.fetchone()

      if auth_user:

        messages_query = '''UPDATE messages SET recipient_user_id=%s, subject=%s, body=%s 
                            WHERE is_deleted=0 and message_id=%s'''
    
        cursor.execute(messages_query, (new_message['recipient_user_id'], new_message['subject'], new_message['body'], new_message['message_id']))

        recipients_query = '''UPDATE recipients SET recipient_user_id=%s 
                              WHERE is_deleted=0 and message_id=%s'''
    
        cursor.execute(recipients_query, (new_message['recipient_user_id'], new_message['message_id']))
        conn.commit()
        conn.close()
        return True

      else:
        return False

    except:
      return False


  def deleteMessage2(self, del_message):  
    try:
      conn, cursor = db_connect()
      messages_query = '''UPDATE messages SET is_deleted=1 
                          WHERE message_id=%s'''
    
      cursor.execute(messages_query, (del_message,))
    
      recipients_query = '''UPDATE recipient SET is_deleted=1 
                          WHERE message_id=%s'''
    
      cursor.execute(recipients_query, (del_message,))
      conn.commit()
      conn.close()
      return True
    
    except:
      return False


  def getMessageById2(self, message_id):
    try:
      conn, cursor = db_connect()
    
      messages_query = '''SELECT sender_user_id, recipient_user_id, subject, body, date FROM messages 
                          WHERE is_deleted=0 and message_id=%s'''

      cursor.execute(messages_query, (message_id,))
      message_id2 = cursor.fetchone()
    
      recipients_query = '''UPDATE recipient SET is_read=1 
                            WHERE is_deleted=0 and message_id=%s'''

      cursor.execute(recipients_query, (message_id,))
      conn.commit()
      conn.close()
      return message_id2
    
    except:
      return False
    
  