#/usr/bin/env python
from functools import *
from math import *

n = int(input())
a = list(map(int, input().split()))

gcds = []
lgcd = []
rgcd = [0 for _ in range(n)]
l = r = 0 
for i in range(n):
    if i == 0:
        l = 0 
    else:
        l = gcd(l, a[i-1])
    lgcd.append(l)

for i in range(n):
    if i == 0:
        r = 0 
        rgcd[n-1] = r 
    else:
        r = gcd(r, a[n-i])
        rgcd[n-i-1] = r 

for i in range(n):
    g = gcd(lgcd[i], rgcd[i])
    gcds.append(g)

print(max(gcds))
