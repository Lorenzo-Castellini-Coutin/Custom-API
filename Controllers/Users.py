from Models.UserDAO import UserDAO
from flask import Flask, jsonify, request
from Authentication_Validation import *

class Users:
   def addNewUser1(self, user_data):
      if check_datatypes(user_data):

         if check_phone_date_email_names(user_data):

            if check_datalength(user_data):
               user_add1 = UserDAO().addNewUser2(user_data)
               
               if user_add1:
                  return jsonify(f'User added successfully. Your user id is:{user_add1[0]}'), 200
                  
               else:
                  return jsonify('Something went wrong with adding the new user.'), 500

            else:
               return jsonify('One or more of the user data is longer than expected.'), 400
            
         else:
            return jsonify('Email, phone number, and/or first and last names might not be valid.'), 400
         
      else:
         return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400
      
      
   def AuthenticateUser1(self, user_data):
      if check_data_auth(user_data):
         user_info1 = UserDAO().AuthenticateUser2(user_data)
         
         if user_info1:
            return jsonify('User authenticated.'), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong in the authentication process.'), 500

      else:
         return jsonify('Email address, password, and/or first and last name might not be supported/incorrect.'), 400
   
   
   def updateUser1(self, user_data):
      if check_datatypes(user_data):

         if check_phone_date_email_names(user_data):

            if check_datalength(user_data):
               user_update1 = UserDAO().updateUser2(user_data)
               
               if user_update1:
                  return jsonify('User information updated successfully.'), 200
               
               else:
                  return jsonify('The user might not exist/already deleted, or something went wrong with updating the user.'), 500

            else:
               return jsonify('One or more of the user data is longer than expected.'), 400
            
         else:
            return jsonify('Email, phone number, and/or first and last names might not be correct.'), 400
         
      else:
         return jsonify('One or more of the user-supplied data values are of invalid type or not supported.'), 400
      
      
   def getUserById1(self, user_id):
      if type(user_id) == int and user_id > 0:
         user_info1 = UserDAO().getUserById2(user_id)
         
         if user_info1:
            return jsonify(user_info1), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong with retrieving the user.'), 500
      
      else:
         return jsonify('The user id is of invalid type or not supported.'), 400
      

   def deleteUser1(self, user_id):
      if type(user_id) == int and user_id > 0:
         delete_user1 = UserDAO().deleteUser2(user_id)
         
         if delete_user1:
            return jsonify('User deleted succesfully.'), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong with deleting the user.'), 500
      
      else:
         return jsonify('The user id is of invalid type or not supported.'), 400
      

