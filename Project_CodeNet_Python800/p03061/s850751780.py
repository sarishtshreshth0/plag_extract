n=int(input())
a=[*map(int,input().split())]
from math import *
l=a.copy()
r=a.copy()
for i in range(n-1):
  l[i+1]=gcd(l[i],l[i+1])
  r[-i-2]=gcd(r[-i-1],r[-i-2])
a=max(l[-2],r[1])
for i in range(1,n-1):
  a=max(a,gcd(l[i-1],r[i+1]))
print(a)