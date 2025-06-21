import math
from functools import reduce
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x = [y - X for y in x]
print(reduce(math.gcd, x))
