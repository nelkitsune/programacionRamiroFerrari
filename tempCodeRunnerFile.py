fibonacci_1 = 0
fibonacci_2 = 1
print("Los primeros 10 números de la sucesión de Fibonacci son:")
count = 0
while count < 10:
    print(fibonacci_1)
    fibonacci_temp = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_temp
    count += 1