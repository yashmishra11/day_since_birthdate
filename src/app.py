from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Route to calculate the number of days since the provided birthdate
@app.route('/days_since', methods=['POST'])
def days_since():
    # Get the birthdate from the request body
    data = request.get_json()
    birthdate_str = data.get('birthdate')

    # Validate if the birthdate is provided in the correct format (YYYY-MM-DD)
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({'error': 'Invalid birthdate format. Use YYYY-MM-DD.'}), 400

    # Calculate the difference in days
    current_date = datetime.now()
    days_difference = (current_date - birthdate).days

    # Return the result as JSON
    return jsonify({'days_since': days_difference})

if __name__ == '__main__':
    app.run(debug=True)
