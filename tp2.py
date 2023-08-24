#1
antiguedad_compu = int(input("ingrese en aos la antiguedad de la compu: "))
if antiguedad_compu <= 2 :
    print("el computador es nuevo")
else:
    print("la computadora es vieja")
#2
antiguedad_compu = int(input("ingrese en aos la antiguedad de la compu: "))
if antiguedad_compu < 0 :
    print("ocurrio un error, ingrese un numero positivo")
    if antiguedad_compu <= 2 :
        print("el computador es nuevo")
    else:
        print("la computadora es vieja")
#3
nombres = input("ingrese el nombre de dos perosnas separadas por UN espacio y despues del ultimo nombre un .: ")
nombre1 = nombres[0:nombres.find(" ")]
nombre2 = nombres[nombres.find(" ") +1 : (".")]
if nombre1[0] == nombre2[0] :
    print("hay coincidencia")
else:
    print("no hay coincidencia")
#4
