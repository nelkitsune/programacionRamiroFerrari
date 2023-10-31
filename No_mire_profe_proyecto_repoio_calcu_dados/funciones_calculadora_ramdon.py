import random 
def calcular(expresion):
    try:
        resultado = eval(expresion)
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero"
    except Exception as e:
        return "Error: " + str(e)