import funciones_calculadora_ramdon

while True:
    print("Ingresa una expresión matemática o 'salir' para terminar el programa")
    expresion = input(": ")
    if expresion == "salir":
        break

    resultado = funciones_calculadora_ramdon.calcular(expresion)
    print("Resultado:", resultado)

