# Consider a three dimensional grid of cubes (x, y, z). 
# An amoeba in cube  can divide itself into three amoebas to occupy the cubes (x + 1, y, z),
# (x, y + 1, z) and (x, y, z + 1), provided these cubes are empty.

# Originally there is only one amoeba in the cube (0, 0, 0). After N divisions there will be
# 2N + 1 amoebas arranged in the grid. An arrangement may be reached in several different ways 
# but it is only counted once. Let D(N) be the number of different possible arrangements after  divisions.

# For example, D(2) = 3, D(10) = 44499, D(20) = 9204559704 and the last nine digits of D(100) are 780166455.

# Find D(10000), enter the last nine digits as your answer.

import numpy as np

def D(N):
    INIT = [[0, 0, 0]]
    for i in range (1, N):
        temp = INIT[:]
        for j in temp:
            INIT.remove(j)
            x = j[0]
            y = j[1]
            z = j[2]
            INIT.append([x + 1, y, z])
            INIT.append([x, y + 1, z])
            INIT.append([x, y, z + 1])
    return INIT

N = 10
res = np.array(D(N))
res = np.unique(res, axis = 0)
res = res.shape[0]
print('PROBLEM 763: %d' % (res))
