# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def is_exact_sqrt(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c2 = a**2 + b**2
        if(is_exact_sqrt(c2)):
            c = math.sqrt(c2)
            print('a: %d, b: %d, c: %d' % (a, b, c))
            if(a + b + c == 1000): 
                print('a + b + c = %d' % (a + b + c))
                solution = a * b * c

print('PROBLEM 9: %d' % (solution))