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