from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido a la calculadora en Flask! Usa /sumar, /restar, /multiplicar, /dividir con parámetros a y b."

@app.route('/sumar', methods=['GET'])
def sumar():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'resultado': a + b})

@app.route('/restar', methods=['GET'])
def restar():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'resultado': a - b})

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'resultado': a * b})

@app.route('/dividir', methods=['GET'])
def dividir():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if b == 0:
        return jsonify({'error': 'No se puede dividir por cero'}), 400
    return jsonify({'resultado': a / b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
