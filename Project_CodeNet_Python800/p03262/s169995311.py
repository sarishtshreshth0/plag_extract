n, x = map(int, input().split())
X = tuple(map(lambda k:abs(int(k)-x), input().split()))
from math import gcd
from functools import reduce
ans = reduce(gcd, X)
print(ans)