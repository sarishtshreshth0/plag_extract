import math
from functools import reduce
N, X = map(int, input().split())
x = list(map(int, input().split()))
x = [y - X for y in x]
if len(x)==1:
    for y in x:
        print(abs(y))
else:
    print(reduce(math.gcd, x))
