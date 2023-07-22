
res = 0

for i in range (1, 1001):
    res += i ** i

res = str(res)[-10:]

print('PROBLEM 48: %s' % (res))