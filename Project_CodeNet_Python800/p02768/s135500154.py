from math import *
def modpow(a,n,m):
  res=1
  while n>0:
    if n&1:res=res*a%m
    a=a*a%m
    n//=2
  return res
n,a,b=map(int,input().split())
mod=10**9+7
ans=modpow(2,n,mod)-1
na=1
nb=1
for i in range(a):
  na*=(n-i)%mod
  na%=mod
fa=1
for i in range(1,a+1):
  fa*=i
  fa%=mod
na*=modpow(fa,mod-2,mod)
for i in range(b):
  nb*=(n-i)%mod
  nb%=mod
fb=1
for i in range(1,b+1):
  fb*=i
  fb%=mod
nb*=modpow(fb,mod-2,mod)
print((ans-nb-na)%mod)