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
aux = 0
while True:
    option = (input("ingrese D para depositar R para retirar. Para finalizar deje el campo vacio: ").upper())
    if option == "D":
        while True:
            entered = float(input("ingrese la cantidad que desea meter: $"))
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
        while True:
            if deposit <= 0:
                print("no tienes dinero para retirar.... volviendo al menu")
                break
            else:
                remove = float(input("Ingrese cual es la cantidad que desea retirar: $"))
                if remove <= deposit and remove > 0:
                    print(f"retirarndo {remove} de su cuenta")
                    deposit -= remove
                    print(f"le queda en el deposito un total de ${deposit}")
                elif remove > deposit :
                    print("quiere retirar mas dinero del que tienes en tu cuenta. ingrese un numero menor")
                    continue
                else:
                    print("error. debe ingresar unn numero positivo y mayor a 0. volviendo al menu")
                    break
    elif option == "":
        print(f"la cantidad de dinero en su cuenta es de {deposit}")
        break
    else:
        print("opcion ingresada incorrecta. intentelo otra ves")
        
        
#4

prime_counter = 0
while True:
    num1 = int(input("Ingrese un número mayor que 1 (o 0 para finalizar): "))
    if num1 == 1 or num1 < 0:
        print("nu puede ingresar 1 o numeros menores a 0")
        continue
    if num1 == 0 :
        break
    if num1 > 1:
        cousin = True
        for i in range(2, int(num1 ** 0.5) + 1):
            if num1 % i == 0:
                cousin = False
                break
        if cousin:
            prime_counter += 1
print(f"La cantidad total de números primos ingresados es: {prime_counter}")

#5

year_inicio = int(input("Ingrese el año de inicio: "))
year_fin = int(input("Ingrese el año de fin: "))
encontrado = False
print(f"Años bisiestos y múltiplos de 10 en el rango {year_inicio}-{year_fin}:")
for year in range(year_inicio, year_fin + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if year % 10 == 0:
            print(year)
            encontrado = True
if encontrado == False:
    print("No se encontraron años bisiestos en el rango especificado.")
#6
for num2 in range(1, 21):
    if num2 % 2 != 0:
        continue
    print(num2)
#7
numbers = [10, 20, 30, 40, 50]
target = 30
for number in numbers:
    if number == target:
        print("Número encontrado:", number)
        break
#8
while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Ha elegido la Opción 1.")
    elif opcion == "2":
        print("Ha elegido la Opción 2.")
    elif opcion == "3":
        print("Ha elegido la Opción 3.")
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")