#punto 1 
base = 10
altura = 5
area = base * altura
perimetro = base + altura
print(f"el area es {area} y el perimetro es {perimetro}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#punto 2
catetoA = 3
catetoB = 4
hipotenusa = ((catetoA**2) + (catetoB**2)) **(1/2)
print(int(f"la hipotenusa es = {hipotenusa}"))

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#punto 3
num1 = 10
num2 = 15
print(f"suma = {num1 + num2} resta = {num1 - num2} multiplicacion = {num1 * num2} division = {num1 / num2}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#punto 4
faherenheit = int(input("ingrese la temperatura en faherenheit: "))
celsius = (faherenheit - 32) * 5/9
print(f"la temperatura en celsius es de {celsius}°")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#punto 5
#a
A = input(nombre, "cual es tu juego favorito") 
#rpt a) La variable A no es buena practica. la variable nombre no esta inicialisada y en python se concatena con +
#forma correcta A
nombre = "ramiro"
cancion_favorita = input(nombre + "cual es tu cancion favorita:  ")
#b
precio = input("Precio: ")
total = precio + (precio * 0.1)
#rpt B : lo que esta mal es que no esta especificado el tipo de variable que se ingresa
#forma correcto b
precio = float(input("Precio: "))
total = precio + (precio * 0.1)
#c
edad = int(input("Edad: "))
print(tu edad ed, edad)
#rpt C : aqui lo que esta mal es que esta mal echo es string
#forma correcta c
edad = int(input("Edad: "))
print(f"tu edad es: {edad}")
#d
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad=18)
#rpt d: lo que esta mal aqui es que para concatenar no se usa la , y que se tendria que usar ==
#forma correcta
edad = int(input("Edad: "))
print(f"Veamos si tu edad es 18… {edad == 18}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#6)
num3 = int(input("ingrese el primer numero "))
num4 = int(input("ingrese el segundo numero "))
num5 = int(input("ingrese el tercer numero "))
resultado6 = (num3 + num4 + num5) / 3
print(resultado6)

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#7
minutos_ingre = int(input("ingrese la cantidad de minutos: "))
horas = minutos_ingre // 60
minutos_restantes = (minutos_ingre / 60 - horas) * 60
minutos_restantes = float()
print(f"la cantidad de tiempo es de: {horas} horas y {minutos_restantes} minutos")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#8
sueldo_base= int(input("ingrese su sueldo: "))
venta1= int(input("ingrese el valor de la primera compra "))
venta2= int(input("ingrese el valor de la segunda compra "))
venta3= int(input("ingrese el valor de la tercera compra "))
resultado_ventas_comision= (venta1 * 0.10) + (venta2 * 0.10) + (venta3 * 0.10)
resultado_total= sueldo_base + resultado_ventas_comision
print(f"la cantidad que resivira el vendedor sumando tanto el sueldo base como las dos comiciones es de {resultado_total}$")

#print(100 * 0.10 )

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#9
producto_base = int(input("ingrese el valor del producto: "))
print(f"el valor total del producto con el 15% de descuento es de {producto_base / 1.15}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#10
parcial1=int(input("ingrese la nota del parcial 1: "))
parcial2=int(input("ingrese la nota del parcial 2: "))
parcial3=int(input("ingrese la nota del parcial 3: "))
examen_final=int(input("ingrese la nota del examen final: "))
trabajo_final=int(input("ingrese la nota del trabajo final: "))
promedio_parcial= ((parcial1 + parcial2 + parcial3)/3) * 0.55
examen_final *= 0.30
trabajo_final *= 0.15
#print (examen_final , trabajo_final, promedio_parcial)
nota_final= promedio_parcial + examen_final + trabajo_final
print(nota_final)

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#11
num6=int(input("ingrese el primer numero: "))
num7=int(input("ingrese el segundo numero: "))
resultado_absoluto = (num6-num7)
if resultado_absoluto < 0:
    resultado_absoluto *=-1
print(f"El valor de la distancia que hay entre {num6} y {num7} es de {resultado_absoluto}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#12
num_raiz = int(input("ingrese un numero para saber su raiz cubica y cuadrada: "))
num_raiz_cuadrada = num_raiz **1/2
num_raiz_cubica = num_raiz**1/3
print(f"la raiz cuadrada del numero {num_raiz} es: {num_raiz_cuadrada}")
print(f"la raiz cubica del numero {num_raiz} es: {num_raiz_cubica}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#13
num_correcto = input("ingrese el numero que decea invertir: ")
numero_listado = list(num_correcto)
#print(numero_listado[::-1])
num_invertido = numero_listado[1] + numero_listado [0]
print (num_invertido)

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#14
numA = int(input("ingrese el valor de A: "))
numB = int(input("ingrese el valor de B: "))
auxiliarC = numA
numA = numB
numB = auxiliarC
print(f"la variable A ahora vale {numA} y la variable b ahora vale {numB}")
#no se me ocurre como hacer esto sin una tercera variable como auxiliar

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#15
hora_ciclista = int(input("ingrese a la hora que partio: "))
minuto_ciclista = int(input("ingrese el minuto ne el que partio: "))
segundos_ciclista = int(input("ingrese el segundo en el que partio: "))
segundos_llegadas = int (input("ingrese la cantidad de segundos que le tomo llegar: "))
#60 = 1m      60m = 1h
minutos_t = segundos_llegadas // 60
horas_t = minutos_t // 60
minutos_f = (minutos_t / 60 - horas_t) * 60
segundos_f = (segundos_llegadas / 60 - minutos_t) * 60
minutos_f //= 1
segundos_f //= 1
segundos_f = segundos_ciclista + segundos_f
minutos_f = minuto_ciclista + minutos_f
horas_t = hora_ciclista + horas_t 
if segundos_f > 60 : 
    minutos_f = minutos_f + segundos_f // 60
    segundos_f = (segundos_f / 60) * 60

if minutos_f > 60 : 
    horas_t = horas_t + segundos_f // 60
    minutos_ingre = (minutos_f / 60) * 60

print(f"la hora de llegada fue= {horas_t}/{minutos_f}/{segundos_f}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#16
nombre_1 =  list(input("ingrese su primero nombre: "))
apellido_2 = list(input("ingrese su primer apellido: "))
apellido_3 = list(input("ingrese su segundo apellido: "))
print(F"las iniciales son {nombre_1[0]}, {apellido_2[0]},{apellido_3[0]}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#17
usuario = input("ingrese su nombre de usuario: ")
print(f"ahora estas en la matrix {usuario}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#18
coste = float(input("ingrese el coste de la cena: "))
coste_f = (coste * 1.10)
coste_f = coste_f * 1.062
print(coste_f)  

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#19
#dia = int(input("porfavor ingrese su dia de nacimiento en numeros: "))
#mes = int(input("porfavor ingrese su dia de mes en numeros: "))
#ano = int(input("porfavor ingrese su dia de años en numeros: "))
#print(f"la fecha de nacimiento es: {dia}/{mes}/{ano}")
fecha_a = input("ingrese la fecha de nacimiento con el siguiente formato: dia / mes / año : ")
print(f"la fecha de nacimiento es: {fecha_a}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#20
fecha_completa = input("Ingrese su fecha de nacimiento en formato DDMMAAAA: ")
if len(fecha_completa) == 8:
    # Separar la fecha en día, mes y año.
    dia = int(fecha_completa[:2])
    mes = int(fecha_completa[2:4])
    anio = int(fecha_completa[4:])
    fecha_formateada = f"{dia:02d}/{mes:02d}/{anio}"
    print(f"Fecha de nacimiento: {fecha_formateada}")
else:
    print("Formato de fecha incorrecto. Debe tener 8 caracteres (DDMMAAAA).")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#21
kml = int(input("ingrese la cantidad de KM que puede recorrer su moto por cada litro de combustible: "))
capaciodad = int(input("ingrese cuantos litros puede almacenar su moto: "))
distancia = int(input("ingrese la distancia que debe recorrer: "))
resultado_21 = distancia / (kml * capaciodad)
print(f"la cantidad de tanques que va a nececitar son: {resultado_21}")

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

