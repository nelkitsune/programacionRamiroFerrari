#Ramiro Ferrari comicion 3
#inicio del codigo y inicio de variables de apoyo
name =  input("ingrese su nombre: ")
cont =0
odd_number = 0
#inicio del bucle while principal
while True:
    number_max=0
    #menu 
    print(f"bienvenido {name} seleccione el juego que decea jugar")
    print("opcion A: Juego de numeros")
    print("opcion B: juego de palabras")
    print("opcion C: salir")
    option= input(f"{name} Escriba la opcion a continuacion: ").upper()
    #verificacion del menu
    if option == "A": #juego de los numeros
        while True:
            #ingreso de datos del juego de numeros
            number = float(input(f"{name} ingrese un numero enteros: "))
            #verificacion si el numero ingresado es un 0, par o impar
            if number == 0 :
                #caso de que sea 0
                break
            elif number %2 == 0:
                #caso de que sea par
                if number_max == 0:
                    number_max = number
                elif number_max < number:
                    number_max = number
            elif number %2 != 0:
                #caso de que sea impar
                odd_number +=number
                cont +=1
                result = odd_number/cont
        #inprimimos los resultados
        print(f"{name} El mayor numero par ingresado es = {number_max} y el promedio de los numero impares es = {result}")
    if option == "B": #juego de la palabra
        while True:
            sentence = input("Ingrese una palabra: ") #ingreso de la palabra
            if sentence == "":#comprobacion si puso o no una palbra
                print(f"{name} tiene que ingresar una palabra: ")
                continue
            else:
                #inicio de las variaables contadoras
                a_count = 0
                e_count = 0
                i_count = 0
                o_count = 0
                u_count = 0
                for letter in sentence: #bucle para buscar y contar vocales
                    letter = letter.lower()
                    if letter == 'a':
                        a_count += 1
                    elif letter == 'e':
                        e_count += 1
                    elif letter == 'i':
                        i_count += 1
                    elif letter == 'o':
                        o_count += 1
                    elif letter == 'u':
                        u_count += 1
                    #inprimimos los resultados
                print(f"{name} La cantidad de 'a': {a_count}")
                print(f"{name} La cantidad de 'e': {e_count}")
                print(f"{name} La cantidad de 'i': {i_count}")
                print(f"{name} La cantidad de 'o': {o_count}")
                print(f"{name} La cantidad de 'u': {u_count}")
                break
    if option == "C":#opcion de salida del codigo
        print(f"Gracias {name} por jugar con nosotros")
        break
    else:#caso de que la letra ingresada no sea la correcta
        print(f"{name} Opcion incorrecta, reitentelo otra ves")

