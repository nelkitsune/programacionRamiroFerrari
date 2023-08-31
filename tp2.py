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
letra.upper()
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

ingrediente_pizza = input("desea su pizza con Pimiento, tofu, peperoni, jamon y/o salmon:  ")
ingrediente_pizza= ingrediente_pizza.lower()
if ingrediente_pizza == "pimiento" or ingrediente_pizza == "tofu":
    print("la pizza es vegetariana")
elif ingrediente_pizza== "peperoni" or ingrediente_pizza== "jamon" or ingrediente_pizza== "salmon" :
    print("la pizza no es vegetaria")
else:
    print("hubo un error")

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
#na ni idea

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
horas=int(input("ingrese la cantidad de horas trabajadas: "))
salario_hora = int ( input ("ingrese el salario por hora: "))
if horas > 48 :
    horas_final = 48 - horas
    horas -=horas_final
    salario_final = (salario_hora * horas) + ((salario_hora * horas_final) * 1.10)
else:
    salario_final = salario_hora * horas
print(f"el salario final es de ${salario_final}")

#19
cantidad = int(input("ingrese la cantidad de lapices que quiere comprar: "))
if cantidad >= 1000 :
    print(f"el costo total es de {(cantidad * 60)*1.07}")
else:
    print(f"el costo final es ")

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