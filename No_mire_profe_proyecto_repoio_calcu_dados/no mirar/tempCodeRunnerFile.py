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