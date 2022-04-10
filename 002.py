def fibo(index):
    if index == 0: return 1
    if index == 1: return 2
    return fibo(index - 1) + fibo (index - 2)

index = 0
sum = 0
while fibo(index) < 4000000:
    if fibo(index) % 2 == 0: sum += fibo(index)
    index += 1

print('PROBLEM 2: %d' % (sum))
