from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins (for testing; restrict in production)

@app.route("/days_since", methods=["POST"])
def days_since():
    data = request.json
    birthdate = data.get("birthdate")
    if not birthdate:
        return jsonify({"error": "Birthdate is required"}), 400

    from datetime import datetime
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    days_since = (today - birthdate).days

    return jsonify({"days_since": days_since})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
