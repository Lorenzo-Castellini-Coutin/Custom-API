from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

class UserDAO:
  def __init__(self):  #self explains the behaviour for the rest of the class
    self.conn = sqlite3.connect('usersdatabase.db')
    self.cursor = self.conn.cursor()    #Object associated with db that allows to execute SQL commands

  def addNewUser(self, user_id, firstname, lastname, datebirth, gender, phonenum, email, passw, prem):
    self.cursor.execute("INSERT INTO users (user_id, first_name, last_name, date_of_birth, gender, phone_number, email_address, password, is_premium)", (user_id, firstname, lastname, datebirth, gender, phonenum, email, passw, prem,))

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

  def sendNewMessage(self, subject, body, date):
    self.cursor.execute("INSERT INTO messages (subject, body, date) VALUES (?,?,?)", (subject, body, date,))
    
  def deleteMessage():
    pass
  
  def getMessageById(self, messid):
    self.cursor.execute("SELECT * FROM users WHERE m_id=?", (messid,))
  
class Users:
  pass
