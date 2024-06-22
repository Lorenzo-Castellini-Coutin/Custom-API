from Models.UserDAO import UserDAO
from flask import Flask, jsonify, request

class Users:
   def addNewUser1(self, user_data):
      UserDAO().addNewUser2(user_data)
      
   def getUserByEmail1(self, user_email):
      user_email1 = UserDAO.getUserByEmail2(user_email)
      return user_email1

   def getUsersById(self):
      pass