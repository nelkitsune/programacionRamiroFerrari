import tp5Funciones
#1

dni = input("ingrese su numero de documneto: ")
resultado = tp5Funciones.tamanioDni(dni)
print(resultado)

#2
import tp5Funciones
word = input("ingrese un string: ")
word_log = tp5Funciones.size_string(word)
print(word_log)
#3
import tp5Funciones
while True:
    option = input("ingrese A para ingresar un socio, B para salir: ").upper()
    if option == "A":
        name = input("ingrese su nombre ccompleto separado por espacios: ")
        dni = input("ingrese su dni: ")
        condition = tp5Funciones.tamanioDni(dni)
        if condition == True:
            date_list=tp5Funciones.partner(name,dni)
            print (f"nombre: {date_list[0]}")
            print (f"dni: {date_list[1]}")
            print (f"id: {date_list[2]}")
        else:
            print("error vuelva a ingresar los datos")
            continue
    elif option == "B":
        break
    else:
        print("opcion ingresada incorrecta, cerrando el programa por seguridad")
        break

#4
import tp5Funciones
num1 = int(input("ingrese un numero entero: "))
num2= int(input("ingrese otro numero entero: "))
tp5Funciones.num_mult(num1,num2)

#5
import tp5Funciones
num_day = int(input("ingrese la cantidad de dias: "))
for i in range(1, num_day+1, 1):
    temperature_max = int(input(f"ingrese la temperatura maxima del dia {i}: "))
    temperature_min= int(input(f"ingrese la temperatura minima del dia {i}: "))
    result = tp5Funciones.prom_2_temp(temperature_max,temperature_min)
    print(f"la temperatura media del dia {i} fue de {result}°")
    print("o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
    

#6
#orueba="Hola, tú" 
#orueba_list = []
#resultS=""
#for letra in orueba:
#    orueba_list.append(letra)
#    print("a")
#long_orueba_list= len(orueba_list)
#for i in range(0,long_orueba_list,1):
#    print("b")
#    resultS += orueba_list[i]+" "
#print(resultS)
import tp5Funciones
word2 = input("ingrese una cadena: ")
print(tp5Funciones.espacios_word(word2))

#7
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

#8
radius = float(input("Ingrese el radio de la circunferencia: "))
area, perimeter = calculate_circle_area_perimeter(radius)
print(f"Área de la circunferencia: {area}")
print(f"Perímetro de la circunferencia: {perimeter}")
#9
import tp5Funciones
attempts = 0
condition2 = True
while condition2== True:
    if attempts > 3:
        print("numero de intentos alcanzados, intentelo mas tarde")
        break
    if attempts != 0:
        print(f"le quedan {3-attempts} intento/s ")
    login = input("ingrese su usuario: ")
    pasword = input("ingrese su contrasenia: ")
    attempts , condition2 = tp5Funciones.login(login,pasword,attempts,condition2)

#10
import tp5Funciones
shopping_cart = {
    "producto1": {"precio": 100, "descuento": 10}, "producto2": {"precio": 50, "descuento": 5}, "producto3": {"precio": 200, "descuento": 15}}
precio_total = tp5Funciones.dicount_cart(shopping_cart)
print(f"Precio total con descuentos: {precio_total}")
#11
import tp5Funciones
numeros = [1, 2, 3, 4, 5]
resultados = tp5Funciones.punto11(tp5Funciones.punto11_2, numeros)
print(resultados)

#12
import tp5Funciones

word3 = input("ingrese una frase: ")
word3_dic=tp5Funciones.frase(word3)
print(word3_dic)

#13
import tp5Funciones
vector = [3, 4]
modulo = tp5Funciones.vectors(vector)
print(f"El módulo del vector {vector} es {modulo}")

#14
import tp5Funciones

numero = int(input("Ingrese un número entero: "))
if tp5Funciones.prim(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

#15
import tp5Funciones
tp5Funciones.main()

#16
import tp5Funciones
tp5Funciones.main2()

#17
import tp5Funciones
tp5Funciones.main3()
