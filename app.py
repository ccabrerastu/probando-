from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Calculadora Flask</h2>
        <form action="/calcular" method="get">
            <input type="number" name="a" placeholder="Número 1" required>
            <input type="number" name="b" placeholder="Número 2" required>
            <select name="operacion">
                <option value="sumar">Sumar</option>
                <option value="restar">Restar</option>
                <option value="multiplicar">Multiplicar</option>
                <option value="dividir">Dividir</option>
            </select>
            <button type="submit">Calcular</button>
        </form>
    '''

@app.route('/calcular')
def calcular():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    operacion = request.args.get('operacion')

    if operacion == "sumar":
        resultado = a + b
    elif operacion == "restar":
        resultado = a - b
    elif operacion == "multiplicar":
        resultado = a * b
    elif operacion == "dividir":
        if b == 0:
            return "Error: No se puede dividir por 0"
        resultado = a / b
    else:
        return "Operación no válida"

    return f"Resultado: {resultado}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
