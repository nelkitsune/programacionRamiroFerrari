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
print(deposit)