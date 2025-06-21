import math
from functools import reduce

n, k = map(int, input().split())
x = list(map(int, input().split()))
y = []

for i,X in enumerate(x):
    val = abs(X - k)
    y.append(val)

print(reduce(math.gcd, y))