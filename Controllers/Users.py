from Models.UserDAO import UserDAO
from flask import Flask, jsonify, request
from Authentication_Validation import *

class Users:
   def addNewUser1(self, user_data):
      checks = check_new_user_data(user_data)
      
      if checks == 1:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif checks == 2:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif checks == 3:
            return jsonify('Verify that the user-supplied data is correct/accurate.'), 400
      
      else:
         adduser1 = UserDAO().addNewUser2(user_data)

         if adduser1:
            return jsonify(f'User account created. The user id is: {adduser1}'), 200
         
         else:
            return jsonify('Something went wrong while creating the new account.'), 500
         
      
   def AuthenticateUser1(self, user_data):
      checks = check_auth_data(user_data)

      if checks == 1:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif checks == 2:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif checks == 3:
         return jsonify('Verify that the user-supplied credentials are correct/accurate.'), 400

      else:
         user_auth1 = UserDAO().AuthenticateUser2(user_data)
         
         if user_auth1:
            return jsonify('User authenticated.'), 200
         
         else:
            return jsonify('Either the user never existed/was already deleted, or something went wrong in authentication.'), 500


   
   def updateUser1(self, user_data):
      checks = check_new_user_data(user_data)

      if checks == 1:
         return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif checks == 2:
         return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
      elif checks == 3:
         return jsonify('Verify that the user-supplied data is correct/accurate.'), 400
      
      else:
         adduser1 = UserDAO().updateUser2(user_data)

         if adduser1:
            return jsonify('User account was updated with the given information.'), 200
         
         else:
            return jsonify('Either the user never existed/was already deleted, or something went wrong in the updating.'), 500
      
      
   def getUserById1(self, user_id):
      if user_id.isdigit():
         user_info1 = UserDAO().getUserById2(user_id)
         
         if user_info1:
            return jsonify(user_info1), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong with retrieving the user.'), 500
      
      else:
         return jsonify('The user id is of invalid type or not supported.'), 400
      

   def deleteUser1(self, user_id):
      if user_id.isdigit():
         delete_user1 = UserDAO().deleteUser2(user_id)
         
         if delete_user1:
            return jsonify('User deleted succesfully.'), 200
         
         else:
            return jsonify('The user might not exist/already deleted, or something went wrong with deleting the user.'), 500
      
      else:
         return jsonify('The user id is of invalid type or not supported.'), 400
      







#Notes:
#The numbers 1, 2, 3 are used for error handling in order to return a particular error message given the type of error.
#The numbers 1 and 2 used in variables mean controller functions and model functions, respectively.
#Error codes 400 mean bad request from client-side, 200 means that the execution was successful, and 500 is a server-side or db-side error.