from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/days_since', methods=['POST'])
def days_since():
    data = request.json
    return jsonify({"message": "CORS is now enabled!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
