def long_of_chain(n, dict):
    temp = n
    count = 0
    while temp > 1:
        if temp not in dict.keys():
            count += 1
            if(temp % 2 == 0):
                temp = temp / 2
            else:
                temp = 3 * temp + 1
        else:
            return count + dict[temp] + 1
    return count + 1

dict = {}
for i in range(1000001):
    dict[i] = long_of_chain(i, dict)

res = max(dict, key = dict.get)

print('PROBLEM 14: %d' % (res))