from Functions import db_connect
from Hashing_and_Tokens import verification_hashing, generate_token
from Dates import expiration_time_gmt

class AuthenticationDAO:
    def authenticateUser(self, user_signin):
        try:
            conn, cursor = db_connect()

            users_query = '''SELECT user_id, password, salt FROM users 
                             WHERE is_deleted=0 AND first_name=%s AND last_name=%s AND email_address=%s'''

            cursor.execute(users_query, (user_signin['firstname'], user_signin['lastname'], user_signin['email']))

            user_info = cursor.fetchone()
          
            if verification_hashing(user_signin['password'], user_info['salt'], user_info['password']):
                user_auth_token = generate_token()

                session_expiration_date = expiration_time_gmt()

                auth_query = '''INSERT INTO authentication (authentication_token, session_expiration_date, user_id)
                                VALUES(%s, %s, %s) 
                        
                                ON DUPLICATE KEY UPDATE 

                                authentication_token = VALUES(authentication_token),
                                session_expiration_date = VALUES(session_expiration_date),
                                user_id = VALUES(user_id);'''
                
                cursor.execute(auth_query, (user_auth_token, session_expiration_date, user_info['user_id']))

                auth_info = '''SELECT authentication_token FROM authentication WHERE
                               user_id=%s'''

                cursor.execute(auth_info, (user_info['user_id'],))

                token = cursor.fetchone()

                conn.commit()

                return token['authentication_token']
            
            else:
                return False

        except Exception as e:
            print(f'An error occured in AuthenticateUsers: {e}')
            return False
        
        finally:
            if conn:
                conn.close()


    def verifyAuthTokens(self, user_id, token):
        try:    
            conn, cursor = db_connect()

            auth_query = '''SELECT authentication_token FROM authentication
                            WHERE NOW() < session_expiration_date AND user_id=%s AND authentication_token=%s'''

            cursor.execute(auth_query, (user_id, token))

            user_tokens = cursor.fetchone()

            return user_tokens
            
        except Exception as e:
            print(f'An error ocurred on verifyAuthTokens: {e}')
            return False


