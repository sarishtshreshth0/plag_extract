n,a,b = map(int,input().split())
# (2**n-1)-nCa-nCb
mod = 10**9+7
M = pow(2,n,mod)-1

def comb(v):
    ans = 1
    for i in range(1,v+1): 
        ans *= n-i+1
        ans *= pow(i,mod-2,mod)
        ans %= mod
    return ans

print((M-comb(a)-comb(b))%mod)