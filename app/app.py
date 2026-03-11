from flask import Flask, jsonify
import os

app = Flask(__name__)
FAKE_API_KEY = "AKIA1234567890ABCD12"
@app.route("/")
def home():
    return jsonify({
        "message": "Secure CI/CD Secret Detection Project",
        "status": "running"
    })

@app.route("/health")
def health():
    api_key = os.getenv("API_KEY", "not_set")
    return jsonify({
        "health": "ok",
        "api_key_configured": api_key != "not_set"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
