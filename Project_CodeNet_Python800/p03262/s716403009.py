from math import gcd
from functools import reduce
n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
for i in range(n):
  a[i]=abs(a[i]-x)

d=reduce(gcd,a)
print(d)