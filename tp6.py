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