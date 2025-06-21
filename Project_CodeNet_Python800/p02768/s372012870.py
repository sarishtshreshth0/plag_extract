from math import factorial
n,a,b=map(int,input().split())
mod=10**9+7

nCa=1
nCb=1

tmp=n
for i in range(a):
    nCa*=tmp
    tmp-=1
    nCa%=mod
nCa=nCa*pow(factorial(a),mod-2,mod)%mod
tmp=n
for i in range(b):
    nCb*=tmp
    tmp-=1
    nCb%=mod
nCb=nCb*pow(factorial(b),mod-2,mod)%mod

print(((pow(2,n,mod))-nCa-nCb-1)%mod)