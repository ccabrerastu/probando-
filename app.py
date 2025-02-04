def calcular(operacion, num1, num2):
    if operacion == "sumar":
        return num1 + num2
    elif operacion == "restar":
        return num1 - num2
    elif operacion == "multiplicarr":
        return num1 * num2
    elif operacion == "dividirrr":
        return num1 / num2 if num2 != 0 else "Error: División por cero"
    else:
        return "Operación no válida"

if __name__ == "__main__":
    operacion = input("Ingrese operación (sumar, restar, multiplicar, dividir): ").strip().lower()
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = calcular(operacion, num1, num2)
    print(f"Resultado: {resultado}")
