from Models.UsersDAO import UserDAO
from Models.AuthenticationDAO import AuthenticationDAO
from flask import jsonify
from Data_Validation import *

class Users:
   def addNewUser(self, user_data):
      error_code = validate_user(user_data)
      
      match error_code:
         case 1:   
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
         case 2:
            return jsonify('One or more of the user-supplied are of invalid/unsupported type.'), 400
      
         case 3:
            return jsonify('One or more of the user-supplied credentials are incorrect/inaccurate.'), 400
      
         case 100:
            new_user_id = UserDAO().addNewUser(user_data)

            if new_user_id:
               return jsonify(f'User account created. The user id is: {new_user_id}.'), 200
         
            else:
               return jsonify('Something went wrong.'), 500
         
      
   def userLogin(self, user_data):
      error_code = validate_login(user_data)

      match error_code:
         case 1:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
         case 2:
            return jsonify('One or more of the user-supplied are of invalid/unsupported type.'), 400
      
         case 3:
            return jsonify('One or more of the user-supplied credentials are incorrect/inaccurate.'), 400

         case 100:
            user_login = AuthenticationDAO().authenticateUser(user_data)
         
            if user_login:
               return jsonify(f'User authenticated. The user id is: {user_login}.'), 200
         
            else:
               return jsonify('The user might have been deleted/never existed.'), 404


   def updateUser(self, user_data, user_id):
      error_code = validate_user(user_data)

      match error_code:
         case 1:
            return jsonify('One or more of the user-supplied data execeeded the maximum length supported.'), 400
      
         case 2:
            return jsonify('One or more of the user-supplied are of invalid/unsupported type.'), 400
      
         case 3:
            return jsonify('One or more of the user-supplied credentials are incorrect/inaccurate.'), 400
      
         case 100:
            if user_id.isdigit():
               user_auth = AuthenticationDAO().verifyAuthTokens(user_id)

               if user_auth:
                  update_user = UserDAO().updateUser(user_data, user_id)

                  if update_user:
                     return jsonify(f'User with id: {update_user}, was updated.'), 200
               
                  else:
                     return jsonify('The user might have been deleted/never existed.'), 404
         
               else:
                  return jsonify('The user is not authenticated.'), 401
            
            else:
               return jsonify('The user id is of invalid type or not supported.'), 400
      
      
   def getUserById(self, user_id):
      if user_id.isdigit():
         user_auth = AuthenticationDAO().verifyAuthTokens(user_id)

         if user_auth:
            user_info = UserDAO().getUserById(user_id)

            if user_info:
               return jsonify(user_info), 200
         
            else:
               return jsonify('The user might have been deleted/never existed.'), 404

         else:
            return jsonify('User is not authenticated.'), 401
      
      else:
         return jsonify('The user id is of invalid type/not supported.'), 400
      

   def deleteUser(self, user_id):
      if user_id.isdigit():
         user_auth = AuthenticationDAO().verifyAuthTokens(user_id)
         
         if user_auth:
            delete_user = UserDAO().deleteUser(user_id)

            if delete_user:
               return jsonify(f'User with id: {delete_user}, was deleted.'), 200
            
            else:
               return jsonify('The user might not exist/already deleted, or something went wrong.'), 404
         
         else:
            return jsonify('User is not authenticated.'), 401
         
      else:
         return jsonify('The user id is of invalid type or not supported.'), 400
      






