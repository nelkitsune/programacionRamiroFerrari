import random
def rat(option, time):
    if option == 3:
        return 7
    elif option == 2:
        time = time + rat(random.randint(1,3),time)
        return 3
    elif option == 1 : 
        time = time + rat(random.randint(1,3),time)
        return 5
