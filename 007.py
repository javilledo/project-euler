# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

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