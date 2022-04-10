import math


res = math.pow(2, 1000)

res = f"{res:.0f}"

res = sum([int(x) for x in res])

print('PROBLEM 16: %d' % (res))