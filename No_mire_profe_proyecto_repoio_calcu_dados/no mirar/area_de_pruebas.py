adn = [
    "ATGCAG",
    "CAGTAG",
    "TTATTG",
    "AGAAAG",
    "CCCCTA",
    "TCACTG"]

for i in range(6):
    for j in range(3):
        if adn[i][j] == adn[i][j+1] and adn[i][j+1] == adn[i][j+2] and adn[i][j+2] == adn[i][j+3]:
            print("papa")
            print(i,j)
#forma efectiva de transponer una matriz
adn = list(zip(*adn))
#forma efectiva de transponer una matriz

for i in range(6):
    for j in range(3):
        if adn[i][j] == adn[i][j+1] and adn[i][j+1] == adn[i][j+2] and adn[i][j+2] == adn[i][j+3]:
            print("papa")
            print(i,j)



#for j in range(6):
 #   for i in range(3):
 #       if adn[i][j] == adn[i+1][j] and adn[i+1][j] == adn[i+2][j] and adn[i+2][j] == adn[i+3][j]:
 #           print("papa")

def transponer_matriz(matriz):
    # Usamos zip() para transponer la matriz y luego convertimos cada fila transpuesta en una lista
    matriz_transpuesta = [list(columna) for columna in zip(*matriz)]
    return matriz_transpuesta

adn = [
    "ATGCAG",
    "CAGTTG",
    "TTATAG",
    "AGAAAG",
    "CCCCTA",
    "TCACTG"]

matriz_transpuesta = transponer_matriz(adn)

print(matriz_transpuesta)

for i in range(6):
    for j in range(3):
        if matriz_transpuesta[i][j] == matriz_transpuesta[i][j+1] and matriz_transpuesta[i][j+1] == matriz_transpuesta[i][j+2] and matriz_transpuesta[i][j+2] == matriz_transpuesta[i][j+3]:
            print("papa")
            print(i,j)

papas = [
    "ATGCAG",
    "CAGTTG",
    "TTATAG",
    "AGAAAG",
    "CCCCTA",
    "TCACTG"]
print (papas)
papa=list(zip(*papas))
print(papa)

adn = [
    "ATGCAG",
    "CAGTAG",
    "TTATTG",
    "AGAAAG",
    "CCCCTA",
    "TCACTG"]

for i in range(3):
    for j in range(3):
        if adn[i][j] == adn[i+1][j+1] and adn[i+1][j+1] == adn[i+2][j+2] and adn[i+2][j+2] == adn[i+3][j+3]:
            print("papa")
            print(i,j)

adn = [
    "ATGCAG",
    "CAGTGG",
    "TTAGTG",
    "AGGAAG",
    "CCCCTA",
    "TCACTG"]

for i in range(3):
    for j in range(3):
        print(i," ",j)
        if adn[i][j] == adn[i-1][j-1] and adn[i-1][j-1] == adn[i-2][j-2] and adn[i-2][j-2] == adn[i-3][j-3]:
            print("papa")
            print(i,j)