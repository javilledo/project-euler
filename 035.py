
import itertools

def is_prime(n):
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def get_digits(n):
    return [int(el) for el in list(str(n))]

def get_permutations(n):
    res = []
    temp = set(itertools.permutations(get_digits(n)))
    for el in temp:
        c = ''
        for d in el:
            c += str(d)
        res.append(int(c))
    return(res)

def circular_rotation(n):
    """
    Devuelve todas las rotaciones circulares de un número.
    Por ejemplo: 197 -> [197, 971, 719]
    """
    res = []
    s = str(n)
    length = len(s)
    
    for i in range(length):
        # Rotar: tomar desde posición i hasta el final + desde inicio hasta posición i
        rotated = s[i:] + s[:i]
        res.append(int(rotated))
    
    return res


res = 0

# Recorrer números del 1 al 1000000
for num in range(1, 1000001):
    # Obtener todas las rotaciones circulares
    rotations = circular_rotation(num)
    
    # Verificar si todas las rotaciones son primas
    all_prime = True
    for rotation in rotations:
        if not is_prime(rotation):
            all_prime = False
            break
    
    # Si todas las rotaciones son primas, incrementar res
    if all_prime:
        res += 1
        print(f"{num}: {rotations} - Todas son primas")

print('PROBLEM 35: %d' % (res))