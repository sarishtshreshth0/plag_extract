from functools import reduce
def gcd(a,b):
    if b>0:
        return gcd(b,a%b)
    else:
        return a

N,X=map(int,input().split())
x=[int(i)for i in input().split()]
dist=[abs(X-i)for i in x]
d=reduce(gcd,dist)
print(d)