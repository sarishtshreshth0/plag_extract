
from math import gcd
from functools import reduce

N, X = map(int, input().split())
A = list(map(int, input().split()))

res = reduce(gcd, [abs(v - X) for v in A])
print(res)
