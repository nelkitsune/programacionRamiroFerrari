#1)
name = input("ingrese el nombre: ")
for i in range(10):
    print(name)

#2)

age = int(input("ingrese su edad: "))
for i in range(age):
    print(i+1)

#3)
aux =""
num1 = int(input("ingrese un numero"))
for i in range(num1):
    if  i % 2 != 0:
        aux2= str(i)
        aux = str (aux +", " + aux2)

print(aux)

#4)
auxiliary2=""
num2 = int(input("ingrese un numeor entero positivo: "))
for i in range(num2, 0 , -1):
    auxiliary3 = str(i)
    auxiliary2 = str(auxiliary2 + ", " + auxiliary3)
print(auxiliary2)

#5)
money = float(input("ingrese la cantidad que desea invertir: "))
interest = float (input ("ingrese el interes anual: "))
years = int (input("ingrese la cantidad de años: "))
interest = interest / 100
for i in range (1, years + 1):
    capital_obtained = money * (1 + interest)
    print(f"el capital obtenido en el año {i} es de ${capital_obtained}")
    money = capital_obtained

#6)
auxiliary4 = "*"
num3 = int(input("ingrese un numero para hacer un triangulito: "))
for i in range(1,num3 + 1):
    triangle=""
    for j in range(1,i +1):
        triangle += auxiliary4
    print(triangle)

#7)
for i in range(1, 10+1):
    for j in range(1, 10+1):
        print(f"{i} x {j} = {i*j}")

#8)
auxiliary5 = ""
pyramid=""
num4 = int(input("ingrese un numero para hacer un triangulito: "))
for i in range(1,num4 + 1):
    auxiliary5=""
    if i % 2 != 0:
        auxiliary5 = str(i)
        pyramid = pyramid + " " + auxiliary5
        print(pyramid)

#9)
password = input("registre su contraseña: ")
conditional = True
while conditional:
    password2= input("ingrese la contraseña: ")
    if password == password2:
        conditional = False
        print("contraseña correcta")
    else: 
        print("contraseña incorrecta")

#10)
counter = 0
num5 = int(input("ingrese un numero: "))
for i in range(1, num5 +1):
    if num5 % i == 0:
        counter +=1
    if counter == 2:
        print("es primo")

#11)
text = input("ingrese una palabra: ")
quantity = len(text)
for i  in range(1, quantity+1):
    print(text[-i])

#12)
counter2 = 0
sentence = input("ingrese una frase: ")
letter = input("ingrese una letra: ")
for i in sentence:
    if i == letter:
        counter2 +=1
print(f"La letra: {letter} se repitio una cantidad de veces igual a {counter2} ")

#13
conditional2 = True
exitt = "salir"
auxiliary6 = ""
while conditional2:
    echo = input("ingrese una palabra o ingrese salir para terminar: ")
    auxiliary6 = echo.lower()
    if auxiliary6 != exitt:
        print(echo)
    else:
        conditional2 = False

#14
num6 = int(input("ingrese el primer numero: "))
num7 = int(input("ingrese el segundo numero: "))
auxiliary7=0
auxiliary8=0
odd =""
pairs=""
#this if is to make sure that it will always be the smaller number that will be placed in the range
if num6 > num7:
    auxiliary7 = num6
    auxiliary8 = num7
elif num7 > num6:
    auxiliary7 = num7
    auxiliary8 = num6
else:
    auxiliary7 = num6
    auxiliary8 = num7
for i in range(auxiliary8 +1,auxiliary7):
    auxiliary9 = str(i)
    if i % 2 == 0:
        pairs = pairs + " " + auxiliary9
    else:
        odd = odd + " " + auxiliary9
print(f"los pares que se encuentran entre {auxiliary8} y el {auxiliary7} son {pairs}")
print(f"los impares que se encuentran entre {auxiliary8} y el {auxiliary7} son {odd}")

#15
divisible = " "
num8 = int(input("ingrese un numero entero mayor que 0: "))
for i in range(1, num8+1):
    if num8 % i == 0: 
        divisible = divisible + " "+ str(i)
print(divisible)
#16
negative = 0
counter3 = int(input("ingrese la cantidad de numeros que va a ingresar: "))
for i in range(counter3):
    num9 = int(input("ingrese un numero: "))
    if num9 < 0:
        negative = negative +1
print(f"la cantidad de negativos ingresados fue de: {negative}")
#17
text2 = input("ingrese una frase: ")
vocals = "aeiou"
text_vocals= ""
for i in range(5):
    auxiliary10 = vocals[i]
    print(auxiliary10)
    auxiliary10 = text2.find(auxiliary10)
    if auxiliary10 >= 0:
        text_vocals = text_vocals + " " + text2[auxiliary10]
print(text_vocals)
#18
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
#19
savings = float(input("ingrese la meta a la que desea ahorrar: "))
conditional3 = True
total_saved = 0
while conditional3:
    money_deposited = float(input("ingrese la cantidad de dinero que desea ahorrar: "))
    if money_deposited > 0:
        total_saved += money_deposited
    else:
        print("solo numeros positivos")
    if total_saved >= savings:
        print("meta alcansada")
        conditional3 = False
#20
conditional4 = 1
counter4 = 0
while conditional4 != 0:
    conditional4 = int(input("ingrese un numero entero: "))
    if conditional4 != 0:
        counter4 += conditional4
print(f"la suma de los numeros ingresados es {counter4}")
#21
conditional5 = 1
numMayor = 0
while conditional5 != 0:
    conditional5 = int(input("ingrese un numero entero: "))
    if conditional5 != 0:
        if conditional5 > numMayor:
            numMayor = conditional5
print(f"el numero mayor ingresado es: {numMayor}")

#22
pair_numbers = 0
while True:
    numbers = int(input("Ingrese un número entero positivo (o -1 para terminar): "))
    if numbers == -1:
        break
    if numbers % 2 == 0:
        pair_numbers += 1
    digit_sum = 0
    num_temp = abs(numbers)  
    while num_temp > 0:
        digito = num_temp % 10
        digit_sum += digito
        num_temp //= 10
    print(f"La suma de los dígitos de {numbers} es {digit_sum}")
print(f"Se ingresaron {pair_numbers} números pares.")
#23
conditional6 = 1
while conditional6 > 0:
    conditional6 = int(input("ingrese el valor del producto: "))
    if conditional6 == 0:
        break
print("fin de la ejecucion")
#24
conditional7 = 1
total=0
while conditional7 > 0:
    conditional7 = int(input("ingrese el valor del producto: "))
    if conditional7 > 0:
        total += conditional7
    elif conditional7 < 0:
        print("error ingrese de nuevo el numero")
    elif conditional7 == 0:
        break
if total >= 1000:
    print(f"felicidades obtuvo un descuento e 10%. el total de la compra es: ${total-(total*0.10)}")
else:
    print(f"la cantidad a pagar es de: ${total}")
#25
num10 = int(input("Ingrese un número entero positivo: "))
if num10 < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, num10 + 1):
        factorial *= i
    print(f"El factorial de {num10} es {factorial}")