import sqlite3
from Models import UserDAO
from Models import MessageDAO

def db_connect():  #Function that creates connection with db
    conn = sqlite3.connect('usersdatabase.db')
    cursor = conn.cursor()
    return conn, cursor


