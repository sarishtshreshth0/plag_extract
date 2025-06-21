from math import gcd
from functools import reduce

_, X = map(int, input().split())
print(reduce(gcd, (abs(i - X) for i in set(map(int, input().split())))))