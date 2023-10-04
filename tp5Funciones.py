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
