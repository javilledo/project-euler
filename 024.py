
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# PERMUTATIONS
import itertools
res = list(itertools.permutations(data))

# JOIN AS NUMBERS
res = [int(str(t).replace('[', '').replace(']', '').replace(', ', '')) for t in (list(el) for el in res)]

# ORDER ARRAY
res = sorted(res)

# GET ELEMENT ONE MILLIONTH
res = res[1000000 - 1]

print('PROBLEM 24: %d' % (res))
