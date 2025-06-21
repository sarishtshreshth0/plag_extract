from math import factorial
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,a,b = nm()
mod = 10**9+7

MAX = 10**6


def modpow(a,n,mod):
  res = 1
  while n>0:
    if n&1:
      res = res * a % mod
    a = a * a % mod
    n>>=1
  return res
    

ans = modpow(2,n,mod) - 1

def modcom(n,a,mod):
  X=1
  Y=1
  for i in range(a):
    X*=(n-i)
    X%=mod
  for i in range(a):
    Y*=(a-i)
    Y%=mod
  return X * modpow(Y,mod-2,mod)%mod


ans -= modcom(n,a,mod)
ans -= modcom(n,b,mod)

print(ans % mod)