def comb_once(n,k,MOD):
    ans = 1
    for i in range(k):
        ans*=n-i
        ans*=pow(i+1,-1,MOD)
        ans%=MOD
    return ans
  
MOD=10**9+7  
n,a,b = map(int,input().split())
print((pow(2,n,MOD)-1-comb_once(n,a,MOD)-comb_once(n,b,MOD))%MOD)