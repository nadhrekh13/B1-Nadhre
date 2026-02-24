import json
import sqlite3

class UserStore:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.init_db()

    def init_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )''')
        self.connection.commit()

    def load(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def save(self, user_data):
        self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (user_data['name'], user_data['email']))
        self.connection.commit()

    def find_by_id(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return self.cursor.fetchone()

    def update_user(self, user_id, updated_data):
        self.cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (updated_data['name'], updated_data['email'], user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.connection.commit()