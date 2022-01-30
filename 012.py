
def len_get_divisors(number):
    res = [1]
    for i in range(2, number + 1):
        if(number % i == 0): res.append(i)
    return len(res)

sum = 1
for i in range(2, 1000000000):
    sum += i
    print('i:', i, 'sum:', sum)
    if(sum > 100000000000):
        len_divisors = len_get_divisors(sum)
        print('i:', i, 'sum:', sum, 'divisors:', len_divisors)
        if(len_divisors > 500): 
            break



# print('PROBLEM 12: %d' % (res))