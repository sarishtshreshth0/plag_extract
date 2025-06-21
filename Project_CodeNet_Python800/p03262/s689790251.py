from functools import reduce
from math import gcd
n,x = map(int,input().split())
a = list(map(int,input().split()))
print(reduce(gcd,(abs(ai-x) for ai in a)))