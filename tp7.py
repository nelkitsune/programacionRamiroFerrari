import funciones_ordenamineto
#1
list_des_bur = [7, 2, 9, 1, 5, 3, 8, 4, 6]
list_or_bur = funciones_ordenamineto.bubble_sort(list_des_bur)
print(list_or_bur)

#2
list_worl_des_sele = ["rodrigo", "miguel", "avion","auto", "casino", "casa"]
list_worl_or = funciones_ordenamineto.selection_sort(list_worl_des_sele)
print(list_worl_or)

#3
list_dic_book = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1967,
        "editorial": "Sudamericana"
    },
    {
        "titulo": "To Kill a Mockingbird",
        "autor": "Harper Lee",
        "año_publicacion": 1960,
        "editorial": "J.B. Lippincott & Co."
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "año_publicacion": 1949,
        "editorial": "Secker & Warburg"
    },
    {
        "titulo": "El Gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "año_publicacion": 1925,
        "editorial": "Scribner"
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año_publicacion": 1605,
        "editorial": "Francisco de Robles"
    }
]
option = input("a = año, b = autor, c = title, d = publisher:  ").lower()
if option == "a":
    list_book_or = sorted(list_dic_book, key=funciones_ordenamineto.sort_by_year)
    for book in list_book_or:
        print(book)
elif option== "b":
    list_book_or = sorted(list_dic_book, key=funciones_ordenamineto.sort_by_author)
    for book in list_book_or:
        print(book)
elif option== "c":
    list_book_or = sorted(list_dic_book, key=funciones_ordenamineto.sort_by_title)
    for book in list_book_or:
        print(book)
elif option== "d":
    list_book_or = sorted(list_dic_book, key=funciones_ordenamineto.sort_by_publisher)
    for book in list_book_or:
        print(book)

#4
list_worl = []
wol_lis_tam = []
for i in range ( 0, 10, 1):
    world= input("ingrese una palabra:")
    list_worl.append(world)

for wol in list_worl:
    wol_tam= len(wol)
    wol_lis_tam.append(wol_tam)
wol_lis_tam = funciones_ordenamineto.insertion_sort(wol_lis_tam)
print(wol_lis_tam)
#5
list_or_bur = funciones_ordenamineto.bubble_sort_descendente(list_des_bur)
print(list_or_bur)
#6
num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
num_or = funciones_ordenamineto.counting_sort(num)
print(num_or)
#7
import funciones_ordenamineto
list_friki = ["a",2,"t",6,"b",5,"u","o",7,1,45,"r","z"]
list_friki_or = funciones_ordenamineto.or_list_mix(list_friki)
print(list_friki_or)
#8
import funciones_ordenamineto
num2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
num2_or = funciones_ordenamineto.merge_sort(num2)
print(num2_or)