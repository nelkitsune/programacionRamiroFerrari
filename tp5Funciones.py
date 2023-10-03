def tamanioDni (num_dni):
    tamanioD = len(num_dni)
    if tamanioD >= 7 and tamanioD <=8:
        return  True
    else:
        return False

def size_string (wordd):
    wordd = wordd.strip();wordd = wordd.strip(" ");wordd = wordd.strip(".")
    worddlist=wordd.split()
    wordd_long = worddlist[-1]
    return len(wordd_long)
