import flask
import sqlite3

class UserDAO:
  def __init__(self):
    self.conn = sqlite3.connect('usersdatabase.db')
    self.cursor = self.conn.cursor()

  def addNewUser():
    pass
  def getUserByEmail():
    pass
  def getUserById():
    pass

class MessageDAO:
  def __init__(self):
    pass
  def sendNewMessage():
    pass
  def deleteMessage():
    pass
  def getMessageById():
    pass
  
class Users:
  
#class Messages: