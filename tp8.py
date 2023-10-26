import tp8_funciones
#1
print(tp8_funciones.count_digit_recursivo(12345))

#2
print(tp8_funciones.potencia(16, 2))
#3
a = "abracadabra"
b = "a"
ocurrencias = tp8_funciones.conception(a, b)
print(ocurrencias)
#4

print(tp8_funciones.Odd(5))  
print(tp8_funciones.Odd(6))  
print(tp8_funciones.Odd(8)) 
#5
lis = [3, 7, 2, 9, 5, 8, 1]
may= tp8_funciones.find_largest(lis)
print("El mayor elemento de la lista es:", may) 

#6
original_list = [1, 3, 3, 7]
n = 2
replicated_list = tp8_funciones.replicate(original_list, n)
print(replicated_list)
#7
n = int(input("Ingrese un número n: "))
p = int(input("Ingrese un número p: "))
print("El valor de K(n, p) es:", tp8_funciones.K(n, p))
#8
n = int(input("Ingrese un número n: "))
k = int(input("Ingrese un número k: "))
resultado = tp8_funciones.pascal(n, k)
print(f"El valor del elemento en la fila {n} y la columna {k} es: {resultado}")
#9

list = ["a", "b", "c"]
k = 3
tp8_funciones.combinaciones(list, k)

#10
N = int(input("Ingrese un número N: "))
ancho, largo = tp8_funciones.medidas_hoja_A(N)
print(f"El ancho de la hoja A{N} es {ancho} mm")
print(f"El largo de la hoja A{N} es {largo} mm")