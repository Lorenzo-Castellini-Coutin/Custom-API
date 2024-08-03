from Functions import db_connect
from Hashing_and_Tokens import verification_hashing, generate_token
from Dates import expiration_time_utc

class AuthenticationDAO:
    def authenticateUser(self, user_data):
        try:
            conn, cursor = db_connect()

            users_query = '''SELECT user_id, password, salt FROM users 
                             WHERE is_deleted=0 AND first_name=%s AND last_name=%s AND email_address=%s'''

            cursor.execute(users_query, (user_data['firstname'], user_data['lastname'], user_data['email']))

            user_info = cursor.fetchone()

            user_match = verification_hashing(user_data['password'], user_info['salt'], user_info['password'])

            if user_match:
                user_auth_token = generate_token()

                session_expiration_date = expiration_time_utc()

                auth_query = '''INSERT INTO authentication_data (authentication_token, session_expiration_date, user_id)
                                VALUES(%s, %s, %s) 
                        
                                ON DUPLICATE KEY UPDATE 

                                authentication_token = VALUES(authentication_token),
                                session_expiration_date = VALUES(session_expiration_date),
                                user_id = VALUES(user_id);'''
                
                cursor.execute(auth_query, (user_auth_token, session_expiration_date, user_data['user_id']))

                return user_data['user_id']

        except Exception as e:
            print(f'An error occured in AuthenticateUsers: {e}')
            return False
        
        finally:
            if conn:
                conn.close()


    def verifyAuthTokens(self, user_id):
        try:    
            conn, cursor = db_connect()

            auth_query = '''SELECT authentication_token FROM authentication_data
                            WHERE NOW() <= session_expiration_date AND user_id=%s'''

            user_tokens = cursor.fetchone(auth_query, (user_id,))

            if user_tokens:
                return True
        
            else:
                return False
            
        except Exception as e:
            print(f'An error ocurred on verifyAuthTokens: {e}')
            return False



