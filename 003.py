
def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

def next_high_divisor(num):
    for i in range (2, num - 1):
        if num % i == 0:
            yield int(num / i)

INPUT = 600851475143       

iterable_high_divisors = next_high_divisor(INPUT)

find_solution = False
while find_solution == False:
    temp_divisor = next(iterable_high_divisors)
    if is_prime(temp_divisor): 
        find_solution = True
        print('PROBLEM 3: %d' % (temp_divisor))