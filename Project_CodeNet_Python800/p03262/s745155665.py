import math
from functools import reduce

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
x = list(map(lambda n: n - x[0], x))
print(reduce(math.gcd, x[1:]))