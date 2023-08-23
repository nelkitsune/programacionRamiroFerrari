fecha = input("ingrese la fecha en el siguiente formato dia, dd/mm ")
dia_semana = fecha[ 0 : fecha.find(",")]
dia_fecha = int(fecha[ fecha.find(" ") : fecha.find("/")])
mes_fecha = int(fecha [ fecha.find("/")+1:])
dia_semana_low = dia_semana.lower()
print (dia_semana_low)

if (dia_semana_low != "lunes") and dia_semana_low != "martes" and dia_semana_low != "miercoles" and dia_semana_low != "jueves" and dia_semana_low != "viernes":
    print("dia de la semana incorrecto, reinicie el programa")
else:
    if dia_fecha > 31 :
        print("fecha incorrecta, reinicie el programa")
    else:
        if dia_fecha > 31 :
            print("fecha incorrecta, reinicie el programa")
        else:
            if dia_semana_low == "lunes" or dia_semana_low == "martes" or dia_semana_low == "miercoles":
                hu_examenes = (input("ingrese porfavot si hubo examenes (solo con si o no): "))
                hu_examenes=hu_examenes.lower()
                if hu_examenes == "si":
                    aprobados = int(input("ingrese la cantidad de aprobados: "))
                    desaprobados = int(input("ingrese la cantidad de desaprobados: "))
                    cantidad = aprobados + desaprobados
                    porcen_aprobados =  aprobados * 100 / cantidad
                    porcen_desaprobados = desaprobados * 100 / cantidad
                    print(f"el porcentaje de aprobados es de {porcen_aprobados}% y el de desaprobados es de {porcen_desaprobados}% ")
            elif dia_semana_low == "jueves":
                    porcentaje_asistencia = input("ingrese el porcentaje que asistio a la clase con el siguiente formato numero% :    ")
                    num_porcentaje_asistencia = int(porcentaje_asistencia[ 0 : porcentaje_asistencia.find("%")])
                    if num_porcentaje_asistencia > 50:
                        print("asistio la mayoria")
                    else:
                        print("no asistio la mayoria")
            else:
                if (dia_fecha == 1 and mes_fecha == 1) or (dia_fecha == 1 and mes_fecha ==7):
                    print("se comienza nuevo ciclo")
                    cantidad_alumnos_viajes = int(input("ingrese la cantidad de alumnos: "))
                    cantidad_dinero_alumno = int(input("ingrese la cantidad de dinero que tiene que pagar cada alumno sin el signo $: "))
                    print(f"la cantidad de ingresos totales es de ${cantidad_dinero_alumno * cantidad_alumnos_viajes}")
