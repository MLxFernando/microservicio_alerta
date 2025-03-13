from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

# Umbrales para alertas
HIGH_THRESHOLD = 180
LOW_THRESHOLD = 70

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    glucose_level = data['glucose_level']
    alert_message = ""

    if glucose_level > HIGH_THRESHOLD:
        alert_message = "¡Alerta! Nivel de glucosa demasiado alto."
    elif glucose_level < LOW_THRESHOLD:
        alert_message = "¡Alerta! Nivel de glucosa demasiado bajo."

    if alert_message:
        return jsonify({"alert": alert_message, "glucose_level": glucose_level}), 200
    else:
        return jsonify({"message": "Nivel de glucosa dentro de los límites."}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
