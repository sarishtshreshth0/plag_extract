import functools
from fractions import gcd
n,x =map(int,input().split())
if n==1:
    c = abs(int(input())-x)
    print(c)
else:
    lis = list(map(int,input().split()))
    for i in range(n):
        lis[i] = abs(lis[i]-x)
    print(functools.reduce(gcd,lis))