def is_palindrome(number):
    array = [int(i) for i in str(number)]
    array_reverse = res = array[::-1]
    if(array == array_reverse):
        return True

solutions = []

for i in range(100, 1000):
    for j in range(100, 1000):
        temp = i * j
        if(is_palindrome(temp)):
                solutions.append(temp)

print('PROBLEM 4: %d' % (max(solutions)))