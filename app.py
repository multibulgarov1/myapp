from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# -----------------------------
# БАЗА ДАННЫХ
# -----------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# ГЛАВНАЯ
# -----------------------------
@app.route("/")
def home():
    return "🔥 Flask + SQLite работает"

# -----------------------------
# РЕГИСТРАЦИЯ
# -----------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, password))
        conn.commit()
        return jsonify({"status": "success", "message": "User created"})
    except:
        return jsonify({"status": "error", "message": "User exists"})
    finally:
        conn.close()

# -----------------------------
# ЛОГИН ЧЕРЕЗ БАЗУ
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))

    user = c.fetchone()
    conn.close()

    if user:
        return jsonify({"status": "success", "message": "Login OK"})
    else:
        return jsonify({"status": "error", "message": "Wrong login"})

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
