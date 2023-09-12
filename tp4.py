#1
varx = 0
while varx <=30:
    varx += 1
    if varx == 4 or varx == 6 or varx == 10:
        print(f"Se ha saltado el valor {varx}")
        continue
    print(f"El valor del bucle es: {varx}")
    if varx == 15:
        print(f"se a interrumpido el bucle cuando el valor de x era {varx}")
        break
#2
text_line_list=[]
while True:
    text_line = input("ingrese una linea (dejar en blanco para finalizar): ")
    if text_line =="":
        break
    text_line_list.append(text_line)

print("\nLineas en mayusculas")
for text_line in text_line_list:
    print(text_line.upper())


#3
print("bienvenido a su cuenta de banco.")
deposit = 0
while True:
    option = (input("ingrese D para depositar R para retirar. Para finalizar deje el campo vacio: ").upper())
    if option == "D":
        while True:
            entered = int(input("ingrese la cantidad que desea meter: $"))
            if entered <= 0:
                print("Ingrese un valor mayor a 0 ")
                continue
            else:
                deposit += entered 
            option_deposit = input("ingrese A para seguir en deposito o B para volver al menu: ").upper()
            if option_deposit == "A":
                continue
            elif option_deposit == "B":
                print("volviendo al menu")
                break
            else:
                print("opcion incorrecta, volviendo al menu")
                break
    elif option == "R":
        print("b")
    elif option == "":
        print("c")
        break
    else:
        print("opcion ingresada incorrecta")