from functools import reduce
from math import gcd

N,X = map(int,input().split())
a = list(map(int,input().split()))
print(reduce(gcd,(abs(a[i] - X) for i in range(N))))
