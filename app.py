from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido a la calculadora en Flask!"

@app.route('/sumar', methods=['GET'])
def sumar():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({'resultado': num1 + num2})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

@app.route('/restar', methods=['GET'])
def restar():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({'resultado': num1 - num2})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)