from math import *
N,X=map(int,input().split())
x=sorted([X]+list(map(int,input().split())))
d=[abs(x[i+1]-x[i]) for i in range(N)]
ans=0
for i in range(N):
    ans=gcd(ans,d[i])
print(ans)