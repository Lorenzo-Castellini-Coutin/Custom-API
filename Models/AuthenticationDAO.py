from Functions import db_connect
from Hashing import verification_hashing

class AuthenticationDAO:
    def AuthenticateUser(self, user_data):
        try:
            conn, cursor = db_connect()

        except Exception as e:
            print(f'An error occured in AuthenticateUsers: {e}')
            return False
        
        finally:
            if conn:
                conn.close()




def generate_token():
    auth_token = secrets.token_bytes(32)
    return auth_token
