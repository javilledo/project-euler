def is_palindrome(n):
    arr = list(str(n)) 
    if(arr == arr[::-1]): 
        return True
    else: 
        return False

def decimal_to_binary(n): 
    return format(n, "b")
  
res = []
limit = 1000001

for i in range(1, limit):
    if(is_palindrome(i) and is_palindrome(decimal_to_binary(i))): res.append(i)

res = sum(res)

print('PROBLEM 36: %d' % (res))