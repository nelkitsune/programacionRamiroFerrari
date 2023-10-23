def count_digit_recursivo(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digit_recursivo(n // 10)


def potencia(n, b):
    if n == 1:
        return True
    if n < b or n % b != 0:
        return False
    return potencia(n // b, b)

def conception(a, b, pos=0):
    conceptions = []
    pos = a.find(b, pos)
    if pos != -1:
        conceptions.append(pos)
        conceptions.extend(conception(a, b, pos + 1))
    return conceptions

def Odd(n):
    if n == 0:
        return True  
    else:
        return Couple(n - 1)
def Couple(n):
    if n == 0:
        return False
    else:
        return Odd(n - 1)


def find_largest(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    largest_left = find_largest(left_half)
    largest_right = find_largest(right_half)
    if largest_left is None:
        return largest_right
    if largest_right is None:
        return largest_left
    return max(largest_left, largest_right)

def replicate(list, n):
    if not list:
        return []
    if n <= 0:
        return []
    else:
        return [list[0]] * n + replicate(list[1:], n)

