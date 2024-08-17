from Functions import db_connect

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

      new_message = cursor.fetchone()

      recipients_query = '''INSERT INTO recipients (sender_user_id, recipient_user_id, message_id, reply_id) 
                            VALUES(%s, %s, %s, %s)'''
    
      cursor.execute(recipients_query, (message['sender_user_id'], message['recipient_user_id'], new_message['message_id'], message['reply_id']))
      conn.commit()
        
      return new_message['message_id']

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
                          WHERE is_deleted=0 AND message_id=%s AND sender_user_id=%s'''
    
      cursor.execute(messages_query, (new_message['recipient_user_id'], new_message['subject'], new_message['body'], message_id, new_message['sender_user_id']))

      update = cursor.rowcount

      recipients_query = '''UPDATE recipients SET is_read=0, recipient_user_id=%s 
                            WHERE message_id=%s'''
    
      cursor.execute(recipients_query, (new_message['recipient_user_id'], message_id,))
      conn.commit()

      if not update:
        return False
      
      else:
        return update

    except Exception as e:
      print(f'An error ocurred in updateMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()

  
  def getInbox(self, recipient_user_id):
    try:
      conn, cursor = db_connect()

      recipients_query = '''UPDATE recipients SET is_read=1 
                            WHERE is_deleted=0 AND recipient_user_id=%s'''
      
      cursor.execute(recipients_query, (recipient_user_id,))
      conn.commit()
      
      messages_query = '''SELECT m.message_id, m.subject, m.body, m.sender_user_id, m.reply_id, m.message_date, m.last_update_date FROM messages m
                          JOIN recipients r ON m.message_id = r.message_id
                          WHERE r.is_deleted=0 AND r.recipient_user_id=%s'''
      
      cursor.execute(messages_query, (recipient_user_id,))
      
      inbox = cursor.fetchall()
    
      return inbox
  
    
    except Exception as e:
      print(f'An error occured in getInbox: {e}')
      return False
    
    finally:
      if conn: 
        conn.close()
    

  def getSent(self, sender_user_id):
    try:
      conn, cursor = db_connect()

      messages_query = '''SELECT subject, body, recipient_user_id, message_date, last_update_date, message_id FROM messages
                          WHERE is_deleted=0 AND sender_user_id=%s'''
      
      cursor.execute(messages_query, (sender_user_id,))

      sent = cursor.fetchall()

      conn.commit()
      return sent

    except Exception as e:
      print(f'An error ocurred in getSent: {e}')
      return False
    
    finally:
      if conn:
        conn.close()


  def deleteMessage(self, user_id, message_id):  
    try:
      conn, cursor = db_connect()

      messages_query = '''UPDATE messages SET is_deleted=1 
                          WHERE message_id=%s AND sender_user_id=%s'''
    
      cursor.execute(messages_query, (message_id, user_id['user_id']))
      conn.commit()

      delete_sender_message = cursor.lastrowid

      if not delete_sender_message:
        recipients_query = '''UPDATE recipients SET is_deleted=1 AND is_read=1
                              WHERE message_id=%s AND recipient_user_id=%s'''
        
        cursor.execute(recipients_query, (message_id, user_id['user_id']))
        conn.commit()

        return True
      
      else:
        return delete_sender_message
    
    except Exception as e:
      print(f'An error ocurred in deleteMessage: {e}')
      return False
    
    finally:
      if conn:
        conn.close()


  def getMessageById(self, user_id, message_id):
    try:
      conn, cursor = db_connect()
    
      messages_query = '''SELECT sender_user_id, recipient_user_id, subject, body, message_date FROM messages 
                          WHERE is_deleted=0 AND message_id=%s AND sender_user_id=%s'''

      cursor.execute(messages_query, (message_id, user_id['user_id']))
      
      get_sender_message = cursor.fetchone()
      
      if not get_sender_message:
      
        messages_query = '''SELECT sender_user_id, recipient_user_id, subject, body, message_date FROM messages 
                            WHERE message_id=%s AND recipient_user_id=%s'''
        
        cursor.execute(messages_query, (message_id, user_id['user_id']))

        get_recipient_message = cursor.fetchone()

        recipients_query = '''UPDATE recipients SET is_read=1
                              WHERE is_deleted=0 AND message_id=%s AND recipient_user_id=%s'''
        
        cursor.execute(recipients_query,(message_id, user_id['user_id']))

        conn.commit()

        return get_recipient_message
      
      else:
        return get_sender_message
    
    except Exception as e:
      print(f'An error ocurred in getMessageByID: {e}')
      return False
    
    finally:
      if conn:
        conn.close()
    
  