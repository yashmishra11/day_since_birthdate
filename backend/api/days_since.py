from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/api/days_since', methods=['POST'])
def days_since():
    data = request.get_json()
    birthdate_str = data.get('birthdate')

    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({'error': 'Invalid birthdate format. Use YYYY-MM-DD.'}), 400

    days_difference = (datetime.now() - birthdate).days
    return jsonify({'days_since': days_difference})

# Vercel-specific handler
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
