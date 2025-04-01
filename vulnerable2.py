from flask import Flask, request
import sqlite3

app = Flask(__name__)

db_file = "vulnerable.db"

# Initialize database
def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ""
    )
    conn.commit()
    conn.close()

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # **VULNERABLE SQL QUERY** (Allows SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return "Login Successful!"
    else:
        return "Invalid Credentials", 401

if __name__ == "__main__":
    init_db()
    app.run(debug=True)