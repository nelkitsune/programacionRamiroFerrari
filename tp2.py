#1
antiguedad_compu = int(input("ingrese en anos la antiguedad de la compu: "))
if antiguedad_compu <= 2 :
    print("el computador es nuevo")
else:
    print("la computadora es vieja")
#2
antiguedad_compu = int(input("ingrese en anos la antiguedad de la compu: "))
if antiguedad_compu < 0 :
    print("ocurrio un error, ingrese un numero positivo")
    if antiguedad_compu <= 2 :
        print("el computador es nuevo")
    else:
        print("la computadora es vieja")
#3
nombres = input("ingrese el nombre de dos perosnas separadas por UN espacio y despues del ultimo nombre un .: ")
nombre1 = nombres[0:nombres.find(" ")]
nombre2 = nombres[nombres.find(" ") +1 : nombres.find(".")]
nombre1_lower = nombre1.lower()
nombre2_lower = nombre2.lower()
if nombre1_lower[0] == nombre2_lower[0] :
    print("hay coincidencia")
else:
    print("no hay coincidencia")
#4
print("bienvenido a la votacion")
print("candidato A partido rojo")
print("candidato B partido verde")
print("candidato C partido azul")
voto = input("ingrese la letra que corresponda segun que candidato quiera: ")
voto=voto.upper()
if voto == "A" or voto == "B" or voto == "C":
    if voto == "A":
        print("usted a votado por el partido rojo")
    elif voto == "B":
        print("usted voto por el partido verde")
    else :
        print("usted voto por el partido azul")
else :
    print("Voto incorrecto porfavor reinicie el programa")
#5
letra = input("ingrese UNA letra: ")
letra =letra.upper()
validar = len(letra)
if validar > 1:
    print("ocurrio un error")
else:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" :
        print("la letra es una vocal")
    else:
        print("la letra no es una vocal")
#6
ano_bisiesto = int(input("ingrese un ano: "))
if ano_bisiesto % 4 == 0:
    if ano_bisiesto % 100 == 0:
        if ano_bisiesto % 400 == 0:
            print("el ano es bisiesto")
        else:
            print("el ano no es bisiesto")
    else:
        print("el ano es bisiesto")
else:
    print("el ano no es bisiesto")
#7
num1=int(input("inrese el primer numero"))
num2=int(input("inrese el segundo numero"))
num3=int(input("inrese el tercer numero"))
if num1 < num2 and num1 < num3:
    print(f"el numero menor es el {num1}")
elif num2 < num1 and num2 < num3:
    print(f"el numero menor es el {num2}")
elif num3 < num1 and num3 < num2 :
    print(f"el numero menor es el numero {num3}")
else:
    print("los 3 numeros son iguales")
#8

usuario1 = input("ingrese el usuario: ")
contraseña1 = input("ingrese la contraseña: ")
if usuario1 == "Gwenevere" and contraseña1 == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#9
nombre_curso = input("ingrese su nombre: ")
genero = input("ingrese su genero (h o m): ")

if genero == "m" :
    if nombre_curso[0]  <= "m":
        print("perteneces al grupo a")
    else:
        print("preteneces al grupo b")
elif genero == "h":
    if nombre_curso[0]  <= "n":
        print("perteneces al grupo a")
    else:
        print("preteneces al grupo b")
else:
    print ("error")

#10
edad_u = int(input("ingrese su edad "))

if edad_u < 4 :
    print("no debe pagar nada ")
elif edad_u >= 4 and edad_u < 18 :
    print("debe pagar 500 pesos")
else:
    print("debe pagar 1000 pesos")

#11
opcion_pizza = input("desea una pizza vegetariana(a) o una pizza no vegetariana(b): ")
opcion_pizza = opcion_pizza.lower()
if opcion_pizza == "a":
    opcion_pizza_ele = "vegetariana"
    opcion_ingrediente = input("ingrese uno de los siguientes ingredientes: tofu(a), pimiento(b).: ")
    opcion_ingrediente = opcion_ingrediente.lower()
    if opcion_ingrediente == "a":
        ingrediente = "tofu"
    elif opcion_ingrediente == "b":
        ingrediente = "pimiento"
    else:
        print("ocurrio un error")
elif opcion_pizza == "b":
    opcion_pizza_ele = "no vegetariana"
    opcion_ingrediente = input("ingrese uno de los siguientes ingredientes: Peperoni(a), Jamó(b), Salmón(C).: ")
    opcion_ingrediente = opcion_ingrediente.lower()
    if opcion_ingrediente == "a":
        ingrediente = "peperoni"
    elif opcion_ingrediente == "b":
        ingrediente = "jamon"
    elif opcion_ingrediente == "c":
        ingrediente = "salmon"
    else:
        print("ocurrio un error")
