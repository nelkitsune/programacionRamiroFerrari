conditional7 = 1
total=0
while conditional7 > 0:
    conditional7 = int(input("ingrese el valor del producto: "))
    if conditional7 > 0:
        total += conditional7
    elif conditional7 < 0:
        print("error ingrese de nuevo el numero")
    elif conditional7 == 0:
        break
if total >= 1000:
    print(f"felicidades obtuvo un descuento e 10%. el total de la compra es: ${total-(total*0.10)}")
print("fin de la ejecucion")