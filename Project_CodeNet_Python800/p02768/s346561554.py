mod = 10**9+7
n,a,b = map(int,input().split())
base = pow(2,n,mod)-1
def comb(n,k):
  comb = 1
  for i in range(n-k+1,n+1):
    comb *= i
    comb %= mod
  for i in range(1, k+1):
    comb *= pow(i,mod-2,mod)
    comb %= mod
  return comb
print((base-comb(n,a)-comb(n,b))%mod)