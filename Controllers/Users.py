from Models.UserDAO import UserDAO
from flask import Flask, jsonify, request

class Users:
   def addNewUser1(self, user_data):
      if len(user_data) == 9:
         new_user = UserDAO().addNewUser2(user_data)
         if new_user:
            return jsonify('User added succesfully.'), 200
         else:
            return jsonify('Something went wrong in the database while performing your request.'), 500
      else:
         return jsonify('Something went wrong with the info provided.'), 400

   
   def AuthenticateUser1(self, user_data):
      pass
   
   
   def updateUser1(self, user_data):
      if len(user_data) == 9:
         update_user = UserDAO().updateUser2(user_data)
         if update_user:
            return jsonify('User info updated successfully.'), 200
         else:
            return jsonify('Something went wrong in the database while performing your request.'), 500
      else:
         return jsonify('Something went wrong with the info provided.'), 400
      
      
   def getUserById1(self, user_id):
      user_info = UserDAO().getUserById2(user_id)
      if user_info is None:
         return jsonify('User not found or was already deleted.'), 400
      else:
         return jsonify(user_info), 200
      

   def deleteUser1(self, user_id):
      delete_user = UserDAO().deleteUser2(user_id)
      if delete_user:
         return jsonify('User deleted succesfully.'), 200
      else:
         return jsonify('User was either already deleted or not deleted successfully.')
      

