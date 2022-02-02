from cgitb import reset
import sqlite3
from unittest import result

class Database():

    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite')
        self.conn.row_factory = sqlite3.Row
    
    def get_messages(self):
        result = self.conn.execute('SELECT * FROM  messages')
        return result.fetchall()

    def insert_message(self, user, message):
        self.conn.execute('INSERT  INTO messages (user, message) VALUES (?, ?)', [user, message])
        self.conn.commit()