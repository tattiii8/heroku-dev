from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Heroku! v4")

@app.route("/api")
def api():
    return jsonify(status="ok", data={"message": "This is your API v4!"})


if __name__ == "__main__":
    app.run()
