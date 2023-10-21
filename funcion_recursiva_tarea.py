import random
def rat():
    time = 0
    while True:
        elec = random.randint(1, 3)  # Elegir un camino al azar
        if elec == 1:
            time += 3
        elif elec == 2:
            time += 5
        else:  # eleccion == 3
            time += 7
            break  # La rata ha salido de la jaula
    return time
