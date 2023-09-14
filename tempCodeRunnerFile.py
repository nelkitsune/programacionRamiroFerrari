savings = float(input("ingrese la meta a la que desea ahorrar: "))
conditional3 = True
total_saved = 0
while conditional3:
    money_deposited = float(input("ingrese la cantidad de dinero que desea ahorrar: "))
    if money_deposited > 0:
        total_saved += money_deposited
    else:
        print("solo numeros positivos")
    if total_saved >= savings:
        print("meta alcansada")
        conditional3 = False