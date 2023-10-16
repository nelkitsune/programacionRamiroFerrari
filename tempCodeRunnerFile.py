
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Encuentra el elemento mínimo en el resto de la lista
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambia el elemento mínimo con el primer elemento no ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12, 22, 11, 90]
selection_sort(mi_lista)
print("Lista ordenada:")
print(mi_lista)
