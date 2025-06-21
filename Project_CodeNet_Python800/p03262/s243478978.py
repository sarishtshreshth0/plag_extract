from math import gcd
from functools import reduce

_, X = map(int, input().split())
x = set(map(int, input().split()))
x.add(X)
x = sorted(x)
print(reduce(gcd, (j - i for i, j in zip(x[:-1], x[1:]))))