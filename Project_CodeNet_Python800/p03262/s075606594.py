import math
from functools import reduce

def my_gcd(*N):
    return reduce(math.gcd, N)

N, X = map(int,input().split())
C = list(map(int,input().split()))

if X not in C:
	C.append(X)
C.sort()

D = []
for i in range(len(C)-1):
	D.append(C[i+1] - C[i])

print(my_gcd(*D))