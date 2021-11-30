# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

max_num = 2000000
prime_numbers = [2]
range_to_check = list(range(3, max_num + 1, 2))

notify = 1
for i in range_to_check:
    for j in prime_numbers[:]:
        prime = True
        if(i % j == 0):
            prime = False
            break
    if(prime):
        prime_numbers.append(i)
        notify += 1
        if(notify % 10000 == 0): print(i)

res = sum(prime_numbers)
print('PROBLEM 10: %d' % (res))