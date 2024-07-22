from Functions import db_connect
from Hashing import hashing

class UserDAO:
  def addNewUser2(self, user_data):
    conn, cursor = db_connect() 
    
    pw, salt = hashing(user_data['password'])
    
    query = '''INSERT INTO users (first_name, last_name, date_of_birth, gender, phone_number, email_address, password, salt, is_premium) 
               VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
    cursor.execute(query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium']))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes <= 0:
      return False
    else:
      return True
    
  def updateUsers2(self, user_data):
    conn, cursor = db_connect()
    query = '''UPDATE users SET first_name=%s, last_name=%s, date_of_birth=%s, gender=%s, phone_number=%s, email_address=%s, password=%s, is_premium=%s 
               WHERE is_deleted=0 and user_id=%s'''
    
    cursor.execute(query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], user_data['password'], user_data['premium'], user_data['user_id']))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes <= 0:
      return False
    else:
      return True
  
  def getUserById2(self, user_id):
    conn, cursor = db_connect()
    query = '''SELECT user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, is_premium FROM users 
               WHERE is_deleted=0 and user_id=%s'''
    
    cursor.execute(query, (user_id,))
    user_info2 = cursor.fetchone()
    conn.close()
    return user_info2
  
  def deleteUsers2(self, user_id):
    conn, cursor = db_connect()
    query = 'UPDATE users SET is_deleted=1 WHERE user_id=%s'

    cursor.execute(query, (user_id,))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes <= 0:
      return False
    else:
      return True
  
  
   

