from Models.UserDAO import UserDAO
from flask import Flask, jsonify, request
from Authentication_Validation import *

class Users:
   def addNewUser1(self, user_data):
      if check_datatypes(user_data):

         if check_phone_and_names(user_data):

            if check_datalength(user_data):
               user_add = UserDAO().addNewUser2(user_data)
               
               if user_add:
                  return jsonify('User added successfully.'), 200
                  
               else:
                  return jsonify('Something went wrong with adding the new user.'), 500

            else:
               return jsonify('One or more of the user data is longer than expected.'), 400
            
         else:
            return jsonify('Email, phone number, and/or first and last names might not be valid.'), 400
         
      else:
         return jsonify('One or more of the user data is not supported.'), 400
      
      
   def AuthenticateUser1(self, user_data):
      if check_data_auth(user_data):
         user_info = UserDAO().AuthenticateUser2(user_data)
         
         if user_info:
            return jsonify('User authenticated.'), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong in the authentication process.'), 500

      else:
         return jsonify('Email, password, and/or first and last names might not be supported'), 400
   
   
   def updateUser1(self, user_data):
      if check_datatypes(user_data):

         if check_phone_and_names(user_data):

            if check_datalength(user_data):
               user_update = UserDAO().updateUser2(user_data)
               
               if user_update:
                  return jsonify('User information updated successfully.'), 200
               
               else:
                  return jsonify('The user might not exist/already deleted, or something went wrong updating the user.'), 500

            else:
               return jsonify('One or more of the user data is longer than expected.'), 400
            
         else:
            return jsonify('Email, phone number, and/or first and last names might not be correct.'), 400
         
      else:
         return jsonify('One or more of the user data is not supported.'), 400
      
      
   def getUserById1(self, user_id):
      if user_id > 0:
         user_info = UserDAO().getUserById2(user_id)
         
         if user_info:
            return jsonify(user_info), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong retrieving the user.'), 500
      
      else:
         return jsonify('User ID is of unsupported type.'), 400
      

   def deleteUser1(self, user_id):
      delete_user = UserDAO().deleteUser2(user_id)
      if delete_user:
         return jsonify('User deleted succesfully.'), 200
      else:
         return jsonify('The user might not exist/already deleted, or something went wrong retrieving the user.'), 500
      

