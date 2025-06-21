f=lambda:map(int,input().split())
n,x=f()
d=[abs(i-x) for i in f()]
from math import *
a=d.pop()
for i in d: a=gcd(a,i)
print(a)