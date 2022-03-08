def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res

def sum_of_factorials_of_digits(n):
    res = sum([factorial(int(el)) for el in list(str(n))])
    return res

res = []

for i in range(3, 1000000):
    if i == sum_of_factorials_of_digits(i): res.append(i)

res = sum(res)
print('PROBLEM 34: %d' % (res))