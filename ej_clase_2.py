# ejercicio 1
cantidad = int(input("ingresela cantidad de lugares que se movera: "))
for i in range(5):
    num_auxiliar = ""
    str_auxiliar = ""
    men_cod = ""
    cantidad_aux = ""
    men = input("ingrese el mensaje que desea mandar: ")
    abcd = "abcdefghijklmnñopqrstuvwxyz"
    long = len(men)
    list_men = list(men)

    for n in range(long):
        num_auxiliar = abcd.find(list_men[n])
        if list_men[n] in abcd:
            num_auxiliar += cantidad
            if num_auxiliar > 26:
                cantidad_aux = num_auxiliar - 26
                num_auxiliar = 0
                num_auxiliar += cantidad_aux
            str_auxiliar = abcd[num_auxiliar]
            list_men[n] = str_auxiliar
    for c in range(long):
        men_cod += list_men[c]
    print(men_cod)

# ejercicio 2
contador_auxiliar_pares = 0
contador_auxiliar_impares=0
num = 1
contador_pares = 0
contador_inpares = 0
auxiliar = ""
contador = 0
list_temporal = ""
while num != 0:
    contador_auxiliar_pares = 0
    contador_auxiliar_impares=0
    contador = 0
    num = int(input("ingrese un numero para averiguar la cantidad de pares o impares y/o ponga un 0 para finalizar la ejecucion: "))
    if num == 0:
        print("fin de la ejecucion")
    elif num > 9 or num < (-9):
        auxiliar = num
        while auxiliar > 0:
            contador = (auxiliar % 10)
            auxiliar = auxiliar // 10
            if contador % 2 == 0:
                print("el numero es par")
                contador_pares += 1
                contador_auxiliar_pares += 1 
            else:
                print("el numero es inpar")
                contador_inpares += 1
                contador_auxiliar_impares += 1
    else:
        if num % 2 == 0:
            print("el numero es par")
            contador_pares += 1
            contador_auxiliar_pares += 1 
        else:
            print("el numero es inpar")
            contador_inpares += 1
            contador_auxiliar_impares += 1
    print(f"la cantidad de pares que ingreso es {contador_auxiliar_pares} y la cantidad de impares es de {contador_auxiliar_impares}")
print(f"la cantidad de digitos pares fue de {contador_pares} y de inpares fue de {contador_inpares}")
