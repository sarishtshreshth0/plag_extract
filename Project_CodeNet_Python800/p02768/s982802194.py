n,a,b=map(int,input().split())
mod=10**9+7
def comb(n,k,mod):
  if k>n-k:
    k=n-k
  c=1
  for i in range(n-k+1,n+1):
    c*=i
    c%=mod
  d=1  
  for i in range(1,k+1):
    d*=i
    d%=mod
  return (c*pow(d,mod-2,mod))%mod

ans=pow(2,n,mod)-1-comb(n,a,mod)-comb(n,b,mod)
print(ans%mod)
