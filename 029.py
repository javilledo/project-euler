
import numpy as np

a_min = 2
a_max = 100

b_min = 2
b_max = 100

res = []

for a in range(a_min, a_max + 1):
    for b in range (b_min, b_max + 1):
        res.append(a**b)

res = len(np.unique(res))
print('PROBLEM 29: %d' % (res))