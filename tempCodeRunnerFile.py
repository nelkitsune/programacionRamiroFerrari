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