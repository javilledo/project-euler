import time

def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def num_of_primes(list: list) -> int:
    bool_list = [is_prime(num) for num in list]
    return sum(bool_list)

def next_prime(min: int, max: int) -> iter:
    num = min
    while num < max:
        if(is_prime(num)): 
            yield num
        num += 1    

prime_iterator = next_prime(2, 100)

# def all_permutations(num: int):

# check execution duration
start_time = time.time()

# execution


# check execution duration
final_time = time.time()
print("--- %s seconds ---" % (final_time - start_time))


# print('PROBLEM 51: %d' % (res))