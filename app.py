from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Heroku!")

@app.route("/api")
def api():
    return jsonify(status="ok", data={"message": "This is your API!"})

if __name__ == "__main__":
    app.run()
