#1
num_list_suma=0
poteito = 1
num_list = []
while True:
    condition = float(input("ingrese un numero (o 0 para terminar): "))
    if condition == 0:
        break
    else:
        num_list.append(condition)
#print(num_list)

#2
#este punto fue echo utilizando la lista anterior :p
condition2 = float(input("ingrese un numero mas, si esta en la lista sera eliminado y remplazado: "))
num_list_long = len(num_list)
for i in range(0,num_list_long,1):
    if condition2 == num_list[i]:
        del num_list[i]
        #print (num_list)
        poteito = 0
        break
if poteito == 1:
    print("no a sido posible eliminar")
else:
    print("si a sido posible eliminar")

#3
for i in num_list:
    num_list_suma += i
print(f"la sma de los numero de la lista es {num_list_suma}")

#4
num_list_menor = []
num_menor = float(input("ingrese un numero, se generara una lista con los numeros menores a este que pertenescan a la otra lista: "))
for i in num_list:
    if i < num_menor:
        num_list_menor.append(i)
for i in num_list_menor:
    print(i)

#5
num_list_tuplas_repetidas=[]
num_list_long = len(num_list)
for i in range(0,num_list_long,1) :
    rep = num_list.count(num_list[i])
    if num_list[i] in num_list_tuplas_repetidas:
        continue
    else:
        num_list_tuplas_repetidas.append((num_list[i],rep)) 
print(num_list_tuplas_repetidas)

#6
primary_level = []
secondary_level =[]
while True:
    name = input("ingrese el nombre de pila del alumno de primaria: ").lower()
    if name == "x":
        break
    else:
        primary_level.append(name)
while True:
    name = input("ingrese el nombre de pila del alumno de secundario: ").lower()
    if name == "x":
        break
    else:
        secondary_level.append(name)
"""
date = len(primary_level)
new_list= []
for i in range(0,date,1):
    if primary_level[i]in secondary_level:
        continue
    else:
        new_list.append(primary_level[i])
date = len(secondary_level)
for i in range(0,date,1):
    new_list.append(secondary_level[i])
print(new_list)
"""
list_prim_sec = set(primary_level)
list_prim_sec.update(secondary_level)
print( list_prim_sec)
name_rep = set(primary_level) & set(secondary_level)
print("\nNombres que se repiten entre nivel primario y secundario:")
for name in name_rep:
    print(name)
name_rep_no = set(primary_level) - set(secondary_level)
print("\nNombres de nivel primario que no se repiten en nivel secundario:")
for name in name_rep_no:
    print(name)

#7
character_count = {}
strings_processed = 0
while strings_processed < 50:
    entrada = input("Ingrese un string (o 'x' para salir): ")
    if entrada == 'x':
        break
    for caracter in entrada:
        if caracter in character_count:
            character_count[caracter] += 1
        else:
            character_count[caracter] = 1
    strings_processed += 1
print("\nCantidad total de ocurrencias de cada carácter:")
for caracter, cantidad in character_count.items():
    print(f"'{caracter}': {cantidad}")
