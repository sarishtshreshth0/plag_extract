n=int(input())
a=[*map(int,input().split())]
from math import *
l,r=[0]*n,[0]*n
for i in range(1,n):
  l[i]=gcd(l[i-1],a[i-1])
  r[~i]=gcd(r[-i],a[-i])
m=0
for i in range(n):
  m=max(m,gcd(l[i],r[i]))
print(m)