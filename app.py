import tkinter as tk
from tkinter import messagebox

def calcular():
    operacion = operacion_var.get()
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operacion == "sumar":
            resultado.set(num1 + num2)
        elif operacion == "restar":
            resultado.set(num1 - num2)
        elif operacion == "multiplicar":
            resultado.set(num1 * num2)
        elif operacion == "dividir":
            resultado.set(num1 / num2 if num2 != 0 else "Error: División por cero")
        else:
            messagebox.showerror("Error", "Operación no válida")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

# Configuración de la ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x250")

# Variables
operacion_var = tk.StringVar()
resultado = tk.StringVar()

# Widgets
tk.Label(root, text="Número 1:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Número 2:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

tk.Label(root, text="Operación:").pack()
operaciones = ["sumar", "restar", "multiplicar", "dividir"]
tk.OptionMenu(root, operacion_var, *operaciones).pack()

tk.Button(root, text="Calcular", command=calcular).pack()

tk.Label(root, text="Resultado:").pack()
tk.Entry(root, textvariable=resultado, state='readonly').pack()

# Ejecutar
root.mainloop()

