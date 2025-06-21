from math import gcd

N,X=map(int,input().split())
L=list(map(lambda x:int(x)-X,input().split()))

a=L[0]
for b in L:
    a=gcd(a,b)
print(a)
