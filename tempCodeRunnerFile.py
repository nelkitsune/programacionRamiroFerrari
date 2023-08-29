horas=int(input("ingrese la cantidad de horas trabajadas: "))
salario_hora = int ( input ("ingrese el salario por hora: "))
if horas > 48 :
    horas_final = 48 - horas
    horas -=horas_final
    salario_final = (salario_hora * horas) + ((salario_hora * horas_final) * 1.10)
else:
    salario_final = salario_hora * horas
print(f"el salario final es de ${salario_final}")