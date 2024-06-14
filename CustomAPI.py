import flask
import sqlite3

class UserDAO:
  def __init__(self):
    self.conn = sqlite3.connect('usersdatabase.db')
    self.cursor = self.conn.cursor()

  def addNewUser():
    pass
  def getUserByEmail(self, email):
    self.cursor.execute("SELECT * FROM users WHERE email_address=?", (email,))
    return self.cursor.fetchall()
  
  def getUserById(self, id):
    self.cursor.execute("SELECT * FROM users WHERE user_id=?", (id,))
    return self.cursor.fetchall()

class MessageDAO:
  def __init__(self):
    self.conn = sqlite3.connect('usersdatabase.db')
    self.cursor = self.conn.cursor()

  def sendNewMessage():
    pass
  def deleteMessage():
    pass
  def getMessageById(self, messid):
    self.cursor.execute("SELECT * FROM users WHERE")
  
class Users:
  
#class Messages: