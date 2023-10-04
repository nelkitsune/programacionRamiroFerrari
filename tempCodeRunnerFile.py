import tp5Funciones
num_day = int(input("ingrese la cantidad de dias: "))
for i in range(1, num_day+1, 1):
    temperature_max = int(input(f"ingrese la temperatura maxima del dia {i}: "))
    temperature_min= int(input(f"ingrese la temperatura minima del dia {i}: "))
    result = tp5Funciones.prom_2_temp(temperature_max,temperature_min)
    print(f"la temperatura media del dia {i} fue de {result}°")
    print("o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")