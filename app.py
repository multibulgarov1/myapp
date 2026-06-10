from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 Flask API Running"

# GET
@app.route("/api/user")
def user():
    return {
        "name": "Pavel",
        "level": "beginner"
    }

# POST (НОВОЕ)
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json  # получаем данные

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return jsonify({
            "status": "success",
            "message": "Login OK"
        })

    return jsonify({
        "status": "error",
        "message": "Wrong login"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
