import math

def gen_triangle(max_level):
    i = 1
    res = 0
    while i < max_level + 1:
        res += i
        i += 1
        yield res

def get_divisors(n) :

    res = []
     
    i = 1

    while i <= math.sqrt(n):
         
        if (n % i == 0) :
             
            if (n / i == i) :
                res.append(i)
            else :
                res.append(i)
                res.append(int(n/i))
        i = i + 1
    res.sort()
    return res

triangle = gen_triangle(1000000)

res = 0

for i in triangle:
    if (len(get_divisors(i)) > 500):
        res = i
        break

print('PROBLEM 12: %d' % (res))
