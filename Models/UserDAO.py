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
    query = '''SELECT * FROM users WHERE email_address=? and is_deleted=0''', (user_email)
    user_email2 = cursor.fetchall(query, user_email)
    conn.commit()
    conn.close()
    return user_email2
  
  def getUserById(cursor, self):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (self.id,))
    return cursor.fetchall()

