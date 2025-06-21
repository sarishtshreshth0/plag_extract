def comb(n,k):
    nCk = 1
    MOD = 10**9+7

    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk
n,a,b=map(int,input().split())
mod=10**9+7
ans=(2**n-1)%mod
aa=comb(n,a)%mod
bb=comb(n,b)%mod
ans-=aa+bb
print(ans%mod)