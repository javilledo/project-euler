
digits = 0
index = 1
current = 1
previous = 1
next = 1

while digits < 1000:
    next = current + previous
    previous = current
    current = next
    index += 1
    digits = len(str(current))

res = index + 1

print('PROBLEM 25: %d' % (res))