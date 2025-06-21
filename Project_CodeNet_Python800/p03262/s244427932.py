import math
from functools import reduce
N, A = map(int, input().split())
X = list(map(int, input().split()))
L = ([abs(x-A) for x in X])
print(reduce(math.gcd, L))