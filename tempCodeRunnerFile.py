frase = input("Ingrese una frase: ")

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for letra in frase:
    letra = letra.lower()
    if letra == 'a':
        a_count += 1
    elif letra == 'e':
        e_count += 1
    elif letra == 'i':
        i_count += 1
    elif letra == 'o':
        o_count += 1
    elif letra == 'u':
        u_count += 1

print(f"Cantidad de 'a': {a_count}")
print(f"Cantidad de 'e': {e_count}")
print(f"Cantidad de 'i': {i_count}")
print(f"Cantidad de 'o': {o_count}")
print(f"Cantidad de 'u': {u_count}")