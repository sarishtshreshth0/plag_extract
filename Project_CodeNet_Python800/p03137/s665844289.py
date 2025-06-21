import numpy as np
#from numba import njit

#(N, K) = map(int, input().split())
#A = np.array(list(map(int, input().split())))
(N,M) = map(int, input().split())
X = map(int, input().split())
X = sorted(X)

Y = []
for i in range(1,M):
    Y.append((i,X[i] - X[i-1]))

Y = sorted(Y, key=lambda x: (x[1]))
Y.reverse()

I = list(map(lambda x: x[0], Y[0:min(N-1, len(Y))]))
I.sort()

Z = []
last = 0
for i in range(0,min(N-1, len(Y))):
    if last < I[i]:
        Z.append(X[last:I[i]])
        last = I[i]
Z.append(X[last:])
if len(Z) == 0:
    Z.append(X)

s = 0
for array in Z:
    if len(array) > 0:
        u = max(array)
        l = min(array)
        s += u - l

print(s)