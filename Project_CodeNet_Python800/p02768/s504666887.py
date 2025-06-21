import math


n,a,b=map(int,input().split())
mod=10**9+7

c1=1
c2=1

for i in range(n-a+1,n+1):
    c1*=i
    c1%=mod
for j in range(1,a+1):
    c1*=pow(j,mod-2,mod)
    c1%=mod
    
for i in range(n-b+1,n+1):
    c2*=i
    c2%=mod
for j in range(1,b+1):
    c2*=pow(j,mod-2,mod)
    c2%=mod

ans=pow(2,n,mod)-1

print((ans-c1-c2)%mod)
