from Functions import db_connect
from Hashing import hashing_with_salt, verification_hashing
from Authentication_Validation import generate_token

class UserDAO:
  def addNewUser2(self, user_data):
    try:  
      conn, cursor = db_connect() 
    
      pw, salt = hashing_with_salt(user_data['password'])
    
      users_query = '''INSERT INTO users (first_name, last_name, date_of_birth, gender, phone_number, email_address, password, salt, is_premium) 
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
      cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium']))
      conn.commit()
      conn.close()
      return True

    except:
      return False


  def AuthenticateUser2(self, user_data):
    try:  
      conn, cursor = db_connect()

      users_query = '''SELECT user_id, password, salt FROM users WHERE is_deleted=0, first_name=%s, last_name=%s, email=%s'''

      cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['email']))
      user_info2 = cursor.fetchone()

      pw = verification_hashing(user_data['password'], user_info2['salt'])
      
      if user_info2['password'] == pw:
        token = generate_token()
        is_auth = 1
        auth_query = '''INSERT INTO authentication_data (user_id, authentication_token, is_authenticated)
                        VALUES(%s, %s, %s)'''
        
        cursor.execute(auth_query, (user_info2['user_id'], token, is_auth))
        conn.commit()
        conn.close()
    
    except:
      return False

    
  def updateUser2(self, user_data):
    try:
      conn, cursor = db_connect()
    
      auth_query = '''SELECT is_authenticated FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, user_data['user_id'])

      auth_user = cursor.fetchone()

      if auth_user:
        pw, salt = hashing_with_salt(user_data['password'])

        users_query = '''UPDATE users SET first_name=%s, last_name=%s, date_of_birth=%s, gender=%s, phone_number=%s, email_address=%s, password=%s, salt=%s, is_premium=%s 
                         WHERE is_deleted=0 and user_id=%s'''
    
        cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium'], user_data['user_id']))
        conn.commit()
        conn.close()
        return True
      
      else:
        return False

    except:
      return False

  
  def getUserById2(self, user_id):
    try:  
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, (user_id,))

      auth_user = cursor.fetchone()

      if auth_user:
        users_query = '''SELECT user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, is_premium FROM users 
                         WHERE is_deleted=0 and user_id=%s'''
    
        cursor.execute(users_query, (user_id,))
        user_info2 = cursor.fetchone()
        conn.close()
        return user_info2

      else:
        return False
      
    except:
      return False
  
  
  def deleteUser2(self, user_id):
    try:
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, (user_id,))

      auth_user = cursor.fetchone()
      
      if auth_user:
        users_query = '''UPDATE users SET is_deleted=1 WHERE user_id=%s'''

        cursor.execute(users_query, (user_id,))

        auth_query = '''UPDATE authentication_data SET is_authenticated=0 WHERE user_id=%s'''

        cursor.execute(auth_query, (user_id,))
        conn.commit()
        conn.close()
        return True
      
      else:
        return False

    except:
      return False

  
  
   

