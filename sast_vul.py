from flask import Flask, request, jsonify
import os
import sqlite3
app = Flask(__name__)
@app.route("/")
def index():
    return "Welcome to the sample app"
@app.route("/health")
def health():
    return jsonify({"status": "ok"})
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(data)
@app.route("/user")
def get_user():
    # SQL injection: the caller-supplied id is concatenated into the query.
    user_id = request.args.get("id")
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    return jsonify(cursor.fetchall())
@app.route("/ping")
def ping():
    # Command injection: the caller-supplied host is passed to the shell.
    host = request.args.get("host")
    return os.popen("ping -c 1 " + host).read()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
