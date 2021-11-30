# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

max_number = 2000000
INPUT = [i for i in range(2, max_number + 1)]
prime_numbers_array = INPUT[:]
prime_numbers_adding = []

def is_prime(number):
    is_prime = True
    for i in range(2, number):
        if(number % i == 0):
            is_prime = False
            return is_prime
    return is_prime

for i in INPUT:
    if(is_prime(i)):
        prime_numbers_adding.append(i)
        prime_numbers_array.remove(i)
        for j in prime_numbers_array:
            if(j % i == 0):
                prime_numbers_array.remove(j)
                if(j % 1000 == 0):
                    print(j)

res = sum(prime_numbers_adding)
print('PROBLEM 10: %d' % (res))