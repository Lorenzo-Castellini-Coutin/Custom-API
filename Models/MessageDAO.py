from Functions import db_connect
from datetime import datetime

class MessageDAO:
  def sendNewMessage2(self, message):
    try:
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated, session_expiration_date FROM authentication_data
                      WHERE user_id=%s AND user_id=%s'''
      
      cursor.execute(auth_query, (message['sender_user_id'], message['recipient_user_id']))

      auth_user = cursor.fetchone()

      session_expiration_date = auth_user[1]

      expiration_date_str = session_expiration_date.strftime('%Y-%m-%d %H:%M:%S')

      current_date = datetime.now()

      current_date_str = current_date.strftime('%Y-%m-%d %H:%M:%S')

      
      if auth_user and current_date_str <= expiration_date_str:
        messages_query = '''INSERT INTO messages (sender_user_id, recipient_user_id, reply_id, subject, body) 
                            VALUES(%s, %s, %s, %s, %s)'''
    
        cursor.execute(messages_query, (message['sender_user_id'], message['recipient_user_id'], message['reply_id'], message['subject'], message['body']))

        recipients_query = '''INSERT INTO recipients (sender_user_id, recipient_user_id) 
                              VALUES(%s, %s)'''
    
        cursor.execute(recipients_query, (message['sender_user_id'], message['recipient_user_id']))
        conn.commit()
        
        messages_query2 = '''SELECT message_id FROM messages 
                             WHERE subject=%s AND body=%s'''

        cursor.execute(messages_query2, (message['subject'], message['body']))

        new_message2 = cursor.lastrowid
        
        return new_message2

      elif auth_user and current_date_str > session_expiration_date:
        auth_query = '''UPDATE authentication_data SET is_authenticated=0
                        WHERE user_id=%s AND user_id=%s'''
        
        cursor.execute(auth_query, (message['sender_user_id'], message['recipient_user_id']))
        conn.commit()

    except Exception as e:
      print(f'An error ocurred in sendNewMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()

    
  def updateMessage2(self, new_message):
    try:
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated, session_expiration_date FROM authentication_data
                      WHERE user_id=%s AND user_id=%s'''
      
      cursor.execute(auth_query, (new_message['sender_user_id']))

      auth_user = cursor.fetchone()

      session_expiration_date = auth_user[1]

      expiration_date_str = session_expiration_date.strftime('%Y-%m-%d %H:%M:%S')

      current_date = datetime.now()

      current_date_str = current_date.strftime('%Y-%m-%d %H:%M:%S')

      if auth_user and current_date_str <= expiration_date_str:
        messages_query = '''UPDATE messages SET recipient_user_id=%s, subject=%s, body=%s 
                            WHERE is_deleted=0 AND message_id=%s'''
    
        cursor.execute(messages_query, (new_message['recipient_user_id'], new_message['subject'], new_message['body'], new_message['message_id']))

        recipients_query = '''UPDATE recipients SET recipient_user_id=%s 
                              WHERE is_deleted=0 AND message_id=%s'''
    
        cursor.execute(recipients_query, (new_message['recipient_user_id'], new_message['message_id']))
        conn.commit()
        return True

      elif auth_user and current_date_str > session_expiration_date:
        auth_query = '''UPDATE authentication_data SET is_authenticated=0
                        WHERE user_id=%s AND user_id=%s'''
        
        cursor.execute(auth_query, (new_message['sender_user_id']))
        conn.commit()

    except Exception as e:
      print(f'An error ocurred in updateMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()


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
      return True
    
    except Exception as e:
      print(f'An error ocurred in deleteMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()


  def getMessageById2(self, message_id):
    try:
      conn, cursor = db_connect()
    
      messages_query = '''SELECT sender_user_id, recipient_user_id, subject, body, date FROM messages 
                          WHERE is_deleted=0 AND message_id=%s'''

      cursor.execute(messages_query, (message_id,))
      message_id2 = cursor.fetchone()
    
      recipients_query = '''UPDATE recipient SET is_read=1 
                            WHERE is_deleted=0 AND message_id=%s'''

      cursor.execute(recipients_query, (message_id,))
      conn.commit()
      conn.close()
      return message_id2
    
    except Exception as e:
      print(f'An error ocurred in getMessageByID: {e}')
      return False
    
    finally:
      if conn:
        conn.close()
    
  