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