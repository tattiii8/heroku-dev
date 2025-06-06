from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Heroku! v4")

@app.route("/api")
def api():
    return jsonify(status="ok", data={"message": "This is your API v4!"})

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/api/user")
def user_info():
    return jsonify(
        status="ok",
        data={
            "id": 1,
            "name": "Test User",
            "email": "test@example.com"
        }
    )

@app.route("/api/items")
def item_list():
    return jsonify(
        status="ok",
        data=[
            {"id": 101, "name": "Item A", "price": 10.99},
            {"id": 102, "name": "Item B", "price": 5.49},
            {"id": 103, "name": "Item C", "price": 20.00}
        ]
    )

if __name__ == "__main__":
    app.run()
