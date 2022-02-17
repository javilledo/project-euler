def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def sum_of_digits(n):
    return sum([int(el) for el in str(n)])

res = sum_of_digits(factorial(100))

print('PROBLEM 20: %d' % (res))