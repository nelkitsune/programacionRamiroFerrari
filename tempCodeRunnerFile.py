fecha = input("ingrese la fecha en el siguiente formato dia, dd/mm ")
dia_semana = fecha[ 0 : fecha.find(",")]
dia_fecha = fecha[ fecha.find(" ") : fecha.find("/")]
mes_fecha = fecha [ fecha.find("/")+1:]
print(dia_semana + "/" + dia_fecha + "/" + mes_fecha)