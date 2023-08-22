fecha = input("ingrese la fecha en el siguiente formato dia, dd/mm ")
dia_semana = fecha[ 0 : fecha.find(",")]
dia_fecha = int(fecha[ fecha.find(" ") : fecha.find("/")])
mes_fecha = int(fecha [ fecha.find("/")+1:])
dia_semana = dia_semana.lower()

if dia_semana != ("lunes" or "martes" or "miercoles" or "jueves" or "viernes" or "sabado" or "domingo"):
    print("dia de la semana incorrecto, reinicie el programa")
else:
    if dia_fecha > 31 :
        print("fecha incorrecta, reinicie el programa")
    else:
        if dia_fecha > 31 :
            print("fecha incorrecta, reinicie el programa")