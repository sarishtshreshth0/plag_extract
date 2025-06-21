f=lambda:[*map(int,input().split())]
n,x=f()
d=[abs(i-x) for i in f()]
a=d.pop()
from math import *
for i in d:
  a=gcd(a,i)
print(a)