#8
goals = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
    [3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
    [4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
    [6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
    [7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

wins = [0] * 10
draws = [0] * 10
losses = [0] * 10
goals_scored = [0] * 10
goals_conceded = [0] * 10

for i in range(10):
    for j in range(10):
        if i != j:
            if goals[i][j] > goals[j][i]:
                wins[i] += 1
            elif goals[i][j] < goals[j][i]:
                losses[i] += 1
            else:
                draws[i] += 1
            goals_scored[i] += goals[i][j]
            goals_conceded[i] += goals[j][i]

goal_difference = [goals_scored[i] - goals_conceded[i] for i in range(10)]
points = [wins[i] * 3 + draws[i] for i in range(10)]

for i in range(10):
    print(f"Equipo {i + 1}: Victorias: {wins[i]}, Empates: {draws[i]}, Derrotas: {losses[i]}, Diferencia de goles: {goal_difference[i]}, Puntos: {points[i]}")
#9
import random
existe_valor = True
value_to_be_searched = "______________"
table = [
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"],
["______________", "______________", "______________", "______________", "______________"]
]
deck_of_cards = [
    "As de Corazones", "2 de Corazones", "3 de Corazones", "4 de Corazones", "5 de Corazones",
    "6 de Corazones", "7 de Corazones", "8 de Corazones", "9 de Corazones", "10 de Corazones",
    "As de Diamantes", "2 de Diamantes", "3 de Diamantes", "4 de Diamantes", "5 de Diamantes",
    "6 de Diamantes", "7 de Diamantes", "8 de Diamantes", "9 de Diamantes", "10 de Diamantes",
    "As de Corazones", "2 de Corazones", "3 de Corazones", "4 de Corazones", "5 de Corazones",
    "6 de Corazones", "7 de Corazones", "8 de Corazones", "9 de Corazones", "10 de Corazones",
    "As de Diamantes", "2 de Diamantes", "3 de Diamantes", "4 de Diamantes", "5 de Diamantes",
    "6 de Diamantes", "7 de Diamantes", "8 de Diamantes", "9 de Diamantes", "10 de Diamantes",
]
random.shuffle(deck_of_cards)
mat_memo=[
    [deck_of_cards[0],deck_of_cards[1],deck_of_cards[2],deck_of_cards[3],deck_of_cards[4]],
    [deck_of_cards[5],deck_of_cards[6],deck_of_cards[7],deck_of_cards[8],deck_of_cards[9]],
    [deck_of_cards[10],deck_of_cards[11],deck_of_cards[12],deck_of_cards[13],deck_of_cards[14]],
    [deck_of_cards[15],deck_of_cards[16],deck_of_cards[17],deck_of_cards[18],deck_of_cards[19]],
    [deck_of_cards[20],deck_of_cards[21],deck_of_cards[22],deck_of_cards[23],deck_of_cards[24]],
    [deck_of_cards[25],deck_of_cards[26],deck_of_cards[27],deck_of_cards[28],deck_of_cards[29]],
    [deck_of_cards[30],deck_of_cards[31],deck_of_cards[32],deck_of_cards[33],deck_of_cards[34]],
    [deck_of_cards[35],deck_of_cards[36],deck_of_cards[37],deck_of_cards[38],deck_of_cards[39]]
]
print (mat_memo)
while existe_valor == True:
    for row in table:
        for elemento in row:
            print(elemento, end='\t')
        print()
    option1 = int (input("ingrese la fila de primera carta que desea ver (esta tabla va de 0 a 4 de columna y de 0 a 7 de fila): "))
    option1b = int (input("ingrese la columna de la primera carta que desea ver (esta tabla va de 0 a 4 de columna y de 0 a 7 de fila): "))
    option2 = int (input("ingrese la fila de segunda carta que desea ver (esta tabla va de 0 a 4 de columna y de 0 a 7 de fila): "))
    option2b = int (input("ingrese la columna de la segunda carta que desea ver (esta tabla va de 0 a 4 de columna y de 0 a 7 de fila): "))
    if (option1 >= 0 and option1 <=7) and (option1b >= 0 and option1b <=4):
        if (option2 >= 0 and option2 <=7) and (option2b >= 0 and option2b <=4):
            if mat_memo[option1][option1b] == mat_memo[option2][option2b]:
                print("las cartas son iguales")
                table [option1][option1b] = mat_memo[option1][option1b]
                table [option2][option2b] = mat_memo[option1][option1b]
            else:
                print("las cartas no son iguales")
        else:
            print("error en el ingreso de datos")
            continue
    else:
        print("error en el ingreso de datos")
        continue
    for i in table:
        for e in i:
            if e == value_to_be_searched:
                existe_valor = True  
                break
            else:
                existe_valor = False
#10
def get_main_diagonal(matrix):
    main_diagonal = []
    for i in range(len(matrix)):
        main_diagonal.append(matrix[i][i])
    return main_diagonal

def get_reverse_diagonal(matrix):
    reverse_diagonal = []
    for i in range(len(matrix)):
        reverse_diagonal.append(matrix[i][len(matrix) - 1 - i])
    return reverse_diagonal

matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal = get_main_diagonal(matriz_cuadrada)
diagonal_inversa = get_reverse_diagonal(matriz_cuadrada)

print("Diagonal Principal:", diagonal_principal)
print("Diagonal Inversa:", diagonal_inversa)
#11

currencies = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Ingrese el nombre de una divisa: ")

if divisa in currencies:
    symbol = currencies[divisa]
    print(f"El símbolo de {divisa} es {symbol}")
else:
    print("La divisa ingresada no está en el diccionario")
