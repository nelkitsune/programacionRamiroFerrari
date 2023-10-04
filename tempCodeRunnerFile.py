import tp5Funciones
num_list=[]
while True:
    num3 = int(input("ingrese un numero o ingrese 0 para terminar: "))
    if num3 != 0:
        num_list.append(num3)
    else:
        break
resultA = tp5Funciones.list_max_men(num_list,"a")
resultB = tp5Funciones.list_max_men(num_list,"b")
print(f"el resultado mayor es: {resultA}")
print(f"el resultaod menor es: {resultB}")