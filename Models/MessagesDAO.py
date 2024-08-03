from Functions import db_connect
from datetime import datetime

class MessageDAO:
  def sendNewMessage(self, message):
    try:
      conn, cursor = db_connect()
    
      messages_query = '''INSERT INTO messages (sender_user_id, recipient_user_id, subject, body, reply_id) 
                          VALUES(%s, %s, %s, %s, %s)'''
    
      cursor.execute(messages_query, (message['sender_user_id'], message['recipient_user_id'], message['subject'], message['body'], message['reply_id']))

      messages_info_query = '''SELECT message_id, reply_id FROM messages 
                               WHERE subject=%s AND body=%s'''

      cursor.execute(messages_info_query, (message['subject'], message['body']))

      new_message = cursor.lastrowid

      new_message_id = new_message['message_id']

      recipients_query = '''INSERT INTO recipients (sender_user_id, recipient_user_id, message_id, reply_id) 
                            VALUES(%s, %s, %s, %s)'''
    
      cursor.execute(recipients_query, (message['sender_user_id'], message['recipient_user_id'], new_message_id, message['reply_id']))
      conn.commit()
        
      return new_message

    except Exception as e:
      print(f'An error ocurred in sendNewMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()

    
  def updateMessage(self, new_message, message_id):
    try:
      conn, cursor = db_connect()
      
      messages_query = '''UPDATE messages SET recipient_user_id=%s, subject=%s, body=%s 
                          WHERE is_deleted=0 AND message_id=%s'''
    
      cursor.execute(messages_query, (new_message['recipient_user_id'], new_message['subject'], new_message['body'], message_id,))

      recipients_query = '''UPDATE recipients SET recipient_user_id=%s 
                            WHERE is_deleted=0 AND message_id=%s'''
    
      cursor.execute(recipients_query, (new_message['recipient_user_id'], message_id,))
      conn.commit()
      return True

    except Exception as e:
      print(f'An error ocurred in updateMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()


  def deleteMessage(self, del_message):  
    try:
      conn, cursor = db_connect()

      messages_query = '''UPDATE messages SET is_deleted=1 
                          WHERE message_id=%s'''
    
      cursor.execute(messages_query, (del_message,))
    
      recipients_query = '''UPDATE recipients SET is_deleted=1 
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


  def getMessageById(self, message_id):
    try:
      conn, cursor = db_connect()
    
      messages_query = '''SELECT sender_user_id, recipient_user_id, subject, body, message_date FROM messages 
                          WHERE is_deleted=0 AND message_id=%s'''

      cursor.execute(messages_query, (message_id,))
      message_id2 = cursor.fetchone()
    
      recipients_query = '''UPDATE recipients SET is_read=1 
                            WHERE is_deleted=0 AND message_id=%s'''

      cursor.execute(recipients_query, (message_id,))
      conn.commit()
      return message_id2
    
    except Exception as e:
      print(f'An error ocurred in getMessageByID: {e}')
      return False
    
    finally:
      if conn:
        conn.close()
    
  