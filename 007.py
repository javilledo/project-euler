def is_prime(number):
    for i in range(2, number):
        res = True
        if(number%i == 0):
            res = False
            break
    return res

print('%d: %d' % (1, 2))

index = 2
number = 3

while index <= 10001:
    if(is_prime(number)):
        print('%d: %d' % (index, number))
        index = index + 1
    number = number + 1

print('PROBLEM 7: %d' % (number - 1))