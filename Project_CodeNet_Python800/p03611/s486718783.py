import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
x = np.hstack([a - 1, a, a + 1])
x[x < 0] = 0
r = np.bincount(x)
print(r[1:].max())