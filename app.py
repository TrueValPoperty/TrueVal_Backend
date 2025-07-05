from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "TrueVal Backend API is running!"})

@app.route('/api/valuation')
def valuation():
    return jsonify({"value": 250000, "confidence": "high"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
