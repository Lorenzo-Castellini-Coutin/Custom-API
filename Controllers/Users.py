from Models import UserDAO
from flask import Flask, jsonify, request

class Users:
  def addNewUser(new_user_data):
    UserDAO.addNewUser(new_user_data)

  def getUserByEmail(self):
    pass

  def getUsersById(self):
    pass