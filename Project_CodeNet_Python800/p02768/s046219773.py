from functools import reduce

n,a,b=map(int,input().split())

mod=10**9+7
def nCk(n,k):
  c=reduce(lambda x,y: x*y%mod, range(n,n-k,-1))
  m=reduce(lambda x,y: x*y%mod, range(1,k+1))
  return c*pow(m,mod-2,mod)%mod

all=pow(2,n,mod)
nCa=nCk(n,a)
nCb=nCk(n,b)

print((all-nCa-nCb-1)%mod)