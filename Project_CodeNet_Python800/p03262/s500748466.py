from functools import reduce
from math import gcd
n,x = map(int,input().split())
a = list(map(int,input().split()))
b = []
for ai in a:
    b.append(abs(ai-x))
print(reduce(gcd,b))