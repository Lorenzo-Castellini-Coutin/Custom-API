from Functions import db_connect
from Hashing_and_Tokens import hashing_with_salt


class UserDAO:
  def addNewUser(self, user_data):
    try:  
      conn, cursor = db_connect() 
    
      pw, salt = hashing_with_salt(user_data['password'])
    
      users_query = '''INSERT INTO users (first_name, last_name, date_of_birth, gender, phone_number, email_address, password, salt, is_premium) 
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
      cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium']))
      conn.commit()
      
      new_user_id = cursor.lastrowid
      
      return new_user_id
      
    except Exception as e:
      print(f'An error ocurred in addNewUser: {e}')
      return False
    
    finally:
     if conn:
      conn.close()

    
  def updateUser(self, user_data, user_id):
    try:
      conn, cursor = db_connect()

      users_query = '''UPDATE users SET first_name=%s, last_name=%s, date_of_birth=%s, gender=%s, phone_number=%s, email_address=%s, password=%s, salt=%s, is_premium=%s 
                       WHERE is_deleted=0 AND user_id=%s'''
    
      cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium'], user_id,))
      conn.commit()
      conn.close()
      
      update_user_id = cursor.lastrowid
      return update_user_id

    except Exception as e:
      print(f'An error ocurred in updateUser: {e}')
      return False
    
    finally:
      if conn:
        conn.close()

  
  def getUserById(self, user_id):
    try:  
      conn, cursor = db_connect()
  
      users_query = '''SELECT user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, is_premium FROM users 
                       WHERE is_deleted=0 AND user_id=%s'''
    
      cursor.execute(users_query, (user_id,))
      user_info = cursor.fetchone()
      conn.close()
      return user_info
      
    except Exception as e:
      print(f'An error ocurred in getUserById: {e}')
      return False
    
    finally:
      if conn:
        conn.close()
  
  
  def deleteUser(self, user_id):
    try:
      conn, cursor = db_connect()
      
      users_query = '''UPDATE users SET is_deleted=1 WHERE user_id=%s'''

      cursor.execute(users_query, (user_id,))

      auth_query = '''UPDATE authentication_data SET is_authenticated=0 WHERE user_id=%s'''

      cursor.execute(auth_query, (user_id,))
      conn.commit()
      
      delete_user = cursor.lastrowid
      return delete_user

    except Exception as e:
      print(f'An error ocurred in deleteUser: {e}')
      return False
    
    finally:
      if conn:
        conn.close()

  
  
   

