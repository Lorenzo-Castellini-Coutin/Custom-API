from Functions import db_connect

class UserDAO:
  def addNewUser2(self, user_data):
    conn, cursor = db_connect()
    
    query = '''INSERT INTO users (user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, password, is_premium)
                VALUES(?,?,?,?,?,?,?,?,?)'''
    
    cursor.execute(query, (user_data['user_id'], user_data['firstname'], user_data['lastname'], user_data['birthdate'], user_data['gender'], user_data['phone'], user_data['email'], user_data['password'], user_data['premium']))
    conn.commit()
    conn.close()

  def getUserByEmail2(self, user_email):
    conn, cursor = db_connect()
    query = 'SELECT user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address FROM users WHERE is_deleted=0 and email_address=?'
    cursor.execute(query, (user_email,))
    user_email2 = cursor.fetchone()
    conn.commit()
    conn.close()
    return user_email2
  
  def getUserById2(self, user_id):
    conn, cursor = db_connect()
    query = 'SELECT user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address FROM users WHERE is_deleted=0 and user_id=?'
    cursor.execute(query, ((user_id,)))
    user_id2 = cursor.fetchone()
    conn.commit()
    conn.close()
    return user_id2
   

