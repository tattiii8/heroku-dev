from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Heroku! v2")

@app.route("/api")
def api():
    return jsonify(status="ok", data={"message": "This is your API v2!"})

if __name__ == "__main__":
    app.run()
