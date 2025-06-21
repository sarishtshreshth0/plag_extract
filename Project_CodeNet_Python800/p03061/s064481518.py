from math import*
n,*a=map(int,open(0).read().split())
b=[0]
for i in a:b+=gcd(b[-1],i),
w=m=0
for i in range(n):m=max(m,gcd(w,b[-i-2]));w=gcd(w,a[~i])
print(m)