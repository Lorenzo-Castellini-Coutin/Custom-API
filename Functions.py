import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def db_connect():
    connection = mysql.connector.connect (
        host = os.getenv('SERVER_HOST'),
        port = os.getenv('SERVER_PORT'),
        user = os.getenv('DB_user'),
        password = os.getenv('DB_password'),
        database = os.getenv('DB_name')
    )
    cursor = connection.cursor()
    return connection, cursor




