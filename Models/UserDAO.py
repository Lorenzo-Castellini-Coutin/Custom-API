from Functions import db_connect

class UserDAO:
  def __init__(self, user_id, first_name, last_name, datebirth, gender, phone, email, passw, prem):
    self.userid = user_id
    self.first = first_name
    self.last = last_name
    self.birth = datebirth
    self.gender = gender
    self.phonenum = phone
    self.email = email
    self.passw = passw
    self.prem = prem

  db_connect()

  def addNewUser(cursor, self):
    cursor.execute("INSERT INTO users (user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, password, is_premium)", (self.userid, self.first, self.last, self.birth, self.gender, self.phonenum, self.email, self.passw, self.prem,))

  def getUserByEmail(cursor, self):
    cursor.execute("SELECT * FROM users WHERE email_address=?", (self.email,))
    return cursor.fetchall()
  
  def getUserById(cursor, self):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (self.id,))
    return cursor.fetchall()

