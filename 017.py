from matplotlib.cbook import flatten
from num2words import num2words

res = 0

for i in range(1, 1001):
    temp = num2words(i).split('-')
    temp = [el.split(' ') for el in temp]
    flatten_list = []
    for x in temp:
        for y in x:
            flatten_list.append(y)
    res += sum([len(x) for x in flatten_list])

print('PROBLEM 17: %d' % (res))


