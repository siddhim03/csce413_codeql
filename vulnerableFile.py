import sqlite3
import os
import pickle
from flask import Flask, request

app = Flask(__name__)

db = sqlite3.connect(':memory:', check_same_thread=False)
cursor = db.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
db.commit()

@app.route('/sql_injection')
def sql_injection():
    user_input = request.args.get('username')
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    result = cursor.execute(query).fetchall()
    return str(result)  # Vulnerable to SQL Injection

@app.route('/command_injection')
def command_injection():
    filename = request.args.get('file')
    os.system(f"cat {filename}")  # Vulnerable to Command Injection
    return "File contents displayed."

@app.route('/insecure_deserialization', methods=['POST'])
def insecure_deserialization():
    data = request.data
    obj = pickle.loads(data)  # Vulnerable to Insecure Deserialization
    return str(obj)

if __name__ == '__main__':
    app.run(debug=True)
