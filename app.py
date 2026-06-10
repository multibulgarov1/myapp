from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 My First Auto Deploy Flask App"

@app.route("/api")
def api():
    return {"status": "ok"}

@app.route("/api/user")
def user():
    return {
        "name": "Pavel",
        "level": "beginner"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