print(f"la pizza es {opcion_pizza_ele} y tiene {ingrediente}, queso y salsa")
"""
ingrediente_pizza = input("desea su pizza con Pimiento, tofu, peperoni, jamon y/o salmon:  ")
ingrediente_pizza= ingrediente_pizza.lower()
if ingrediente_pizza == "pimiento" or ingrediente_pizza == "tofu":
    print("la pizza es vegetariana")
elif ingrediente_pizza== "peperoni" or ingrediente_pizza== "jamon" or ingrediente_pizza== "salmon" :
    print("la pizza no es vegetaria")
else:
    print("hubo un error")
"""
#12
ano_actual = int(input("ingrese al año actual: "))
ano_ingresado = int(input("ingrese un año para averiguar cuanto falta o cuanto paso"))
if ano_actual < ano_ingresado :
    print(f" Los años que faltan son {ano_ingresado - ano_actual}")
elif ano_actual > ano_ingresado:
    (f" Los años que faltan son {ano_actual - ano_ingresado}")
elif ano_actual == ano_ingresado:
    print("son los mismos años")
else:
    print("error")

#13
num4=int(input("ingrese un numero: "))
num5=int(input("ingrese otro numero: "))
if num4 > num5:
    if num4 % num5 == 0:
        print("el numero mayor es multiplo del menor")
    else:
        print("el numero mayor no es multiplo dle menor")
elif num5 > num4:
    if num5 % num4 == 0:
        print("el numero mayor es multiplo del menor")
    else:
        print("el numero mayor no es multiplo dle menor")
elif num4 < 0 or num5 < 0:
    print("no se puede ingresar numeros negativos")
else:
    print("no se puede inngresar valores nulos")

#14
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones (todos los números son solución).")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación {a}x + {b} = 0 es x = {x:.2f}")

#15
pregunta = input("ingrese t si quieres saber le area de un triangulo o ingrese c para saber el area de un circulo: ")
pregunta = pregunta.lower()
if pregunta == "t":
    triangulo_base = int(input("ingrese la base del triangulo: "))
    triangulo_altura = int(input("ingrese la altura del triangulo: "))
    triangulo_area = (triangulo_altura * triangulo_base) / 2
    print(f"el area de un triangulo es {triangulo_area}")
elif pregunta == "c":
    circulo_radio = int(input("ingrese el radio del circulo: "))
    circulo_area = 3.14*circulo_radio^2
    print(f"el area de un circulo es {circulo_area}")
else:
    print("error")

#16

numa = int(input("ingrese el numero a: "))
numb = int(input("ingrese el numero b: "))
opcion = int(input("ingrese 1 para la suma, 2 para la multiplicacion, 3 para la resta y 4 para la diivision: "))
if opcion == 1 :
    print(f"el resultado es {numa + numb}")
elif opcion == 2 :
    print(f"el resultado es {numa * numb}")
elif opcion == 3 :
    print(f"el resultado es {numa - numb}")
elif opcion == 4 :
    if numb == 0:
        print("No se puede dividir entre cero")
    else: 
        print(f"el resultado es {numa / numb}")

#17
dia = input("ingrese un dia: ")
dia = dia.lower()
if dia == "lunes":
    print("hoy es lunes")
elif dia == "viernes":
    print("hoy es viernes")
elif dia == "sabado" or dia =="domingo":
    print("hoy es fin de semana")
elif dia == "martes" or dia =="miercoles" or dia == "jueves":
    print("otro mensaje")
else:
    print("error")

#18
horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))
jornada_minima = 48
if horas_trabajadas > jornada_minima:
    horas_extras = horas_trabajadas - jornada_minima
    salario_total = (jornada_minima * salario_por_hora) + (horas_extras * salario_por_hora * 1.1)
else:
    horas_extras = 0
    salario_total = horas_trabajadas * salario_por_hora
print(f"Horas extras trabajadas: {horas_extras:.2f} horas")
print(f"Salario total: ${salario_total:.2f}")

#19

cantidad_lapices = int(input("Ingrese la cantidad de lápices a comprar: "))
costo_por_lapiz = 60
costo_total = cantidad_lapices * costo_por_lapiz
if cantidad_lapices >= 1000:
    descuento = 0.07 * costo_total
    costo_total_con_descuento = costo_total - descuento
    print(f"Costo total con descuento (7%): ${costo_total_con_descuento:.2f}")
else:
    print(f"Costo total sin descuento: ${costo_total:.2f}")
#20

nota_a = int(input("ingrese la primera nota: "))
nota_b = int(input("ingrese la segunda nota: "))
nota_c = int(input("ingrese la tercera nota: "))
nota_d = int(input("ingrese la cuarta nota: "))
nota_promedio = (nota_a + nota_b + nota_c + nota_d)/4
if nota_promedio >= 6:
    print("aprobo")
else:
    print("desaprobo")