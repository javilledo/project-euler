
import itertools

from matplotlib.pyplot import get

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
    return [int(el) for el in list(str(334))]

def get_permutations(n):
    res = []
    temp = set(itertools.permutations(get_digits(n)))
    for el in temp:
        c = ''
        for d in el:
            c += str(d)
        res.append(int(c))
    return(res)








