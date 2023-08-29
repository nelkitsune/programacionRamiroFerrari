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
    print("numero 1 es el nume")