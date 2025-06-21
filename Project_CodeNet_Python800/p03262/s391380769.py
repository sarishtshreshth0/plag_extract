f=lambda:[*map(int,input().split())]
n,x=f()
l=f()
d=[x-l[0]]
for i in range(n-1):
  d+=[l[i+1]-l[i]]
a=d[0]
from math import *
for i in d:
  a=gcd(a,i)
print(a)