from flask import Flask, request, jsonify

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


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
