import funcion_recursiva_tarea
import random
val = random.randint(1,3)
if val == 1:
    time = 3
    print(f"se tardo un total de {funcion_recursiva_tarea.rat(random.randint(1,3),time)} minutos")
elif val == 2:
    time = 5
    print(f"se tardo un total de {funcion_recursiva_tarea.rat(random.randint(1,3),time)} minutos")
elif val == 3:
    time = 7
    print("tardo 7 minutos")
