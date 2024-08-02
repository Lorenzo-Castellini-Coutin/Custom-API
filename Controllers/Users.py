from Models.UsersDAO import UserDAO
from Models.AuthenticationDAO import AuthenticationDAO
from flask import Flask, jsonify
from User_Data_Validation import *

class Users:
   def addNewUser(self, user_data):
      error_code = check_new_user_data(user_data)
      
      if error_code == 1:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif error_code == 2:
            return jsonify('One or more of the user-supplied are of invalid/unsupported type.'), 400
      
      elif error_code == 3:
            return jsonify('One or more of the user-supplied credentials are incorrect/inaccurate.'), 400
      
      else:
         new_user_id = UserDAO().addNewUser(user_data)

         if new_user_id:
            return jsonify(f'User account created. The user id is: {new_user_id}'), 200
         
         else:
            return jsonify('Something went wrong while creating the new account.'), 500
         
      
   def userLogin(self, user_data):
      error_code = check_login_data(user_data)

      if error_code == 1:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif error_code == 2:
            return jsonify('One or more of the user-supplied are of invalid/unsupported type.'), 400
      
      elif error_code == 3:
         return jsonify('One or more of the user-supplied credentials are incorrect/inaccurate.'), 400

      else:
         user_login = AuthenticationDAO().authenticateUser(user_data)
         
         if user_login:
            return jsonify(f'User authenticated. The user id is: {user_login}'), 200
         
         else:
            return jsonify('Either the user never existed/was already deleted, or something went wrong in authentication.'), 500


   
   def updateUser(self, user_data, user_id):
      error_code = check_new_user_data(user_data)

      if error_code == 1:
         return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif error_code == 2:
         return jsonify('One or more of the user-supplied are of invalid/unsupported type.'), 400
      
      elif error_code == 3:
         return jsonify('One or more of the user-supplied credentials are incorrect/inaccurate.'), 400
      
      else:
         if user_id.isdigit():
            adduser1 = UserDAO().updateUser2(user_data, user_id)

            if adduser1:
               return jsonify('User account was updated with the given information.'), 200
         
            else:
               return jsonify('Either the user never existed/was already deleted, or something went wrong in the updating.'), 500
            
         else:
            return jsonify('The user id is of invalid type or not supported.'), 400
      
      
   def getUserById(self, user_id):
      if user_id.isdigit():
         user_info1 = UserDAO().getUserById2(user_id)
         
         if user_info1:
            return jsonify(user_info1), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong with retrieving the user.'), 500
      
      else:
         return jsonify('The user id is of invalid type/not supported.'), 400
      

   def deleteUser(self, user_id):
      if user_id.isdigit():
         delete_user = UserDAO().deleteUser2(user_id)
         
         if delete_user:
            return jsonify('User deleted succesfully.'), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong with deleting the user.'), 500
      
      else:
         return jsonify('The user id is of invalid type or not supported.'), 400
      







#Notes:
#The numbers 1, 2, 3 are used for error handling in order to return a particular error message given the type of error.
#The numbers 1 and 2 used in variables mean controller functions and model functions, respectively.
#Error codes 400 mean bad request from client-side, 200 means that the execution was successful, and 500 is a server-side or db-side error.