
n_max = 1001 * 1001
res = [1]

salto = 0
n = 1

while n <= n_max:
    salto = salto + 2
    cicle = 1
    while cicle <= 4:
        n = n + salto
        if(n > n_max): break
        res.append(n)
        cicle += 1

res = sum(res)
print('PROBLEM 28: %d' % (res))