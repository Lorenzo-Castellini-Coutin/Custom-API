from Functions import db_connect

class MessageDAO:
  db_connect()

  def sendNewMessage(self, subject, body, date):
    self.cursor.execute("INSERT INTO messages (subject, body, date) VALUES (?,?,?)", (subject, body, date,))
    
  def deleteMessage(self, subject):  #Ask how will the message be found?
    self.cursor.execute("")
  
  def getMessageById(self, messid):
    self.cursor.execute("SELECT * FROM users WHERE m_id=?", (messid,))