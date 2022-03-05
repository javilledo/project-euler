
power = 5

res = []

for i in range(2, 1000000):
    temp = sum([int(el)**power for el in list(str(i))])
    if i ==  temp: res.append(i)

res = sum(res)
print('PROBLEM 30: %d' % (res))