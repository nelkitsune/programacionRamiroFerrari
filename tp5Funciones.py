import math

def tamanioDni (num_dni):
    tamanioD = len(num_dni)
    if tamanioD >= 7 and tamanioD <=8:
        return  True
    else:
        return False

def size_string (wordd):
    wordd = wordd.strip();wordd = wordd.strip(" ");wordd = wordd.strip(".")
    worddlist=wordd.split()
    wordd_long = worddlist[-1]
    return len(wordd_long)

def partner (name,dni):
    name_div = name.split()
    name_fin = name_div[0]
    for i in range(0,3):
        name_fin = name_fin + dni[i]
    date_list = [name_div[0],dni,name_fin]
    return date_list

def num_mult (num1,num2):
    if num2 % num1 == 0 :
        print("el primer numero si es multiplo del segundo: ")
    else:
        print("el primer numero no es multiplo del segundo: ")

def prom_2_temp (num1,num2):
    return (num1 + num2) / 2

def espacios_word (word2):
    word2_list = []
    resultS=""
    for letra in word2:
        word2_list.append(letra)
    long_word2_list= len(word2_list)
    for i in range(0,long_word2_list,1):
        resultS += word2_list[i]+" "
    return  resultS

def list_max_men (list_num, option):
    cant = len(list_num)
    if option == "a":
        result = -10000000000000000000000000000000000
        for i in range(0,cant, 1):
            if list_num[i] > result:
                result = list_num[i]
    if option == "b":
        result = 10000000000000000000000000000000000000
        for i in range(0,cant , 1):
            if list_num[i] < result:
                result = list_num[i]
    return result

def calculate_circle_area_perimeter(radius):
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def login(logi,pasword, attems, condition):
    login_or = "usuario1"
    pasword_or = "asdasd"
    if logi == login_or and pasword == pasword_or:
        condition = False
        print("usuario y contraseña correctos")
        return condition, attems
    else:
        print("usuario o contrasenia incorrecto/s, intente otra ves")
        return attems+1 , condition 

def dicount_cart(cart):
    price_f = 0
    for producto, info in cart.items():
        price = info["precio"]
        discount = info["descuento"]
        price_d = price - (price * discount / 100)
        price_f += price_d
    return price_f

def punto11(funcion, lista):
    resultado = [funcion(elemento) for elemento in lista]
    
    return resultado
def punto11_2(numero):
    return numero ** 2

def frase (word):
    word_dic ={}
    word_list = word.split()
    number = len(word_list)
    for i in range(0,number,1):
        auxiliari = word_list[i]
        number_word = len(auxiliari)
        word_dic[auxiliari] = {number_word} 
    return word_dic

def vectors(vector):
    sum_square = sum(component ** 2 for component in vector)
    modulo = math.sqrt(sum_square)
    return modulo

def prim(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial
def main():
    total_count = 0
    
    while True:
        try:
            number = int(input("Ingrese un número (o -1 para terminar): "))
            
            if number == -1:
                break
            
            factorial = calculate_factorial(number)
            print(f"El factorial de {number} es {factorial}")
            
            total_count += 1
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    print(f"Cantidad total de números leídos: {total_count}")

def calculate_frequency(number, digit):
    frequency = 0
    while number > 0:
        current_digit = number % 10
        if current_digit == digit:
            frequency += 1
        number //= 10
    return frequency
def main2():
    number = input("Ingrese un número entero: ")
    digit = input("Ingrese un dígito: ")

    if number.isdigit() and digit.isdigit():
        number = int(number)
        digit = int(digit)

        if 0 <= digit <= 9:
            frequency = calculate_frequency(number, digit)
            print(f"El dígito {digit} aparece {frequency} veces en el número {number}.")
        else:
            print("Ingrese un dígito válido (0-9).")
    else:
        print("Debe ingresar números enteros válidos.")


def main3():
    highest_number = 0
    while True:
        try:
            number = int(input("Ingrese un número primo (o un número no primo para finalizar): "))
            if number <= 0:
                print("Debe ingresar un número entero positivo.")
                continue
            if not is_prime(number):
                break
            digit_sum = sum(int(digit) for digit in str(number))
            print(f"La suma de los dígitos de {number} es {digit_sum}")
            digit = int(input("Ingrese un dígito para contar su frecuencia: "))
            if 0 <= digit <= 9:
                frequency = str(number).count(str(digit))
                print(f"El dígito {digit} aparece {frequency} veces en {number}")
            if number > highest_number:
                highest_number = number
        except ValueError:
            print("Debe ingresar un número entero válido.")
    if highest_number > 0:
        factorial_highest = calculate_factorial2(highest_number)
        print(f"El factorial del mayor número ingresado ({highest_number}) es {factorial_highest}")

def calculate_factorial2(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
