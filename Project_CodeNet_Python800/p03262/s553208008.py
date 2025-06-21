import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)

N, X = map(int, input().split())
x = list(map(int, input().split()))

dist = [0] * N
for i in range(N):
    dist[i] = abs(x[i] - X)

# distの最大公約数が欲しい
g = gcd(*dist)
print(g)
