from math import gcd
n,x = map(int,input().split())
l = list(map(int,input().split()))
for i in range(n):
    l[i] = abs(l[i] - x)
d = l[0]
for i in range(1,n):
    d = gcd(d,l[i])
print(d)