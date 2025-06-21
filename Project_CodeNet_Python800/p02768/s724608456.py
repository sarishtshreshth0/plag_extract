def MI(): return map(int, input().split())
MOD=10**9+7
def nCr(n,k):
  tmp=1
  for i in range(n-k+1,n+1):
    tmp*=i
    tmp%=MOD
  for i in range(1,k+1):
    tmp*=pow(i,MOD-2,MOD)
    tmp%=MOD
  return tmp
N,A,B=MI()
ans=pow(2,N,MOD)-1-nCr(N,A)-nCr(N,B)
print(ans%MOD)