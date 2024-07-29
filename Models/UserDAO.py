from Functions import db_connect
from Hashing import hashing_with_salt, verification_hashing
from Authentication_Validation import generate_token
from datetime import datetime, timedelta

class UserDAO:
  def addNewUser2(self, user_data):
    try:  
      conn, cursor = db_connect() 
    
      pw, salt = hashing_with_salt(user_data['password'])
    
      users_query = '''INSERT INTO users (first_name, last_name, date_of_birth, gender, phone_number, email_address, password, salt, is_premium) 
                       VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
      cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium']))
      conn.commit()
      user_add2 = cursor.lastrowid
      return user_add2

    except:
      return False
    
    finally:
     if conn:
      conn.close()


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
        expiration_date = datetime.now() + timedelta(days = 7)
        
        auth_query = '''INSERT INTO authentication_data (user_id, authentication_token, is_authenticated, session_expiration_date)
                        VALUES(%s, %s, %s, %s)'''
        
        cursor.execute(auth_query, (user_info2['user_id'], token, is_auth, expiration_date))
        conn.commit()
        
        auth_user2 = cursor.lastrowid
        
        return auth_user2
      
    except:
      return False
    
    finally:
      if conn:  
        conn.close()

    
  def updateUser2(self, user_data):
    try:
      conn, cursor = db_connect()
    
      auth_query = '''SELECT is_authenticated, session_expiration_date FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, user_data['user_id'])

      auth_user = cursor.fetchone()

      current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      if auth_user and current_date <= auth_user[1]:
        pw, salt = hashing_with_salt(user_data['password'])

        users_query = '''UPDATE users SET first_name=%s, last_name=%s, date_of_birth=%s, gender=%s, phone_number=%s, email_address=%s, password=%s, salt=%s, is_premium=%s 
                         WHERE is_deleted=0 and user_id=%s'''
    
        cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], pw, salt, user_data['premium'], user_data['user_id']))
        conn.commit()
        conn.close()
        return True
      
      elif auth_user and current_date > auth_user[1]:
        auth_query = '''UPDATE authentication_data SET is_authenticated=0
                        WHERE user_id=%s'''
        
        cursor.execute(auth_query,user_data['user_id'])
        conn.commit()
        conn.close()

      else:
        conn.close()
        return False
        

    except Exception as e:
      print(e)
      return False
    
    finally:
      conn.close()

  
  def getUserById2(self, user_id):
    try:  
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated, session_expiration_date FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, (user_id,))

      auth_user = cursor.fetchone()

      current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


      if auth_user and current_date <= auth_user[1] :
        users_query = '''SELECT user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, is_premium FROM users 
                         WHERE is_deleted=0 and user_id=%s'''
    
        cursor.execute(users_query, (user_id,))
        user_info2 = cursor.fetchone()
        conn.close()
        return user_info2

      elif auth_user and current_date > auth_user[1]:
        auth_query = '''UPDATE authentication_data SET is_authenticated=0
                        WHERE user_id=%s'''
        
        cursor.execute(auth_query, (user_id,))
        conn.commit()
        conn.close()

      else:
        conn.close()
        return False
      
    except:
      return False
    
    finally:
      conn.close()
  
  
  def deleteUser2(self, user_id):
    try:
      conn, cursor = db_connect()
      
      auth_query = '''SELECT is_authenticated, session_expiration date FROM authentication_data
                      WHERE user_id=%s'''
      
      cursor.execute(auth_query, (user_id,))

      auth_user = cursor.fetchone()

      current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      
      if auth_user and current_date <= auth_user[1]:
        users_query = '''UPDATE users SET is_deleted=1 WHERE user_id=%s'''

        cursor.execute(users_query, (user_id,))

        auth_query = '''UPDATE authentication_data SET is_authenticated=0 WHERE user_id=%s'''

        cursor.execute(auth_query, (user_id,))
        conn.commit()
        conn.close()
        return True
      
      elif auth_user and current_date > auth_user[1]:
        auth_query = '''UPDATE authentication_data SET is_authenticated=0
                        WHERE user_id=%s'''
        
        cursor.execute(auth_query, (user_id,))
        conn.commit()
        conn.close()

      else:
        conn.close()
        return False

    except:
      return False
    
    finally:
      conn.close()

  
  
   

