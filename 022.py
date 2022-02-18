
# OPEN DATA
with open('p022_names.txt') as f:
    RAW_DATA = [str.replace('"', '') for str in f.readlines()[0].split(',')]

# ORDER DATA ALPHABETICALLY
data = sorted(RAW_DATA) # index 0 ... 5162

# CREATE DICT FOR VALUES
import string
d = dict.fromkeys(string.ascii_lowercase, 0)
count = 1
for key in d.keys(): 
    d[key] = count
    count += 1

# ORDER OF ELEMENTS
order = [i for i in range(1, len(data) + 1)] # 1 ... 5163

# SUM OF VALUE OF CHARACTERS FOR EACH WORD
sum_of_words = []
for w in data:
    sum = 0
    for c in w:
        sum += d[c.lower()]
    sum_of_words.append(sum) # index 0 ... 5162

res = []
index = 0
for sum_num in sum_of_words:
    res.append(sum_num * order[index])
    index += 1

total = 0
for r in res:
    total += r

print('PROBLEM 22: %d' % (total))